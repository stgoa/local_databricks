# -*- coding: utf-8 -*-
"""Database connection and session handle."""

from local_databricks import SETTINGS
from local_databricks.settings import __app_name__
from pyspark.sql import SparkSession

# pylint: disable=no-member


# Create SparkSession from builder
def create_local_spark_session(local= False):
    print("connecting to local sqlite")
    SPARK = SparkSession \
        .builder \
        .appName(__app_name__) \
        .master('local[*]') \
        .getOrCreate()
    return SPARK


if __name__ == "__main__":
    create_local_spark_session(local=True)
