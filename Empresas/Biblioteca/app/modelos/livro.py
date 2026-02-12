class Livro:
    """
        Representa um livro no sistema da biblioteca.

        Esta classe gerencia as informações básicas de um livro e seu estado
        de disponibilidade através de encapsulamento.

        Attributes:
            titulo (str): O título do livro.
            autor (str): O autor da obra.
            ano_publicacao (int): O ano em que o livro foi publicado.
        """

    def __init__(self, titulo: str, autor: str, ano_publicacao: int):
        """
                Inicializa um novo livro.

                Args:
                    titulo (str): Título da obra.
                    autor (str): Nome do autor.
                    ano_publicacao (int): Ano de lançamento.
                """
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.__emprestado: bool = False  # Atributo privado: controle interno

    def emprestar(self) -> bool:
        """
                Altera o estado do livro para emprestado caso esteja disponível.

                Returns:
                    bool: True se o empréstimo foi realizado com sucesso,
                          False se o livro já estava emprestado.
                """
        if not self.__emprestado:
            self.__emprestado = True
            return True
        return False

    def devolver(self) -> None:
        """Define o estado do livro como disponível."""
        self.__emprestado = False

    def status(self) -> str:
        """
                Retorna uma representação textual da disponibilidade.

                Returns:
                    str: 'Emprestado' ou 'Disponível'.
                """
        return 'Emprestado' if self.__emprestado else 'Disponível'

    def __str__(self) -> str:
        return f"{self.titulo} - {self.autor} ({self.status()})"
