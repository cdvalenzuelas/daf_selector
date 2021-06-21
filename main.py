import pandas as pd
import numpy as np
from auxiliar_funtions import temp_plus
from response import response

def main():
  degree = input("Seleccione °C [1] o °F [2]:" ) #Seleccionar entre grados centígrados o grados farenheit
  letter = 'F' if degree == 2 else 'C' #Seleccionar la letra adecuada para el mensaje

  temp = float(input(f'Ingrese la temperatura máxima del recinto [{letter}]: ')) # Ingreso de la temperatura

  f_tem, c_tem = (None, None)

  if letter == 'F':
    f_temp = temp
    c_temp = round((temp-32)*5/9, 2)
  else:
    c_temp = temp
    f_temp = round(32+9*temp/5, 2)

  
  nfpa_72_requirement = input("El detector debe cumplir con NFPA 72 (es dispositivo de iniciación) [s/n]: ") #Debe ser un dispositivo de iniciación?
  min_temp_set = round(temp_plus(temp=temp, degree=degree), 2) #Establecer una temperatura mínima de seteo  
  
  df1 = pd.read_csv('vertical.csv') #Leer tabla de temperaturas de seteo
  df2 = pd.read_csv('vertical_specifications.csv') #Leer tabla de especificaciones técnicas

  df1 = df1.loc[:,:][df1['f_setting'] >= min_temp_set].head(1) #Seleccionado la temperaura de seteo más cercana
  
  if df1['f_setting'].values[0] >= 600: #tener cuiddo con las temperaturas de setero grandes
    print('El modelo únicamnte está disponibe como detector normalmente abierto')
  
  if nfpa_72_requirement == 's': #Filtrando los detectores para ver si son dispositivos iniciadores
    df2 = df2[df2['contact_operation'] != 'normally closed (open on rise)']  

  #Seleccionar el material
  materials = df2['head_material'].unique() #Mostrando que materiales hay disponibles
  heads = df2['head'].unique() #Mostrando que cabeza hay disponibles

  #Seleccionar el material
  material = input(f'Selecciones el material deseado {materials}: ')
  head = input(f'Selecciones el material deseado {heads}: ')
  df2 = df2[(df2['head_material']==material)&(df2['head']==head)] 

  #Preguntar en caso de que haya más de una solución
  if df2.shape[0] > 1:
    df2.reset_index(drop=True, inplace=True)
    print('----------------------------------------------------------------------------------------------------')
    print(df2)
    print('----------------------------------------------------------------------------------------------------')
    index = int(input('Sellecciones una de las opciones permitidas: '))
    selected = df2.loc[index,:]

  with open('response.txt', 'w', encoding='utf-8') as f: #With es un manejador contextual(maneja el flujo del archivo y evita que se rompa)
    f.write(response(temp=df1, model = df2, f_temp=f_temp, c_temp=c_temp, nfpa_72_requirement=nfpa_72_requirement, head=head, material=material))
  
  print('----------------------------------------------------------------------------------------------------')
  print('Hecho')
  print('----------------------------------------------------------------------------------------------------')

if __name__ == '__main__':
  main()  
  