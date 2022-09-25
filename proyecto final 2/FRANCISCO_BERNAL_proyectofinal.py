#encuentra el cuadrante
#iniciamos con este tarea ya que un poco parecido al anterior basndo y siguiendo las instruciones como viene en el doc que nos enviaron

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
#al ser una palabra cosrta decidi hacelo el if cuando el rango es pequeño y asi saliera el mensaje de palabra correcta
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