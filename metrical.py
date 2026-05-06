import streamlit as st
st.title('Conversion App')
amount = st.number_input('Enter amount you want to convert:')
con = st.selectbox('Pick Method Of Conversion',['None','In to Cm','Cm to In','Meter to Feet','Feet to Meter','Mile to Km','Km to Mile'])
if st.button("Convert"):
    if con == 'In to Cm':
            IC = amount * 2.54
            st.write('Your answer is approximately',IC,'Centimetres')
    if con == 'Cm to In':
            Ci = amount // 2.54
            st.write('Your answer is aproximately',Ci,'Inches')
    if con == 'Meter to Feet':
            Mf = amount * 3.28
            st.write('Your answer is aproximately',Mf,'Feet')
    if con == 'Feet to Meter':
            Fm = amount // 3.28
            st.write('Your answer is aproximately',Fm,'Meters')
    if con == 'Mile to Km':
            Mk = amount * 1.61
            st.write('Your answer is aproximately',Mk,'Kilometres')
    if con == 'Km to Mile':
            Km = amount // 1.61
            st.write('Your answer is aproximately',Km,'Miles')
