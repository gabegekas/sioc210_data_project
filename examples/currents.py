import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from scipy.interpolate import make_interp_spline
import pandas as pd
from scipy.special import comb


def bezier_curve(x_points, y_points, num=200):
    """
    Make a smooth curve based on the given points
    :param x_points: x coordinates
    :param y_points: y coordinates
    :param num: number of points on the smooth curve
    :return: list of points that sketches the curve
    """
    n = len(x_points) - 1
    if num <= n:
        num = n+1
    t = np.linspace(0.0, 1.0, num=num)
    curve = np.zeros((num, 2))
    for i, tt in enumerate(t):
        x_curve = sum(comb(n, j) * (1 - tt) ** (n - j) * tt ** j * x_points[j] for j in range(n + 1))
        y_curve = sum(comb(n, j) * (1 - tt) ** (n - j) * tt ** j * y_points[j] for j in range(n + 1))
        curve[i] = [x_curve, y_curve]
    return curve


def plot_currents(min_lon, max_lon, min_lat, max_lat, min_depth, max_depth,
                  start_date, end_date, data_file=None, current_count=100):
    """
    Plot the currents from the bouy displacement data.
    data_file is optional, but it is recommended to use local data or save
    the remote data to local files for a better stability.
    :param min_lon: minimum longitude of interested region, from -180 to 180
    :param max_lon: maximum longitude of interested region, from -180 to 180
    :param min_lat: minimum latitude of interested region, from -90 to 90
    :param max_lat: maximum latitude of interested region, from -90 to 90
    :param min_depth: minimum depth of interested region, from 0 to 100
    :param max_depth: maximum depth of interested region, from 0 to 100
    :param start_date: start date of interested period, e.g. "2015-06", "2015-01-07"
    :param end_date: end date of interested period, e.g. "2015-06", "2015-01-07"
    :param data_file: local bouy data used for analysis (optinal), e.g. "data.csv"
    :param current_count: number of currents to be plotted
    """
    df = pd.DataFrame()
    if data_file is not None:
        df = pd.read_csv(data_file)
    else:
        import argopy
        f = argopy.DataFetcher()
        count = 0
        while count <= 100:
            try:
                f = f.region([min_lon, max_lon, min_lat, max_lat, min_depth, max_depth, start_date, end_date])
                df = f.data.to_dataframe()
                df.to_csv('data.csv', index=False)
                break
            except:
                count += 1
    new_df = df[['PLATFORM_NUMBER','LONGITUDE','LATITUDE','TEMP']]
    df = new_df
    grouped_df = df.groupby('PLATFORM_NUMBER')
    dataframes_by_id = [group for _, group in grouped_df]

    scales = []
    for single in dataframes_by_id:
        val = 0
        val += abs(single['LONGITUDE'].iloc[-1]-single['LONGITUDE'].iloc[0])
        val += abs(single['LATITUDE'].iloc[-1] - single['LATITUDE'].iloc[0])
        if val >= 100 or single['LATITUDE'].max()-single['LATITUDE'].min()>90:
            val = 0
        scales.append(val)

    max_indices = sorted(range(len(scales)), key=lambda i: scales[i], reverse=True)[:current_count]
    dfs_to_be_plot = [dataframes_by_id[i] for i in max_indices]

    fig = plt.figure(figsize=(36,18))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.LAND, color='lightgray')
    ax.set_xlim([min_lon, max_lon])
    ax.set_ylim([min_lat, max_lat])
    ax.set_xlabel('Longitude', fontsize=12, labelpad=10)
    ax.set_ylabel('Latitude', fontsize=12, labelpad=10)
    fig.suptitle('Currents extracted from bouy displacement data', fontsize=14)
    cmap = plt.get_cmap('coolwarm')
    for single in dfs_to_be_plot:
        print(single)
        lon = single['LONGITUDE'].tolist()
        lat = single['LATITUDE'].tolist()
        dif = len(lon) // 100 + 1
        lon = lon[::dif]
        lat = lat[::dif]
        curve = bezier_curve(lon, lat)
        ax.plot(curve[:, 0], curve[:, 1], color=cmap(single['TEMP'].mean()/20.0))
        vl = single['TEMP'].mean()/20.0
        if vl > 0.5:
            cl = 'red'
        else:
            cl = 'blue'
        ax.arrow(lon[-1], lat[-1], (lon[-1]-lon[0])/10, (lat[-1]-lat[0])/10, length_includes_head=True, head_width=0.7, head_length=1, fc=cl, ec=cl)

    ax.set_xticks(np.arange(min_lon, max_lon+1, (max_lon-min_lon)/10), crs=ccrs.PlateCarree())
    ax.set_yticks(np.arange(min_lat, max_lat+1, (max_lat-min_lat)/10), crs=ccrs.PlateCarree())

    fig.show()


if __name__ == "__main__":
    plot_currents(-180,180,-90,90,0,10,'2015-01','2015-06',current_count=700)
    plot_currents(-180,180,-90,90,0,10,'2015-07','2015-12',current_count=700)

