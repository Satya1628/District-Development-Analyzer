import streamlit as st
import pandas as pd
import joblib

# -----------------------
# Load Model
# -----------------------

model = joblib.load("development_model.pkl")
encoder = joblib.load("label_encoder.pkl")
literacy_model = joblib.load("literacy_prediction_model.pkl")
df = pd.read_csv("district_development_dataset.csv")

# -----------------------
# Title
# -----------------------

st.set_page_config(
    page_title="District Development Analyzer",
    layout="wide"
)

st.title("🏛️ Smart District Development Analyzer")

st.write(
    "Predict the Development Category of an Indian District using Machine Learning."
)

# -----------------------
# Sidebar
# -----------------------

menu = st.sidebar.selectbox(
    "Select Module",
    [
        "Home",
        "Dataset",
        "Prediction",
        "Feature Importance",
        "About"
    ]
)

# -----------------------
# Home
# -----------------------

if menu=="Home":

    st.header("Project Overview")

    st.write("""
    This project predicts district development category
    based on socioeconomic census indicators.

    ML Model:
    Random Forest Classifier
    """)

# -----------------------
# Dataset
# -----------------------

elif menu=="Dataset":

    st.header("Dataset Preview")

    st.dataframe(df.head())

    st.write("Rows:",df.shape[0])

    st.write("Columns:",df.shape[1])

# -----------------------
# Prediction
# -----------------------

elif menu=="Prediction":

    st.header("Development Prediction")

    literacy = st.slider(
        "Literacy Rate",
        0.0,
        100.0,
        70.0
    )

    female = st.slider(
        "Female Literacy Rate",
        0.0,
        100.0,
        65.0
    )

    worker = st.slider(
        "Worker Participation Rate",
        0.0,
        100.0,
        40.0
    )

    sc = st.slider(
        "SC Percentage",
        0.0,
        100.0,
        15.0
    )

    stp = st.slider(
        "ST Percentage",
        0.0,
        100.0,
        10.0
    )

    gender = st.slider(
        "Gender Ratio",
        700.0,
        1200.0,
        950.0
    )

    household = st.slider(
        "People Per Household",
        2.0,
        10.0,
        5.0
    )

    if st.button("Predict"):

       X = [[
    literacy / 100,
    female / 100,
    worker / 100,
    sc ,
    stp ,
    (gender-700)/(1200-700),      # wait before changing these
    household    # wait before changing these
        ]]
       pred = model.predict(X)
       probs = model.predict_proba(X)
       result = encoder.inverse_transform(pred)
       st.success(
        f"Predicted Category : {result[0]}"
    )
       st.subheader("Prediction Confidence")
       for cls, prob in zip(encoder.classes_, probs[0]):
        st.write(f"{cls}: {prob*100:.2f}%")

elif menu == "Literacy Prediction":

    st.header("📚 Literacy Rate Prediction")

    female = st.slider(
        "Female Literacy Rate",
        0.0,
        100.0,
        60.0
    )

    worker = st.slider(
        "Worker Participation Rate",
        0.0,
        100.0,
        40.0
    )

    sc = st.slider(
        "SC Percentage",
        0.0,
        100.0,
        15.0
    )

    stp = st.slider(
        "ST Percentage",
        0.0,
        100.0,
        10.0
    )

    gender = st.slider(
        "Gender Ratio",
        700.0,
        1200.0,
        950.0
    )

    household = st.slider(
        "People Per Household",
        2.0,
        10.0,
        5.0
    )

    if st.button("Predict Literacy Rate"):

        X = [[
            female / 100,
            worker / 100,
            sc,
            stp,
            (gender - 700) / 500,
            household
        ]]

        literacy_pred = literacy_model.predict(X)[0]

        literacy_pred = literacy_pred * 100

        st.success(
            f"Predicted Literacy Rate: {literacy_pred:.2f}%"
        )
# -----------------------
# Feature Importance
# -----------------------

elif menu=="Feature Importance":

    st.header("Feature Importance")

    importance = pd.DataFrame({

        "Feature":[

            "Literacy Rate",

            "Female Literacy",

            "Worker Participation",

            "SC Percentage",

            "ST Percentage",

            "Gender Ratio",

            "People Per Household"

        ],

        "Importance":

        model.feature_importances_

    })

    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )

    st.bar_chart(
        importance.set_index("Feature")
    )

    st.dataframe(importance)

# -----------------------
# About
# -----------------------

else:

    st.header("About Project")

    st.write("""
    Smart District Development Analyzer

    Developed using:

    • Census Dataset

    • Random Forest Classifier

    • Streamlit

    • Python

    End Semester Machine Learning Project
    """)