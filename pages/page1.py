import streamlit as st
import requests
import pandas as pd

# Função para carregar a base de dados (com cache)
@st.cache(allow_output_mutation=True)
def load_base():
    url = "https://github.com/futpythontrader/YouTube/blob/main/Base_de_Dados/futpythontraderpunter.csv?raw=true"
    data_jogos = pd.read_csv(url)

    return data_jogos

# Carregar a base de dados
df = load_base()

# Filtros
st.header("Filtros")
min_H = st.number_input("FT_Odd_H", min_value=1.01, max_value=10.0, value=1.01)
max_H = st.number_input("FT_Odd_H", min_value=1.01, max_value=10.0, value=10.0)

min_D = st.number_input("FT_Odd_D", min_value=1.01, max_value=10.0, value=1.01)
max_D = st.number_input("FT_Odd_D", min_value=1.01, max_value=10.0, value=10.0)

min_A = st.number_input("FT_Odd_A", min_value=1.01, max_value=10.0, value=1.01)
max_A = st.number_input("FT_Odd_A", min_value=1.01, max_value=10.0, value=10.0)

min_Over25 = st.number_input("FT_Odd_Over25", min_value=1.01, max_value=10.0, value=1.01)
max_Over25 = st.number_input("FT_Odd_Over25", min_value=1.01, max_value=10.0, value=10.0)

min_BTTS = st.number_input("FT_Odd_BTTS_Yes", min_value=1.01, max_value=10.0, value=1.01)
max_BTTS = st.number_input("FT_Odd_BTTS_Yes", min_value=1.01, max_value=10.0, value=10.0)

# Filtrar o dataframe
df_filtrado = df[(df['FT_Odd_H'] >= min_H) & (df['FT_Odd_H'] <= max_H) &
                 (df['FT_Odd_D'] >= min_D) & (df['FT_Odd_D'] <= max_D) &
                 (df['FT_Odd_A'] >= min_A) & (df['FT_Odd_A'] <= max_A) &
                 (df['FT_Odd_Over25'] >= min_Over25) & (df['FT_Odd_Over25'] <= max_Over25) &
                 (df['FT_Odd_BTTS_Yes'] >= min_BTTS) & (df['FT_Odd_BTTS_Yes'] <= max_BTTS)]

# Calcular o profit acumulado
df_filtrado['Profit_acu'] = df_filtrado['Profit'].cumsum()
df_filtrado = df_filtrado.dropna()
df_filtrado = df_filtrado.reset_index(drop=True)
df_filtrado.index += 1
profit = round(df_filtrado['Profit_acu'].tail(1).item(), 2)
ROI = round((df_filtrado['Profit_acu'].tail(1) / len(df_filtrado) * 100).item(), 2)

# Exibir os resultados em uma tabela
st.header("Resultados")
st.write("Profit:", profit, "stakes em", len(df_filtrado), "jogos")
st.write("ROI:", ROI, "%")
st.write(df_filtrado)
