from tarefa import Tarefa

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo, descricao):
        tarefa = Tarefa(titulo, descricao)
        self.tarefas.append(tarefa)

    def visualizar_tarefas(self):
        for index, tarefa in enumerate(self.tarefas):
            print(f"Tarefa {index + 1}:")
            print(tarefa)
            print()

    def localizar_tarefa(self, titulo):
        for tarefa in self.tarefas:
            if tarefa.titulo.lower() == titulo.lower():
                return tarefa
        return None

    def atualizar_status(self, titulo, novo_status):
        tarefa = self.localizar_tarefa(titulo)
        if tarefa:
            tarefa.status = novo_status
            print(f"Status da tarefa '{titulo}' atualizado para '{novo_status}'.")
        else:
            print(f"Tarefa '{titulo}' não encontrada.")

    def remover_tarefa(self, titulo):
        tarefa = self.localizar_tarefa(titulo)
        if tarefa:
            self.tarefas.remove(tarefa)
            print(f"Tarefa '{titulo}' removida com sucesso.")
        else:
            print(f"Tarefa '{titulo}' não encontrada.")