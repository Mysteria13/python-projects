import streamlit as st
import pandas as pd
import plotly.express as px

#berverages: Espresso, Cappuccino, Latte, Mocha and Americano

col1,col2 = st.columns(2)

with col1:
    Espresso = st.number_input ('How much Espresso was sold this week')
    Cappuccino = st.number_input ('How much Cappuccino was sold this week')
    Latte = st.number_input ('How much Latte was sold this week')
with col2:
    Mocha = st.number_input ('How much Mocha was sold this week')
    Americano= st.number_input ('How much Americano was sold this week')
if st.button ('Sumbit Weekly Sales'):
    beveragedict = {'Espresso':[Espresso],'Cappuccino':[Cappuccino],'Latte':[Latte],'Mocha':[Mocha],'Americano':[Americano]}
    st.write(beveragedict)
    beveragetables = pd.DataFrame (beveragedict)
    beveragevertical = beveragetables.melt(var_name='Beverages', value_name='Sales')
    st.table(beveragetables)
    st.table(beveragevertical)


    barchart = px.bar (beveragevertical,x='Beverages',y='Sales')
    st.plotly_chart(barchart)