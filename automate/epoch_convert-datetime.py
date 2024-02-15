from datetime import datetime

# Define a specific date and time
specific_time = datetime(2024, 2, 15, 17, 38, 00)  # Replace with your desired date and time

# Convert to epoch time in seconds
epoch_time = specific_time.timestamp()

# Convert to epoch time in milliseconds
epoch_time_ms = int(epoch_time * 1000)

# Print the results
print("Epoch time for", specific_time, ":", epoch_time)
print("Epoch time in milliseconds:", epoch_time_ms)
