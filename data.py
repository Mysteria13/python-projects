#A teacher wants to track the attendance of students in their class for a week. Create a Python program to collect, save, and analyze attendance records.
#Create a New File
#Ask the teacher to submit the following details for each student:
#Student Name
#Roll Number
#Total Days Present
#Total Days Absent
#Save these details in a CSV file. (20 marks)
#Display the Dictionary Representation
#Show the dictionary of all attendance records. (20 marks)
#Display the Table Representation
#Display the collected data in a table format. (5 marks)
#Show the Table from the CSV File
#Display the first 10 saved responses from the CSV file. (10 marks)
#Plot a Bar Chart
#Plot a bar chart with the students’ names on the x-axis and their total days present on the y-axis. (20 marks)
import streamlit as st
import pandas as pd
import plotly_express as px
menu = st.sidebar.selectbox('Pick setting',['Info','Results'])
readcsv = pd.read_csv('data.csv')

col1,col2 = st.columns(2)

if menu == 'Results':
    st.table(readcsv)
    days = ['Present','Absent']
    daystable = readcsv[days].mean().reset_index()
    barchart = px.bar(daystable,x='index',y=0,labels={'index':'Days','0':'Amount'}) 
    st.plotly_chart(barchart)    
    
if menu == 'Info':
    with col1:
        name = st.text_input ('Please enter student name:')
        roll = st.number_input ('Please enter Students Roll Number',0)
    with col2:
        present = st.number_input ('Please enter number of days Present',0)
        absent = st.number_input ('Please enter number of days Absent',0)
    if st.button("Save Student Data"):
        if name and roll and present and absent:
            st.write (name,'is roll number',roll,'and has been present for',present,'days.And has been absent for',absent,'days')
            datadict ={"Student":[name],"Number":[roll],"Present":[present],"Absent":[absent]}
            st.write(datadict)
            data_table = pd.DataFrame(datadict)
            st.table(data_table)
            tablesjoin = pd.concat([readcsv,data_table],ignore_index=True)
            tablesjoin.to_csv('data.csv',index=False)
            st.success("Student Data Saved")
        else:
          st.error ('please fill in all the boxes')