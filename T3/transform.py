import pandas as pd
import matplotlib.pyplot as plt
def transform_data(df):

    df_cleaned = df.drop_duplicates().copy()
    resumen = df_cleaned.describe()

    return resumen


def graficos(df):
    df_cleaned = df.drop_duplicates().copy()
    df.plot(x)