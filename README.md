[![CI](https://github.com/nogibjj/Mini_Project10_Yabei/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Mini_Project10_Yabei/actions/workflows/cicd.yml)
# Mini Project 10

## Overview

This project utilizes PySpark to perform data processing on a dataset of car attributes. The main objective is to analyze the car dataset to uncover insights into fuel efficiency, engine characteristics, and more, by applying various transformations and Spark SQL queries.

## Dataset

The dataset contains various car attributes including MPG (miles per gallon), cylinders, displacement, horsepower, weight, acceleration, model year, and origin. It is structured in a semicolon-separated values (SSV) format and includes historical data for car models.

## Features

- **Data Loading:** Load data into a Spark DataFrame with the appropriate schema.
- **Data Description**: Calculate the dataset statistics, including mean, median, and standard deviation.
- **Data Transformation:** Apply data transformation to clean and prepare the data for analysis.
- **Spark SQL Query:** Use Spark SQL to perform structured queries on the data.
- **Data Summary Report:** Generate a summary report in markdown that highlights the above data manipulation.


## Preparation:

To set up your environment to run this PySpark script, follow these steps:

1. Install the packages:
   ```bash
   make install
   ```

2. Running the Script
   ```bash
   python main.py
   ```
3. Linting
   ```bash
   make lint
   ```
4. Testing
   ```bash
   make test
   ```
5. Formating
   ```bash
   make format```

## Output

The script outputs a markdown report summarizing the insights from the data. This report includes the results of Spark SQL queries and data transformation steps, as well as any additional findings from the analysis.

To view the report, open the `analysis_report.md` in a markdown viewer or a code editor with markdown preview.
