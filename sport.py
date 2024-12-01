import streamlit as st
st.title('Sport App made by Lisa')
name = st.text_input ("Please enter your name:")
favourite_sport =st.text_input("Please enter your favourite_sport")
favourite_team =st.text_input("Please enter your favourite_team")
favourite_player =st.text_input("Please enter your favourite_player") 
("Hi", name, "Your favorite sport is " ,favourite_sport, "you cheer for" ,favourite_team, "and your favourite player is" ,favourite_player)