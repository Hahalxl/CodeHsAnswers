import pandas as pd

gpu_stat = pd.read_csv("gpu.csv")

# Fill the NULL/None values from the last one
gpu_stat.fillna(0, inplace=True)

# Defining the dataset
nvidia_rtx = gpu_stat[gpu_stat["gpuName"].str.startswith("GeForce")]
amd_rx = gpu_stat[gpu_stat["gpuName"].str.startswith("Radeon")]

# Merging them together
amd_nvidia = pd.merge(nvidia_rtx, amd_rx, on="gpuName", how="outer")
print(amd_nvidia)
