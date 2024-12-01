
# Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
# datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
# `tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
# librerias de pandas para resolver las preguntas.

# Construya una tabla que contenga `c1` y una lista separada por ':' de los
# valores de la columna `c2` para el archivo `tbl0.tsv`.
# Rta/
# c1
# A               1:1:2:3:6:7:8:9
# ...

import pandas as pd

def pregunta_10():
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    # Agrupar y convertir los valores de c2 en cadenas separadas por ':'
    result = df.groupby('c1')['c2'].apply(lambda x: ':'.join(map(str, sorted(x))))
    # Crear el DataFrame con el índice esperado y la columna `c2`
    result_df = result.reset_index()
    result_df.columns = ['_c1', 'c2']  # Asegurarse de usar los nombres esperados
    result_df.set_index('_c1', inplace=True)  # Configurar `_c1` como índice
    print(result_df)
    return result_df

pregunta_10()
    