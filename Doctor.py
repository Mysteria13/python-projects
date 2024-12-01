import streamlit as st
st.title('Doctor Submission Form')
st.subheader('Fill the form below and we will get back to you as soon as we can')
col1,col2=st.columns(2)
with col1:
  firstname = st.text_input ("First name")
with col2:
  lastname =st.text_input ("Last name")

col3,col4,col5=st.columns(3)
st.subheader ('Date')
with col3:
 day=st.selectbox ('Day',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'],0)
with col4:
  month =st.selectbox ("Month",['January','Febuary','March','April','May','June','July','August','September','October','November','December'])
with col5:
  year =st.selectbox ("Year",['1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023'])
col6,col7 = st.columns(2)
with col6:
  Gender =st.selectbox ('Gender',['Male','Female'])
with col7:
  Phone= st.number_input = ("(000)000 0000 ",0)

ad = st.text_input (" Address ")

adE = st.text_input ("Street Address Line")
adEs = st.text_input ("Street Address Line 2")
col8,col9 = st.columns(2)
with col8:
  city =st.text_input ("City")
  
with col9:
  state =st.text_input ("State/Province")
  
pos =st.text_input ("Postal/ Zip Code")

col10,col11 = st.columns(2)
with col10:
  email =st.text_input ("Email")
mad =st.radio("Have you ever visited our Facility",['Yes','No'])

if st.button ('Submit'):
  st.write("Thanks for applying")
