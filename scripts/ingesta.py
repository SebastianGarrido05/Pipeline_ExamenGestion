import pandas as pd
import logging
import scripts.validacion_individual as vi
from datetime import datetime

# logging.info("Leyendo CSV...")
def cargar_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        logging.error(f"Error al cargar el CSV: {e}")
        return pd.DataFrame()

# df = cargar_csv("./data/raw/ventas_datamart.csv")
#         'nombre_cliente','region','producto','categoria',
#         'cantidad','precio_unitario','descuento_pct',
#         'estado_pedido','fecha_despacho'
#     ],
#     how='all'
# )
