import streamlit as st

userid = 'Student1'

st.image(f'{userid}.png')
profilepic = st.file_uploader("Upload a new profile picture", type=["png", "jpg", "jpeg"])

if st.button('Save Picture'):
    if profilepic:
        st.image(profilepic)
        picname = f'{userid}.png'
        with open(picname, 'wb') as f:
            f.write(profilepic.getbuffer())
        st.success("Profile picture updated successfully!")
