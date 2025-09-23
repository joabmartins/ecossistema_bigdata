from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, count

# 1. Iniciar a sessão Spark
spark = SparkSession.builder.appName("AnaliseGenerosPopulares").getOrCreate()


# 2. Lê o arquivo csv
df = spark.read.csv("filmes.csv", header=True, inferSchema=True)

# 3. Obtem filmes com nota acima de 4
df_altas_avaliaçoes = df.filter(df["Avaliacao"] > 4.0)

# 4. Divide a coluna genero
df_generos_array = df_altas_avaliaçoes.withColumn(
    "genero_array",
     split(df_altas_avaliaçoes.genero, ";")
)

# 5. explode (separa) o array de generos difirentes
df_generos_explode = df_generos_array.withColumn(
    "genero_individual", 
    explode(df_generos_array.genero_array)
)

 # 6. Agrupa os dados por cada genero e conta a frequencia 
df_resultado = df_generos_explode.groupBy("genero_individual").agg(count("*").alias("total_filmes")).orderBy("total_filmes", ascending=False)

# 7. Exibir os dados
df_resultado.show(10, truncate=False)

# 8. fecha a sessão
spark.stop()
                                                