import json
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

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

mesureRun = dataframes[1]

variables = ["DISA","ALTITUDE","MASS","TAS"]
predictor = ["FUELFLOW"]

X = pd.DataFrame(mesureRun.get(variables), columns=variables)
Y = pd.DataFrame(mesureRun.get(predictor), columns=predictor)

print(X.describe())
print(Y.describe())

reg = LinearRegression().fit(X, Y)
print("Regreasaion Score: ")
print(reg.score(X, Y))

#Plot
#variables = ["DISA","ALTITUDE","MASS","TAS"]

plot = [1]
conts = [2,3,4]

plotVariable = variables[plot]
predictor = ["FUELFLOW"]
#keep const
varKeepConst = variables[const]
konst = [100,100,100];

plotVariableArr = X.get(plotVariable)

modelPred = reg.predict(X)

plt.scatter(plotVariableArr, Y.get(predictor),  color='black')

#plt.plot(X.get(plotVariable), modelPred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
