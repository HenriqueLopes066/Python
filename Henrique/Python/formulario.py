import streamlit as st



st.title("Formulário")

nome = st.text_input("nome",
placeholder="Digite seu nome")




idade = st.text_input("idade",
placeholder="Digite sua idade:")

task = st.checkbox("Estou estudando em casa")

cor = st.color_picker("escolha uma cor")
stacks = st.selectbox("Escolha as stacks",["BackEnd", "FrontEnd", "FulStack", "Estagiário"])


on = st.toggle("Ligar")
print(on)

