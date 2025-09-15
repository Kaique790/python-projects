import pandas as pd
import streamlit as st

df = pd.read_excel("funcionarios-empresa.xlsx")
pd.DataFrame(df)

df = df.dropna(how="all", axis=1)

st.set_page_config(
    page_title="Análise de funcionários",
)

st.sidebar.subheader("Início")

st.title("Análise dos funcionários")
st.subheader("Métricas da empresa")

st.markdown("<a href='/Gráficos' target='_self'>Ir para página de Gráficos</a>",
            unsafe_allow_html=True)

st.divider()

options = [
    "Quantos funcionários a empresa possui?",
    "Qual o salário líquido médio, o maior e o menor?",
    "Qual o valor total gasto com gratificações e horas extras?",
    "Qual funcionário (nome) recebeu a maior gratificação e qual recebeu a menor?",
    "Qual funcionário paga o maior imposto de renda e qual paga o menor?",
    "Qual funcionário tem o maior salário líquido?",
    "Qual funcionário tem o menor salário líquido?",
]

qtd_func = df["Nome Completo"].nunique()

liquid_salarys = df["Salário Líquido"]
gross_salarys = df["Salário Bruto"]

mean_salary = liquid_salarys.mean()

max_salary = liquid_salarys.max()
min_salary = liquid_salarys.min()

selected_option = st.selectbox("Selecione o que deseja:", options)

if selected_option:
    st.subheader(selected_option)

if selected_option == options[0]:
    st.metric(label="A empresa possui:", value=f"{qtd_func} funcionários")

if selected_option == options[1]:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Salário liquido médio:", value=f"{mean_salary:.2f}")
    with col2:
        st.metric(label="Maior salário liquido:", value=f"R$ {max_salary:.2f}")
    with col3:
        st.metric(label="Menor salário liquido:", value=f"R$ {min_salary:.2f}")

if selected_option == options[2]:
    total_gratifications = df["Gratificação R$"].sum()
    total_overtime = df["Hora Extra (Total.)"].sum()

    total_spent = total_gratifications + total_overtime
    st.metric(label="total gasto:", value=f"R$ {total_spent:.2f}")

if selected_option == options[3]:
    max_gratification = df["Gratificação R$"].max()
    min_gratification = df["Gratificação R$"].min()

    higher_workers = df[df["Gratificação R$"]
                        == max_gratification]["Nome Completo"]
    min_workers = df[df["Gratificação R$"] ==
                     min_gratification]["Nome Completo"]

    st.subheader("Funcionários com maior gratificação:")
    col1, col2 = st.columns(2)

    st.markdown("---")

    st.subheader("Funcionários com menor gratificação:")
    min1, min2 = st.columns(2)

    for i, w in enumerate(higher_workers):
        if i % 2 == 0:
            with col1:
                st.write(w)
            continue
        with col2:
            st.write(w)

    for i, w in enumerate(min_workers):
        if i % 2 == 0:
            with min1:
                st.write(w)
            continue
        with min2:
            st.write(w)

if selected_option == options[4]:
    max_tax = df["Imposto de Renda R$"].max()
    min_tax = df["Imposto de Renda R$"].min()

    higher_worker = df[df["Imposto de Renda R$"]
                       == max_tax]["Nome Completo"].iloc[0]
    min_worker = df[df["Imposto de Renda R$"]
                    == min_tax]["Nome Completo"].iloc[0]

    st.metric("O funcionário com maior imposto de renda é: ", higher_worker)
    st.metric("O funcionário com menor imposto de renda é: ", min_worker)

if selected_option == options[5]:
    higher_salary_worker = df[df["Salário Líquido"] == max_salary]

    name = higher_salary_worker["Nome Completo"].iloc[0]
    salary = higher_salary_worker["Salário Líquido"].iloc[0]

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Funcionário:", name)
    with col2:
        st.metric("Salário:", f"R$ {salary:.2f}")

if selected_option == options[6]:
    min_salary_worker = df[df["Salário Líquido"] == min_salary]

    name = min_salary_worker["Nome Completo"].iloc[0]
    salary = min_salary_worker["Salário Líquido"].iloc[0]

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Funcionário:", name)
    with col2:
        st.metric("Salário:", f"R$ {salary:.2f}")
