import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd

files = ["observations_AVISO_historical_r1i1p1f1_1993_2019_time_series.nc",
        "observations_ORAS5_historical_r1i1p1f1_1993_2019_time_series.nc"]
ds = [xr.open_dataset(f".\data\{f}", engine='h5netcdf') for f in files]
print(ds)

# Group variables
rssh_aviso = [var for var in ds[0].data_vars if var.startswith("rssh_")]
rssh_oras5 = [var for var in ds[1].data_vars if var.startswith("rssh_")]

# Def subplot
nvar = min(len(rssh_aviso), len(rssh_oras5))
fig, axes = plt.subplots(nrows=nvar, ncols=1, figsize=(12, 4*nvar), sharex=True)
fig.suptitle("Correlation two by two of RSSH Variables", fontsize=16, fontweight='bold')

# Function to plot paired time series with correlation
def plot_correlation(var1, var2, dataset1, dataset2, ax):
    if var1 not in dataset1 or var2 not in dataset2:
        print(f"Skipping pair ({var1}, {var2}) - One of the variables is missing.")
        return

    df = pd.DataFrame({
        var1: dataset1[var1].values.flatten(),
        var2: dataset2[var2].values.flatten()
    }).dropna()

    if df.shape[1] < 2:  # Ensure both variables exist in the DataFrame
        print(f"Skipping pair ({var1}, {var2}) - Not enough data for correlation.")
        return

    correlation = df.corr().iloc[0, 1]  # Compute correlation

    # Plot time series
    ax.plot(dataset1["time"], dataset1[var1], label=f"{var1} (AVISO)")
    ax.plot(dataset2["time"], dataset2[var2], label=f"{var2} (ORAS5)", linestyle='dashed')

    # Formatting
    ax.set_title(f"Correlation ({var1} & {var2}): {correlation:.2f}")
    ax.legend(loc="upper right")
    ax.grid(True)
