import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import pandas as pd
import xarray as xr

def ID_Phase_NOAA(PDOindex, period, bound):

    PDOindex['Date'] = pd.to_datetime(PDOindex[['Year', 'Month']].assign(Day=1))
    PDOindex['Phase Change'] = 0

    index = PDOindex["Value"]

    phaseBool = []
    NeutralDates = []
    PhaseChange = []

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

    #print(PDOindex)

    for i in range(0, len(phaseBool)):
        Flag = False

        for j in range(0,5):

            if phaseBool[i+j] == 1:
                Flag = True

        if Flag == True:
            phaseBool[i] = 1

    print(len(NeutralDates))

    PDOindex['Color'] = ['red' if value > bound else 'blue' if value < -bound else 'black' for value in PDOindex['Value']]

    PDOindex['Rolling Average'] = PDOindex['Value'].rolling(window=period, center=True).mean()

    fig,ax = plt.subplots(figsize=(15,4))
    ax.bar(PDOindex['Date'], PDOindex['Value'], width=45, color=PDOindex['Color'])
    ax.plot(PDOindex['Date'], PDOindex['Rolling Average'], color='black', linewidth=2, label=f'{period}-Month Rolling Average')
    ax.set_xlabel("Date")
    ax.set_xlabel("Date")
    ax.set_ylabel("PDO Index Value")
    ax.set_title("NOAA PDO Index")
    ax.legend()

    fig2,ax2 = plt.subplots(figsize=(15,4))
    ax2.step(PDOindex['Date'], PDOindex['Phase Change'])
    ax2.set_ylim(0,2)
    ax2.set_yticks([0,1,2])
    plt.show()

    return NeutralDates

############## function end

file = "NOAA_PDO_Index.csv"

NOAAdata = pd.read_csv(file)
PDOindex = pd.DataFrame(NOAAdata)

neutral = ID_Phase_NOAA(PDOindex, 72, 0.1)