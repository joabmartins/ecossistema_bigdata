from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round

#inicializar a sessão do spark
spark = SparkSession.builder \
.appName("ETLsimples") \
.getOrCreate() \

#extração (extract)
try:
    df = spark.read.csv("dados/agencia_bancaria.csv", header=True, inferSchema=True)
    print("dados extraidos com sucesso!!")
except Exception as e:
    print(f"Erro ao extrair dados: {e}")
    spark.stop()
    exit()

#tranformação (transform)
dados_tansformados = df.withColumn("dolar", round(col("saldo") / 5.33, 2))
print("dados transformados com sucesso!! ")
dados_tansformados.show()

#carregamento
try:
    output_path = "dados/output.csv"
    dados_tansformados.write.mode("overwrite").csv(output_path, header=True)
    print(f"dados carregados {output_path} com sucesso!!")
except Exception as e:
    print(f"erro ao carregar os dados {e}")
    spark.stop()
    exit()

#encerra a sessão spark
spark.stop