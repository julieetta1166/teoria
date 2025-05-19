19-05-25
Prueba
1. Obtener el nombre de todos los usuarios mayores a 20 años de los siguintes paises: España, Francia y Turquia. Cuantos son masculinos y cvuiatos femeninos, y graficar

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('users.csv')

paises_objetivo = ['Spain', 'France', 'Turkey']
filtro = (df['edad'] > 20) & (df['pais'].isin(paises_objetivo))
usuarios_filtrados = df[filtro]

nombres = usuarios_filtrados['nombre'].tolist()
print("Nombres de usuarios filtrados:")

conteo_genero = usuarios_filtrados['genero'].value_counts()
print("Conteo por género:")
print(conteo_genero)

plt.figure(figsize=(6, 4))
conteo_genero.plot(kind='bar', color=['skyblue', 'pink'])
plt.title('Distribución de Género (Usuarios >20 años en España, Francia y Turquía)')
plt.xlabel('Género')
plt.ylabel('Cantidad')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

2. Obtener todos los usuarios entre las edades de 45 y 60. Cuntos son asculinos y cuantos son femeninos, hacer un grafico con matlobit
