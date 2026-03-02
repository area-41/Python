import requests
import pandas as pd


class FipeAPI:
    BASE_URL = "https://parallelum.com.br/fipe/api/v1/carros/marcas"

    def _get_as_df(self, endpoint):
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.get(url, timeout=15)
            # Se der erro 500 ou 404, tratamos aqui sem quebrar o app
            if response.status_code != 200:
                print(f"\n[Aviso] A API não encontrou dados para esta seleção (Status {response.status_code}).")
                return pd.DataFrame()

            data = response.json()
            if isinstance(data, dict) and 'modelos' in data:
                return pd.DataFrame(data['modelos'])
            return pd.DataFrame(data) if isinstance(data, list) else pd.DataFrame([data])
        except Exception as e:
            print(f"\n[Erro Crítico] Falha de conexão: {e}")
            return pd.DataFrame()


    def listar_marcas(self):
        return self._get_as_df("")

    def listar_modelos(self, marca_id):
        return self._get_as_df(f"/{marca_id}/modelos")

    def listar_anos(self, marca_id, modelo_id):
        return self._get_as_df(f"/{marca_id}/modelos/{modelo_id}/anos")

    def buscar_preco_final(self, marca_id, modelo_id, ano_id):
        return self._get_as_df(f"/{marca_id}/modelos/{modelo_id}/anos/{ano_id}")