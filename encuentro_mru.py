#Script encuentro dos cuerpos mru 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import os 
from sympy import symbols, Eq, solve 
 
# Definir la variable t para SymPy 
t = symbols('t') 
 
# Definir las ecuaciones de movimiento 
x1 = 35 * t 
x2 = 1000 - 20 * t 
 
# Posibles soluciones (x1=x2) 
equation = Eq(x1, x2) 
soluciones = solve(equation, t) 
print(f'Las soluciones posibles son {soluciones}') 
 
# Solución problema 
encuentro_t = float(soluciones[0]) 
encuentro_x = 35 * encuentro_t 
 
print(f'El tiempo de encuentro es {encuentro_t:.2f} segundos') 
print(f'El lugar de encuentro es {encuentro_x:.2f} metros') 
 
# Definir parámetros del movimiento 
t_max = 30 # Tiempo máximo (s) 
dt = 1     #  Intervalo de tiempo (5) 
 
# Crear el array de tiempos 
ti = np.arange(0, t_max + dt, dt) 
 
# Evaluar las ecuaciones de movimiento usando el array de tiempos 
x1 = 35 * ti 
x2 = 1000 - 20 * ti 

# Crear una tabla con Pandas 
tabla = pd.DataFrame({'Tiempo (s)': ti, 'Posición Cuerpo 1 (m)': x1, 'Posición Cuerpo 2 (m)': x2}) 
print(tabla)

#Gráfica de posiciones 
plt.figure(figsize=(8, 5)) 
plt.plot(ti, x1, 'bo-', label='Cuerpo 1: $x_1 = 35t$') 
plt.plot(ti, x2, 'ro-', label='Cuerpo 2: $x_2 1000 20t$') 
plt.scatter (encuentro_t, encuentro_x, color='green', zorder=3, label=f'Encuentro ({encuentro_t:.2f} s, {encuentro_x:.2f} m)') 
plt.xlabel('Tiempo (s)') 
plt.ylabel('Posición (m)') 
plt.title('Movimiento de dos cuerpos hacia el encuentro') 
plt.legend() 
plt.grid() 
 
#Guardar la gráfica 
folder_path = 'fisica_computacional/cinematica' 
file_name = 'encuentro_mru.png 
full_path = os.path.join(folder_path, file_name) 
plt.savefig(full_path) 
 
# Mostrar la gráfica (si es necesario) 
plt.show()
