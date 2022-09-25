entrada = input("¡Hola! Introduce tu edad: ")

edad = 0

if entrada.isnumeric() :
    edad = int(entrada)
else :
    print("dato incorrecto. Debes introducir un número")
    exit()

if edad <= 0 :
    print("WOOOOWWW!! que joven eres, pero, lo siento  eso no es posible")
elif edad > 115 :
    print(" vaya!!!  ¿Cómo le haces para vivir tanto? No te creo, mejor intenta nuevamente")
elif edad < 18 :
    print(" Erese menor de edad asi que no puedes comprar tu cigarro")
else :
    print("eres mayor de edad. Aqui tienes tu cigarro")



