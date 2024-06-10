import streamlit as st
import pandas as pd
import os
import codecs

# Set page title
st.set_page_config(page_title="Customer Data")

# Get user input
customer_id = st.text_input("Enter Customer ID")

# Check if customer ID exists in customers_data folder
customer_data_folder = "customers_data"
customer_file = f"{customer_id}.csv"
customer_data_path = os.path.join(customer_data_folder, customer_file)

if os.path.exists(customer_data_path):
    # Read and display customer data
    customer_data = pd.read_csv(customer_data_path)
    st.subheader("Customer Data")
    st.dataframe(customer_data)
    
    # Allow user to download customer data
    csv_download = customer_data.to_csv().encode('utf-8')
    st.download_button(
        label="Download Customer Data",
        data=csv_download,
        file_name=f"{customer_id}.csv",
        mime="text/csv"
    )
    
    # Display customer profile
    customer_profile_folder = "customers_profile"
    customer_profile_file = f"{customer_id}.txt"
    customer_profile_path = os.path.join(customer_profile_folder, customer_profile_file)
    
    # if os.path.exists(customer_profile_path):
    #     with open(customer_profile_path, "r") as f:
    #         customer_profile = f.read()
    #     st.subheader("Customer Profile")
    #     st.write(customer_profile)
    if os.path.exists(customer_profile_path):
        with codecs.open(customer_profile_path, "r", encoding='utf-8') as f:
            customer_profile = f.read()
        st.subheader("Customer Profile")
        st.write(customer_profile)
        
        # Display recommendations button
        if st.button("Recommendations"):
            st.write("Here are some recommendations for this customer.")
    else:
        st.write(f"No profile found for customer {customer_id}.")
else:
    st.write(f"No data found for customer {customer_id}.")