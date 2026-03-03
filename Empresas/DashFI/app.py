import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(page_title="Dashboard Financeiro", layout="wide")

st.title("Monitor de Ativos em Tempo Real")
st.markdown("Selecione o ativo abaixo para visualizar a cotação e o histórico.")

# 1. Menu de Escolha (Sidebar)
with st.sidebar:
    st.header("Configurações")
    # Lista de ativos para o usuário escolher
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

# 2. Busca de Dados via yfinance
ticker_data = yf.Ticker(ticker_symbol)
df = ticker_data.history(period=periodo)

# 3. Verificação de Dados e Exibição de Métricas
if len(df) > 1:  # Garante que temos pelo menos 2 linhas para calcular a variação
    preco_atual = df['Close'].iloc[-1]
    preco_anterior = df['Close'].iloc[-2]
    variacao = preco_atual - preco_anterior
    pct_variacao = (variacao / preco_anterior) * 100

    col1, col2 = st.columns(2)
    col1.metric(
        label=f"Preço Atual ({escolha})", 
        value=f"{preco_atual:.2f}", 
        delta=f"{pct_variacao:.2f}%"
    )
    
    # 4. Gráfico Interativo
    fig = go.Figure(data=[go.Candlestick(
                x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
    
    fig.update_layout(title=f"Histórico de Preços - {escolha}", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

elif len(df) == 1:
    st.warning("Dados insuficientes para calcular a variação (apenas 1 registro encontrado).")
    st.metric(label=f"Preço Atual ({escolha})", value=f"{df['Close'].iloc[-1]:.2f}")
else:
    st.error(f"Nenhum dado encontrado para o ticker '{ticker_symbol}'. Verifique se o mercado está aberto ou se o símbolo está correto.")

  
    # Exibir tabela de dados brutos
    with st.expander("Ver dados brutos"):
        st.write(df)
else:
    st.error("Erro ao carregar dados. Verifique o Ticker ou sua conexão.")
