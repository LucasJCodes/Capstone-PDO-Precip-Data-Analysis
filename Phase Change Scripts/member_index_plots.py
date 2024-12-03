import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from PDOindex import ID_Phase
from performEOF import PDO_index


bound = 0.1
period = 72

#iterate through plotting the index and phase changes for each of the 10 members, saving each to its own .png
for i in range(11, 21):
    data_in = xr.open_dataset("Data/SSTmem"+ str(i) + ".nc")

    index = PDO_index(data_in)

    index = index.to_dataset()
    squeezed = index.squeeze(dim = "mode")

    neutral, dates = ID_Phase(squeezed["pcs"], period, bound)

    #Since the plot wants to use datetime formats, we need to convert cftime into datetime formats, done through saving the dataset as a DataFrame and using a Pandas command
    data = squeezed["pcs"].to_dataframe()
    data['time'] = data.index
    data.reset_index(drop = True, inplace = True)

    data['time'] = pd.to_datetime([f"{date.year}-{date.month:02d}-{date.day:02d}" for date in data['time']])

    data['Color'] = xr.DataArray(['red' if pcs > bound else 'blue' if pcs < -bound else 'black' for pcs in index["pcs"]])#, dims = index["pcs"].dims, coords = index["pcs"].coords)

    rollingAvg = data["pcs"].rolling(window = period, center=True).mean()

    fig,ax = plt.subplots(2, 1, figsize=(15,4))

    legend_elements = [Line2D([0], [0], color='black', lw=2, label=f'{period}-Month Rolling Average')]

    width = (data['time'].iloc[1] - data['time'].iloc[0]).days * 0.9
    ax1 = ax[0].bar(data['time'].values, data["pcs"], width = width, color = data['Color'])
    ax[0].plot(data['time'], rollingAvg, color='black', linewidth=2, label=f'{period}-Month Rolling Average')
    ax[0].set_ylabel("PDO Index")
    ax[0].legend(handles = legend_elements, loc = "upper left")

    ax2 = ax[1].step(data['time'], neutral)
    ax[1].set_ylim(0,2)
    ax[1].set_yticks([0,1,2])
    ax[1].set_ylabel("Phase Change (T/F)")

    fig.suptitle("Member " + str(i) + " PDO Index (top) and Phase Changes (bottom)")

    plt.savefig("Plots/member" + str(i) + "index.png")