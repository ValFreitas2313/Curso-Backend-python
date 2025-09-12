def exibir_menu():

    print("\n=== sistema de cadastro de alunos ===")
    print("1 cadastrar novo aluno:")
    print("2 lista de alunos cadastrado:")
    print("3 buscar aluno por matricula:")
    print("4 sair:")

def cadastrar_aluno(aluno):
    nome = input("digite o nome do aluno: ")

    while True:
        matricula = input("digite a matricula (apenas numero): ")

        try:
            matricula = input("digite _int = int(matricula:")
    
        except ValueError:
            print("matricula invalida! digite apenas numeros.")

        curso = input("digite o curso do aluno:").strip()
        aluno = {"nome": nome, "matricula": matricula, "curso": curso }
        
        print(f"aluno {nome} cadastrado com sucesso!")

def listar_aluno(aluno):
    
    if not aluno:
        print("nenhum aluno cadastrado ainda.")
    else:
        print("\n--- alunos cadastrado ---")
        for i, aluno in enumerate(aluno, start = 1): 
            print(f"{i}, nome: {aluno['nome']}, matricula:{aluno['matricula']}, curso: {aluno['curso']}")

def buscar_aluno(aluno):
    if not aluno:
        print("nenhum aluno cadastrado para buscar.")
        print("digite a matricula do aluno que deseja buscar:")
    
    try: matricula_int = int("matricula")
    except ValueError:
        print("matricula inválida! digite apenas numeros.")

        return
    for aluno in aluno:
        if aluno["matricula"] == matricula_int:
            print(f"aluno encotrado: nome: {aluno['curso']},curso: {aluno['curso']}")
        return
        print("nenhum aluno encontrado com esta matricula.")

def main():
    aluno = []

    while True:
        exibir_menu()
        opcao = input("escolha uma opcao:")
        if opcao == "1": cadastrar_aluno(aluno)
        elif opcao == "2": listar_aluno(aluno)
        elif opcao == "3": buscar_aluno(aluno)
        elif opcao == "4": "sair"



if __name__ == "__main__":main()
