import pandas as pd
import numpy as np
import matplotlib.pyplot as mp

gpu_stat = pd.read_csv(r"gpu.csv")
gpu_stat.fillna(0, inplace=True)

# Getting the data
nvidia = gpu_stat[gpu_stat["gpuName"].str.startswith("GeForce RTX")]
amd = gpu_stat[gpu_stat["gpuName"].str.startswith("Radeon RX")]

# Get the model
nvidia['model'] = nvidia['gpuName'].str.extract(r'(\d+(\s?(Ti|Super))?)$')
nvidia['model'] = pd.to_numeric(nvidia['model'], errors='coerce')
nvidia["name"] = nvidia['gpuName'].str.extract(r'(\d{4} Ti|\d{4})')


print(nvidia[['gpuName','model']])

amd['model'] = amd['gpuName'].str.extract(r'(\d+)$')
amd['model'] = pd.to_numeric(amd['model'], errors='coerce')

nvidia = nvidia.loc[nvidia['model'] > 2080, :]
amd = amd.loc[amd['model'] > 6000, :]
s = nvidia.loc[(nvidia.model < 4000), :]
print(s)

#mp.plot(amd.model, amd.G3Dmark)
#mp.bar(, nvidia.loc[(nvidia.model > 3000) & (nvidia.model < 4000), :].G3Dmark, width=0.5)
mp.show()
