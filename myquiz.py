# create an app for your friends on how much they know you or know something or general quiz
# asks the user to enter his/her name on the questionnaire page
# the questionnaire page can be arranged in 3 or more columns (use your own ideas(-radio - selecbox))
# a button under after all to submit and this checks the right questions and add the scores and save the user score under the user name
# the other page plots the charts of all users who answered and shows their scores
# the app should be able to save the scores in a file and read from it
# import the necessary libraries 
# add points to each individual answer
import streamlit as st
import pandas as pd
import plotly.express as px
try:
   readcsv = pd.read_csv('Results.csv')
except:
   readcsv = pd.DataFrame()
st.set_page_config(page_title="My Quiz App", page_icon=":guardsman:", layout="wide")
Menu = st.sidebar.selectbox('Choose one',['Quiz','Results'])
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
         st.image("color.png")
         st.write('What is my favorite color?') 
         color = st.radio('Select my favorite color:', ['Choose','Red', 'Green', 'Blue', 'Yellow', 'Purple'])
         if color == 'Choose':
            st.error('Please select a color.')
         elif color == 'Red':
            score += 4
         elif color == 'Green':
            score += 2
         elif color == 'Blue':
            score += 1
         elif color == 'Yellow':
            score += 3
         elif color == 'Purple':
            score += 5

         st.subheader('Question 3')
         st.image("images.jpg")
         st.write('What is my favorite subject?')
         subject = st.radio('Select my favorite subject:', ['Choose','Math', 'Science', 'History', 'Geography', 'English'])
         if subject == 'Choose':
            st.error('Please choose a subject')
         elif subject == 'Math':
            score += 5
         elif subject == 'Science':
            score += 4
         elif subject == 'History':
            score += 3
         elif subject == 'Geography':
            score += 1
         elif subject == 'English':
            score += 2

         st.subheader('Question 5')
         st.image("book (1).jpg")
         st.write('What is my favorite book')
         book = st.radio('Select my favourite book:', ['Choose','Harry Potter', 'The Hobbit', 'Things Fall Apart', 'From Sharkdog to Nightowl',  'The Lion, The Witch and The Wardrobe'])
         if book == 'Choose':
            st.error('Please select a book.')
         elif book == "The Hobbit":
            score += 1
         elif book == 'Harry Potter':
            score += 5
         elif book == 'Things Fall Apart':
            score += 2
         elif book == 'From Sharkdog to Nightowl':
            score += 4
         elif book == 'The Lion, The Witch and The Wardrobe':
            score += 3

         st.subheader('Question 7')
         st.image('animal.jpg')
         st.write('What is my favorite animal?')
         animal = st.radio('Select my favorite animal:', ['Choose','Dog', 'Owl', 'Elephant', 'Lion', 'Tiger'])
         if animal == 'Choose':
            st.error('Please select an animal.')
         elif animal == 'Dog':
            score += 3
         elif animal == 'Owl':
            score += 5
         elif animal == 'Elephant':
            score += 2
         elif animal == 'Lion':
            score += 1
         elif animal == 'Tiger':
            score += 4

         st.subheader('Question 9')
         st.image('place.jpg')
         st.write('What is my favorite place?')
         place = st.radio('Select my favorite place:', ['Choose','Beach', 'Mountains', 'City', 'Forest', 'Desert'])
         if place == 'Choose':
            st.error('Please select a place.')
         elif place == 'Beach':
            score += 5
         elif place == 'Mountains':
            score += 4
         elif place == 'City':
            score += 3
         elif place == 'Forest':
            score += 2
         elif place == 'Desert':
            score += 1

      with col2:
         st.subheader('Question 2')
         st.image('sport.jpg')
         st.write('What is my favorite sport?')
         sports = st.radio('Select my favourite sport:',['Choose','Basketball','Swimming','Horse Riding','Volleyball','Running'])
         if sports == 'Choose':
            st.error('Please select a sport.')
         elif sports == "Horse Riding":
            score += 1
         elif sports == 'Basketball':
            score += 4
         elif sports == 'Swimming':
            score += 5
         elif sports == 'Volleyball':
            score += 3
         elif sports == 'Running':
            score += 2

         st.subheader('Question 4') 
         st.image('food.jpg') 
         st.write('What is my favorite food?')
         food = st.radio('Select my favorite food:', ['Choose','Jollof Rice','Fried Rice','Spagetti','Indomie','Plaintain'] )
         if food == 'Choose':
            st.error('Please select a food')
         elif food == "Jollof Rice":
            score += 2
         elif food == 'Fried Rice':
            score += 3
         elif food == 'Spagetti':
            score += 5
         elif food == 'Indomie':
            score += 4
         elif food == 'Plaintain':
            score += 1

         st.subheader('Question 6')
         st.image('movie.jpg')
         st.write('What is my favorite movie?')
         movie = st.radio('Select my favorite movie:', ['Choose','The Lion King', 'Titanic', 'Avatar', 'Rush Hour', 'Spy Kids'])
         if movie == 'Choose':
            st.error('Please select a movie')
         elif movie == 'The Lion King': 
            score += 2
         elif movie == 'Titanic':
            score += 1
         elif movie == 'Avatar':
            score += 3
         elif movie == 'Rush Hour':
            score += 5
         elif movie == 'Spy Kids':
            score += 4

         st.subheader('Question 8')
         st.image('drink.jpg') 
         st.write('What is my favorite drink?')
         drink = st.radio('Select my favorite drink:', ['Choose','Coke', 'Fanta', 'Sprite', 'Pepsi', 'Water'])
         if drink == 'Choose':
            st.error("Please select a drink")
         elif drink == 'Coke':
            score += 2
         elif drink == 'Fanta':
            score += 5
         elif drink == 'Sprite':
            score += 4
         elif drink == 'Pepsi':
            score += 3
         elif drink == 'Water':
            score += 1

         st.subheader('Question 10')
         st.image('dessert.jpg')
         st.write('What is my favorite dessert?')
         dessert = st.radio('Select my favorite dessert:', ['Choose','Ice Cream', 'Cake', 'Brownie', 'Pudding', 'Pie'])
         if dessert == 'Choose':
            st.error('Please select a dessert.')
         elif dessert == 'Ice Cream':
            score += 4
         elif dessert == 'Cake':
            score += 5
         elif dessert == 'Brownie':
            score += 2
         elif dessert == 'Pudding':
            score += 3
         elif dessert == 'Pie':
            score += 1

      if st.button('Submit'):
         if (color != 'Choose' and sports != 'Choose' and food != 'Choose' and subject != 'Choose' and book != 'Choose' and animal != 'Choose' and place != 'Choose' and movie != 'Choose' and drink != 'Choose' and dessert != 'Choose'):
            st.success('Quiz submitted successfully!')
            st.write(name, 'Your score is:', score)
            if score >= 50:
               st.success('You have amazing taste')
            elif score >= 40:
               st.warning('You have decent taste.')
            elif score >= 30:
               st.warning('You have an okay taste.')
            else:
               st.error('You need to replace your bad tastes.')
            score_dict = {"Name": [name], "Scores": [score]}
            score_table = pd.DataFrame(score_dict)
            st.table(score_table)
            tablesjoin = pd.concat([readcsv, score_table], ignore_index=True)
            tablesjoin.to_csv('Results.csv', index=False)
            st.success('Results Saved')
         else:
            st.error('Please answer all questions before submitting.')