from pyspark.sql import SparkSession

# Crear sesión de Spark
spark = SparkSession.builder \
    .appName("Analisis_TRM_Colombia_Batch") \
    .getOrCreate()

# Cargar el archivo CSV de la TRM
df_trm = spark.read.csv(
    "trm_colombia.csv",
    header=True,
    inferSchema=True
)

# Mostrar datos iniciales
df_trm.show(5)

# Ver estructura del dataset
df_trm.printSchema()

# Limpieza de datos
df_trm_clean = df_trm.dropna()

# Renombrar columnas si es necesario (ajusta a tu CSV)
df_trm_clean = df_trm_clean \
    .withColumnRenamed("fecha", "Fecha") \
    .withColumnRenamed("valor", "TRM")

# Ordenar por fecha
df_trm_ordenado = df_trm_clean.orderBy("Fecha")

# Mostrar resultados
df_trm_ordenado.show(10)

spark.stop()
``