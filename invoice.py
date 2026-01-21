import streamlit as st
import pandas as pd
from fpdf import FPDF
import base64
col1,col2 =st.columns(2)
col3,col4=st.columns(2)
logourl = 'lisa.png'
with col2:
  st.header(':rainbow[**Invoice**]')
with col4:
  Invoice = st.text_input(':rainbow[Invoice#:]',placeholder='Invoice#')
  Invoicedate = st.date_input(':rainbow[Invoice Date:]')
  Due = st.date_input(':rainbow[Due Date:]')
with col1:
  st.write(':rainbow[Lisaautos]')
  st.write(':rainbow[226 Constance, Canadian Autos]')
  st.write(':rainbow[Ontario,Canada]')
with col3:
  st.write(':rainbow[Bill to:]')
  customer = st.text_input('w',placeholder='Customer Name',label_visibility= 'collapsed')
  email = st.text_input('w',placeholder='Email Address',label_visibility= 'collapsed')
col5,col6,col7,col8=st.columns(4)
with col5:
  st.write(':rainbow[Description]')
  des = st.text_input('w',placeholder='Description',label_visibility= 'collapsed')
with col6:
    st.write(':rainbow[Quanity]')
    qua = st.number_input('w',0,placeholder='Quanity',label_visibility= 'collapsed')  
with col7:
    st.write(':rainbow[Price|Unit]')
    pu = st.number_input('w',0,placeholder='Price|Unit',label_visibility='collapsed')
with col8:
    tp = qua * pu
    st.write(':rainbow[Total Price]')
    tp = st.number_input('w',qua * pu,placeholder='Total Price',label_visibility='collapsed',disabled=True)
st.divider()
col9,col10= st.columns(2)
with col9:
   st.write(':rainbow[Payment Information]')
   st.write(':rainbow[Acc Name: Lisaautos]')
   st.write(':rainbow[Acc Number: 234 113 1308]')
   st.write(':rainbow[Bank Name:Trust Bank]')
with col10:
  tp = qua * pu
  st.write(':rainbow[Payment Due]')
  st.subheader(f':rainbow[${tp}]')


def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    colx = 10
    coly = 10
    colw = 90
    colh = 10
    pdf.image(logourl,x=colx,y=coly,w=25)
    pdf_file = 'invoice.pdf'
    pdf.output(pdf_file)
    return pdf_file
pdf_funct = generate_pdf()
with open(pdf_funct,'rb') as binary:
   pdf_data = binary.read()


view1 , view2 = st.columns[2]
with view1:
    st.download_button(label=':rainbow[Download PDF]',data=pdf_data, file_name=             )