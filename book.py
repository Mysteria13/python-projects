import streamlit as st
st.title('Book App made by Lisa')
name = st.text_input ("Please enter your name:")
favourite_book =st.text_input("Please enter your favourite_book")
favourite_character =st.text_input("Please enter your favourite_character")
favourite_part =st.text_input("Please enter your favourite_part") 
("Hi" ,name, "Your favourite book is", favourite_book, "you love the character" ,favourite_character, "and your favorite part is", favourite_part)
