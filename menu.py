# menu.py

class Menu:
    def __init__(self, gerenciador_tarefas):
        self.gerenciador_tarefas = gerenciador_tarefas

    def exibir_menu(self):
        print("=== Menu ===")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Localizar Tarefa")
        print("4. Atualizar Status")
        print("5. Remover Tarefa")
        print("6. Sair")

    def executar(self):
        while True:
            self.exibir_menu()
            opcao = input("Selecione uma opção: ")

            if opcao == "1":
                titulo = input("Digite o título da tarefa: ")
                descricao = input("Digite a descrição da tarefa: ")
                self.gerenciador_tarefas.adicionar_tarefa(titulo, descricao)
            elif opcao == "2":
                self.gerenciador_tarefas.visualizar_tarefas()
            elif opcao == "3":
                titulo = input("Digite o título da tarefa a ser localizada: ")
                tarefa = self.gerenciador_tarefas.localizar_tarefa(titulo)
                if tarefa:
                    print("Tarefa encontrada:")
                    print(tarefa)
                else:
                    print("Tarefa não encontrada.")
            elif opcao == "4":
                titulo = input("Digite o título da tarefa a ser atualizada: ")
                novo_status = input("Digite o novo status da tarefa: ")
                self.gerenciador_tarefas.atualizar_status(titulo, novo_status)
            elif opcao == "5":
                titulo = input("Digite o título da tarefa a ser removida: ")
                self.gerenciador_tarefas.remover_tarefa(titulo)
            elif opcao == "6":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Por favor, selecione uma opção válida.")
