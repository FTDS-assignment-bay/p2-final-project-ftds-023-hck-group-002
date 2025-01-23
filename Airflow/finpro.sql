CREATE TABLE retail_store (
    id SERIAL PRIMARY KEY,
    Store_id VARCHAR,
   	Date DATE,
    Product_id VARCHAR,
    Category VARCHAR,
	Region VARCHAR,
	Inventory_Level INT,
	Units_Sold INT,
	Units_Ordered INT,
	Demand_Forecast FLOAT,
	Price FLOAT,
    Discount INT,
    Weather_Condition VARCHAR,
    Promotion INT,
    Competitor_Pricing FLOAT,
    Seasonality VARCHAR
);