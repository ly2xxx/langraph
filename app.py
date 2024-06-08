import streamlit as st
from langgraph_agent_example import construct_agent, create_graph_workflow
from io import BytesIO

# We import the necessary functions from langgraph_agent_example.py: construct_agent and create_graph_workflow.
# In the main function, we create a Streamlit app with a title "AWS Well-Architected Framework Assistant".
# We create the agent and the LangGraph workflow using the construct_agent and create_graph_workflow functions, respectively.
# We use st.text_area to create a text input area where the user can enter their query about the AWS Well-Architected Framework.
# When the user clicks the "Submit" button (st.button("Submit")), we invoke the LangGraph workflow with the user's input using chain.invoke({"input": user_input, "intermediate_steps": []}).
# We extract the output from the agent's response (output = result['agent_outcome'].return_values["output"]).
# Finally, we display the output using st.write(output).
def main():
    st.title("AWS Well-Architected Framework Assistant")

    # Create Agent
    agent_runnable = construct_agent()

    # Create LangGraph Workflow with Agent as Entrypoint
    chain = create_graph_workflow(agent_runnable)

    # Display the graph visualization
    graph = chain.get_graph(xray=True)
    mermaid_png = graph.draw_mermaid_png()
    png_bytes = BytesIO(mermaid_png)
    st.image(png_bytes, caption="Graph Visualization", use_column_width=True)

    # Get user input
    user_input = st.text_area("Enter your query about the AWS Well-Architected Framework:")

    # File picker
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "txt", "docx"])

    if st.button("Submit"):
        # Invoke the LangGraph Workflow with user input and intermediate steps
        result = chain.invoke({"input": user_input, "intermediate_steps": []})

        # Print the output of the LangGraph Workflow - this is the output of the Agent
        output = result['agent_outcome'].return_values["output"]
        st.write(output)

    

if __name__ == "__main__":
    main()
    