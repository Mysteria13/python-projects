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
try:
    seecsv = pd.read_csv('Results.csv')
except FileNotFoundError:
    seecsv = pd.DataFrame()
st.set_page_config(page_title="General Quiz App", page_icon=":guardswomen:", layout="wide") 
Menu = st.sidebar.selectbox('Choose one', ['General Quiz','Personal Quiz', 'Results'])
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
    chart = st.radio("Plot a chart",['Bar','Pie'], horizontal = True)
    if chart == 'Bar':
        st.subheader('Bar Chart of General Quiz Scores')
        if not readcsv.empty:
            barchart = px.bar(readcsv, x='Name', y='Scores', title='Scores of Participants', labels={'Name': 'Participant Name', 'Score': 'Score'})
            st.plotly_chart(barchart) 
    elif chart == 'Pie':
        st.subheader('Pie Chart of  General Quiz Scores')
        if not readcsv.empty:
            piechart = px.pie(readcsv, names='Name', values='Scores',title='Scores of Participants', labels={'Name': 'Participant Name', 'Score': 'Score'})
            st.plotly_chart(piechart)

    st.title ('Personal Quiz Results')
    st.subheader('Total score is 50')
    st.write('Here are the scores of all participants in the Personal quiz:')
    st.table(seecsv)
    st.subheader('Average Score')
    average_scores = seecsv['Score'].mean()
    st.write(f'The average score of all participants is: {average_score:.2f}')
    st.subheader('Bar Chart of Scores')
    charts = st.radio("Plot a chart",['Bars','Pies'], horizontal = True)
    if charts == 'Bars':
        st.subheader('Bar Chart of Personal Quiz Scores')
        if not seecsv.empty:
            barschart = px.bar(seecsv, x='Names', y='Score', title='Scores of Participants', labels={'Name': 'Participant Name', 'Score': 'Score'})
            st.plotly_chart(barschart) 
    elif charts == 'Pies':
        st.subheader('Pie Chart of Personal Quiz Scores')
        if not seecsv.empty:
            pieschart = px.pie(seecsv, names='Names', values='Score',title='Scores of Participants', labels={'Name': 'Participant Name', 'Score': 'Score'})
            st.plotly_chart(pieschart)

    

score = 0
if Menu == 'General Quiz':
    st.title('General Quiz')
    name = st.text_input('Enter Your Name')
    if name == '':
        st.error('Please enter your name to start the quiz.')
    else:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Question 1')
            #st.image("")
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
            #st.image("")
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
            #st.image("")
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
            st.subheader('Question 7')
            #st.image('')
            st.write('Which country is known as the land of thousands of lakes?')
            Fd = st.radio('Select your answer:',['Choose','Sweden','Norway','Finland','Denmark','Iceland'])
            if Fd == 'Choose':
                st.error('Please select a amswer')
            elif Fd =='Norway':
                score += 3
            elif Fd =='Iceland':
                score +=4
            elif Fd =='Denmark':
                score +=1
            elif Fd == 'Finland':
                score +=5
            elif Fd == 'Sweden':
                score += 2
            st.subheader('Question 9')
            #st.image("")
            st.write('Which country is known as the land of cakes?')
            Sc = st.radio('Select your answer:', ['Choose', 'Scotland', 'Ireland', 'England', 'Wales', 'Northern Ireland'])
            if Sc == 'Choose':
                st.error('Please select a answer.')
            elif Sc == 'Scotland':
                score += 5
            elif Sc == 'Ireland':
                score += 2
            elif Sc == 'England':
                score += 1
            elif Sc == 'Wales':
                score += 3
            elif Sc == 'Northern Ireland':
                score += 4
        with col2:
            st.subheader('Question 2')
            #st.image("")
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
            #st.image("")
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
            #st.image("")
            st.write('Which country is known for its kangaroos?')
            Au = st.radio ('Select your Option:', ['Choose',  'New Zealand', 'South Africa', 'Canada','Australia', 'United States'])
            if Au == 'Choose':
                st.error('Please select a Place.')
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
            st.subheader('Question 8')
            #st.image("")
            st.write('Which country is known as the midnight sun?')
            Nw = st.radio ('Select your choice:', ['Choose', 'Sweden', 'Norway', 'Finland', 'Denmark', 'Iceland'])
            if Nw == 'Choose':
                st.error('Please select a choice.') 
            elif Nw == 'Norway':
                score += 5
            elif Nw == 'Sweden':    
                score += 2
            elif Nw == 'Finland':
                score += 1
            elif Nw == 'Denmark':
                score += 3
            elif Nw == 'Iceland':
                score += 4
            st.subheader('Question 10')
            #st.image("")
            st.write('Which country is known as the land of the free?')
            Us = st.radio('Select your or any answer:', ['Choose', 'United States', 'Canada', 'Mexico', 'Brazil', 'Argentina'])
            if Us == 'Choose':
                st.error('Please select an answer.')
            elif Us == 'United States':
                score += 5
            elif Us == 'Canada':
                score += 2
            elif Us == 'Mexico':
                score += 1
            elif Us == 'Brazil':
                score += 3
            elif Us == 'Argentina':
                score += 4
    if st.button ('Submit'):
     if (Ny !='Choose' and Et != 'Choose' and As != 'Choose' and Fd != 'Choose' and Sc != 'Choose' and Ps != 'Choose' and Jp != 'Choose' and Au != 'Choose' and Nw != 'Choose' and Us != 'Choose'): 
              
              if score > 50:
                st.error('Your score cannot be more than 50. Please check your answers.')
              else:
                st.success(f'Thank you {name} for taking the quiz! Your score is: {score}')
                new_data = pd.DataFrame({'Name': [name], 'Scores': [score]})
                readcsv = pd.concat([readcsv, new_data], ignore_index=True)
                readcsv.to_csv('Result.csv', index=False)
                st.balloons()
                st.write('Your score has been saved successfully!') 
                st.write('You can check the results in the Results section.')
                st.write('Thank you for participating in the quiz!')
                st.write('Have a great day!')
     else: 
        st.error ('Please enter all the questions')
elif Menu == 'Personal Quiz':
    st.title('Personal Quiz')
    st.write('Test how well you know me! Answer the questions below to find out.')
    st.write('Each question has a different score based on your answer. Try to get the highest score possible!')
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
                score_dict = {"Names": [name], "Score": [score]}
                score_table = pd.DataFrame(score_dict)
                st.table(score_table)
                tablesjoin = pd.concat([seecsv, score_table], ignore_index=True)
                tablesjoin.to_csv('Results.csv', index=False)
                st.success('Results Saved')
            else:
                st.error('Please answer all questions before submitting.')