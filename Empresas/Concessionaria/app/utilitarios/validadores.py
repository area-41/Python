import re


class ValidadorVeiculo:
    """
    Métodos Estáticos (@staticmethod), ideais para utilitários pois não precisam acessar
    dados da instância (o self), funcionando como funções puras de validação
    """

    @staticmethod
    def validar_preco(valor: float) -> bool:
        """Verifica se o preço é um número positivo."""
        if not isinstance(valor, (int, float)):
            return False
        return valor > 0

    @staticmethod
    def validar_ano(ano: int) -> bool:
        """Exemplo de validação de regra de negócio: não aceitamos carros futuros."""
        from datetime import datetime
        ano_atual = datetime.now().year
        return 1900 <= ano <= (ano_atual + 1)

    @staticmethod
    def validar_placa(placa: str) -> bool:
        """
        Valida se a placa segue o padrão Mercosul ou Antigo.
        Demonstra conhecimento em Expressões Regulares (Regex).
        """
        padrao = r"^[A-Z]{3}[0-9][A-Z0-9][0-9]{2}$"
        return bool(re.match(padrao, placa.upper()))