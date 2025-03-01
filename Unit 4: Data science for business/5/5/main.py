import pandas as pd
import numpy as np

# Importing the dataset
gpu_stat = pd.read_csv("GPU.csv")

# Check for dulicated values
print(gpu_stat.duplicated().sum())

# Data type
print(gpu_stat.dtypes)

# Check for null/None type values
print(gpu_stat.isnull().sum())


# Filling the null/None into 0
gpu_stat.fillna(0, inplace=True)

# Check again (incase)
print(gpu_stat.isnull().sum())


# Percentage of null values in the whole dataset
print(gpu_stat.isnull().mean())



# I should not check any Fuzzywuzzy value as there are no duplicated names.

# Nvdia and amd gpu that is Geforce and Radeon
nvidia_rtx = gpu_stat[gpu_stat["gpuName"].str.startswith("GeForce")]
amd_rx = gpu_stat[gpu_stat["gpuName"].str.startswith("Radeon")]
df = pd.concat([nvidia_rtx, amd_rx])
