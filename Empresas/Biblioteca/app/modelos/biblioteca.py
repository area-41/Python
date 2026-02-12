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

    def listar_acervo(self) -> None:
        """Imprime todos os livros e seus respectivos estados."""
        for livro in self.__acervo:
            print(livro)

    @property
    def Biblioteca__acervo(self):
        return self._biblioteca__acervo

    @property
    def biblioteca__acervo(self):
        return self._biblioteca__acervo
