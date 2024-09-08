import pandas as pd
from tabulate import tabulate


def mostrar_datos(data_frame):
    lista = ["departamento", "municipio", "cultivo", "topografia", "ph_agua_suelo_2_5_1_0", "f_sforo_p_bray_ii_mg_kg",
             "potasio_k_intercambiable_cmol_kg"]

    # Redondear las columnas de fósforo y potasio a 2 decimales
    data_frame["f_sforo_p_bray_ii_mg_kg"] = data_frame["f_sforo_p_bray_ii_mg_kg"].round(2)
    data_frame["potasio_k_intercambiable_cmol_kg"] = data_frame["potasio_k_intercambiable_cmol_kg"].round(2)

    # Mostrar la tabla con los valores redondeados
    print(tabulate(data_frame[lista], tablefmt="fancy_grid",
                   headers=["Departamento", "Municipio", "Cultivo", "Topologia", "PH", "Fosforo", "Potasio"]))


def mostrar_mediana(data_frame, columna):
    # Asegurarse de que los datos en la columna sean numéricos
    data_frame[columna] = pd.to_numeric(data_frame[columna], errors='coerce')

    # Calcular la mediana
    mediana = data_frame[columna].median()

    # Mostrar la mediana
    print(f"La mediana de la columna '{columna}' es: {mediana}")
    return mediana
