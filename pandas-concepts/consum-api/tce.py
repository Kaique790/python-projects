import pandas as pd

def get_datas_to_tce(type_option: str, fields: list[str]):
    city = input("Digite um cidade de São Paulo: ")
    year= int(input("Digite um ano de 2014 a 2019: "))
    month= int(input("Digite um mês de 1 a 12: "))

    url = f"https://transparencia.tce.sp.gov.br/api/xml/{type_option}/{city}/{year}/{month}"
    tce_df = pd.read_xml(url)

    return tce_df[fields]

def format_str_in_df(df, colum):
    df[colum] = (
        tce_df[colum]
        .astype(str)
        .str.replace(".", "")
        .str.replace(",",".")
        .astype(float)
    )

def calc_expense (type_option):
    columns = fields
    if type_option == "despesas":
        format_str_in_df(tce_df, "vl_despesa")

        expense_by_organ_df = tce_df[columns].groupby("orgao")["vl_despesa"].sum()
        return expense_by_organ_df
    
    format_str_in_df(tce_df, "vl_arrecadacao")

    expense_by_organ_df = tce_df[columns].groupby("orgao")["vl_arrecadacao"].sum()
    return expense_by_organ_df

options = input("Qual o tipo? despesas ou receitas: ")
fields = []

if options == "despesas":
    fields = ["mes", "evento", "orgao", "vl_despesa"]
else:
    fields = ["mes", "orgao", "vl_arrecadacao"]

print(fields)

tce_df = get_datas_to_tce(options, fields=fields)
expense_by_organ_df = calc_expense(options)

print(expense_by_organ_df)