import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
#read file from source
file_path = r"C:\Users\Window\Downloads\metadata.csv\metadata.csv"
#Load the CSV file into a DataFrame
df = pd.read_csv(file_path)
# Add interactive elements
st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")
# Add interactive elements
year_range = st.slider("Select year range", 2019, 2022, (2020, 2021))
# Add visualizations based on selection
# Basic info
print(df.shape)
print(df.info())

# Check missing values
print(df.isnull().sum())

# Simple visualization
df['year'] = pd.to_datetime(df['publish_time']).dt.year
year_counts = df['year'].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values)
plt.title('Publications by Year')
plt.show()