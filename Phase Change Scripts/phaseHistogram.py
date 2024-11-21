# Need a function that's going to count the number of januarys, februarys, etc. that are classified as phase changes.

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

def phaseMonths(boolean):
    # Takes in a boolean from one member, then finds the number of phase changes (boolean == 1) per month and puts them in a list.

    phaseMonths = np.arange(0, 12)
    for m in range(0, 12):
        phaseMonths[m] = 0
        i = 0
        while (i+m)*12 < len(boolean):
            phaseMonths[m] = phaseMonths[m] + boolean[(i+m)*12]
            i+=1
    return phaseMonths

def sumMonths(booleans):
    sum = np.zeros(12)  # Initialize array for cumulative sums
    for b in booleans:
        sum += phaseMonths(b)
    return sum

# Read in the booleans dataset
data = xr.open_dataset('/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Data/phaseChanges.nc')

months = np.arange(1, 13, 3)
count = sumMonths(data['is_phase_change'])
seasons = ['Winter', 'Spring', 'Summer', 'Fall']
seasons_sums = [
    sum(count[0:3]),  # Jan, Feb, Mar (Winter)
    sum(count[3:6]),  # Apr, May, Jun (Spring)
    sum(count[6:9]),  # Jul, Aug, Sep (Summer)
    sum(count[9:12])  # Oct, Nov, Dec (Fall)
]

# Create a bar plot of the number of phase changes.
fig, ax = plt.subplots()
ax.bar(seasons, seasons_sums, width = 0.6, color = 'seagreen')
ax.set_title('Number of Phase Change Months Per Season - All Members')
ax.set_ylim(350, 400)
plt.show()