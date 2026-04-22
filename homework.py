import streamlit as st
import requests

apikey = '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'
apilink = "https://openrouter.ai/api/v1/chat/completions" #THIS CONNECTS TO OPENROUTER
headers = {'Authorization': f'Bearer {apikey}', 'Content-Type': 'application/json'}

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
st.title('Python Ai Helper')

topic = st.sidebar.selectbox('Pick a topic',['Python Operators','Python Functions','Python Dictionary','Python List','Python Variables','Python Data Types','Python If Else'])

topic_prompt = f''' Give a Brief but easy to understand Detailed explanation of 4-5 lines of this topic:{topic}  with 4-5 examples 
'''
question_prompt = f''' Give A Multi-Chioce Question without answer for this topic:{topic}
'''

gen = st.sidebar.pills('',['Generating Topic'])
if gen:
    with st.spinner('Generating Topic'):
        homework_response = ask_ai(topic_prompt)
        multi_response = ask_ai(question_prompt)
        st.subheader(f'{topic} Summary')
        st.info(homework_response)
        ans_prompt = f''' Give answer for this Question:{question_prompt}
        '''
        ans_response = ask_ai(multi_response)
        tab1,tab2 = st.tabs(['Question','Answer'])
        with tab1:
           st.subheader('Multi-Choice Question')
           st.info(multi_response)
        with tab2:
           st.subheader('Answer')
           st.info(ans_response)
st.sidebar.write('Made By Lisa')