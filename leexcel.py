import pandas as pd

produtos = pd.read_excel("Produtos.xlsx", engine='openpyxl')

for i, row in produtos.iterrows():
    print(row.MARCA)