import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("users.csv")

filtro = ((df["pais"].isin(["Canada", "Germany", "France"])) &

(df["edad"] >= 30) &
(df["nombre"].notnull()))
df_filtrado= df[filtro]

edad_promedio =df_filtrado.groupby("pais") ["edad"].mean()

colores=['lightgreen', 'red', 'gold']

edad_promedio.plot(kind="bar", color=colores)

plt.title("EDAD PROMEDIO: +30")
plt.xlabel("País")
plt.ylabel("Edad Promedio")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df= pd.read_csv("StudentsPerformance.csv")
conteos, bins =np.histogram(df["math score"], bins=10)
bin_centers =0.5* (bins[1:] + bins[:-1]) 
anchos=np.diff(bins) 
colores=['gold','lightcoral','lightskyblue','lightgreen','red','blue','pink','purple','yellow']
plt.figure(figsize=(8, 5))
plt.bar(bin_centers, conteos, width=anchos, color=colores, edgecolor='black')
plt.title("Distribución de puntajes de Matemáticas")
plt.xlabel("Puntaje")
plt.ylabel("Cantidad de estudiantes")
plt.grid(axis='y', linestyle=' ', alpha=0.7)
plt.tight_layout()
plt.show()
