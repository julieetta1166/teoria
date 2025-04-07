#COMO CREAR FILAS Y COLUMNAS
import numpy as np
import pandas as pd
provincia=['Cordoba', 'Mendoza', 'Santa Fe', 'Buenos Aires']
poblacion=[ '700', '800', '900', '1000']
diccionario= {"PROVINCIA":provincia,"POBLACION":poblacion}
df= pd.DataFrame (diccionario)
print (df)

#COMO ABRIR UN CSV 
import pandas as pd
df=pd.read_csv ('StudentsPerformance.csv')
print(df)

#FUNCIONES
import pandas as pd
df=pd.read_csv ('StudentsPerformance.csv')
print(df.head(20)) #Mostrar las primeras filas
print(df.tail())  #Mostrar las ultimas filas
print(df.to_string()) #Mostrar todo
print (df.shape) #Muestra la cantidad de filas y columnas
print(df.dtypes)#Muestra los tgipos de datos de cada columna
print(df.mean()) #Muestra la media
print(df.info())  #Muestra las filas para limpiar los datos non-null(incompletas)
print(df.describe())#Muestra datos estadisticos de la tabla en general
print(df["gender"].head) #Muestra la columna que pidamos
print(df[['gender','lunch']].head) #Como mostrar dos columnas
