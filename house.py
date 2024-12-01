import streamlit as st
bill=0
st.title("House Buyer app")
col1, col2 = st.columns(2)
#"""write a python program for house buyers


#Ask them for their name
#ask them for their yearly salary
#if they earn below 100000 they can buy or rent an apartment
#If the earn between 100000-500,000 they can buy a bungalow
#If the earn between >500,000-1,000,000 they can buy a duplex
#If the earn between >1,000,000-5,000,000 they can buy a manshion
#if the earn above 5000000 they can buy an estate

with col1:
      name = st.text_input('Please enter your name')
with col2:
     yearly_salary = st.number_input('Please enter your yearly salary',0)
if st.checkbox("Check the house you can afford"):
     if yearly_salary < 10000:
        st.write("Sorry you can afford any houses yet")  
     elif yearly_salary >= 10000 and yearly_salary <= 100000:
         st.write("You can rent or buy an apartment")
         if st.checkbox("Buy an apartment: $60,000"):
              st.write("Ok Done")
              bill +=60000
         if st.checkbox("Rent an apartment yearly: $4,000"):
               st.write("Ok Done")
               bill +=4000
     elif yearly_salary > 100000 and yearly_salary  <= 500000:
            st.write ("You can rent or buy a Bungalow")
            if st.checkbox("Buy a Bungalow: $200,000"):
              st.write("Ok Done")
              bill +=200000
            if st.checkbox("Rent a Bungalow Yearly: $10,000"):
               st.write("Ok Done")
               bill +=10000
     elif yearly_salary > 500000 and yearly_salary <= 1000000:
          st.write ("You can rent or buy a Duplex")
          if st.checkbox("Buy a Duplex: $700,000"):
              st.write("Ok Done")
              bill +=700000
          if st.checkbox("Rent a Duplex Yearly: $50,000"):
               st.write("Ok Done")
               bill +=50000
     elif yearly_salary > 1000000 and yearly_salary <= 5000000:
          st.write("You can buy or rent a Mansion")
          if st.checkbox("Buy a Mansion: $3,000,000"):
              st.write("Ok Done")
              bill +=3000000
          if st.checkbox("Rent a Mansion: $300,000"):
               st.write("Ok Done")
               bill +=300000
     elif  yearly_salary > 5000000:
           st.write("You can buy an estate")
           if st.checkbox("Buy an estate: $8,000,000"):
              st.write("Ok Done")
              bill +=8000000


if st.button("Check total bill "):
    st.write(name,'your total bill is', bill,'dollars')