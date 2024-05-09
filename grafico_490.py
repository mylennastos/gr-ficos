import pandas as pd
from datetime import datetime
from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource
from bokeh.models import Range1d

# Carregando os dados
df = pd.read_csv(r"C:/Users/Mylenna/Documents/Teste-LIDAR/temperatura490(interno).txt", sep=" ; ", names=['Col1', 'Col2'],engine='python')
df[['Name','Temperatura']] = df['Col2'].str.split(':', expand=True)
df['Temperatura'] = df['Temperatura'].str.replace('C', "")
df['Temperatura'] = pd.to_numeric(df['Temperatura']) 
df = df.drop('Col2', axis=1)
df['Col1'] = df['Col1'].str.strip()
df['Col1'] = pd.to_datetime(df['Col1'], format='%Y-%m- %d %H:%M:%S:', errors='coerce')

# Removendo linhas com valores nulos (caso ocorram devido a erros na conversão)
df.dropna(subset=['Col1'], inplace=True)

# Filtrando os dados
df_SENSOR = df[df['Name'] == 'Temperatura do LIDAR']
df_central = df[df['Name'] == 'Temperatura interna central']

df_sensor_clean = df_SENSOR.dropna()
df_central_clean = df_central.dropna()

# Criando a fonte de dados para o gráfico
source_sensor = ColumnDataSource(df_sensor_clean)
source_central = ColumnDataSource(df_central_clean)

# Definindo os valores mínimos e máximos para os eixos x e y
min_value_x = df['Col1'].min()
max_value_x = df['Col1'].max()
min_value_y = df['Temperatura'].min()
max_value_y = df['Temperatura'].max()

# Limitando a faixa de temperatura para valores mais razoáveis
min_value_y = max(min_value_y, 20)  # Definindo um mínimo de -20 °C
max_value_y = min(max_value_y, 60)   # Definindo um máximo de 60 °C

# Criando o gráfico com a faixa de valores definida
p = figure(title='Variação da Temperatura ao Longo do Tempo', x_axis_label='Data e Hora', y_axis_label='Temperatura em °C',
           x_range=(min_value_x, max_value_x), y_range=(min_value_y, max_value_y))

# Adicionando linhas e pontos ao gráfico
p.line(x='Col1', y='Temperatura', source=source_sensor, color='turquoise', legend_label='Temperatura do LIDAR')
p.circle(x='Col1', y='Temperatura', source=source_sensor, color='blue', legend_label='Temperatura do LIDAR')
p.line(x='Col1', y='Temperatura', source=source_central, color='lime', legend_label='Temperatura Interna Central')
p.circle(x='Col1', y='Temperatura', source=source_central, color='green', legend_label='Temperatura Interna Central')

# Salvando o gráfico em um arquivo HTML
output_file("temperatura490_interno.html")
save(p)




