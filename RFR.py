#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan

import numpy as np
from sklearn.tree import DecisionTreeRegressor as DTR
from sklearn.ensemble import RandomForestRegressor as RFR
from sklearn.ensemble import ExtraTreesRegressor as ETR
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import KFold

data_train = np.loadtxt('OERconstruction.csv', delimiter=",", dtype="float")
x = data_train[..., 0:15 ]
ss = MinMaxScaler()
x = ss.fit_transform(x)
y = data_train[...,15 ]

kf = KFold(n_splits=4, shuffle=True, random_state=1)
i = 0
xtrain = {}
xtest = {}
ytrain = {}
ytest = {}
for train, test in kf.split(x):
    xtrain[i] = x[train]
    xtest[i] = x[test]
    ytrain[i] = y[train]
    ytest[i] = y[test]
    i+=1

for j in range(1):
    model = RFR(n_estimators = 200)
    model.fit(xtrain[j], ytrain[j])

    print('iteration:', j)
    #rmse = np.sqrt(mse(ytrain[j], model.predict(xtrain[j])))
    #r2 = r2_score(ytrain[j], model.predict(xtrain[j]))
    rmset = np.sqrt(mse(ytest[j], model.predict(xtest[j])))
    r2t = r2_score(ytest[j], model.predict(xtest[j]))
    print(ytrain[j])
    print(model.predict(xtrain[j]))
    print(ytest[j])
    print(model.predict(xtest[j]))
    np.savetxt("ytain.csv", ytrain[j], delimiter=',')
    np.savetxt("ytainp.csv", model.predict(xtrain[j]), delimiter=',')
    np.savetxt("ytest.csv", ytest[j], delimiter=',')
    np.savetxt("ytestp.csv",model.predict(xtest[j]), delimiter=',')
    # print('pre:', model.predict(xtest[j]))
    # print(ytest[j])
    # print(rmse)
    # print(r2)
    print(rmset)
    print(r2t)
    #print(model.feature_importances_)