from dataclasses import dataclass


@dataclass
class PropostaEmprestimo:
    renda_mensal: float
    valor_parcela: float
    nome_cliente: str = "Consumidor"
