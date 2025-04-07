COMO CREAR FILAS Y COLUMNAS
import numpy as np
import pandas as pd
provincia=['Cordoba', 'Mendoza', 'Santa Fe', 'Buenos Aires']
poblacion=[ '700', '800', '900', '1000']
diccionario= {"PROVINCIA":provincia,"POBLACION":poblacion}
df= pd.DataFrame (diccionario)
print (df)

COMO ABRIR UN CSV 
import pandas as pd
df=pd.read_csv ('StudentsPerformance.csv')
print(df)
