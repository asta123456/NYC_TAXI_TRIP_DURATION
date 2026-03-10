# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv("C:\\Users\\ASTALAKSHMI\\Downloads\\archive (2)\\NYC.csv")
print(df.head())

# %%
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
df['hour'] = df['pickup_datetime'].dt.hour
# %%
import pandas as pd

# Load dataset
df = pd.read_csv("C:\\Users\\ASTALAKSHMI\\Downloads\\archive (2)\\NYC.csv")

# Show first 5 rows
print(df.head())

# Dataset information
print(df.info())

# Check missing values
print(df.isnull().sum())
#%%
# Convert pickup time to datetime
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])

# Extract useful feature
df['hour'] = df['pickup_datetime'].dt.hour

# Select useful columns
df = df[['trip_duration','passenger_count','pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','hour']]

print(df.head())
#%%
# Input variables
X = df[['passenger_count','pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','hour']]

# Output variable
y = df['trip_duration']
#%%
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)
#%%
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print("Model trained successfully")
#%%
score = model.score(X_test, y_test)
print("Model accuracy:", score)
#%%
import pickle

pickle.dump(model, open("taxi_model.pkl","wb"))

print("Model saved")