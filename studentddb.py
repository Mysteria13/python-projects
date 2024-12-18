import streamlit as st #this creates web page for your python app
import pandas as pd#this works with csv and converts to table
import plotly.express as px#this is used to plot charts
st.set_page_config(page_title='Student Databse',page_icon='👌')
st.title(' Student database App ')

menu = st.sidebar.selectbox("Choose an option",["input scores","scores database/chart"])

try: #attempt to do what is below 
   readcsv = pd.read_csv('scores.csv')
except:#if there is an error in the above attempt then do this
     readcsv = pd.DataFrame()#create an empty dataframe for me

     #csv : comma seperated values
#menu page to only show the table 
if menu == "scores database/chart":
    st.table(readcsv)
    subjects = ["Math","English","Science","Art","History","Geography"]
    subjectstable = readcsv[subjects].mean().reset_index()

    barchart = px.bar(subjectstable,x='index',y=0) 
    st.plotly_chart(barchart)    
if menu == "input scores": 
     name = st.text_input('Please enter Student name')
     col1, col2, = st.columns(2)
     with col1:
          math = st.number_input('Enter students math score',0)
          English = st.number_input('Enter students english score',0)
          Science = st.number_input('Enter students science score',0)
     with col2:
          Art = st.number_input('Enter students art score',0)
          History = st.number_input('Enter students history score',0)
          Geo = st.number_input('Enter students geography score',0)
     Total = math + English + Science + Art + History + Geo
     ave = Total/6
     if ave >= 100:
          grade = 'A+'
     elif ave >= 90:
          grade = 'A'
     elif ave >= 80:
          grade = 'B+'
     elif ave >= 70:
          grade ='B' 
     elif ave >= 60:
          grade ='B-' 
     elif ave >= 50:
          grade ='C' 
     elif ave >= 40:
          grade ='D' 
     elif ave <= 30:
          grade ='F' 
     if st.button ("Save student scores"):
          if name and math and English and Science and Art and History and Geo:
           st.write (name,"your total score is",Total,"average is",ave,"grade is", grade, "Good job!!!")
          scoresdict = {"Name":[name],"Math":[math],"English":[English],"Science":[Science],"Art":[Art],"History":[History],"Geography":[Geo],"Average":[ave],"Grade":[grade]}
          st.write (scoresdict)
          student_table = pd.DataFrame(scoresdict)
          st.table(student_table)
          tablesjoin = pd.concat([readcsv,student_table],ignore_index=True)
          tablesjoin.to_csv('scores.csv',index=False)
          st.success('Student Data Saved')
     else:
          st.error ('please fill in all the boxes')