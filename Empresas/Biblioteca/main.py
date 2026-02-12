import sys
from app.modelos.livro import Livro
from app.servicos.gestor_dados import GestorDados
from app.utilitarios.tests import rodar_teste_completo
from app.modelos.biblioteca import Biblioteca


def listar_todos(bib):
    bib.listar_acervo()


def buscar_titulo(bib):
    termo = input("Digite o título ou parte dele: ")
    for r in bib.buscar_por_titulo(termo): print(r)


def buscar_autor(bib):
    termo = input("Digite o nome do autor: ")
    for r in bib.buscar_por_autor(termo): print(r)


def buscar_genero(bib):
    termo = input("Digite o gênero: ")
    for r in bib.buscar_por_genero(termo): print(r)


def buscar_editora(bib):
    termo = input("Digite a editora: ")
    for r in bib.buscar_por_editora(termo): print(r)


def realizar_emprestimo(bib):
    titulo = input("Título para empréstimo: ")
    print(bib.realizar_emprestimo(titulo))


def realizar_devolucao(bib):
    titulo = input("Título para devolução: ")
    livro = next((l for l in bib.get_acervo() if l.titulo.lower() == titulo.lower()), None)
    if livro:
        livro.devolver()
        print(f"✅ '{titulo}' devolvido!")
    else:
        print("❌ Livro não encontrado.")


def salvar_e_sair(bib):
    GestorDados.salvar_acervo(bib)
    print("💾 Dados salvos. Saindo...")
    sys.exit()


def menu_principal():
    biblioteca = GestorDados.carregar_acervo()

    # 2. Verificar se a biblioteca está vazia usando o método público get_acervo()
    # Isso evita o erro de acessar atributos privados diretamente
    if not biblioteca.get_acervo():
        print(" Arquivo não encontrado ou vazio. Criando dados iniciais...")
        popular()
    else:
        print(f" {len(biblioteca.get_acervo())} livros carregados do banco de dados.")

    # DICIONÁRIO DE OPÇÕES (Dispatch Table)
    opcoes = {
        "1": {"desc": "Listar Acervo", "func": listar_todos},
        "2": {"desc": "Buscar por Título", "func": buscar_titulo},
        "3": {"desc": "Buscar por Autor", "func": buscar_autor},
        "4": {"desc": "Buscar por Gênero", "func": buscar_genero},
        "5": {"desc": "Buscar por Editora", "func": buscar_editora},
        "6": {"desc": "Emprestar Livro", "func": realizar_emprestimo},
        "7": {"desc": "Devolver Livro", "func": realizar_devolucao},
        "8": {"desc": "Salvar e Sair", "func": salvar_e_sair}
    }

    while True:
        print("\n" + "=" * 40)
        print("      SISTEMA BIBLIOTECÁRIO 2.0      ")
        print("=" * 40)
        for chave, valor in opcoes.items():
            print(f"{chave}. {valor['desc']}")

        escolha = input("\nSelecione uma opção: ")

        if escolha in opcoes:
            # Chama a função mapeada no dicionário passando a biblioteca como argumento
            opcoes[escolha]["func"](biblioteca)
        else:
            print("⚠️ Opção inválida!")


def popular():
    bib = Biblioteca()

    # Lista de 20 livros com os novos parâmetros
    livros_iniciais = [
        Livro("Código Limpo", "Robert C. Martin", 2008, "Alta Books", 456, "978-8576082675", "Tecnologia"),
        Livro("O Hobbit", "J.R.R. Tolkien", 1937, "HarperCollins", 336, "978-8595084741", "Fantasia"),
        Livro("1984", "George Orwell", 1949, "Companhia das Letras", 416, "978-8535914849", "Ficção Distópica"),
        Livro("Duna", "Frank Herbert", 1965, "Aleph", 680, "978-8576573135", "Ficção Científica"),
        Livro("Dom Casmurro", "Machado de Assis", 1899, "Carambaia", 256, "978-8569002211", "Literatura Brasileira"),
        Livro("Arquitetura Limpa", "Robert C. Martin", 2017, "Alta Books", 432, "978-8550804606", "Tecnologia"),
        Livro("Sapiens", "Yuval Noah Harari", 2011, "L&PM", 464, "978-8525432186", "História/Ciência"),
        Livro("O Algoritmo Mestre", "Pedro Domingos", 2015, "Novatec", 344, "978-8575225000", "Tecnologia/IA"),
        Livro("Fundação", "Isaac Asimov", 1951, "Aleph", 240, "978-8576573005", "Ficção Científica"),
        Livro("O Processo", "Franz Kafka", 1925, "Companhia de Bolso", 320, "978-8535907476", "Clássico"),
        Livro("Crime e Castigo", "Fiódor Dostoiévski", 1866, "Todavia", 592, "978-8588808411", "Clássico"),
        Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "HarperCollins", 96, "978-8595081511",
              "Infantil"),
        Livro("Frankenstein", "Mary Shelley", 1818, "Zahar", 304, "978-8537815591", "Terror/Gótico"),
        Livro("Admirável Mundo Novo", "Aldous Huxley", 1932, "Biblioteca Azul", 312, "978-8525056009",
              "Ficção Distópica"),
        Livro("A Arte da Guerra", "Sun Tzu", -500, "Best Seller", 160, "978-8576840336", "Estratégia"),
        Livro("Pai Rico, Pai Pobre", "Robert Kiyosaki", 1997, "Alta Books", 336, "978-8550801483", "Finanças"),
        Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967, "Record", 448, "978-8501012074",
              "Realismo Mágico"),
        Livro("Orgulho e Preconceito", "Jane Austen", 1813, "Martin Claret", 424, "978-8572329272", "Romance"),
        Livro("O Retrato de Dorian Gray", "Oscar Wilde", 1890, "Pandorga", 256, "978-8584422234", "Clássico"),
        Livro("Grande Sertão: Veredas", "Guimarães Rosa", 1956, "Companhia das Letras", 624, "978-8535932157",
              "Literatura Brasileira")
    ]

    for livro in livros_iniciais:
        bib.adicionar_livro(livro)

    GestorDados.salvar_acervo(bib)
    print("✨ Acervo reconstruído com 20 livros detalhados!")


if __name__ == "__main__":
    # Rodar o main ou o teste
    menu_principal()
    # rodar_teste_completo()
    # popular()
