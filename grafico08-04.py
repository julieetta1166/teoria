GRAFICO BASICO
import matplotlib.pyplot as plt #importar libreria
x=[ 1, 2,3,4,5]   #datos
y=[ 11, 16, 20,13, 17] #datos
plt.plot(x,y) #crear grafico
plt.xlabel('eje x') #etiqueta
plt.ylabel('eje y') #etiqueta
plt.title('Grafico de ejemplo') #titulo
plt.show() #mostrar graficos
