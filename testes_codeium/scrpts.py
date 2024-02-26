import random
from datetime import datetime, timedelta

# Generate random dates within a specific range
def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + timedelta(days=random_number_of_days)

# Generate 50 insertion scripts for TbCliente
for i in range(1, 51):
    name = f'Client{i} Lastname{i}'
    address = f'{i} Street, City'
    phone = f'555-10{i:02d}'
    sex = random.choice(['M', 'F', 'O', None])
    birth_date = random_date(datetime(1950, 1, 1), datetime(2000, 12, 31)).strftime('%Y-%m-%d')
    print(f"INSERT INTO TbCliente (@id, nome, endereco, telefone, sexo, dataNascimento) VALUES ({i}, '{name}', '{address}', '{phone}', {sex}, '{birth_date}');")