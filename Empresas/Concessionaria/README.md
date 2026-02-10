# 🚗 Sistema de Gerenciamento - Loja de Carros
Este projeto faz parte do meu portfólio profissional (pasta empresas/) e simula o backend de um sistema de gerenciamento de estoque para uma concessionária. O objetivo principal é demonstrar o domínio de conceitos avançados de Programação Orientada a Objetos (POO) em Python.

## Tecnologias e Conceitos Aplicados
Neste projeto, apliquei padrões de design e princípios de engenharia de software para garantir um código limpo e escalável:

Abstração: Uso da classe base Veiculo (módulo abc) para definir contratos obrigatórios para as subclasses.

Herança: Implementação de classes específicas (Carro, Moto) que herdam comportamentos comuns, reduzindo a duplicidade de código.

Encapsulamento: Uso de atributos privados e protegidos (_preco, __veiculos) com decoradores @property para controle rigoroso de acesso e validação de dados.

Type Hinting: Uso de dicas de tipagem para melhorar a legibilidade e facilitar a manutenção em IDEs como PyCharm.

Organização em Pacotes: Estrutura modular separando modelos de domínio, serviços de lógica de negócio e utilitários.

## Estrutura do Projeto

A estrutura utilizada neste projeto utilizou o padrão de pastas app/ para separar a lógica da interface (main.py), 
o que facilita testes unitários e manutenção.

    Plaintext
    LojaDeCarros/
    ├── app/
    │   ├── modelos/       # Definição das classes e regras de negócio base
    │   └── servicos/      # Lógica de manipulação de dados (Estoque)
    ├── main.py            # Script principal para execução do sistema
    └── requirements.txt   # Dependências do projeto

## Como Executar
Certifique-se de ter o Python 3.x instalado.

Clone este repositório:


    -- Bash
    git clone https://github.com/area-41/Python/Empresas/Concessionaria.git

Acesse a pasta do projeto:

    -- Bash
    cd Empresas/Concessionaria

Execute o sistema:

    -- Bash
    python main.py

![Python Tests](https://github.com/area-41/Python/actions/workflows/python-tests.yml/badge.svg)

Desenvolvido por [Victor Marques](https://www.linkedin.com/in/victor-marques-data-analyst/) Conecte-se comigo no LinkedIn


