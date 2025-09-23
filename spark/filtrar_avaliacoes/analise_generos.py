from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, count

# 1.inicia a sessão Spark
spark = SparkSession.builder \
.appName("AnaliseGenerosPopulares") \
.getOrCreate()

#2. lê o arquivo csv
df = spark.read.csv("filmes.csv", header=True, inferSchema=True)

#3. obtem filmes com nota acima de 4
df_altas_avaliacoes = df.filter(df["Avaliacao"]> 4.0)

#4. divide a coluna genero
df_generos_array = df_altas_avaliacoes.withColumn(
    "genero_array",
    split(df_altas_avaliacoes.genero, ";")
)

#5. explode (separa) o array de generos diferentes
df_generos_explode = df_generos_array.withColumn(
    "genero_individual",
    explode(df_generos_array.genero_array)
)

#6. agrupa os daods por cada genero e contra a frequencia
df_resultado = df_generos_explode.groupBy("genero_individual") \
.agg(count("*").alias("total_filmes")) \
.orderBy("total_filmes", ascending=False)

#7. exibir dados
df_resultado.show(10, truncate=False)

#8.fecha a sessão
spark.stop()