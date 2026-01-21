#At Greenfield Academy, the sports department is keeping a Sports Performance Database for all students who participated in the annual inter-house competition.
#For each student, they want to record scores for:
#100m Sprint
# Long Jump
#Shot Put
#High Jump
#The sports coordinator’s job is to:
#Enter the student’s name into the database.
#Type in the scores for all four events.
#Calculate:
#Total score
#Average score
#Performance Level (A: 70+, B: 60–69, C: 50–59, E: below 50)
#Save the record so it appears when “View Database” is selected.
#💻 Your Task
#Using the program:
#Open the app and go to “Input Student Score”.
#Type the name of the athlete and their four event scores.
#Click Submit student score to save it.
#Switch to “View Database” to see the performance records of all athletes.
import streamlit as st
import pandas as pd
try:
    readcsv = pd.read_csv ('mark.csv')
    st.write(readcsv)
except:
    readcsv = pd.DataFrame()
    st.write(readcsv)
menu = st.sidebar.selectbox('Menu', [ 'Enter Info', 'View Database'])
if menu == "View Database":
    #st.table(readcsv)
    sports = ["Sprint","Long Jump","Shot Put","High Jump"]
    sportstable = readcsv[sports].mean().reset_index()
if menu == 'Enter Info':
    name = st.text_input('Enter the name of the Student')
    col1,col2 = st.columns(2)
    with col1:
        sprint = st.number_input('Enter the student sprint score', min_value=0, max_value=100, value=0)
        long_jump = st.number_input('Enter the student long jump score', min_value=0, max_value=100, value=0)
    with col2:
        shotput = st.number_input('Enter the student shot put  score', min_value=0, max_value=100, value=0)
        high_jump = st.number_input('Enter the student high jump score', min_value=0, max_value=100, value=0)
    Total = sprint + long_jump + shotput + high_jump
    ave = Total/4
    if ave >= 70:
        grade = 'A'
    elif 60 >= ave <= 69:
        grade = 'B'
    elif 50 >= ave <= 59:
        grade = 'C'
    elif 40 >= ave <= 49:
        grade = 'D'
    elif ave <= 39:
        grade = 'F'
    if st.button ("Save student scores"):
          if name and sprint and long_jump and shotput and high_jump:
           st.write (name,"your total score is",Total,"average is",ave,"grade is",grade, "Good job!!!")
          marksdict = {"Name":[name],"Sprint":[sprint],"Long Jump":[long_jump],"Shot Put":[shotput],"High Jump":[high_jump],"Average":[ave],"Grade":[grade],"Total":[Total]}
          st.write (marksdict)
          mark_table = pd.DataFrame(marksdict)
          #st.table(mark_table)
          tablesjoin = pd.concat([readcsv,mark_table],ignore_index=True)
          tablesjoin.to_csv('mark.csv',index=False)
          st.success('Student Scores Saved')
    else:
          st.error ('please fill in all the boxes')
        
        
    