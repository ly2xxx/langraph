import streamlit as st
import pandas as pd

def display_csv(uploaded_files):
    for file in uploaded_files:
        try:
            df = pd.read_csv(file)
            st.write(f"Contents of {file.name}:")

            # Create a dropdown for column selection
            columns = list(df.columns)
            selected_column = st.selectbox(f"Select a column for {file.name}", columns)

            # Create a search box for filtering
            search_value = st.text_input(f"Search for {file.name}", key=f"search_{file.name}")

            # Filter the DataFrame based on the search value
            if search_value:
                filtered_df = df[df[selected_column].astype(str).str.contains(search_value, case=False)]
            else:
                filtered_df = df

            st.write(filtered_df)

            # Add a button to export the search results
            if st.button(f"Export search results for {file.name}"):
                csv = filtered_df.to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name=f"{file.name}_search_results.csv",
                    mime="text/csv",
                )

            # Add a button to copy the search results to clipboard
            if st.button(f"Copy search results for {file.name}"):
                csv = filtered_df.to_csv(index=False)
                st.code(csv, language="csv")
                st.write("Search results copied to clipboard.")

        except Exception as e:
            st.error(f"Error reading {file.name}: {e}")

st.title("CSV File Viewer")

uploaded_files = st.file_uploader("Choose CSV files", accept_multiple_files=True)

if uploaded_files:
    display_csv(uploaded_files)
else:
    st.warning("No files uploaded yet.")