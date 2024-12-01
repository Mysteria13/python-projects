import streamlit as st
st.title('Cars  App made by Lisa')
name = st.text_input ("Please enter your name:")
set_recieved =st.number_input("Please enter your amount of set_recieved:")
cars_per_set =st.number_input("Please enter your amount of cars_per_set")
net_cars = cars_per_set * set_recieved 
gift_cars =st.number_input("Please enter your amount of gift_cars:")
gave_away_cars =st.number_input("Please enter your amount of gave_away_cars:")
net_cars = cars_per_set * set_recieved + gift_cars
if st.button("Check Amount"): #check if this button called age is clicked
    st.write(name,'your total amount of coins is' ,net_cars)

