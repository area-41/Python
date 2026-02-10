import unittest
from app.utilitarios.validadores import ValidadorVeiculo


class TestValidadorVeiculo(unittest.TestCase):

    def test_preco_valido(self):
        """Testa se preços positivos retornam True"""
        self.assertTrue(ValidadorVeiculo.validar_preco(15000))
        self.assertTrue(ValidadorVeiculo.validar_preco(0.1))

    def test_preco_invalido(self):
        """Testa se preços negativos ou zero retornam False"""
        self.assertFalse(ValidadorVeiculo.validar_preco(-500))
        self.assertFalse(ValidadorVeiculo.validar_preco(0))
        self.assertFalse(ValidadorVeiculo.validar_preco("mil"))

    def test_placa_mercosul(self):
        """Testa o padrão de placas Mercosul (ex: ABC1D23)"""
        self.assertTrue(ValidadorVeiculo.validar_placa("ABC1D23"))
        self.assertTrue(ValidadorVeiculo.validar_placa("bra3r19"))  # Minúsculo deve funcionar

    def test_placa_invalida(self):
        """Testa placas fora do padrão"""
        self.assertFalse(ValidadorVeiculo.validar_placa("ABC-1234"))  # Traço não permitido no seu regex
        self.assertFalse(ValidadorVeiculo.validar_placa("1234567"))


if __name__ == "__main__":
    unittest.main()
