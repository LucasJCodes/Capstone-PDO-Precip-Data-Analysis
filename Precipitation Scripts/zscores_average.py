# Hi yet again. Today we're going to subset the zscores that fall within PDO phase change months and average them together by month.

import xarray as xr
import numpy as np

def phaseMask(zscores, pc_months):
    # Zscores is the zscores dataset and pc_months is the list of phase change months.

    phaseChange_zs = zscores.where(zscores['time.month'].isin(pc_months), drop=True)

    # Calculate the average zscores for each month at each gridpoint during phase changes.
    avg_zs = phaseChange_zs.groupby('time.month').mean('time')
