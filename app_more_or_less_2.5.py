import streamlit as st
import requests
from datetime import date


st.markdown("<h2 style='text-align: center;'>More or Less: 2.5 Goals</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Um app para estimativa e separação dos jogos</h4>", unsafe_allow_html=True)
st.divider()


# Criando a caixa de seleção de data
data = st.date_input("Selecione uma data", date.today())

# Fazendo uma solicitação GET para o endpoint
response = requests.get('https://api.sportsdata.io/v4/soccer/scores/json/Areas?key=594352b9547d44d698c51b234bf5f24f')

# Analisando a resposta JSON
data = response.json()

# Extraindo a lista de áreas
areas = [area['Name'] for area in data]

# Criando um seletor para as áreas
selected_area = st.selectbox('Selecione uma área', areas)

# Endpoint da API
endpoint = "https://api.sportsdata.io/v4/soccer/stats/json/BoxScoresByDate/{competition}/{date}?key=594352b9547d44d698c51b234bf5f24f"

# Dados de exemplo
competition = "example"  # Substitua "example" pelo nome da competição desejada

# Montando a URL do endpoint com os parâmetros
url = endpoint.format(competition=competition, date=data)

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