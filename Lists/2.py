'''
    Cargar una lista con numeros al azar de cuatro digitos. La cantidad de elementos
    tambien sera un numero al azar de dos digitos.
    Eliminar todas las apariciones de un valor en la lista anterior. El valor a
    eliminar se ingresa desde el teclado y la funcion lo recibe como parametro.
    Determinar si el contenido de una lista cualquiera es capicua, sin usar listas
    auxiliares.
'''

import random

def createList(quantity):
    newList = []
    cont = 0
    while cont < quantity:
        newElement = random.randint(0, 9999)
        newList.append(newElement)
        cont += 1;
    return newList

def deleteElementAppearances(element, list):
    i = 0;
    while i < len(list):
        if element == list[i]:
            list.remove(element)
        else:
            i += 1

def isPalindrome(list):
    isListPalindrome = True
    i = 0
    j = -1
    lenght = len(list)
    cont = 0
    while cont < lenght:
        if list[i] != list[j]:
            isListPalindrome = False
        else:
            i += 1
            j -= 1
            lenght = lenght / 2
        cont += 1
            
    return isListPalindrome
    

def main():
    numElements = random.randint(1,9)
    listCreated = createList(numElements)
    print(listCreated)

    fakeList = [1,3,4,3,2,4,3,9,12] # to check deleteElementAppearences function.
    print(fakeList)
    deleteElement = int(input('Delete an element from the List: '))
    deleteElementAppearances(deleteElement, fakeList)
    print(fakeList)


    fakeList2 = [22,3,4,3,22] # to check isPalindrome function.
    print(fakeList2)
    print(isPalindrome(fakeList2))

main()