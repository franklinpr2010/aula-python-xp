from datetime import datetime, timedelta

agora = datetime.now()
print(agora)  # Saída: 2025-04-14 21:18:00.123456

minha_data = datetime(2025, 4, 14, 21, 30, 0)
print(minha_data)  # Saída: 2025-04-14 21:30:00

#Use a classe timedelta para calcular diferenças entre datas:
hoje = datetime.now()
futuro = hoje + timedelta(days=10)  # Adiciona 10 dias
print(futuro)  # Saída: 2025-04-24 21:18:00

from datetime import datetime

data1 = datetime(2025, 4, 14)
data2 = datetime(2025, 5, 1)

if data1 < data2:
    print("data1 é anterior a data2")
else:
    print("data2 é anterior ou igual a data1")
    

hoje = datetime.now()
final_do_ano = datetime(hoje.year, 12, 31)
dias_restantes = (final_do_ano - hoje).days
print(f"Faltam {dias_restantes} dias para o fim do ano!")

agora = datetime.now()
mais_trinta = agora + timedelta(minutes=30)
print(mais_trinta)

agora = datetime.now()
print(agora.strftime("Hoje é %A, %d de %B de %Y"))