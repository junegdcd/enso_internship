import xarray as xr
import matplotlib.pyplot as plt

file = "observations_AVISO_historical_r1i1p1f1_1993_2019_time_series.nc"
ds = xr.open_dataset(f".\data\{file}", engine='h5netcdf')
print(ds)

# Group variables
ssh_vars = [var for var in ds.data_vars if var.startswith("ssh_")]
rssh_vars = [var for var in ds.data_vars if var.startswith("rssh_")]

# Function to plot grouped variables
def plot_variables(var_list, title, dataset, ax):
    for var in var_list:
        ax.plot(dataset["time"], dataset[var], label=var)
    ax.set_title(title)
    #ax.set_xlabel("Time")
    #ax.set_ylabel("Var")
    ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    ax.grid(True)

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 8), sharex=True)
fig.suptitle("AVISO time series", fontsize=16, fontweight='bold')
plot_variables(ssh_vars, "SSH Variables", ds, axes[0])
plot_variables(rssh_vars, "RSSH Variables", ds, axes[1])
plt.show()

