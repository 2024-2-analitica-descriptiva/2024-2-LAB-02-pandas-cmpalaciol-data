
# Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
# datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
# `tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
# librerias de pandas para resolver las preguntas.

# Agregue el año como una columna al data frame que contiene el archivo `tbl0.tsv`.
# Rta/
#      c0 c1  c2          c3  year
# 0     0  E   1  1999-02-28  1999
# ...

import pandas as pd

def pregunta_09():
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    df['year'] = df['c3'].str[:4]
    print(df)
    return df

pregunta_09()
    