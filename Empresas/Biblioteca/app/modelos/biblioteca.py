from typing import List
from .livro import Livro


class Biblioteca:
    """
    Gerencia o acervo e as regras de negócio de empréstimo.
    """
    def __init__(self):
        self._biblioteca__acervo = None
        self.__acervo: List[Livro] = []

    def adicionar_livro(self, livro: Livro) -> None:
        """Adiciona um objeto Livro à lista interna."""
        self.__acervo.append(livro)

    def get_acervo(self) -> List[Livro]:
        """Retorna uma cópia da lista do acervo para leitura."""
        return self.__acervo

    def realizar_emprestimo(self, titulo: str) -> str:
        """
        Localiza o livro e tenta executar o método de empréstimo do objeto.
        """
        for livro in self.__acervo:
            if livro.titulo.lower() == titulo.lower():
                if livro.emprestar():
                    return f"Sucesso: '{titulo}' emprestado."
                return f"Aviso: '{titulo}' já está emprestado."
        return "Erro: Livro não encontrado."

    """
    def listar_acervo(self) -> None:
        # Imprime todos os livros e seus respectivos estados.
        for livro in self.__acervo:
            print(livro)
    """

    def listar_acervo(self):
        if not self.get_acervo():
            print("\n O acervo está vazio.")
            return

        print(f"\n{' ' * 20} LISTA DE LIVROS NO ACERVO")
        for livro in self.get_acervo():
            print(livro)  # Aqui chama o seu novo __str__


    @property
    def biblioteca__acervo(self):
        return self._biblioteca__acervo

    def buscar_por_autor(self, autor: str) -> List[Livro]:
        """Retorna uma lista de livros de um autor específico."""
        return [livro for livro in self.__acervo if autor.lower() in livro.autor.lower()]

    def buscar_por_ano(self, ano: int) -> List[Livro]:
        """Retorna uma lista de livros publicados em um ano específico."""
        return [livro for livro in self.__acervo if livro.ano_publicacao == ano]

    def buscar_por_genero(self, genero: str) -> List[Livro]:
        """
        Retorna uma lista de livros filtrados por gênero.

        Args:
            genero (str): O gênero a ser pesquisado.

        Returns:
            List[Livro]: Lista de objetos que pertencem ao gênero.
        """
        return [livro for livro in self.__acervo if genero.lower() in livro.genero.lower()]

    def buscar_por_titulo(self, titulo: str) -> List[Livro]:
        """Busca livros que contenham o termo no título."""
        return [l for l in self.__acervo if titulo.lower() in l.titulo.lower()]

    def buscar_por_editora(self, editora: str) -> List[Livro]:
        """Busca livros de uma editora específica."""
        return [l for l in self.__acervo if editora.lower() in l.editora.lower()]