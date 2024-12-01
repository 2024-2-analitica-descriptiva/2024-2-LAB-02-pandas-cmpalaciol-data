
# Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
# datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
# `tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
# librerias de pandas para resolver las preguntas.

# Construya una tabla que contenga `c0` y una lista separada por ','
# de los valores de la columna `c5a`  y `c5b` (unidos por ':') de la tabla `tbl2.tsv`.
# Rta/
#      c0                                   c5
# 0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
# ...

import pandas as pd

def pregunta_12():
    df = pd.read_csv("files/input/tbl2.tsv", sep="\t")
    df['c5'] = df['c5a'] + ':' + df['c5b'].astype(str)
    result = df.groupby('c0')['c5'].apply(lambda x: ','.join(sorted(x))).reset_index()
    print(result)
    return result

pregunta_12()
    