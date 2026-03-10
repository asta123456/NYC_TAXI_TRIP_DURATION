# 🚕 Taxi Trip Duration Prediction

This project predicts the **duration of a taxi trip** using Machine Learning.
The model is trained using the NYC Taxi Trip dataset and deployed as a simple web application using Streamlit.

---

## 📌 Project Overview

The goal of this project is to build a machine learning model that predicts how long a taxi trip will take based on several input features such as passenger count and pickup/dropoff locations.

The application allows users to input trip details and get an estimated trip duration instantly through a web interface.

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

The app is deployed using **Streamlit Community Cloud** and the code is hosted on **GitHub**.

---

## 📂 Project Structure

```
NYC-taxi-trip-duration
│
├── model.py            # Machine learning model training
├── app.py              # Streamlit web application
├── taxi_model.pkl      # Saved trained model
├── train.csv           # Dataset
└── README.md           # Project documentation
```

---

## ⚙️ Steps in the Project

1. Load the dataset
2. Understand and clean the data
3. Select input and output variables
4. Split the dataset into training and testing sets
5. Train the machine learning model
6. Evaluate the model performance
7. Save the trained model using pickle
8. Build a user interface using Streamlit
9. Deploy the project

---

## 🚀 How to Run the Project

1. Clone the repository

```
git clone <your-repo-link>
```

2. Install required libraries

```
pip install pandas numpy scikit-learn streamlit
```

3. Train the model

```
python model.py
```

4. Run the Streamlit application

```
streamlit run app.py
```

---

## 🎯 Features

* Predict taxi trip duration
* Simple user interface
* Machine learning based prediction
* Interactive web application

---

## 📊 Dataset

The model uses the **NYC Taxi Trip Duration dataset** which contains information such as:

* Passenger count
* Pickup location
* Dropoff location
* Pickup time
* Trip duration

---

## 📌 Future Improvements

* Improve model accuracy
* Add map visualization
* Deploy advanced machine learning models



Marjani
Machine Learning Project
