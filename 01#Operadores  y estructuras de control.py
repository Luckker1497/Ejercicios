"""
Operadores y estructuras de control

"""

#Ejercicios Aritmeticos
num1 = 38
num2 = 12
sum = num1 + num2
res = num1 - num2
div= num1 / num2
mul = num1 * num2
mod= num1 % num2
exp= num1 ** num2
dive = num1 // num2
print("La suma de 38 + 12 = ", sum)
print("La resta de 38 - 12 = ", res)
print("La division de 38 / 12 = ", div)
print("La multiplicacion de 38 * 12 = ", mul)
print("El modulo de 38 % 12 = ", mod)
print("El exponente de 38 ** 12 = ", exp)
print("La division entera de 38 // 12 = ", dive)

#Operadores de comparacion
igual = 15==3
desigual = 54 != 56
mayor = 32 >= 23
menor = 45<=44
print ("¿10 == 3? ", igual)
print ("¿54 != 56? ", desigual)
print ("¿32 >= 23? ", mayor)
print ("¿45 <= 44? ", menor)

#Operadores logicos
y = 10 - 4 == 6
o = 47 + 32 == 57
n = not 42 + 2 == 29

print("AND ¿10 - 4 es = 6? AND 42 + 2 = 29", y and o ) #Se debe cumplir ambas operaciones
print("OR ¿10 - 4 es = 6? OR 42 + 2 = 29", y or n ) #se debe cumplir al menos una
print("NOT  42 + 2 = 29",  n ) #Al negarlo se convierte en verdadero

#Operadores de asignacion
my_number = 11


