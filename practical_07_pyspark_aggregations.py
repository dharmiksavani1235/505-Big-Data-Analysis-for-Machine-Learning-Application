"""
DS-505 Practical: PySpark Grouped Aggregations
Simple student-friendly program based on the uploaded workbook.
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, max, sum, round

spark = SparkSession.builder.appName("DS505_Aggregations").master("local[*]").getOrCreate()

# Create department dataset
data = [
    ("Amit", "Sales", 45000),
    ("Pooja", "Engineering", 85000),
    ("Rahul", "Sales", 52000),
    ("Sneha", "Marketing", 48000),
    ("Vikram", "Engineering", 92000),
    ("Ananya", "Marketing", 54000),
    ("Karan", "Sales", 49000),
    ("Riya", "Engineering", 88000)
]
df = spark.createDataFrame(data, ["Employee", "Department", "Salary"])

print("--- INPUT DATASET ---")
df.show()

# GroupBy Aggregation
print("--- DEPARTMENT-WISE AGGREGATION METRICS ---")
dept_summary = df.groupBy("Department").agg(
    count("*").alias("Headcount"),
    round(avg("Salary"), 2).alias("Average_Salary"),
    max("Salary").alias("Max_Salary"),
    sum("Salary").alias("Total_Payroll")
).orderBy(col("Average_Salary").desc())

dept_summary.show()

# Action execution
print(f"Total Unique Departments: {dept_summary.count()}")
print(f"Total Records in Dataset : {df.count()}")
