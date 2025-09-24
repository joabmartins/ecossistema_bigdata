from pyspark.sql import Sparksession
from pyspark.sql.functions import count

# Inicia a Sessão Spark
spark = Sparksession.builder.appName("CntagemFilmesporAvaliacao").getOrCreat()

# Lê o arquivo CSV
df = spark.read.csv("filmes.csv", header=True, inferSchema=True)

#1. Agrupar
#2. Contar
#3. Ordenar
resultado = df.groupBy("Avaliacao").agg(count("*").alias("total_filmes")).orderBy("Avaliacao")

# Exibe o resultado no console
resultado.show()

spark.stop()