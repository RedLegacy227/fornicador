import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image



st.set_page_config(
    page_title="Fornicador Data Analysis",
    page_icon=":bar_chart:",
    layout="wide",
)
st.title("⚽ Next Games ⚽")

st.markdown(
    """
    <span style="color: green">**⭐ Soccer Data Analysis ⭐**</span><br>
    <span style="color: orange">*Betting is not about who Win's!!!*</span><br>
    <span style="color: #FFc048">** By RedLegacy227.**</span>  
    """,
    unsafe_allow_html=True,
)

def load_data_jogos():
    data_jogos = pd.read_csv(
        "https://github.com/RedLegacy227/fornicador/blob/main/dados_csv/proximos_jogos.csv?raw=True"
    )
    data_jogos = data_jogos[
        [
            "League",
            "Date",
            "Time",
            "Round",
            "Home",
            "Away",
            "Class_Home",
            "Class_Away",
            "FT_Odd_H",
            "FT_Odd_D",
            "FT_Odd_A",
            "HT_Odd_Over05",
            "HT_Odd_Under05",
            "FT_Odd_Over15",
            "FT_Odd_Under15",
            "FT_Odd_Over25",
            "FT_Odd_Under25",
            "FT_Odd_Over35",
            "FT_Odd_Under35",
            "FT_Odd_BTTS_Yes",
            "FT_Odd_BTTS_No",
            "p_H",
            "p_D",
            "p_A",
            "CV_HDA",
            "P_expt_H",
            "P_expt_A",
            "PPJ_H",
            "CV_PPJ_H",
            "PPJ_A",
            "CV_PPJ_A",
            "Power_Ranking_HT_H",
            "CV_Power_Ranking_HT_H",
            "Power_Ranking_HT_A",
            "CV_Power_Ranking_HT_A",
            "Power_Ranking_FT_H",
            "CV_Power_Ranking_FT_H",
            "Power_Ranking_FT_A",
            "CV_Power_Ranking_FT_A",
            "Media_Geral_GM_H",
            "Media_Geral_GS_H",
            "Media_Geral_GM_A",
            "Media_Geral_GS_A",
            "Media_GM_H_6j",
            "Media_GS_H_6j",
            "Media_GM_A_6j",
            "Media_GS_A_6j",
            "Media_Saldo_Golos_H_HT",
            "CV_Saldo_Golos_H_HT",
            "Media_Saldo_Golos_A_HT",
            "CV_Saldo_Golos_A_HT",
            "Media_Saldo_Golos_H_FT",
            "CV_Saldo_Golos_H_FT",
            "Media_Saldo_Golos_A_FT",
            "CV_Saldo_Golos_A_FT",
            "Media_Total_1HT_H",
            "CV_Media_Total_1HT_H",
            "Media_Total_1HT_A",
            "CV_Media_Total_1HT_A",
            "Media_Total_2HT_H",
            "CV_Media_Total_2HT_H",
            "Media_Total_2HT_A",
            "CV_Media_Total_2HT_A",
            "Average_Goals_Scored_by_Home_Teams",
            "Average_Goals_Conceded_by_Home_Teams",
            "Average_Goals_Scored_by_Away_Teams",
            "Average Goals Conceded by Away Teams",
            "Media_primeiro_gol_home",
            "Media_primeiro_gol_away",
            "Media_primeiro_gol_home_sofrido",
            "Media_primeiro_gol_away_sofrido",
            "Porc_Marcou_Primeiro_Golo_H_1P",
            "Porc_Marcou_Primeiro_Golo_A_1P",
            "Porc_Sofreu_Primeiro_Golo_H_1P",
            "Porc_Sofreu_Primeiro_Golo_A_1P",
            "Porc_Marcou_Primeiro_Golo_H",
            "Porc_Marcou_Primeiro_Golo_A",
            "Porc_Sofreu_Primeiro_Golo_H",
            "Porc_Sofreu_Primeiro_Golo_A",
            "media_chutes_home",
            "media_chutes_away",
            "media_chutes_por_gol_H",
            "media_chutes_por_gol_A",
            "media_movel_chutes_por_gol_H",
            "media_movel_chutes_por_gol_A",
            "media_ataques_perigosos_por_gol_H",
            "media_ataques_perigosos_por_gol_A",
            "media_movel_ataques_perigosos_por_gol_H",
            "media_movel_ataques_perigosos_por_gol_A",
            "media_cartoes_amarelos_H",
            "media_cartoes_amarelos_A",
            "media_movel_media_cartoes_amarelos_H",
            "media_movel_media_cartoes_amarelos_A",
            "media_cartoes_vermelhos_H",
            "media_cartoes_vermelhos_A",
            "media_movel_media_cartoes_vermelhos_H",
            "media_movel_media_cartoes_vermelhos_A",
            "Media_FT_Corners_H_MAR",
            "CV_Corners_H_MAR",
            "Media_FT_Corners_A_MAR",
            "CV_Corners_A_MAR",
            "Media_FT_Corners_H_SFR",
            "CV_Corners_H_SFR",
            "Media_FT_Corners_A_SFR",
            "CV_Corners_A_SFR",
            "Media_VG_H",
            "CV_VG_H",
            "Media_VG_A",
            "CV_VG_A",
            "Media_CG_H",
            "CV_CG_H",
            "Media_CG_A",
            "CV_CG_A",
            "Porc_Over05HT_Home",
            "Porc_Over05HT_Away",
            "Porc_Under05HT_Home",
            "Porc_Under05HT_Away",
            "Porc_Over15HT_Home",
            "Porc_Over15HT_Away",
            "Porc_Under15HT_Home",
            "Porc_Under15HT_Away",
            "Porc_Over15FT_Home",
            "Porc_Over15FT_Away",
            "Porc_Under15FT_Home",
            "Porc_Under15FT_Away",
            "Porc_Over25FT_Home",
            "Porc_Over25FT_Away",
            "Porc_Under25FT_Home",
            "Porc_Under25FT_Away",
            "Porc_Over35FT_Home",
            "Porc_Over35FT_Away",
            "Porc_Under35FT_Home",
            "Porc_Under35FT_Away",
            "Porc_BTTS_Yes_Home",
            "Porc_BTTS_Yes_Away",
            "Porc_BTTS_No_Home",
            "Porc_BTTS_No_Away",
            "Porc_Home_Win_HT",
            "Porc_Away_Win_HT",
            "Porc_Home_Win_FT",
            "Porc_Away_Win_FT",
            "0x0_Home",
            "0x0_Away",
            "1x0_Home",
            "1x0_Away",
            "1x1_Home",
            "1x1_Away",
            "0x1_Home",
            "0x1_Away",
            "2x0_Home",
            "2x0_Away",
            "2x1_Home",
            "2x1_Away",
            "2x2_Home",
            "2x2_Away",
            "0x2_Home",
            "0x2_Away",
            "1x2_Home",
            "1x2_Away",
            "3x0_Home",
            "3x0_Away",
            "3x1_Home",
            "3x1_Away",
            "3x2_Home",
            "3x2_Away",
            "3x3_Home",
            "3x3_Away",
            "0x3_Home",
            "0x3_Away",
            "1x3_Home",
            "1x3_Away",
            "2x3_Home",
            "2x3_Away",
            "Goleada_Home",
            "Goleada_Away",
            "O_qualquer_Empate_Home",
            "O_qualquer_Empate_Away"
        ]
    ]

    return data_jogos


df_jogos = load_data_jogos()

with st.sidebar:
    st.sidebar.header("⚽ Next Games Web App ⚽")
    st.sidebar.image("Fornicador.tif", use_column_width=True)

    with st.expander("Data Sellection"):
        sorted_unique_date = sorted(df_jogos.Date.unique())
        selected_date = st.multiselect("Date", sorted_unique_date, sorted_unique_date)
        if not selected_date:
            st.warning("Chose a Date to Analyse.")
        else:
            df_jogos = df_jogos[df_jogos["Date"].isin(selected_date)]


# Define o valor mínimo e máximo iniciais com base na coluna "FT_Odd_H" do DataFrame
valor_min_home = float(df_jogos["FT_Odd_H"].min())
valor_max_home = float(df_jogos["FT_Odd_H"].max())
valor_min_draw = float(df_jogos["FT_Odd_D"].min())
valor_max_draw = float(df_jogos["FT_Odd_D"].max())
valor_min_away = float(df_jogos["FT_Odd_A"].min())
valor_max_away = float(df_jogos["FT_Odd_A"].max())
valor_min_over = float(df_jogos["FT_Odd_Over25"].min())
valor_max_over = float(df_jogos["FT_Odd_Over25"].max())

st.markdown(
    """
<span style="color: blue">**Odds_Filter**</span><br>
""",
    unsafe_allow_html=True,
)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    valor_min_home, valor_max_home = st.slider(
        "Home",
        float(df_jogos["FT_Odd_H"].min()),
        float(df_jogos["FT_Odd_H"].max()),
        (valor_min_home, valor_max_home),
        step=0.01,
    )
with col2:
    valor_min_draw, valor_max_draw = st.slider(
        "Draw",
        float(df_jogos["FT_Odd_D"].min()),
        float(df_jogos["FT_Odd_D"].max()),
        (valor_min_draw, valor_max_draw),
        step=0.01,
    )
with col3:
    valor_min_away, valor_max_away = st.slider(
        "Away",
        float(df_jogos["FT_Odd_A"].min()),
        float(df_jogos["FT_Odd_A"].max()),
        (valor_min_away, valor_max_away),
        step=0.01,
    )
with col4:
    valor_min_over, valor_max_over = st.slider(
        "Over 0.5 HT",
        float(df_jogos["HT_Odd_Over05"].min()),
        float(df_jogos["HT_Odd_Over05"].max()),
        (valor_min_over, valor_max_over),
        step=0.01,
    )
with col5:
    valor_min_over, valor_max_over = st.slider(
        "Over 2.5",
        float(df_jogos["FT_Odd_Over25"].min()),
        float(df_jogos["FT_Odd_Over25"].max()),
        (valor_min_over, valor_max_over),
        step=0.01,
    )


df_filtrado = df_jogos[
    (valor_min_home <= df_jogos['FT_Odd_H']) & (df_jogos['FT_Odd_H'] <= valor_max_home) &
    (valor_min_draw <= df_jogos['FT_Odd_D']) & (df_jogos['FT_Odd_D'] <= valor_max_draw) &
    (valor_min_away <= df_jogos['FT_Odd_A']) & (df_jogos['FT_Odd_A'] <= valor_max_away) &
    (valor_min_over <= df_jogos['FT_Odd_Over25']) & (df_jogos['FT_Odd_Over25'] <= valor_max_over)
]


st.subheader("Jogos do Dia")
st.markdown(f"Total jogos para o dia  de Hoje : {len(df_filtrado)} jogos")
st.dataframe(df_filtrado)
st.markdown("""---""")

# .......................................................................
# .......................................................................

df_over_ht05 = df_jogos.copy()
df_over_ft15 = df_jogos.copy()
df_over_ft25 = df_jogos.copy()
# ........................................................................

df_2tmp = df_jogos.copy()
df_l_Home = df_jogos.copy()
df_l_Away = df_jogos.copy()
df_l_zebra_H = df_jogos.copy()
df_l_zebra_A = df_jogos.copy()
df_correccoes = df_jogos.copy()
df_cs_2x2 = df_jogos.copy()
df_cs_3x1 = df_jogos.copy()
df_cs_1x3 = df_jogos.copy()
df_ltd_h = df_jogos.copy()
df_ltd_a = df_jogos.copy()
# .......................................................................

df_l_0x1 = df_jogos.copy()
df_l_1x0 = df_jogos.copy()
# .......................................................................

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(
    [
        "Overs",
        "Goal 2nd Half",
        "Lay 0x1",
        "Lay 1x0",
        "Lay Home",
        "Lay Away",
        "Lay Zebra - Alison",
        "Correcções - Alison",
        "Correct Score - Alison",
        "LTD - Alison"
    ]
)
with tab1:
    filtro_Over_ht = (
        # (df_over_ht05.Porc_Over05HT_Home >=70)&
        # (df_over_ht05.Porc_Over05HT_Away >= 70)&
        (df_over_ht05.Media_Total_1HT_H >= 0.65)
        & (df_over_ht05.Media_Total_1HT_A >= 0.70)
        & (df_over_ht05.CV_Media_Total_1HT_H <= 0.7)
        & (df_over_ht05.CV_Media_Total_1HT_A <= 0.7)
    )
    df_over_ht = df_over_ht05[filtro_Over_ht]
    st.subheader("Trend Over 0,5 HT")
    st.markdown(f"Total Games Today  : {len(df_over_ht)} games")
    st.dataframe(df_over_ht)

    filtro_Over_ft15 = (
        (df_over_ft15.Porc_Over15FT_Home >= 65)
        & (df_over_ft15.Porc_Over15FT_Away >= 65)
        & (df_over_ft15.Media_CG_H >= 3.6)
        & (df_over_ft25.CV_CG_H <= 0.7)
        & (df_over_ft15.Media_CG_A >= 3.6)
        & (df_over_ft25.CV_CG_A <= 0.7)
        & (abs(df_over_ft15.Class_Home - df_over_ft15.Class_Away) >= 3)
    )
    df_over_ft15 = df_over_ft15[filtro_Over_ft15]
    st.subheader("Trend Over 1,5 FT")
    st.markdown(f"Total Games Today  : {len(df_over_ft15)} games")
    st.dataframe(df_over_ft15)

    filtro_Over_25 = (
        (df_over_ft25.Porc_Over25FT_Home >= 65)
        & (df_over_ft25.Porc_Over25FT_Away >= 65)
        & (df_over_ft25.Media_CG_H >= 3.8)
        & (df_over_ft25.CV_CG_H <= 0.7)
        & (df_over_ft25.Media_CG_A >= 3.8)
        & (df_over_ft25.CV_CG_A <= 0.7)
    )
    df_over_25 = df_over_ft25[filtro_Over_25]
    st.subheader("Trend Over 25 FT")
    st.markdown(f"Total Games Today : {len(df_over_25)} games")
    st.dataframe(df_over_25)


with tab2:
    filtro_2tmp = (
        (df_2tmp.Media_GM_H_6j > 1.4)
        & (df_2tmp.Media_GM_A_6j > 1.4)
        & (df_2tmp.CV_Media_Total_2HT_H <= 0.7)
        & (df_2tmp.CV_Media_Total_2HT_A <= 0.7)
    )

    df_2tmp = df_2tmp[filtro_2tmp]
    st.subheader("Goal trends in the 2nd half")
    st.markdown("""---""")
    st.markdown(
        """
                For this filter, when the score at the end of the first half is equal to 0 x 0, 0 x 1, 1 x 1, 1 x 0, 1 x 2 or 2 x 1 as long as if we have a team at a disadvantage they are running behind of the result
                 We consider looking for a bet on Asian goals with a longer time interval, depending on the dynamics of the match and the performance of the teams. Our goal is to find opportunities with minimum odds of at least @1.60 on the Over limit and @2.00 for the Asian.
                """
    )
    st.markdown(f"Total Games Today  : {len(df_2tmp)} games")
    st.dataframe(df_2tmp)
    st.markdown("""---""")

with tab3:
    filtro_lay0x1 = (
        (df_l_0x1["0x1_Home"] == 0)
        & (df_l_0x1["0x1_Away"] == 0)
        & (df_l_0x1["Media_CG_H"] >= 3.8)
        & (df_l_0x1["CV_CG_H"] <= 0.8)
        & (df_l_0x1["Media_primeiro_gol_home"] < df_l_0x1["Media_primeiro_gol_away"])
        & (df_l_0x1["Media_primeiro_gol_home"] <= 50)
    )
    df_l_0x1 = df_l_0x1[filtro_lay0x1]
    st.subheader("Lay 0x1")
    st.markdown("""---""")
    st.markdown(
        """
                For this Filter you can enter to max odd 13. We close position at 60 Minutes if 0x0 or 80 Minutes if 1x0. Our goal is not to loose full stake.
                """
    )
    st.markdown(f"Total Games Today : {len(df_l_0x1)} games")
    st.dataframe(df_l_0x1)
    st.markdown("""---""")

with tab4:
    filtro_lay1x0 = (
        (df_l_1x0["1x0_Home"] == 0)
        & (df_l_1x0["1x0_Away"] == 0)
        & (df_l_1x0["Media_CG_A"] >= 3.8)
        & (df_l_1x0["CV_CG_A"] <= 0.8)
        & (df_l_1x0["Media_primeiro_gol_away"] < df_l_1x0["Media_primeiro_gol_home"])
        & (df_l_1x0["Media_primeiro_gol_away"] <= 50)
    )

    df_l_1x0 = df_l_1x0[filtro_lay1x0]
    st.subheader("Lay 1x0")
    st.markdown("""---""")
    st.markdown(
        """
                For this Filter you can enter to max odd 13. We close position at 60 Minutes if 0x0 or 80 Minutes if 1x0. Our goal is not to loose full stake.
                """
    )
    st.markdown(f"Total Games Today : {len(df_l_1x0)} games")
    st.dataframe(df_l_1x0)
    st.markdown("""---""")

with tab5:
    filtro_lay_home = (
        ((df_l_Home["Power_Ranking_FT_A"] - df_l_Home["Power_Ranking_FT_H"]) > 2.5)
        & (df_l_Home["CV_Power_Ranking_FT_A"] <= 0.8)
        & (df_l_Home["Media_CG_A"] >= 3.6)
        & (df_l_Home["CV_CG_A"] <= 0.85)
    )
    df_l_Home = df_l_Home[filtro_lay_home]
    st.subheader("Lay Home")
    st.markdown("""---""")
    st.markdown(
        """
                For this Filter, you can enter lay home pre-live and monitor the game in live. Exit the operation if the Home team is demonstrating the opposite of what was predicted.
                """
    )
    st.markdown(f"Total Games Today : {len(df_l_Home)} games")
    st.dataframe(df_l_Home)
    st.markdown("""---""")

with tab6:
    filtro_lay_away = (
        ((df_l_Away["Power_Ranking_FT_H"] - df_l_Away["Power_Ranking_FT_A"]) >= 2.5)
        & (df_l_Away["CV_Power_Ranking_FT_H"] <= 0.8)
        & (df_l_Away["Media_CG_H"] > 3.6)
        & (df_l_Away["CV_CG_H"] <= 0.85)
    )
    df_l_Away = df_l_Away[filtro_lay_away]
    st.subheader("Lay Away")
    st.markdown("""---""")
    st.markdown(
        """
                For this Filter, you can enter lay away pre-live and monitor the game in live. Exit the operation if the Away team is demonstrating the opposite of what was predicted.
                """
    )
    st.markdown(f"Total Games Today : {len(df_l_Away)} games")
    st.dataframe(df_l_Away)
    st.markdown("""---""")

with tab7:
    filtro_lay_zebra_H = (
        (df_l_zebra_H["FT_Odd_A"] <= 1.9)
        & (
            (df_l_zebra_H["Power_Ranking_FT_A"] - df_l_zebra_H["Power_Ranking_FT_H"])
            >= 1.5
        )
        & (
            df_l_zebra_H["Porc_Marcou_Primeiro_Golo_H"]
            <= df_l_zebra_H["Porc_Marcou_Primeiro_Golo_A"]
        )
        & (df_l_zebra_H["Media_primeiro_gol_home"] <= 65)
    )
    df_l_zebra_H = df_l_zebra_H[filtro_lay_zebra_H]
    st.subheader("Trend Lay Zebra Home")
    st.markdown(f"Total Games Today  : {len(df_l_zebra_H)} games")
    st.dataframe(df_l_zebra_H)

    filtro_lay_zebra_A = (
        (df_l_zebra_A["FT_Odd_H"] <= 1.9)
        & (
            (df_l_zebra_A["Power_Ranking_FT_H"] - df_l_zebra_A["Power_Ranking_FT_A"])
            >= 1.5
        )
        & (
            df_l_zebra_A["Porc_Marcou_Primeiro_Golo_A"]
            <= df_l_zebra_A["Porc_Marcou_Primeiro_Golo_H"]
        )
        & (df_l_zebra_A["Media_primeiro_gol_away"] <= 65)
    )
    df_l_zebra_A = df_l_zebra_A[filtro_lay_zebra_A]
    st.subheader("Trend Lay Zebra Away")
    st.markdown(f"Total Games Today  : {len(df_l_zebra_A)} games")
    st.dataframe(df_l_zebra_A)

with tab8:
    # Calculate the midpoint
    midpoint = (1.90 + 4.4) / 2

    # Apply the filter to the DataFrame df_correccao_H
    filtro_correccoes = (
        (df_correccoes["FT_Odd_H"] >= midpoint - 1)
        & (df_correccoes["FT_Odd_H"] <= midpoint + 1)
        & (df_correccoes["FT_Odd_A"] >= midpoint - 1)
        & (df_correccoes["FT_Odd_A"] <= midpoint + 1)
        & (df_correccoes["FT_Odd_D"] >= 3.55)
        
        
    )

    df_correccoes = df_correccoes[filtro_correccoes]
    st.subheader("Corrections")
    st.markdown("""---""")
    st.markdown(
        """
                For this Filter, you can enter lay away to the worst team on field or back on the best time on field. Exit the operation if the team that is in your favour changes the behavior that made you enter.
                """
    )
    st.markdown(f"Total Games Today : {len(df_correccoes)} games")
    st.dataframe(df_correccoes)
    st.markdown("""---""")

with tab9:
    filtro_cs_2x2 = (
        (df_cs_2x2["FT_Odd_BTTS_Yes"] <= 1.7)
        &(df_cs_2x2["FT_Odd_Over25"] <= 1.7)
        & (abs(df_cs_2x2["FT_Odd_H"] - df_cs_2x2["FT_Odd_A"]) <= 2)
        & (df_cs_2x2["Porc_BTTS_Yes_Home"]> 33)
        
        
    )
    df_cs_2x2 = df_cs_2x2[filtro_cs_2x2]
    st.subheader("Trend Back 2x2")
    st.markdown(f"Total Games Today  : {len(df_cs_2x2)} games")
    st.dataframe(df_cs_2x2)
    
    filtro_cs_3x1 = (
        (df_cs_3x1["FT_Odd_BTTS_Yes"] <= 1.7)
        &(df_cs_3x1["FT_Odd_Over25"] <= 1.7)
        &(df_cs_3x1["FT_Odd_H"] <= 2.20)
        
        
    )
    df_cs_3x1 = df_cs_3x1[filtro_cs_3x1]
    st.subheader("Trend Back 3x1")
    st.markdown(f"Total Games Today  : {len(df_cs_3x1)} games")
    st.dataframe(df_cs_3x1)
    
    filtro_cs_1x3 = (
        (df_cs_1x3["FT_Odd_BTTS_Yes"] <= 1.7)
        &(df_cs_1x3["FT_Odd_Over25"] <= 1.7)
        &(df_cs_1x3["FT_Odd_A"] <= 2.20)
        
        
    )
    df_cs_1x3 = df_cs_1x3[filtro_cs_1x3]
    st.subheader("Trend Back 1x3")
    st.markdown(f"Total Games Today  : {len(df_cs_1x3)} games")
    st.dataframe(df_cs_1x3)
    
with tab10:

    filtro_ltd_H = (
        (df_ltd_h["FT_Odd_H"] >= 13.5)
       # & (
        #    (df_ltd_h["Power_Ranking_FT_A"] - df_ltd_h["Power_Ranking_FT_H"])
        #    >= 2)

    )
    df_ltd_h = df_ltd_h[filtro_ltd_H]
    st.subheader("Trend LTD Zebra Home")
    st.markdown(f"Total Games Today  : {len(df_ltd_h)} games")
    st.dataframe(df_ltd_h)

    filtro_ltd_A = (
        (df_ltd_a["FT_Odd_A"] >= 13.5)
        #& (
        #    (df_ltd_a["Power_Ranking_FT_H"] - df_ltd_a["Power_Ranking_FT_A"])
        #    >= 2
        #)
       
    )
    df_ltd_a = df_ltd_a[filtro_ltd_A]
    st.subheader("Trend LTD Zebra Away")
    st.markdown(f"Total Games Today  : {len(df_ltd_a)} games")
    st.dataframe(df_ltd_a)