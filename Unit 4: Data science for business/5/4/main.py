import pandas as pd

gpu_stat = pd.read_csv("gpu.csv")

# Fill the NULL/None values from the last one
gpu_stat.fillna(0, inplace=True)

# Defining the dataset
nvidia_rtx = gpu_stat[gpu_stat["gpuName"].str.startswith("GeForce")]
amd_rx = gpu_stat[gpu_stat["gpuName"].str.startswith("Radeon")]

# Combined Nvidia and amd (also sorted)
df = pd.concat([nvidia_rtx, amd_rx])

df["ppd"] = df["G3Dmark"] / df.loc[df["price"] > 0, :].price
print(df.ppd)

# Find the best performance per dollar
