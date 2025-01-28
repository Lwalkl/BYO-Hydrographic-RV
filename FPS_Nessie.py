from post_processing.HydroSurveyor.process_file_HydroSurveyor import Hydro_process
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pickle as pickle
import scipy.stats as spy

# This file is the summary analysis file for the surfzone test, the first few commented lines process and save the data by using
# functions from other scripts. We are using the pickle module in order to write the data as bytes into a txt file. The rest of the
# script then loads the data using pickle and generates some plots. Some of the plots require other individual data streams to work.
# To get these other data streams simple run hydroprocess on the raw data for whatever it needs to process.

# CombinedData = Hydro_process(
#     r"Z:\BHI_NearshoreJetskiSurvey_Data\2024_12_04\SecondExtract\1_M9Hydro.mat"
# )
# with open(r"Z:\BHI_NearshoreJetskiSurvey_Data\2024_12_04\SecondExtract\processed.txt",'wb') as file:
#     pickle.dump(CombinedData, file)

with open(
    r"Z:\BHI_NearshoreJetskiSurvey_Data\2024_12_04\SecondExtract\processed.txt",
    "rb",
) as file:
    CombinedData = pickle.load(file)

#Plot Longshore, Crosshore, and Vertical Components

def adcp_comparison_Abs(CombinedData):

    lw = 1
    fig, axs = plt.subplots(3, sharex=True)
    axs[0].plot(
        (CombinedData["DateTime"]),
        (pd.DataFrame(np.nanmean(CombinedData["LSVel"], axis=1))),
        label="Longshore",
    )
    axs[0].legend()
    axs[1].plot(
        CombinedData["DateTime"],
        (pd.DataFrame(np.nanmean(CombinedData["CSVel"], axis=1))),
        color="Red",
        label="Cross-Shore",
        linewidth=lw,
    )
    axs[1].legend()
    axs[2].plot(
        CombinedData["DateTime"],
        (pd.DataFrame(np.nanmean(CombinedData["VertVel"], axis=1))),
        color="Green",
        label="Vertical",
        linewidth=lw,
    )
    fig.suptitle("Velocity Components versus Time")
    fig.supxlabel("Time (DD HH:MM)")
    fig.supylabel("Velocity (m/s)")
    plt.xlim(CombinedData['DateTime'][0],CombinedData['DateTime'][-1])
    axs[2].legend()
    plt.show()



def bathy_plot(CombinedData):
    # Sample data: Replace with your actual longitude, latitude, and depth values
    x = CombinedData["Longitude"]  # Longitude
    y = CombinedData["Latitude"]  # Latitude
    z = CombinedData["VbDepth"]  # Depth (negative for bathymetry)

    # Create 3D figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Plotting options:
    # 1. Scatter Plot
    im1 = ax.scatter(x, y, z, c=z, cmap="viridis")  # Color by depth
    ax.invert_zaxis()
    cbar = plt.colorbar(im1, ax=ax, shrink=0.5, aspect=5)
    cbar.set_label("Depth (meters)")
    # Set labels and title
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_zlabel("Depth")
    plt.title("3D Bathymetry Survey")

    plt.show()

adcp_comparison_Abs(CombinedData)

bathy_plot(CombinedData)