# Big Data Analytics for Strategic Film Production

A repository for film industry data acquisition, preparation, and analytics using web scraping, Hadoop/HDFS upload, and SQL data loading.

## What this project does

This project collects movie data from online sources, cleans and stores it, then makes it available for analysis in a relational database.

Key capabilities:
- Scrapes film metadata from Rotten Tomatoes and TMDB using Scrapy spiders
- Saves scraped datasets as CSV files for downstream processing
- Uploads CSV files into HDFS for distributed storage
- Loads cleaned datasets from HDFS into MySQL tables for analytics and reporting

## Why this project is useful

It provides a reproducible pipeline for building a film production analytics dataset from public movie sources. Use it to:
- gather film metadata and ratings
- explore genre, director, rating, and data-source trends
- build a centralized analytics dataset for strategic production decisions

## Project structure

- `Python Codes and cleaning code/`
  - `datacleaning.ipynb` — notebook for cleaning and exploring data
  - `files_to_hadoop.py` — uploads local CSV files to HDFS
  - `sql.py` — reads CSV data from HDFS and loads it into MySQL
- `Scrapping/rottentomato/` — Scrapy project that extracts Rotten Tomatoes movie details
- `Scrapping/tmdbdata/` — Scrapy project that extracts TMDB top-rated movie details
- `SQL Queries/SQL Queries.txt` — sample SQL queries for exploring loaded movie tables

## Getting started

### Prerequisites

- Python 3.8+ (or compatible Python 3 release)
- `pip` for Python package installation
- Scrapy
- HDFS access and compatible client libraries
- MySQL server with credentials for loading data

### Install dependencies

```bash
pip install scrapy pandas sqlalchemy hdfs mysql-connector-python pyhdfs
```

> The repository does not include a dedicated dependency file. Adjust packages to your environment and virtual environment as needed.

### Run the Rotten Tomatoes scraper

From `Scrapping/rottentomato/`:

```bash
cd "Scrapping/rottentomato"
scrapy crawl tomato -o rotten_tomato.csv
```

### Run the TMDB scraper

From `Scrapping/tmdbdata/`:

```bash
cd "Scrapping/tmdbdata"
scrapy crawl tmdb1 -o tmdb_1.csv
```

### Upload CSV files to HDFS

Update paths in `Python Codes and cleaning code/files_to_hadoop.py` then run:

```bash
python "Python Codes and cleaning code/files_to_hadoop.py"
```

### Load data from HDFS into MySQL

Update connection settings in `Python Codes and cleaning code/sql.py` and run:

```bash
python "Python Codes and cleaning code/sql.py"
```

## Usage examples

Sample SQL queries are provided in `SQL Queries/SQL Queries.txt` to analyze movie counts, genres, ratings, and director-level summaries.

## Where to get help

- Review the Scrapy documentation for spider usage
- Check HDFS and MySQL connection requirements in your cluster environment
- Use repository file comments and sample SQL queries as a starting point

