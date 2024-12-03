import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.lines import Line2D
import datetime
import pandas as pd
import xarray as xr

def ID_Phase_NOAA(PDOindex, period, bound, gap):

    PDOindex['Date'] = pd.to_datetime(PDOindex[['Year', 'Month']].assign(Day=1))
    PDOindex['Phase Change'] = 0

    index = PDOindex["Value"]

    #fill the half of a period length with zeros so it accounts for a centered mean
    phaseBool = []
    NeutralDates = []

    for i in range(0, int(period/2)):
        phaseBool.append(0)

    for i in range(0, len(PDOindex)-period):
        SUM = 0

        for j in range(0, period):
            SUM = SUM + index[i+j]

        Average = SUM/period

        if ((Average >= -bound) and (Average <= bound)):

            central_month_index = i + period // 2
            NeutralDates.append(PDOindex['Date'][central_month_index])
            PDOindex.at[central_month_index, 'Phase Change'] = 1
            phaseBool.append(1)

        else: 
            phaseBool.append(0)

    #add zeros of length half of the period to the end to account for the centered rolling mean
    for i in range(0, int((period/2))):
        phaseBool.append(0)

    #print(PDOindex)

    for i in range(0, len(phaseBool)-gap):
        Flag = False

        if (phaseBool[i] == 1):
            for j in range(1, gap+1):

                if phaseBool[i+j] == 1:
                    Flag = True

        if Flag == True:
            phaseBool[i + 1] = 1
    

    print(len(NeutralDates))

    PDOindex['Color'] = ['red' if value > bound else 'blue' if value < -bound else 'black' for value in PDOindex['Value']]

    PDOindex['Rolling Average'] = PDOindex['Value'].rolling(window=period, center=True).mean()

    legend_elements = [Line2D([0], [0], color='black', lw=2, label=f'{period}-Month Rolling Average')]

    fig,ax = plt.subplots(2, 1, figsize=(15,4))
    ax[0].bar(PDOindex['Date'], PDOindex['Value'], width=45, color=PDOindex['Color'])
    ax[0].plot(PDOindex['Date'], PDOindex['Rolling Average'], color='black', linewidth=2, label=f'{period}-Month Rolling Average')
    ax[0].set_ylabel("PDO Index")
    ax[0].legend(handles=legend_elements, loc = "upper left")

    ax[1].step(PDOindex['Date'], phaseBool)
    ax[1].set_ylim(0,2)
    ax[1].set_yticks([0,1,2])
    ax[1].set_xlabel("Date (Months)")
    ax[1].set_ylabel("Phase Change (T/F)")

    fig.suptitle("Observational PDO Index (top) and Phase Changes (bottom)")
    plt.savefig("Plots/observationalIndex.png")
    '''
    ax[2].step(PDOindex['Date'], PDOindex['Phase Change'])
    ax[2].set_ylim(0,2)
    ax[2].set_yticks([0,1,2])
    ax[2].set_xlabel("Date")
    ax[2].set_title('PDO Phase Change Months (No Gap Fill)')
    '''

    return NeutralDates

############## function end

file = "NOAA_PDO_Index.csv"

NOAAdata = pd.read_csv(file)
PDOindex = pd.DataFrame(NOAAdata)

neutral = ID_Phase_NOAA(PDOindex, 72, 0.1, 20)