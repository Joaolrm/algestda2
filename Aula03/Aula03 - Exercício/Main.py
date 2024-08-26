from lista_pacientes import *

def interface_menu():
    opcao_valida = {'H': help_, 'A': adicionar_, 'L': localizar_, 'T': todos_pacientes_, 'F': fim_}
    while True:
        opcao = input("""
        ===================================
        [A]dicionar Paciente
        [L]ocalizar Paciente
        [T]odos Pacientes

        [H]elp - Enunciado
        [F]im

        -----------------------------------
        Obs.: Escolha pela letra do menu
        ===================================: """).upper()

        return opcao_valida[opcao]


def adicionar_():
    print("=" * 40)
    paciente1 = Paciente("João", 30)
    paciente2 = Paciente("Pedro", 40)
    paciente3 = Paciente("Maria", 35)
    paciente4 = Paciente("Tevez", 30)
    paciente5 = Paciente("Jorge", 30)
    pacientes.add_paciente(paciente5)
    pacientes.add_paciente(paciente3)
    pacientes.add_paciente(paciente1)
    pacientes.add_paciente(paciente2)
    pacientes.add_paciente(paciente4)
    input("Alguns pacientes adicionados como teste. Enter")


def localizar_():
    print("=" * 40)
    print("Localizar paciente pelo registro médico:")
    # registro_medico_para_pesquisa = 1003. # Exemplo
    registro_para_pesquisa = int(input("Entre com o registro do paciente: "))
    paciente_encontrado = pacientes.busca_paciente(registro_para_pesquisa)

    if paciente_encontrado:
        print(f"Paciente encontrado - Nome: {paciente_encontrado.nome}, Idade: {paciente_encontrado.idade}")
    else:
        print(f"Paciente com prontuário {registro_para_pesquisa} não encontrado.")
    input("[Enter] para retornar ao menu.")


def todos_pacientes_():
    print("=" * 40)
    print("Lista de pacientes:")
    pacientes.lista_pacientes()
    input("[Enter] para retornar ao menu.")


def fim_():
    raise ValueError("Finalizando...")


def help_():
    print("======================================================================")
    print("======================================================================")
    print("Instruções:")
    print("""
    Um hospital deseja implementar um sistema de gerenciamento de pacientes 
        quando estes dão entrada para atendimento, utilizando listas encadeadas.
    Cada nó da lista deve armazenar informações sobre um paciente como:
        nome, idade e número do prontuário de entrada.
    A lista deve ser ordenada pelo número do prontuário.

    Para facilitar a busca de pacientes pelo número do prontuário, o hospital 
        deseja implementar uma função de pesquisa binária que recebe como entrada 
        o número do prontuário e retorna o nó correspondente.

    A função deve retornar None caso o número do prontuário não seja encontrado 
        na lista.

    Escreva um programa em Python que implemente uma lista simplesmente encadeada. 
    Seu código deverá permitir ao usuário realizar as seguintes operações:

        - Adicionar um novo paciente à lista, 
            informando nome, idade e número do prontuário de entrada.
        - Listar todos os pacientes da lista em ordem 
            alfabética pelo nome.
        - Buscar um paciente pelo número do prontuário.

    O programa deve exibir mensagens de erros: 
        - caso, na inserção, o número do prontuário já exista na lista ou 
        - caso, na pesquisa, o número do prontuário informado na busca 
          não seja encontrado.
""")
    print("======================================================================")
    input("ENTER - Retorna ao menu.")


def main():
    while True:
        try:
            interface_menu()()
        except ValueError as saida:
            print(saida)
            break
        except:
            input("Ops. Inválida. Enter")


if __name__ == '__main__':
    main()