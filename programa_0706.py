import pandas as pd  
import matplotlib.pyplot as plt
import streamlit as st

st.header("Dados da empresa 1")

arquivo = "https://raw.githubusercontent.com/WesleyInfoBr2/aula_teste/main/empresa1.csv" 
dfe = pd.read_csv(arquivo, sep=';') 
st.dataframe(dfe.head(3))

fig, ax = plt.subplots()
dfe.plot(ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
dfe.plot(kind = 'scatter', x = 'EBITDA', y = 'Lucro operacional', ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
dfe["Lucro do período"].plot(kind = 'hist', ax=ax)
st.pyplot(fig)


st.write(dfe.groupby('Ano').mean())


