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

