###simple test


###write a program for a use
##ask for the name and -age - use a radio to ask for gender
##use a selectbox to ask to choose best color - use a type to ask best game

#use a type to ask to type best movie - use a type to ask best friend
#create a submit button and show this in a success bar
#Jeida (F), your best game is: Minecraft, Color: Blue, Movie: Spiderman, Friend: Tofe###
import streamlit as st 

st.title(' Memory App made by Lisa')

name = st.text_input('Please enter your name') 
age = st.number_input('Please enter your age',0)
gender = st.radio("chooose gender",['male', 'female'], horizontal=True)
Colour =st. selectbox ("Choose any colour",['Blue','Purple','Gold','Green','Silver','Red','Pink','Black'])
game = st.text_input('Please enter your best game') 
movie = st.text_input('Please enter your best movie') 
Best_friend= st.text_input('Please enter your best friend name') 
if st.button ("Sumbit"):
    st.write(name,gender,"your best game is:",game,"Colour:",Colour,"Movie:",movie,"Friend:",Best_friend,)



