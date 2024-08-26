class Paciente():
    
    geradorRegistro = 0

    def __init__(self, nome, idade):
        Paciente.geradorRegistro += 1
        self.nome = nome
        self.idade = idade
        self.registroEntrada = Paciente.geradorRegistro
        self.proximo = None

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Idade: {self.idade}, Prontuário: {self.registroEntrada}"
