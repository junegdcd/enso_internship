import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import scipy.stats
from Ex6_plot_comparison_D20_SSHA import ds_pretreatement,\
    ds_compute_anomalies, compute_statistics, plot_map_stat, plot_map_phy
# ---------------------------------------------------------------------------------------------------------------------#
# Exercise 7: Plot maps of aviso and ctl to compare stds, skewness, ...
# ---------------------------------------------------------------------------------------------------------------------#
# --- Functions ---


# --- Main ---
paths = ["./data_fliu/CTL_1980-2018_1M_grid_uos.nc", # change it with AVISO ssh
         "./data_fliu/CTL_1980-2018_1M_grid_vos.nc"]
ds = ds_pretreatement(paths)
ds = ds_compute_anomalies(ds, "time_counter", ["uos", "vos"])
ds_stat = compute_statistics(ds, ["uos_anom", "vos_anom"])

plot_map_phy(ds, ["uos", "vos"])

print('ds_ex7', ds)
plt.show()

