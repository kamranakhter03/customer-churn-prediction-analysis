CREATE TABLE customer_churn (
    Customer_ID VARCHAR(20) PRIMARY KEY,
    Age SMALLINT,
    Gender VARCHAR(20),
    Region VARCHAR(20),
    City_Tier VARCHAR(20),
    Customer_Segment VARCHAR(20),
    Tenure_Months SMALLINT,
    Contract_Type VARCHAR(30),
    Subscription_Plan VARCHAR(20),
    Monthly_Charges DECIMAL(10,2),
    Total_Charges DECIMAL(12,2),
    Payment_Method VARCHAR(30),
    Auto_Payment VARCHAR(5),
    Paperless_Billing VARCHAR(5),
    Internet_Service VARCHAR(20),
    Phone_Service VARCHAR(5),
    Streaming_Service VARCHAR(5),
    Online_Security VARCHAR(5),
    Tech_Support VARCHAR(5),
    Device_Protection VARCHAR(5),
    Avg_Monthly_Usage_GB DECIMAL(10,2),
    Num_Logins_Last_Month SMALLINT,
    Support_Tickets_Last_6_Months SMALLINT,
    Late_Payments_Last_Year SMALLINT,
    Customer_Satisfaction DECIMAL(4,2),
    NPS_Score SMALLINT,
    Discount_Received VARCHAR(5),
    Discount_Percent DECIMAL(5,2),
    Complaints_Last_Year SMALLINT,
    Last_Interaction_Days SMALLINT,
    Marketing_Emails_Opened SMALLINT,
    Cross_Sell_Products SMALLINT,
    Customer_Lifetime_Value DECIMAL(12,2),
    Churn_Risk_Score DECIMAL(5,2),
    Churn_Reason VARCHAR(50),
    Churn VARCHAR(5)
);


-- Import the dataset into PostgreSQL.
-- Replace the path below with the absolute path of customer_churn_dataset.csv
-- on your local system before running the COPY command.

/*
	COPY customer_churn
	FROM 'C:/path/to/Customer-Churn-Prediction/data/customer_churn_dataset.csv'
	DELIMITER ','
	CSV HEADER;
*/

SELECT * FROM customer_churn;