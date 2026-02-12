# 📚 Sistema de Gerenciamento de Biblioteca

Este projeto é uma demonstração prática de conceitos avançados de **Programação Orientada a Objetos (POO)** em Python, com foco em encapsulamento, persistência de dados e organização de arquitetura em camadas.

## ️ Tecnologias e Conceitos
- **Python 3.x**: Linguagem base.
- **Encapsulamento**: Uso de atributos privados (`__emprestado`) e métodos de acesso (Getters).
- **Persistência**: Salvamento e leitura de dados em arquivos **JSON** e **TXT**.
- **Arquitetura Modular**: Divisão em `modelos`, `servicos` e `utilitarios`.

## Estrutura do Projeto
- `app/modelos/`: Contém as classes `Livro` e `Biblioteca`.
- `app/servicos/`: Lógica de exportação e importação de dados (`GestorDados`).
- `app/utilitarios/`: Scripts de teste e ferramentas de apoio.
- `data/`: Local onde o banco de dados JSON é armazenado.
- `main.py`: Ponto de entrada com menu interativo.

## Como Executar
1. Clone o repositório.
2. Certifique-se de que a estrutura de pastas está correta.
3. Execute o comando:
   ```bash
   python main.py