import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import math

# Define files
files = [
    "observations_AVISO_historical_r1i1p1f1_1993_2019_hovmoeller.nc",
    "observations_ORAS5_historical_r1i1p1f1_1993_2019_hovmoeller.nc"
]

# Load datasets
ds = [xr.open_dataset(f"./data/{f}") for f in files]

# Extract relevant variables
rssh_aviso = [var for var in ds[0].data_vars if var.startswith("rssh_")]
rssh_oras5 = [var for var in ds[1].data_vars if var.startswith("rssh_")]


# Function to plot Hovmöller diagrams side by side
def plot_hovmoller(var, dataset1, dataset2):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 5), sharey=True)

    time1 = dataset1["time"]
    lon1 = dataset1["longitude"]
    data1 = dataset1[var]

    time2 = dataset2["time"]
    lon2 = dataset2["lon"]
    data2 = dataset2[var]

    # Determine symmetric color limits for each plot
    vmin1 = np.nanmin(data1.values)
    print(vmin1)
    vmax1 = np.nanmax(data1.values)
    vlim1 = max(abs(vmin1), abs(vmax1))

    vmin2 = np.nanmin(data2.values)
    vmax2 = np.nanmax(data2.values)
    vlim2 = max(abs(vmin2), abs(vmax2))

    # Plot Hovmöller diagrams
    max_cbar = int(max(abs(np.round(vmin1, 0)), abs(np.round(vmax1, 0))))
    N = np.round(max_cbar,1) * 2 + 6
    levels = np.linspace(-max_cbar, max_cbar, N + 1)
    cmap = plt.get_cmap('coolwarm', N)
    print(levels)
    print()

    c1 = axes[0].contourf(lon1, time1, data1, levels=levels, cmap=cmap, vmin=-max_cbar, vmax=max_cbar)
    c2 = axes[1].contourf(lon2, time2, data2, levels=levels, cmap=cmap, vmin=-max_cbar, vmax=max_cbar)

    axes[0].set_title(f"AVISO - {var}")
    axes[1].set_title(f"ORAS5 - {var}")

    for ax in axes:
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Time")

    # Create a single colorbar
    cbar = fig.colorbar(c1, ax=axes, orientation="vertical")
    cbar.set_label(var)


# Plot each variable
for var in rssh_aviso:
    if var in rssh_oras5:
        plot_hovmoller(var, ds[0], ds[1])

plt.show()
