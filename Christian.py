import streamlit as st
st.title('Christian Caculator App made by Lisa')
name = 'Sarah'
bible=50
account_username  = 'Godisgood'
account_password = "6546g"
account_login = account_username, account_password
bill = 0
st.subheader ("Devotion book Selection")
pass1,pass2,pass3 = st.columns(3)
with pass1:
     if st.checkbox("Daily Devotions : $10"):
       bill += 10
       st.write ("ok done")
with pass2:
    if st.checkbox("Bible Study Guide : $20"):
      bill += 20
      st.write ("ok done")   
with pass3:
    if st.checkbox("Prayer Journal : $15"):
      bill += 15
      st.write ("ok done")           
st.subheader ("Outfits")
out1,out2,out3 = st.columns(3)
with out1:
    if st.checkbox("Outfit 1 : $30"):
      bill += 30
      st.write ("ok done")
with out2:
    if st.checkbox("Outfit 2 : $50"):
      bill += 50
      st.write ("ok done")
with out3:
    if st.checkbox("Outfit 3 : $70"):
      bill += 70
      st.write ("ok done")
st.subheader ("Pet Purchase")
pet1,pet2,pet3 = st.columns(3)
with pet1:
    if st.checkbox("Cat: $25"):
      bill += 25
      st.write ("ok done")
with pet2:
    if st.checkbox("Dog: $25"):
      bill += 25
      st.write ("ok done")
with pet3:
    if st.checkbox("Hamster: $25"):
      bill += 25
      st.write ("ok done")
st.subheader ("Fancy Arifacts")
sub1,sub2,sub3 = st.columns(3)
with sub1:
     if st.checkbox("Rosary Beads : $20"):
       bill += 20
       st.write ("ok done")
with sub2:
    if st.checkbox("Cross Necklace : $10"):
      bill += 10
      st.write ("ok done")    
with sub3:
    if st.checkbox("Icon : $30"):
      bill += 30
      st.write ("ok done")        
total = bill + bible
if st.button("Check amount"):
   st.write (name,"your total amount for your Christian journey is",total,"dollars")