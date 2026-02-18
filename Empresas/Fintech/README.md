# Fintech Risk Engine

Este projeto é um Simulador de Análise de Risco de Crédito modular, desenvolvido em Python. Ele demonstra a aplicação de regras de negócio complexas em um ambiente estruturado seguindo padrões de engenharia de software utilizados em grandes Fintechs.

### Objetivo
O motor avalia propostas de empréstimo com base na regra de comprometimento de renda. O sistema garante que nenhuma parcela ultrapasse 30% da renda mensal bruta do cliente, tratando erros de entrada e garantindo a integridade dos cálculos.

### Arquitetura do Projeto
A solução foi dividida em camadas para garantir separação de responsabilidades e facilitar a testabilidade:

modelos/: Define as entidades de dados (Data Classes).

servicos/: Contém a lógica de negócio (Engine de Risco).

app.py: Interface de linha de comando para interação com o usuário.

tests/: Suite de testes unitários para garantir a confiabilidade das regras.

### Como Executar
Pré-requisitos: Python 3.8 ou superior instalado.

Instalação em modo de desenvolvimento
Clone o repositório: Bash
        
    git clone https://github.com/area-41/fintech.git

    cd fintech

Instale o pacote localmente: Bash

    pip install -e .

Executando o Simulador
Após a instalação, você pode rodar o simulador de qualquer lugar do terminal usando o comando registrado no setup.py: Bash

    analise-risco

### Testes Automatizados
Para rodar os testes unitários e verificar se todas as regras de negócio estão operacionais: Bash

    python -m unittest discover tests

### Destaques Técnicos

- Modularização Profissional: Uso de arquivos __init__.py para gerenciamento de pacotes.

- Resiliência: Tratamento de exceções customizadas para entradas inválidas.

- Escalabilidade: Configuração de setup.py pronta para distribuição e integração com pipelines de CI/CD.

- Tipagem: Uso de Type Hinting para melhor legibilidade e manutenção do código.


Desenvolvido por [Victor Marques](https://github.com/area-41)

#### "Transformando lógica de negócios em código limpo e escalável."