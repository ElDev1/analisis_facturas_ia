from groq import Groq
import fitz
from dotenv import load_dotenv
import os
import pandas as pd
from io import StringIO
from prompt import prompt

load_dotenv('.env')

def extraer_texto_pdf(ruta_pdf):

  doc = fitz.open(ruta_pdf)
  text = '\n'.join([page.get_text('text') for page in doc])
  return text


def estructurar_texto(texto):
  client = Groq(
  api_key=os.environ.get("GROQ_API_KEY"),
  )

  chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Eres un experto en extracción de datos de facturas. Devuelve solo el CSV sin explicaciones ni mensajes adicionales. Si no puedes extraer datos, devuelve exactamente la palabra 'error' sin comillas.",
        },
        {
            "role": "user",
            "content": prompt + "\n Este es el texto a parsear:\n" + texto,
        },

    ],
    model="llama-3.3-70b-versatile",
  )

  return chat_completion.choices[0].message.content


def csv_a_dataframe(csv):
  dtype_cols = {
    'fecha_factura': str,
    'proveedor': str,
    'concepto': str,
    'importe': str,
    'moneda': str
  }

  df_temp = pd.read_csv(StringIO(csv), delimiter=';', dtype=dtype_cols)

  return df_temp

