import streamlit as st
import requests
from datetime import date


st.markdown("<h2 style='text-align: center;'>More or Less: 2.5 Goals</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Um app para estimativa e separação dos jogos</h4>", unsafe_allow_html=True)
st.divider()


# Fazendo uma solicitação GET para o endpoint de áreas
response_areas = requests.get('https://api.sportsdata.io/v4/soccer/scores/json/Areas?key=594352b9547d44d698c51b234bf5f24f')

# Analisando a resposta JSON de áreas
data_areas = response_areas.json()

# Extraindo a lista de áreas
areas = [area['Name'] for area in data_areas]

# Criando um seletor para as áreas
selected_area = st.selectbox('Selecione uma área', areas)

# Obtendo a lista de competições correspondente à área selecionada
competitions = [area['Competition'] for area in data_areas if area['Name'] == selected_area]
selected_competition = st.selectbox('Selecione uma competição', competitions)

# Endpoint da API
endpoint = "https://api.sportsdata.io/v4/soccer/stats/json/BoxScoresByDate/{competition}/{date}?key=594352b9547d44d698c51b234bf5f24f"

# Filtros
filtro_data = st.date_input("Selecione uma data", value=date.today())

# Montando a URL do endpoint com os parâmetros
url = endpoint.format(competition=selected_competition, date=filtro_data)

# Fazendo a requisição HTTP
response = requests.get(url)

if response.status_code == 200:
    # Obtendo os dados da resposta
    data = response.json()

    # Filtrando os dados com base na área selecionada
    dados_filtrados = [placar for placar in data if placar['area'] == selected_area]

    # Exibindo os placares filtrados
    st.write("Placares:")
    for placar in dados_filtrados:
        st.write(placar['data'], placar['area'], placar['placar'])
else:
    st.write("Erro ao obter os dados dos placares. Status:", response.status_code)



"""

---
###### Minhas Redes:
Visite o meu [Linkedin](https://www.linkedin.com/MadisonQuedevez "Linkedin Oficial do Criador")


"""