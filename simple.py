import streamlit as st
col1, col2 = st.columns(2)
with col1:
      name = st.text_input('Please enter your name')
with col2:
     age = st.number_input('Please enter your age',0)
     if st.button("Submit"):
      st.write("Hello",name,"you are now",age,"congratulations!!!!!")