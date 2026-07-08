import pandas as pd
import logging 
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

logging.info("validando region cliente...")

# se quitan espacios y estandarizar formato
df["region"] = (
    df["region"]
    .astype("string")
    .str.strip()
    .str.title()
)

# se corrigen variantes conocidas
REGIONES_EQUIVALENTES = {
    "Metropolitana De Santiago": "Metropolitana",
    "Region Metropolitana": "Metropolitana",
    "Valparaíso": "Valparaiso",
    "Bio Bio": "Biobio",
    "Biobío": "Biobio"
}

df["region"] = df["region"].replace(REGIONES_EQUIVALENTES)

# Regiones permitidas según el negocio
REGIONES_VALIDAS = [
    "Metropolitana",
    "Valparaiso",
    "Biobio"
]

# Buscar registros con región inválida o nula
errores_region = df[
    df["region"].isna() |
    (~df["region"].isin(REGIONES_VALIDAS))
]
   # Region-
    
    


# Producto

# Quitamos espacios al inicio y final
df["producto"] = (
    df["producto"]
    .astype("string")
    .str.strip()
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

    #producto-



# Cateogria

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
    "tecnología": "Tecnologia",
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
    #categoria-

# Cantidad

# Se convierte la columna a tipo numérico
df["cantidad"] = pd.to_numeric(
    df["cantidad"],
    errors="coerce"
)

# Se buscan cantidades inválidas
errores_cantidad = df[
    df["cantidad"].isna() |
    (df["cantidad"] <= 0)
]
    #cantidad-


    # Precio unitario



    # Descuento



    # Estado pedido



    # Fecha despacho


