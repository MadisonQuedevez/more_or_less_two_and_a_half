import streamlit as st
from datetime import date
from ipywidgets import DatePicker


st.markdown("<h2 style='text-align: center;'>More or Less: 2.5 Goals</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Um app para estimativa e separação dos jogos</h4>", unsafe_allow_html=True)
st.divider()

# Criando a caixa de seleção de data personalizada com largura e altura
date_select = DatePicker(value=date.today(), layout={'width': '150px', 'height': '50px'})

# Exibindo o widget no Streamlit
st.write(date_select)



"""

---
###### Minhas Redes:
Visite o meu [Linkedin](https://www.linkedin.com/MadisonQuedevez "Linkedin Oficial do Criador")


"""