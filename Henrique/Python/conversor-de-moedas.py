import streamlit as st


st.title("conversor de moedas!")

dolar = st.number_imput("dolar",placeholder="digite o valor em dolar:",step=2)
reais = dolar * 5
st.text("f0 valor de {dolar:.2f} dolares é igual a {reais:}")













