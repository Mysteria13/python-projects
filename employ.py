import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')
try:
   readcsv = pd.read_csv('employ.csv')
   #st.write(readcsv)
except FileNotFoundError:
   readcsv = pd.DataFrame()
   #st.write(readcsv)
staff_id = f'Staff_{len(readcsv) + 1}'

menu = st.sidebar.selectbox('Menu',['Register Staff','Staff Database','Staff File'])
if menu == 'Staff Database':
   st.header('List Of Employees')
   st.table(readcsv)

if menu == 'Register Staff':
   st.title('Register Staff')
   col1,col2 = st.columns(2)
   with col1:
      name = st.text_input ('First Name')
      email = st.text_input ('Email Address')
   with col2:
      lname = st.text_input ('Last Name')
      gen = st.selectbox ('Gender',['Male','Female'])
   dep = st.selectbox ('Department',['Select','Management','Operations','Marketing/Sales','Finance','Research and Development'])
   jobt = st.selectbox ('Job Title',['Select','Financial Analyst',' Brand Manager','Logistics Coordinator/Supervisor','Laboratory Technician','Board of Directors'])
   col3,col4 = st.columns(2)
   with col3:
      consta = st.selectbox ('Contract Status',['Select','Intern','Part-time','Full-time'])
   with col4:
      moninc = st.number_input ('Monthly Income',0)
   edu = st.selectbox ('Educational Degree',['None','Bachelors Degree','Masters Degree','PhD/Doctorate'])
   if st.button('Submit Registrations'):
      if not all([name,email,lname]):
            st.warning('Please fill in all required fields.')
      else:
         st.success('Registration Complete')
         st.balloons()
         em_dict= {'Staff ID':[staff_id],'First Name':[name],'Email':[email],'Last Name':[lname],'Gender':[gen],'Department':[dep],'Job Title':[jobt],'Contract Status':[consta],'Monthly Income':[moninc],'Educational Degree':[edu]}
         em_table = pd.DataFrame(em_dict)
         tablesjoin = pd.concat([readcsv,em_table],ignore_index=True)
         tablesjoin.to_csv('employ.csv',index=False)
if menu == 'Staff File':
   cl1,cl2,cl3 = st.columns(3)
   with cl2:
      findem = st.text_input('Enter Staff ID')
      findem_button = st.button('Find Staff')

   if findem_button:
      findemressult = readcsv[readcsv['Staff ID'].str.lower() == findem.lower()]
      #st.write(findemressult)
      if findemressult.empty:
         st.error('Staff ID Not Found, Kindly Double Check ID')
         st.stop()

      else:
         g1,g2,g3= st.columns(3)
         with g1:
            st.info(f'{findemressult['First Name'].iloc[0]} {findemressult['Last Name'].iloc[0]}')
         st.subheader('Personal Informaton')
         st.divider()
         get1,get2,get3 = st.columns(3)
         with get1:
            st.write(f'Email: {findemressult['Email'].iloc[0]}')
         with get2:
            st.write(f'Gender: {findemressult['Gender'].iloc[0]}')
         with get3:
            st.write(f'Degree: {findemressult['Educational Degree'].iloc[0]}')
         st.divider()
         st.subheader('Job Information')
         st.divider()
         get4,get5,get6 = st.columns(3)
         with get4:
            st.write(f'Department: {findemressult['Department'].iloc[0]}')
         with get5:
             st.write(f'Job Title: {findemressult['Job Title'].iloc[0]}')
         with get6:
            st.write(f'Staff ID: {findemressult['Staff ID'].iloc[0]}')
         st.divider()
         get7,get8,get9 = st.columns(3)
         with get7:
            st.write(f'Contract Status: {findemressult['Contract Status'].iloc[0]}')
         with get8:
            st.write(f'Salary: {findemressult['Monthly Income'].iloc[0]:,}')
