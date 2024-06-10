import pandas as pd
import argparse

def get_customer_data(csv_path, customer_id, output_path):
    # Read the CSV file
    df = pd.read_csv(csv_path)

    # Filter the DataFrame based on the customer_id
    customer_data = df[df['customer_id'] == customer_id]

    if customer_data.empty:
        print(f"No data found for customer ID: {customer_id}")
    else:
        print(f"Data for customer ID: {customer_id}")
        print(customer_data)

        # Export customer data to a CSV file
        customer_data.to_csv(output_path, index=False)
        print(f"Customer data exported to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get customer data from a CSV file")
    parser.add_argument("csv_path", help="Path to the CSV file")
    parser.add_argument("customer_id", help="Customer ID to search for")
    parser.add_argument("output_path", help="Path to the output CSV file for customer data")
    args = parser.parse_args()

    get_customer_data(args.csv_path, args.customer_id, args.output_path)