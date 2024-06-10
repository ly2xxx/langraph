import os
import csv
import argparse

def split_csv(input_file, output_dir, chunk_size=100 * 1024 * 1024):  # 100 MB
    """
    Split a CSV file into multiple files of a specified size.

    Args:
        input_file (str): Path to the input CSV file.
        output_dir (str): Path to the output directory where the split files will be saved.
        chunk_size (int): Maximum size of each output file in bytes (default: 100 MB).
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Get the header row

        current_chunk = []
        current_chunk_size = 0
        chunk_count = 0

        for row in reader:
            row_size = sum(len(str(value)) for value in row)
            if current_chunk_size + row_size > chunk_size:
                # Save the current chunk to a file
                output_file = os.path.join(output_dir, f"chunk_{chunk_count}.csv")
                with open(output_file, 'w', newline='') as out_file:
                    writer = csv.writer(out_file)
                    writer.writerow(header)
                    writer.writerows(current_chunk)

                # Reset the current chunk
                current_chunk = []
                current_chunk_size = 0
                chunk_count += 1

            current_chunk.append(row)
            current_chunk_size += row_size

        # Save the remaining chunk (if any)
        if current_chunk:
            output_file = os.path.join(output_dir, f"chunk_{chunk_count}.csv")
            with open(output_file, 'w', newline='') as out_file:
                writer = csv.writer(out_file)
                writer.writerow(header)
                writer.writerows(current_chunk)

    print(f"CSV file split into {chunk_count + 1} chunks.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split a CSV file into multiple files of a specified size.")
    parser.add_argument("input_file", help="Path to the input CSV file.")
    parser.add_argument("output_dir", help="Path to the output directory where the split files will be saved.")
    parser.add_argument("--chunk_size", type=int, default=100 * 1024 * 1024, help="Maximum size of each output file in bytes (default: 100 MB).")

    args = parser.parse_args()

    split_csv(args.input_file, args.output_dir, args.chunk_size)