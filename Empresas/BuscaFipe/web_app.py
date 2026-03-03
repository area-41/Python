import streamlit as st
import pandas as pd
from core.fipe_handler import FipeAPI

# Configuração da Página
st.set_page_config(page_title="Consulta Tabela FIPE 2026", page_icon="🚗")


def main():
    api = FipeAPI()
    
    st.title("🚗 Consulta Tabela FIPE")
    st.markdown("Busque preços atualizados de veículos de forma simples.")

    # 1. Sidebar para a Letra (Garante que 'letra' sempre exista)
    st.sidebar.header("Filtros")
    letra = st.sidebar.selectbox(
        "Selecione a letra inicial da marca:", 
        list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        index=0 # Começa no 'A' por padrão
    )

    # Agora st.write funcionará, pois 'letra' já foi definida acima
    st.write(f"Filtrando marcas que começam com: **{letra}**")

    # 2. Busca de Marcas
    marcas_df = api.listar_marcas()
    
    if not marcas_df.empty:
        # Filtro flexível para evitar erros de espaços ou maiúsculas/minúsculas
        marcas_filtradas = marcas_df[
            marcas_df['nome'].str.strip().str.upper().str.startswith(letra)
        ]
        
        if not marcas_filtradas.empty:
            # Seleção de Marca
            opcoes_marcas = dict(zip(marcas_filtradas['nome'], marcas_filtradas['codigo']))
            marca_nome = st.selectbox("Selecione a Marca:", options=list(opcoes_marcas.keys()))
            id_marca = opcoes_marcas[marca_nome]

            # Seleção de Modelo
            modelos_df = api.listar_modelos(id_marca)
            if not modelos_df.empty:
                opcoes_modelos = dict(zip(modelos_df['nome'], modelos_df['codigo']))
                modelo_nome = st.selectbox("Selecione o Modelo:", options=list(opcoes_modelos.keys()))
                id_modelo = opcoes_modelos[modelo_nome]

                # Seleção de Ano
                anos_df = api.listar_anos(id_marca, id_modelo)
                if not anos_df.empty:
                    opcoes_anos = dict(zip(anos_df['nome'], anos_df['codigo']))
                    ano_nome = st.selectbox("Selecione o Ano/Combustível:", options=list(opcoes_anos.keys()))
                    id_ano = opcoes_anos[ano_nome]

                    # Resultado Final
                    if st.button("Consultar Preço"):
                        resultado = api.buscar_preco_final(id_marca, id_modelo, id_ano)
                        if not resultado.empty:
                            st.success(f"### Valor: {resultado['Valor'].iloc[0]}")
                            st.info(f"**Modelo:** {resultado['Modelo'].iloc[0]} | **Referência:** {resultado['MesReferencia'].iloc[0]}")
        else:
            st.warning(f"Nenhuma marca encontrada com a letra '{letra}'.")

if __name__ == "__main__":
    main()
