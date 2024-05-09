import pandas as pd
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show 

df = pd.read_csv(r"C:/Users/Mylenna/Documents/Teste-LIDAR/Teste exposto ao sol s ventilação/Temperatura407.txt", sep=" ; ", names=['Col1', 'Col2'])
df[['Name','Temperatura']] = df['Col2'].str.split(':', expand=True)
df['Temperatura'] = df['Temperatura'].str.replace('C', "")
df['Temperatura'] = pd.to_numeric(df['Temperatura']) 
df = df.drop('Col2', axis=1)

df_lateral = df[df['Name'] == 'Temperatura interna lateral']
df_SENSOR = df[df['Name'] == 'Temperatura do Sensor IR']
df_central = df[df['Name'] == 'Temperatura interna central']
df_Chassi = df[df['Name'] == 'Temperatura do chassi']

x1 = df_SENSOR['Col1']
y1 = df_SENSOR['Temperatura']
x2 = df_central['Col1']
y2 = df_central['Temperatura']
x3 = df_lateral['Col1']
y3 = df_lateral['Temperatura']
x4 = df_Chassi['Col1']
y4 = df_Chassi['Temperatura']
plt.plot(x1, y1, color='turquoise')
plt.scatter(x1, y1, color='blue')
plt.plot(x2, y2, color='lime')
plt.scatter(x2, y2, color='green')
plt.plot(x3, y3, color='violet')  
plt.scatter(x3, y3, color='purple')  
plt.plot(x4, y4, color='yellow')
plt.scatter(x4, y4, color='orange')
plt.title('Variação da Temperatura ao Longo do Tempo')
plt.xlabel('Data e Hora')
plt.ylabel('Temperatura em °C')
plt.grid()
plt.legend(['Temperatura do LIDAR', 'Hora', 'Temperatura Interna Central', 'Hora', 'Temperatura lateral', 'Hora','Temperatura do Chassi','Hora'])
plt.show()

plt.figure.savefig('meu_grafico.html')