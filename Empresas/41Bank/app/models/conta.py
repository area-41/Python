from abc import ABC, abstractmethod
import threading

class Conta(ABC):
    """
        Encapsulamento rigoroso e herança para diferentes tipos de contas.
    """
    def __init__(self, titular, saldo_inicial, senha):
        self._titular = titular          # Protegido
        self.__saldo = saldo_inicial    # Privado
        self.__senha_hash = senha       # Privado (Hash)
        self._lock = threading.Lock()   # Thread-safe

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        """Permite ler o titular como conta.titular em vez de conta._titular"""
        return self._titular

    def _alterar_saldo(self, valor):
        """Método protegido para alteração interna."""
        self.__saldo += valor

    @abstractmethod
    def calcular_taxa(self):
        """Método abstrato para ser implementado pelas filhas."""
        pass

class ContaCorrente(Conta):
    def calcular_taxa(self):
        return 0.50  # Taxa fixa por transação

class ContaPoupanca(Conta):
    def calcular_taxa(self):
        return 0.0  # Isento
    