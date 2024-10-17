import argopy
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import time


def plot_temp_vs_abs_latitude():
    try:
        df_raw = pd.read_csv('data.csv')
    except:
        print("Importing data...")
        t0 = time.time()
        ArgoSet = argopy.DataFetcher().region([-180, 180, -90, 90, 0, 5, '2015-01', '2015-02'])
        print("Time to import : ", time.time() - t0)
        ds = ArgoSet.data.argo.point2profile().to_dataframe()
        print("Time to get data from DataFetcher : ", time.time() - t0)
        ds.to_csv('data.csv')

    # Remove rows where temp is None
    df = df_raw.dropna(subset=['TEMP'])

    # Define the variables to work with:
    temp = np.array(df['TEMP'])
    lat = np.array(df['LATITUDE'])

    # Absolute value of latitudes
    abs_lat = np.abs(lat)

    # Scatter and grid
    plt.scatter(abs_lat, temp, s=1)
    plt.grid(True)

    # Title and Labels
    plt.title('Temperature Vs. Absolute Value of Latitude')
    plt.xlabel('|Latitude|')
    plt.ylabel('Temperature')

    # Save figure and show the plot
    plt.savefig('figures/temp_vs_abs(latitude).png')
    plt.show()
    return True


if __name__ == "__main__":
    flag = False
    while not flag:
        try:
            flag = plot_temp_vs_abs_latitude()
        except:
            print("Argo Server Timeout Error : retrying")
            print("To exit, press ctrl+c 2x")
            time.sleep(2)
