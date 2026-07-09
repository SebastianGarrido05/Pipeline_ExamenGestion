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

logging.info("validando region cliente...")

# se quitan espacios y estandarizar formato
ig.df["region"] = (
    ig.df["region"]
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

ig.df["region"] = ig.df["region"].replace(REGIONES_EQUIVALENTES)

# Regiones permitidas según el negocio
REGIONES_VALIDAS = [
    "Metropolitana",
    "Valparaiso",
    "Biobio"
]

# Buscar registros con región inválida o nula
errores_region = ig.df[
    ig.df["region"].isna() |
    (~ig.df["region"].isin(REGIONES_VALIDAS))
]
   # Region-
    
    


# Producto

# Quitamos espacios al inicio y final
ig.df["producto"] = (
    ig.df["producto"]
    .astype("string")
    .str.strip()
)

# Se eliminan espacios dobles o múltiples
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

    #producto-



# Cateogria

#se quitan los espacios y se estandarizar formato
ig.df["categoria"] = (
    ig.df["categoria"]
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
    #categoria-

# Cantidad

# Se convierte la columna a tipo numérico
ig.df["cantidad"] = pd.to_numeric(
    ig.df["cantidad"],
    errors="coerce"
)

# Se buscan cantidades inválidas
errores_cantidad = ig.df[
    ig.df["cantidad"].isna() |
    (ig.df["cantidad"] <= 0)
]
    #cantidad-


    # Precio unitario



    # Descuento



    # Estado pedido



    # Fecha despacho


