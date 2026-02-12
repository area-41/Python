#from app.modelos.livro import Livro
from app.servicos.gestor_dados import GestorDados
#from app.utilitarios.tests import rodar_teste_completo


def main():
    # 1. Tentar carregar dados existentes do arquivo JSON
    # O método carregar_acervo já retorna uma instância de Biblioteca
    biblioteca = GestorDados.carregar_acervo()

    """
    # 2. Verificar se a biblioteca está vazia usando o método público get_acervo()
    # Isso evita o erro de acessar atributos privados diretamente
    if not biblioteca.get_acervo():
        print(" Arquivo não encontrado ou vazio. Criando dados iniciais...")
        biblioteca.adicionar_livro(Livro("O Hobbit", "Tolkien", 1937))
        biblioteca.adicionar_livro(Livro("1984", "Orwell", 1949))
        biblioteca.adicionar_livro(Livro("Dom Casmurro", "Machado de Assis", 1899))
    else:
        print(f" {len(biblioteca.get_acervo())} livros carregados do banco de dados.")
    """
    while True:
        print("\n" + "=" * 30)
        print("   SISTEMA DE BIBLIOTECA   ")
        print("=" * 30)
        print("1. Listar Acervo Completo")
        print("2. Buscar por Autor")
        print("3. Buscar por Ano")
        print("4. Realizar Empréstimo")
        print("5. Devolver Livro")
        print("6. Salvar e Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":  # Exibir status atual (vindo do JSON ou da criação inicial)
            print("\n --- Acervo Atual ---")
            biblioteca.listar_acervo()

        elif opcao == "2":
            autor = input("Digite o nome do autor: ")
            resultados = biblioteca.buscar_por_autor(autor)
            for r in resultados: print(r)

        elif opcao == "3":
            try:
                ano = int(input("Digite o ano: "))
                resultados = biblioteca.buscar_por_ano(ano)
                for r in resultados: print(r)
            except ValueError:
                print("Ano inválido.")

        elif opcao == "4":  # Emprestar um livro para ver a mudança no próximo salvamento
            print("\n-- Processando operação de Empréstimo --")
            titulo = input("Título do livro para empréstimo (Ex.: 1984): ")
            print(biblioteca.realizar_emprestimo(titulo))
            # print(biblioteca.realizar_emprestimo("1984"))
            # print(biblioteca.realizar_emprestimo("Admirável Mundo Novo"))

        elif opcao == "5":
            titulo = input("Título do livro para devolução: ")
            livro = next((l for l in biblioteca.get_acervo() if l.titulo.lower() == titulo.lower()), None)
            if livro:
                livro.devolver()
                print(f"Sucesso: '{titulo}' devolvido.")
            else:
                print("Livro não encontrado.")

        elif opcao == "6":  # Salvar mudanças (Persiste o estado 'Emprestado' de volta no JSON)
            GestorDados.salvar_acervo(biblioteca)
            print("\n Processo finalizado e dados sincronizados.\n\n")
            print("Até logo!")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    # Rodar o main ou o teste
    main()
    # rodar_teste_completo()
