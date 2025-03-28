# ---------------------------------------------------------------------------------------------------------------------#
# Plot time series and main characteristics of AVISO and Control Simulation
# ---------------------------------------------------------------------------------------------------------------------#
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
paths = ["./data_timeseries_hovmoeller/observations_AVISO_historical_r1i1p1f1_1993_2019_time_series.nc",
    "./data_fliu/CTL_1980-2018_1M_grid_ssh.nc"]
ds = [xr.open_dataset(p) for p in paths]
ssh_aviso_n34 = ds[0]["ssh_n34e"]
ssh_aviso_n3 = ds[0]["ssh_n30e"]
ssh_aviso_n4 = ds[0]["ssh_n40e"]

# Conversion to pandas and cm
ds[1]["ssh"] = ds[1]["ssh"] * 100
ds[1] = ds[1].assign_coords(time_counter=[pd.Timestamp(t.strftime('%Y-%m-%d %H:%M:%S')) for t in ds[1]["time_counter"].values])

# Define regions
regions = {
    "N30": [(-5, 5), (210, 270)],
    "N40": [(-5, 5), (160, 210)],
    "N34": [(-5, 5), (190, 240)]
}

# Extract SSH variables of AVISO
ssh_aviso = {key: ds[0][f"ssh_{key.lower()}e"] for key in regions}

# Truncate time range (keep intersect)
start_date = ds[0]["time"].min().values
end_date = ds[1]["time_counter"].max().values
print(start_date, end_date)
ds[0] = ds[0].sel(time=slice(start_date, end_date))
ds[1] = ds[1].sel(time_counter=slice(start_date, end_date))
print(ds[0]["time"].values)
print(ds[1]["time_counter"].values)

# Compute spatial mean over each region for CTL
ssh_ctl = {key: ds[1]["ssh"].sel(lat=slice(*box[0]), lon=slice(*box[1])).mean(dim=["lat", "lon"]) for key, box in regions.items()}

# Remove mean seasonal cycle
for key in ssh_ctl:
    climatology = ssh_ctl[key].groupby("time_counter.month").mean("time_counter")
    ssh_ctl[key] = ssh_ctl[key].groupby("time_counter.month") - climatology

# Compute statistics
stats = {key: {
    "avg_aviso": ssh_aviso[key].mean().values,
    "avg_ctl": ssh_ctl[key].mean().values,
    "std_aviso": ssh_aviso[key].std().values,
    "std_ctl": ssh_ctl[key].std().values,
    "correlation": np.corrcoef(ssh_aviso[key].values, ssh_ctl[key].values, rowvar=False)[0 ,1]
} for key in regions}

# Plot AVISO and CTL SSH in subplots
fig, axes = plt.subplots(3, 1, figsize=(12, 12), sharex=True)
for i, (key, ax) in enumerate(zip(regions.keys(), axes)):
    print(stats[key]['correlation'])
    ax.plot(ds[0]["time"], ssh_aviso[key], label=f"{key} SSH AVISO mean = {stats[key]['avg_aviso']:.4f}, std = {stats[key]['std_aviso']:.2f}")
    ax.plot(ds[1]["time_counter"], ssh_ctl[key], label=f"{key} SSH CTL    mean = {stats[key]['avg_ctl']:.4f}, std = {stats[key]['std_ctl']:.2f}", color='orange')
    ax.set_title(f"AVISO and CTL SSH Anomalies averaged on {key}, correlation: {stats[key]['correlation']:.4f}")
    ax.set_ylabel("SSH (cm)")
    ax.grid(True)
    ax.legend(loc='upper left')

axes[-1].set_xlabel("Time")
plt.show()
