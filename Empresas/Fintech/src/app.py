import sys
import os


# Garante que o Python encontre o diretório 'src'
from src.modelos import PropostaEmprestimo
from src.servicos import ServicoAnaliseRisco

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def run():
    print("--- 🏦 FINTECH RISK ENGINE v1.0 ---")
    try:
        renda = float(input("Renda Mensal (R$): "))
        parcela = float(input("Parcela Desejada (R$): "))

        proposta = PropostaEmprestimo(renda_mensal=renda, valor_parcela=parcela)
        servico = ServicoAnaliseRisco()

        res = servico.validar_proposta(proposta)

        status = "✅ APROVADO" if res["aprovado"] else "❌ REPROVADO"
        print(f"\nResultado: {status}")
        print(f"Uso da Renda: {res['comprometimento']}%")

    except ValueError as e:
        print(f"⚠️ Erro: {e}")


if __name__ == "__main__":
    run()
