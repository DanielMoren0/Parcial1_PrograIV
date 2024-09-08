import pandas as pd
from sodapy import Socrata

def obtener_datos_covid(limite, departamento):
    cliente = Socrata("www.datos.gov.co", None)
    resultados = cliente.get("ch4u-f3i5", limit=limite, departamento=departamento)
    return pd.DataFrame.from_records(resultados)