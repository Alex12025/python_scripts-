#Estudio mrua 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import os 

# Parámetros del MRUA 
x0 = 0      # Posicion inicial (m)
v0 = 2      # Velocidad inicial (m/s)
a = 5       # Aceleracion (m/s²)
t_max = 10  # Tiempo maximo (s)
dt = 1      # Intervalo de tiempo (s)
 
# Crear el array de tiempos 
t = np.arange(0, t_max + dt, dt) 

# Calcular la posición en cada instante de tiempo 
x = x0 + v0 * t + 0.5 * t**2 

# Calcular la velocidad en cada instante de tiempo 
v = v0 +a * t 

# Crear una tabla con Pandas 
tabla = pd.DataFrame({'Tiempo (s)': t, 'Posición (m)': x, 'Velocidad (m/s)': v}) 
print(tabla) 

# Gráfica x-t (Posición vs Tiempo) 
plt.figure(figsize=(10, 4)) 

plt.subplot(1, 2, 1) 
plt.plot(t, x, 'bo-', label="Posición $x = x_0 + v_0t + \\frac{1}{2}at^2$") 
plt.xlabel("Tiempo (s)") 
plt.ylabel("Posición (m)") 
plt.title("Gráfica x-t (MRUA)") 
plt.legend() 
plt.grid() 
 
# Gráfica v-t (Velocidad vs Tiempo) 
plt.subplot(1, 2, 2) 
plt.plot(t, v, 'ro-', label="Velocidad $v = v_0 + at$") 
plt.xlabel("Tiempo (s)") 
plt.ylabel("Velocidad (m/s)") 
plt.title("Gráfica v-t (MRUA)") 
plt.legend()
