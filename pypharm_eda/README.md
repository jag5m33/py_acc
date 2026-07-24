Pharmaceutical Sales Dataset Analysis 

The dataset contains information regarding dstirbution records for pharmceutical sales. EDA (Exploratory Data Analysis) and Executive Visualisations conducted in this project aims to catpure the transactional activity ranging from the global supply chains, regional sales teams, product classifications and customer channels. 
The Architecture:
    
    - Feilds: contains data dictinoary outlining each vairable definitino 
    
    - Data: transactional information (254,082 rows, 18 features)


Data Dictionary:

    Feild Names
    Distributor : Name of primary wholesaling partner or Distributor 
    Customer Names : Name of receiving entity (hospital, private clinics, retail pharmacies)
    City : Municipality where customers are located
    Country : Country of operation (european markets)
    Latitude : Geographical latitude coordinate of customer location 
    Longitude : Geographical Longitude coordinate of customer location 
    Channel : Broad operational channel classification (hospital vs pharmacy, public vs private)
    Sub-channel : Specific channel Sub-categorisation (private retail, instituions, experimerntal, clinics)
    Product Names : Name of Pharmaceutical Product distributed
    Product Class : Therapuetic Class or Pharmacological cateogry (Drug purpose: Pain, Antiseptic, Antifungal, Antiviral, Antibiotic etc.)
    Quantity : Number of units ordered/distributed
    Price : Unit price per product item sold
    Sales : total revenue calculated: QUANTITY x Price
    Month :  Month of transaction 
    Year : Year of transaction
    Name of Sales Rep : Individual sales rep. managing account
    Manager : regional/functional sales manager overseeing team of sales reps
    Sales Team : Organisational sales division of each team (identifiers)


Data Cleaning: What needs to be checked 

    - no missing values (impute)
    - correct data types per column 
    - ensuring correct units per column (for sales - ensure the calculation is correct- no negative values, no outlandish values)
    - outliers 
    - Merge columns that waste space having seperate features (feature selection/engineering)

EDA - Exploratory Data Analysis: Criteria to Fulfill:

1. Longitudinal Revenue Trends (Annual & Monthly Seasonality)

    - Key Goal: Identify macro-level revenue trajectory, year-over-year (YoY) growth rates, and any seasonal dips or spikes (e.g., Q4 budget flushes vs. summer slowness).
    - What to look at: Aggregate total `Sales` by year and month to track historical growth from 2017 to 2020.
    
2. Geographic & Spatial Performance Mapping

    - Key Goal: Discover which regions or cities generate the highest revenue concentrations and visualize geographic clusters across Germany and Poland using spatial bubble charts.
    - What to look at: Leverage the `Latitude`, `Longitude`, `Country`, and `City` fields to map sales distribution.

3. Product Portfolio & Therapeutic Class Dominance

    - Key Goal: Determine your "blockbuster" product classes versus underperforming lines to highlight core revenue drivers in your presentation.
    - What to look at: Analyze sales volume and revenue contribution segmented by `Product Class` and specific `Product Name`.

4. Channel & Sub-Channel Efficiency Analysis

    - Key Goal: Evaluate whether institutional sales or retail channels drive higher transaction values and profit margins.
    - What to look at: Compare performance metrics between `Channel` (e.g., Hospital vs. Pharmacy) and `Sub-channel` (e.g., Private, Retail, Institution).

5. Distributor Performance & Concentration Risk

    - Key Goal: Uncover dependency risks by determining what percentage of total company revenue is handled by top-tier wholesale partners.
    - What to look at: Aggregate sales and order quantities by `Distributor` (identifying major players like *Gerlach LLC*).

6. Sales Force Effectiveness & Regional Manager Rankings

    - Key Goal: Rank top-performing sales representatives and teams to spotlight sales force productivity and identify coaching opportunities for lagging regions.
    - What to look at: Evaluate total sales generated per `Name of Sales Rep`, grouped under their respective `Manager` and `Sales Team`.

7. Quantity vs. Unit Price Correlation Dynamics

    - Key Goal: Understand purchasing behaviors—do customers buy high quantities of lower-priced items, or do premium drugs sell in smaller batch sizes?
    - What to look at: Examine the relationship between `Quantity` ordered and the product `Price` using scatter plots and correlation matrices.

8. Return & Chargeback Impact Analysis (Data Cleaning Fallout)

    - Key Goal: Quantify the financial leakage caused by product returns and see which products or channels experience the highest return frequencies.
    - What to look at: Analyze records with negative `Quantity` and `Sales` values to isolate product returns or data correction entries.

9. Average Order Value (AOV) & Transaction Size Distributions

    - Key Goal: Identify standard purchasing thresholds and detect outlier transactions (massive institutional bulk orders vs. small retail top-ups).
    - What to look at: Calculate the distribution of transaction ticket sizes (`Sales` per individual row) across different customer types.

10. Multi-Dimensional Executive Summary Dashboard (Slide Prep)

    - Key Goal: Synthesize your core findings into clean, presentation-ready visualizations that tell a cohesive story for executive stakeholders.
    - What to look at: Combine top-line metrics (Total Revenue, Total Volume, Active Customers, Top Reps) into a unified multi-plot view.
