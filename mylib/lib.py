import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

def create_spark_session(app_name):
    return SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()

def load_data(spark, file_path):
    return spark.read.option("header", "true").csv(file_path, sep=";")

def transform_data(df):
    df = df.withColumn("MPG", col("MPG").cast("float")) \
           .withColumn("Cylinders", col("Cylinders").cast("integer")) \
           .withColumn("Displacement", col("Displacement").cast("float")) \
           .withColumn("Horsepower", col("Horsepower").cast("float")) \
           .withColumn("Weight", col("Weight").cast("float")) \
           .withColumn("Acceleration", col("Acceleration").cast("float")) \
           .withColumn("Model", col("Model").cast("integer")) \
           .withColumn("Origin", col("Origin").cast("string"))

    transformed_df = df.filter(col("MPG") >= 15)
    return transformed_df

def run_sql_query(spark, df):
    df.createOrReplaceTempView("cars")

    result_df = spark.sql("""
        SELECT Origin, AVG(Weight) as Average_Weight
        FROM cars
        GROUP BY Origin
    """)
    return result_df

if __name__ == "__main__":
    spark = create_spark_session("Car Data Analysis")

    data_file_path = "data/cars.csv"  
    df = load_data(spark, data_file_path)

    transformed_df = transform_data(df)

    result_df = run_sql_query(spark, transformed_df)

    result_df.show()

    # result_df.write.format("csv").save("output/average_weight_by_origin.csv")
