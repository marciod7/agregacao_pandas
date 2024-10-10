import mysql.connector

try:
    cnx = mysql.connector.connect(user='root', password='025016',
                                  host='127.0.0.1',
                                  database='sampledb2')
    cursor = cnx.cursor()
    
    # Definindo a query
    query = """
    SELECT date, ticker, price, 
           LAG(price) OVER (PARTITION BY ticker ORDER BY date) AS previous_price
    FROM stocks;
    """
    
    cursor.execute(query)
    
    # Recuperando os resultados
    results = cursor.fetchall()
    for row in results:
        print(row)

except mysql.connector.Error as err:
    print("Error-Code: ", err.errno)
    print("Error-Message: {}".format(err.msg))

finally:
    if 'cursor' in locals():  # Verifica se o cursor foi definido
        cursor.close()
    if 'cnx' in locals():  # Verifica se a conexão foi estabelecida
        cnx.close()
