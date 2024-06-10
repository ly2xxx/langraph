import os
import pandas as pd
import argparse

def merge_csv_files(folder_path, output_file):
    dfs = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path)
            dfs.append(df)

    # Merge all DataFrames based on the "customer_id" column
    merged_df = dfs[0]
    for df in dfs[1:]:
        merged_df = merged_df.merge(df, on="customer id", how="outer")

    merged_df.to_csv(output_file, index=False)
    print(f"CSV files merged and saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge CSV files from a folder")
    parser.add_argument("folder_path", help="Path to the folder containing CSV files")
    parser.add_argument("output_file", help="Path to the output file for the merged CSV")
    args = parser.parse_args()

    merge_csv_files(args.folder_path, args.output_file)