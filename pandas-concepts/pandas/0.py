import pandas as pd

dataframe = pd.DataFrame

vendas = {
    'data': ['15/02/2022', '22/03/2029'],
    'valor': [300, 400],
    'produto': ['feijão', 'arroz'],
    'qtde': [50, 70]
}

vendas_df = dataframe(vendas)