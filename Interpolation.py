import json
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np
from scipy.interpolate import griddata

#Regreasaion Model For Fuel Flow

#4D Function For fuleFLow

#Speed Intervall

#Global variables
global airCraftData

def LoadDataFromFile(filePath):
    #LOAD DATA
    with open(filePath, "r") as fin:
        ac_data = json.loads(fin.read())

    tables = ac_data["tables"]
    dataframes = []

    for table in tables:
        if table["header"]["flightphase"] == "cruise":
            cols = table["header"]["variables"]
            data = table["table"]
            dataframes.append(pd.DataFrame(data, columns=cols))

    print("Loaded "+str(len(dataframes)) + " tabels\n")
    return(dataframes)

def LoadDataPoor():
    print("Loading DataPoor...")
    DataPorFilePaths = ["ac_poor_1.bsad","ac_poor_2.bsad","ac_poor_3.bsad","ac_poor_4.bsad","ac_poor_5.bsad","ac_poor_6.bsad","ac_poor_7.bsad"]
    dataframes = []
    #Load all tabels as Data Frames From all files
    for filePath in DataPorFilePaths:
        print("loading: "+"data/"+filePath)
        #dataframes = dataframes + LoadDataFromFile("data/ac_poor_1.bsad")
        dataframes = dataframes + LoadDataFromFile("data/"+filePath)

    #Merge All data Frames
    variables = ["DISA","ALTITUDE","MASS","TAS","FUELFLOW"]
    totalDataFrame = pd.DataFrame(columns=variables)
    for df in dataframes:
        #print(df.describe())
        totalDataFrame = totalDataFrame.append(df)

    print("Loaded Data:")
    print(totalDataFrame.describe())

    return(totalDataFrame)

def LoadDataRich():
    print("Loading DataRich...")
    #TODO


def CleanData(data):
    print("cleaning Data")
    #TODO

def IntepolateData(data,wantedPoints):

    dataPointCoordinates = data.get.to_numpy()
    dataPointValues = Y.to_numpy()
    #Make GRid for all point that want to be interpolated
    #grid_Disa, grid_ALTITUDE, grid_MASS, grid_TAS= np.mgrid[0:1000:10j, 0:1000:10j, 0:1000:10j, 0:1000:10j]
    interpolatePoints = np.array(wantedPoints)
    #grid_FUELFLOW = griddata(dataPointCoordinates, dataPointValues, (grid_Disa, grid_ALTITUDE, grid_MASS, grid_TAS), method='nearest')
    grid_FUELFLOW = griddata(dataPointCoordinates, dataPointValues, interpolatePoints, method='nearest')

    print(grid_FUELFLOW)
def PlotData(data):
    print("Ploting Data...")

def GetFuelFlow(disa,altitude,mass,tas):
    global airCraftData
    met = 'linear'
    #met = 'cubic'
    #met = 'nearest'
    variables = ["DISA","ALTITUDE","MASS","TAS"]
    predictor = ["FUELFLOW"]
    dataPointCoordinates = airCraftData[variables].to_numpy()
    dataPointValues = airCraftData[predictor].to_numpy()
    wantedPoint = [disa,altitude,mass,tas]
    interpolatePoints = np.array(wantedPoint)
    fuleFlow = griddata(dataPointCoordinates, dataPointValues, interpolatePoints, method=met)
    return(fuleFlow)

def main():
    global airCraftData
    airCraftData = LoadDataPoor()
    [disa,altitude,mass,tas] =  [-5.0,19000.0,12700.58636,456.0]
    fuleflow = GetFuelFlow(disa,altitude,mass,tas)

    print(str(disa) + " "+str(altitude) + " "+str(mass) + " "+str(tas) + " => " + str(fuleflow))


if __name__== "__main__":
    main()
