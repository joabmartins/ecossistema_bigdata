from pyspark.sql import Sparksession
from pyspark.sql.functions import count


# Inicia a Sessão Spark
spark = Sparksession.builder.appName("ContagemFilmesPorAvaliacao").getOrCreat()

#Lê o arquivo Csv
df = spark.read.csv("filmes.csv", header=True, inferSchema=True)

#1 agrupar
#2 Contar
3# Ordenar

resultado = df.groupBy("Avaliacao") \
    .agg(count("*").alias("total_filmes")) \
    .orderBy("Avaliacao")

#Exibe o resultado no console
resultado.show()

spark.stop()