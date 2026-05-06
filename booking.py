import streamlit as st
from streamlit_calendar import calendar
import pandas as pd
from datetime import datetime
st.info('Book An Appointment With Mr. Tee')

try:
   bookings = pd.read_csv('bookings.csv')
except:
   bookings = pd.DataFrame()

st.sidebar.subheader('Book A Class')

name = st.sidebar.text_input('Name Please')

choosedate = st.sidebar.date_input('Choose date')
timeslots = [f'{i}:00' for i in range(8,25)]
choosetime = st.sidebar.selectbox('Choose a timeslot',timeslots)
if st.sidebar.button('Book a Slot'):
    booking_dict = {'Name': [name],'Date': [choosedate],'Time': [choosetime]}
    new_booking = pd.DataFrame(booking_dict)
    new_booking.to_csv('bookings.csv',mode='a',index= False,header=bookings.empty)
    st.table(bookings)

events = []
for i in range(len(bookings)):
    get_name = bookings.loc[i,'Name']
    get_date = bookings.loc[i,'Date']
    get_time = bookings.loc[i,'Time']

    start_date = datetime.strftime(f'{get_date} {get_time}',"%y-%m-%d %H:%M")
