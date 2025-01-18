# O que deve ser feito?
# Com uma visão mensal
# faturamento por unidade
# tipo de produto mais vendido, contribuição por filial
# Desempenho das forma de pagamento
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
col3, col4, col5 = st.columns(3)# (Três caixas imaginárias Col3, Col4 e Col5) Três gráficos na parte inferior a da tela

fig_date = px.bar(df_filtered, x='Date', y='Total', color='City', title='Faturamento por dia') # Criando um gráfico de barras
col1.plotly_chart(fig_date) # Reservando o espaço col1 para o gráfico

fig_prod = px.bar(df_filtered, x="Date", y="Product line", color="City", title="Faturamento por tipo de produto", orientation="h") # Gráfico de barra na horizontal
col2.plotly_chart(fig_prod) # Reservando o espaço col2 para o gráfico

city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index() # Agrupando a contribuição por filial
fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por filial") #Gráfico de barra da contribuição por filial
col3.plotly_chart(fig_city, use_container_width=True) # Reservando o espaço col3 para o gráfico

fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por tipo de pagamento") #Gráfico de pizza para forma de pagemento
col4.plotly_chart(fig_kind, use_container_width=True) # Reservando o espaço col4 para o gráfico

city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index() # Agrupando a rating por filial
fig_rating = px.bar(df_filtered, y="Rating", x="City", title="Avaliação") # gráfico da rating
col5.plotly_chart(fig_rating, use_container_width=True) # Reservando o espaço col5 para o gráfico