import pandas as pd
import logging
from datetime import datetime

# login
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def procesar_csv(file_path, output_path):

    logging.info("Leyendo CSV...")
    df = pd.read_csv(file_path)

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

    df.to_csv(output_path, index=False)

    logging.info("Proceso terminado correctamente.")