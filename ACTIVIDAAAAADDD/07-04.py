ACTIVIDAD 1:
Abrir archivo csv
Mostrar la columna gender maxcore
Mostrar la cantiddad de fila y columna que tiene
Mostrar las primeras 40 filas
Mostrar las ultimas 15 lineas
Mostrar la media
Mostrar los tipos de datos de cada columna 

import pandas as pd
df=pd.read_csv ('StudentsPerformance.csv')
print(df[['gender',"math score"]])
print(df.head(40)) #Muestra las primeras filas
print(df.tail(15))  #Muestra las ultimas filas
print (df.shape) #Muestra la cantidad de filas y columnas
print(df.dtypes) #Muestra los tipos de datos de cada columna
print(df.mean()) #Muestra la media

ACTIVIDAD 2:
Abrir el csv
Mostar las 3 ultimas columnas
Mostrar las primeras 100 filas
Mostrar la media, el minimo, maximo y cantidad
Convertir a string

import pandas as pd
df=pd.read_csv ('StudentsPerformance.csv')
print(df[['gender',"math score"]])
print(df[['gender','lunch','math score']].head) #Como mostrar dos columnas
print(df.head(100)) #Muestra las primeras filas
print(df.cant())
print(df.max())
print(df.min())
print(df.mean()) #Muestra la media
