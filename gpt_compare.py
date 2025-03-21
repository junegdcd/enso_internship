import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

file = "observations_AVISO_historical_r1i1p1f1_1993_2019_time_series.nc"
ds = xr.open_dataset(f".\data\{file}", engine='h5netcdf')
print(ds)

# Identify variable groups based on prefixes before the first underscore
var_groups = {}
for var in ds.data_vars:
    if "_" in var:  # Ensures we only group variables with prefixes
        prefix = var.split("_")[0]
        var_groups.setdefault(prefix, []).append(var)

# Sort groups by number of variables for consistent ordering
var_groups = dict(sorted(var_groups.items(), key=lambda x: len(x[1]), reverse=True))

# Determine subplot layout (rows and columns)
num_groups = len(var_groups)
num_cols = 2  # Set number of columns (adjust as needed)
num_rows = int(np.ceil(num_groups / num_cols))  # Calculate required rows

# Create figure and axes
fig, axes = plt.subplots(num_rows, num_cols, figsize=(14, 6 * num_rows), sharex=True)

# Flatten axes if there's more than one row
axes = np.atleast_1d(axes).flatten()

# Plot each variable group in its own subplot
for ax, (prefix, vars) in zip(axes, var_groups.items()):
    for var in vars:
        ax.plot(ds["time"], ds[var], label=var)
    ax.set_title(f"{prefix.upper()} Variables")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.legend()
    ax.grid(True)

# Hide unused subplots (if any)
for i in range(len(var_groups), len(axes)):
    fig.delaxes(axes[i])

# Adjust layout and show
plt.tight_layout()
plt.show()
