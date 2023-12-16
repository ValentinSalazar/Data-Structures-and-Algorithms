'''
    Generar una lista de 50 numeros aleatorios del 1 al 100.
    Recibir una lista como parametro y devolver True si la misma contiene
    algun elemento repetido. La funcion NO debe modificar la lista.
    Recibir una lista como parametro y devolver una nueva lista con los
    elementos unicos de la lista original, sin importar el orden.
'''
import random

def createList():
    cont = 0
    newList = []
    while cont < 5:
        element = random.randint(1,10)
        newList.append(element)
        cont += 1
    return newList

def hasRepeatedElements(list):
    hasRepeated = False
    
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                hasRepeated = True
                                   
    return hasRepeated

def listWithNoRepeats(list):
    listWithNoRepeats = []

    for i in range(len(list)):
        if list.count(list[i]) <= 1:
            listWithNoRepeats.append(list[i])
    
    return listWithNoRepeats


def main():
    listCreated = createList()
    print(listCreated)

    print(hasRepeatedElements(listCreated))

    print(listWithNoRepeats(listCreated))
main()