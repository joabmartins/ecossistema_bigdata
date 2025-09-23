from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, count

#Inicia a Sessão Spark
spark = SparkSession.builder \
.appName("AnaliseGenerosPopulares") \
.getOrCreate()

#Lê o arquivo csv
df = spark.read.csv("filmes.csv", header=True, inferSchema=True)

#obtem filmes com avaliacao acima de de nota 4
df_altas_avalicoes = df.filter(df["Avaliacao"] > 4.0)

#Divide a coluna genero
df_generos_array = df_altas_avalicoes.withColumn(
    "generos_array",
    split(df_altas_avalicoes.genero, ";")
)

#exlode (separa) o array de diferentes generos
df_generos_explode = df_generos_array.withColumn(
    "genero_individual",
    explode(df_generos_array.generos_array)
)

#Agrupa os dados por cada genero e conta a frequencia
df_resultado = df_generos_explode.groupBy("genero_individual") \
.agg(count("*").alias("total_filmes")) \
.orderBy("total_filmes", ascending=False)

print(df_resultado.show(10, truncate=False))

#fecha a sessão
spark.stop()