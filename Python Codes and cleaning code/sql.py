import pyhdfs
import pandas as pd
from sqlalchemy import create_engine
from hdfs import InsecureClient
from sqlalchemy import text

# Connection details for HDFS and MySQL
hdfs_address = 'master-node'
hdfs_api_port = 9870
db_host = '192.168.56.101'
db_user = 'root'
db_password = '123123'
db_name = 'projectschemasql'
db_port = 3306

# Initialize HDFS client
hdfs = InsecureClient(f'http://100.79.105.86:{hdfs_api_port}', user='hadoop')

# HDFS directory path and file listing
hdfs_directory = '/home/hadoop/data/nameNode/data/'
hdfs_files = hdfs.list(hdfs_directory)
print("Files in the HDFS directory:", hdfs_files)

# Function to load CSV files from HDFS
def load_csv(hdfs, directory, file_name):
    with hdfs.read(f'{directory}/{file_name}', encoding='utf-8') as f:
        return pd.read_csv(f)

# Reading CSV files into DataFrames
data_source = load_csv(hdfs, hdfs_directory, 'data_source.csv')
ratings = load_csv(hdfs, hdfs_directory, 'rating.csv')
genres = load_csv(hdfs, hdfs_directory, 'genre1.csv')
main = load_csv(hdfs, hdfs_directory, 'main_file.csv')
directors = load_csv(hdfs, hdfs_directory, 'modified_director.csv')

# Strip whitespace from genre columns
genres.columns = genres.columns.str.strip()

# Create SQLAlchemy engine for MySQL
db_engine = create_engine(f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}')

# Load DataFrames into MySQL tables
data_source.to_sql('data_source', con=db_engine, if_exists='replace', index=False)
ratings.to_sql('rating', con=db_engine, if_exists='replace', index=False)
genres.to_sql('genre1', con=db_engine, if_exists='replace', index=False)
main.to_sql('main_file', con=db_engine, if_exists='replace', index=False)
directors.to_sql('modified_director', con=db_engine, if_exists='replace', index=False)

print("Data successfully loaded into MySQL")


