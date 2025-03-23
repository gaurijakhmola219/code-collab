import pandas as pd

# Path to the merged CSV file
merged_file_path = r"C:\Users\gauri\Downloads\merged_job.csv"

# Load the merged dataset
merged_df = pd.read_csv(merged_file_path)

# Step 1: Drop duplicate rows
merged_df.drop_duplicates(inplace=True)

# Step 2: Convert all string columns to lowercase and remove extra spaces
for col in merged_df.select_dtypes(include='object').columns:
    merged_df[col] = merged_df[col].str.lower().str.strip()

# Step 3: Perform One-Hot Encoding
categorical_cols = merged_df.select_dtypes(include='object').columns
encoded_df = pd.get_dummies(merged_df, columns=categorical_cols, drop_first=True)

# Save the encoded dataset
encoded_file_path = r"C:\Users\gauri\Downloads\encoded_jobs.csv"
encoded_df.to_csv(encoded_file_path, index=False)

print("✅ One-Hot Encoding completed and encoded dataset saved at:", encoded_file_path)
