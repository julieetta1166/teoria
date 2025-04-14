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

SUMAR VARIAS COLUMNAS
import pandas as pd
import numpy as np
df=pd.read_csv ('StudentsPerformance.csv')
print(df['math score']+ df['reading score']+ df['writing score'] )#SUMAR TRES COLUMNAS
CREAR NUMEROS DECIMALES
import pandas as pd
import numpy as np
df=pd.read_csv ('StudentsPerformance.csv')
a=np.random.uniform(1,100,size=1000)
df['columna de arreglo']=a
print(df)

SUMANDO LOS NUMEROS DE LA COLUMNA DE MATH SCORE
import pandas as pd
import numpy as np
df=pd.read_csv ('StudentsPerformance.csv')
print(df['math score'].sum)
print(df.head) 

FUNCIONES
import pandas as pd
import numpy as np
df=pd.read_csv ('StudentsPerformance.csv')
print(df['math score'].sum) #suma
print(df['math score'].count) #cuenta las filas
print(df['math score'].mean) 
print(df['math score'].std) #estandar
print(df.head) 
