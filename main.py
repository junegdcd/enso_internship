import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

file = "observations_AVISO_historical_r1i1p1f1_1993_2019_hovmoeller.nc"
ds = xr.open_dataset(f"./data_timeseries_hovmoeller/{file}")
rssh_aviso = [var for var in ds.data_vars if var.startswith("rssh_")]
rssh_north = ['rssh_pequ', 'rssh_pen1', 'rssh_pen3']
rssh_south = ['rssh_pequ', 'rssh_pes1', 'rssh_pes3']

# Function to plot Hovmöller diagrams
def plot_hovmoller(dataset, variables, title="Hovmöller Diagrams"):
    num_vars = len(variables)
    ncols = min(3, num_vars)  # Max 3 columns
    nrows = int(np.ceil(num_vars / ncols))  # Compute rows dynamically

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14, 3 * nrows), sharey=True)
    axes = np.atleast_1d(axes).flatten()  # Flatten to handle single-row cases

    # Determine shared color scale
    vmin = min(np.nanmin(dataset[var].values) for var in variables)
    vmax = max(np.nanmax(dataset[var].values) for var in variables)
    max_cbar = int(max(abs(np.round(vmin, 0)), abs(np.round(vmax, 0))))
    N = int(np.round(max_cbar, 1) * 2)
    levels = np.linspace(-max_cbar, max_cbar, N + 1)
    cmap = plt.get_cmap('coolwarm', N)

    # Plot each Hovmöller diagram
    for i, var in enumerate(variables):
        ax = axes[i]
        time = dataset["time"]
        lon = dataset["longitude"]
        data = dataset[var]

        c = ax.contourf(lon, time, data, levels=levels, cmap=cmap, vmin=-max_cbar, vmax=max_cbar)
        ax.set_title(var)
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Time")

    # Remove empty subplots if any
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # Add a single colorbar
    cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])  # Adjust position
    cbar = fig.colorbar(c, cax=cbar_ax)
    cbar.set_label("Data Value")
    cbar.ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x)}"))  # Format labels
    fig.suptitle(title, fontsize=14)

plot_hovmoller(ds, rssh_aviso, title="All RSSH Variables")
plot_hovmoller(ds, rssh_north, title="Hovmoeller Diagram for RSSH (eq and north only)")
plot_hovmoller(ds, rssh_north, title="Hovmoeller Diagram for RSSH (eq and south only)")
plt.show()
