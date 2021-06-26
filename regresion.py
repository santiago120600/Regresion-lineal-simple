import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y = [2,3,5,6,5]

promedio_x= sum(x) / len(x)
print("Promedio x: ",promedio_x);

promedio_y = sum(y) / len(y)
print("Promedio y: ",promedio_y);

xMenosPromedio = [] 
yMenosPromedio = [] 
xMenosXCuadrado = []

for valor in x:
    resta = valor - promedio_x
    xMenosPromedio.append(resta)

for valor in y:
    resta = valor - promedio_y
    yMenosPromedio.append(resta)

for valor in x:
    resultado = (valor - promedio_x)**2
    xMenosXCuadrado.append(resultado);

sumaCuadradosX = sum(xMenosXCuadrado)
print("Suma de los cuadrados",sumaCuadradosX)

print("X menos es promedio de x",xMenosPromedio)    
print("y Menos el promedio de y",yMenosPromedio)    
print("x menos el cuadrado",xMenosXCuadrado);

#Multiplicar el resultado de x menos el promedio de x y y menos el promedio de y
multiplicacionXyY = list(np.multiply(xMenosPromedio,yMenosPromedio)) 
print("Lista resultado de la multi",multiplicacionXyY)
sumaResultadoMultiplicacion = sum(multiplicacionXyY)
print("Resultado de sumar los elementos de la lista de la multiplicacion",sumaResultadoMultiplicacion)

w1 = sumaResultadoMultiplicacion / sumaCuadradosX 
print(w1)

# y = w0 +w1x
#obtener w0
w0 = -1*w1*promedio_x + promedio_y
print("w0 ", w0)
#obtener linea de regresion
linea_regresion = []
regresion_x = []
rango_regresion = 11
for valor_x in range(1,rango_regresion):
    valor_y = w0 + w1*valor_x
    regresion_x.append(valor_x)
    linea_regresion.append(valor_y)

print("linea regresión: ",linea_regresion)

# Graficar
plt.plot(x, y, label="Data")
plt.plot(regresion_x, linea_regresion, label="Linear Regression")
plt.legend()
plt.show()
