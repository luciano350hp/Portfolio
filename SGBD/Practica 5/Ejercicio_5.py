#!/usr/bin/python

# Imports necesarios
import numpy as np
import pandas as pd
from matplotlib import cm
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

#LEO EL CSV
data = pd.read_csv('dataset.csv')
#print(data.head())
#print(data.shape)

#Seleccionamos las variables independientes
X_multiple = data[['NS','surface_total_in_m2','rooms']]

#Defino la variable dependiente
y_multiple = data ['price']

#Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train, X_test, y_train, y_test = train_test_split(X_multiple, y_multiple, test_size=0)

#Defino el algoritmo a utilizar
lr_multiple = linear_model.LinearRegression()

#Entreno el modelo
lr_multiple.fit(X_train, y_train)

#Realizo una predicción
#Y_pred_multiple = lr_multiple.predict(X_test)

print('DATOS DEL MODELO REGRESIÓN LINEAL MULTIPLE')
print()
print('Valor de las pendientes o coeficientes "a": BETA 1, 2 Y 3')
print(lr_multiple.coef_)
print('Valor de la intersección o coeficiente "b" BETA 0:')
print(lr_multiple.intercept_)
print('Precisión del modelo: r-squared')
print(lr_multiple.score(X_train, y_train))
