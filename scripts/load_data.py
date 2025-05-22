import pandas as pd
from sqlalchemy import create_engine
import urllib.parse
import logging
import os

# Set up logging
os.makedirs('logs', exist_ok=True)
logging.basicConfig(filename='logs/load_errors.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection
try:
    password = urllib.parse.quote_plus("YourPasswordHere")  # Replace with your actual password
    engine = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/retail_dw')
    logging.info("Database connection established")
except Exception as e:
    logging.error(f"Database connection failed: {str(e)}")
    raise

# Function to validate CSV
def validate_csv(file_path, expected_columns):
    if not os.path.exists(file_path):
        logging.error(f"CSV file not found: {file_path}")
        raise FileNotFoundError(f"CSV file not found: {file_path}")
    df = pd.read_csv(file_path)
    if not all(col in df.columns for col in expected_columns):
        logging.error(f"Missing columns in {file_path}. Expected: {expected_columns}, Found: {list(df.columns)}")
        raise ValueError(f"Missing columns in {file_path}")
    return df

# Clear existing data
try:
    with engine.connect() as conn:
        conn.execute("TRUNCATE TABLE fact_sales")
        conn.execute("TRUNCATE TABLE dim_date")
        conn.execute("TRUNCATE TABLE dim_product")
        conn.execute("TRUNCATE TABLE dim_store")
    logging.info("Tables truncated")
except Exception as e:
    logging.error(f"Error truncating tables: {str(e)}")
    raise

# Load dim_date
try:
    df_date = validate_csv('data/dim_date.csv', ['date_id', 'full_date', 'day', 'month', 'quarter', 'year'])
    df_date['full_date'] = pd.to_datetime(df_date['full_date'], errors='coerce')
    df_date = df_date.drop_duplicates()
    df_date.to_sql('dim_date', engine, if_exists='append', index=False)
    logging.info("Successfully loaded dim_date")
    print("Successfully loaded dim_date")
except Exception as e:
    logging.error(f"Error loading dim_date: {str(e)}")
    print(f"Error loading dim_date: {str(e)}")

# Load dim_product
try:
    df_product = validate_csv('data/dim_product.csv', ['product_id', 'name', 'category', 'brand'])
    df_product = df_product.drop_duplicates()
    df_product.to_sql('dim_product', engine, if_exists='append', index=False)
    logging.info("Successfully loaded dim_product")
    print("Successfully loaded dim_product")
except Exception as e:
    logging.error(f"Error loading dim_product: {str(e)}")
    print(f"Error loading dim_product: {str(e)}")

# Load dim_store
try:
    df_store = validate_csv('data/dim_store.csv', ['store_id', 'store_name', 'city', 'region'])
    df_store = df_store.drop_duplicates()
    df_store.to_sql('dim_store', engine, if_exists='append', index=False)
    logging.info("Successfully loaded dim_store")
    print("Successfully loaded dim_store")
except Exception as e:
    logging.error(f"Error loading dim_store: {str(e)}")
    print(f"Error loading dim_store: {str(e)}")

# Load fact_sales
try:
    df_sales = validate_csv('data/fact_sales.csv', ['sale_id', 'date_id', 'product_id', 'store_id', 'quantity_sold', 'revenue'])
    df_sales = df_sales.drop_duplicates()
    df_sales.to_sql('fact_sales', engine, if_exists='append', index=False)
    logging.info("Successfully loaded fact_sales")
    print("Successfully loaded fact_sales")
except Exception as e:
    logging.error(f"Error loading fact_sales: {str(e)}")
    print(f"Error loading fact_sales: {str(e)}")