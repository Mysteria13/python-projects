import streamlit as st
import pandas as pd
st.title('Event Registation Form')
st.subheader('Info about event')
col1,col2,col3 = st.columns(3)
with col1:
    en = st.write('Event Name:')
    D = st.write('Date:')
    T = st.write('Time:')
    S = st.write('Speaker:')
with col2:
    Event_name = st.write('Robotics Science Masterclass')
    Date = st.write('3rd Febuary 2026')
    Time = st.write('2pm - 5pm')
    Speaker = st.write ('Alexander Thorne(Robotics Science Expert)')
with col3:
    st.write()

st.divider()
st.subheader('Participant Information')
col3,col4 = st.columns(2)
with col3:
    name = st.text_input('Enter your Full Name: ')
with col4:
    dob = st.date_input ('Enter Your Date of Birth:')
col5,col6,col7 = st.columns(3)
with col5:
    Gen = st.radio('Gender',['Male','Female'])
with col6:
    phone = st.number_input('Please enter your phone number',0)
with col7:
    email = st.text_input('Please enter your email:')
hear = st.radio('Where did you hear about the event from:',['Facebook','Twitter','Instagram','Youtube','Other'],horizontal=True)
st.divider