# Retail-Sales-Analysis
Retail Sales Data Analysis Using Hadoop Pig and Hive is a big data project that extracts insights from e-commerce transactions using the UCI Online Retail dataset. It leverages Apache Hadoop, Pig, and Hive to process, analyze, and summarize sales data from a UK-based online store.
📁 Dataset
- **Source:** [UCI Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail)
- **Description:** Contains transactions from a UK-based online retailer between 2010 and 2011.

## Tools & Technologies
- Hadoop (HDFS)
- Apache Pig
- Apache Hive
- Python (Data Cleaning)
- Linux Shell

## Objective
- Clean and format retail data
- Analyze total sales per country
- Identify top-selling products
- Evaluate monthly trends and customer spending

## Project Structure
See folder structure in this repo.

## Setup Instructions

### 1. Prerequisites
- Hadoop with HDFS configured
- Pig installed
- Hive installed
- Python 3

### 2. Upload Data to HDFS
```bash
bash hdfs_upload.sh
```

### 3. Run Pig Scripts
```bash
pig pig/total_sales_per_country.pig
pig pig/top_10_products.pig
```

### 4. Run Hive Queries
```bash
hive -f hive/create_table.hql
hive -f hive/country_sales.hql
```

---

## Sample Output
- **Pig**: Total sales per country
- **Hive**: Top 10 customers based on spending
