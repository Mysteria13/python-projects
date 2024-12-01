import streamlit as st
st.title('Coin  App made by Lisa')
name = st.text_input ("Please enter your name:")
gold_coins =st.number_input("Please enter your amount of gold_coins:")

silver_coins =  st.number_input("Please enter your amount of silver_coins:")
bronze_coins =st.number_input("Please enter your amount of bronze_coins:")

total = gold_coins + silver_coins + bronze_coins
if st.button("Check Amount"): #check if this button called age is clicked
    st.write(name,'your total amount of coins is' ,total)