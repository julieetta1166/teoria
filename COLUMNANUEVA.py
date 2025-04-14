COLUMNA NUEVA
import pandas as pd
df=pd.read_csv ('StudentsPerformance.csv')
df['nueva columna']= 70
print(df)

COLUMNA DE ARREGLO
import pandas as pd
import numpy as np
df=pd.read_csv ('StudentsPerformance.csv')
a=np.arange(0,1000)
df['columna de arreglo']=a
print(df)
