# Importando de forma absoluta
from app.models.conta import Conta


class BancoService:
    """
    Para evitar Deadlocks em transferências simultâneas entre duas contas (A para B e B para A),
    uma técnica comum é ordenar o acesso aos locks pelo ID da conta.
    """

    @staticmethod
    def transferir(origem: Conta, destino: Conta, valor: float):
        # Ordenação de locks para evitar Deadlock
        primeiro, segundo = (origem, destino) if id(origem) < id(destino) else (destino, origem)

        with primeiro._lock, segundo._lock:
            taxa = origem.calcular_taxa()
            total_necessario = valor + taxa

            if origem.saldo >= total_necessario:
                origem._alterar_saldo(-total_necessario)
                destino._alterar_saldo(valor)
                return True
            return False
