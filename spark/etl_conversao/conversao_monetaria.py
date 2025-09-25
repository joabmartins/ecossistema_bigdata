from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round

# 1.Inicializar a sessão do Spark
spark = SparkSession.builder.appName("ETLSimples").getOrCreate()

# 2.Extração (Extract)
try:
    df = spark.read.csv("dados/agencia_bancaria.csv", header=True, inferSchema=True)
    print("Dados extraídos com sucesso!")
except Exception as e:
    print(f"Erro ao extrair dados: {e}")
    spark.stop()
    exit()

# 3.Transformação (Transform)
dados_transformados = df.withColumn("dolar", round(col("saldo") / 5.33, 2))
print("os dados foram transformados com sucesso!")
dados_transformados.show()

# 4. Carregamento (Load)
try:
    output_path = "dados/output.csv"
    dados_transformados.write.mode("overwrite").csv(output_path, header=True)
    print(f"Os Dados carregados para {output_path} com sucesso!")
except Exception as e:
    print(f"Erro ao carregar os dados: {e}")
    spark.stop()
    exit()

# 5.Encerra a sessão do Spark

spark.stop()