import pandas as pd

dataframe = pd.DataFrame

vendas_df = pd.read_excel('Vendas.xlsx')
# print(vendas_df.head(10))
# print(vendas_df.shape)
# print(vendas_df.describe())

# ---- Uma coluna = Series
# ---- + de uma coluna = tabela

# produtos = vendas_df[["Produto", "Data"]]
# print(produtos)

# pegar somente os produtos: Iguatemi Esplanada, somente as coluas qunatidade produtor valor final

colunas = ["Produto", "Quantidade", "Valor Final"]
produto = "Camiseta"

produtosIguatemi_df = vendas_df.loc[vendas_df["Produto"] == produto, colunas]
linhas = vendas_df.loc[1:5]

print(produtosIguatemi_df)
print("Linhas", linhas)