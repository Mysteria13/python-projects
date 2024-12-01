import streamlit as st
st.title('Savings App made by Lisa')

cash = 5000
st.write("Your inital savings is ",cash)
phone_cost = st.number_input('Please enter the phone cost',0)
clothes_cost = st.number_input('Please enter the clothes cost',0)
book_cost = st.number_input('Please enter the book cost',0)
decorations_cost = st.number_input('Please enter the decorations cost',0)
dinner_cost = st.number_input('Please enter the dinner cost',0)
remaining_amount = cash - (phone_cost + clothes_cost + book_cost + decorations_cost + dinner_cost)
st.write("Your remaining amount is",remaining_amount,'dollars')
personal_shopping = st.number_input('Please enter amount for personal shopping',0)
remaining_amount = remaining_amount - personal_shopping
st.write("Your remaining amount is",remaining_amount,'dollars')

