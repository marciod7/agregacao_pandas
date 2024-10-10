import yfinance as yf
import mysql.connector
from mysql.connector import errorcode

# Inicializando a lista de dados
data = []

# Lista de tickers das ações
tickers = ['TSLA', 'META', 'ORCL', 'AMZN']

# Iterando sobre os tickers
for ticker in tickers:
    tkr = yf.Ticker(ticker)
    hist = tkr.history(period='5d').reset_index()
    
    # Convertendo os dados em um formato adequado
    records = hist[['Date', 'Close']].to_records(index=False)
    records = list(records)
    
    # Formatando os dados e convertendo np.float64 para float, arredondando para 2 casas decimais
    records = [(ticker, str(elem[0])[:10], round(float(elem[1]), 2)) for elem in records]
    
    # Adicionando os dados formatados à lista `data`
    data += records

# Exibindo os dados para verificar
print(data)

# Conexão com o MySQL e inserção dos dados
try:
    cnx = mysql.connector.connect(user='root', password='025016',
                                  host='127.0.0.1',
                                  database='sampledb2')
    cursor = cnx.cursor()
    
    # Definindo a query
    query_add_stocks = ("""INSERT INTO stocks (ticker, date, price)
                           VALUES (%s, %s, %s)""")
    
    # Adicionando as linhas de preço das ações
    cursor.executemany(query_add_stocks, data)
    
    cnx.commit()
    print("Dados inseridos com sucesso!")

except mysql.connector.Error as err:
    print("Error-Code: ", err.errno)
    print("Error-Message: {}".format(err.msg))

finally:
    if 'cursor' in locals():  # Verifica se o cursor foi definido
        cursor.close()
    if 'cnx' in locals():  # Verifica se a conexão foi estabelecida
        cnx.close()
