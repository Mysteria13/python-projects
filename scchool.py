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
#put profile picture with the login info page
#put a notification if username not found or password incorrect or button pressed with no details
#all tables not needed to be shown
#use the username provided in the registration to login
import streamlit as st
import pandas as pd
try:
    readcsv = pd.read_csv('school.csv')
    st.write(readcsv)
except:
    readcsv = pd.DataFrame()
    st.write(readcsv)
menu = st.sidebar.selectbox('Menu', [ 'Register', 'Login'])
if menu == 'Register':
    st.title('Register')
    st.subheader('Student Information')
    profile_pic = st.file_uploader('Upload Profile Picture')
    if profile_pic:
        st.image(profile_pic, width = 300)
    userid = User = st.text_input('Student ID')
    if userid:
        st.image(f'{userid}.png')
        st.success('Profile picture uploaded successfully!')
    
    profile_pic = st.file_uploader("Upload a new profile picture", type=["png", "jpg", "jpeg"])
    if st.button('Save Picture'):
       if profile_pic:
            picname = f'{userid}.png'
            with open(picname, 'wb') as f:
                f.write(profile_pic.getbuffer())
            st.success("Profile picture updated successfully!")
    col1,col2, = st.columns(2)
    
    with col1:
        first_name = st.text_input('First Name')
        gender = st.radio('Gender', ['Male', 'Female'], horizontal = True)
        grade = st.selectbox('Grade', ['Grade 6','Grade 7', 'Grade 8', 'Grade 9', 'Grade 10', 'Grade 11', 'Grade 12'])
        User =st.text_input('Please create Username')
    with col2:
        Lock = st.text_input('Please Create password ',type = 'password')
        last_name = st.text_input('Last Name') 
        DOB = st.date_input('DOB')
        student_email = st.text_input('Student Email')
    
    address = st.text_input('Address')
    st.subheader('Parent Information')
    cl1,cl2= st.columns(2)
    with cl1:
        parent_contact = st.text_input('Parent Contact')
        parent_email = st.text_input('Parent Email')
    with cl2:
        parent_name = st.text_input('Parent Name')
        relation= st.selectbox('Relation', ['Father', 'Mother', 'Guardian'])
    if st.button('Submit'):
        student_data = { 'First Name': [first_name], 'Last Name': [last_name], 'Grade': [grade] , 'Date of Birth':[DOB] ,'Gender':[gender] , 'Address': [address], 'Student Email': [student_email],'Parent Name': [parent_name], 'Parent Contact': [parent_contact], 'Parent Email': [parent_email], 'Relation': [relation],'Username':[User],'Password':[Lock]}
        st.write(student_data)
        student_table = pd.DataFrame(student_data )
        #st.table(student_table)
        tablesjoin = pd.concat([readcsv, student_table], ignore_index=True)
        tablesjoin.to_csv('school.csv', index=False)
        st.success('Registration Successful')
        st.balloons() 
elif menu == 'Login':
    username = st.sidebar.text_input('Username')
    password = st.sidebar.text_input('Password', type='password')
    adpass = 'Admin'
    searchuser = readcsv[readcsv['Username'] == username]
    if username == 'Username':
        st.warning('Invalid username. Please try again.')
        
    if username == '':
        st.warning('Please enter your username')
    if password == '':
        st.warning('Please enter your password')
    if st.sidebar.button('Login'):
        if password == adpass:
            searchuser = readcsv[readcsv['Username'] == username]
            #st.table(searchuser)
        
            if not searchuser.empty:
                getfn = searchuser['First Name'].iloc[0]
                getln = searchuser['Last Name'].iloc[0]
                st.title(f"{getfn} {getln}") 
                st.success('Login Successful')
                st.balloons()
                st.subheader('Profile Picture')
                profile_pic = f'{username}.png'
                try:
                    with open(profile_pic, 'rb') as f:
                        st.image(f, width=300)
                except FileNotFoundError:
                    st.warning("Profile picture not found.")

                col1, col2,col3 = st.columns(3)
                with col1:
                    st.subheader('Personal Information')
                    getDob = searchuser['Date of Birth'].iloc[0]
                    st.write('Date of Birth:', getDob)
                    getgen = searchuser['Gender'].iloc[0]
                    st.write('Gender:', getgen)
                    getadm = searchuser['Address'].iloc[0]
                    st.write('Address:', getadm)
                with col2:
                    st.subheader('Academic Information')
                    getgrade = searchuser['Grade'].iloc[0]
                    st.write('Grade:', getgrade)
                    getsemail = searchuser['Student Email'].iloc[0]
                    st.write('Student Email:', getsemail)
                with col3:
                    st.subheader('Parent Information')
                    getrel = searchuser['Relation'].iloc[0]
                    getpname = searchuser['Parent Name'].iloc[0]
                    st.write(f"{getrel} Name:", getpname)
                    getpemail = searchuser['Parent Email'].iloc[0]
                    st.write(f"{getrel} Email:", getpemail)
                    getpcontact = searchuser['Parent Contact'].iloc[0]
                    st.write(f"{getrel} Contact:", getpcontact)
                    
            else:
                st.error('No user found with the provided username.')




