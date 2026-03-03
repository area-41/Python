import streamlit as st
import pandas as pd
from core.fipe_handler import FipeAPI

# Configuração da Página
st.set_page_config(page_title="Consulta Tabela FIPE 2026", page_icon="🚗")

def main():
    api = FipeAPI()
    
    st.title("🚗 Consulta Tabela FIPE")
    st.markdown("Busque preços atualizados de veículos de forma simples.")

    # 1. Sidebar para a Letra
    st.sidebar.header("Filtros")
    letra = st.sidebar.selectbox(
        "Selecione a letra inicial da marca:", 
        list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        index=0
    )

    st.write(f"Filtrando marcas que começam com: **{letra}**")

    # 2. Busca de Marcas
    marcas_df = api.listar_marcas()
    
    if not marcas_df.empty:
        # A LINHA ABAIXO DEVE ESTAR IDENTADA (4 ESPAÇOS OU 1 TAB)
        # Debug para ver o que a API está trazendo
        # st.write("🔍 Debug - Primeiras marcas:", marcas_df['nome'].head().tolist())

        # Filtro robusto: Remove espaços e garante comparação em maiúsculo
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

                    if st.button("Consultar Preço"):
                        resultado = api.buscar_preco_final(id_marca, id_modelo, id_ano)
                        if not resultado.empty:
                            st.success(f"### Valor: {resultado['Valor'].iloc[0]}")
                            st.info(f"**Modelo:** {resultado['Modelo'].iloc[0]}")
                            
                            # Botão de download CSV que criamos anteriormente
                            csv = resultado.to_csv(index=False).encode('utf-8')
                            st.download_button("📥 Baixar CSV", csv, "fipe.csv", "text/csv")
        else:
            st.warning(f"Nenhuma marca encontrada com a letra '{letra}'.")
    else:
        st.error("Erro ao conectar com a API. Verifique sua conexão.")

if __name__ == "__main__":
    main()
