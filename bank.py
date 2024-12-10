#A simple bank app
#create 2 menu page (transaction, about us)
#Transaction page:
#Initial amount of user is $10,000
#Ask the user if her wants to deposit, withdraw or view account balance
#Then perform necessary operation and process to get user request done
import streamlit as st
import pandas as pd
Money = 10000
menu= st.sidebar.selectbox("Menu",['Transaction','About us'])
if menu == 'Transaction':
    st.subheader ("Transaction")
    pick = st.selectbox ("Do you want to ",['Deposit','Withdraw','View account balance'])
    if pick == 'Deposit':
        amount = st.selectbox ("Pick amount to deposit",['$50','$80','$100','$200','$500','$1000'],0)
        if amount == '$50':
            Money += 50
        if amount == '$80':
            Money +=80
        if amount == '$100':
            Money += 100
        if amount == '$200':
            Money += 200
        if amount == '$500':
            Money += 500
        if amount == '$1000':
            Money += 1000
    if pick == 'Withdraw':
        take = st.selectbox('Pick amount to Withdraw',['$50','$80','$100','$200','$500','$1000'],0)
        if take == '$50':
            Money -= 50
        if take == '$80':
            Money -= 80
        if take == '$100':
            Money -= 100
        if take == '$200':
            Money -= 200
        if take == '$500':
            Money -= 500
        if take == '$1000':
            Money -= 1000
    if pick == 'View account balance':
        st.write ('Your money is currently',Money,'dollars')