import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt

# Function to read CSV file and ignore empty/non-numeric values
def read_csv_file(filename):
    try:
        # Read CSV, ignore empty cells, drop invalid data
        data = pd.read_csv(filename, header=None, skip_blank_lines=True).dropna()
        
        # Convert to NumPy array, flatten, and ignore non-numeric values
        return pd.to_numeric(data[0], errors='coerce').dropna().values.flatten()
    
    except pd.errors.EmptyDataError:
        print(f"Warning: {filename} is empty! Returning an empty array.")
        return np.array([])
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return np.array([])

# Function to compute Signal-to-Noise Ratio (SNR)
def compute_snr(original, filtered):
    noise = original - filtered
    signal_power = np.mean(original ** 2)
    noise_power = np.mean(noise ** 2)
    return 10 * np.log10(signal_power / noise_power)

# Function to compute Mean Squared Error (MSE)
def compute_mse(original, filtered):
    return np.mean((original - filtered) ** 2)

# Function to compute Convergence Speed (Rate of MSE reduction)
def compute_convergence_speed(mse_values):
    return -np.gradient(mse_values).mean()

# File paths
input_file = "input.csv"
output_file = "output.csv"

# Read input and output data
input_data = read_csv_file(input_file)
output_data = read_csv_file(output_file)

# Check if data is successfully loaded
if len(input_data) == 0 or len(output_data) == 0:
    print("Error: One or both CSV files are empty or contain no valid data!")
    sys.exit()  # Exit the script properly

# Ensure same length
min_len = min(len(input_data), len(output_data))
input_data = input_data[:min_len]
output_data = output_data[:min_len]

# Compute evaluation metrics
snr = compute_snr(input_data, output_data)
mse = compute_mse(input_data, output_data)

# Compute Convergence Speed
mse_values = [compute_mse(input_data[:i], output_data[:i]) for i in range(1, min_len)]
convergence_speed = compute_convergence_speed(mse_values)

# Plot Input vs Output Signal
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(input_data, label="Input Signal", color="blue")
plt.plot(output_data, label="Filtered Output", color="red", linestyle="dashed")
plt.title("Input vs. Output Signal")
plt.legend()
plt.grid()

# Plot Convergence Speed (MSE over time)
plt.subplot(2, 1, 2)
plt.plot(mse_values, label="MSE", color="green")
plt.title("MSE Convergence Over Time")
plt.xlabel("Iterations")
plt.ylabel("MSE")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# Print the evaluation metrics
print(f"Signal-to-Noise Ratio (SNR): {snr:.2f} dB")
print(f"Mean Squared Error (MSE): {mse:.6f}")
print(f"Convergence Speed: {convergence_speed:.6f}")