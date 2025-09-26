def add_tarefas(tarefas):
    titulo = input("digite o titulo da tarefa: ")
    tarefas.append({'titulo': titulo, 'concluida': False})
    
def listar_tarefas(tarefas):
    for i, tarefa in enumerate(tarefas)
    print(f"{1}, {tarefa}")

def marcar_concluida(tarefas):
    listar_tarefas(tarefas)
    num = int(input("Qual tarefa você quer marcar? ")
    tarefa[num - 1]['concluida']) = True
    print(f"tarefa {num} foi concluida")
    
def sair(tarefas):
    
    return False

def main():
    
    tarefas = []
    
    opcao = {
        '1': add_tarefa,
        '2': listar_tarefas,
        '3': marcar_concluida,
        '4': sair
    }
    continuar = True
    while continuar:
        print(opcao)
        escolha = input("qual a sua escolha: ")
        
        funçao = opcao.get(escolha)
        
        
        if funcao:
            if funcao(tarefas) == False:
                continue = False         