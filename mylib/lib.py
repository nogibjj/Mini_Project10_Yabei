from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os

# Initialize Spark Session
def create_spark_session(app_name):
    return SparkSession.builder.appName(app_name).getOrCreate()

def load_data(spark, file_path):
    return spark.read.option("header", "true").csv(file_path, sep=";")

