import streamlit as st #this is a framework/page for your python app to run

st.title('Age Caculator App made by Lisa')#big text

name = st.text_input('Please enter your name') #text_input is to ask  for texts or strings

yob = st.number_input('Please enter your year of birth',0)#number_input is when you want to ask forma

currentyear = st.number_input('Please enter the current year',0)

age = currentyear - yob 

if st.button("Check Age"): #check if this button called age is clicked
    st.write(name,'you wiil be',age,'year old in' ,currentyear) # do this
    # the space in front is indentation (only run this when code above is true)