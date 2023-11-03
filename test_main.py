"""
PySpark Application Test Suite for Car Data
"""
from pyspark.sql.session import SparkSession
import pytest
from mylib.lib import (
    initiate_spark_session,
    read_dataset,
    describe,
    transform_origin,
)


@pytest.fixture(scope="session")
def spark_session():

    session = initiate_spark_session("TestCarDataProcessing")
    yield session
    session.stop()


def test_data_loading(spark_session: SparkSession):
    data_path = "data/cars.csv"
    car_df = read_dataset(spark_session, data_path)
    assert car_df is not None and car_df.count() > 0

def test_data_describe(spark_session: SparkSession):
    car_df = read_dataset(spark_session, "data/cars.csv")
    description_data = describe(car_df)
    assert description_data is not None

def test_data_transform(spark_session: SparkSession):
    car_df = read_dataset(spark_session, "data/cars.csv")
    transformed_car_df = transform_origin(car_df)
    assert transformed_car_df is not None
    assert "RegionCategory" in transformed_car_df.columns


def run_tests():
    session = spark_session()
    test_data_loading(session)
    test_data_loading(session)
    test_data_transform(session)


if __name__ == "__main__":
    run_tests()
