import streamlit as st
from langgraph_agent_example import construct_agent, create_graph_workflow
from langgraph_researcher_example import create_researcher_graph_workflow, enter_chain
from io import BytesIO

# We import the necessary functions from langgraph_agent_example.py: construct_agent and create_graph_workflow.
# In the main function, we create a Streamlit app with a title "AWS Well-Architected Framework Assistant".
# We create the agent and the LangGraph workflow using the construct_agent and create_graph_workflow functions, respectively.
# We use st.text_area to create a text input area where the user can enter their query about the AWS Well-Architected Framework.
# When the user clicks the "Submit" button (st.button("Submit")), we invoke the LangGraph workflow with the user's input using chain.invoke({"input": user_input, "intermediate_steps": []}).
# We extract the output from the agent's response (output = result['agent_outcome'].return_values["output"]).
# Finally, we display the output using st.write(output).
def main():
    st.title("Multi-agent Assistant Demo")

    # Create Agent
    agent_runnable = construct_agent()

    # Create LangGraph Workflow with Agent as Entrypoint
    chain_agent = create_graph_workflow(agent_runnable)
    chain_researcher = create_researcher_graph_workflow()

    # Dropdown to select chain
    chain_selection = st.selectbox("Select chain", ["chain_agent", "chain_researcher"])

    # Display the graph visualization
    # graph = chain.get_graph(xray=True)
    # mermaid_png = graph.draw_mermaid_png()
    # png_bytes = BytesIO(mermaid_png)
    # st.image(png_bytes, caption="Summarizer", use_column_width=True)
    if chain_selection == "chain_agent":
        displayGraph(chain_agent, chain_selection)
    elif chain_selection == "chain_researcher":
        displayGraph(chain_researcher, chain_selection)

    # Get user input
    user_input = st.text_area("Enter your query:")

    # File picker
    # uploaded_file = st.file_uploader("Choose a file", type=["pdf", "txt", "docx"])
    uploaded_files = []
    num_files = st.number_input("Pick your file(s) - Number of files to upload", min_value=1, value=1, step=1)
    for i in range(num_files):
        file = st.file_uploader(f"Choose file {i+1}", type=["pdf", "txt", "docx"], key=f"file_{i}")
        if file:
            uploaded_files.append(file)

    if st.button("Submit"):
        if chain_selection == "chain_agent":
            # Invoke the LangGraph Workflow with user input and intermediate steps
            result = chain_agent.invoke({"input": user_input, "intermediate_steps": []})

            # Print the output of the LangGraph Workflow - this is the output of the Agent
            output = result['agent_outcome'].return_values["output"]
            st.write(output)
        elif chain_selection == "chain_researcher":
            research_chain = enter_chain | chain_researcher
            for s in research_chain.stream(
                user_input, {"recursion_limit": 100}
            ):
                if "__end__" not in s:
                    st.write(s)
                    st.write("---")
        else:
            st.write("Under development")

def displayGraph(chain, chain_selection):
    # Display the graph visualization
    graph = chain.get_graph(xray=True)
    mermaid_png = graph.draw_mermaid_png()
    png_bytes = BytesIO(mermaid_png)
    st.image(png_bytes, caption=chain_selection, use_column_width=True)

if __name__ == "__main__":
    main()
    