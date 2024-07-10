import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('/Users/nathanmerlino/my_project/vehicles_us.csv')

st.title('Car Advertisement Dataset EDA')

st.header('Dataset Overview')
st.write('This dataset contains information about car advertisements in the US.')

# Display dataset
st.dataframe(df)

# Step 5: Describe the columns
st.header('Column Descriptions')
st.markdown("""
- **price**: The sale price of the vehicle.
- **model_year**: The year the car model was manufactured.
- **manufacturer**: The manufacturer of the vehicle based on the first word in the model name.
- **model**: The specific model of the car.
- **condition**: The condition of the car (e.g., excellent, good, fair).
- **cylinders**: Number of cylinders in the engine.
- **fuel**: Type of fuel used by the vehicle.
- **odometer**: The distance the vehicle has traveled in miles.
- **transmission**: The type of transmission (e.g., automatic, manual).
- **type**: The body type of the vehicle (e.g., sedan, SUV).
- **paint_color**: The color of the vehicle.
- **is_4wd**: Whether the vehicle has 4-wheel drive (True/False).
- **date_posted**: The date the advertisement was posted.
- **days_listed**: Number of days the advertisement was active.
""")

st.header('Histogram of Price by Condition')

fig = px.histogram(df, x='price', color='condition', title='Histogram of Price by Condition', range_x=[0,80000])
st.plotly_chart(fig)

