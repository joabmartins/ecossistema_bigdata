from pyspark.sql import SparkSession
from pyspark.sql.functions import count 

#inicie uma sessão Spark
spark = SparkSession.builder \
    .appName("ContagemFilmesPoravaliacao") \
    .getOrCreate()

#lê arquivo csv
df=spark.read.csv("filmes.csv", header=True, inferSchema=True)

#1.agrupar
#2. contar
#3. ordenar
resultado = df.groupBy("Avaliacao") \
    .agg(count("*").alias("total_filmes")) \
    .orderBy("Avaliacao")

#exibe o resultado no consol
resultado.show()

spark.stop()