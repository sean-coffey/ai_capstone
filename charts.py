#!/usr/bin/env python

"""
module to contain code for EDA charts
"""

import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from ingestion import get_ts

## plot style, fonts and colors
plt.style.use('seaborn')

SMALL_SIZE = 9
MEDIUM_SIZE = 12
LARGE_SIZE = 14
COLORS = ["darkorange", "royalblue", "slategrey"]

plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)  # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
plt.rc('figure', titlesize=LARGE_SIZE)  # fontsize of the figure title

DATA_DIR = os.path.join(".", "data", "cs-train")
IMAGE_DIR = os.path.join(".", "plots")


def save_plot(file_name):
    if not os.path.exists(IMAGE_DIR):
        os.mkdir(IMAGE_DIR)
    image_path = os.path.join(IMAGE_DIR, file_name)
    plt.savefig(image_path, bbox_inches='tight', pad_inches=.5, dpi=200)
    print(f"{image_path} created.")


def create_normalised_line_plot(df,title='All'):
    """
    basic line plot for time series
    """
    print("... creating plot")

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # normalise the data
    scaler = MinMaxScaler()
    # fit and transform the data
    numeric_columns = ['revenue', 'total_views','unique_streams','purchases']
    # Draw the heatmap with the mask and correct aspect ratio
    plot_data = pd.pivot_table(df,
                               index='year_month',
                               values=numeric_columns,
                               aggfunc='sum'
                               )
    plot_data[numeric_columns] = scaler.fit_transform(plot_data[numeric_columns])
    ax = sns.lineplot(data=plot_data)
    ax.set_title("Normalised line plot for " + title)
    plt.setp(ax.get_xticklabels(), rotation=30)

    save_plot(title + "-normalised_line_plot.png")


def plot_attribute_by_country(ts_countries,attribute):
    f,axs = plt.subplots(int((len(ts_countries)+1)/2),2, sharex=True, figsize=(7,11))
    f.suptitle(t=attribute + " by country",fontsize=MEDIUM_SIZE)
    n,i,j = 0,0,0
    for key,df in ts_countries.items():
        ax = axs[i,j]
        plot_data = pd.pivot_table(df,
                               index='year_month',
                               values=attribute,
                               aggfunc='sum'
                               )

        ax.bar(x=plot_data.index,height=plot_data[attribute])
        ax.set_title(key)
        #plt.setp(ax.get_xticklabels(), rotation=30)
        ax.get_xaxis().set_visible(False)

        n += 1
        i, j = int(n/2), n%2
    f.tight_layout()

    save_plot(attribute + "-by_country.png")

def normalised_by_country(ts_countries):
    f,axs = plt.subplots(int((len(ts_countries)+1)/2),2, sharex=True, figsize=(7,11))
    f.suptitle(t="normalised features by country",fontsize=MEDIUM_SIZE)
    # normalise the data
    scaler = MinMaxScaler()
    # fit and transform the data
    numeric_columns = ['revenue', 'total_views', 'unique_streams', 'purchases']
    n,i,j = 0,0,0
    for key,df in ts_countries.items():
        ax = axs[i,j]
        plot_data = pd.pivot_table(df,
                                   index='year_month',
                                   values=numeric_columns,
                                   aggfunc='sum'
                                   )
        plot_data[numeric_columns] = scaler.fit_transform(plot_data[numeric_columns])
        ax.plot(plot_data.index,plot_data.values)
        ax.set_title(key)
        ax.get_xaxis().set_visible(False)
        ax.legend()

        n += 1
        i, j = int(n/2), n%2
    f.tight_layout()

    save_plot("normalised_by_country.png")



if __name__ == "__main__":
    data_dir = os.path.join(".", "data", "cs-train")
    ts_all = get_ts(DATA_DIR)
    ts_all.pop('all', None)
    normalised_by_country(ts_all)
