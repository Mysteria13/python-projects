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


    #INVOICE
    pdf.set_font(family='Courier',size=23,style='B')
    pdf.set_xy(colx+130,coly+5)
    pdf.cell(colw,colh,txt='INVOICE',ln=True,align='L')

    #Lisaautos
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+0,coly+35)
    pdf.cell(colw,colh,txt='Lisaautos',ln=True,align='L')
    
    #address
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+0,coly+45)
    pdf.cell(colw,colh,txt='226 Constance, Canadian Autos',ln=True,align='L')
    
    #State
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+0,coly+55)
    pdf.cell(colw,colh,txt='Ontario,Canada',ln=True,align='L')
    
    #Bill to
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+0,coly+100)
    pdf.cell(colw,colh,txt='Bill to:',ln=True,align='L')
    
    #customer
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+0,coly+110)
    pdf.cell(colw,colh,txt=customer,ln=True,align='L')
    
    #email
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+0,coly+120)
    pdf.cell(colw,colh,txt=email,ln=True,align='L')
    
    #Invoice number
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+115,coly+110)
    pdf.cell(colw,colh,txt=f'Invoice#: {Invoice}',ln=True,align='L')

    
    # Invoice date
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+103,coly+120)
    pdf.cell(colw,colh,txt=f'Invoice Date: {Invoicedate}',ln=True,align='L')
    
  #description
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+0,coly+150)
    pdf.cell(colw,colh,txt='DESCRIPTION',ln=True,align='L')
    
    #Quantity
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+80,coly+150)
    pdf.cell(colw,colh,txt='QUANTITY',ln=True,align='L')
    
    #Price|Unit
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+110,coly+150)
    pdf.cell(colw,colh,txt='PRICE|UNIT',ln=True,align='L')
    
    #total price
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+145,coly+150)
    pdf.cell(colw,colh,txt='TOTAL PRICE',ln=True,align='L')

    #line
    pdf.set_line_width(0.5)
    pdf.line(colx,coly+160,colx+180,coly+160)
    
    #description
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+0,coly+163)
    pdf.cell(colw,colh,txt=f'{des}',ln=True,align='L')

    #qua
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+90,coly+163)
    pdf.cell(colw,colh,txt=f'{qua}',ln=True,align='L')

    #Pu
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+120,coly+163)
    pdf.cell(colw,colh,txt=f'{pu}',ln=True,align='L')

    #tp
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+155,coly+163)
    pdf.cell(colw,colh,txt=f'{tp}',ln=True,align='L')

    #payment
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+0,coly+195)
    pdf.cell(colw,colh,txt='Payment Information',ln=True,align='L')

    #acc name
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+0,coly+203)
    pdf.cell(colw,colh,txt='Account Name: Lisaautos',ln=True,align='L')

    #acc number
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+0,coly+211)
    pdf.cell(colw,colh,txt='Account Number: 234 113 1308 ',ln=True,align='L')
    
    #bank name
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+0,coly+219)
    pdf.cell(colw,colh,txt='Bank Name: Trust Bank ',ln=True,align='L')
    
    #due date
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+0,coly+227)
    pdf.cell(colw,colh,txt=f'Pay before {Due} ',ln=True,align='L')

    #Payment due
    pdf.set_font(family='Courier',size=13,style='B')
    pdf.set_xy(colx+120,coly+193)
    pdf.cell(colw,colh,txt='Payment Due',ln=True,align='L')
    #total in big size
    pdf.set_font(family='Courier',size=30,style='B')
    pdf.set_xy(colx+120,coly+213)
    pdf.cell(colw,colh,txt=f'${tp}',ln=True,align='L')
    pdf_file = 'invoice.pdf'
    pdf.output(pdf_file)
    return pdf_file
pdf_funct = generate_pdf()
with open(pdf_funct,'rb') as binary:
   pdf_data = binary.read()


view1, view2 = st.columns(2)

with view1:
        st.download_button(label=':blue[Download PDF]', data=pdf_data, file_name=f'{customer}_invoice.pdf', mime='application/pdf')

with view2:
    if st.button(":blue[View Invoice]"):
        #Write the PDF using base64
        pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')

        #Generate the HTML to embed the PDF
        pdf_embed = f'<embed src="data:application/pdf;base64,{pdf_base64}" type="application/pdf" width="100%" height="600px" />'

        #Display the embedded pdf (Markdown helps us use HTML in streamlit)
        st.markdown(pdf_embed,unsafe_allow_html=True)