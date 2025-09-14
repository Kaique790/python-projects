
import streamlit as st
import pandas as pd

import plotly.express as px

df = pd.read_excel("funcionarios-empresa.xlsx")
pd.DataFrame(df)

df = df.dropna(how="all", axis=1)

st.set_page_config(
    page_title="Gráficos",
)

st.sidebar.title("Gráficos")

st.title("Análise com Gráficos")
st.subheader("Métrica da Empresa")

st.markdown("<a href='/' target='_self'>Ir para página inicial</a>",
            unsafe_allow_html=True)

st.divider()


def salary_chart(df):
    chart_salary_data = df[["Nome Completo",
                            "Salário Bruto", "Salário Líquido"]]

    salarys_comp_chart = px.bar(
        chart_salary_data,
        x=["Salário Bruto", "Salário Líquido"],
        y="Nome Completo",
        labels={
            "value": "Valor R$",
            "variable": "Tipo de Salário"
        }
    )

    st.subheader("Salário Bruto vs Salário Líquido:")
    st.plotly_chart(salarys_comp_chart)


def gratifications_chart(df):
    chart_gratification_data = df[["Nível Funcional",
                                   "Gratificação R$"]]

    gratification_chart = px.bar(
        chart_gratification_data, x="Gratificação R$", y="Nível Funcional")

    st.subheader("Total de gratificação por nivel funcional:")
    st.plotly_chart(gratification_chart)


salary_chart(df)
gratifications_chart(df)

st.divider()
st.markdown("<a href='/' target='_self'>Ir para página inicial</a>",
            unsafe_allow_html=True)
