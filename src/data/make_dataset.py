# src/data/make_dataset.py

import os
import pandas as pd

def load_and_combine_data(data_dir):
    dataframes = []
    cycle_lengths = {}

    for i in range(1, 20):  # D01 to D19
        file_name = f"{data_dir}/D{i:02d}.txt"
        df = pd.read_csv(file_name, delimiter='\t', header=None, names=['Time', 'Speed', 'Acceleration'])
        df['Cycle'] = f'{i}'
        cycle_lengths[f'D{i:02d}'] = len(df)
        dataframes.append(df)

    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df, cycle_lengths

def save_processed_data(df, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'combined_data.csv')
    df.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")

def save_cycle_lengths(cycle_lengths, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'cycle_lengths.txt')
    with open(output_file, 'w') as f:
        for cycle, length in cycle_lengths.items():
            f.write(f'{cycle}: {length}\n')
    print(f"Cycle lengths saved to {output_file}")

def main():
    raw_data_dir = "data/raw"
    processed_data_dir = "data/processed"

    combined_df, cycle_lengths = load_and_combine_data(raw_data_dir)
    save_processed_data(combined_df, processed_data_dir)
    save_cycle_lengths(cycle_lengths, processed_data_dir)

if __name__ == "__main__":
    main()
