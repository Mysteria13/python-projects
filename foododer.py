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
st.set_page_config(layout='wide')

st.title('Food order App made by Lisa')
st.image("https://images.immediate.co.uk/production/volatile/sites/30/2022/11/Meze-style-sharing-board-2f05456.jpg")
bill = 0
st.subheader("Food Category")
food1,food2,food3,food4= st.columns(4)

with food1:
   if st.checkbox("Fish & Chips: $15"):
    bill += 15
   st.write("Ok Done")

with food2:
    if st.checkbox("Fried Rice & Chicken: $20"):
      bill += 20 
      st.write("Ok Done")

with food3:
    if st.checkbox("Jollof Rice & Turkey: $20"):
      bill += 20
      st.write("Ok Done") 

with food4:
  if st.checkbox(" Pepper Soup & Catfish : $15"):
     bill +=15
     st.write("Ok Done")



st.subheader("Fruit Category")
fruit1,fruit2,fruit3,fruit4= st.columns(4)

with fruit1:
    if st.checkbox("Strawberry & Grapes: $5"):
      bill += 5
    st.write("Ok Done")

with fruit2:
       if st.checkbox("Pinapple & Apple: $6"):
        bill += 6
        st.write("Ok Done")

with fruit3:
      if st.checkbox("Rasberry & Papaya: $7"):
         bill += 7
         st.write("Ok Done") 

with fruit4:
      if st.checkbox(" Mango & Cherry : $8"):
            bill += 8
      st.write("Ok Done")


st.subheader("Drink Category")
drink1,drink2,drink3, drink4= st.columns(4)

with drink1:
    if st.checkbox("Whiskey: $20"):
      bill += 20
    st.write("Ok Done")

with drink2:
       if st.checkbox("Soda: $16"):
          bill += 16
       st.write("Ok Done")

with drink3:
      if st.checkbox("Wine: $17"):
         bill += 17
         st.write("Ok Done") 

with drink4:
      if st.checkbox(" Fruit Smoothie : $15"):
         bill += 15
         st.write("Ok Done")
            

if st.button("Check Bill"):
    st.write("Your Bill is", bill," dollars")
                                         
