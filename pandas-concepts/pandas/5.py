import pandas as pd

dataframe = pd.DataFrame

vendas_df = pd.read_excel('Vendas.xlsx')
vendas_df["Comissão"] = vendas_df["Valor Final"] * 0.05

vendas_dez_df = pd.read_excel('Vendas - Dez.xlsx')
vendas_df = pd.concat([vendas_df, vendas_dez_df])

# preencher com média da coluna
# mediaComissao = vendas_df["Comissão"].mean()
# vendas_df["Comissão"] = vendas_df["Comissão"].fillna(mediaComissao)

# preencher com valor de cima
vendas_df["Comissão"] = vendas_df["Comissão"].ffill()

print(vendas_df)