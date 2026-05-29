# Faza 3 - Big Data

Ky repository permban materialet e fazes se trete te projektit Big Data: analizen me Spark, te dhenat per NoSQL, analizen e rrjetit dhe dokumentimin final.

## Struktura e projektit

```text
.
├── Documentation/
│   ├── Phase3_Report.pdf
│   └── Phase3_Presentation.pptx
├── Network/
│   ├── Rezultatet_dataseti/
│   ├── Vizualizimi/
│   └── Workspace/
├── NoSQL Data/
│   ├── FuelPrice.csv
│   └── WorldBank_dataset.csv
├── Spark/
│   └── Phase3Spark.ipynb
├── queries.js
└── README.md
```

## Parakushtet

- Python 3.10+.
- Jupyter Notebook ose JupyterLab.
- Apache Spark / PySpark per ekzekutimin e notebook-ut ne folderin `Spark`.
- MongoDB ose MongoDB Compass per ekzekutimin e query-ve ne `queries.js`.
- Gephi, nese deshironi te hapni workspace-in dhe vizualizimet e rrjetit.

## Konfigurimi

1. Klononi repository-n:

   ```bash
   git clone https://github.com/ElsaKrasniqii/Faza3_Big_Data.git
   cd Faza3_Big_Data
   ```

2. Krijoni dhe aktivizoni nje ambient virtual per Python:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Instaloni paketat e nevojshme per notebook-et:

   ```bash
   pip install notebook jupyterlab pyspark pandas matplotlib seaborn
   ```

## Ekzekutimi i analizes Spark

1. Hapni Jupyter:

   ```bash
   jupyter lab
   ```

2. Hapni notebook-un:

   ```text
   Spark/Phase3Spark.ipynb
   ```

3. Ekzekutoni qelizat me radhe. Sigurohuni qe path-et e dataset-eve ne notebook te perputhen me lokacionin e skedareve ne projekt.

## Ekzekutimi i query-ve NoSQL

1. Hapni MongoDB ose MongoDB Compass.
2. Krijoni databazen per projektin.
3. Importoni dataset-et:

   ```text
   NoSQL Data/FuelPrice.csv
   NoSQL Data/WorldBank_dataset.csv
   ```

4. Ekzekutoni query-te nga:

   ```text
   queries.js
   ```

## Analiza e rrjetit

- Dataset-et dhe rezultatet gjenden ne `Network/Rezultatet_dataseti/`.
- Vizualizimet gjenden ne `Network/Vizualizimi/`.
- Workspace-i per hapje ne Gephi gjendet ne `Network/Workspace/NetworkAnalysis.xml`.

## Dokumentimi

Raporti dhe prezantimi final gjenden ne:

```text
Documentation/Phase3_Report.pdf
Documentation/Phase3_Presentation.pptx
```
