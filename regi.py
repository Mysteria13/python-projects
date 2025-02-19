#create 2 menu pages
#PAGE 1 
#for USER REGISTRATION PAGE WITH FILLING OF INFOMATION:
#-IMAGE UPLOAD
#-name -email
#-number - country -state
#PAGE 2
#THEN A PAGE TO SHOW USER INFORMATION AFTER LOGIN (PICTURE ETC)
#This will be for each user
import streamlit as st
menu = st.sidebar.selectbox ('Choose an option',['Registration','Info'])

if menu == 'Registration':
    uploadimage = st.file_uploader('Please Upload Your Profile Picture',type=['jpg','jpeg','png'])
    col1,col2=st.columns(2)
    with col1:
       Name = st.text_input ('Enter your name')
       Email = st.text_input ('Enter your Email')
    with col2:
        num = st.text_input('Enter your phone number')
        country = st.text_input('Enter your country')
        state = st.text_input('Enter your state')
if st.button ('Sumbit'):
    st.success('Info Saved') 