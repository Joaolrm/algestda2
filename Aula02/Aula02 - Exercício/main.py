import function


randLista = function.geradorDeListasInteiro(10, 50)
print(randLista)
print(function.getIndexByValue(randLista, 13))
listaOrdenada = sorted(randLista)

print(listaOrdenada)
valor = function.binarySearch(listaOrdenada, 13)
print(valor)