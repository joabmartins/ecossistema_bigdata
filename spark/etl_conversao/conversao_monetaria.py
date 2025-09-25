from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round

# 1. Inicializar a sessão Spark
spark = SparkSession.builder \
.appName("ETLSimples")\
.getOrCreate()

# 2. Extração (Extract)
try:
    df = spark.read.csv("dados/agencia_bancaria.csv", header=True, inferSchema=True)
    print("Dados extraidos com sucesso!")
except Exception as e:
    print(f"Erro ao extrair dados: {e}")
    spark.stop()
    exit()

# 3. Transformação (Transform)
dados_transformados = df.withColumn("dolar", round(col("saldo") / 5.33, 2))
print("dados transformados com sucesso!")
dados_transformados.show()

# 4. Carregamento (load)
try:
    output_path = "dados/output.csv"
    dados_transformados.write.mode("overwrite").csv(output_path, header=True)
    print(f"Dados carregados para {output_path} com sucesso")
except Exception as e:
    print(f"Erro ao carregar os dados: {e}")
    spark.stop()
    exit()

# 5. Encerra a sessão Spark
spark.stop()