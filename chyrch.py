import streamlit as st 

st.title(' Church Age App made by Lisa')
col1, col2, col3 = st.columns(3)
with col1:
      name = st.text_input('Please enter your name')
with col2:
     age = st.number_input('Please enter your Age',3)
with col3:
  Gen = st.text_input('Please enter your gender')
if st.button (" Submit"):
  st.write (name,"Welcome to your group" )
  if age < 3:
    st.write ("Sorry your not old enough to be in the childrens church")
  elif age > 3 and age < 13:
      st.write ("The Kids group")
  elif age > 12 and age < 20:
      st.write ("The Teens group ")
  elif age > 19 and age < 36:
      st.write ("The Youth group ")
  elif age > 35 and age <= 64:
      st.write ("The Adult group ")
  elif age > 64:
      st.write ("The Elderly group ")