"""
Main application entry point for PySpark data processing
"""

from mylib.lib import create_spark_session, load_data, transform_data, run_sql_query

if __name__ == "__main__":
    spark = create_spark_session("Car Data Analysis")

    data_file_path = "data/cars.csv" 
    df = load_data(spark, data_file_path)

    transformed_df = transform_data(df)

    result_df = run_sql_query(spark, transformed_df)

    result_df.show()

    # result_df.write.format("csv").save("output/average_weight_by_origin.csv")
