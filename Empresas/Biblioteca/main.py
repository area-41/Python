"""from app.modelos.livro import Livro
from app.servicos.gestor_dados import GestorDados


def main():
    # 1. Tentar carregar dados existentes
    biblioteca = GestorDados.carregar_acervo()

    if not biblioteca.biblioteca__acervo:
        print("📭 Biblioteca vazia. Criando dados iniciais...")
        biblioteca.adicionar_livro(Livro("O Hobbit", "Tolkien", 1937))
        biblioteca.adicionar_livro(Livro("1984", "Orwell", 1949))

    # 2. Exibir status
    print("\n--- Acervo Atual ---")
    biblioteca.listar_acervo()

    # 3. Realizar uma operação
    print("\n" + biblioteca.realizar_emprestimo("1984"))

    # 4. Salvar mudanças
    GestorDados.salvar_acervo(biblioteca)


if __name__ == "__main__":
    # Rodar o main ou o teste
    # rodar_teste_completo()
    main()
"""

from app.modelos.livro import Livro
from app.servicos.gestor_dados import GestorDados

def main():
    # 1. Tentar carregar dados existentes do arquivo JSON
    # O método carregar_acervo já retorna uma instância de Biblioteca
    biblioteca = GestorDados.carregar_acervo()

    # 2. Verificar se a biblioteca está vazia usando o método público get_acervo()
    # Isso evita o erro de acessar atributos privados diretamente
    if not biblioteca.get_acervo():
        print(" Arquivo não encontrado ou vazio. Criando dados iniciais...")
        biblioteca.adicionar_livro(Livro("O Hobbit", "Tolkien", 1937))
        biblioteca.adicionar_livro(Livro("1984", "Orwell", 1949))
        biblioteca.adicionar_livro(Livro("Dom Casmurro", "Machado de Assis", 1899))
    else:
        print(f" {len(biblioteca.get_acervo())} livros carregados do banco de dados.")

    # 3. Exibir status atual (vindo do JSON ou da criação inicial)
    print("\n --- Acervo Atual ---")
    biblioteca.listar_acervo()

    # 4. Realizar uma operação de demonstração
    # Vamos tentar emprestar um livro para ver a mudança no próximo salvamento
    print("\n Processando operação:")
    print(biblioteca.realizar_emprestimo("1984"))
    print(biblioteca.realizar_emprestimo("Admirável Mundo Novo"))


    # 5. Salvar mudanças (Persiste o estado 'Emprestado' de volta no JSON)
    GestorDados.salvar_acervo(biblioteca)
    print("\n Processo finalizado e dados sincronizados.")

if __name__ == "__main__":
    main()