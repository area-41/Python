from .veiculo import Veiculo
from app.utilitarios.validadores import ValidadorVeiculo


class Moto(Veiculo):
    """
    Classe com Polimorfismo, pois terá uma lógica de calcular_ipva diferente (geralmente uma alíquota menor ao carro)
    e um atributo específico (cilindradas), o que justifica a existência da subclasse.
    """
    def __init__(self, marca: str, modelo: str, preco: float, cilindradas: int):
        # super() chama o construtor da classe pai (Veiculo)
        super().__init__(marca, modelo, preco)
        self.cilindradas = cilindradas

    @property
    def preco(self):
        """Retorna o preço formatado (Encapsulamento)"""
        return f"R$ {self._preco:,.2f}"

    @preco.setter
    def preco(self, valor: float):
        """Garante que o preço da moto seja sempre positivo"""
        if ValidadorVeiculo.validar_preco(valor):
            self._preco = valor
        else:
            raise ValueError("Preço inválido para o cadastro do veículo.")

    def calcular_ipva(self):
        """
        Exemplo de Polimorfismo: Motos costumam pagar 2% de IPVA,
        enquanto carros pagam 4%.
        """
        return self._preco * 0.02

    def __str__(self):
        """Método especial para representação em string"""
        return f"Moto: {self.marca} {self.modelo} ({self.cilindradas}cc)"
