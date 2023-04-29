nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

magos = []
cientificos = []
otros = []

# Clasificar los nombres en grupos
for nombre in nombres:
    if nombre in ['Harry Houdini', 'David Blaine', 'Teller']:
        magos.append(nombre)
    elif nombre in ['Newton', 'Hawking', 'Einstein']:
        cientificos.append(nombre)
    else:
        otros.append(nombre)

# definir la función hacer_grandioso()
def hacer_grandioso():
    for i in range(len(magos)):
        magos[i] = 'El gran ' + magos[i]

# definir la función imprimir_nombres()
def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre)

# imprimir la lista completa de nombres
print("Lista completa de nombres:")
imprimir_nombres(nombres)
print()

# hacer grandiosos a los magos
hacer_grandioso()

# imprimir los magos grandiosos
print("Magos grandiosos:")
imprimir_nombres(magos)
print()

# imprimir los científicos
print("Científicos:")
imprimir_nombres(cientificos)
print()

# imprimir los otros nombres
print("Otros:")
imprimir_nombres(otros)
