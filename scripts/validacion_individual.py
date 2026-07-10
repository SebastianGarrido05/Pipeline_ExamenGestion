import pandas as pd
import numpy as np
import logging 

# -------------------------------------------------------------
# CADA UNO HACE 4, VALIDACION DE AMBOS TIPOS Y ADEMÁS LIMPIEZA
# -------------------------------------------------------------

def convertir_fecha(fecha):
    FORMATOS = [
    "%Y-%m-%d",
    "%d/%m/%Y",
    "%d-%m-%Y"]

    if pd.isna(fecha):
        return pd.NA
    
    fecha = str(fecha).strip()

    if fecha == "":
        return pd.NA

    for formato in FORMATOS:
        try:
            return pd.to_datetime(fecha, format=formato).strftime("%Y-%m-%d")
        except ValueError:
            continue

    return pd.NA


# id_pedido (S)
def validar_id_pedido(df):
    try:
        # Se ordena el df por 'id_pedido'
        logging.info("Ordenando por id_pedido...")
        df = df.sort_values(by='id_pedido')

        # Se busca duplicados en la columna 'id_pedido'
        logging.info("Normalizando texto...")
        df = df.map(lambda x: x.lower().strip() if isinstance(x, str) else x)

        df["id_pedido"] = pd.to_numeric(df["id_pedido"], errors="coerce")   # Convierte a numerico, si no se puede los deja cmo NaN
        df["id_pedido"] = df["id_pedido"].fillna(pd.NA)                     # Saca nulos
        df["id_pedido"] = df["id_pedido"].astype("Int64")                   # Conviente a entero

        return df
    except Exception as e:
        logging.error(f"Error al validar id_pedido: {e}")
        return None

# Fecha (S)

def Validar_fecha_pedido(df):
    try:
        # Se da formato a la columna de fecha de pedido utilizando la funcion convertir fecha
        df["fecha_pedido"] = df["fecha_pedido"].apply(convertir_fecha)

        # Se buscan registros con fecha de pedido nula
        errores_fecha_pedido = df[df["fecha_pedido"].isna()]

        # Se reemplazan los valores nulos de fecha de pedido con "None"
        df["fecha_pedido"] = df["fecha_pedido"].fillna("None")

        return df
    except Exception as e:
        logging.error(f"Error al validar fecha de pedido: {e}")
        return None


# Rut cliente (S)

    # Rut cliente


# Nombre cliente (S)

    # Nombre cliente


# Region
def Validar_region(df):
    try:
        # se quitan espacios y estandarizar formato
        REGIONES_EQUIVALENTES = {
            "": "Sin Información",
            "metropolitana": "Metropolitana",
            "region metropolitana": "Metropolitana",
            "metropolitana de santiago": "Metropolitana",

            "valparaiso": "Valparaiso",
            "valparaíso": "Valparaiso",

            "biobio": "Biobio",
            "bio bio": "Biobio",
            "biobío": "Biobio",

            "araucania": "Araucania",

            "coquimbo": "Coquimbo",

            "maule": "Maule",

            "ohiggins": "OHiggins",
            "o'higgins": "OHiggins"
        }

        df["region"] = (
            df["region"]
            .astype("string")
            .fillna("")
            .str.strip()
            .str.lower()
        )

        df["region"] = df["region"].replace(REGIONES_EQUIVALENTES)

        # Regiones permitidas según el negocio
        REGIONES_VALIDAS = [
            "Metropolitana",
            "Valparaiso",
            "Biobio",
            "Araucania",
            "Coquimbo",
            "Maule",
            "OHiggins"
        ]

        # Buscar registros con región inválida o nula
        logging.info("Buscando nulos de region cliente...")
        errores_region = df[
            df["region"].isna() |
            (~df["region"].isin(REGIONES_VALIDAS))
        ]
        return df
    except Exception as e:
        logging.error(f"Error al validar región: {e}")
        # Region-
    
# Producto
def Validar_producto(df):
    try:
        # Quitamos espacios al inicio y final
        df["producto"] = (
            df["producto"]
            .astype("string")
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
            .str.title()
        )

        # Se eliminan espacios dobles o múltiples
        df["producto"] = df["producto"].str.replace(
            r"\s+",
            " ",
            regex=True
        )

        # Se capitaliza cada palabra
        df["producto"] = df["producto"].str.title()

        # Buscar productos nulos o vacíos
        errores_producto = df[
            df["producto"].isna() |
            (df["producto"] == "")
        ]
        return df
    except Exception as e:

        logging.error(f"Error al validar producto: {e}")
        #producto-

# Cateogria
def Validar_categoria(df):
    try:
        #se quitan los espacios y se estandarizar formato
        df["categoria"] = (
            df["categoria"]
            .astype("string")
            .str.strip()
            .str.lower()
        )

        CATEGORIAS_EQUIVALENTES = {
            "tech": "Tecnologia",
            "technology": "Tecnologia",
            "tecnologia": "Tecnologia",

            "hogar": "Hogar",

            "moda": "Moda"
        }

        df["categoria"] = df["categoria"].replace(CATEGORIAS_EQUIVALENTES)

        CATEGORIAS_VALIDAS = [
            "Tecnologia",
            "Hogar",
            "Moda"
        ]

        errores_categoria = df[
            df["categoria"].isna() |
            (~df["categoria"].isin(CATEGORIAS_VALIDAS))
        ]
        return df
    except Exception as e:

        logging.error(f"Error al validar categoría: {e}")
            #categoria-

# Cantidad
def Validar_cantidad(df):
    try:
        # Se convierte la columna a tipo numérico
        df["cantidad"] = pd.to_numeric(
            df["cantidad"],
            errors="coerce"
        )

        # Se buscan cantidades inválidas
        df["cantidad"] = df["cantidad"].fillna(1)

        print(df["cantidad"].dtype)
        print(df["cantidad"].head(20))

        print("Menores o iguales a 0:")
        print(df[df["cantidad"] <= 0])

        df.loc[df["cantidad"] <= 0, "cantidad"] = 1

        print("Después de la corrección:")
        print(df[df["cantidad"] <= 0])
            #cantidad-    
        return df
    except Exception as e:

        logging.error(f"Error al validar cantidad: {e}")

# Ultimas 4 columnas
# Precio unitario
def Validar_precio_unitario(df):
    precios = {
        "Apiradora Robot Xiaomi": 39990,
        "Auriculares Sony WH-1000": 49990,
        "Bolso Cuero Sintetico": 19990,
        "Cafetera De Longhi": 79990,
        "Chaqueta Parka Columbia": 29990,
        "Disco SSD 500GB": 59990,
        "Freidora de Aire Ultracomb": 69990,
        "Gorra New Era": 4990,
        "Hervidor Electrico Oster": 29990,
        "Jeans Skinny Levi's": 9990,
        "Lampara LED de Escritorio": 14990,
        "Licuadora Oster 600W": 39990,
        "Microondas Mabe 20L": 79990,
        "Monitor Samsung 24": 149990,
        "Mouse Inalambrico Logitech": 14990,
        "Notebook Lenovo IdeaPad": 199990,
        "Parka Impermeable North Face": 39990,
        "Pendrive 64GB Kingston": 19990,
        "Perfume Hugo Boss": 39990,
        "Plancha a Vapor Philips": 14990,
        "Polera Oversize Zara": 9990,
        "Purificador Aire Xiaomi": 99990,
        "Set Cuchillos Tramontina":39990,
        "Smart TV 43 LG": 199990,
        "Tablet Samsung A8": 79990,
        "Teclado Mecanico Redragon": 19990,
        "Vestido Floral H&M": 14990,
        "Webcam Logitech C920": 79990,
        "Zapatillas Nike Air Max": 39990
    }
    try:
        # Se eliminan simbolos de moneda y comas
        df["precio_unitario"] = (
            df["precio_unitario"]
            .str.replace("$","", regex=False)
            .str.replace(",","", regex=False)
        )

        # Se asignan precios unitarios segun el producto
        df["precio_unitario"] = (
            df["producto"].map(precios).fillna(df["precio_unitario"])
        )

        # Se convierte la columna a tipo int
        df["precio_unitario"] = df["precio_unitario"].astype("float")

        # Se buscan precios unitarios inválidos
        errores_precio_unitario = df[
            df["precio_unitario"].isna() |
            (df["precio_unitario"] <= 0)
        ]

        return df
    except Exception as e:
        logging.error(f"Error al validar precio unitario: {e}")
        return None

# Descuento
def Validar_descuento(df):
    try:
        # Se eliminan simbolos de porcentaje y comas
        df["descuento_pct"] = (
            df["descuento_pct"]
            .astype("string")
            .str.replace("%","", regex=False)
            .str.replace(",","", regex=False)
        )

        # Se convierte la columna a tipo float
        df["descuento_pct"] = pd.to_numeric(
            df["descuento_pct"],
            errors="coerce"
        ).astype("float")

        df.loc[df["descuento_pct"] < 0, "descuento_pct"] = 0
        df.loc[df["descuento_pct"] > 100, "descuento_pct"] = 100

        # Se buscan descuentos invalidos
        errores_descuento = df[
            df["descuento_pct"].isna() |
            (df["descuento_pct"] < 0) |
            (df["descuento_pct"] > 100)
        ]
        return df
    except Exception as e:
        logging.error(f"Error al validar descuento: {e}")
        return None


# Estado pedido

def Validar_estado_pedido(df):
    try:
        # Se estandariza el formato de la columna
        df["estado_pedido"] = (
            df["estado_pedido"]
            .astype("string")
            .str.strip()
            .str.lower()
        )

        ESTADOS_EQUIVALENTES = {
            "pendiente": "Pendiente",
            "cancelado": "Cancelado",
            "despachado": "Despachado",
            "entregado": "Entregado"
        }

        df["estado_pedido"] = df["estado_pedido"].replace(ESTADOS_EQUIVALENTES)

        ESTADOS_VALIDOS = [
            "Pendiente",
            "Cancelado",
            "Despachado",
            "Entregado"
        ]

        errores_estado_pedido = df[
            df["estado_pedido"].isna() |
            (~df["estado_pedido"].isin(ESTADOS_VALIDOS))
        ]
        return df
    except Exception as e:
        logging.error(f"Error al validar estado del pedido: {e}")
        return None


# Fecha despacho

def Validar_fecha_despacho(df):
    try:
        # Se da formato a la columna de fecha de despacho utilizando la funcion convertir fecha
        df["fecha_despacho"] = df["fecha_despacho"].apply(convertir_fecha)

        # Se buscan registros con fecha de despacho nula
        errores_fecha_despacho = df[df["fecha_despacho"].isna()]

        # Se reemplazan los valores nulos de fecha de despacho con "None"
        df["fecha_despacho"] = df["fecha_despacho"].fillna("None")

        return df
    except Exception as e:
        logging.error(f"Error al validar fecha de despacho: {e}")
        return None

# Funcion total venta (nueva columna)
def Crear_total_venta(df):
    try:
        df["total_venta"] = np.ceil(
            df["cantidad"] *
            df["precio_unitario"] *
            (1 - df["descuento_pct"] / 100)
        )
        return df

    except Exception as e:
        logging.error(f"Error al calcular total de venta: {e}")
        return None
    
# Crear segmento de precio (nueva columna)
def Crear_segmento_precio(df):
    try:
        # Se crea la columna de segmento de precio
        df["segmento_precio"] = pd.cut(
            df["precio_unitario"],
            bins=[0, 10000, 50000, float("inf")],
            labels=["Bajo", "Medio", "Alto"],
            right=False
        )
        return df
    except Exception as e:
        logging.error(f"Error al crear segmento de precio: {e}")
        return None