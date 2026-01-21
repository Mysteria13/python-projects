import streamlit as st 
saved_amount=200
st.title("Charity Planner app by Lisa")
name =st.text_input ("Please enter your name")

venue_rental= st.number_input('Enter amount spent for renting sports venue',0)
if venue_rental >= 100:
    st.write (' you are spending too much money on one event')
equipment_cost= st.number_input('Enter amount spent for equipment',0)
if equipment_cost >= 100:
    st.write (' you are spending too much money on one event')
prize_cost= st.number_input('Enter amount spent for prizes',0)
if prize_cost >= 100:
    st.write (' you are spending too much money on one event')
refreshments_cost= st.number_input('Enter amount spent for refreshments',0)
if refreshments_cost >= 100:
    st.write (' you are spending too much money on one event')
ticket_sales= st.number_input('Enter amount earned from selling Tickets',0)
Refreshment_sales= st.number_input('Enter amount earned from selling refreshments',0)
total_amount_spent = venue_rental + equipment_cost + prize_cost + refreshments_cost
total_amount_earned = ticket_sales + Refreshment_sales
total_earned = saved_amount + total_amount_earned
remaining_balance = total_earned - total_amount_spent
if remaining_balance > 0:
    st.write  (name,'your remaining amount is ',remaining_balance)
elif remaining_balance <= 0:
    st.write (name,"you have spent more than you have saved ")
