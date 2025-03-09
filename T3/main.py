from extract import extractCSVData
from transform import transform_data
import pandas as pd

def main_menu():

    global df, transformed_data
    while True:
        print("\n--- Menu Principal ---")
        print("1. Extraer datos")
        print("2. transformar data y resumen estadistico")
        print("3. Matriz de corelacion")
        print("4. Realizar consultas predefinidas")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            df = extractCSVData()
            if df is not None:
                print("Datos extraídos correctamente.")
            else:
                print("No se pudo extraer la información.")

        elif opcion == "2":
            if df is None:
                print("Primero debes extraer los datos (opción 3).")
            else:
                transformed_data = transform_data(df)
                print(transformed_data)
        elif opcion == "3":
            df = pd.read_csv("winequality-red.csv", sep=";")
            correlation_matrix = df.corr()
            print(correlation_matrix)
        elif opcion == "4":
           break
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_menu()


