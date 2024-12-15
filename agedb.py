####Homework Create an python app
#-Ask for the user name on the left column and their email on the right column
#next create an age calculator to find out their age
#create a submit button
#show their name, email and age after submit button is clicked
#create a csv and a table to show the user name, email and age on the table
#PUBLISH THIS ONE AND SHARE THE LINK
import streamlit as st
import pandas as pd

readcsv = pd.read_csv('age.csv')
st.title = ("Age app")
menu = st.sidebar.selectbox("Choose an option",["input info","Response"])
if menu == "Response":
    st.table(readcsv)
     
if menu == 'input info':
    col1,col2= st.columns(2)
    with col1:
        name = st.text_input('Please enter your name')
    with col2:
        email= st.text_input('Please enter your email address')
    col3,col4=st.columns (2)
    with col3:
     yob = st.number_input('Please enter your year of birth',0)
    with col4:
     currentyear = st.number_input('Please enter the current year',0)
    age = currentyear - yob 
    if st.button ("Sumbit info"):
          st.write (name,"your email is",email,"and your age is",age,)
          agedict = {"Name":[name],"Email":[email],"Age":[age]}
          st.write(agedict)
          age_table=pd.DataFrame (agedict)
          st.table (age_table)
          tablesjoin = pd.concat([readcsv,age_table],ignore_index=True)
          tablesjoin.to_csv (age.csv,index=False)
          st.success ('Info Sumbitted')