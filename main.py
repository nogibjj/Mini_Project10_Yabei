"""
Main application entry point for PySpark data processing
"""
from mylib.lib import (
    initiate_spark_session,
    read_dataset,
    describe,
    transform_origin,
    append_to_report,
)


def run_data_analysis():
    spark = initiate_spark_session("Car Data Analysis")

    data_file_path = "data/cars.csv"
    car_data = read_dataset(spark, data_file_path)
    description_data = describe(car_data)
    description_data.createOrReplaceTempView("description_view")
    transformed_data = transform_origin(car_data)
    transformed_data.createOrReplaceTempView("car_data_view")
    query_result = spark.sql(
        """
        SELECT RegionCategory, COUNT(*) AS TotalCars
        FROM car_data_view
        GROUP BY RegionCategory
        ORDER BY TotalCars DESC
    """
    )

    query_result.show()
    append_to_report(
        "Spark SQL Query Result", query_result.limit(10).toPandas().to_markdown()
    )

    # query_result.write.format("csv").save("output/query_result.csv")

    spark.stop()


if __name__ == "__main__":
    run_data_analysis()
