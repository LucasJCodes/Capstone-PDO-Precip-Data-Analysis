# Need a function that's going to count the number of januarys, februarys, etc. that are classified as phase changes.

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

# Read in the booleans dataset
data = xr.open_dataset('/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Data/phaseChanges.nc')

# Print the list of phase changes by month for each member (output should be 10 lists).
for i in range(0, 10):
    boolsTest = data['is_phase_change'][i]
    print(phaseMonths(boolsTest))