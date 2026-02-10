from .veiculo import Veiculo
from app.utilitarios.validadores import ValidadorVeiculo


class Carro(Veiculo):
    def __init__(self, marca, modelo, preco, portas):
        super().__init__(marca, modelo, preco)
        self.portas = portas

    @property
    def preco(self):  # uso de @property para controlar o acesso aos dados
        return f"R$ {self._preco:,.2f}"

    @preco.setter
    def preco(self, valor: float):
        if ValidadorVeiculo.validar_preco(valor):
            self._preco = valor
        else:
            raise ValueError("Preço inválido para o cadastro do veículo.")

    def calcular_ipva(self):
        return self._preco * 0.04  # Exemplo de lógica específica
