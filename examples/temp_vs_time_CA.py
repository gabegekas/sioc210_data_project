import argopy
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
import pandas as pd
import time
from datetime import datetime


def plot_temp_vs_time_CA():
    # Fetch data for California in 2015
    try:
        df_raw = pd.read_csv('data_CA_2015.csv')
    except:
        print("Importing data...")
        t0 = time.time()
        ArgoSet = argopy.DataFetcher().region([-124, -116, 32, 42, 0, 5, '2015-01', '2015-12'])
        print("Time to import : ", time.time() - t0)
        ds = ArgoSet.data.argo.point2profile().to_dataframe()
        print("Time to get data from DataFetcher : ", time.time() - t0)
        ds.to_csv('data_CA_2015.csv')
        df_raw = pd.read_csv('data_CA_2015.csv')

    # Remove rows where temp is None
    df = df_raw.dropna(subset=['TEMP'])

    # Define the variables to work with:
    temp = np.array(df['TEMP'])
    time_strings = np.array(df['TIME'])

    # Assigns each datetime formatted time string to an array of datetime objects
    time = np.array([datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S') for time_string in time_strings])

    # Plots month name in x-axis
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%B'))

    # Scatter data and add grid
    plt.scatter(time, temp, s=1)
    plt.grid(True)

    # Title and labels
    plt.xlabel('Month')
    plt.ylabel('Temperature')
    plt.title('Temperature Vs. Time (California, 2015)')

    # Save figure and show the plot
    plt.savefig('figures/temp_vs_timeCA.png')
    plt.show()
    return True


if __name__ == "__main__":
    flag = False
    while not flag:
        try:
            flag = plot_temp_vs_time_CA()
        except:
            print("Argo Server Timeout Error : retrying")
            print("To exit, press ctrl+c 2x")
            time.sleep(2)
