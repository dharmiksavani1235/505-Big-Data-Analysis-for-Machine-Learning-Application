"""
DS-505 Practical: PySpark Selection, Filtering and Column Transformations
Simple student-friendly program based on the uploaded workbook.
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("DS505_Transformations").master("local[*]").getOrCreate()

# Create sample dataset
data = [
    (1, "Aarav", "IT", 65000, "Surat"),
    (2, "Diya", "HR", 45000, "Navsari"),
    (3, "Rohan", "IT", 72000, "Surat"),
    (4, "Pooja", "Finance", 58000, "Ahmedabad"),
    (5, "Kabir", "IT", 81000, "Surat"),
    (6, "Neha", "Finance", 62000, "Surat")
]
columns = ["ID", "Name", "Dept", "Salary", "City"]
df = spark.createDataFrame(data, columns)

print("--- ORIGINAL DATAFRAME ---")
df.show()

# 1. Column Selection
print("--- 1. SELECT NAME AND SALARY ---")
df.select("Name", "Salary").show()

# 2. Multi-condition Filtering
print("--- 2. FILTER (Dept == 'IT' AND Salary > 70000) ---")
df.filter((col("Dept") == "IT") & (col("Salary") > 70000)).show()

# 3. Add Computed Column (Bonus = 10% of Salary)
print("--- 3. ADD COMPUTED 'Bonus' COLUMN ---")
df_with_bonus = df.withColumn("Bonus", col("Salary") * 0.10)
df_with_bonus.show()

# 4. Rename Column
print("--- 4. RENAME 'Salary' TO 'Base_Salary' ---")
df_renamed = df_with_bonus.withColumnRenamed("Salary", "Base_Salary")
df_renamed.show()
