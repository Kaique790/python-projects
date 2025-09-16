import pandas as pd

dataframe = pd.DataFrame

vendas_df = pd.read_excel('Vendas.xlsx')
gerentes_df = pd.read_excel('Gerentes.xlsx')

vendas_df = vendas_df.merge(gerentes_df)

print(vendas_df)
