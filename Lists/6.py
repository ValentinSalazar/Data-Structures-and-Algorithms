'''
    Escribir una funcion que reciba una lista como parametro y devuelva True
    si la lista esta ordenada de forma ascendente o False en caso contrario.
    Por ejemplo, ordenada([1,2,3]) retorna True y ordenada(['b', 'a']) False.
    Desarrollar ademas un programa para verificar el comportamiento de la funcion.
'''

def isOrdered(list):
    newList = list.copy()
    newList.sort()

    return newList == list

def isOrdered2(list):
    validateOrder = True
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            validateOrder = False
    return validateOrder

def main():
    
    # print(isOrdered([1,2,3,4,5,6]))
    # print(isOrdered([7,2,3,4,25,6]))
    # print(isOrdered(['b', 'a']))
    print(isOrdered2([1,2,3,4,5,6]))
    print(isOrdered2([1,5,2,3,7,4,8]))
    print(isOrdered2(['b', 'a']))


main()