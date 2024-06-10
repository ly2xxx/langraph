import pandas as pd
import argparse

def get_customer_data(csv_path, customer_id):
    # Read the CSV file
    df = pd.read_csv(csv_path)

    # Filter the DataFrame based on the customer_id
    customer_data = df[df['Customer id'] == customer_id]

    if customer_data.empty:
        print(f"No data found for customer ID: {customer_id}")
    else:
        print(f"Data for customer ID: {customer_id}")
        print(customer_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get customer data from a CSV file")
    parser.add_argument("csv_path", help="Path to the CSV file")
    parser.add_argument("customer_id", help="Customer ID to search for")
    args = parser.parse_args()

    get_customer_data(args.csv_path, args.customer_id)