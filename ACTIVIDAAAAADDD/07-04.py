ACTIVIDAD 1:

import pandas as pd
df=pd.read_csv ('StudentsPerformance.csv')
print(df[['gender',"math score"]])
print(df.head(40)) #Muestra las primeras filas
print(df.tail(15))  #Muestra las ultimas filas
print (df.shape) #Muestra la cantidad de filas y columnas
print(df.dtypes) #Muestra los tipos de datos de cada columna
print(df.mean()) #Muestra la media

ACTIVIDAD 2:
Abrir rl csv
Mostar las 3 ultimas columnas
Mostrar las primeras 100 filas
Mostrar la media, el minimo, maximo y cantidad
Convertir a string
