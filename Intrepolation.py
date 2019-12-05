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

def LoadData():
    #LOAD DATA
    with open("data/ac_poor_1.bsad", "r") as fin:
        ac_data = json.loads(fin.read())

    tables = ac_data["tables"]
    dataframes = []

    for table in tables:
        if table["header"]["flightphase"] == "cruise":
            cols = table["header"]["variables"]
            data = table["table"]
            dataframes.append(pd.DataFrame(data, columns=cols))

    #Merge All data Frames
    print(len(dataframes))
    mesureRun = dataframes[1]

    variables = ["DISA","ALTITUDE","MASS","TAS"]
    predictor = ["FUELFLOW"]

    X = pd.DataFrame(mesureRun.get(variables), columns=variables)
    Y = pd.DataFrame(mesureRun.get(predictor), columns=predictor)
    return(X,Y)


def CleanData(data):
    print("cleaning Data")

def Intepolation(wantedPoint,dataType):

    [X,Y] = LoadData()

    variables = ['DISA','ALTITUDE','MASS','TAS']
    predictor = ['FUELFLOW']

    dataPointCoordinates = X.to_numpy()
    dataPointValues = Y.to_numpy()
    #Make GRid for all point that want to be interpolated
    #grid_Disa, grid_ALTITUDE, grid_MASS, grid_TAS= np.mgrid[0:1000:10j, 0:1000:10j, 0:1000:10j, 0:1000:10j]
    interpolatePoints = np.array([0,0,0,0])
    #grid_FUELFLOW = griddata(dataPointCoordinates, dataPointValues, (grid_Disa, grid_ALTITUDE, grid_MASS, grid_TAS), method='nearest')
    grid_FUELFLOW = griddata(dataPointCoordinates, dataPointValues, interpolatePoints, method='nearest')

    print(grid_FUELFLOW)

def main():
    dataSet = "Por"
    wantedPoint = [0,0,0,0]
    Intepolation(wantedPoint,dataSet)

if __name__== "__main__":
    main()
