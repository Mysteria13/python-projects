import streamlit as st
import pandas as pd
#ALSO GOAL ACHEVIEVED AND GOAL LEFT
readcsv = pd.read_csv('donations.csv')
menu = st.sidebar.selectbox("Choose an option",['Create Donations','View Donations','Donate'])
if menu == 'Create Donations':
    st.subheader  (":blue [Create Donation]") 
    st.divider()
    col1,col2 = st.columns(2)
    with col1:
     cam_title = st.text_input ("State Campaign Title")
    with col2:
     email = st.text_input ("Set Email")
    st.divider()
    cam_dit = st.text_area ("Campaign Details",height=200)
    st.divider()
    col3,col4 = st.columns(2)
    with col3:
     amount =st. selectbox ("Goal amount",['$10','$20','$50','$100','Custom amount'],0)
    if amount =='$10':
      amount = 10
    if amount =='$20':
      amount = 20
    if amount =='$30':
      amount = 30
    if amount =='$50':
      amount = 50
    if amount =='$100':
      amount = 100
    if amount =='$500':
      amount = 500
    if amount =='Custom amount':
      with col4:
       amount = st.number_input ("Please enter custom amount",0)
    st.divider()
    with col3:
      if st.button ("Create Campaign"):
        #this creates a dict which assigns the variables to their categories in csv
        donations_dict = {'Campaign Title':[cam_title],'Campaign Email':[email],'Campaign amount':[amount],'Campaign Details':[cam_dit]}
        st.write(donations_dict)
        #this converts the dict to a tableform dataframe
        donations_table = pd.DataFrame(donations_dict) 
        #st.table(donations_table)
        #this will join the two tables together existing in csv,new from input]
        donations_join = pd.concat([readcsv,donations_table],ignore_index=True)
        donations_join.to_csv('donations.csv',index = False)
        st.success("Donation Campaign created")
if menu =="View Donations":
  st.subheader(":orange[Campaign Details]")
  alltitles = readcsv['Campaign Title']
  col1,col2 = st.columns(2)
  with col1:
    selectitle = st.selectbox ("Choose one title",alltitles)

  filtertitle = readcsv[readcsv ['Campaign Title'] == selectitle]
  #st.table(filtertitle)
  getdit = filtertitle['Campaign Details'].iloc[0]
  getEmail = filtertitle['Campaign Email'].iloc[0]

  st.divider()
  st.write(getdit)
  st.write(getEmail)
  

