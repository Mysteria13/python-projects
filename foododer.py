"""
-Add a restaurant picture
-Create a restaurant app that welcomes users and shows them the food selections
-If they choose/select their meals, show them the total amount
-Ask a question if you want to share the bill with others #use checkbox
-if yes, then ask how many people want to share the bill
-Then show the amount each person must contribute to pay the bill
Food Category (4 items each)
Fruits Category (4 items each)
Drinks Category (4 items each)
"""
import streamlit as st 
#st.set_page_config(layout='wide')

st.title('Food order App made by Lisa')
st.image("https://images.immediate.co.uk/production/volatile/sites/30/2022/11/Meze-style-sharing-board-2f05456.jpg")


food1,food2,food3= st.columns(3)

with food1:
   st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTEqToTwxmIDdgCDvdd770cIYfqhpcdBGBog&s')
   
with food2:
    fcp = 15
    st.subheader('Fish and Chips: $15')
with food3:
    fish = st.number_input('Enter amount of items',0)    
    food = fcp * fish 

st.divider()
fruit1,fruit2,fruit3= st.columns(3)

with fruit1:
  st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCjHab768bbU_DZcFFVZvgCd2rF78gATyX0w&s')
with fruit2:
    sgp = 5
    st.subheader('Strawberry and Grapes: $5')
with fruit3:
    strawgrape = st.number_input ("Enter Amount of item",0)
    fruit = sgp * strawgrape
   
st.divider()
drink1,drink2,drink3= st.columns(3)

with drink1:
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaViYPzmovnFyqFbfdPrSmbifi-1ZCncvRCQ&s')

with drink2:
    fsp = 15
    st.subheader('Fruit Smoothie: $15')
with drink3:
    smoothie = st.number_input("Enter amount of item",0)
    drink = fsp * smoothie
total = drink + fruit + food

if st.button ('Check Balance'): 
    st.header('You have:')
    if food > 0:
       st.write(f'{fish} plate of Fish and Chips: ${food}')
    else:
        st.write('You didnt buy any food')
    if fruit > 0:
       st.write(f'{strawgrape} bowl of Strawberry and Grapes: ${fruit}')
    else:
        st.write('You didnt buy any fruits')
    if drink > 0:
       st.write(f'{smoothie} cup of Fruit Smoothie: ${drink}')
    else:
        st.write('You didnt buy any drinks')
    if total > 0:
       st.subheader(f'Your total is ${total}')
    