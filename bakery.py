#You are the manager of a small bakery, and you want to analyze the weekly sales of your baked goods. The bakery sells five types of items: Bread, Cakes, Muffins, Cookies, and Pastries. At the end of the week, you want to input the sales figures for each item, display them in a table, and generate a bar chart to visualize which items sold the most.
#Set up the Streamlit app structure:
#Import necessary libraries (streamlit, pandas, plotly.express).
#Set a title for the app (e.g., “Bakery Weekly Sales Analysis”).
#Create input fields for sales data:
#Use st.number_input for each item to collect the weekly sales figures for Bread, Cakes, Muffins, Cookies, and Pastries.
#Process the data:
#Store the item names and sales figures in a pandas DataFrame.
#Ensure that the data is displayed in a table using st.dataframe.
#visualize the data:
#Use Plotly Express to create a bar chart showing sales for each item.
#Display the bar chart in Streamlit using st.plotly_chart.
#Run the app:
#Test the app locally using streamlit run app.py.
import streamlit as st
import pandas as pd
import plotly_express as px
st.title ('Bakery Weekly Sales Analysis')

col1,col2 = st.columns(2)
    
with col1:
    bread = st.number_input ("Please enter amount made from selling this Bread:",0)
    cake = st.number_input ('Please enter amount made from selling this Cake:',0)
    cookies = st.number_input ('Please enter amount made from selling this Cookies:',0)
with col2:
    pastries = st.number_input ('Please enter amount made from selling this Pasteries:',0)
    muffins = st.number_input ('Please enter amount made from selling this Muffins:',0)

if st.button ('View results'):
  fooddict = {'Bread':[bread],'Cake':[cake],'Cookies':[cookies],'Pastries':[pastries],'Muffins':[muffins]}
  st.write (fooddict)
  foodtable = pd.DataFrame (fooddict)
  st.table (foodtable)
  verticaltable = foodtable.melt(var_name='Food', value_name='Sales')
  st.table(verticaltable)
  barchart = px.bar(verticaltable,x='Food',y='Sales')
  st.plotly_chart(barchart) 