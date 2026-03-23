import pandas as pd
import os

def load_data():
    folder = "data"
    all_files = [f for f in os.listdir(folder) if f.endswith('.csv')]

    print("CSV files found:", all_files)

    dataframes = []

    for file in all_files:   # ← LOOP STARTS HERE
        path = os.path.join(folder, file)
        df = pd.read_csv(path)

        print(f"\nProcessing {file}")
        print("Columns:", df.columns)

        # Use datasets with real labels
        if 'body' in df.columns and 'label' in df.columns:
            df = df[['body', 'label']]
            df.columns = ['text', 'label']

        elif 'text_combined' in df.columns and 'label' in df.columns:
            df = df[['text_combined', 'label']]
            df.columns = ['text', 'label']

        else:
            print(f"Skipping {file} (no usable labeled data)")
            continue   # ✅ NOW it's correctly inside the loop

        dataframes.append(df)

    # After loop
    if len(dataframes) == 0:
        raise ValueError("No valid data found")

    combined_df = pd.concat(dataframes, ignore_index=True)

    print("Total dataset size:", combined_df.shape)

    return combined_df