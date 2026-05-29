world_bank_dataset = spark.table("world_bank_dataset")
fuel_price = spark.table("fuel_price")
worlbank_dwh = spark.table("worlbank_dwh")
world_oil_data = spark.table("world_oil_data")

world_bank_dataset.createOrReplaceTempView("worldbank")
fuel_price.createOrReplaceTempView("fuelprices")
worlbank_dwh.createOrReplaceTempView("worldbank_xml")
world_oil_data.createOrReplaceTempView("energy")

# Query 1: Average Indicator Values for Kosovo
spark.sql("""
SELECT
    CountryName,
    AVG(CAST(IndicatorValue AS DOUBLE)) AS avg_value
FROM worldbank_xml
WHERE CountryName = 'Kosovo'
GROUP BY CountryName
""").show()

# Query 2: Ranking Countries by GDP per Capita
spark.sql("""
SELECT
    CountryName,
    Year,
    CAST(IndicatorValue AS DOUBLE) AS gdp_per_capita
FROM worldbank_xml
WHERE IndicatorName = 'GDP per capita (current US$)'
  AND IndicatorValue IS NOT NULL
ORDER BY gdp_per_capita DESC
LIMIT 10
""").show()

# Query 3: Total Energy by Country
spark.sql("""
SELECT Country,
       SUM(Value) AS Total_Energy
FROM energy
GROUP BY Country
ORDER BY Total_Energy DESC
LIMIT 10
""").show()
