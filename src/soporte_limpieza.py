import pandas as pd
import numpy as np
from datetime import datetime

def mod_titulo_columnas(df):
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace(' ', '_')

def cambio_float(df):   
    for x in df.iloc[:, 10:14]:
        try:
            if df[x].dtypes == "float64":
                df[x] = df[x]
            else:
                df[x] = df[x].str.replace(',', '').astype(float)
        except:
            df[x] = df[x].astype(float)

def cambio_fecha(df):
        df["DATA_LANÇAMENTO"] = df["DATA_LANÇAMENTO"].fillna(method = "bfill")
        df["DATA_LANÇAMENTO"] = pd.to_datetime(df["DATA_LANÇAMENTO"], format='mixed')
        df["DIA_LANÇAMENTO"] = df["DATA_LANÇAMENTO"].dt.day
        df["MES_LANÇAMENTO"] = df["DATA_LANÇAMENTO"].dt.month
        df["ANO_LANÇAMENTO"] = df["DATA_LANÇAMENTO"].dt.year

def limpieza_archivos(df):
    for x in df:
        mod_titulo_columnas(x)
        cambio_float(x)
        cambio_fecha(x)