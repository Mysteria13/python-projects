# create an app for your friends on how much they know you or know something or general quiz
# asks the user to enter his/her name on the questionnaire page
# the questionnaire page can be arranged in 3 or more columns (use your own ideas(-radio - selecbox))
# a button under after all to submit and this checks the right questions and add the scores and save the user score under the user name
# the other page plots the charts of all users who answered and shows their scores
# the app should be able to save the scores in a file and read from it
# import the necessary libraries 
# add points to each individual answer 1
import streamlit as st
import pandas as pd
import plotly.express as px

try :
    readcsv = pd.read_csv('Result.csv')    
except FileNotFoundError:
    readcsv = pd.DataFrame()
st.set_page_config(page_title="General Quiz App", page_icon=":guardswomen:", layout="wide") 
Menu = st.sidebar.selectbox('Choose one', ['Quiz', 'Results'])
if Menu == "Results":
    st.title('Quiz Results')
    total_score = 50
    st.subheader('Total score is 50')
    st.subheader('Scores of all participants')
    st.write('Here are the scores of all participants in the quiz:')
    st.table(readcsv)
    st.subheader('Average Score')
    average_score = readcsv['Scores'].mean()
    st.write(f'The average score of all participants is: {average_score:.2f}')
    st.subheader('Bar Chart of Scores')
    if not readcsv.empty:
        barchart = px.bar(readcsv, x='Name', y='Scores', title='Scores of Participants', labels={'Name': 'Participant Name', 'Score': 'Score'})
        st.plotly_chart(barchart) 
score = 0
if Menu == 'Quiz':
    st.title('Quiz')
    name = st.text_input('Enter Your Name')
    if name == '':
        st.error('Please enter your name to start the quiz.')
    else:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Question 1')
            st.image("")
            st.write('Which city is known as the big apple?') 
            Ny = st.radio('Select yor answer:', ['Choose', 'Miami','New York','London', 'Toronto', 'Chicago'])
            if Ny == 'Choose':
                st.error('Please select a answer.')
            elif Ny == 'New York':
                score += 5
            elif Ny == 'Miami':
                score += 2
            elif Ny == 'London':
                score += 1
            elif Ny == 'Toronto':
                score += 3
            elif Ny == 'Chicago':
                score += 5
            st.subheader('Question 3')
            st.image("")
            st.write('Which Country is known for its pyramids?')
            Et = st.radio('Select your answer:', ['Choose', 'Greece', 'Italy', 'Egypt', 'Mexico', 'India'])
            if Et == 'Choose':
                st.error('Please select a answer.')
            elif Et == 'Egypt':
                score += 5
            elif Et == 'Greece':
                score += 2
            elif Et == 'Italy':
                score += 1
            elif Et == 'Mexico':
                score += 3
            elif Et == 'India':
                score += 4
            st.subheader('Question 5')
            st.image("")
            st.write('What is the largest continent?')
            As = st.radio('Select your answer:', ['Choose', 'Asia', 'Africa', 'Europe', 'North America', 'South America'])
            if As == 'Choose':
                st.error('Please select a answer.')
            elif As == 'Asia':
                score += 5
            elif As == 'Africa':
                score += 2
            elif As == 'Europe':
                score += 1
            elif As == 'North America':
                score += 3
            elif As == 'South America':
                score += 4

        with col2:
            st.subheader('Question 2')
            st.image("")
            st.write('What is the capital of France?') 
            Ps = st.radio('Select your answer:', ['Choose', 'Berlin', 'Madrid', 'Rome', 'Lisbon','Paris'])
            if Ps == 'Choose':
                st.error('Please select a answer.')
            elif Ps == 'Paris':
                score += 5
            elif Ps == 'Berlin':
                score += 2
            elif Ps == 'Madrid':
                score += 1
            elif Ps == 'Rome':
                score += 3
            elif Ps == 'Lisbon':
                score += 4
            st.subheader('Question 4')
            st.image("")
            st.write('Which country is known as the land of the rising sun?')
            Jp = st.radio('Select your answer:', ['Choose', 'China', 'South Korea','Japan', 'Thailand', 'Vietnam'])
            if Jp == 'Choose':
                st.error('Please select a answer.')
            elif Jp == 'Japan':
                score += 5
            elif Jp == 'China':
                score += 2
            elif Jp == 'South Korea':
                 score += 1
            elif Jp == 'Thailand':
                score += 3
            elif Jp == 'Vietnam':
                score += 4


            st.subheader('Question 6')
            st.image("")
            st.write('Which country is known for its kangaroos?')
            Au = st.radio('Select your answer:', ['Choose',  'New Zealand', 'South Africa', 'Canada','Australia', 'United States'])
            if Au == 'Choose':
                st.error('Please select a answer.')
            elif Au == 'Australia':
                score += 5
            elif Au == 'New Zealand':
                score += 2
            elif Au == 'South Africa':
                score += 1
            elif Au == 'Canada':
                score += 3
            elif Au == 'United States':
                score += 4