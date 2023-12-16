'''
    Crear una lista de los cuadrados de los numeros entre 1 y N (ambos incluidos),
    donde N se ingresa desde el teclado. Luego se solicita imprimir los ultimos
    10 valroes de la lista.
'''
def typeAnumber():
    newNumber = int(input("Type a Number: "))
    return newNumber

def createList(number):
    newList = []
    for i in range(1, number+1):
        newList.append(i**2)
    return newList

def main():
    numberTyped = typeAnumber()
    listCreated = createList(numberTyped)
    print(listCreated)
main()