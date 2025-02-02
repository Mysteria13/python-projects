#Set up the Streamlit app:
#Import streamlit, pandas, and plotly.express.
#Set the app title as “Bookstore Weekly Sales Analysis.”
#Input sales data:
#Use st.number_input to enter sales for Fiction, Non-fiction, Comics, Magazines, and Textbooks.
#Display data:
#Store the category names and sales in a pandas DataFrame.
#Use st.table to display the data.
#Create a bar chart:
#Use Plotly Express to visualize the sales data.
#Show the chart using st.plotly_chart.
#Run the app:
#Test the app locally using streamlit run app.py.
import streamlit as st
import pandas as pd
import plotly_express as px
st.title ('Bookstore Weekly Sales Analysis.')
cl1,cl2 = st.columns(2)
with cl1:
    Fiction = st.number_input('Enter Weekly Sales for Fiction')
    Nonfiction = st.number_input('Enter Weekly Sales for Nonfiction')
    Comics = st.number_input('Enter Weekly Sales for Comics')
with cl2:
 Magazines = st.number_input('Enter Weekly Sales for Magazines')
 Textbooks = st.number_input('Enter Weekly Sales for Textbooks')
if st.button('Sumbit Weekly Sales'):
   bookdict = {'Fiction':[Fiction],'Nonfiction':[Nonfiction],'Comics':[Comics],'Magazines':[Magazines],'Textbooks':[Textbooks]}
   st.write (bookdict)
   booktables = pd.DataFrame (bookdict)
   booktablesvertical = booktables.melt(var_name='Books',value_name='Sales')
   st.table (booktables)
   st.table(booktablesvertical)

   barchart = px.bar (booktablesvertical,x='Books',y='Sales')
   st.plotly_chart(barchart)