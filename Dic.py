import streamlit as st
name = st.text_input('Please enter Student name')
age = st.number_input('Enter your age',0)
year=st.selectbox("input your year",["year1","year2","year3"])
if st.button ("send results"):
    dic = {"name":[name],"age":[age],"year":[year]}
    st.write(dic)
    st.table(dic)