import funciones 
import pandas as pd
import os 
from sqlalchemy import create_engine

r_facturas = './facturas'

df = pd.DataFrame()

for factura in sorted(os.listdir(r_facturas)):
  print(f'Procesando factura: {factura}')

  texto_no_estructurado = funciones.extraer_texto_pdf('./facturas/'+factura)
  #print(texto_no_estructurado)

  texto_estructurado = funciones.estructurar_texto(texto_no_estructurado)
  print(texto_estructurado)

  df_factura = funciones.csv_a_dataframe(texto_estructurado)

  df = pd.concat([df, df_factura], ignore_index=True)
  print(df)