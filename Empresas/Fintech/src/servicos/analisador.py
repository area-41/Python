from src.modelos import PropostaEmprestimo


class ServicoAnaliseRisco:
    def __init__(self, limite_percentual: float = 0.30):
        self.limite = limite_percentual

    def validar_proposta(self, proposta: PropostaEmprestimo) -> dict:
        if proposta.renda_mensal <= 0:
            raise ValueError("A renda mensal deve ser positiva.")

        percentual_uso = proposta.valor_parcela / proposta.renda_mensal
        aprovado = percentual_uso <= self.limite

        return {
            "aprovado": aprovado,
            "comprometimento": round(percentual_uso * 100, 2),
            "valor_maximo_permitido": proposta.renda_mensal * self.limite
        }
