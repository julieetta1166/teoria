GRAFICO LINEAL
import matplotlib.pyplot as plt #importar libreria
x=[ 1, 2,3,4,5]   #datos
y=[ 11, 16, 20,13, 17] #datos
plt.plot(x,y) #crear grafico
plt.xlabel('eje x') #etiqueta
plt.ylabel('eje y') #etiqueta
plt.title('Grafico de ejemplo') #titulo
plt.show() #mostrar graficos

GRAFICO CIRCULAR
import matplotlib.pyplot as plt #importar libreria
label=[ 'a','b','c','d']   #datos
datos=[ 25,35,20,20] #datos
colores=['gold','lightcoral','lightskyblue','lightgreen']
plt.pie(datos,labels=label,colors=colores,autopct='%1.1f%%',startangle=140)
plt.axis('equal')
plt.show()
