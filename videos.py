import streamlit as st
import pandas as pd
import webbrowser

menu = st.sidebar.selectbox('Menu',['Video Categories','Video Ratings'])
if menu == 'Video Categories':
    videocat = st.sidebar.pills('Choose Videos',['All','Education','Animals','Space','Sport','Religion'],default='All')

    if videocat == 'All' or videocat == 'Education':
        st.subheader('Education Category')

        edu1,edu2,edu3,edu4 = st.columns(4)
        with edu1:
            st.image('')
            st.write('Learning the Alphabet')
            if st.button ('Play Video'):
                webbrowser.open('https://www.youtube.com/watch?v=ccEpTTZW34g')
            
            st.image('')
            st.write('Division')
            if st.button ('Play Video'):
                webbrowser.open('https://www.youtube.com/watch?v=rGMecZ_aERo')
             
        with edu2:
            st.image('')
            st.write('Additon')
            if st.button ('Play Video'):
                webbrowser.open('https://www.youtube.com/watch?v=Q9sLfMrH8_w')
            
            st.image('')
            st.write('Subtraction')
            if st.button ('Play Video'):
              webbrowser.open('https://www.youtube.com/watch?v=qKxQ33KcRWQ')

        with edu3:
            st.image('')
            st.write('BEDMAS')
            if st.button ('Play Video'):
                webbrowser.open('https://www.youtube.com/watch?v=dAgfnK528RA')
            st.image('')
            st.write('Bill Nye')
            if st.button ('Play Video'):
                webbrowser.open('https://www.youtube.com/watch?v=h3iXRTp8J_4')
        with edu4:
            st.image('')
            st.write('Multiplication Tables')
            if st.button ('Play Video'):
                webbrowser.open('https://www.youtube.com/watch?v=hJiiLDPsuzo')
            st.image('')
            st.write('Decimal') 
            if st.button ('Play Video'):
                webbrowser.open('https://www.youtube.com/watch?v=kwh4SD1ToFc')          

    if videocat =='All' or videocat == 'Animals':
        st.subheader('Animal Catergory')
        ani1,ani2,ani3,ani4 = st.columns(4)
        with ani1:
            st.image('')
            st.write("Lions")
            if st.button ('Play Video'):
                webbrowser.open('')
            st.image('')
            st.write('Tigers')
            if st.button ('Play Video'):
                webbrowser.open('')
            
        with ani2:
            st.image('')
            st.write('dolphins')
            if st.button ('Play Video'):
                webbrowser.open('')
            st.image('')
            st.write('Whales')
            if st.button ('Play Video'):
                webbrowser.open('')
        with ani3:
            st.image('')
            st.write('Lizards')
            if st.button ('Play Video'):
                webbrowser.open('')
            st.image('')
            st.write('Snakes')
            if st.button ('Play Video'):
                webbrowser.open('')
        with ani4:
            st.image('')
            st.write('Mosquitoes')
            if st.button ('Play Video'):
                webbrowser.open('')
            st.image('')
            st.write('Spiders')
            if st.button ('Play Video'):
                webbrowser.open('')
    if videocat == 'All'or videocat == 'Space':
        st.subheader('Space Category')
        spa1,spa2,spa3,spa4 = st.columns(4)
        with spa1:
            st.image('')
            st.write('Saturn')
            if st.button ('Play Video'):
                webbrowser.open('')
            st.image('')
            st.write('Jupiter')
            if st.button ('Play Video'):
                webbrowser.open('')
        with spa2:
            st.image('')
            st.write('Mars')
            if st.button ('Play Video'):
                webbrowser.open('') 
            st.image('')
            st.write('Venus')
            if st.button ('Play Video'):
                webbrowser.open('')
        with spa3:
            st.image('')
            st.write('Mercury')
            if st.button ('Play Video'):
                webbrowser.open('')
            st.image('')
            st.write('Neptune')
            if st.button ('Play Video'):
                webbrowser.open('')
        with spa4:
            st.image('')
            st.write('Earth')
            if st.button ('Play Video'):
                webbrowser.open('')
            st.image('')
            st.write('Uranus')
            if st.button ('Play Video'):
                webbrowser.open('')