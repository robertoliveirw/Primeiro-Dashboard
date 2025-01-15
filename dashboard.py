# O que deve ser feito?
# Com uma visão mensal
# faturamento por unidade…
# tipo de produto mais vendido, contribuição por filial,
# Desempenho das forma de pagamento…
# Como estão as avaliações das filiais?

import streamlit as st  # Biblioteca de construção de Dash
import pandas as pd  # Biblioteca de manipulação de dados
import plotly.express as px  # Construção de gráficos

st.set_page_config(layout='wide') # Definir a página como wide para ficar maior

df = pd.read_csv('supermarket_sales.csv', sep=';', decimal=',') # Separadores das colunas e o que marca a casa decimal (. ou ,)
df["Date"] = pd.to_datetime(df["Date"]) # Tirando a data de String para data
df = df.sort_values('Date') # Ordenando (Como se tivesse colocando um filtro no excel)

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month)) # Concatenando o ano e o mês
month = st.sidebar.selectbox("Mês", df["Month"].unique()) # Adicionando uma caixa de seleção

df_filtered = df[df["Month"] == month] # Filtro do Pandas
#df_filtered # Aparecendo o filtro

col1, col2 = st.columns(2) # (Duas caixas imaginárias Col1 e Col2) Dois gráficos na parte de cima da tela
col3, col4, col5 = st.columns(3)# (Três caixas imaginárias Col3, Col4 e Col5) Três gráficos na parte de cima da tela

fig_date = px.bar(df_filtered, x='Date', y='Total', color='City', title='Faturamento por dia') #Criando um gráfico de barras
col1.plotly_chart(fig_date) #Reservando o espaço col1 para o gráfico