import pandas as pd
import streamlit as st

dataframe = pd.read_excel("scraper.xlsx")

st.set_page_config(page_title="Painel - Mercado free")

st.title("Painel de rendimento")
st.subheader("Análise dos principais notebooks")

st.write("Quantidade de empresas: ", dataframe["FABRICANTE"].nunique())

selectedManufactures = st.multiselect("Escolha uma opção", dataframe["FABRICANTE"].unique())
new_df = dataframe

if selectedManufactures:
    new_df = new_df[new_df["FABRICANTE"].isin(selectedManufactures)]

all_yield = new_df["RECEITA_BRUTA"].sum()
all_mean = new_df["RECEITA_BRUTA"].mean()

total, mean = st.columns(2)
st.markdown("---")

with total:
    st.subheader("Rendimento geral total")
    st.metric("Total bruto em R$: ", f"R$ {all_yield:,.2f}")
with mean:
    st.subheader("Média geral total")
    st.metric("Total bruto em R$: ", f"R$ {all_mean:,.2f}")

def insert_metrics(df, field, current_value):
    value = df.loc[df[field] == current_value]
    with st.popover(f"Ver receita {current_value}", width=1000):
        st.subheader(f"Métricas {current_value}")
        st.metric("Total bruto em R$: ", f"R$ {value["RECEITA_BRUTA"].sum():,.2f}")
        st.metric("Média bruta em R$: ", f"R$ {value["RECEITA_BRUTA"].mean():,.2f}")

col1, col2 = st.columns(2)

for i, selected in enumerate(selectedManufactures):
    if i % 2 == 0:
        with col1:
            insert_metrics(df=dataframe, field="FABRICANTE", current_value=selected)
    else:
        with col2:
            insert_metrics(df=dataframe, field="FABRICANTE", current_value=selected)

# st.bar_chart(dataframe.groupby("FABRICANTE")["RECEITA_BRUTA"].sum())
