from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MyFirstApp").getOrCreate()
df = spark.range(1000).toDF("number")
df.show()

# 加个输入让窗口停留
input("按回车键退出...")