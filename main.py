#import funciones 
import pandas as pd
import os 
from sqlalchemy import create_engine

r_facturas = './facturas'

print('hola')

df = pd.DataFrame()

for factura in sorted(os.listdir(r_facturas)):
  print(f'Procesando factura: {factura}')