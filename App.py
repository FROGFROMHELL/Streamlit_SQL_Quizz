import streamlit as st
import pandas as pd
import duckdb

data = {'nom': ['Chacha', 'Cathy', 'Caro'], 'âge': [37, 65, 31]}
df = pd.DataFrame(data)

st.title('Bienvenue sur SQL QUIZZ')

SQL_Query = st.text_area(label='Tape ta requête')
result = duckdb.query(SQL_Query).df()
st.write(f"Votre requête : {SQL_Query}")
st.dataframe(result)
