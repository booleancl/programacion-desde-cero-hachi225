# Las variables en python se declaran y asignan en una sola linea
# La declaracion entrega su nombre y le asigna su valor

num_one = 1
num_two = 2
num_three = num_one + num_two

print(num_three)

num_two = 5
num_four = num_one + num_two

print(num_four)

print(5/2) # Python automáticamente agrega el decimal 
print(5.0/2)
print(5+2*5) #Precedencia clásica, primero la multiplicación
print(2**5) #Potencias
print(5%2) # Resto de una división (módulo '%')
print(1/0.3) # Muchos decimales

true_value = True
false_value = False
minus_one = 3**1/4

if minus_one:
    print("Esto se ejecutara")
else:
    print("Entonces este se ejecutara")
    print("Esto es parte del if")
print("Esto no es parte del if")