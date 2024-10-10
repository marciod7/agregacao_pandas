import pandas as pd

# Dados atualizados
data = ['Jeff Russell', 'Jane Boorman', 'Tom Heints']
emps_names = pd.Series(data, index=[9001, 9002, 9003], name='names')

# Dados de telefones e emails
data_phones = ['98845-2356', '99823-3678', '98876-2200']
emps_emails = pd.Series(['jeff@example.com', 'jane@example.com', 'tom@example.com'], index=[9001, 9002, 9003], name='emails')

# Criando Series para os telefones
emps_phones = pd.Series(data_phones, index=[9001, 9002, 9003], name='phones')

# Concatenando os dados em um DataFrame
df = pd.concat([emps_names, emps_emails, emps_phones], axis=1)

# Exibindo o DataFrame
print(df)
