#encuentra el cuadrante

x = int (input(" Introducir coordenada en X: "))
y = int (input(" Introducir coordenada en Y: "))

if((x > 0) and (y > 0)):
    print("se encuentra en el primer cuadrante")

elif((x < 0) and (y > 0)):
    print("se encuentra en el segundo cuadrante")

elif((x < 0) and (y < 0)):
    print("se encuentra en el tercer cuadrante")

elif((x > 0) and (y < 0)):
    print("se encuntra en el cuarto cuadrante")

else:
    print("punto en el origen")

######################################
#longitud de una frase

palabra = input("¡Hola! Introduce una palabra: ")
print(len(palabra))



if len(palabra) == 4 :
    print("Palabra correcta")
if len(palabra) == 5 :
    print("Palabra correcta")
if len(palabra) == 6 :
    print("Palabra correcta")
if len(palabra) == 7 :
    print("Palabra correcta")
if len(palabra) == 8 :
    print("Palabra correcta")
elif len(palabra) < 4 :
    print("Hacen falta letras")
elif len(palabra) > 8 :
    print("Sobran letras")