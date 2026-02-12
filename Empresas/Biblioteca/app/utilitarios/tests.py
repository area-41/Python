from ..modelos.livro import Livro
from ..modelos.biblioteca import Biblioteca
from ..servicos.gestor_dados import GestorDados


def rodar_teste_completo():
    """Executa um ciclo completo de criação, alteração e salvamento."""
    print(" Iniciando Teste de Integração...")

    bib = Biblioteca()
    bib.adicionar_livro(Livro("Python Fluente", "Luciano Ramalho", 2015))
    bib.realizar_emprestimo("Python Fluente")

    GestorDados.salvar_acervo(bib)
    print(" Teste concluído.")
