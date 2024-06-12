class ValidadorTarefa:
    @staticmethod
    def validar_titulo(titulo):
        return titulo.strip() != ""

    @staticmethod
    def validar_descricao(descricao):
        return descricao.strip() != ""