
import streamlit as st
import pandas as pd
import plotly.express as px

from pandas import DataFrame
from PIL import Image


df = pd.read_excel("funcionarios-empresa.xlsx")
pd.DataFrame(df)

df = df.dropna(how="all", axis=1)

try:
    favicon = Image.open("favicons/metrics.png")
except FileNotFoundError:
    favicon = ":material/home:"

st.set_page_config(
    page_title="Gráficos",
    page_icon=favicon
)

st.sidebar.title("Gráficos")

st.title("Análise com Gráficos")
st.subheader("Métrica da Empresa")

st.markdown("<a href='/' target='_self'>Ir para página inicial</a>",
            unsafe_allow_html=True)

st.divider()


def salary_chart(df: DataFrame):
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


def gratifications_chart(df: DataFrame):
    chart_gratification_data = df[["Nível Funcional",
                                   "Gratificação R$"]]

    gratification_chart = px.bar(
        chart_gratification_data, x="Gratificação R$", y="Nível Funcional")

    st.subheader("Total de gratificação por nivel funcional:")
    st.plotly_chart(gratification_chart)


def salary_evolution_chart(df: DataFrame):
    df.sort_values('Nome Completo', ascending=True, inplace=True)

    chart_salary_data = df[["Nome Completo", "Salário Líquido"]]

    salarys_evolution_chart = px.line(
        chart_salary_data,
        y="Salário Líquido",
        x="Nome Completo",
    )

    st.subheader("Evolução do Salário Líquido:")
    st.plotly_chart(salarys_evolution_chart)


def IR_impact_chart(df: DataFrame):
    chart_salary_data = df[["Imposto de Renda R$", "Salário Bruto"]]

    salarys_comp_chart = px.line(
        chart_salary_data,
        x="Salário Bruto",
        y="Imposto de Renda R$",
    )

    st.subheader("Impacto do imposto de renda:")
    st.write("É calculado em relação ao salário bruto e não líquido.")

    st.plotly_chart(salarys_comp_chart)


salary_chart(df)
gratifications_chart(df)
salary_evolution_chart(df)
IR_impact_chart(df)

st.divider()
st.markdown("<a href='/' target='_self'>Ir para página inicial</a>",
            unsafe_allow_html=True)
