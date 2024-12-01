import streamlit as st
st.title('Football Caculator App made by Lisa')
name = 'Liam'
match_tickets=100
account_username  = 'Liamisthegoat'
account_password = "abcdef123456"
account_login = account_username, account_password
bill = 0
st.subheader ("Season Pass Selection")
pass1,pass2 = st.columns(2)
with pass1:
     if st.checkbox("Standard Pass : $200"):
       bill += 200
       st.write ("ok done")
with pass2:
    if st.checkbox("VIP Pass : $500"):
      bill += 500
      st.write ("ok done")      
st.subheader ("Team Merchandise")
team1,team2,team3 = st.columns(3)
with team1:
    if st.checkbox("Jersey: $60"):
      bill += 60
      st.write ("ok done")
with team2:
    if st.checkbox("Scarf : $30"):
      bill += 30
      st.write ("ok done")
with team3:
    if st.checkbox("Hat : $20"):
      bill += 20
      st.write ("ok done")
st.subheader ("Snacks Purchase")
snack1,snack2,snack3 = st.columns(3)
with snack1:
    if st.checkbox("Popcorn: $10"):
      bill += 10
      st.write ("ok done")
with snack2:
    if st.checkbox("Hotdog: $15"):
      bill += 15
      st.write ("ok done")
with snack3:
    if st.checkbox("Soda: $5"):
      bill += 5
      st.write ("ok done")
st.subheader ("Premium Sports Channel Subscription")
sub1,sub2 = st.columns(2)
with sub1:
     if st.checkbox("Monthly subscription  : $20"):
       bill += 20
       st.write ("ok done")
with sub2:
    if st.checkbox("Annual subscription: $200"):
      bill += 200
      st.write ("ok done")      
total = bill + match_tickets
if st.button("Check amount"):
   st.write (name,"your total amount for your football journey is",total,"dollars")