"""
DS-505 Practical: PySpark Session and DataFrame Schema Inspection
Simple student-friendly program based on the uploaded workbook.
"""

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# Step 1: Initialize PySpark SparkSession in local cluster mode
spark = SparkSession.builder \
    .appName("DS505_Unit2_Practical5") \
    .master("local[*]") \
    .getOrCreate()

print("--- SPARK SESSION DETAILS ---")
print(f"Spark Application Name : {spark.sparkContext.appName}")
print(f"Spark Version          : {spark.version}")
print(f"Spark Master Mode      : {spark.sparkContext.master}")

# Step 2: Define structured employee data and schema
data = [
    ("E101", "Aarav Sharma", "Engineering", 75000.0, "Surat"),
    ("E102", "Diya Patel", "Analytics", 68000.0, "Ahmedabad"),
    ("E103", "Rohan Mehta", "Engineering", 82000.0, "Surat"),
    ("E104", "Sneha Joshi", "Marketing", 54000.0, "Vadodara"),
    ("E105", "Kabir Shah", "Analytics", 71000.0, "Surat")
]

schema = StructType([
    StructField("Emp_ID", StringType(), True),
    StructField("Name", StringType(), True),
    StructField("Department", StringType(), True),
    StructField("Salary", DoubleType(), True),
    StructField("City", StringType(), True)
])

# Step 3: Create DataFrame and inspect structure
df = spark.createDataFrame(data, schema=schema)

print("\n--- PYSPARK DATAFRAME SCHEMA HIERARCHY ---")
df.printSchema()

print("\n--- PYSPARK DATAFRAME RECORDS (.show) ---")
df.show()
