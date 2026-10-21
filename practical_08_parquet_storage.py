"""
DS-505 Practical: Parquet Storage using PySpark
Simple student-friendly program based on the uploaded workbook.
"""

from pyspark.sql import SparkSession
import os

spark = SparkSession.builder.appName("DS505_Parquet").master("local[*]").getOrCreate()

# Step 1: Create sample IoT sensor telemetry DataFrame
data = [
    ("Sensor_01", "Temperature", 24.5, "2026-10-10 10:00:00"),
    ("Sensor_02", "Humidity", 65.2, "2026-10-10 10:00:00"),
    ("Sensor_01", "Temperature", 25.1, "2026-10-10 10:05:00"),
    ("Sensor_03", "Pressure", 1013.25, "2026-10-10 10:05:00"),
    ("Sensor_02", "Humidity", 64.8, "2026-10-10 10:10:00")
]
columns = ["Sensor_ID", "Metric_Type", "Metric_Value", "Timestamp"]
df = spark.createDataFrame(data, columns)

print("--- ORIGINAL SENSOR DATAFRAME ---")
df.show()

# Step 2: Write to Apache Parquet columnar file format
parquet_path = "sensor_telemetry.parquet"
df.write.mode("overwrite").parquet(parquet_path)
print(f"Successfully serialized DataFrame to Parquet storage at: '{parquet_path}'")

# Step 3: Read back from Parquet format
df_parquet = spark.read.parquet(parquet_path)

print("\n--- RELOADED FROM PARQUET FORMAT ---")
df_parquet.printSchema()
df_parquet.show()

print(f"Verified Record Count: {df_parquet.count()} rows.")
