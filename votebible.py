import streamlit as st
import pandas as pd 
import plotly_express as px
readcsv = pd.read_csv ('bible.csv')
menu = st.sidebar.selectbox ('Choose Option',['Cast your vote','View results'])
col1,col2 = st.columns(2)
if menu == 'Cast your vote':
  with col1:
    name = st.text_input ("Enter your name")
  with col2:
    Bible_character = st.selectbox ("Choose your favourie character",['Ruth','Joseph','Abraham','Moses','David'])
    if st.button ('Cast your vote'):
      st.write("Thanks for voting for",Bible_character)
      bibledict = {'Name':[name],'Character':[Bible_character]}
      bibletable = pd.DataFrame(bibledict)
      bible_join = pd.concat ([readcsv,bibletable],ignore_index=True)
      bible_join.to_csv('bible.csv',index= False)
      st.success("Okay Done!")
if menu == 'View results':
  with st.expander('Click to see table'):
    characterstable = readcsv["Character"].value_counts().reset_index()
    st.table(characterstable)




    piechart = px.pie(characterstable,names='Character',values='count')
    st.plotly_chart(piechart)
  