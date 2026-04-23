import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Dashboard Financeiro", layout="wide")

st.title("Monitor de Ativos em Tempo Real")

# 1. Menu de Escolha (Sidebar)
with st.sidebar:
    st.header("Configurações")
    ticker_dict = {
        "Bitcoin (BTC)": "BTC-USD",
        "Dólar (USD)": "USDBRL=X",
        "Copel (CPLE3)": "CPLE3.SA",
        "Petrobras (PETR4)": "PETR4.SA",
        "Ethereum (ETH)": "ETH-USD"
    }
    
    escolha = st.selectbox("Selecione o Ativo:", list(ticker_dict.keys()))
    ticker_symbol = ticker_dict[escolha]
    
    periodo = st.select_slider("Período do Histórico:", 
                               options=["1d", "5d", "1mo", "6mo", "1y", "5y"], 
                               value="1mo")

# 2. Busca de Dados
@st.cache_data(ttl=3600) # Otimiza a performance salvando em cache por 1 hora
def buscar_dados(ticker, p):
    return yf.Ticker(ticker).history(period=p)

df = buscar_dados(ticker_symbol, periodo)

# 3. Lógica de Exibição
if not df.empty:
    if len(df) > 1:
        preco_atual = df['Close'].iloc[-1]
        preco_anterior = df['Close'].iloc[-2]
        variacao = preco_atual - preco_anterior
        pct_variacao = (variacao / preco_anterior) * 100

        col1, col2 = st.columns([1, 3])
        with col1:
            st.metric(label=f"Preço Atual ({escolha})", 
                      value=f"{preco_atual:.2f}", 
                      delta=f"{pct_variacao:.2f}%")
            
            # Botão para baixar os dados (Persistência)
            csv = df.to_csv().encode('utf-8')
            st.download_button(
                label="📥 Baixar Dados (CSV)",
                data=csv,
                file_name=f'{ticker_symbol}_historico.csv',
                mime='text/csv',
            )
        
        with col2:
            # 4. Gráfico Interativo
            fig = go.Figure(data=[go.Candlestick(
                        x=df.index,
                        open=df['Open'],
                        high=df['High'],
                        low=df['Low'],
                        close=df['Close'])])
            
            fig.update_layout(height=450, template="plotly_dark", margin=dict(l=20, r=20, t=20, b=20))
            st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("Dados insuficientes para análise de variação.")
        st.write(df)

    # Expander para dados brutos fora do fluxo principal
    with st.expander("🔍 Ver tabela de dados completa"):
        st.dataframe(df, use_container_width=True)

else:
    st.error(f"Não foi possível encontrar dados para {ticker_symbol}. O mercado pode estar fechado ou o ticker está incorreto.")
