import scripts.validacion_individual as vi
import pandas as pd
import scripts.ingesta as ig
from pathlib import Path

pd.set_option("display.max_rows", None)

BASE_DIR = Path(__file__).resolve().parent
entrada = BASE_DIR / "data" / "raw" / "ventas_datamart.csv"
df = ig.cargar_csv(entrada)

print("Inicio:", df.shape)

df = vi.validar_id_pedido(df)
print("Id Pedido:", df is None)

df = vi.Validar_cantidad(df)
print("Cantidad:", df is None)

#Ultimas 4 columnas
df = vi.Validar_precio_unitario(df)
print("Precio:", df is None)

df = vi.Validar_descuento(df)
print("Descuento:", df is None)

df = vi.Validar_estado_pedido(df)
print("Estado:", df is None)

df = vi.Validar_fecha_despacho(df)
print("Fecha:", df is None)

df = vi.Crear_total_venta(df)
print("Total Venta:", df is None)

df = vi.Crear_segmento_precio(df)
print("Segmento Precio:", df is None)

print(df)