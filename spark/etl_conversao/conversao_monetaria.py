from pyspark.sql import SparkSession
from pyspark.sql.functions import col,round

# 1. Inicializar a sessao spark
spark = SparkSession.builder \
.appName("ETLSimples") \
.getOrCreate()

#2. Extração (EXTRACT)
try:
     df = spark.read.csv("dados/agencia_bancaria.csv", header=True, inferSchema=True)
     print("Dados extraidos com Sucesso!   ")
except Exception as e:
     print(f"Erro ao extrair dados: {e}")
     spark.stop()
     exit()

# 3. Trasformação (Trasform)
dados_trasformados = df.withColumn("dolar", round(col("saldo") / 5.33, 2))
print("dados trasformados com sucesso! ")
dados_trasformados.show()

#4. Carregamento (Load)
try:
    output_path = "dados/output.csv"
    dados_trasformados.write.mode('overwrite').csv(output_path, header=True)
    print(f"Dados carregados para{output_path} com sucesso! ")
except Exception as e:
     print(f"Erroe ao carregar os dados {e}")
     spark.stop()
     exit()

    # 5. Encerra a sessão Spark

spark.stop()