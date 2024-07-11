import pandas as pd
import plotly.express as px
import streamlit as st

# Adjusted file path assuming 'vehicles_us.csv' is in the same directory as 'app.py'
file_path = 'vehicles_us.csv'

# Read the dataset
df = pd.read_csv(file_path)

# Convert 'date_posted' to datetime
df['date_posted'] = pd.to_datetime(df['date_posted'])

# Fill missing values using .fillna() without inplace=True
median_model_year = df['model_year'].median()
median_cylinders = df['cylinders'].median()
median_odometer = df['odometer'].median()

df['model_year'] = df['model_year'].fillna(median_model_year)
df['cylinders'] = df['cylinders'].fillna(median_cylinders)
df['odometer'] = df['odometer'].fillna(median_odometer)

df['is_4wd'] = df['is_4wd'].fillna(False).astype(bool)

# Replace missing values in 'paint_color' with 'no color'
df['paint_color'] = df['paint_color'].fillna('no color')

# Function to extract manufacturer from model
def extract_manufacturer(model):
    return model.split()[0]

df['manufacturer'] = df['model'].apply(extract_manufacturer)

# Rearrange columns
df = df[['price', 'model_year', 'manufacturer', 'model', 'condition', 'cylinders', 'fuel', 
         'odometer', 'transmission', 'type', 'paint_color', 'is_4wd', 'date_posted', 
         'days_listed']]

# Streamlit app setup
st.title('Car Advertisement Dataset EDA')

st.header('Dataset Overview')
st.write('This dataset contains information about car advertisements in the US.')

show_top_manufacturers = st.checkbox('Show Top 3 Manufacturers')

# Filter dataframe based on top manufacturers
if show_top_manufacturers:
    top_manufacturers = df['manufacturer'].value_counts().nlargest(3).index
    filtered_df = df[df['manufacturer'].isin(top_manufacturers)]
else:
    filtered_df = df

# Display dataset
st.dataframe(filtered_df)

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

st.header('Days Listed Comparison between Manufacturers')


# Selectbox for selected_manufacturer1
selected_manufacturer1 = st.selectbox('Select Manufacturer 1', options=df['manufacturer'].unique(), index=df['manufacturer'].unique().tolist().index('chevrolet'))

# Selectbox for selected_manufacturer2
selected_manufacturer2 = st.selectbox('Select Manufacturer 2', options=df['manufacturer'].unique(), index=df['manufacturer'].unique().tolist().index('toyota'))


# Filter dataframe based on selected manufacturers
filtered_df = df[(df['manufacturer'] == selected_manufacturer1) | (df['manufacturer'] == selected_manufacturer2)]

# Plot days listed for selected manufacturers
fig = px.histogram(filtered_df, x='days_listed', color='manufacturer',
                   title=f'Days Listed Comparison: {selected_manufacturer1} vs {selected_manufacturer2}')
st.plotly_chart(fig)

df = df[df['model_year'] >= 1960]
# Scatter plot using Plotly Express
st.title('Price vs. Model Year')

# Scatter plot using Plotly Express
fig = px.scatter(df, x='model_year', y='price', title='Price vs. Model Year')
st.plotly_chart(fig)