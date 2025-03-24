import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


files = ["observations_AVISO_historical_r1i1p1f1_1993_2019_time_series.nc",
        "observations_ORAS5_historical_r1i1p1f1_1993_2019_time_series.nc"]
ds = [xr.open_dataset(f".\data\{f}", engine='h5netcdf') for f in files]
rssh_aviso = [var for var in ds[0].data_vars if var.startswith("rssh_")]
rssh_oras5 = [var for var in ds[1].data_vars if var.startswith("rssh_")]

def compute_rmse(h1, h2):
    """Compute the time series of RMSE between h1 and h2"""
    return np.sqrt(((h1-h2)**2).mean())

# Function to plot grouped variables
def plot_correlation(var1, var2, dataset1, dataset2, ax):
    """Plot the correlation of given variables of two datasets"""
    # Compute correlation
    s1 = dataset1[var1].to_pandas()
    s2 = dataset2[var2].to_pandas()
    correlation = s1.corr(s2)
    # Compute STD
    std1 = s1.std()
    std2 = s2.std()
    # Compute RSME
    rmse = compute_rmse(s1, s2)
    print(rmse)

    # Plot time series
    ax.plot(dataset1["time"], dataset1[var1], label=f"{var1} (AVISO)")
    ax.plot(dataset2["time"], dataset2[var2], label=f"{var2} (ORAS5)", linestyle='dashed')
    ax.set_title(f"Time series {var1}, correlation : {correlation:.4f}, RSME : {rmse:4f}, stds = ({std1:.4f},{std2:.4f})", fontsize=10)
    ax.set_ylabel("RSSH")
    ax.legend(loc="upper right")
    ax.grid(True)

# Plot
nvar = min(len(rssh_aviso), len(rssh_oras5))
fig, axes = plt.subplots(nrows=nvar, ncols=1, figsize=(12, 4*nvar), sharex=True)
fig.suptitle("Correlation of RSSH Variables from AVISO and ERAS5 datasets", fontsize=16, fontweight='bold')
for i, (var1, var2) in enumerate(zip(rssh_aviso, rssh_oras5)):
    plot_correlation(var1, var2, ds[0], ds[1], axes[i])

plt.subplots_adjust(hspace=0.5)
plt.xlabel("Time")
plt.show()

