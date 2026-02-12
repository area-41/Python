from ..modelos.livro import Livro
from ..servicos.gestor_dados import GestorDados


def rodar_teste_completo():
    """Executa um ciclo completo de criação, alteração e salvamento."""
    print("\n\n Iniciando Teste de Integração... Será adicionado o Livro Python Fluente e em seguida emprestado.")

    """Testa sem apagar o que já existe."""
    # 1. CARREGA o que já tem no JSON primeiro
    biblioteca = GestorDados.carregar_acervo()

    # 2. ADICIONA algo novo apenas para teste
    print("Adicionando o Livro no acervo...")
    biblioteca.adicionar_livro(Livro("Python Fluente", "Luciano Ramalho", 2015))

    print("Tentando emprestar o Livro...")
    print(biblioteca.realizar_emprestimo("Python Fluente"))

    # 3. SALVA o conjunto completo (antigos + novo)
    GestorDados.salvar_acervo(biblioteca)
    print(" Teste concluído: Novo livro somado ao acervo existente.")
