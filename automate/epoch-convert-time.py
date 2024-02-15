import time

# Get current time in seconds since the epoch
current_time = time.time()

# Get current time in milliseconds since the epoch
current_time_ms = int(current_time * 1000)

# Print the results
print("Current time in seconds:", current_time)
print("Current time in milliseconds:", current_time_ms)