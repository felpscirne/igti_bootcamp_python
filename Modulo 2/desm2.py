import numpy as np
import pandas as pd



df = pd.read_csv("https://pycourse.s3.amazonaws.com/bike-sharing.csv")

# 1. Qual o tamanho desse dataset?
print("Tamanho do dataset:",df.shape)

# 2. Qual a média da coluna windspeed?
print("Média da coluna windspeed:",df['windspeed'].mean())

# 3. Qual a média da coluna temp?
print("Média da coluna temp:",df['temp'].mean())

# 4. Quantos registros de locações existem para o ano de 2011 (número de linhas, numero de colunas)?
print("Registros de locações para 2011:",df[df['year'] == 0].shape)

# 5. Quantos registros de locações existem para o ano de 2012 (número de linhas, numero de colunas)?
print("Registros de locações para 2012:",df[df['year'] == 1].shape)

# 6. Quantas locações de bicicletas foram efetuadas em 2011?
print("Locações de bicicletas em 2011:",df[df['year'] == 0]['total_count'].sum())

# 7. Quantas locações de bicicletas foram efetuadas em 2012?
print("Locações de bicicletas em 2012:",df[df['year'] == 1]['total_count'].sum())

# 8. Qual estação do ano contém a maior média de locações de bicicletas?
print("Estação do ano com maior média de locações:",df.groupby('season')['total_count'].mean().idxmax())

# 9. Qual estação do ano contém a menor média de locações de bicicletas?
print("Estação do ano com menor média de locações:",df.groupby('season')['total_count'].mean().idxmin())

# 10. Qual horário do dia contém a maior média de locações de bicicletas?
print("Horário do dia com maior média de locações:",df.groupby('hour')['total_count'].mean().idxmax())

# 11. Qual horário do dia contém a menor média de locações de bicicletas?
print("Horário do dia com menor média de locações:",df.groupby('hour')['total_count'].mean().idxmin())

# 12. Que dia da semana contém a maior média de locações de bicicletas?
print("Dia da semana com maior média de locações:",df.groupby('weekday')['total_count'].mean().idxmax())

# 13. Que dia da semana contém a menor média de locações de bicicletas?
print("Dia da semana com menor média de locações:",df.groupby('weekday')['total_count'].mean().idxmin())

# 14. Às quartas-feiras (weekday = 3), qual o horário do dia contém a maior média de locações de bicicletas?
print("Horário do dia com maior média de locações às quartas:",df[df['weekday'] == 3].groupby('hour')['total_count'].mean().idxmax())

# 15. Aos sábados (weekday = 6), qual o horário do dia contém a maior média de locações de bicicletas?
print("Horário do dia com maior média de locações aos sábados:",df[df['weekday'] == 6].groupby('hour')['total_count'].mean().idxmax())


