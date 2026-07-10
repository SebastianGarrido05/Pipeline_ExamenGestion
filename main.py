import scripts.ingesta as ig
import scripts.validacion_individual as vi
import pandas as pd
from pathlib import Path
import logging
from scripts.carga import Carga_bd

# login
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# RUTAS TEST
BASE_DIR = Path(__file__).resolve().parent

carpeta = BASE_DIR / "data" / "test"
cont = len(list(carpeta.glob("test*.csv"))) + 1

entrada = BASE_DIR / "data" / "raw" / "ventas_datamart.csv"
salida = BASE_DIR / "data" / "test" / f"test{cont}.csv"
# nombre_archivo = carpeta / f"test{cont}.csv"

# =================================================================

logging.info("Leyendo CSV...")

df = ig.cargar_csv(entrada)

df = vi.Validar_region(df)
df = vi.Validar_producto(df)
df = vi.Validar_categoria(df)
df = vi.Validar_cantidad(df) # ARROJA TABLA // ARREGLAR
df = vi.Validar_precio_unitario(df)
df = vi.Validar_descuento(df)
df = vi.Validar_estado_pedido(df)
df = vi.Validar_fecha_despacho(df)

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

# EXPORTAR

logging.info("Exportando dataset limpio...")

df.to_csv(salida, index=False)

logging.info("Proceso terminado correctamente.")

Carga_bd(df)