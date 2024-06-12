# main.py

from menu import Menu
from gerenciador_tarefas import GerenciadorTarefas

def main():
    gerenciador = GerenciadorTarefas()
    menu = Menu(gerenciador)
    menu.executar()

if __name__ == "__main__":
    main()
