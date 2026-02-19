class ContaCorrente:
    def __init__(self, titular: str, saldo_inicial: float, renda: float):
        self.titular = titular
        self.__saldo = saldo_inicial  # Privado
        self.__renda = renda          # Privado

    # Getter para o saldo (Apenas leitura)
    @property
    def saldo(self):
        return self.__saldo

    # Getter para a renda (Usado no motor de risco)
    @property
    def renda(self):
        return self.__renda

    def depositar(self, valor: float):
        if valor > 0:
            self.__saldo += valor
            self.__registrar_log(f"Depósito de R$ {valor}")

    def __registrar_log(self, mensagem: str):
        """Método privado: Apenas a própria classe usa."""
        print(f"[LOG INTERNO]: {mensagem}")

    def to_dict(self):
        """Converte para dicionário para salvar no JSON."""
        return {
            "titular": self.titular,
            "saldo": self.__saldo,
            "renda": self.__renda
        }
