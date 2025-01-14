# O que deve ser feito?
# Com uma visão mensal
# faturamento por unidade…
# tipo de produto mais vendido, contribuição por filial,
# Desempenho das forma de pagamento…
# Como estão as avaliações das filiais?

import streamlit as st  # Biblioteca de construção de Dash
import pandas as pd  # Biblioteca de manipulação de dados
import plotly.express as px  # Construção de gráficps

# Definir a página como wide para ficar maior
st.set_page_config(layout='wide')

# Separadores das colunas e o que marca a casa decimal (. ou ,)
df = pd.read_csv('supermarket_sales.csv', sep=';', decimal=',')
df["Date"]
