import pandas as pd

def compare_csv_files(csv_file1, csv_file2):
  """
  Compares two CSV files and displays differences.

  Args:
    csv_file1: Path to the first CSV file.
    csv_file2: Path to the second CSV file.
  """

  # Read CSV files into DataFrames
  df1 = pd.read_csv(csv_file1)
  df2 = pd.read_csv(csv_file2)

  # Compare DataFrames and identify differences
  differences = pd.concat([df1.set_index('id', drop=False).diff(other=df2.set_index('id', drop=False)),
                          df2.set_index('id', drop=False).diff(other=df1.set_index('id', drop=False))]).dropna(how='all', axis=1)

  # Check for rows missing in either file
  missing_in_1 = df2.set_index('id', drop=False).merge(df1.set_index('id', drop=False), how='left', indicator=True)
  missing_in_1 = missing_in_1[missing_in_1['_merge'] == 'left_only']
  missing_in_2 = df1.set_index('id', drop=False).merge(df2.set_index('id', drop=False), how='left', indicator=True)
  missing_in_2 = missing_in_2[missing_in_2['_merge'] == 'right_only']

  # Print different row values
  if not differences.empty:
    print("Differences in existing rows:")
    print(differences)

  # Print missing rows
  if not missing_in_1.empty:
    print("Rows missing in file 1:")
    print(missing_in_1)
  if not missing_in_2.empty:
    print("Rows missing in file 2:")
    print(missing_in_2)

# Example usage
compare_csv_files("file1.csv", "file2.csv")
