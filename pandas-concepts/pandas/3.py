import pandas as pd

dataframe = pd.DataFrame

vendas_df = pd.read_excel('Vendas.xlsx')

# Cria nova coluna com valores
vendas_df["Comissão"] = vendas_df["Valor Final"] * 0.05

# Criar coluna com valores padrões
# Também pode mudas valores de colunas existentes

vendas_df.loc[:, "Imposto"] = 0

# Adicionar outra tabela no vendas_df
vendas_dez_df = pd.read_excel('Vendas - Dez.xlsx')
vendas_df = pd.concat([vendas_df, vendas_dez_df])

vendas_df.loc[:, "Imposto"] = 0
vendas_df["Comissão"] = vendas_df["Valor Final"] * 0.05
print(vendas_df)