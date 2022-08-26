# texto_variado ="palabra 123 +-* #%&"
# print(type(texto_variado))

# #podemos utilizar comillas triples para que el texto se muestre como la cadena que hemos escrito
# print("""
# funcionamiento de \
# programa: (opciones)
#   -1 Para acceder a opciones
#       -2 Para salir
# """)

###########################################

#subscripting e indexado

# texto = "Python"

# print(texto[0])
# print(texto[5])
# print(texto[-1])
# print(texto[-6])

# print(texto[6]) # error no podemos acceder a una psocion que no existe
# print(texto[-7]) # error no podemos acceder a una psocion que no existe

# letra = texto[0]
# print(letra)

# #texto[0] = "P" #error no podemos modificar una cadena

# letra = "p"
# print(letra)

# texto_compuesto = letra + texto[1] #concatenación
# print(texto_compuesto) 

####################################################################################

#slicing o substringing
texto = "Python"
# print(texto[0:3])
# print(texto[0:-3])
# print(texto[0:-2])
# print(texto[2:])
# print(texto[:3])

# print(texto[-3::-1])

# print(texto[::-1])
# print(texto[1:50])
# print(texto[2:2])

#######################################################################
#cadenas y formatos

texto = "Hola mundo! Buenastardes"
# print(texto.lower())
# print(texto.upper())
# print(texto.capitalize())
# print(texto.title())
# print(texto.swapcase())
# # texto = texto.upper()
# print(texto)

print("{} + {} = {}".format(2, 3, 2+3))
print("{} + {} = {}".format("Hola", "mundo", "Hola mundo"))
print("{:.3f} + {:.4f} = {}".format(2, 3, 2+3))
print("{1} + {0} = {2}".format(2, 3, 2+3))
print("{2} + {0} = {1}".format("Hola", "mundo", "Hola mundo"))
print("{:d} = {:b} = {:o} = {:x}".format(15, 15, 15, 15))

