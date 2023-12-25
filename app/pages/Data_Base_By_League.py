import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import warnings
warnings.filterwarnings("ignore")


st.set_page_config(
    page_title="Fornicador Data Base - Leagues Data",
    page_icon=":bar_chart:",
    layout="wide",
)
st.title("⚽ Leagues Data Base ⚽")

st.markdown(
    """
    <span style="color: green">**⭐ Soccer Data Analysis ⭐**</span><br>
    <span style="color: orange">*Betting is not about who Win's!!!*</span><br>
    <span style="color: #FFc048">** By RedLegacy227.**</span>  
    """,
    unsafe_allow_html=True,
)

ligas = [
    'VIETNAME - LIGA V',
    'COLÔMBIA - PRIMEIRA A',
    'COLÔMBIA - PRIMEIRA B',
    'PARAGUAI - PRIMEIRA DIVISÃO',
    'ARGENTINA - TAÇA DA LIGA PROFISSIONAL',
    'EQUADOR - LIGA PRO',
    'JAPÃO - LIGA J1',
    'COREIA DO SUL - LIGA K1',
    'COREIA DO SUL - LIGA K2',
    'GEÓRGIA - PRIMEIRA LIGA',
    'MALÁSIA - SUPER LIGA',
    'BOLÍVIA - DIVISÃO PROFISSIONAL',
    'PERU - LIGA 1',
    'SINGAPURA - PRIMEIRA LIGA',
    'IRLANDA - PRIMEIRA DIVISÃO',
    'CHILE - PRIMEIRA DIVISÃO',
    'SUÉCIA - ALLSVENSKAN',
    'SUÉCIA - SUPERETTAN',
    'VENEZUELA - LIGA FUTVE',
    'EUA - MLS',
    'CHINA - SUPER LIGA',
    'CHINA - LIGA JIA',
    'FINLÂNDIA - PRIMEIRA LIGA',
    'FINLÂNDIA - SEGUNDA LIGA',
    'NORUEGA - LIGA DE ELITE',
    'NORUEGA - SEGUNDA LIGA',
    'URUGUAI - PRIMEIRA DIVISÃO',
    'BRASIL - SERIE B',
    'BRASIL - SÉRIE A',
    'CANADÁ - PRIMEIRA LIGA',
    'JAMAICA - PRIMEIRA LIGA',
    'ROMÉNIA - LIGA 1',
    'BÓSNIA E HERZEGOVINA - PRIMEIRA LIGA',
    'CROÁCIA - PRIMEIRA LIGA',
    'DINAMARCA - SUPER LIGA',
    'SÉRVIA - SUPER LIGA',
    'ARGENTINA - LIGA PROFISSIONAL',
    'ALEMANHA - 2. BUNDESLIGA',
    'BULGÁRIA - LIGA PARVA',
    'BÉLGICA - PRIMEIRA LIGA',
    'DINAMARCA - PRIMEIRA DIVISÃO',
    'MÉXICO - LIGA MX',
    'POLÓNIA - PRIMEIRA LIGA',
    'SUIÇA - SEGUNDA LIGA',
    'UCRÂNIA - PRIMEIRA LIGA',
    'ÁUSTRIA - PRIMEIRA LIGA',
    'ÁUSTRIA - SEGUNDA LIGA',
    'ALEMANHA - 3. LIGA',
    'FRANÇA - LIGA2',
    'REPÚBLICA CHECA - PRIMEIRA LIGA',
    'SUIÇA - SUPER LIGA',
    'COSTA RICA - PRIMEIRA DIVISÃO',
    'MÉXICO - LIGA DE EXPANSION MX',
    'ESCÓCIA - CAMPEONATO',
    'ESCÓCIA - PRIMEIRA LIGA',
    'ROMÉNIA - LIGA 2',
    'FRANÇA - LIGA 1',
    'INGLATERRA - CAMPEONATO',
    'PAÍSES BAIXOS - PRIMEIRA DIVISÃO',
    'PORTUGAL - LIGA PORTUGAL',
    'INGLATERRA - LIGA 1',
    'INGLATERRA - LIGA 2',
    'PORTUGAL - LIGA PORTUGAL 2',
    'ARÁBIA SAUDITA - PRIMEIRA LIGA',
    'ALEMANHA - BUNDESLIGA',
    'CROÁCIA - PRVA NL',
    'ESPANHA - LALIGA',
    'ESPANHA - LALIGA2',
    'INGLATERRA - PREMIER LEAGUE',
    'PAÍS DE GALES - PRIMEIRA LIGA CYMRU',
    'PAÍSES BAIXOS - EREDIVISIE',
    'PORTUGAL - LIGA 3',
    'TURQUIA - LIGA 1',
    'TURQUIA - SUPER LIGA',
    'ITÁLIA - SÉRIE B',
    'ÁFRICA DO SUL - PRIMEIRA LIGA',
    'ITÁLIA - SÉRIE A',
    'INDONÉSIA - LIGA 1',
    'IRLANDA DO NORTE - PRIMEIRA LIGA NIFL',
    'TAILÂNDIA - LIGA 1',
    'CATAR - PRIMEIRA LIGA',
    'GRÉCIA - SUPER LIGA',
    'ANGOLA - GIRABOLA',
    'HONG KONG - PRIMEIRA LIGA',
    'EGIPTO - PRIMEIRA LIGA',
    'GRÉCIA - SUPER LIGA 2',
    'AUSTRÁLIA - LIGA A',
    'ÍNDIA - SUPER LIGA',
]

ligas_ordenadas = sorted(ligas)

with st.sidebar:
    st.sidebar.header("⚽ Leagues Data Base ⚽")
    st.sidebar.image("Fornicador.tif", use_column_width=True)
    selected_league = st.sidebar.selectbox("Leagues", ligas_ordenadas)


def load_data(league):
    print("Carregando arquivo CSV...")
    data = pd.read_csv("https://github.com/RedLegacy227/fornicador/blob/main/dados_csv/fornicador_dados_gerais.csv?raw=True")
    print("Arquivo CSV carregado!")
    data = data[data["League"] == league]
    return data

df = load_data(selected_league)
st.subheader("Selected League - " + selected_league)

st.dataframe(df)
