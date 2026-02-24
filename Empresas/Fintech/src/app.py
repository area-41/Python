import sys
import os

# Ajuste para garantir que o pacote 'src' seja reconhecido
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.modelos.conta import ContaCorrente
from src.servicos import ServicoAnaliseRisco
from src.servicos.persistencia import ServicoPersistencia
from src.servicos.logger import logger
from src.servicos.security import SecurityService # Note o caminho 'services' (plural)
from functools import wraps

# Ajuste para garantir que o pacote 'src' seja reconhecido
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def login_requerido(funcao_original):
    """
    Decorador que garante que o usuário esteja autenticado antes de executar a função protegida.
    """
    @wraps(funcao_original)
    def wrapper(*args, **kwargs):
        print(f"\nAcesso Restrito: Autenticação necessária para '{funcao_original.__name__}'")
        if realizar_login():
            return funcao_original(*args, **kwargs)
        else:
            print("Acesso negado. Retornando ao menu principal.")
    return wrapper

def exibir_menu():
    print("\n" + "="*50)
    print("FINTECH RISK SYSTEM v3.5 - ADMIN PORTAL")
    print("="*50)
    print("1. Cadastrar Nova Conta (com Senha)")
    print("2. Acessar Conta (Login)")
    print("3. Listar Todas as Contas")
    print("4. Atualizar Dados (Requer Login)")
    print("5. Encerrar Conta (Requer Login)")
    print("0. Sair")
    print("="*50)


def cadastrar_conta():
    try:
        nome = input("Nome do Titular: ")
        renda = float(input("Renda Mensal (R$): "))
        deposito = float(input("Depósito Inicial (R$): "))
        senha = input("Defina uma senha de acesso: ")

        # 1. Criamos o hash seguro da senha
        senha_hash = SecurityService.hash_password(senha)

        # 2. Criamos o objeto e preparamos os dados
        nova_conta = ContaCorrente(nome, deposito, renda)
        dados_finais = nova_conta.to_dict()
        dados_finais["senha"] = senha_hash  # Injetamos o hash no dicionário

        # 3. Persistência
        ServicoPersistencia.salvar_conta(dados_finais)

        logger.info(f"Nova conta e senha registradas para: {nome}")
        print(f"\nConta de '{nome}' cadastrada com sucesso!")

    except ValueError as e:
        logger.error(f"Erro no cadastro: {e}")
        print(f"\nErro: {e}")


def realizar_login():
    """Função de barreira para validar acesso."""
    nome = input("Digite o nome do titular: ")
    dados = ServicoPersistencia.buscar_conta_por_titular(nome)

    if not dados or "senha" not in dados:
        print("Conta não encontrada ou sem senha cadastrada.")
        return None

    senha_digitada = input("Digite sua senha: ")

    # Verificação usando o Hashlib via SecurityService
    if SecurityService.verify_password(dados["senha"], senha_digitada):
        print(f"Acesso concedido! Bem-vindo(a), {nome}.")
        return dados
    else:
        print("Senha incorreta. Operação cancelada.")
        logger.warning(f"Tentativa de login falha para o usuário: {nome}")
        return None


def consultar_conta_com_login():
    dados = realizar_login()
    if dados:
        print(f"\n--- Dados Privados ---")
        print(f"Titular: {dados['titular']} | Saldo: R$ {dados['saldo']:.2f}")

        analisador = ServicoAnaliseRisco()
        valor = float(input("\nValor para simulação de empréstimo: "))
        res = analisador.validar_proposta_por_renda(dados['renda'], valor)
        print(f"Análise: {res['status']} ({res['comprometimento']}% de comprometimento)")


def listar_contas():
    contas = ServicoPersistencia.listar_contas()
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return

    print(f"\n{'TITULAR':<20} | {'RENDA':<12} | {'SALDO':<12}")
    print("-" * 50)
    for c in contas:
        print(f"{c['titular']:<20} | R$ {c['renda']:<9.2f} | R$ {c['saldo']:<9.2f}")

@login_requerido
def atualizar_dados():
    nome = input("Nome do titular para atualizar: ")
    conta = ServicoPersistencia.buscar_conta_por_titular(nome)

    if conta:
        print(f"Dados atuais: Renda R$ {conta['renda']} | Saldo R$ {conta['saldo']}")
        try:
            nova_renda = float(input("Nova Renda Mensal (ou repita a atual): "))
            novo_saldo = float(input("Novo Saldo (ou repita o atual): "))

            sucesso = ServicoPersistencia.atualizar_conta(nome, {"renda": nova_renda, "saldo": novo_saldo})
            if sucesso:
                print(f"Dados de {nome} atualizados com sucesso!")
        except ValueError:
            print("Erro: Valores numéricos inválidos.")
    else:
        print("Conta não encontrada.")

@login_requerido
def deletar_conta():
    nome = input("Nome do titular da conta a ser encerrada: ")
    confirmar = input(f"Tem certeza que deseja deletar a conta de {nome}? (s/n): ")

    if confirmar.lower() == 's':
        if ServicoPersistencia.deletar_conta(nome):
            print(f"Conta de {nome} removida do sistema.")
        else:
            print("Conta não encontrada.")


def run():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":   cadastrar_conta()
        elif opcao == "2": consultar_conta_com_login()
        elif opcao == "3": listar_contas()
        elif opcao == "4": atualizar_dados()  # O decorador cuida do login sozinho!
        elif opcao == "5": deletar_conta()  # O decorador cuida do login sozinho!
        elif opcao == "0":
            print("\nEncerrando sistema... Até logo!")
            break
        else: print("\nOpção inválida.")


if __name__ == "__main__":
    run()
