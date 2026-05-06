import streamlit as st
import requests




apilink = "https://openrouter.ai/api/v1/chat/completions"




try:
   apikey = st.secrets["OPENROUTER_API_KEY"]
except:
   apikey = st.sidebar.text_input("Enter your OpenRouter API Key", type="password")


headers = {
   "Authorization": f"Bearer {apikey}",
   "Content-Type": "application/json",
   "HTTP-Referer": "https://pythonhomework.streamlit.app/", 
}




def askai(content):
   data = {
       "model": "openai/gpt-4o-mini",
       "messages": [{"role": "user", "content": content}],
       "max_tokens": 300,
       "temperature": 0.7
   }


   try:
       response = requests.post(apilink, headers=headers, json=data)


       if response.status_code == 200:
           return response.json()['choices'][0]['message']['content']
       else:
           return f"❌ Error {response.status_code}: {response.text}"


   except Exception as e:
       return f"⚠️ Request failed: {e}"




st.title("🐍 Python AI Tutor")


topic = st.sidebar.selectbox(
   "Choose a Python topic",
   ['variables', 'lists', 'functions', 'dictionaries',
    'while loops', 'for loops', 'if else', 'range']
)


generate = st.sidebar.button("Generate Topic")




if generate:
   if not apikey:
       st.warning("Please enter your OpenRouter API key")
   else:
       with st.spinner("Generating..."):


           explanation_prompt = f"""
           Give a brief, clear, and beginner-friendly explanation of Python topic: {topic}.
           Include simple examples.
           """


           question_prompt = f"""
           Create one multiple choice question on Python topic: {topic}.
           Do NOT include the answer.
           """


           expinfo = askai(explanation_prompt)
           qsinfo = askai(question_prompt)


           st.subheader(f"📘 About Python: {topic}")
           st.info(expinfo)


           # Get answer
           answer_prompt = f"Answer this question:\n{qsinfo}"
           ansinfo = askai(answer_prompt)


           tab1, tab2 = st.tabs(["Question", "Answer"])


           with tab1:
               st.subheader("📝 Question")
               st.info(qsinfo)


           with tab2:
               st.subheader("✅ Answer")
               st.success(ansinfo)

