'''
    Eliminar de una lista de palabras, las palabras que se encuentren en una segunda
    lista. Imprimir la lista original, la lista de palabras a eliminar y
    la lista resultante.
'''

def deleteWordsFromAList(firstList:str, secondList:str):
    for i in range(len(secondList)):
        if secondList[i] in firstList:
            firstList.remove(secondList[i])

def main():
    wordsList = ['Hola', 'Juan', '23', 'Buenos Aires']
    wordsList2 = ['Hola', 'Pablo', '44', 'Buenos Aires']
    print(wordsList)
    print(wordsList2)
    deleteWordsFromAList(wordsList, wordsList2)
    print(wordsList)

main()