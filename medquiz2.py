import streamlit as st
total = 0
name = st.text_input('Please enter your name')
question1 = st.radio('Your friend’s nose suddenly starts bleeding 😮, What should you do first?',['Choose','A) Tilt their head back and pinch the nose','B) Tilt their head forward and pinch the nose','C) Make them lie flat on the ground'])
if question1 == 'B) Tilt their head forward and pinch the nose':
    st.write('Thats right',name)
    total += 1
elif question1 == 'Choose':
    st.warning (' Please pick A, B, or C.')
else:
    st.write(' Oops, not the best choice.')
question2 = st.radio('Someone is eating and suddenly starts coughing hard, can’t speak, and looks panicked😨, What should you do first? ',['Choose','A)Give them water to drink','B)Tell them to lie down and rest','C)Perform the Heimlich maneuver'])
if question2 == 'C)Perform the Heimlich maneuver':
    st.write('Thats right',name)
    total += 1
elif question1 == 'Choose':
    st.warning (' Please pick A, B, or C.')
else:
    st.write(' Oops, not the best choice.')
question3 = st.radio('You see your friend faint while standing in the sun ☀️,What should you do first?',['Choose','A)Lay them on their back and lift their legs','B)Give them food immediately','C)Shake them to wake them up'])
if question3 == 'A)Lay them on their back and lift their legs':
    st.write('Thats right',name)
    total += 1
elif question1 == 'Choose':
    st.warning (' Please pick A, B, or C.')
else:
    st.write(' Oops, not the best choice.')
if st.button('Sumbit'):
    if (question1 != 'Choose' and question2 != 'Choose' and question3 != 'Choose' ):
        st.write("You got", total, "out of 3 correct.")
        if total == 3:
          st.write("🎉 Excellent! You know your first aid well.")
        elif total == 2:
          st.write("👍 Good job! Just a little more practice needed.")
        else:
          st.write("📚 Keep learning! First aid can save lives.")
    else:
        st.error('Please answer all questions before submitting.')



