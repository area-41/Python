import sys
import os
from src.modelos.conta import ContaCorrente
from src.servicos import ServicoAnaliseRisco
from src.servicos.persistencia import ServicoPersistencia
from src.servicos.logger import logger  # Importando o novo serviço


# Ajuste para garantir que o pacote 'src' seja reconhecido
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def exibir_menu():
    print("\n" + "="*50)
    print("FINTECH RISK SYSTEM v3.0")
    print("="*50)
    print("1. Cadastrar Nova Conta")
    print("2. Consultar Conta e Risco")
    print("3. Listar Todas as Contas")
    print("4. Atualizar Dados (Renda/Saldo)")
    print("5. Encerrar (Deletar) Conta")
    print("0. Sair")
    print("="*50)


def cadastrar_conta():
    try:
        nome = input("Nome do Titular: ")
        renda = float(input("Renda Mensal (R$): "))
        deposito = float(input("Depósito Inicial (R$): "))

        nova_conta = ContaCorrente(nome, deposito, renda)
        # Aqui o método agora valida a duplicidade
        ServicoPersistencia.salvar_conta(nova_conta.to_dict())
        # Registro de Auditoria
        logger.info(f"Nova conta cadastrada: {nome} | Renda: R$ {renda}")
        print(f"\nConta de '{nome}' cadastrada!")

    except ValueError as e:
        logger.error(f"Erro ao tentar cadastrar conta: {e}")
        print(f"\nErro de entrada: {e}")


def consultar_conta():
    nome = input("Digite o nome do titular para busca: ")
    logger.info(f"Busca realizada pelo titular: {nome}")
    dados = ServicoPersistencia.buscar_conta_por_titular(nome)

    if dados:
        print(f"\n--- Dados da Conta ---")
        print(f"Titular: {dados['titular']}")
        print(f"Saldo Atual: R$ {dados['saldo']:.2f}")
        print(f"Renda Declarada: R$ {dados['renda']:.2f}")

        # Simulação de análise de crédito automática para o titular buscado
        analisador = ServicoAnaliseRisco()
        valor_solicitado = float(input("\nValor da parcela para simulação de empréstimo: "))
        res = analisador.validar_proposta_por_renda(dados['renda'], valor_solicitado)

        print(f"\nANÁLISE DE RISCO:")
        print(f"Status: {res['status']}")
        print(f"Comprometimento: {res['comprometimento']}%")
    else:
        print("\nConta não encontrada no sistema.")


def listar_contas():
    contas = ServicoPersistencia.listar_contas()
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return

    print(f"\n{'TITULAR':<20} | {'RENDA':<12} | {'SALDO':<12}")
    print("-" * 50)
    for c in contas:
        print(f"{c['titular']:<20} | R$ {c['renda']:<9.2f} | R$ {c['saldo']:<9.2f}")


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

        if opcao == "1": cadastrar_conta()
        elif opcao == "2": consultar_conta()
        elif opcao == "3": listar_contas()
        elif opcao == "4": atualizar_dados()
        elif opcao == "5": deletar_conta()
        elif opcao == "0":
            print("\nEncerrando sistema... Até logo!")
            break
        else: print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    run()
