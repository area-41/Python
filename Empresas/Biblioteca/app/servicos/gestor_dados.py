import json
import os
from ..modelos.biblioteca import Biblioteca


class GestorDados:
    @staticmethod
    def salvar_acervo(biblioteca: Biblioteca, pasta: str = "data"):
        # Garante que a pasta existe antes de tentar salvar
        if not os.path.exists(pasta):
            os.makedirs(pasta)

        # Usamos o método público get_acervo() em vez do atributo privado __acervo
        acervo = biblioteca.get_acervo()

        dados = []
        for livro in acervo:
            dados.append({
                "titulo": livro.titulo,
                "autor": livro.autor,
                "ano": livro.ano_publicacao,
                "status": livro.status()
            })

        caminho_json = os.path.join(pasta, "acervo.json")
        with open(caminho_json, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

        print(f" Dados salvos com sucesso em {caminho_json}")

    @staticmethod
    def carregar_acervo(caminho_json: str = "data/acervo.json") -> Biblioteca:
        nova_bib = Biblioteca()
        if not os.path.exists(caminho_json):
            return nova_bib  # Retorna biblioteca vazia se o arquivo não existir

        try:
            with open(caminho_json, "r", encoding="utf-8") as f:
                dados = json.load(f)
                for item in dados:
                    from ..modelos.livro import Livro  # Import local para evitar circularidade
                    livro = Livro(item['titulo'], item['autor'], item['ano'])
                    if item.get('status') == 'Emprestado':
                        livro.emprestar()
                    nova_bib.adicionar_livro(livro)
            return nova_bib
        except Exception as e:
            print(f" Erro ao carregar: {e}")
            return nova_bib
