import streamlit as st
import pandas as pd
import plotly.express as px
vus = pd.read_csv('vehicles_us.csv')

#adding a header

st.header("Vehicle Sales Analysis Dashboard")

#Plotly histogram with price distribution

fig_price = px.histogram(vus, x='price', title='Price Distribution')
st.plotly_chart(fig_price)

#PLotly histogram with odometer readings/milage

fig_odometer = px.histogram(vus, x='odometer', title='Odometer Distribution', labels={'odometer': 'Odometer (Thousands)'})
st.plotly_chart(fig_odometer)

#Plotly scatter plot

fig_price_odometer = px.scatter(vus, x='odometer', y='price', title='Price vs Odometer', labels={'odometer': 'Odometer (Thousands)', 'price': 'Price (USD)'})
st.plotly_chart(fig_price_odometer)

#Scatter plot with price v model
fig_price_model_year = px.scatter(vus, x='model_year', y='price', title='Price vs Model Year')
st.plotly_chart(fig_price_model_year)

#Violin plot with price v condition
fig_price_condition = px.violin(vus, x='condition', y='price', title='Price vs Condition', points='all') 
st.plotly_chart(fig_price_condition)
                
# Adding a checkbox for filtering data

if st.checkbox("Show only vehicles under $20,000"):
    filtered_data = vus[vus['price'] < 20000]
    st.write(filtered_data)
