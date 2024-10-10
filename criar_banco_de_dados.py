import mysql.connector

try:
    # Conectando ao banco de dados
    cnx = mysql.connector.connect(user='root', password='025016',
                                  host='127.0.0.1',
                                  database='sampledb')
    cursor = cnx.cursor()
    
    # Definindo a consulta
    query = ("SELECT * FROM emps WHERE empno > %s")  # Corrigido para "emps"
    empno = 9001
    
    # Executando a consulta
    cursor.execute(query, (empno,))
    
    # Recuperando e imprimindo os resultados
    for (empno, empname, job) in cursor:
        print("{}, {}, {}".format(empno, empname, job))

except mysql.connector.Error as err:
    print("Error-Code:", err.errno)
    print("Error-Message:", err.msg)

finally:
    # Fechando o cursor e a conexão de forma segura
    if cursor:
        cursor.close()
    if cnx:
        cnx.close()
