#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan


import numpy as np
from sklearn.kernel_ridge import KernelRidge as KRR
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


data_train = np.loadtxt('ORRconstruction.csv', delimiter=",", dtype="float")
x = data_train[..., 0:15 ]
ss = MinMaxScaler()
x = ss.fit_transform(x)
y = data_train[...,15 ]


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=21, random_state=4)

params = {'alpha': 1,
          'kernel': 'linear',
          'gamma': 0,
          'degree': 3,
          'coef0': '1'}

model = KRR(**params)
model.fit(x_train, y_train)

rmse = np.sqrt(mse(y_train,model.predict(x_train)))
r2 = r2_score(y_train,model.predict(x_train))
rmset = np.sqrt(mse(y_test,model.predict(x_test)))
r2t = r2_score(y_test,model.predict(x_test))
print('pre:', model.predict(x_test))
print(y_test)
print(rmse)
print(r2)
print(rmset)
print(r2t)