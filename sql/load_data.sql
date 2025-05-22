USE retail_dw;

-- Clear existing data
TRUNCATE TABLE fact_sales;
TRUNCATE TABLE dim_date;
TRUNCATE TABLE dim_product;
TRUNCATE TABLE dim_store;

-- Load dim_date
LOAD DATA LOCAL INFILE 'Filepath/dim_date.csv'
INTO TABLE dim_date
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(date_id, full_date, day, month, quarter, year);

-- Load dim_product
LOAD DATA LOCAL INFILE "Filepath/dim_product.csv"
INTO TABLE dim_product
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(product_id, name, category, brand);

-- Load dim_store
LOAD DATA LOCAL INFILE 'Filepath/dim_store.csv'
INTO TABLE dim_store
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(store_id, store_name, city, region);

-- Load fact_sales
LOAD DATA LOCAL INFILE 'Filepath/fact_sales.csv'
INTO TABLE fact_sales
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(sale_id, date_id, product_id, store_id, quantity_sold, revenue);