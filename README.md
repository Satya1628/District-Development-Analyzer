# 🏛️ District Development Analyzer

A machine learning-based web application that analyzes socioeconomic indicators and predicts the development category of Indian districts. The project uses census data and a Random Forest Classifier to explore district-level development patterns and generate predictions.

## 📌 Project Overview
Here(https://district-development-analyzer-jgobeuzdn2jrv4xgcmsjzr.streamlit.app/)

District development depends on several socioeconomic factors, including literacy, workforce participation, gender ratio, and household characteristics.

The **District Development Analyzer** provides an interactive dashboard to explore district data, predict development categories, estimate literacy rates, and understand the importance of different features.

## ✨ Features

- **Dataset Exploration:** Preview the district dataset and inspect its rows and columns.
- **Development Category Prediction:** Predict a district's development category using user-defined socioeconomic indicators.
- **Literacy Rate Prediction:** Estimate literacy rates based on selected demographic features.
- **Prediction Confidence:** Display the model's predicted class probabilities.
- **Feature Importance:** Visualize the relative importance of input features in the development classification model.
- **Interactive Dashboard:** Explore the application through a simple Streamlit interface.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Data Processing:** Pandas
- **Machine Learning:** Scikit-learn, Random Forest Classifier
- **Model Persistence:** Joblib
- **Web Application:** Streamlit
- **Development Environment:** Jupyter Notebook

## 📂 Project Structure

```text
District-Development-Analyzer/
│
├── app.py
├── main.ipynb
├── requirements.txt
│
├── 2011-IndiaStateDistSbDist-0000.xlsx - Data (1).csv
├── EDA_Dataset.csv
├── cleaned_district_data.csv
├── district_development_dataset.csv
│
├── development_model.pkl
├── label_encoder.pkl
└── literacy_prediction_model.pkl
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Satya1628/District-Development-Analyzer.git
```

### 2. Navigate to the project directory

```bash
cd District-Development-Analyzer
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser, where you can explore the dataset and use the prediction modules.

## 🧠 Machine Learning Workflow

1. **Data Collection:** Work with district-level census and socioeconomic data.
2. **Exploratory Data Analysis:** Inspect the dataset to understand its structure and characteristics.
3. **Data Preprocessing:** Prepare the data for model training.
4. **Model Training:** Use a Random Forest Classifier for development category prediction.
5. **Model Persistence:** Save trained models and the label encoder using Joblib.
6. **Prediction:** Generate predictions from user-provided feature values.
7. **Visualization:** Display feature importance and prediction results through Streamlit.

## 🎯 Objectives

- Apply machine learning to a socioeconomic development problem.
- Explore district-level census data.
- Understand the relationship between demographic indicators and predicted development categories.
- Build an interactive application that makes machine learning predictions accessible to users.

## 🔮 Future Improvements

- Add more socioeconomic indicators, such as healthcare, education, and infrastructure access.
- Improve model evaluation with appropriate classification metrics.
- Include district-wise comparisons and interactive visualizations.
- Expand the analysis with updated datasets.
- Deploy the application online for public access.

## ⚠️ Disclaimer

This project is intended for educational and analytical purposes. Predictions are based on the available dataset and trained models; they should not be treated as official government development classifications or definitive assessments of a district.

## 👨‍💻 Author

**Satya1628**

GitHub: [Satya1628](https://github.com/Satya1628)

## ⭐ Acknowledgements

This project uses census-related data to explore machine learning applications in socioeconomic development analysis.

If you find this project useful, consider giving the repository a star!
