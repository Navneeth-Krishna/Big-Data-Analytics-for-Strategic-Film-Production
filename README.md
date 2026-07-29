# Big Data Analytics for Strategic Film Production — Summary

Collects, cleans, and loads film industry data from public sources into analytics-ready formats. Includes web scrapers for Rotten Tomatoes, TMDB, and TheNumbers, plus Python scripts for HDFS upload and MySQL ingestion.

## What this project does

- Scrapes movie metadata and ratings from:
  - Rotten Tomatoes
  - TMDB (The Movie Database)
  - TheNumbers box office pages
- Cleans and prepares scraped data using Python and Pandas
- Uploads CSV datasets to HDFS for distributed storage
- Loads HDFS CSV data into MySQL for analysis
- Provides exploratory notebooks for data cleaning and transformation

## Why this project is useful

- Supports strategic film production research by combining ratings, metadata, budget, and box office information
- Demonstrates an end-to-end data engineering workflow from scraping to data ingestion
- Includes reusable Scrapy spiders and data pipeline scripts
- Helps with learning practical Python, web scraping, HDFS, and SQL integration

## Repository structure

- `Scrapping/rottentomato/` — Scrapy project for Rotten Tomatoes scraping
- `Scrapping/tmdbdata/` — Scrapy project for TMDB scraping
- `Scrapping/TheNumbers/` — Notebook and scraper code for TheNumbers box office data
- `Python Codes and cleaning code/` — HDFS upload and MySQL ingestion scripts
- `SQL Queries/` — SQL queries related to the project
- `Data Engineering 1 - Group 1 Domain Movies (1).pdf` — project report

## Getting started

### Prerequisites

- Python 3.8+ (recommended)
- Git
- A Python virtual environment
- Optional infrastructure:
  - HDFS cluster accessible from the loader script
  - MySQL server for data ingestion

### Recommended Python packages

Install packages as needed for each component:

```bash
pip install scrapy pandas requests beautifulsoup4 selenium hdfs sqlalchemy mysql-connector-python pyhdfs
```

> Note: This repository does not include a top-level `requirements.txt`, so install dependencies per component.

## Usage examples

### 1. Run Rotten Tomatoes scraping

```bash
cd Scrapping/rottentomato
scrapy crawl tomato -O rotten_tomato.csv
```

If you want the alternate Rotten Tomatoes spider:

```bash
cd Scrapping/rottentomato
scrapy crawl tomatoo -O rotten_tomato_alt.csv
```

### 2. Run TMDB scraping

```bash
cd Scrapping/tmdbdata
scrapy crawl tmdb -O tmdb_1.csv
```

Alternate TMDB spider:

```bash
cd Scrapping/tmdbdata
scrapy crawl tmdb1 -O tmdb_1_alt.csv
```

### 3. Use TheNumbers scraper

Open the notebook at `Scrapping/TheNumbers/thenumbers.ipynb` and run the cells to scrape box office and budget data into CSV.

### 4. Upload CSV files to HDFS

Update file paths in `Python Codes and cleaning code/files_to_hadoop.py` and run:

```bash
python "Python Codes and cleaning code/files_to_hadoop.py"
```

### 5. Load data from HDFS into MySQL

Update connection settings in `Python Codes and cleaning code/sql.py`, then run:

```bash
python "Python Codes and cleaning code/sql.py"
```

## Notebooks and analysis

- `Python Codes and cleaning code/datacleaning.ipynb` — data cleaning and transformation examples
- `Scrapping/tmdbdata/tmdb_images.ipynb` — TMDB scraping and image handling exploration
- `Scrapping/TheNumbers/thenumbers.ipynb` — TheNumbers web scraping workflow

## Project report

The repository includes a project report at:

- `Data Engineering 1 - Group 1 Domain Movies (1).pdf`

Use that report for background, methodology, and project objectives.

## Where to get help

- Review the code in `Scrapping/` and `Python Codes and cleaning code/`
- Open an issue in the repository if you need guidance or encounter bugs
- Ask the project maintainers or group members directly if available

