import random
def geradorDeListasInteiro(qtd:int, max:int)->list:
    randList = []
    x = 0
    while x < qtd:
        x += 1
        randList.append(random.randint(0, max))

    return randList

def getIndexByValue(lista, valor):
    for i, x in enumerate(lista):
        if x == valor:
            return i

def binarySearch(lista, valor):
    inicio = 0
    fim = len(lista)-1
    

    while inicio <= fim:
        meio = (fim+inicio)//2
        if lista[meio] == valor:
            return meio

        elif valor < lista[meio]:
            fim = meio - 1
            

        elif  valor >  lista[meio]:
            inicio = meio + 1
            
    return
        