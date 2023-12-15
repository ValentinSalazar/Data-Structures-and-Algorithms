'''
    Solicita al usuario numeros enteros, alojalos en una lista y
    realizar la suma de todos los elementos.
    Ademas, obtener el promedio de todos sus elementos, mostrar por
    pantalla el elemento mas grande y mas chico de la lista.
'''


def createList():
    newList = []
    element = int(input("Type a number(-1 to exit): "))
    while element != -1:
        newList.append(element)
        element = int(input("Type another number(-1 to exit): "))
    return newList

def sumElements(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

def avgElements(list):
    return sumElements(list) / len(list)

def maxAndMinElements(list):
    max = list[0]
    min = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
        if list[i] < min:
            min = list[i]

    return max, min

def main():
    listCreated = createList()
    print(listCreated)

    sumList = sumElements(listCreated)
    print(f'Sum is {sumList}')

    average = avgElements(listCreated)
    print(f'Average {average}')
    
    maxElement, minElement = maxAndMinElements(listCreated)
    print(f'Max Element {maxElement} and Min Element {minElement}')


main()

