import streamlit as st #this creates web page for your python app
import pandas as pd#this works with csv and converts to table
import plotly.express as px#this is used to plot charts'
from fpdf import FPDF
import base64 
st.set_page_config(page_title='Student Databse',page_icon='👌')
st.title(' Student database App ')

menu = st.sidebar.selectbox("Choose an option",["input scores","scores database/chart"])


try: #attempt to do what is below 
   readcsv = pd.read_csv('scores.csv')
except:#if there is an error in the above attempt then do this
     readcsv = pd.DataFrame()#create an empty dataframe for me

     #csv : comma seperated values
#menu page to only show the table 


if menu == "input scores": 
     name = st.text_input('Please enter Student name')
     col1, col2, = st.columns(2)
     with col1:
          math = st.number_input('Enter students math score',0)
          English = st.number_input('Enter students english score',0)
          Science = st.number_input('Enter students science score',0)
     with col2:
          Art = st.number_input('Enter students art score',0)
          History = st.number_input('Enter students history score',0)
          Geo = st.number_input('Enter students geography score',0)
     Total = math + English + Science + Art + History + Geo
     ave = Total/6
     if ave >= 100:
          grade = 'A+'
     elif ave >= 90:
          grade = 'A'
     elif ave >= 80:
          grade = 'B+'
     elif ave >= 70:
          grade ='B' 
     elif ave >= 60:
          grade ='B-' 
     elif ave >= 50:
          grade ='C' 
     elif ave >= 40:
          grade ='D' 
     elif ave <= 30:
          grade ='F' 
     if st.button ("Save student scores"):
          if name and math and English and Science and Art and History and Geo:
           st.write (name,"your total score is",Total,"average is",ave,"grade is",grade, "Good job!!!")
          scoresdict = {"Name":[name],"Math":[math],"English":[English],"Science":[Science],"Art":[Art],"History":[History],"Geography":[Geo],"Average":[ave],"Grade":[grade]}
          st.write (scoresdict)
          student_table = pd.DataFrame(scoresdict)
          st.table(student_table)
          tablesjoin = pd.concat([readcsv,student_table],ignore_index=True)
          tablesjoin.to_csv('scores.csv',index=False)
          st.success('Student Data Saved')
     else:
          st.error ('please fill in all the boxes')

     
def generate_pdf():
          pdf = FPDF()
          pdf.add_page()
          colx = 10
          colx = 10
          coly = 10
          colw = 90
          colh = 10
          # Results
          pdf.set_font(family='Courier',size=25,style='B')
          pdf.set_xy(colx+0,coly+5)
          pdf.cell(colw,colh,txt='Results For Leagues Secondary School',ln=True,align='L')

          #Student Name
          pdf.set_font(family='Courier',size=23,style='B')
          pdf.set_xy(colx+0,coly+35)
          pdf.cell(colw,colh,txt=name,ln=True,align='L')

          #Subjects
          pdf.set_font(family='Courier',size=13,style='B')
          pdf.set_xy(colx+0,coly+45)
          pdf.cell(colw,colh,txt='Subjects                                    Score',ln=True,align='L')
 
          #Math
          pdf.set_font(family='Courier',size=13,style='B')
          pdf.set_xy(colx+0,coly+55)
          pdf.cell(colw,colh,txt=f'Mathematics                                   {math}',ln=True,align='L')
           
          #English
          pdf.set_font(family='Courier',size=13,style='B')
          pdf.set_xy(colx+0,coly+65)
          pdf.cell(colw,colh,txt=f'English                                       {English}',ln=True,align='L')

          #Science
          pdf.set_font(family='Courier',size=13,style='B')
          pdf.set_xy(colx+0,coly+75)
          pdf.cell(colw,colh,txt=f'Science                                       {Science}',ln=True,align='L')

          #art
          pdf.set_font(family='Courier',size=13,style='B')
          pdf.set_xy(colx+0,coly+85)
          pdf.cell(colw,colh,txt=f'Art                                           {Art}',ln=True,align='L')

          #history
          pdf.set_font(family='Courier',size=13,style='B')
          pdf.set_xy(colx+0,coly+95)
          pdf.cell(colw,colh,txt=f'History                                       {History}',ln=True,align='L')
       
          
          #Geography
          pdf.set_font(family='Courier',size=13,style='B')
          pdf.set_xy(colx+0,coly+105)
          pdf.cell(colw,colh,txt=f'Geography                                     {Geo}',ln=True,align='L')

          #total
          pdf.set_font(family='Courier',size=15,style='B')
          pdf.set_xy(colx+70,coly+125)
          pdf.cell(colw,colh,txt=f'Grade:{grade}',ln=True,align='L')

          #ave
          pdf.set_font(family='Courier',size=13,style='B')
          pdf.set_xy(colx+0,coly+115)
          pdf.cell(colw,colh,txt=f'Average Mark                                  {ave}',ln=True,align='L')
          pdf_file = 'Student.pdf'
          pdf.output(pdf_file)
          return pdf_file
          

          
if menu == "scores database/chart":
    st.table(readcsv)
    subjects = ["Math","English","Science","Art","History","Geography"]
    subjectstable = readcsv[subjects].mean().reset_index()

    barchart = px.bar(subjectstable,x='index',y=0,labels={'index':'Subject','0':'Average'}) 
    st.plotly_chart(barchart) 
    
if st.sidebar.button('Download'):
    pdf_funct = generate_pdf()
    with open(pdf_funct,'rb') as binary:
            pdf_data = binary.read()
    
    view1, view2 = st.columns(2) 
    with view1:
               st.download_button(label=':rainbow[Download PDF]', data=pdf_data, file_name=f'{name}_results.pdf', mime='application/pdf')

    with view2:
         if st.button(":blue[View Invoice]"):
               #Write the PDF using base64
               pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')

               #Generate the HTML to embed the PDF
               pdf_embed = f'<embed src="data:application/pdf;base64,{pdf_base64}" type="application/pdf" width="100%" height="600px" />'

               #Display the embedded pdf (Markdown helps us use HTML in streamlit)
               st.markdown(pdf_embed,unsafe_allow_html=True)

 
