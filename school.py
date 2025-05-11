#Design an app for a school to register them
#Students can use their username and password to view their page
#Registration:
#-where the school can upload their profile picture
#seperate student and parent information by columns
#-student information
#- studentID
#-first and last names
#-grade (selectbox)
#-gender (radio)
#-DOB (date_input)
#-student email
#-parent name
#-parent contact
#-Parent email
#-address
#remove home from the menu entirely
#put a notification if username not found or password incorrect or button pressed with no details
#all tables not needed to be shown
#use the username provided in the registration to login


import streamlit as st
import pandas as pd

# Load or initialize the CSV file
try:
    readcsv = pd.read_csv('school.csv')
    st.write(readcsv)
except FileNotFoundError:
    readcsv = pd.DataFrame()
    st.write(readcsv)

# Sidebar menu
menu = st.sidebar.selectbox('Menu', ['Register', 'Login'])

if menu == 'Register':
    st.title('Register')
    st.subheader('Student Information')

    # Profile picture upload
    profile_pic = st.file_uploader('Upload Profile Picture', type=["png", "jpg", "jpeg"])
    if profile_pic:
        st.image(profile_pic, width=300)

    # Student information inputs
    userid = st.text_input('Student ID')
    first_name = st.text_input('First Name')
    last_name = st.text_input('Last Name')
    grade = st.selectbox('Grade', ['Grade 6', 'Grade 7', 'Grade 8', 'Grade 9', 'Grade 10', 'Grade 11', 'Grade 12'])
    gender = st.radio('Gender', ['Male', 'Female'], horizontal=True)
    dob = st.date_input('Date of Birth')
    student_email = st.text_input('Student Email')
    address = st.text_input('Address')
    username = st.text_input('Create Username')
    password = st.text_input('Create Password', type='password')

    # Parent information inputs
    st.subheader('Parent Information')
    parent_name = st.text_input('Parent Name')
    parent_contact = st.text_input('Parent Contact')
    parent_email = st.text_input('Parent Email')
    relation = st.selectbox('Relation', ['Father', 'Mother', 'Guardian'])

    # Submit button
    if st.button('Submit'):
        if not all([userid, first_name, last_name, username, password]):
            st.warning('Please fill in all required fields.')
        else:
            student_data = {
                'Student ID': [userid],
                'First Name': [first_name],
                'Last Name': [last_name],
                'Grade': [grade],
                'Date of Birth': [dob],
                'Gender': [gender],
                'Address': [address],
                'Student Email': [student_email],
                'Parent Name': [parent_name],
                'Parent Contact': [parent_contact],
                'Parent Email': [parent_email],
                'Relation': [relation],
                'Username': [username],
                'Password': [password]
            }
            student_table = pd.DataFrame(student_data)
            updated_data = pd.concat([readcsv, student_table], ignore_index=True)
            updated_data.to_csv('school.csv', index=False)
            st.success('Registration Successful')
            st.balloons()

elif menu == 'Login':
    st.title('Login')

    # Login inputs
    username = st.sidebar.text_input('Username')
    password = st.sidebar.text_input('Password', type='password')

    if st.sidebar.button('Login'):
        if username == '' or password == '':
            st.warning('Please enter both username and password.')
        else:
            user_data = readcsv[readcsv['Username'] == username]
            if user_data.empty:
                st.error('Username not found.')
            elif user_data['Password'].iloc[0] != password:
                st.error('Incorrect password.')
            else:
                st.success('Login Successful')
                st.write(f"Welcome, {user_data['First Name'].iloc[0]} {user_data['Last Name'].iloc[0]}")
                st.write(f"Grade: {user_data['Grade'].iloc[0]}")
                st.write(f"Date of Birth: {user_data['Date of Birth'].iloc[0]}")
                st.write(f"Gender: {user_data['Gender'].iloc[0]}")
                st.write(f"Address: {user_data['Address'].iloc[0]}")
                st.write(f"Student Email: {user_data['Student Email'].iloc[0]}")
                st.write(f"Parent Name: {user_data['Parent Name'].iloc[0]}")
                st.write(f"Parent Contact: {user_data['Parent Contact'].iloc[0]}")
                st.write(f"Parent Email: {user_data['Parent Email'].iloc[0]}")
                st.write(f"Relation: {user_data['Relation'].iloc[0]}")
