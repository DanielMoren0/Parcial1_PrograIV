<<<<<<< HEAD
import api.datos_covid
=======
import api.datos
>>>>>>> d151273 (commit funcionando)
import ui.mostrar

def main():
    limite_registros = input("Digite el número de registros que desea consultar:")
    nombre_departamento = input("Ingrese el departamento que desea consultar:")
    #nombre_municipio = input("Ingrese el municipio que desea consultar:")
    #nombre_cultivo = input("Ingrese el cultivo que desea consultar:")

<<<<<<< HEAD
    data_frame = api.datos_covid.obtener_datos_covid(limite_registros, nombre_departamento.upper())
=======
    data_frame = api.datos.obtener_datos(limite_registros, nombre_departamento.upper())
>>>>>>> d151273 (commit funcionando)
    ui.mostrar.mostrar_datos(data_frame)

    ui.mostrar.mostrar_mediana(data_frame, "ph_agua_suelo_2_5_1_0")
    ui.mostrar.mostrar_mediana(data_frame, "f_sforo_p_bray_ii_mg_kg")
    ui.mostrar.mostrar_mediana(data_frame, "potasio_k_intercambiable_cmol_kg")

if __name__ == "__main__":
    main()