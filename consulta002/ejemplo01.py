# if y else son estructuras de control de flujo que permiten realizar decisiones en el código.
numero = int(input("Ingresa un munero: "))
if numero > 0:
    print("El número es positivo.")
else:
    print("El número es negativo")

#Puedes usar if y else para manejar múltiples condiciones con elif(agregar mas deciciones )
numero = int(input("Ingresa un munero: "))
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")