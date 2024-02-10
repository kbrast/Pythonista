# Search for a specific filename or partial spelling pattern and return the results

# Import the glob module
import glob

# Define the file name or pattern to search for
file_name = "example.txt" # Exact file name
# file_name = "*.txt" # All files with .txt extension
# file_name = "examp?e.*" # Files with similar spelling pattern

# Define the directory to search in
directory = "/home/user/Documents/" # Change this to your desired directory

# Use glob.glob to get a list of matching file paths
file_paths = glob.glob(directory + file_name)

# Print the results to the terminal
print(f"Found {len(file_paths)} matching files:")
for file_path in file_paths:
    print(file_path)

# Uncomment the following lines to send the output to a file
# output_file = "output.txt" # Change this to your desired output file name
# with open(output_file, "w") as f:
#     f.write(f"Found {len(file_paths)} matching files:\n")
#     for file_path in file_paths:
#         f.write(file_path + "\n")
