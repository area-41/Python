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

<img width="203" height="363" alt="image" src="https://github.com/user-attachments/assets/3663db3c-f2e0-4ba8-9ad9-b772f460e206" />

## 📺 Demonstração do Projeto

[![Demonstração do Sistema](https://img.youtube.com/vi/W36KTkNS89c/0.jpg)](https://www.youtube.com/watch?v=W36KTkNS89c)

*Clique na imagem acima para assistir ao vídeo de demonstração.*

## Como Executar
1. Clone o repositório.
2. Certifique-se de que a estrutura de pastas está correta.
3. Execute o comando:
   ```bash
   python main.py
