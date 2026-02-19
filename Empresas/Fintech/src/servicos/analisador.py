from src.modelos import PropostaEmprestimo


class ServicoAnaliseRisco:
    def __init__(self, limite_percentual: float = 0.30):
        self.limite = limite_percentual

    def validar_proposta_por_renda(self, renda: float, valor_parcela: float) -> dict:
        """
        Analisa o risco baseando-se diretamente nos valores numéricos.
        Útil para quando os dados vêm de objetos com atributos privados.
        """
        if renda <= 0:
            raise ValueError("A renda para análise deve ser maior que zero.")

        percentual_uso = valor_parcela / renda
        aprovado = percentual_uso <= self.limite

        return {
            "aprovado": aprovado,
            "status": "APROVADO" if aprovado else "REPROVADO",
            "comprometimento": round(percentual_uso * 100, 2),
            "limite_maximo_parcela": round(renda * self.limite, 2)
        }