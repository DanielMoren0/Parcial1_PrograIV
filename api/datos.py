import pandas as pd
from sodapy import Socrata


def obtener_datos(limite, departamento, municipio, cultivo):
    cliente = Socrata("www.datos.gov.co", None)
    resultados = cliente.get("ch4u-f3i5", limit=limite, departamento=departamento, municipio=municipio, cultivo=cultivo)
    return pd.DataFrame.from_records(resultados)
