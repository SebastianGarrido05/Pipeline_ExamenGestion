import logging
from scripts.conexion import conectar


def Carga_bd(df):

    conexion = None
    cursor = None

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO "Cliente"(
            rut_cliente,
            nombre_cliente,
            region
        )
        VALUES (%s, %s, %s)
        ON CONFLICT (rut_cliente) DO NOTHING;
        """

        clientes = df[
            [
                "rut_cliente",
                "nombre_cliente",
                "region"
            ]
        ].drop_duplicates()

        for _, fila in clientes.iterrows():
            cursor.execute(
                sql,
                (
                    fila["rut_cliente"],
                    fila["nombre_cliente"],
                    fila["region"]
                )
            )

        sql = """
        INSERT INTO "Producto"(
            producto,
            categoria,
            precio_unitario,
            segmento_precio,
            descuento_pct
        )
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (producto) DO NOTHING;
        """

        productos = df[
            [
                "producto",
                "categoria",
                "precio_unitario",
                "segmento_precio",
                "descuento_pct"
            ]
        ].drop_duplicates()

        for _, fila in productos.iterrows():
            cursor.execute(
                sql,
                (
                    fila["producto"],
                    fila["categoria"],
                    fila["precio_unitario"],
                    fila["segmento_precio"],
                    fila["descuento_pct"]
                )
            )

        sql = """
        INSERT INTO "Pedido"(
            id_pedido,
            rut_cliente,
            producto,
            cantidad,
            estado_pedido,
            fecha_pedido,
            fecha_despacho,
            total_venta
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id_pedido) DO NOTHING;
        """

        for _, fila in df.iterrows():
            cursor.execute(
                sql,
                (
                    fila["id_pedido"],
                    fila["rut_cliente"],
                    fila["producto"],
                    fila["cantidad"],
                    fila["estado_pedido"],
                    fila["fecha_pedido"],
                    fila["fecha_despacho"],
                    fila["total_venta"]
                )
            )

        conexion.commit()

        logging.info(
            "Datos cargados correctamente en la base de datos."
        )

    except Exception as e:

        if conexion:
            conexion.rollback()

        logging.error(
            f"Error al cargar datos en la base de datos: {e}"
        )

        raise

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()