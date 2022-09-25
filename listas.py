#primer ejemplo de lista
# mix = [0, 1.0, "dos", 3 + 4j]

# for i in mix :
#     print(f"{i:6} - Tipo: {type(i)}")

#segundo ejemplo de lista
# mix = [0, 1.0, "dos", 3 + 4j]

# sin_dos = mix[:2] + mix[3:]

# print(mix, sin_dos)

#para duplicar
# duplicado = mix * 3
# print(duplicado)

#para elevadas al cuadrado

# cuadrados = [0, 1, 4, 9, 16, 25]
# for i in range(len(cuadrados)) :
#     print(f"{i}**2 = {cuadrados[i]}")

#para elevadas al cubo
cuadrados = [0, 1, 4, 9, 16, 25]
for i in range(len(cuadrados)) :
    cuadrados[i] = cuadrados[i] *i
    print(f"ahora están al cubo {cuadrados[i]}")

cuadrados.append(7 ** 3)

cuadrados.insert(6, 6 ** 3)

cuadrados.extend([27, 1000, -1])

cuadrados.extend(range(-1, -4, -1))

print(cuadrados)

del cuadrados[9:]   #eliminar valores hasta el rango que le indiquemos

print(cuadrados)

cuadrados.remove(27)

print(cuadrados)

valor_removido = cuadrados.pop(2)

print(valor_removido)

print(cuadrados)

cuadrados.clear()

print(cuadrados)
 

