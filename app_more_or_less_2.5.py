import streamlit as st
from datetime import date


st.markdown("<h2 style='text-align: center;'>More or Less: 2.5 Goals</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Um app para estimativa e separação dos jogos</h4>", unsafe_allow_html=True)
st.divider()


# Definindo um identificador para a caixa de seleção de data
data_key = 'my_date_input'

# Criando a caixa de seleção de data com um identificador único
data = st.date_input("Selecione uma data", date.today(), key=data_key)

# Usando CSS para ajustar o tamanho da caixa de seleção de data
st.markdown(f"""<style>
        #{data_key} {{
            width: 150px;
            height: 50px;
        }}
    </style>""", unsafe_allow_html=True)

# Exibindo a data selecionada
st.write("Você selecionou a data:", data)



"""

---
###### Minhas Redes:
Visite o meu [Linkedin](https://www.linkedin.com/MadisonQuedevez "Linkedin Oficial do Criador")


"""