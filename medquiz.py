import streamlit as st
st.set_page_config(page_title="Medical Awareness Quiz", page_icon=":medical_symbol:", layout="wide")
def homepage():
    st.title(":rainbow[Medical Awareness Quiz]")
    name = st.text_input(":rainbow[Enter your name:]")
    if st.button(":rainbow[Start Quiz]"):
        if name:
            st.write('Correct')
        else:
            st.info(':rainbow[Got a name?]')
homepage()
col1, col2 = st.columns(2)
with col1:
    
        
        def q1():
            st.subheader(':rainbow[Question 1]')
            q1 = st.radio(':rainbow[What is the main job of your heart?]',[':rainbow[A) Pumping blood ]',':rainbow[B) Digesting food ]',':rainbow[C) Storing enregy ]',':rainbow[D) Breathing air ]'])

        q1()
        def q2():
            st.subheader(':rainbow[Question 2]')
            q2 = st.radio(':rainbow[What do vaccines help protect you from?]',[':rainbow[A) Common cold ]',':rainbow[B) Diseases like measles and flu]',':rainbow[C) Cuts and bruises ]',':rainbow[D) None of the above ]'])

        q2() 
        def q3():   
            st.subheader(':rainbow[Question 3]')
            q3 = st.radio(':rainbow[Why is it important to wash your hands?]',[':rainbow[A) To smell nice ]',':rainbow[B) To prevent getting sick ]',':rainbow[C) To look clean ]',':rainbow[D) None of the above ]'])

        q3()
        def q4():
            st.subheader(':rainbow[Question 4]')
            q4 = st.radio(':rainbow[What should you do if you have a fever?]',[':rainbow[A) Go play outside ]',':rainbow[B) Tell an adult and rest ]',':rainbow[C) Eat a lot of candy ]',':rainbow[D) Stay up late ]'])
        q4()
        def q5():
            st.subheader(':rainbow[Question 5]')
            q5 = st.radio(':rainbow[What does a doctor do?]',[':rainbow[A) Fix cars ]',':rainbow[B) Help people stay healthy ]',':rainbow[C) Teach math ]',':rainbow[D) None of the above ]'])
        q5()
        def q6():
            st.subheader(':rainbow[Question 6]')
            q6 = st.radio(':rainbow[What is a healthy snack?]',[':rainbow[A) Candy ]',':rainbow[B) Fruits and vegetables ]',':rainbow[C) Chips ]',':rainbow[D) Soda ]'])
        q6()
        def q7():
            st.subheader(':rainbow[Question 7]')
            q7 = st.radio(':rainbow[What does it mean to be allergic to something?]',[':rainbow[A) You like it a lot ]',':rainbow[B) Your body reacts badly to it ]',':rainbow[C)You can’t eat it ]',':rainbow[D) None of the above ]'])
        q7()   
        def q8():
            st.subheader(':rainbow[Question 8]')
            q8 = st.radio(':rainbow[What should you do if you get a cut?]',[':rainbow[A) Ignore it ]',':rainbow[B) Clean it and put a bandage on it ]',':rainbow[C) Show it to your friends ]',':rainbow[D) Put dirt on it None of the above]'])
        q8()
        def q9():
            st.subheader(':rainbow[Question 9]')
            q9 = st.radio(':rainbow[Why is it important to eat breakfast?]',[':rainbow[A) It’s the best meal of the day ]',':rainbow[B)It gives you energy for school ]',':rainbow[C) You can skip it ]',':rainbow[D)  None of the above ]'])
        q9()
        def q10():
            st.subheader(':rainbow[Question 10]')
            q10 = st.radio(':rainbow[What is one way to keep your bones strong?]',[':rainbow[A)  Eating junk food ]',':rainbow[B) Drinking milk or eating dairy ]',':rainbow[C)  Avoiding exercise ]',':rainbow[D) None of the above]'])
        q10()

with col2:
    def q11():
        st.subheader(':rainbow[Question 11]')
        q11 = st.radio(':rainbow[What is the purpose of first aid?]',[':rainbow[A) To help with homework ]',':rainbow[B)To give immediate care in emergencies ]',':rainbow[C) To make food ]',':rainbow[D)None of the above]'])
    q11()
    def q12():
        st.subheader(':rainbow[Question 12]')
        q12 = st.radio(':rainbow[What can help you breathe better when you’re sick?] ',[':rainbow[A) Eating ice cream ]',':rainbow[B) Drinking warm fluids ]',':rainbow[C) Running around ]',':rainbow[D) None of the above ]'])
    q12()
    def q13():
        st.subheader(':rainbow[Question 13]')
        q13 = st.radio(':rainbow[What is a common symptom of a cold?]',[':rainbow[A) Runny nose]',':rainbow[B) Happy thoughts ]',':rainbow[C)  Dancing ]',':rainbow[D) None of the above ]'])
    q13()
    def q14():
        st.subheader(':rainbow[Question 14]')
        q14 = st.radio(':rainbow[Why should you cover your mouth when you cough?]',[':rainbow[A) To look funny ]',':rainbow[B) To prevent spreading germs ]',':rainbow[C)To make a sound ]',':rainbow[D) None of the above ]'])
    q14()
    def q15(): 
        st.subheader(':rainbow[Question 15]')
        q15 = st.radio(':rainbow[What is a safe way to exercise?]',[':rainbow[A)Jumping on the bed ]',':rainbow[B)Playing sports or riding a bike ]',':rainbow[C)Sitting all day ]',':rainbow[D) None of the above ]'])
    q15()
    def q16():
        st.subheader(':rainbow[Question 16]')
        q16 = st.radio(':rainbow[What does a dentist check?]',[':rainbow[A)  Your eyes ]',':rainbow[B)  Your Teeth]',':rainbow[C) Your Hair ]',':rainbow[D) None of the above ]'])
    q16()
    def q17():
        st.subheader(':rainbow[Question 17]')
        q17 = st.radio(':rainbow[What should you do if you feel dizzy?]',[':rainbow[A)  Keep running]',':rainbow[B)Sit down and tell an adult ]',':rainbow[C) Eat a lot of candy]',':rainbow[D) None of the above ]'])
    q17()
    def q18():
        st.subheader(':rainbow[Question 18]')
        q18 = st.radio(':rainbow[What is the main function of your lungs?]',[':rainbow[A)  To pump blood]',':rainbow[B)To help you breathe ]',':rainbow[C) To digest food]',':rainbow[D) None of the above ]'])
    q18()
    def q19():
        st.subheader(':rainbow[Question 19]')
        q19 = st.radio(':rainbow[What can help you stay healthy during cold and flu season?]',[':rainbow[A) Washing hands frequently]',':rainbow[B)Eating more sweets ]',':rainbow[C)Skipping sleep ]',':rainbow[D) None of the above ]'])
    q19()
    def q20():
        st.subheader(':rainbow[Question 20]')
        q20 = st.radio(':rainbow[What does it mean if someone has a headache?]',[':rainbow[A) They are happy]',':rainbow[B)They might need rest or water ]',':rainbow[C)They want to play]',':rainbow[D) None of the above ]'])
    q20()
    def submit():
        if st.button(':rainbow[Submit Answers]'):
            st.success(':rainbow[Thank you for taking the quiz! Your answers have been submitted.]')
    submit()