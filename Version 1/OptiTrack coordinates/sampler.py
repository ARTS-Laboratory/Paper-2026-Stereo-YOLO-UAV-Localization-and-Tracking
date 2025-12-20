import pandas as pd

# Load your Excel file
df = pd.read_excel("OPT_data.xlsx")  # Replace with your actual file name

n=13 #number of uniform distribution
# Uniformly select 10 rows from the DataFrame
selected_rows = df.iloc[::len(df)//n][:n]  # This samples evenly spaced rows

# Save the selected rows to a new Excel file
selected_rows.to_excel("Sampled_OPT_data.xlsx", index=False)
