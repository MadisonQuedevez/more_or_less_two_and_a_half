import streamlit as st
import datetime
import locale

st.markdown("<h1 style='text-align: center;'>More or Less: 2.5 Goals</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>Um app para estimativa e separação dos jogos</h2>", unsafe_allow_html=True)


def setup_locale():
    # Definir a configuração regional para o formato brasileiro
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

def main():
    setup_locale()

    # Resto do seu código Streamlit
    data = st.date_input("Selecione uma data")

if __name__ == '__main__':
    main()


"""

---
###### Minhas Redes:
Visite o meu [Linkedin](https://www.linkedin.com/MadisonQuedevez "Linkedin Oficial do Criador")


"""