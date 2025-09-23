from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, count

# Inicia a Sessão Spark.
spark = SparkSession.builder \
.appName("AnaliseGenerosPopulares") \
.getOrCreate()

# Lê o arquivo CSV.

df = spark.read.csv("filmes.csv", header=True, inferSchema=True)

#  Obtém filmes com nota acima de 4.

df_altas_avaliacoes = df.filter(df["Avaliacao"] > 4.0)

# Divide  a coluna genero.

df_generos_array = df_altas_avaliacoes.withColumn(
    "genero_array",
    split(df_altas_avaliacoes.genero, ";")
)

# Explode (separa) o array de gêneros diferentes.

df_generos_explode = df_generos_array.withColumn(
    "genero_individual",
    explode(df_generos_array.genero_array)
)

#  Agrupa os dados por cada genero e conta a frequência.

df_resultado = df_generos_explode.groupBy("genero_individual") \
.agg(count("*").alias("total_filmes")) \
.orderBy("total_filmes", ascending=False)

# Exibir os dados

df_resultado.show(10, truncate=False)

# Fecha a sessão.

spark.stop()