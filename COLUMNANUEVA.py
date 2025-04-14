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

COLUMNA CON NUMEROS ALEATORIOS
import pandas as pd
import numpy as np
df=pd.read_csv ('StudentsPerformance.csv')
a=np.random.randint(1,100,size=1000)
df['columna de arreglo']=a
print(df)

CREAR NUMEROS DECIMALES
import pandas as pd
import numpy as np
df=pd.read_csv ('StudentsPerformance.csv')
a=np.random.uniform(1,100,size=1000)
df['columna de arreglo']=a
print(df)

