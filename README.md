Descripción del proyecto
Este proyecto tiene como objetivo realizar el análisis de la Tasa Representativa del Mercado (TRM) de Colombia utilizando herramientas de Big Data, específicamente Apache Spark para el procesamiento en batch y Apache Kafka junto con Spark Streaming para el análisis en tiempo real.
El conjunto de datos utilizado fue obtenido desde el portal oficial Datos Abiertos de Colombia, lo que garantiza la confiabilidad y validez de la información analizada. A través de este proyecto se demuestra cómo Apache Spark permite procesar grandes volúmenes de datos históricos de manera eficiente y escalable.
Este desarrollo fue realizado como parte de la Tarea 3 – Procesamiento de Datos con Apache Spark del curso de Big Data de la Universidad Nacional Abierta y a Distancia (UNAD).

Estructura del repositorio
├── batch_trm.py          # Código de procesamiento en batch con Apache Spark
├── trm_colombia.csv      # Conjunto de datos de la TRM (Datos Abiertos Colombia)
├── README.md             # Documentación del proyectoShow more lines

Tecnologías utilizadas

Apache Spark
PySpark (Python)
Apache Kafka
Spark Streaming
Python 3
Datos Abiertos de Colombia


Conjunto de datos

Nombre del dataset: Tasa Representativa del Mercado (TRM) de Colombia
Fuente: Datos Abiertos de Colombia
Formato: CSV
Variables principales:

Fecha
Valor de la TRM



Procesamiento en batch
El procesamiento en batch se realiza mediante un script en Python utilizando PySpark. En este proceso se llevan a cabo las siguientes actividades:

Carga del archivo CSV de la TRM.
Exploración del esquema y estructura del dataset.
Limpieza de datos eliminando valores nulos.
Ordenamiento de los datos por fecha para analizar el comportamiento histórico de la TRM.


Ejecución del código
1. Requisitos previos

Tener instalado Apache Spark
Tener configurado Python y PySpark
Contar con el archivo trm_colombia.csv en la misma carpeta del script

2. Ejecutar el script
Shellspark-submit batch_trm.pyShow more lines

📈 Resultados esperados

Visualización de los datos de la TRM cargados en Spark.
Limpieza correcta de los valores nulos.
Análisis básico del comportamiento histórico de la Tasa Representativa del Mercado.
Evidencia del uso de Apache Spark para el procesamiento de datos en batch.


🎥 Video demostrativo
El video donde se muestra:

El código desarrollado en Apache Spark.
Los resultados del análisis en batch.
El procesamiento en tiempo real usando Kafka y Spark Streaming.

📎 Enlace del video:
👉 (Agregar aquí el enlace del video)

👨‍🎓 Autor
Miguel Andrés Arias Carreño
Estudiante – Ingeniería de Sistemas
Universidad Nacional Abierta y a Distancia – UNAD

📚 Referencias

Datos Abiertos de Colombia. (s.f.). Tasa Representativa del Mercado (TRM).
Apache Spark Documentation.
Apache Kafka Documentation.
