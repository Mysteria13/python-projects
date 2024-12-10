import streamlit as st 
import pandas as pd
st.title(' Student database App ')

menu = st.sidebar.selectbox("Choose an option",["input scores","scores database"])

try: #attempt to do what is below 
   readcsv = pd.read_csv('scores.csv')
except:#if there is an error in the above attempt then do this
     readcsv = pd.DataFrame()#create an empty dataframe for me

     #csv : comma seperated values
#menu page to only show the table 
if menu == "scores database":
    st.table(readcsv)
     
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
          st.write (name,"your total score is",Total,"average is",ave,"grade is", grade, "Good job!!!")
          scoresdict = {"Name":[name],"Math":[math],"Science":[Science],"Art":[Art],"History":[History],"Geography":[Geo],"Average":[ave],"Grade":[grade]}
          st.write (scoresdict)
          student_table = pd.DataFrame(scoresdict)
          st.table(student_table)
          tablesjoin = pd.concat([readcsv,student_table],ignore_index=True)
          tablesjoin.to_csv('scores.csv',index=False)
          st.success('Student Data Saved')