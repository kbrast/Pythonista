import os 

# Build a script that extracts the name and size of a file in your current working directory
path = os.getcwd()

# Get list of all files in current working directory
dir_list = list(os.listdir(path))

# Create empty dictionary
file_dict = {}

# Get list of file sizes in current working directory and put them in dictionary
# Dictionary syntax is dict_name[key] = value
for item in dir_list:
    file_size = os.stat(item)
    file_dict[item] = file_size

# Print dictionary as a list
# {:d} tells the formatter to treat the argument as an integer
# {:30} tells the formatter to allow 30 spaces for the filename character
# .format(name)
for item in file_dict:
    print({"File: {:30} Size: {:d} Bytes".format(item,file_dict[item].st_size)})