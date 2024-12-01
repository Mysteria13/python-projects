import streamlit as st
st.title('Savings App made by Lisa')

cash = 250
st.write("Your inital savings is ",cash)
snacks_cost = st.number_input('Please enter the snacks cost',0)
theme_park_cost = st.number_input('Please enter the theme park cost',0)
movies_cost = st.number_input('Please enter the movies cost',0)
bikes_cost = st.number_input('Please enter the bikes cost',0)
beach_cost = st.number_input('Please enter the beach cost',0)
remaining_amount = cash - (snacks_cost + theme_park_cost + movies_cost + bikes_cost + beach_cost)
st.write("Your remaining amount is",remaining_amount,'dollars')
