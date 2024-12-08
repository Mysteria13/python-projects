#A simple bank app
#create 2 menu page (transaction, about us)
#Transaction page:
#Initial amount of user is $10,000
#Ask the user if her wants to deposit, withdraw or view account balance
#Then perform necessary operation and process to get user request done
import streamlit as st
import pandas as pd
Money = 10000
menu= st.sidebar.selectbox = ("Menu",['Transaction','About us'])
if menu == 'Transaction':
    st.subheader =("Transaction")