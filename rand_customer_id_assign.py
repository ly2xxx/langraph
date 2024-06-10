import pandas as pd
import random
import argparse

def overwrite_customer_ids(csv1_path, csv2_path, output_path):
    # Read the CSV files
    csv1 = pd.read_csv(csv1_path)
    csv2 = pd.read_csv(csv2_path)

    # Get a list of unique customer IDs from csv1
    unique_customer_ids = csv1['customer_id'].unique().tolist()

    # Shuffle the list of unique customer IDs
    random.shuffle(unique_customer_ids)

    # Overwrite customer IDs in csv2 with random unique IDs from csv1
    csv2['customer_id'] = [unique_customer_ids.pop(0) for _ in range(len(csv2))]

    # Save the updated csv2 to the output file
    csv2.to_csv(output_path, index=False)
    print(f"Customer IDs overwritten and saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Overwrite customer IDs in a CSV file")
    parser.add_argument("csv1_path", help="Path to the first CSV file (source of unique customer IDs)")
    parser.add_argument("csv2_path", help="Path to the second CSV file (target for overwriting customer IDs)")
    parser.add_argument("output_path", help="Path to the output file for the updated CSV")
    args = parser.parse_args()

    overwrite_customer_ids(args.csv1_path, args.csv2_path, args.output_path)
