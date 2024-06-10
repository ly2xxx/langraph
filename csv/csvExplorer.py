import streamlit as st
import pandas as pd

# Read Excel files into Pandas dataframes
df1 = pd.read_excel("customer.csv")
df2 = pd.read_excel("product.csv")
df3 = pd.read_excel("order.csv")

# Define the key field for searching
key_field = "id"  # Replace with the actual column name

# Combine the dataframes into a single dataframe
combined_df = pd.concat([df1, df2, df3], ignore_index=True)

# Streamlit app
st.title("Excel Spreadsheet Explorer")

# Search input
search_term = st.text_input("Enter search term:", "")

# Filter the combined dataframe based on the search term
if search_term:
    filtered_df = combined_df[combined_df[key_field].astype(str).str.contains(search_term, case=False)]
else:
    filtered_df = combined_df

# Display the filtered dataframe
st.write(filtered_df)

# Display the individual dataframes
st.header("Individual Dataframes")
st.subheader("File 1")
st.write(df1)

st.subheader("File 2")
st.write(df2)

st.subheader("File 3")
st.write(df3)
