import pandas as pd
import streamlit as st

dataframe = pd.read_excel("scraper.xlsx")

st.title("Gráfico de produtos")
st.subheader("Análise dos principais notebooks")

st.write("Quantidade de empresas: ", dataframe["FABRICANTE"].nunique())

selectedManufactures = st.multiselect("Escolha uma opção", dataframe["FABRICANTE"].unique())

for selected in selectedManufactures:
    value = dataframe.loc[dataframe["FABRICANTE"] == selected]
    st.subheader(f"Métricas {selected}")
    st.metric("Total bruto em R$: ", f"R$ {value["RECEITA_BRUTA"].sum():,.2f}")
    st.metric("Média bruta em R$: ", f"R$ {value["RECEITA_BRUTA"].mean():,.2f}")

st.bar_chart(dataframe.groupby("FABRICANTE")["RECEITA_BRUTA"].sum())
