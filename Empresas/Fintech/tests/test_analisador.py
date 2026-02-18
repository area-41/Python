import unittest
import sys
import os
from src.modelos import PropostaEmprestimo
from src.servicos import ServicoAnaliseRisco


# Ajuste de caminho para os testes localizarem o pacote src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestServicoAnaliseRisco(unittest.TestCase):
    def setUp(self):
        self.servico = ServicoAnaliseRisco()

    def test_analise_negada_acima_limite(self):
        p = PropostaEmprestimo(3000, 1000)  # 33.3%
        res = self.servico.validar_proposta(p)
        self.assertFalse(res["aprovado"])

    def test_analise_aprovada_no_limite(self):
        p = PropostaEmprestimo(3000, 900)  # 30% cravados
        res = self.servico.validar_proposta(p)
        self.assertTrue(res["aprovado"])


if __name__ == "__main__":
    unittest.main()
