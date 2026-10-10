import streamlit as st
st.title("Situação do Aluno")
nome = st.text_input("Nome do aluno")
nota1 = st.number_input("Primeira nota", 0.0, 10.0, 0.0)
nota2 = st.number_input("Segunda nota", 0.0, 10.0, 0.0)
if st.button("Verificar"):
  media = (nota1 + nota2)/2
  st.write(f"**Nome do Aluno:**{nome}")
  st.write(f"**Média do Aluno:**{media:.1f}")
  if media >= 6.0:
     st.write("Situação: Aprovado")
else:
    st.write("Situação: Reprovado")
