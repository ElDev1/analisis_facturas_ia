import openai
import fitz
from dotenv import load_dotenv
import os
import pandas as pd
from io import StringIO
#from prompt import prompt

load_dotenv('.env')

OPENAI_API_KEY = os.getenvt('OPENAI_API_KEY')

def extraer_texto_pdf(ruta_pdf):

  doc = fitz.open(ruta_pdf)
  text = '\n'.join([page.get_text('text') for page in doc])
  return text


def estructurar_texto(texto):

    cliente = openai.OpenAI(api_key=OPENAI_API_KEY)

    respuesta = cliente.chat.completions.create(
       model='gpt-4o-mini',
       messages=[
          {
             'role': 'system',
             'content': 'Eres un experto en estraccion de datos de facturas.'
          },
          {
             'role': 'user',
             'content': ''
          }
       ]
    )