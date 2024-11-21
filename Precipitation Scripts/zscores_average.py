# Hi yet again. Today we're going to subset the zscores that fall within PDO phase change months and average them together by month.

import xarray as xr
import numpy as np
import precip_zscores
import glob

def phaseMask(zscores, booleans):
    # Zscores is a LIST of the zscores datasets for each members, and pc_months is the list of phase change months.

    #modified_zscores = zscores[0][:][:].where(booleans == 1, other=np.nan)

    #pc_months = booleans.where(booleans['is_phase_change'] == 1, drop = False)

    #test = zscores[0][:][:] * pc_months["is_phase_change"][0]

    modified_zscores = []
    
    for member in range(len(zscores)):

        # Ensure alignment and apply the boolean mask
        modified = zscores[member].where(booleans == 1, other=np.nan)
        modified_zscores.append(modified)

    return modified_zscores

    #print(test)

    # Subset zscores based only the months that are phase changes (the boolean == 1).
    """
    z_mask = []
    for member in range(0, 10):
        #pc_oneMem = pc_months.where(pc_months["is_phase_change"][member], drop = True)
        z_mask.append(zscores[member][:][:] * pc_months["is_phase_change"][member]) #pc_oneMem['is_phase_change'])

    print(z_mask)

    # # Calculate the average zscores for phase change months across all members.
    # avg_zs = phaseChange_zs.groupby('time.month').mean(dim = ['member', 'time'])
    """


# Need to find each member's zscores first.
filenames = sorted(glob.glob('/Users/defor/OneDrive/Documents/Capstone/Capstone-PDO-Precip-Data-Analysis/Data/PRECTmem*.nc'))
#print(filenames)

zscores = [precip_zscores.member_zscore(f) for f in filenames]

#zscores = []
#for f in filenames:
    #zscores.append(precip_zscores.member_zscore(f))
#print(zscores)

bools = xr.open_dataset('/Users/defor/OneDrive/Documents/Capstone/Capstone-PDO-Precip-Data-Analysis/Data/phaseChanges.nc')
#print(bools)

print(zscores[0].shape)  # Shape of a single zscore dataset
print(bools['is_phase_change'].shape)  # Shape of the boolean mask


modified_zscores = phaseMask(zscores, bools['is_phase_change'])

#test = phaseMask(zscores, bools)

print(modified_zscores[0])
