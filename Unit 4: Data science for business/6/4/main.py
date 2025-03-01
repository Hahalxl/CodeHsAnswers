import pandas as pd
import numpy as np

gpu_stat = pd.read_csv(r"gpu.csv")
nvidia_rtx = gpu_stat[gpu_stat["gpuName"].str.startswith("GeForce RTX")]
amd_rx = gpu_stat[gpu_stat["gpuName"].str.startswith("Radeon RX")]
gpu_stat.fillna(0, inplace=True)

# Considering that NVIDIA has older models such as the rtx 2000s I'm going to drop them
nvidia_rtx['model'] = nvidia_rtx['gpuName'].str.extract(r'(\d+)$')
nvidia_rtx['model'] = pd.to_numeric(nvidia_rtx['model'], errors='coerce')

nvidia_rtx = nvidia_rtx.loc[nvidia_rtx['model'] > 2080, :]

# Average G3Dmark point
print("Average G3Dmark points (The higher the better) \n========================================")
print("Nvidia G3Dmark:", round(nvidia_rtx.G3Dmark.mean(), 2))
print("AMD G3Dmark:", round(amd_rx.G3Dmark.mean(), 2), "\n\n")

# Average Price
print("Average price (The lower the better) \n========================================")
print("Nvidia price:", round(nvidia_rtx.price.mean(), 2))
print("AMD price:", round(amd_rx.price.mean(), 2), "\n\n")

# Price per G3Dmark score
amd_rx["pps"] = amd_rx.G3Dmark // amd_rx.price
nvidia_rtx["pps"] = nvidia_rtx.G3Dmark // nvidia_rtx.price


print("Price per score (The higher the better) \n========================================")
print("Nvidia price:", round(nvidia_rtx.pps.mean(), 2))
print("AMD price:", round(amd_rx.pps.mean(), 2), "\n\n")

# Other information
print("AMD\n========================================")
print("Range (price):", amd_rx.price.min(), amd_rx.price.max())
print("Range (G3Dmark):", amd_rx.G3Dmark.min(), amd_rx.G3Dmark.max())
print("Range (TDP):", amd_rx.TDP.min(), amd_rx.TDP.max())
print("Range (gpuValue):", amd_rx.gpuValue.min(), amd_rx.gpuValue.max())
print("\n\n")

print("Nvidia\n========================================")
print("Range (price):", nvidia_rtx.price.min(), "-", nvidia_rtx.price.max())
print("Range (G3Dmark):", nvidia_rtx.G3Dmark.min(), nvidia_rtx.G3Dmark.max())
print("Range (TDP):", nvidia_rtx.TDP.min(), nvidia_rtx.TDP.max())
print("Range (gpuValue):", nvidia_rtx.gpuValue.min(), nvidia_rtx.gpuValue.max())
