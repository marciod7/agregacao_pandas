import pandas as pd
import mysql.connector
from mysql.connector import errorcode
from sqlalchemy import create_engine  # Importando SQLAlchemy

try:
    # Conexão ao banco de dados usando mysql.connector
    cnx = mysql.connector.connect(user='root', password='025016',
                                   host='127.0.0.1',
                                   database='sampledb2')

    # Criar um motor (engine) SQLAlchemy
    engine = create_engine('mysql+mysqlconnector://root:025016@127.0.0.1/sampledb2')

    # Consulta SQL
    query = ("""
             SELECT s.* FROM stocks AS s
             LEFT JOIN
             (SELECT DISTINCT(ticker) FROM
              (SELECT
              price/LAG(price) OVER(PARTITION BY ticker ORDER BY date) AS dif,
              ticker
              FROM stocks) AS b
              WHERE dif < 0.99) AS a
             ON a.ticker = s.ticker
             WHERE a.ticker IS NULL
             """)

    # Executa a consulta e armazena em um DataFrame
    df_stocks = pd.read_sql(query, con=engine)  # Usando o motor do SQLAlchemy
    df_stocks = df_stocks.set_index(['ticker', 'date'])

except mysql.connector.Error as err:
    print("Error-Code:", err.errno)
    print("Error-Message: {}".format(err.msg))
finally:
    if 'cnx' in locals():
        cnx.close()
