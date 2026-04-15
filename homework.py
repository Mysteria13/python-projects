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
topic = st.sidebar.selectbox('Pick a topic',['Python Operators','Python Funtions','Python Dictionary and List','Python Commands'])

topic_prompt = f''' Give a Brief but easy to understand Detailed explanation of 4-5 lines of this topic:{topic}  with 4-5 examples for beginners
'''
gen = st.sidebar.button('Generating Answer')
if gen:
    with st.spinner('Generating Answer'):
        homework_response = ask_ai(topic_prompt)
        st.subheader('The Explanation')
        st.info(homework_response)