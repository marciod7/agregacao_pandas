import json 
import pandas as pd 
data = [
    {"Empno":9001, "Salary": 3000},
    {"Empno":9002, "Salary": 2800},
    {"Empno":9003, "Salary": 2500}
]
json_data = json.dumps(data)
salary = pd.read_json(json_data)
salary = salary.set_index("Empno")

print('Combinando DataFrame')
import pandas as pd

# Criando o DataFrame inicial
data = [['9001', 'Jeff Russell', 'sales'],
        ['9002', 'Jane Boorman', 'sales'],
        ['9003', 'Tom Heints', 'sales']]
emps = pd.DataFrame(data, columns=['Empno', 'Name', 'Job'])
column_types = {'Empno': int, 'Name': str, 'Job': str}
emps = emps.astype(column_types)
emps = emps.set_index('Empno')

# Criando o novo funcionário com o índice Empno
new_emps = pd.DataFrame([{'Empno': 9004, 'Name': 'John Hardy', 'Job': 'sales'}]).set_index('Empno')

# Usando pd.concat() em vez de append()
emps = pd.concat([emps, new_emps])

# Imprimindo o DataFrame final
#print(emps)



emps_salary = emps.join(salary)
#print(emps_salary)

data = [[2608, 9001, 35], [2617, 9001, 35], [2620, 9001, 139],
        [2621, 9002, 95], [2626, 9002, 218]]
orders = pd.DataFrame(data, columns=['Pono', 'Empno', 'Total'])
print(orders)

emps_orders = emps.merge(orders, how='inner', left_on='Empno',
                         right_on='Empno').set_index('Pono')
print(emps_orders)

print(orders.groupby(['Empno'])['Total'].mean())