import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import os 
from numpy.polynomial.polynomial import Polynomial 

#Leer los datos de la hoja de Excel 
df - pd.read_excel('fisica_computacional/cinematica/datos_mrua.xlsx', engine-'openpyx1') 

#Extraer las columnas de tiempo y espacio 
tiempo = df['Tiempo'].values 
espacio = df['Espacio'].values 

#Ajuste polinómico de segundo grado 
coeficientes = np.polyfit(tiempo, espacio, 2) 
polinomio = np.polyld(coeficientes) 

#Generar valores ajustados 
tiempo_fit = np.linspace(min(tiempo), max(tiempo), 100) 
espacio_fit = polinomio(tiempo_fit) 
 
#Imprimir la ecuación ajustada en la terminal 
print(f'Ecuación ajustada: y = {coeficientes[0]:.2f} * t^2 + (coeficientes[1]:.2f} * t + (coeficientes[2]:.2f}') 
 
#Graficar datos y ajuste 
plt.scatter(tiempo, espacio, color='red',label='Datos') 
plt.plot(tiempo_fit, espacio_fit, label-f'Ajuste Polinómico: y = {coeficientes[0]:.2f} * t^2 + {coeficientes[1]:.2f} * t + (coeficientes [2]:.2f}') 
plt.xlabel('Tiempo') 
plt.ylabel('Espacio') 
plt.title(f'Ajuste Polinómico: y = {coeficientes[0]:.2f} * t^2 + {coeficientes[1]:.2f} * t + (coeficientes [2]:.2f}') 
plt.legend() 
plt.grid() 


#Guardar la gráfica 
folder_path = 'fisica_computacional/cinematica' 
file_name = 'laboratorio_mrua.png' 
full_path = os.path.join(folder_path, file_name) 
plt.savefig(full_path) 
 
# Mostrar la grafica (si es necesario)
plt.show()
