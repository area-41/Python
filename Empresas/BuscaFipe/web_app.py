import streamlit as st
import pandas as pd
from core.fipe_handler import FipeAPI

# Configuração da Página
st.set_page_config(page_title="Consulta Tabela FIPE 2026", page_icon="🚗")


def main():
    api = FipeAPI()

    st.title("🚗 Consulta Tabela FIPE")
    st.write(f"Letra selecionada: {letra}")
    st.write(f"Quantidade de marcas encontradas: {len(marcas_filtradas)}")
    if st.checkbox("Mostrar tabela de marcas filtradas"):
       st.write(marcas_filtradas)
    
    st.markdown("Busque preços atualizados de veículos de forma simples.")

    # --- PASSO 1: FILTRO ALFABÉTICO ---
    st.sidebar.header("Filtros")
    letra = st.sidebar.selectbox("Selecione a letra inicial da marca:",
                                 list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    marcas_df = api.listar_marcas()
    
    if not marcas_df.empty:
        # Filtragem por letra
        marcas_filtradas = marcas_df[marcas_df['nome'].str.startswith(letra)]

        if not marcas_filtradas.empty:
            # Passo 2: Seleção de Marca
            opcoes_marcas = dict(zip(marcas_filtradas['nome'], marcas_filtradas['codigo']))
            marca_nome = st.selectbox("Selecione a Marca:", options=list(opcoes_marcas.keys()))
            id_marca = opcoes_marcas[marca_nome]

            # Passo 3: Seleção de Modelo
            modelos_df = api.listar_modelos(id_marca)
            if not modelos_df.empty:
                opcoes_modelos = dict(zip(modelos_df['nome'], modelos_df['codigo']))
                modelo_nome = st.selectbox("Selecione o Modelo:", options=list(opcoes_modelos.keys()))
                id_modelo = opcoes_modelos[modelo_nome]

                # Passo 4: Seleção de Ano
                anos_df = api.listar_anos(id_marca, id_modelo)
                if not anos_df.empty:
                    opcoes_anos = dict(zip(anos_df['nome'], anos_df['codigo']))
                    ano_nome = st.selectbox("Selecione o Ano/Combustível:", options=list(opcoes_anos.keys()))
                    id_ano = opcoes_anos[ano_nome]

                    # BOTÃO DE BUSCA
                    if st.button("Consultar Preço"):
                        resultado = api.buscar_preco_final(id_marca, id_modelo, id_ano)

                        if not resultado.empty:
                            st.success(f"### Valor: {resultado['Valor'].iloc[0]}")

                            # Exibição organizada em colunas
                            col1, col2 = st.columns(2)
                            with col1:
                                st.write(f"**Marca:** {resultado['Marca'].iloc[0]}")
                                st.write(f"**Modelo:** {resultado['Modelo'].iloc[0]}")
                            with col2:
                                st.write(f"**Ano:** {resultado['AnoModelo'].iloc[0]}")
                                st.write(f"**Combustível:** {resultado['Combustivel'].iloc[0]}")

                            st.caption(f"Referência: {resultado['MesReferencia'].iloc[0]}")
        else:
            st.warning(f"Nenhuma marca encontrada com a letra {letra}.")


if __name__ == "__main__":
    main()
