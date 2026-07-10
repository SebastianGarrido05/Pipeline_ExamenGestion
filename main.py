import scripts.ingesta as ing
import scripts.validacion_individual as vi
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

ing.procesar_csv(entrada, salida)


# ing.procesar_csv(entrada, salida)

Carga_bd(pd.read_csv(salida))
