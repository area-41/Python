# Buscador de Preços Tabela FIPE

Material de estudo de programação Python a fim de desenvovlver um aplicativo **Python**, consumo de **APIs REST** e deploy de aplicações web, web app para consulta no site em dados de uma API pública.

O objetivo é oferecer uma interface simples e amigável para qualquer usuário consultar preços médios de veículos no Brasil através da base de dados da FIPE.

📍 **Acesse o projeto aqui:** [BuscaFIPE Online](https://buscafipe-55aybbvvqkassasgtvz35x.streamlit.app/)

---

## Tecnologias Utilizadas

Foram utilizadas as seguintes ferramentas de engenharia de software:

* **Python 3.13:** Linguagem base do projeto.
* **Streamlit:** Para a criação da interface web reativa.
* **Pandas:** Para manipulação e filtragem dos dados da API.
* **Requests:** Para comunicação assíncrona com a API Parallelum FIPE.
* **PyCharm:** IDE utilizada para o desenvolvimento e organização da estrutura.
* **GitHub Actions:** Para garantir a integridade do código.

---

## Desafios de Desenvolvimento

Durante a construção, enfrentei e resolvi alguns desafios técnicos interessantes:

1.  **Filtro Alfabético:** Lógica de filtragem inicial por letra para facilitar a busca em uma lista de marcas que possui mais de 90 itens.
2.  **Tratamento de Erros (Status 500):** Aprendi a lidar com exceções de servidor validando dinamicamente os códigos de "Ano-Combustível", evitando que o app quebrasse em seleções inválidas.
3.  **Deploy em 2026:** Ajustei dependências críticas (como `Altair` e `Streamlit`) para garantir que o ambiente em nuvem funcionasse perfeitamente com as versões mais recentes das bibliotecas.

---

## Estrutura do Projeto

O código foi organizado seguindo boas práticas de separação de responsabilidades:

```text
BuscaFipe/
├── web_app.py           # Interface Web (Streamlit)
├── core/
│   └── fipe_handler.py  # Lógica de consumo da API (Backend)
├── tests/
│   └── test_fipe.py     # Testes unitários automáticos
└── requirements.txt     # Gestão de dependências
```

## Como rodar localmente
Se você quiser testar este projeto no seu computador:

Clone o repositório:

    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)

Instale as dependências:

    pip install -r requirements.txt
    
Execute o Streamlit:

    streamlit run web_app.py
