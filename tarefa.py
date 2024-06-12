class Tarefa:
    def __init__(self, titulo, descricao, status='Pendente'):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status

    def __str__(self):
        return f"Título: '{self.titulo}'\nDescrição: '{self.descricao}'\nStatus: '{self.status}'"
