import os

os.environ["TMP"] = "C:\\Temp"
os.environ["TEMP"] = "C:\\Temp"

file_path = "dataset.csv"

# METADATA
size_bytes = os.path.getsize(file_path)
size_mb = size_bytes / (1024 * 1024)

print("=== METADATA ===")
print(f"File: {file_path}")
print(f"Size: {size_mb:.2f} MB")

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, to_date, year

spark = SparkSession.builder \
    .appName("BigDataProject") \
    .getOrCreate()


df = spark.read.csv("dataset.csv", header=True, inferSchema=True)

print("=== FIRST ROWS ===")
df.show(5)

print("=== SCHEMA ===")
df.printSchema()

print("=== ROW COUNT ===")
print(df.count())

print("=== SUMMARY ===")
df.describe().show()

print("=== GROUP BY COUNTRY (SUM VALUE) ===")
country_stats = df.groupBy("Country") \
    .agg(_sum("Value").alias("Total_Energy")) \
    .orderBy(col("Total_Energy").desc())

country_stats.show(10)

print("=== GROUP BY ENERGY PRODUCT ===")
product_stats = df.groupBy("Energy Product Name") \
    .agg(_sum("Value").alias("Total_Value")) \
    .orderBy(col("Total_Value").desc())

product_stats.show(10)


# =========================
# ADVANCED ANALYSIS 
# =========================

# -------------------------------------------------
# 5) FILTER ANALYSIS (USA ONLY)
# -------------------------------------------------
print("=== FILTER: UNITED STATES DATA ===")

usa_df = df.filter(col("Country") == "United States")
usa_stats = usa_df.groupBy("Energy Product Name") \
    .agg(_sum("Value").alias("USA_Total")) \
    .orderBy(col("USA_Total").desc())

usa_stats.show(10)


# -------------------------------------------------
# 6) SPARK SQL ANALYSIS
# -------------------------------------------------
print("=== SPARK SQL ANALYSIS ===")

df.createOrReplaceTempView("energy")

sql_result = spark.sql("""
SELECT Country, SUM(Value) AS Total_Energy
FROM energy
GROUP BY Country
ORDER BY Total_Energy DESC
""")

sql_result.show(10)



# =========================
# VISUALIZATIONS
# =========================
import matplotlib.pyplot as plt

# -------------------------------------------------
# 1) TOP 5 COUNTRIES (BAR)
# -------------------------------------------------
top_countries = country_stats.limit(5).toPandas()

plt.figure(figsize=(8,5))
plt.bar(top_countries["Country"], top_countries["Total_Energy"])
plt.title("Top 5 Countries by Total Energy")
plt.xlabel("Country")
plt.ylabel("Total Energy")
plt.xticks(rotation=20)
plt.show()


# -------------------------------------------------
# 2) TOP 5 ENERGY PRODUCTS (BAR)
# -------------------------------------------------
top_products = product_stats.limit(5).toPandas()

plt.figure(figsize=(10,5))
plt.bar(top_products["Energy Product Name"], top_products["Total_Value"])
plt.title("Top 5 Energy Products")
plt.xlabel("Energy Product")
plt.ylabel("Total Value")
plt.xticks(rotation=30)
plt.show()


# -------------------------------------------------
# 3) YEARLY ENERGY TREND (LINE CHART)
# -------------------------------------------------
df_year = df.withColumn("YearOnly", year(to_date(col("Year"), "M/d/yyyy")))

year_stats = df_year.groupBy("YearOnly") \
    .agg(_sum("Value").alias("Total_Energy")) \
    .orderBy("YearOnly")

year_pd = year_stats.toPandas()

plt.figure(figsize=(10,5))
plt.plot(year_pd["YearOnly"], year_pd["Total_Energy"])
plt.title("Energy Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Total Energy")
plt.grid(True)
plt.show()


# -------------------------------------------------
# 4) PIE CHART - TOP 5 COUNTRIES SHARE
# -------------------------------------------------
plt.figure(figsize=(7,7))
plt.pie(
    top_countries["Total_Energy"],
    labels=top_countries["Country"],
    autopct="%1.1f%%"
)
plt.title("Energy Share (Top 5 Countries)")
plt.show()


spark.stop()