import unittest
from core.fipe_handler import FipeAPI


class TestFipeFlow(unittest.TestCase):
    def setUp(self):
        self.api = FipeAPI()

    def test_fluxo_completo_amarok(self):
        # Testando se a sequência de IDs 59 -> 5940 -> 2014-3 ainda é válida
        df = self.api.buscar_preco_final("59", "5940", "2014-3")
        self.assertFalse(df.empty)
        self.assertEqual(df['Marca'][0], "VW - VolksWagen")

    def test_input_invalido(self):
        api = FipeAPI()
        # Forçando um ID que não existe
        df = api.buscar_preco_final("999", "9999", "0000-0")
        self.assertTrue(df.empty)  # O app deve retornar um DF vazio em vez de quebrar

    def test_filtro_alfabetico(self):
        api = FipeAPI()
        marcas = api.listar_marcas()
        # Testa se existem marcas com 'V' (como VW e Volvo)
        marcas_v = marcas[marcas['nome'].str.startswith('V')]
        self.assertFalse(marcas_v.empty)
        self.assertIn('VW - VolksWagen', marcas_v['nome'].values)

if __name__ == "__main__":
    unittest.main()
