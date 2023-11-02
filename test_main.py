"""
PySpark Application Test Suite for Car Data
"""
import os
import pytest
from mylib.lib import (
    initiate_spark_session,
    read_dataset,
    transform_origin,
    append_to_report,
)

@pytest.fixture(scope="session")
def spark_session():

    session = initiate_spark_session("TestCarDataProcessing")
    yield session
    session.stop()

def test_data_loading(spark_session):
    data_path = "data/cars.csv" 
    car_df = read_dataset(spark_session, data_path)
    assert car_df is not None and car_df.count() > 0

def test_data_transform(spark_session):
    car_df = read_dataset(spark_session, "data/cars.csv")
    categorized_car_df = transform_origin(car_df)
    assert categorized_car_df is not None
    assert "RegionCategory" in categorized_car_df.columns

def run_tests():
    session = spark_session()
    test_data_loading(session)
    test_data_transform(session)

if __name__ == "__main__":
    run_tests()
