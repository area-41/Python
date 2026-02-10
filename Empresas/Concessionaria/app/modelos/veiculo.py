from abc import ABC, abstractmethod


class Veiculo(ABC):
    """
        Classe com uso de módulo abc para criar uma classe que não pode ser instanciada diretamente, apenas herdada
    """
    def __init__(self, marca: str, modelo: str, preco: float):
        self.marca = marca
        self.modelo = modelo
        self._preco = preco  # Protegido para o Encapsulamento

    @property
    @abstractmethod
    def preco(self):
        """Método abstrato para garantir que as subclasses implementem o Getter"""
        pass

    @abstractmethod
    def calcular_ipva(self):
        """Cada tipo de veículo terá seu cálculo específico"""
        pass
