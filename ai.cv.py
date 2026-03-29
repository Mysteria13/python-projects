import streamlit as st
import requests
from fpdf import FPDF
import base64
#-------------------CONFIGURATIONS------------------------
apikey = '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'
apilink = "https://openrouter.ai/api/v1/chat/completions" #THIS CONNECTS TO OPENROUTER
headers = {'Authorization': f'Bearer {apikey}', 'Content-Type': 'application/json'}
#----------------------------------------

#-----------Funtion to send a.i prompts-------------------------
def ask_ai(content):
    data = {
        "model": "openai/gpt-3.5-turbo", 
        "messages": [{"role": "user", "content": content}],
        "max_tokens": 250, #due to using free version
        "temperature": 0.7 #how original the answers should be ==1 very original
    }
    response = requests.post(apilink, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return "Error getting A.I Response"
if st.sidebar.button('Upload Picture'):
    uploadimage = st.sidebar.file_uploader(' Upload Your  Picture',type=['jpg','jpeg','png'])
name = st.sidebar.text_input('w',placeholder='Enter Your Full Name',label_visibility= 'collapsed')
ad = st.sidebar.text_input('w',placeholder='Enter Your State and Home address',label_visibility= 'collapsed')
pn = st.sidebar.text_input('w',placeholder='Enter your Phone Number',label_visibility= 'collapsed')
if st.sidebar.checkbox('Want to enter Email?'):
    email = st.sidebar.text_input('w',placeholder='Enter your Email Address',label_visibility= 'collapsed')
ks = st.sidebar.text_area('w',placeholder='List Your Key Skills',label_visibility= 'collapsed')
we = st.sidebar.text_area('w',placeholder='State Your Acquired Work Experience',label_visibility= 'collapsed')
ce = st.sidebar.text_area('w',placeholder='Enter Your Educational Certifate/Degrees',label_visibility= 'collapsed')

summary_prompt = f'''Design a professional summary for my CV. Make it 4-5 lines using the information given below:
My Key Skills:{ks}
My Work Experience:{we}
My Education:{ce}
'''

skills_prompt = f''' Create a Bulleted List with one-line explanations for each skill
{ks}
'''

xp_prompt = f''' Format work experience as:
Company/Organization
Start-End Date
Job Title
Responsibilities / Achievements (bullets)
{we}
'''
edu_prompt = f'''Format education as:
Course/Degree
Start-End
School / Provider
{ce}
'''
generate = st.sidebar.button('Generate My Cv')

if generate:
    with st.spinner('Generating Your CV'):
        summary_response = ask_ai(summary_prompt)
        st.subheader('Professional Summary')
        st.info(summary_response)

        skills_response = ask_ai(skills_prompt)
        st.subheader('Key Skills')
        st.info(skills_response)

        xp_response = ask_ai(xp_prompt)
        st.subheader('Work Experience')
        st.info(xp_response)

        education_response = ask_ai(edu_prompt)
        st.subheader('Education')
        st.info(education_response)


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
                pdf.cell(colw,colh,txt=f'{name}',ln=True,align='L')
                #ps
                pdf.set_font(family='Courier',size=25,style='B')
                pdf.set_xy(colx+0,coly+10)
                pdf.cell(colw,colh,txt='Professional Summary',ln=True,align='L')
                # ps2
                pdf.set_font(family='Courier',size=15,style='B')
                pdf.set_xy(colx+0,coly+15)
                pdf.cell(colw,colh,txt=f'{summary_response}',ln=True,align='L')
        #skills
                pdf.set_font(family='Courier',size=25,style='B')
                pdf.set_xy(colx+0,coly+20)
                pdf.cell(colw,colh,txt=' Key Skills',ln=True,align='L')
                #s2
                pdf.set_font(family='Courier',size=15,style='B')
                pdf.set_xy(colx+0,coly+25)
                pdf.cell(colw,colh,txt=f'{skills_response}',ln=True,align='L')
        #work          
                pdf.set_font(family='Courier',size=25,style='B')
                pdf.set_xy(colx+0,coly+30)
                pdf.cell(colw,colh,txt='Work Experience',ln=True,align='L')
                #W2
                pdf.set_font(family='Courier',size=15,style='B')
                pdf.set_xy(colx+0,coly+35)
                pdf.cell(colw,colh,txt=f'{xp_response}',ln=True,align='L')
        #education
                pdf.set_font(family='Courier',size=25,style='B')
                pdf.set_xy(colx+0,coly+40)
                pdf.cell(colw,colh,txt='Education',ln=True,align='L')

                pdf.set_font(family='Courier',size=15,style='B')
                pdf.set_xy(colx+0,coly+45)
                pdf.cell(colw,colh,txt=f'{education_response}',ln=True,align='L')
                pdf_file = 'ai.pdf'
                pdf.output(pdf_file)
                return pdf_file

        if st.button('Download'):
            pdf_funct = generate_pdf()
            with open(pdf_funct,'rb') as binary:
                    pdf_data = binary.read()
            
            view1, view2 = st.columns(2) 
            
            with view1:
                    st.sidebar.download_button(label=':rainbow[Download PDF]', data=pdf_data, file_name=f'{name}_results.pdf', mime='application/pdf')

            with view2:
                if st.button(":blue[View Invoice]"):
                    #Write the PDF using base64
                    pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')

                    #Generate the HTML to embed the PDF
                    pdf_embed = f'<embed src="data:application/pdf;base64,{pdf_base64}" type="application/pdf" width="100%" height="600px" />'

                    #Display the embedded pdf (Markdown helps us use HTML in streamlit)
                    st.markdown(pdf_embed,unsafe_allow_html=True)

