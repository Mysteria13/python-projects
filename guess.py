#create a guess my number app where users are given 3 attempts to guess your number and you tell them if
#guess is too high or too low or correct
#hint: use random & randint, sessionstate, range, input, if elif else, break()
import random
import streamlit as st
st.title ('Guess the Number App')
st.write ('Guess my number from 1-10')
number = random.randint(1,10)
guess = st.number_input('Please Enter your chosen number',1 , 10) 
if st.button ('Sumbit Guess'):
    if number == guess:
       st.success('Guess was correct')
    elif guess < number:
       st.warning ('Guess was too low Try again')
    elif guess > number:
        st.warning (' Guess was too high Try again')
else:  
    st.error('Enter Guess')

      