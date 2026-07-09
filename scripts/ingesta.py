import pandas as pd
import logging
from datetime import datetime

# logging.info("Leyendo CSV...")
df = pd.read_csv("./data/raw/ventas_datamart.csv")

# logging.info("Eliminando filas completamente vacías...")
# df = df.dropna(
#     subset=[
#         'id_pedido','fecha_pedido','rut_cliente',
#         'nombre_cliente','region','producto','categoria',
#         'cantidad','precio_unitario','descuento_pct',
#         'estado_pedido','fecha_despacho'
#     ],
#     how='all'
# )

