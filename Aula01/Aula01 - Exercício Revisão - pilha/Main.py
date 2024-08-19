from Pilha import Pilha

def validarExpressao(expressao):
    
    pilha = Pilha()
    pares = {
            ')': '('
            ,']': '[' 
            ,'}': '{'
        }

    for char in expressao:
        if char in '({[':
            pilha.empilhar(char)
        elif char in ')}]':
            topo = pilha.desempilhar()
            if  topo == None or topo != pares[char]:
                return False
            
    return True

expressoes = [
    "c[d]"
    ,"a{b[c]d}e"
    ,"a{b(c]d}e"
    ,"a[b{c}d]e}"
]

for exp in expressoes:
    print(validarExpressao(exp))