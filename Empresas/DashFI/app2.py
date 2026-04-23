import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# 1. Configuração da Página
st.set_page_config(page_title="Dashboard VIP Financeiro", layout="wide")

# 2. Dicionário de Ativos e Imagens de Fundo (Temáticas)
# A opacidade é controlada no CSS abaixo (0.3 de opacidade = 70% de transparência)
ativos_config = {
    "Bitcoin (BTC)": {
        "ticker": "BTC-USD",
        "bg_img": "https://images.unsplash.com/photo-1518546305927-5a555bb7020d?q=80&w=2069"
    },
    "Dólar (USD)": {
        "ticker": "USDBRL=X",
        "bg_img": "https://images.unsplash.com/photo-1502920514313-52581002a659?q=80&w=2067"
    },
    "Copel (CPLE3)": {
        "ticker": "CPLE3.SA",
        "bg_img": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?q=80&w=2070" # Energia/Linhas
    },
    "Petrobras (PETR4)": {
        "ticker": "PETR4.SA",
        "bg_img": "https://images.unsplash.com/photo-1516195851888-6f1a981a862e?q=80&w=2013" # Plataforma/Óleo
    },
    "Ethereum (ETH)": {
        "ticker": "ETH-USD",
        "bg_img": "https://images.unsplash.com/photo-1622790698141-94e30457ef12?q=80&w=2072"
    }
}

# 3. Sidebar - Escolha do Usuário
with st.sidebar:
    st.header("⚙️ Configurações")
    escolha = st.selectbox("Selecione o Ativo:", list(ativos_config.keys()))
    periodo = st.select_slider("Período:", options=["1d", "5d", "1mo", "1y", "5y"], value="1mo")
    
    st.markdown("---")
    st.markdown("### 📚 Fontes de Dados")
    st.markdown("- [Yahoo Finance](https://finance.yahoo.com/) (Cotações)")
    st.markdown("- [Unsplash](https://unsplash.com/) (Imagens de Fundo)")
    st.info("Nota: Os dados podem ter atraso de até 15 min.")

# 4. Injeção de CSS para Fundo Dinâmico (Alpha 70%)
bg_url = ativos_config[escolha]["bg_img"]
st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url("{bg_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    /* Melhora a legibilidade dos cards */
    [data-testid="stMetricValue"], [data-testid="stMarkdownContainer"] {{
        text-shadow: 2px 2px 4px #000000;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 5. Lógica de Dados
ticker_symbol = ativos_config[escolha]["ticker"]
df = yf.Ticker(ticker_symbol).history(period=periodo)

# 6. Interface Principal
st.title(f"📊 Monitor: {escolha}")

if not df.empty and len(df) > 1:
    preco_atual = df['Close'].iloc[-1]
    variacao = ((df['Close'].iloc[-1] / df['Close'].iloc[-2]) - 1) * 100
    
    col1, col2 = st.columns([1, 4])
    with col1:
        st.metric(label="Preço Atual", value=f"{preco_atual:.2f}", delta=f"{variacao:.2f}%")
        csv = df.to_csv().encode('utf-8')
        st.download_button("📥 Baixar Histórico CSV", data=csv, file_name=f"{ticker_symbol}.csv")

    with col2:
        fig = go.Figure(data=[go.Candlestick(
            x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close']
        )])
        fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
else:
    st.error("Dados indisponíveis no momento.")
