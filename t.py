#create an app
#asking the user to enter first number  
#asking the user to enter second number  
#create 4 buttons for the following operators Add, Subtract, Multiply, Divide
#when user clicks his prefered operator then show a table (no csv) of the following
#number1 | number2 | operator | result
import streamlit as st
import pandas as pd 
import numpy as np
num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)  
operator = st.selectbox("Select an operator", ["Add", "Subtract", "Multiply", "Divide"])
if operator == "Add":
    result = num1 + num2
elif operator == "Subtract":
    result = num1 - num2    