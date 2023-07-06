!pip install streamlit-datepicker


import streamlit as st
from datetime import date
from streamlit_datepicker import st_date_input


st.markdown("<h2 style='text-align: center;'>More or Less: 2.5 Goals</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Um app para estimativa e separação dos jogos</h4>", unsafe_allow_html=True)
st.divider()


# Criando a caixa de seleção de data com largura e altura personalizadas
data = st_date_input("Selecione uma data", date.today(), key="data", width=150, height=50)

# Exibindo a data selecionada
st.write("Data selecionada:", data)




"""

---
###### Minhas Redes:
Visite o meu [Linkedin](https://www.linkedin.com/MadisonQuedevez "Linkedin Oficial do Criador")


"""