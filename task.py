#Employee Task Tracker
#A manager wants to track the tasks assigned to employees in their department for a month. Create a Python program to collect, save, and analyze task records.
#create a New File
#ask the manager to submit the following details for each employee:
#Employee Name
#Employee ID
#Task Assigned
#Due Date
#Task Status (Completed/Incomplete)
#Save these details in a CSV file. (20 marks)
#Display the Dictionary Representation
#Show the dictionary of all task records. (20 marks)
#Display the Table Representation
#Display the collected data in a table format. (5 marks)
#Show the Table from the CSV File
#Display the first 10 saved responses from the CSV file. (10 marks)
#Plot a Bar Chart
#Plot a bar chart with the employee names on the x-axis and the number of tasks completed on the y-axis. (20 marks)
import streamlit as st
import pandas as pd

try:
    readcsv = pd.read_csv('task.csv')
except:
   readcsv = pd.DataFrame()

menu = st.sidebar.selectbox('Pick Setting',['Info','Results'])
col1,col2 = st.columns(2)
if menu == 'Results':
   st.table(readcsv)





if menu == 'Info':
    with col1:
     name = st.text_input ('Enter employee name:')
     ID = st.text_input  ("Enter employee ID:")
    with col2:
       task = st.text_input ('Enter task assigned:') 
       date = st.date_input ('Enter due date:')
       record = st.radio ('Task Status',['Completed','Incompleted'])
       
       taskdict = {'Id':[ID],'Name':[name],'Task':[task],'Due':[date],'Status':[record]}
       taskdataframe = pd.DataFrame (taskdict)
       st.table(taskdataframe)
       tablesjoin = pd.concat ([readcsv,taskdataframe],ignore_index=True)
       tablesjoin.to_csv('task.csv',index = False)
       st.success ('Info Saved')