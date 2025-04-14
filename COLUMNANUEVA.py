COLUMNA NUEVA
import pandas as pd
df=pd.read_csv ('StudentsPerformance.csv')
df['nueva columna']= 70
print(df)
