import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score



data_train = np.loadtxt('24.csv', delimiter=",", dtype="float")
x = data_train[..., 0:15 ]
y = data_train[...,15 ]

print(y)
def stderror_func(y_pre, y):
    return  np.sqrt(np.mean(y_pre-y)**2)
cft = linear_model.LinearRegression()

cft.fit(x, y)

print('model coefficient', cft.coef_)
print('model intercept', cft.intercept_)

y_pre = cft.predict(x)

rmse = np.sqrt(mse(y, y_pre))
stde = stderror_func(y_pre, y)
print(rmse)
print(stde)
