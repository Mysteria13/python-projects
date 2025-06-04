#create an app
#asking the user to enter first number  
#asking the user to enter second number  
#create 4 buttons for the following operators Add, Subtract, Multiply, Divide
#when user clicks his prefered operator then show a table (no csv) of the following
#number1 | number2 | operator | result
#hello world
import streamlit as st
clo1,clo2,clo3= st.columns (3)
with clo1:
  num1 = st.number_input ('Please enter first number :',0)
with clo2:
  num2 = st.number_input ('Please enter second number:',0)
with clo3:
  operators = st.radio('pick an option',['Add','Subtract','Multiply','Divide'])
  
if operators == 'Add':
 result =num1 + num2 
if operators == 'Subtract':
  result = num1 - num2 
if operators == 'Multiply':
  result = num1 * num2
if operators == 'Divide':
  result = num1 / num2
ansdict = {'Number1':[num1],'Number2':[num2],'operator':[operators],'Result':[result]}

if st.button ('Submit'):
 st.table (ansdict)
