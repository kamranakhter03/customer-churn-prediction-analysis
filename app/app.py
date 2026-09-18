from pathlib import Path
from flask import Flask, render_template, request
import joblib
import pandas as pd
from sklearn.preprocessing import OneHotEncoder


app = Flask(__name__)


# Load saved files
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR.parent / "model"

model = joblib.load(MODEL_DIR / "prediction_model.pkl")
scaler = joblib.load(MODEL_DIR / "scaler.pkl")
encoders = joblib.load(MODEL_DIR / "encoders.pkl")
feature_columns = joblib.load(MODEL_DIR / "feature_columns.pkl")


# Categorical features used for encoding
categorical_columns = [
    "customer_segment",
    "contract_type",
    "payment_method",
    "auto_payment",
    "online_security",
    "tech_support",
    "discount_received"
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Collect form data
        input_data = {
            "age": float(request.form["age"]),
            "customer_segment": request.form["customer_segment"],
            "tenure_months": float(request.form["tenure_months"]),
            "contract_type": request.form["contract_type"],
            "monthly_charges": float(request.form["monthly_charges"]),
            "payment_method": request.form["payment_method"],
            "auto_payment": request.form["auto_payment"],
            "online_security": request.form["online_security"],
            "tech_support": request.form["tech_support"],
            "avg_monthly_usage_gb": float(request.form["avg_monthly_usage_gb"]),
            "num_logins_last_month": float(request.form["num_logins_last_month"]),
            "support_tickets_last_6_months": float(
                request.form["support_tickets_last_6_months"]
            ),
            "late_payments_last_year": float(
                request.form["late_payments_last_year"]
            ),
            "customer_satisfaction": float(
                request.form["customer_satisfaction"]
            ),
            "discount_received": request.form["discount_received"],
            "discount_percent": float(request.form["discount_percent"]),
            "complaints_last_year": float(
                request.form["complaints_last_year"]
            ),
            "last_interaction_days": float(
                request.form["last_interaction_days"]
            ),
            "marketing_emails_opened": float(
                request.form["marketing_emails_opened"]
            ),
            "cross_sell_products": float(
                request.form["cross_sell_products"]
            )
        }


        # Convert user input into a DataFrame
        input_df = pd.DataFrame(
            [input_data]
        )


        # Encode categorical features using saved encoders
        for column in categorical_columns:

            encoder = encoders[column]

            if isinstance(encoder, OneHotEncoder):

                encoded = encoder.transform(input_df[[column]])

                encoded_df = pd.DataFrame(
                    encoded,
                    columns=encoder.get_feature_names_out([column]),
                    index=input_df.index
                )

                input_df = pd.concat(
                    [input_df.drop(columns=[column]), encoded_df],
                    axis=1
                )

            else:
                input_df[column] = encoder.transform(input_df[column])


        # Arrange features in the same order used during model training
        input_df = input_df.reindex(
            columns=feature_columns,
            fill_value=0
        )
        
        # Scale using saved scaler
        input_scaled = scaler.transform(input_df)


        # Prediction
        prediction = model.predict(input_scaled)[0]

        churn_probability = model.predict_proba(
            input_scaled
        )[0][1]

        churn_probability = round(
            churn_probability * 100,
            2
        )


        if prediction == 1:
            result = "Customer is likely to Churn"
            result_class = "churn"
        else:
            result = "Customer is not likely to Churn"
            result_class = "no-churn"


        return render_template(
            "index.html",
            prediction=result,
            probability=churn_probability,
            result_class=result_class
        )


    except Exception as e:

        return render_template(
            "index.html",
            prediction="Error while making prediction",
            error=str(e)
        )


if __name__ == "__main__":
    app.run(debug=True)