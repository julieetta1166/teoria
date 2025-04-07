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

#COMO MOSTRAR LAS FILAS
import pandas as pd
df=pd.read_csv ('StudentsPerformance.csv')
print(df.head(20)) #Mostrar las primeras filas
print(df.tail())  #Mostrar las ultimas filas
print(df.to_string()) #Mostrar todo
