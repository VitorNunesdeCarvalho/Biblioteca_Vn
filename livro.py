class Livro:
    def _init_(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.status = "disponível"

    def disponibilidade(self):
        return self.status == "disponível"

    def alterar_status(self, status):
        self.status = status