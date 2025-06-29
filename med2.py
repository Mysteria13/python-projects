import streamlit as st

st.set_page_config(page_title="Medical Awareness Quiz", page_icon=":medical_symbol:", layout="wide")

def homepage():
    st.title(":rainbow[Medical Awareness Quiz]")
    name = st.text_input(":rainbow[Enter your name:]")
    if st.button(":rainbow[Start Quiz]"):
        if name:
            st.session_state['quiz_started'] = True
            st.session_state['name'] = name
        else:
            st.info(':rainbow[Got a name?]')

def q1():
    st.subheader(':rainbow[Question 1]')
    st.radio(
        ':rainbow[What is the main job of your heart?]',
        [
            ':rainbow[A) Pumping blood ]',
            ':rainbow[B) Digesting food ]',
            ':rainbow[C) Storing energy ]',
            ':rainbow[D) Breathing air ]'
        ],
        key='q1'
    )

def q2():
    st.subheader(':rainbow[Question 2]')
    st.radio(
        ':rainbow[What do vaccines help protect you from?]',
        [
            ':rainbow[A) Common cold ]',
            ':rainbow[B) Diseases like measles and flu]',
            ':rainbow[C) Cuts and bruises ]',
            ':rainbow[D) None of the above ]'
        ],
        key='q2'
    )

def q3():
    st.subheader(':rainbow[Question 3]')
    st.radio(
        ':rainbow[Why is it important to wash your hands?]',
        [
            ':rainbow[A) To smell nice ]',
            ':rainbow[B) To prevent getting sick ]',
            ':rainbow[C) To look clean ]',
            ':rainbow[D) None of the above ]'
        ],
        key='q3'
    )

def q4():
    st.subheader(':rainbow[Question 4]')
    st.radio(
        ':rainbow[What should you do if you have a fever?]',
        [
            ':rainbow[A) Go play outside ]',
            ':rainbow[B) Tell an adult and rest ]',
            ':rainbow[C) Eat a lot of candy ]',
            ':rainbow[D) Stay up late ]'
        ],
        key='q4'
    )

if 'quiz_started' not in st.session_state:
    st.session_state['quiz_started'] = False

if not st.session_state['quiz_started']:
    homepage()
else:
    st.write(f":rainbow[Welcome, {st.session_state.get('name', '')}!]")
    q1()
    q2()
    q3()
    q4()