import pandas as pd
import logging
import scripts.validacion_individual as vi
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

logging.info("Leyendo CSV...")
df = pd.read_csv(file_path)
vi.df=df

vi.Validar_region(df)
vi.Validar_producto(df)
vi.Validar_categoria(df)
vi.Validar_cantidad(df)
vi.Validar_precio_unitario(df)
vi.Validar_descuento(df)
vi.Validar_estado_pedido(df)
vi.Validar_fecha_despacho(df)

logging.info("Normalizando texto...")
df = df.map(lambda x: x.lower().strip() if isinstance(x, str) else x)

logging.info("Ordenando por id_pedido...")
df = df.sort_values(by='id_pedido')

logging.info("Eliminando filas completamente vacías...")
df = df.dropna(
    subset=[
        'id_pedido','fecha_pedido','rut_cliente',
        'nombre_cliente','region','producto','categoria',
        'cantidad','precio_unitario','descuento_pct',
        'estado_pedido','fecha_despacho'
    ],
    how='all'
)
df=vi.df

# EXPORTAR

logging.info("Exportando dataset limpio...")

df.to_csv(output_path, index=False)

logging.info("Proceso terminado correctamente.")
