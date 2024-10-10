import redis
from datetime import timedelta

# Conectando ao Redis
r = redis.Redis()

# Definindo valores simples
r.mset({"emp1": "Maya Silver", "emp2": "John Jamison"})

# Definindo uma chave com tempo de expiração
r.setex("cab26", timedelta(minutes=1), value="in the area now")

# Criando um hash
cabDict = {"ID": "cab48", "Driver": "Dan Varsky", "Brand": "Volvo"}
# Usando hset corretamente
r.hset("cab48", mapping=cabDict)

# Obtendo o hash
emp1 = r.hgetall("cab48")

# Decodificando os valores de bytes para string
emp1_decoded = {k.decode('utf-8'): v.decode('utf-8') for k, v in emp1.items()}

# Exibindo o dicionário decodificado
print(emp1_decoded)
