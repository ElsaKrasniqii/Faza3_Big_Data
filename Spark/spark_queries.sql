-- Query 1: Average Indicator Values for Kosovo

SELECT
    CountryName,
    AVG(CAST(IndicatorValue AS DOUBLE)) AS avg_value
FROM worldbank_xml
WHERE CountryName = 'Kosovo'
GROUP BY CountryName;

-- Query 2: Ranking Countries by GDP per Capita

SELECT
    CountryName,
    Year,
    CAST(IndicatorValue AS DOUBLE) AS gdp_per_capita
FROM worldbank_xml
WHERE IndicatorName = 'GDP per capita (current US$)'
  AND IndicatorValue IS NOT NULL
ORDER BY gdp_per_capita DESC
LIMIT 10;

-- Query 3: Total Energy by Country

SELECT Country,
       SUM(Value) AS Total_Energy
FROM energy
GROUP BY Country
ORDER BY Total_Energy DESC
LIMIT 10;
