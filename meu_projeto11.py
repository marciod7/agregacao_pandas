import pandas as pd

# Criando a lista de convidados como um DataFrame
dados = pd.DataFrame({
    'Convidado': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank'],
    'Cor': ['Azul', 'Vermelho', 'Azul', 'Verde', 'Vermelho', 'Azul'],
    'Tipo': ['Refrigerante', 'Carne', 'Sucos', 'Carne', 'Refrigerante', 'Carne'],
    'Quantidade': [2, 3, 1, 4, 2, 5]
})

# Agrupando os dados pela cor da roupa
agrupado_por_cor = dados.groupby('Cor').sum()
print(agrupado_por_cor)

agrupado_cor_tipo = dados.groupby(['Cor', 'Tipo']).sum()
print(agrupado_cor_tipo)

agrupado_funcoes = dados.groupby('Cor').agg(
    Total=('Quantidade', 'sum'),
    Media=('Quantidade', 'mean'),
    Maximo=('Quantidade', 'max')
)
print(agrupado_funcoes)
