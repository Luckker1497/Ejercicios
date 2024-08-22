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
print("La suma de 38 + 12 = ", sum) #Suma
print("La resta de 38 - 12 = ", res) #Resta
print("La division de 38 / 12 = ", div) #Division
print("La multiplicacion de 38 * 12 = ", mul) #Multiplicacion
print("El modulo de 38 % 12 = ", mod) #Modulo (El sobrante de la division)
print("El exponente de 10 ** 2 = ", exp) #Exponente (Las veces que cabe un numero en otro)
print("La division entera de 38 // 12 = ", dive) #Division Entera (Emite la parte demcimal)

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
my_number = 11 #asignacion
print(my_number)
my_number  += 1 #suma y asignacion
print(my_number)
my_number  -= 1 #Resta y asignacion
print(my_number)
my_number  *= 1 #Multiplicacion y asignacion
print(my_number)
my_number  /= 2 #Division y asignacion
print(my_number)
my_number  %= 2 #Exponente y asignacion
print(my_number)
my_number  **= 2 #Modulo y asignacion
print(my_number)
my_number  //= 1 #Division Entera y asignacion
print(my_number)

#Operadores de identidad (Compara 2 valores en memoria)
my_new_number = 2.0
n=my_new_number is my_number
n1=my_new_number is not my_number

print("El numero es igual al nuevo numero? ", n) #Dara false ya que ambos son numeros pero con diferentes posiciones de memoria
print("El numero es igual al nuevo numero? ", n1) #Dara true ya que ambos son numeros pero con mismas posiciones de memoria

#Operadores de pertenencia (Son aquellos donde buscan un caracter dentro de una palabra)
p = 'M' in 'Monica'
p1= 'N' not in 'Piscina'
p2= 'J' in 'Elefante'
print("Existe la letra M en Monica?", p)
print("La letra N existe en Piscina?", p1)
print("La letra J existe en Elefante?", p2)