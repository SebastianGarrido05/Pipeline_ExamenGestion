import pandas as pd
import logging 

# -------------------------------------------------------------
# CADA UNO HACE 4, VALIDACION DE AMBOS TIPOS Y ADEMÁS LIMPIEZA
# -------------------------------------------------------------
df=None


# id_pedido (S)


    # id_pedido


# Fecha (S)

    # Fecha


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


# Precio unitario



# Descuento



# Estado pedido



# Fecha despacho


