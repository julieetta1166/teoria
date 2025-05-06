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
