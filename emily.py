import streamlit as st
st.title('Savings App made by Lisa')

cash = 150
st.write("Your inital savings is ",cash)
snacks_cost = st.number_input('Please enter the snacks cost',0)
toy_cost = st.number_input('Please enter the toy cost',0)
book_cost = st.number_input('Please enter the book cost',0)
taxi_cost = st.number_input('Please enter the taxi cost',0)
game_cost = st.number_input('Please enter the game cost',0)
remaining_amount = cash - (snacks_cost + toy_cost + book_cost + taxi_cost + game_cost)
st.write("Your remaining amount is",remaining_amount,'dollars')
