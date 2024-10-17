import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import time
import argopy


def plot_temp_vs_depth():
    try:
        df_raw = pd.read_csv('data.csv')
    except:
        print("Importing data...")
        t0 = time.time()
        ArgoSet = argopy.DataFetcher().region([80, 95, 5, 20, 0, 2000, '2020-01', '2020-02']) # Bay of Bengal
        print("Time to create DataFetcher variable : ", time.time() - t0)
        ds = ArgoSet.data.argo.point2profile().to_dataframe()
        print("Time to get data from DataFetcher : ", time.time() - t0)
        ds.to_csv('data.csv')

    # Remove rows where temp is None
    df = df_raw.dropna(subset=['TEMP', 'PRES'])

    # Define the variables to work with:
    temp = np.array(df['TEMP'])
    pressure = np.array(df['PRES'])
    print(pressure)

    # Scatter data and add grid
    plt.scatter(temp, pressure, s=1)
    plt.grid(True)
    plt.gca().invert_yaxis()

    # Adding labels to the axes and title
    plt.xlabel('Temperature [C]')
    plt.ylabel('Pressure [dBar]')
    plt.title('Temperature Vs. Pressure')

    # plt.savefig('figures/temp_vs_depth.png')
    plt.show()

    return True


if __name__ == "__main__":
    flag = False
    # plot_temp_vs_depth()
    while not flag:
        try:
            flag = plot_temp_vs_depth()
        except:
            print("Argo Server Timeout Error : retrying")
            print("To exit, press ctrl+c 2x")
            time.sleep(2)
