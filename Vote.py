import streamlit as st # this is the page to display my python app
import pandas as pd
import plotly.express as px 
st.set_page_config(page_title='School Vote',page_icon='L')
readcsv =pd.read_csv('vote2.csv')
menu = st.sidebar.selectbox("Choose an option",['Enter vote','View vote'])
# a selectbox needs to use a list in order to store different items to choose from 
#a list is used to store mutiple items in a variable 

if menu == 'Enter vote':
    col1,col2 = st.columns(2)
    with col1:
        name = st.text_input("Please enter your name")
    with col2:
        vote = st.selectbox ("Pick a contestant",['Lisa','Nancy','Praise','Jason'])
        #---------------------------HOW TO CREATE A BUTTON--------------------------------
        if st.button ('Cast your vote'):
            st.write("Thanks for voting for",vote)
            # ---- how to save to csv----------------------------
            votedict = {'Name':[name],'contestant':[vote]}
            # a dictionary is used when you want to save items in their categories a list cant do this
            votetable = pd.DataFrame(votedict)
            #this converts a dictionary to a table format 
            vote_join = pd.concat([readcsv,votetable],ignore_index=True)
            #this joins the csv data with the new data when you press enter  
            vote_join.to_csv('vote2.csv',index = False)
            #this saves the data in th csv file
            st.success("Okay, Done!")
if menu == 'View vote':
    with st.expander("Click to view table"): #this creates a box you can open and close
     contestantstable = readcsv["contestant"].value_counts().reset_index()#this shows only the table for contestants  and count each item
     st.table(contestantstable)



    piechart = px.pie(contestantstable,names='contestant',values='count')
    st.plotly_chart(piechart)