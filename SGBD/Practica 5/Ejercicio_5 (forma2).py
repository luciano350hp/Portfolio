#!/usr/bin/python

# Imports necesarios
import pandas as pd
from sklearn import linear_model

#LEO EL CSV
data = pd.read_csv('dataset.csv')
#print(data.head())
#print(data.shape)

#Seleccionamos las variables independientes
X = data[['NS','surface_total_in_m2','rooms']]

#Defino la variable dependiente
Y = data ['price']

# Split the data into training/testing sets
X_train = X[:-20]
X_test = X[-20:]

# Split the targets into training/testing sets
y_train = Y[:-20]
y_test = Y[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = regr.predict(X_test)
print (y_pred)
# The coefficients
print('Coeficientes: BETA 1, 2 Y 3 \n', regr.coef_)
print('Valor de la intersección o coeficiente "b" BETA 0:')
print(regr.intercept_)
print('Precisión del modelo: r-squared')
print(regr.score(X_train, y_train))
