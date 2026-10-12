import statistics

data = [4, 7, 9, 2, 8, 5, 1, 6, 4, 4, 7]

# Calculate metrics using built-in methods
mean_val = statistics.mean(data)
median_val = statistics.median(data)

# multimode handles multiple modes; statistics.mode only returns the first one found
mode_vals = statistics.multimode(data) 

print("--- Built-in Statistics Module Results ---")
print(f"Dataset: {data}")
print(f"Mean:    {mean_val:.2f}")
print(f"Median:  {median_val}")
print(f"Mode(s): {mode_vals}")
