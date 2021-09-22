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


data_train = np.loadtxt('ORRconstruction.csv', delimiter=",", dtype="float")
data_pre = np.loadtxt('ORRpre.csv', delimiter=",", dtype="float")
x = data_train[..., 0:15 ]
ss = MinMaxScaler()
x = ss.fit_transform(x)
y = data_train[...,15 ]

x_pre = data_pre[..., 0:15 ]
x_pre = ss.fit_transform(x_pre)


model = RFR(n_estimators = 200)
model.fit(x, y)

rmse = np.sqrt(mse(y, model.predict(x)))
r2 = r2_score(y, model.predict(x))
y_pre = model.predict(x_pre)
np.savetxt("pre.csv", y_pre, delimiter=',')
#rmset = np.sqrt(mse(ytest[j], model.predict(xtest[j])))
#r2t = r2_score(ytest[j], model.predict(xtest[j]))
#print('pre:', model.predict(x_pre))
#print(y)
print(rmse)
print(r2)
#print(rmset)
#print(r2t)
print(model.feature_importances_)
np.savetxt("FI.csv", model.feature_importances_, delimiter=',')