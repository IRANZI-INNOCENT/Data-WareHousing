# Retail Data Warehouse

## Project Overview

This project, completed for **DSA 2040A 2025 Lab 1**, implements a **star schema-based data warehouse** for analyzing retail chain sales. As junior data engineers, the objective is to design and implement a data warehouse using **MySQL**, load data from **CSV files**, perform **analytical SQL queries**, and derive **business insights**.

The project follows the lab manual *Building a Mini Data Warehouse for a Retail Chain*, encompassing:

- Star schema design  
- Data loading  
- Query execution  
- Business reflection  
- GitHub documentation

The data warehouse enables decision-making in areas such as inventory management, marketing, and seasonal planning.

---

## Star Schema Design

A star schema was used, centered around the `fact_sales` table, surrounded by dimension tables. A visualization is available at `docs/schema_diagram.png`.

### Fact Table: `fact_sales`

| Column        | Description                              |
|---------------|------------------------------------------|
| sale_id       | INT, PRIMARY KEY – Unique sale ID        |
| date_id       | INT, FK → `dim_date(date_id)`            |
| product_id    | INT, FK → `dim_product(product_id)`      |
| store_id      | INT, FK → `dim_store(store_id)`          |
| quantity_sold | INT – Units sold                         |
| revenue       | DECIMAL(10,2) – Sale revenue             |

### Dimension Tables

#### `dim_date`

| Column    | Description              |
|-----------|--------------------------|
| date_id   | INT, PRIMARY KEY         |
| full_date | DATE (e.g., 2023-01-01)  |
| day       | INT – Day of the month   |
| month     | INT – Month number       |
| quarter   | INT – Quarter number     |
| year      | INT – Year               |

#### `dim_product`

| Column   | Description                    |
|----------|--------------------------------|
| product_id | INT, PRIMARY KEY             |
| name     | VARCHAR(100) – Product name    |
| category | VARCHAR(50) – Product category |
| brand    | VARCHAR(50) – Product brand    |

#### `dim_store`

| Column     | Description                |
|------------|----------------------------|
| store_id   | INT, PRIMARY KEY           |
| store_name | VARCHAR(100) – Store name  |
| city       | VARCHAR(50) – Store city   |
| region     | VARCHAR(50) – Store region |

---

## Prerequisites

Ensure the following tools are installed:

- **MySQL 8.0+**
  - [Download](https://dev.mysql.com/)
  - Default user: `root`
  - Password: `Yourpassword`

- **MySQL Workbench 8.0+** – For visual verification  
- **Visual Studio Code** – Code editing and running SQL

  - Extensions:
    - `SQLTools` – For executing SQL queries
    - `Jupyter` – To run `generate_diagrams.ipynb`

- **Python 3.10+**
  - Required package: `matplotlib`  
  - Install: `pip install matplotlib`

---

## Setup Instructions

### 1. Configure MySQL
Create a new schema/database for the warehouse using MySQL Workbench.

### 2. Set Up VS Code and SQLTools
Connect to MySQL using the SQLTools extension with your connection credentials.

### 3. Create Tables
Run `sql/schema.sql` to create the fact and dimension tables.

### 4. Load Data
Execute `sql/load_data.sql` to load CSV files using `LOAD DATA LOCAL INFILE`.

### 5. Run Analytical Queries
Run `sql/queries.sql` to derive insights:

- **Query 1**: Total Revenue by Product Category  
- **Query 2**: Monthly Sales Trends  
- **Query 3**: Revenue by Region  
- **Query 4**: Top Products by Quantity Sold  

**Business Use Cases:**

- Query 1: Prioritize high-revenue categories (e.g., Electronics)
- Query 2: Support seasonal marketing campaigns
- Query 3: Target high-performing regions
- Query 4: Optimize inventory for top-selling items

---

## Reflection

Reflection questions and answers are in `docs/reflection.md`:

- Why use a star schema instead of a normalized schema?
- What are the benefits of separating facts and dimensions?
- What business decisions does this warehouse support?

---

## Project Structure

retail-data-warehouse/
├── data/
│ ├── dim_date.csv # Date dimension data
│ ├── dim_product.csv # Product dimension data
│ ├── dim_store.csv # Store dimension data
│ └── fact_sales.csv # Sales fact data
├── sql/
│ ├── schema.sql # Table creation script
│ ├── load_data.sql # Data loading script
│ └── queries.sql # Analytical queries
├── docs/
│ ├── reflection.md # Reflection answers
│ ├── schema_diagram.png # Schema diagram
│ └── workflow_diagram.png # Workflow diagram
├── generate_diagrams.ipynb # Python notebook for visualizations
└── README.md # This file


## Conclusion

This project demonstrates how to build a functional data warehouse using a star schema in MySQL. By loading retail data via `LOAD DATA LOCAL INFILE` and analyzing it with SQL queries, it supports real-world business decisions. The reflection connects the technical design to practical use cases in retail management.
