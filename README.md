Retail Data Warehouse

Project Overview

This project, completed for DSA 2040A 2025 Lab 1, builds a star schema-based data warehouse to analyze sales data for a retail chain. As junior data engineers, the goal is to design and implement a data warehouse in MySQL, load data from CSV files, execute analytical queries, and derive business insights. The project follows the Lab Manual: Building a Mini Data Warehouse for a Retail Chain, covering star schema design, data loading, querying, reflection, and GitHub submission.
The data warehouse enables the retail company to analyze sales across products, stores, and time periods, supporting decisions like inventory management, marketing allocation, and seasonal planning. Key components include:

Star Schema: A fact table (fact_sales) and dimension tables (dim_date, dim_product, dim_store).
Data Loading: CSVs loaded using MySQL’s LOAD DATA LOCAL INFILE via VS Code’s SQLTools.
Analytical Queries: Four SQL queries to compute revenue by category, monthly trends, revenue by region, and top products.
Reflection: Discussion on star schema benefits, fact-dimension separation, and business applications.
Diagrams: Optional visualizations of the schema and workflow, generated with Python and Matplotlib.
GitHub: Public repository with all files and documentation.

This README provides comprehensive instructions to set up, run, and understand the project, tailored for replication on Windows 11 with MySQL 8.0+, VS Code, and Python.

Star Schema
The data warehouse uses a star schema, optimized for analytical queries with a central fact table and surrounding dimension tables, as shown in docs/schema_diagram.png.

Fact Table
fact_sales:
sale_id (INT, PRIMARY KEY): Unique sale identifier.
date_id (INT, FOREIGN KEY): References dim_date(date_id).
product_id (INT, FOREIGN KEY): References dim_product(product_id).
store_id (INT, FOREIGN KEY): References dim_store(store_id).
quantity_sold (INT): Number of units sold.
revenue (DECIMAL(10,2)): Sale revenue.


Dimension Tables

dim_date:
date_id (INT, PRIMARY KEY): Unique date identifier.
full_date (DATE): Date of sale (e.g., 2023-01-01).
day (INT): Day of month.
month (INT): Month number.
quarter (INT): Quarter number.
year (INT): Year.


dim_product:
product_id (INT, PRIMARY KEY): Unique product identifier.
name (VARCHAR(100)): Product name (e.g., Laptop).
category (VARCHAR(50)): Product category (e.g., Electronics).
brand (VARCHAR(50)): Product brand.


dim_store:
store_id (INT, PRIMARY KEY): Unique store identifier.
store_name (VARCHAR(100)): Store name (e.g., Downtown Outlet).
city (VARCHAR(50)): Store city.
region (VARCHAR(50)): Store region (e.g., East).


Schema Diagram
The star schema is visualized in docs/schema_diagram.png, showing fact_sales connected to dim_date, dim_product, and dim_store via foreign keys (date_id, product_id, store_id).
Prerequisites
To replicate this project, ensure the following tools are installed:

MySQL 8.0+: Database management system (download from dev.mysql.com).
Username: root
Password: Yourpassword (as per project setup).


MySQL Workbench 8.0+: SQL client for verification (download from dev.mysql.com).
Visual Studio Code (VS Code): Code editor (download from code.visualstudio.com).

Extensions:
SQLTools: For running SQL queries (install via Extensions: Ctrl+Shift+X, search “SQLTools”).
Jupyter: For running generate_diagrams.ipynb (search “Jupyter” by Microsoft).

Python 3.10+: For generating diagrams (download from python.org).
Required package: matplotlib (install via pip install matplotlib).


Setup Instructions
Follow these steps to set up the data warehouse on Windows 11.
1. Configure MySQL

2. Set Up VS Code and SQLTools


3. Create  Database and Tables in MySQL workbench


4. Load Data

5. Run Analytical Queries
The lab requires four analytical queries to gain business insights, stored in sql/queries.sql:
-- 1. Total Revenue by Product Category
-- 2. Monthly Sales Trends
-- 3. Revenue by Region
-- 4. Top Products by Quantity Sold

Purpose:
Query 1: Identifies high-revenue product categories (e.g., Electronics) for inventory prioritization.
Query 2: Tracks sales trends over time for seasonal planning.
Query 3: Highlights top-performing regions (e.g., East) for marketing focus.
Query 4: Lists top-selling products (e.g., Jeans) for stock optimization.


7. Reflection
The reflection (docs/reflection.md) answers three questions:

Why use a star schema instead of a normalized schema?


What are the benefits of separating facts from dimensions?


What types of business decisions could this warehouse support?


See docs/reflection.md for detailed answers with examples.


Project Structure

retail-data-warehouse\
├── data/
│   ├── dim_date.csv        # Date dimension data
│   ├── dim_product.csv     # Product dimension data
│   ├── dim_store.csv       # Store dimension data
│   ├── fact_sales.csv      # Sales fact data
├── sql/
│   ├── schema.sql          # Table creation script
│   ├── load_data.sql       # Data loading script
│   ├── queries.sql         # Analytical queries
├── docs/
│   ├── reflection.md       # Reflection answers
│   ├── schema_diagram.png  # Star schema visualization
│   ├── workflow_diagram.png # Data loading workflow
├── generate_diagrams.ipynb # Python notebook for diagrams
├── README.md               # This file

Conclusion
This project demonstrates a functional data warehouse using a star schema, loaded with retail sales data, and queried to support business decisions. The use of LOAD DATA LOCAL INFILE in SQLTools resolved Workbench import issues, ensuring efficient data loading. The queries provide actionable insights, and the reflection ties concepts to real-world applications.
