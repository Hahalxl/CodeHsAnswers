import pandas as pd
from fuzzywuzzy import process, fuzz

# Importing the dataset
gpu_stat = pd.read_csv("GPU.csv")
share = pd.read_csv("market.csv")


# Check for dulicated values
print(gpu_stat.duplicated().sum())
print(share.duplicated().sum())

# Check for null/None type values
print(gpu_stat.isnull().sum())
print(share.isnull().sum())

# Percentage of null values in the whole dataset
print(gpu_stat.isnull().mean())
print(share.isnull().mean())


# I should not check any Fuzzywuzzy value as there are no duplicated names.

# Nvdia and amd gpu that is Geforce and Radeon
nvidia_rtx = gpu_stat[gpu_stat["gpuName"].str.startswith("GeForce")]
amd_rx = gpu_stat[gpu_stat["gpuName"].str.startswith("Radeon")]
