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

# errores_dir = BASE_DIR / "data" / "errors" / f"errores{cont}.csv"
# errores_dir.mkdir(exist_ok=True)

# nombre_archivo = carpeta / f"test{cont}.csv"

# =================================================================

logging.info("Leyendo CSV...")

df = ig.cargar_csv(entrada)

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

logging.info("Normalizando texto...")
df = df.map(lambda x: x.lower().strip() if isinstance(x, str) else x)

# df = vi.Validar_id_pedido(df)
logging.info("Ordenando por id_pedido...")
df = df.sort_values(by='id_pedido')

logging.info("Alistando Rut de los clientes...")
df = vi.Validar_rut_cliente(df)

logging.info("Ajustando nombres de clientes...")
df = vi.Validar_nombre_cliente(df)

logging.info("Validando fecha de pedido...")
df = vi.Validar_fecha_pedido(df)

logging.info("Validando región...")
df = vi.Validar_region(df)

logging.info("Asegurando productos...")
df = vi.Validar_producto(df)

logging.info("Validando categorías...")
df = vi.Validar_categoria(df)

logging.info("Regulando Cantidades...")
df = vi.Validar_cantidad(df) # ARROJA TABLA // ARREGLAR

logging.info("Corroborando precio unitario...")
df = vi.Validar_precio_unitario(df)

logging.info("Exportando Segmentos...")
df = vi.Crear_segmento_precio(df)

logging.info("Asignando descuentos...")
df = vi.Validar_descuento(df)

logging.info("Asegurando estado del pedido...")
df = vi.Validar_estado_pedido(df)

logging.info("Registrando Fecha de Despacho...")
df = vi.Validar_fecha_despacho(df)

logging.info("Calculando Total de Venta...")
df = vi.Crear_total_venta(df)

# EXPORTAR

logging.info("Exportando dataset limpio...")

salida_clean = BASE_DIR / "data" / "clean" / "DF_Limpio.csv"  # USAR CUANDO NO SE ESTÉ TESTEANDO Y SE QUIERA GUARDAR EL DF LIMPIO FINAL

df.to_csv(salida, index=False)
Carga_bd(df)
logging.info("Proceso terminado correctamente.")