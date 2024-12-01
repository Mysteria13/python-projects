import streamlit as st
menu = st.sidebar.selectbox("Choose menu",['Homepage','Database','Contact us'])
if menu == 'Homepage':
    st.subheader("HOMEPAGE")
elif menu =='Contact us':
    st.subheader('CONTACT US')
elif menu =='Database':
    st.subheader('DATABASE')
color = 'purple'
# how do you store mutiple items in one variable
#DATA COLLECTIONS
# -list
games = ['roblox , gta, call of duty']
st.write(games)
#SELECTBOX
#this is used to give users mutiple options in a box to choose from
animal =st. selectbox ("Choose any animal",['cat' , 'dog','donkey','hyena','elephant','snake','lion','tiger'])
st.write ('the animal you selected was', animal)
#radio 
#this is used to give users mutiple options to select from doesnt show in a box , so use little options
gender = st.radio("chooose gender",['male', 'female'], horizontal=True)

st.write ('you are a',gender)

#MENU
#this is used to select from one page to another 


