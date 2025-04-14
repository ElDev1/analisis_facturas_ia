# Creación de dashboards y análisis de facturas con IA

Este proyecto en Python permite la lectura y procesamiento automático de facturas en formato PDF desde un directorio específico, utilizando técnicas de inteligencia artificial para extraer la información clave. Los datos extraídos se almacenan en una base de datos, listos para su posterior análisis mediante herramientas de Business Intelligence (BI) como Power BI, Qlik u otras.

## 🧠 ¿Qué hace este proyecto?

- Escanea un directorio en busca de archivos de facturas.
- Usa modelo de IA Qroq para interpretar y extraer campos importantes (fecha, proveedor, total, etc.)
- Guarda los datos estructurados en una base de datos SQLite
- Permite consultas y análisis posteriores a través de herramientas BI.