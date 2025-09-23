from pyspark.sql import SparkSession
from pyspark.sql.functions import count

#inicia a seção Spark
Spark = SparkSession.builder \
.appName("ContageFilmesPorAvaliacao") \
.getOrCreate()

#lê o arquivo csv
df = Spark.read.csv("filmes.csv", header=True, inferSchema=True)

#1. Agrupar
#2. Contar
#3. Ordendar
resultado = df.groupBy("Avaliacao") \
    .agg(count("*").alias("total_filmes")) \
    .orderBy("Avaliacao")
#Exibe o resultado no console
resultado.show()

Spark.stop()