def validar_titulo():
    while True:
        titulo = input("Digite o título da tarefa: ").strip()
        if titulo:
            return titulo
        print("Erro: O título da tarefa não pode ser vazio. Tente novamente.\n")

def validar_prioridade():
    prioridades_validas = ["Alta", "Média", "Media", "Baixa"]
    while True:
        prioridade = input("Digite a prioridade (Alta, Média, Baixa): ").strip().capitalize()
        if prioridade in prioridades_validas:
            # Normaliza 'Media' para 'Média'
            return "Média" if prioridade == "Media" else prioridade
        print("Erro: Prioridade inválida. Digite apenas 'Alta', 'Média' ou 'Baixa'.\n")

def cadastrar_tarefa(lista_tarefas):
    print("\n--- CADASTRO DE NOVA TAREFA ---")
    titulo = validar_titulo()
    descricao = input("Digite a descrição da tarefa: ").strip()
    prioridade = validar_prioridade()
    data_limite = input("Digite a data limite (ex: DD/MM/AAAA): ").strip()
    
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }
    
    lista_tarefas.append(tarefa)
    print("\n Sucesso: Tarefa cadastrada com sucesso!\n")

def visualizar_tarefas(lista_tarefas):
    print("\n--- LISTA DE TAREFAS ---")
    if not lista_tarefas:
        print("Nenhuma tarefa cadastrada no momento.\n")
        return

    for idx, t in enumerate(lista_tarefas, start=1):
        print(f"Tarefa #{idx}")
        print(f"  • Título:      {t['titulo']}")
        print(f"  • Descrição:   {t['descricao']}")
        print(f"  • Prioridade:  {t['prioridade']}")
        print(f"  • Data Limite: {t['data_limite']}")
        print(f"  • Status:      {t['status']}")
        print("-" * 30)
    print()

def main():
    tarefas = []
    while True:
        print("<><><><><><><><><><><><><><><>")
        print("     TASKTRACKER - MENU       ")
        print("<><><><><><><><><><><><><><><>")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")
        print("<><><><><><><><><><><><><><><>")
        
        opcao = input("Escolha uma opção (1-3): ").strip()
        
        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("\nEncerrando o TaskTracker. Até logo!")
            break
        else:
            print("\nOpção inválida. Escolha entre 1, 2 ou 3.\n")

if __name__ == "__main__":
    main()