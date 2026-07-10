# Pipeline ETL para Gestión de Datos

## Descripción

Este proyecto implementa un proceso **ETL (Extract, Transform and Load)** desarrollado en Python, cuyo propósito es automatizar el procesamiento de datos provenientes de un archivo CSV. Durante la ejecución, el pipeline realiza las etapas de extracción, limpieza, validación, transformación y carga de la información hacia una base de datos PostgreSQL.

El desarrollo fue realizado como parte de la evaluación de la asignatura **Gestión de Datos**, aplicando principios de calidad de datos, modularidad, trazabilidad y buenas prácticas de programación.

---

# Objetivos

## Objetivo General

Desarrollar un pipeline ETL capaz de procesar información de ventas, garantizando la calidad de los datos antes de su almacenamiento en una base de datos relacional.

## Objetivos Específicos

* Automatizar la lectura de archivos CSV.
* Validar la integridad y consistencia de los datos.
* Detectar y corregir errores estructurales y semánticos.
* Aplicar transformaciones necesarias para enriquecer la información.
* Almacenar los datos procesados en PostgreSQL.
* Registrar cada etapa del proceso mediante un sistema de logging.

---

# Arquitectura del Pipeline

```text
                      Archivo CSV
                           │
                           ▼
                     Ingesta de Datos
                           │
                           ▼
                    Limpieza de Datos
                           │
                           ▼
          Validación Estructural y Semántica
                           │
                           ▼
                 Transformación de Datos
                           │
                           ▼
                Carga en PostgreSQL
```

---

# Tecnologías Utilizadas

| Tecnología | Descripción                           |
| ---------- | ------------------------------------- |
| Python 3   | Lenguaje principal del proyecto       |
| Pandas     | Manipulación y procesamiento de datos |
| NumPy      | Operaciones numéricas                 |
| PostgreSQL | Base de datos relacional              |
| psycopg2   | Conexión entre Python y PostgreSQL    |
| Logging    | Registro de eventos del sistema       |
| Pathlib    | Gestión de rutas de archivos          |

---

# Estructura del Proyecto

```text
Pipeline_ExamenGestion/

│
├── data/
│   ├── raw/
│   ├── clean/
│   └── test/
│
├── scripts/
│   ├── conexion.py
│   ├── ingesta.py
│   ├── validacion.py
│   ├── validacion_individual.py
│   └── carga.py
│
├── main.py
└── README.md
```

---

# Descripción del Pipeline

## 1. Ingesta

El proceso comienza con la lectura del archivo CSV utilizando Pandas. En esta etapa se verifica la existencia del archivo y se carga su contenido en un DataFrame para iniciar el procesamiento.

## 2. Limpieza

La etapa de limpieza tiene como finalidad mejorar la calidad de la información mediante acciones como:

* Eliminación de registros vacíos.
* Eliminación de espacios innecesarios.
* Normalización del formato de texto.
* Corrección de formatos.
* Organización de los datos.

## 3. Validación

Antes de continuar con el procesamiento, el sistema verifica que los datos cumplan las reglas definidas para el proyecto.

Las validaciones consideran, entre otros aspectos:

* Identificador del pedido.
* RUT del cliente.
* Nombre del cliente.
* Fecha del pedido.
* Región.
* Producto.
* Categoría.
* Cantidad.
* Precio unitario.
* Descuento.
* Estado del pedido.
* Fecha de despacho.

Estas validaciones permiten detectar información incompleta, formatos inválidos y datos inconsistentes.

## 4. Transformación

Una vez validados los datos, el pipeline genera nuevas variables derivadas que enriquecen la información disponible para su posterior análisis.

Entre ellas destacan:

* Cálculo del total de venta.
* Clasificación por segmento de precio.
* Normalización de valores de texto.

## 5. Carga

Finalmente, la información es almacenada en una base de datos PostgreSQL.

El modelo de datos está compuesto por las siguientes tablas:

* Cliente
* Producto
* Pedido

La inserción de registros considera mecanismos para evitar duplicidad de información mediante el uso de restricciones y operaciones de control sobre conflictos.

---

# Validaciones Implementadas

El proyecto contempla dos niveles principales de validación.

## Validación Estructural

Comprueba que:

* Existan todas las columnas requeridas.
* Los tipos de datos sean correctos.
* No existan valores nulos en campos críticos.
* Los formatos sean válidos.

## Validación Semántica

Comprueba que:

* Los valores pertenezcan al dominio esperado.
* Las fechas sean coherentes.
* Los precios sean positivos.
* Las cantidades sean mayores que cero.
* Los descuentos correspondan a valores válidos.
* El estado del pedido sea consistente.

---

# Modelo de Base de Datos

El pipeline utiliza un modelo relacional compuesto por tres entidades principales.

```text
Cliente
    │
    │
    ▼
Pedido
    ▲
    │
Producto
```

Esta estructura evita redundancia de información y mantiene la integridad referencial entre las entidades.

---

# Instalación

Clonar el repositorio:

```bash
git clone https://github.com/usuario/Pipeline_ExamenGestion.git
```

Instalar las dependencias:

```bash
pip install pandas numpy psycopg2
```

Configurar los parámetros de conexión a PostgreSQL en el archivo correspondiente.

Ubicar el archivo CSV dentro del directorio:

```text
data/raw/
```

---

# Ejecución

Para ejecutar el pipeline:

```bash
python main.py
```

Una vez iniciado, el sistema ejecutará automáticamente todas las etapas del proceso ETL.

---

# Resultados Esperados

Al finalizar la ejecución se obtiene:

* Datos limpios y normalizados.
* Registros validados.
* Información transformada.
* Inserción de datos en PostgreSQL.
* Registro detallado de todas las operaciones realizadas.

---

# Registro de Eventos

El proyecto utiliza el módulo `logging` para documentar cada una de las etapas del proceso.

Se registran eventos relacionados con:

* Inicio y finalización del pipeline.
* Lectura de archivos.
* Validaciones ejecutadas.
* Transformaciones realizadas.
* Inserciones en la base de datos.
* Errores detectados durante la ejecución.

Este mecanismo facilita la trazabilidad y el mantenimiento del sistema.

---

# Buenas Prácticas Aplicadas

Durante el desarrollo se implementaron diversas prácticas recomendadas para proyectos de ingeniería de datos:

* Organización modular del código.
* Separación de responsabilidades.
* Validaciones independientes.
* Reutilización de funciones.
* Registro de eventos mediante logging.
* Control de duplicidad de registros.
* Uso de una base de datos relacional para garantizar la integridad de la información.

---


# Conclusiones

El desarrollo de este proyecto permitió implementar un pipeline ETL completo siguiendo una arquitectura modular y aplicando procesos de validación, limpieza y transformación de datos antes de su almacenamiento.

La solución obtenida demuestra la importancia de la calidad de los datos dentro de un proceso ETL y evidencia la utilidad de herramientas como Python, Pandas y PostgreSQL para automatizar procesos de integración de información de manera confiable y escalable.

---

# Autores

Sebastian Garrido

Martin Calderon

Dylan Cruz
