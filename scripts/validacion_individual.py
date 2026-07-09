import pandas as pd
import logging 
import scripts.ingesta as ig
# -------------------------------------------------------------
# CADA UNO HACE 4, VALIDACION DE AMBOS TIPOS Y ADEMÁS LIMPIEZA
# -------------------------------------------------------------

# id_pedido (S)


    # id_pedido


# Fecha (S)

    # Fecha


# Rut cliente (S)

    # Rut cliente


# Nombre cliente (S)

    # Nombre cliente


# Region
def Validar_region():
    try:
        logging.info("validando region cliente...")

        # se quitan espacios y estandarizar formato
        REGIONES_EQUIVALENTES = {
            "Region Metropolitana": "Metropolitana",
            "Metropolitana De Santiago": "Metropolitana",
            "Valparaíso": "Valparaiso",
            "Bio Bio": "Biobio",
            "Biobío": "Biobio",
            "O'Higgins": "OHiggins"
        }

        ig.df["region"] = (
            ig.df["region"]
            .astype("string")
            .fillna("Sin Información")
            .str.strip()
            .str.title()
        )

        ig.df["region"] = ig.df["region"].replace(REGIONES_EQUIVALENTES)

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
        errores_region = ig.df[
            ig.df["region"].isna() |
            (~ig.df["region"].isin(REGIONES_VALIDAS))
        ]
    except Exception as e:

        logging.error(f"Error al validar región: {e}")
   # Region-
    
# Producto
def Validar_producto():
    try:
        logging.info("validando producto cliente...")
        # Quitamos espacios al inicio y final
        ig.df["producto"] = (
            ig.df["producto"]
            .astype("string")
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
            .str.title()
        )

        # Se eliminan espacios dobles o múltiples
        logging.info("corrigiendo faltas ortograficas producto cliente...")
        ig.df["producto"] = ig.df["producto"].str.replace(
            r"\s+",
            " ",
            regex=True
        )

        # Se capitaliza cada palabra
        ig.df["producto"] = ig.df["producto"].str.title()

        # Buscar productos nulos o vacíos
        errores_producto = ig.df[
            ig.df["producto"].isna() |
            (ig.df["producto"] == "")
        ]
    except Exception as e:

        logging.error(f"Error al validar producto: {e}")
        #producto-

# Cateogria
def Validar_categoria():
    try:
        logging.info("validando categoria cliente...")
        #se quitan los espacios y se estandarizar formato
        ig.df["categoria"] = (
            ig.df["categoria"]
            .astype("string")
            .str.strip()
            .str.lower()
        )

        CATEGORIAS_EQUIVALENTES = {
            "tech": "Tecnologia",
            "TECH": "Tecnologia",
            "Tech": "Tecnologia",
            "tecnologia": "Tecnologia",
            "Tecnologia": "Tecnologia",

            "hogar": "Hogar",
            "HOGAR": "Hogar",
            "Hogar": "Hogar",

            "moda": "Moda",
            "MODA": "Moda",
            "Moda": "Moda"
        }

        ig.df["categoria"] = ig.df["categoria"].replace(CATEGORIAS_EQUIVALENTES)

        CATEGORIAS_VALIDAS = [
            "Tecnologia",
            "Hogar",
            "Moda"
        ]

        errores_categoria = ig.df[
            ig.df["categoria"].isna() |
            (~ig.df["categoria"].isin(CATEGORIAS_VALIDAS))
        ]
    except Exception as e:

        logging.error(f"Error al validar categoría: {e}")
            #categoria-

# Cantidad
def Validar_cantidad():
    try:
        logging.info("validando cantidad cliente...")
        # Se convierte la columna a tipo numérico
        ig.df["cantidad"] = pd.to_numeric(
            ig.df["cantidad"],
            errors="coerce"
        )

        # Se buscan cantidades inválidas
        logging.info("buscando faltas de cantidad cliente...")
        ig.df["cantidad"] = df["cantidad"].fillna(1)

        ig.df.loc[df["cantidad"] <= 0, "cantidad"] = 1
            #cantidad-
    except Exception as e:

        logging.error(f"Error al validar cantidad: {e}")


# Precio unitario



# Descuento



# Estado pedido



# Fecha despacho


