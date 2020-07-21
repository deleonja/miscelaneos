'''
Autor: José Alfredo de León
20.07.2020

Script de python muy básico para ejemplificar cómo hacer
gráficas.
'''

# Importar módulo matplotlib.pyplot para poder utilizar funciones
# de graficación
import matplotlib.pyplot as plt
# Importar numpy para poder utilizar arreglos eficientes (en
# comparación de las listas culeras de Python)
import numpy as np

# Definir la función que se desea graficar utilizando funciones de
# numpy.
def x_t(x):
    return np.exp(-0.1*x)*np.sin(x)

# Crear un arreglo con todos los puntos de t (busar documentación
# de numpy para entender a fondo qué hace np.linspace, también
# podría utilizarse np.arange)
t = np.linspace(0, 100, 1000)

# Crear un arreglo con todos los valores de x(t), utilizando la
# función definida arriba
x = x_t(t)

# Utilizar la función plot de matplotlib.pyplot para graficar la curva
# revisar la documnetación para entender todo lo que tiene plt.plot
plt.plot(t, x, '-k', lw=1.2, label=r'$x(t)=e^{-x}\sin (x)$')
# Colocar la leyenda con el label de la curva graficada arriba
plt.legend(loc='best')
# Colocarle grilla a la gráfica, modificando lw se modifica el grosor
# de línea
plt.grid('--k', lw=0.1)
# Label de y
plt.ylabel('x(t)')
# Label de x
plt.xlabel('t')
# Guardar la gráfica. Yo prefiero guardar mis imágenes como PDF porque
# son más livianas (evitan que overleaf se crashee, si es que lo utilizan
# para LaTex) y la definición de la imagen no se pierde.
plt.savefig("graph-example.pdf")
# Mostrar la gráfica. Sin esto no se muestra la gráfica.
plt.show()
