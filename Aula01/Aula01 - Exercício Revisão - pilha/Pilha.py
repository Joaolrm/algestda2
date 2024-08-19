from No import No
class Pilha:
    def __init__(self):
        self.top = None
        self.tamanho = 0

    def empilhar(self, dado):
        no = No(dado)
        if self.top != None:
            no.proximo = self.top
        self.top = no
        self.tamanho += 1

    def desempilhar(self):
        if self.top == None:
            return None
        else:
            dado = self.top.dado
            self.top = self.top.proximo
            self.tamanho -= 1
            return dado
            
            