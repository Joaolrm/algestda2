from Paciente import Paciente
class lista_pacientes:
    def __init__(self):
        self.inicio = None
        self.pacientes = 0

    def busca_paciente(self, registroParaPesquisa):
        if self.inicio == None:
            print("Lista de pacientes vazia")
        else:
            pacienteAux = self.inicio
            while pacienteAux:
                if pacienteAux.registroEntrada == registroParaPesquisa:
                    return pacienteAux
                else: 
                    pacienteAux = pacienteAux.proximo


    def lista_pacientes(self):
        if self.inicio == None:
            print("Lista de pacientes vazia")
        else:
            pacienteAux = self.inicio
            while pacienteAux:
                print(pacienteAux)
                pacienteAux = pacienteAux.proximo
                
    def add_paciente(self, paciente):
        if self.inicio == None:
            self.inicio = paciente
        else:
            if paciente.registroEntrada < self.inicio.registroEntrada:
                paciente.proximo = self.inicio
                self.inicio = paciente
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux:
                    if paciente.registroEntrada < aux.registroEntrada:
                        paciente.proximo = ant.proximo
                        ant.proximo = paciente
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
                if aux == None and paciente.registroEntrada >= ant.registroEntrada:
                    ant.proximo = paciente
            self.pacientes += 1


pacientes = lista_pacientes()
	
		

		


				