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

# Usando a área selecionada para filtrar os dados que você deseja exibir
filtered_data = [area for area in data if area['Name'] == selected_area]

# Exibindo os dados filtrados
st.write(filtered_data)




"""

---
###### Minhas Redes:
Visite o meu [Linkedin](https://www.linkedin.com/MadisonQuedevez "Linkedin Oficial do Criador")


"""