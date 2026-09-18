# Customer Churn Prediction & Analysis

An end-to-end customer churn analytics and machine learning project that combines **PostgreSQL, Python, Machine Learning, Power BI, and Flask** to analyze churn behavior, identify important churn patterns, and predict whether a customer is likely to churn.

---

## Project Overview

Customer churn directly affects retention and long-term business performance. This project was built to analyze customer behavior, understand the main factors associated with churn, and develop a machine learning model that can estimate churn risk for an individual customer.

The project covers the complete workflow:

- Data storage and retrieval using PostgreSQL
- Data quality checks and exploratory data analysis in Python
- Outlier and correlation analysis
- Feature selection and preprocessing
- Classification model comparison
- Logistic Regression model training and evaluation
- Saving reusable preprocessing and model artifacts
- Interactive churn analysis in Power BI
- Flask-based web application for customer-level churn prediction

---

## Business Objective

The main objectives of the project are to:

- Understand the overall churn level in the customer base
- Identify customer, billing, service, and behavioral factors associated with churn
- Compare churn patterns across different customer groups
- Build a machine learning model to predict customer churn
- Create an interactive Power BI dashboard for churn analysis
- Build a Flask application that returns both a churn prediction and churn probability

---

## Dataset Overview

The dataset used in this project contains:

- **35,000 customer records**
- **36 original columns**
- **0 missing values**
- **0 duplicate rows**

### Target Variable

The target column is:

```text
churn
```

Target distribution:

| Churn Status | Customers | Percentage |
|---|---:|---:|
| No | 25,102 | 71.72% |
| Yes | 9,898 | 28.28% |

The target distribution is imbalanced, with churned customers representing approximately **28.28%** of the dataset.

---

## Tools & Technologies

### Data & Database
- PostgreSQL
- SQL
- SQLAlchemy
- psycopg

### Python & Analysis
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

### Machine Learning
- Scikit-learn
- LazyPredict
- XGBoost
- Logistic Regression
- Decision Tree
- Random Forest
- AdaBoost
- Gradient Boosting
- Support Vector Machine
- K-Nearest Neighbors
- Gaussian Naive Bayes

### Visualization
- Power BI

### Web Application
- Flask
- HTML
- CSS
- Joblib

---

## Project Workflow

```text
Customer Dataset
       |
       v
PostgreSQL Database
       |
       v
Python / Jupyter Notebook
       |
       +--> Data Quality Checks
       +--> Exploratory Data Analysis
       +--> Outlier Analysis
       +--> Correlation Analysis
       +--> Feature Selection
       +--> Encoding & Scaling
       |
       v
Machine Learning Model Comparison
       |
       v
Logistic Regression
       |
       +--> Model Evaluation
       +--> Saved Model Artifacts
       |
       +--------------------+
       |                    |
       v                    v
Power BI Dashboard      Flask Web App
```

---

## Data Loading

The notebook connects to a local PostgreSQL database named:

```text
customer_churn_db
```

and loads data from:

```sql
SELECT * FROM customer_churn;
```

The PostgreSQL password is read from the environment variable:

```text
POSTGRES_PASSWORD
```

so the password is not hard-coded inside the notebook.

---

## Data Quality Checks

The following checks were performed before modeling:

- Dataset dimensions
- Data types
- Numerical descriptive statistics
- Categorical descriptive statistics
- Unique categorical values
- Missing-value analysis
- Duplicate-row analysis

The dataset contained **no missing values and no duplicate rows**.

---

## Exploratory Data Analysis

EDA was performed using both numerical and categorical features.

### Target Analysis

The churn distribution showed:

- **71.72% retained customers**
- **28.28% churned customers**

### Numerical Analysis

Numerical features were analyzed using:

- Distribution plots
- KDE plots
- Boxplots
- Pairplots
- Correlation heatmap

### Categorical Analysis

Churn rates were compared across categorical variables such as:

- Contract type
- Customer segment
- Payment method
- Auto payment
- Online security
- Tech support
- Discount received

---

## Outlier Analysis

Outliers were detected using the **IQR method**.

The highest outlier percentages were observed in:

| Feature | Outlier Percentage |
|---|---:|
| complaints_last_year | 8.55% |
| support_tickets_last_6_months | 7.70% |
| total_charges | 6.09% |
| discount_percent | 5.95% |
| customer_lifetime_value | 5.44% |

The outliers were **not removed automatically**, because extreme values in these fields can represent genuine customer behavior rather than data-entry errors.

---

## Correlation Analysis

The correlation analysis identified several strongly related numerical features:

- `customer_lifetime_value` vs `total_charges`: **0.96**
- `total_charges` vs `tenure_months`: **0.87**
- `customer_lifetime_value` vs `tenure_months`: **0.80**
- `nps_score` vs `customer_satisfaction`: **0.65**

These relationships were reviewed during feature selection to reduce redundancy and multicollinearity.

---

## Feature Selection

The following columns were removed before model training:

```text
customer_id
customer_lifetime_value
total_charges
nps_score
churn_risk_score
churn_reason
gender
region
city_tier
subscription_plan
paperless_billing
internet_service
phone_service
streaming_service
device_protection
```

### Reason for Removal

- `customer_id` was an identifier and did not provide predictive information.
- `customer_lifetime_value`, `total_charges`, and `nps_score` were removed to reduce redundancy.
- `churn_risk_score` and `churn_reason` were removed because they could introduce target leakage.
- Other categorical variables were removed because they showed relatively weak relationships with churn during categorical churn-rate analysis.

After feature selection, the model used **20 raw input features**.

---

## Final Model Input Features

The Flask application and model use the following 20 customer inputs:

```text
age
customer_segment
tenure_months
contract_type
monthly_charges
payment_method
auto_payment
online_security
tech_support
avg_monthly_usage_gb
num_logins_last_month
support_tickets_last_6_months
late_payments_last_year
customer_satisfaction
discount_received
discount_percent
complaints_last_year
last_interaction_days
marketing_emails_opened
cross_sell_products
```

---

## Data Preprocessing

### Train-Test Split

The data was split using an **80:20 stratified split**:

- Training set: **28,000 rows**
- Testing set: **7,000 rows**

### Categorical Encoding

Categorical preprocessing was fitted only on the training data.

Multi-category columns were encoded using **OneHotEncoder**:

```text
customer_segment
contract_type
payment_method
```

Binary categorical columns were encoded using **LabelEncoder**:

```text
auto_payment
online_security
tech_support
discount_received
```

`OneHotEncoder` was configured with:

```text
drop='first'
handle_unknown='ignore'
sparse_output=False
```

After encoding, the 20 raw inputs became **26 final model features**.

### Feature Scaling

The encoded features were standardized using:

```text
StandardScaler
```

The scaler was fitted on the training data and then applied to the test data.

---

## Model Comparison

Multiple classification algorithms were compared using **LazyPredict**:

- Logistic Regression
- Decision Tree
- Random Forest
- AdaBoost
- Gradient Boosting
- XGBoost
- Support Vector Machine
- K-Nearest Neighbors
- Gaussian Naive Bayes

AdaBoost achieved slightly higher accuracy, but **Logistic Regression was selected as the final model** because it provided comparable performance while remaining simpler and easier to interpret.

---

## Final Model Performance

The final Logistic Regression model achieved:

| Metric | Result |
|---|---:|
| Accuracy | **81.54%** |
| Churn Precision | **71%** |
| Churn Recall | **58%** |
| Churn F1-Score | **64%** |
| No-Churn Recall | **91%** |

The model performs well as a churn-prediction baseline, although churn recall can still be improved because some customers who actually churn are missed by the model.

---

## Saved Model Artifacts

The following files are saved inside the `model` folder:

```text
prediction_model.pkl
encoders.pkl
scaler.pkl
feature_columns.pkl
```

These files allow the Flask application to reuse the same preprocessing and feature order used during model training.

---

## Power BI Dashboard

The project includes an interactive Power BI dashboard for customer churn analysis.

Power BI file:

```text
dashboard/Customer_Churn_Dashboard.pbix
```

### Dashboard KPIs

- **Total Customers:** 35.0K
- **Churned Customers:** 9.9K
- **Churn Rate:** 28.3%
- **Retention Rate:** 71.7%
- **Average CLV:** 1.9K

### Key Dashboard Insights

- Month-to-Month customers have the highest churn rate at approximately **41.1%**.
- Customers without auto payment show a churn rate of approximately **36.2%**, compared with **17.8%** for customers using auto payment.
- Customers without tech support show a churn rate of approximately **36.4%**, compared with **14.9%** for customers with tech support.
- Churn decreases as customer tenure increases.
- Higher customer satisfaction is associated with lower churn.
- The dashboard also analyzes churn reasons and compares retained and churned customer profiles.

### Dashboard Preview

![Customer Churn Dashboard](dashboard/Customer_Churn_Dashboard.png)

---

## Flask Prediction Application

A Flask web application was created to make predictions using the saved model and preprocessing objects.

The application:

1. Collects 20 customer inputs from the HTML form
2. Applies the saved categorical encoders
3. Reorders the transformed data using `feature_columns.pkl`
4. Applies the saved `StandardScaler`
5. Generates a Logistic Regression prediction
6. Calculates churn probability using `predict_proba()`
7. Displays the result on the web page

The prediction result is displayed as:

```text
Customer is likely to Churn
```

or:

```text
Customer is not likely to Churn
```

The application also displays the predicted **Churn Probability**.

The result card is visually styled differently for churn and no-churn predictions.

---

### Web Application Preview

#### Prediction Form

![Web App Interface](images/web_app_interface.png)

#### Churn Prediction Example

![Churn Prediction](images/churn_prediction.png)

#### No Churn Prediction Example

![No Churn Prediction](images/no_churn_prediction.png)

---

## Project Folder Structure

```text
Customer Churn Prediction Projects/
│
├── app/
│   ├── app.py
│   ├── static/
│   │   └── style.css
│   └── templates/
│       └── index.html
│
├── dashboard/
│   ├── Customer_Churn_Dashboard.pbix
│   └── Customer_Churn_Dashboard.png
│
├── data/
│   └── customer_churn_dataset.csv
│
├── documentation/
│   └── data_dictionary.csv
│
├── images/
│   ├── web_app_interface.png
│   ├── churn_prediction.png
│   └── no_churn_prediction.png
│
├── model/
│   ├── encoders.pkl
│   ├── feature_columns.pkl
│   ├── prediction_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   └── Customer_Churn_Prediction.ipynb
│
├── sql/
│   └── customer_churn_database_setup.sql
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/kamranakhter03/customer-churn-prediction-analysis.git
cd customer-churn-prediction-analysis
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask Application

From the project root directory:

```bash
python app/app.py
```

Then open:

```text
http://127.0.0.1:5000
```

in your browser.

---

## Running the Notebook

To run the complete analysis notebook, PostgreSQL must be available locally.

The notebook expects:

```text
Database: customer_churn_db
Table: customer_churn
```

Set your PostgreSQL password through the `POSTGRES_PASSWORD` environment variable before running the notebook.

The SQL setup file is available at:

```text
sql/customer_churn_database_setup.sql
```

---

## Key Business Insights

The analysis found that:

- Overall customer churn is approximately **28.28%**.
- Month-to-Month customers have substantially higher churn than customers on longer contracts.
- Auto payment is associated with a much lower churn rate.
- Tech support is associated with a much lower churn rate.
- Online security is also associated with lower churn.
- Customers who received discounts showed lower churn than customers who did not receive discounts.
- Cash and Debit Card users showed relatively higher churn rates than other payment methods.
- Higher customer tenure and satisfaction are associated with lower churn.

These patterns can help identify customer groups that may require stronger retention strategies.

---

## Future Improvements

Based on the model evaluation, future work could include:

- Improving churn recall through model tuning
- Applying techniques for handling class imbalance
- Comparing additional tuned classification models
- Optimizing the prediction threshold based on business requirements
- Deploying the Flask application to a cloud platform

---

## Conclusion

This project demonstrates an end-to-end customer churn workflow covering **database integration, exploratory data analysis, feature selection, machine learning, Power BI visualization, and Flask deployment**.

The final Logistic Regression model achieved approximately **81.54% accuracy** and was integrated into a Flask application that provides both a churn prediction and churn probability for individual customers. The Power BI dashboard complements the predictive model by providing an interactive view of retention performance, churn drivers, and customer behavior.
