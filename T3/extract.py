import pandas as pd

def extractCSVData():
    try:
        df = pd.read_csv("winequality-red.csv", sep=";")  # Usa `sep=";"`
        print("Datos cargados correctamente.")
        return df
    except Exception as e:
        print("Error al cargar el archivo CSV:", e)
        return None