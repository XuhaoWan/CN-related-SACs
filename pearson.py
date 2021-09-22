#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan

import numpy as np
from sklearn.preprocessing import MinMaxScaler

data_train = np.loadtxt('mfeatures.csv', delimiter=",", dtype="float")
x = data_train
ss = MinMaxScaler()
x = ss.fit_transform(x)

np.savetxt("prcor.csv", x, delimiter=',')

