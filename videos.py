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
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZGIphs0Sq5tjaiiFG6To_-cHZQ0o7Bh6eXw&s')
            st.write('Learning the Alphabet')
            if st.button ('Play Video',key='1'):
                webbrowser.open('https://www.youtube.com/watch?v=ccEpTTZW34g')
            
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfKTc-vV4v0QcfwabBaqsX_o5kjom1ssfd9A&s')
            st.write('Division')
            if st.button ('Play Video',key='2'):
                webbrowser.open('https://www.youtube.com/watch?v=rGMecZ_aERo')
             
        with edu2:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOqh6NfGQO3OsD_gjhwZiZLZel0o2O_ADXtw&s')
            st.write('Additon')
            if st.button ('Play Video',key='3'):
                webbrowser.open('https://www.youtube.com/watch?v=Q9sLfMrH8_w')
            
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRK3o3Qqbt9BS8JwTp_u9J5XTBAjVugguuuLA&s')
            st.write('Subtraction')
            if st.button ('Play Video',key= '4'):
              webbrowser.open('https://www.youtube.com/watch?v=qKxQ33KcRWQ')

        with edu3:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRChzTbOyuK2Tha2VSzlWI8K1HNu5kmYm-2ag&s')
            st.write('BEDMAS')
            if st.button ('Play Video',key='5'):
                webbrowser.open('https://www.youtube.com/watch?v=dAgfnK528RA')
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoMYcNjRZlyG3fNsj7dC00Cq-zZlFeVyFmdA&s')
            st.write('Bill Nye')
            if st.button ('Play Video',key='6'):
                webbrowser.open('https://www.youtube.com/watch?v=h3iXRTp8J_4')
        with edu4:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvfsgWKvdiwwzKPBmR76ZMlJOSL0GAjLRz8w&s')
            st.write('Multiplication Tables')
            if st.button ('Play Video',key='7'):
                webbrowser.open('https://www.youtube.com/watch?v=hJiiLDPsuzo')
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8bMf4E93MUl3TM4xJgg1P4nGhppwfxW4a5w&s')
            st.write('Decimal') 
            if st.button ('Play Video',key='8'):
                webbrowser.open('https://www.youtube.com/watch?v=kwh4SD1ToFc')          

    if videocat =='All' or videocat == 'Animals':
        st.subheader('Animal Catergory')
        ani1,ani2,ani3,ani4 = st.columns(4)
        with ani1:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREJVBH0AZ7YzSsW0coaTTcXghZrARKdqi1Zg&s')
            st.write("Lions")
            if st.button ('Play Video',key='9'):
                webbrowser.open('https://www.youtube.com/watch?v=OMkEVX23BdM')
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxMqsQKpMnf8qddZR1RtYzutGi9D4f2eg1Kw&s')
            st.write('Tigers')
            if st.button ('Play Video',key='10'):
                webbrowser.open('https://www.youtube.com/watch?v=FK3dav4bA4s')
            
        with ani2:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAdlY0et2fAfqnbA6f_Lp5mcxZYfs0b2pNKw&s')
            st.write('dolphins')
            if st.button ('Play Video',key='11'):
                webbrowser.open('https://www.youtube.com/watch?v=xWTWdLvA1P0')
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGmJSnL5wSqStkEMfVi34-hTEdOOjdJ_3Z-w&s')
            st.write('Whales')
            if st.button ('Play Video',key='12'):
                webbrowser.open('https://www.youtube.com/watch?v=9VO0cQyg5dE')
        with ani3:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQObdM2xIfpOFHLdypvVRY2U-2OdCqgjJoIgw&s')
            st.write('Lizards')
            if st.button ('Play Video',key='13'):
                webbrowser.open('https://www.youtube.com/watch?v=rLY2gNiOFzk')
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTV0-ZUolrO24CzYLtPzCBxZLbzoQp9TE_wUw&s')
            st.write('Snakes')
            if st.button ('Play Video',key='14'):
                webbrowser.open('https://www.youtube.com/watch?v=_qgA63Ixc_Y')
        with ani4:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHlmX2CNQijjJ1uVjXdFnfhWN8pCHJY4GsIA&s')
            st.write('Mosquitoes')
            if st.button ('Play Video',key='15'):
                webbrowser.open('https://www.youtube.com/watch?v=9w-5wJYVmcw')
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbhOdgeM_YGsCUU1K2BOqY7grMMXOAD-1_bw&s')
            st.write('Spiders')
            if st.button ('Play Video',key='16'):
                webbrowser.open('https://www.youtube.com/watch?v=uHyYtcMZYGs')
    if videocat == 'All'or videocat == 'Space':
        st.subheader('Space Category')
        spa1,spa2,spa3,spa4 = st.columns(4)
        with spa1:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbcJ50-FVKOKdPBMv1zTo7-WEfP7-sab_sHQ&s')
            st.write('Saturn')
            if st.button ('Play Video',key='17'):
                webbrowser.open('https://www.youtube.com/watch?v=epZdZaEQhS0')
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5VTkQvuLBXL9BXCDWYu-aYL0k4s2N_BbwDQ&s')
            st.write('Jupiter')
            if st.button ('Play Video',key='18'):
                webbrowser.open('https://www.youtube.com/watch?v=PtkqwslbLY8')
        with spa2:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUFsYG60IsHimjRM92rITkg4eGmmSsQhqRyw&s')
            st.write('Mars')
            if st.button ('Play Video',key='19'):
                webbrowser.open('https://www.youtube.com/watch?v=D8pnmwOXhoY') 
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9cp-Fs1gRDhMnM4D7WwjbiO1dPZQeUcOgnw&s')
            st.write('Venus')
            if st.button ('Play Video',key='20'):
                webbrowser.open('https://www.youtube.com/watch?v=BvXa1n9fjow')
        with spa3:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcdM_b7rOYMYPUUjPVdbpdc5T42h6-Eu4cLg&s')
            st.write('Mercury')
            if st.button ('Play Video',key='21'):
                webbrowser.open('https://www.youtube.com/watch?v=0KBjnNuhRHs')
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSlsWQ6cQ9d952oT_H0pt8V9s-h1ui9kBUJg&s')
            st.write('Neptune')
            if st.button ('Play Video',key='22'):
                webbrowser.open('https://www.youtube.com/watch?v=NStn7zZKXfE')
        with spa4:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPQ29boJgPJIy0tryNORV_VUL-tNArqRZv1g&s')
            st.write('Earth')
            if st.button ('Play Video',key='23'):
                webbrowser.open('https://www.youtube.com/watch?v=HCDVN7DCzYE')
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxjyooxqEq6pmesxx2HajArLY60YKY4Fv58g&s')
            st.write('Uranus')
            if st.button ('Play Video',key='24'):
                webbrowser.open('https://www.youtube.com/watch?v=m4NXbFOiOGk')
    if videocat =='All' or videocat == 'Sport':
        st.subheader('Sport Catergory')
        spo1,spo2,spo3,spo4 = st.columns(4)
        with spo1:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdiL6EFgHunklRCB6MHQhdpojjvFpqul_oIg&s')
            st.write('Soccer')
            if st.button ('Play Video',key='25'):
                webbrowser.open('https://www.youtube.com/watch?v=cpIwMZ3cUEc')
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGQd6LlzAc58mSItXlpIvIbl2JRXU68ri3Ng&s')
            st.write('Football')
            if st.button ('Play Video',key='26'):
                webbrowser.open('https://www.youtube.com/watch?v=3t6hM5tRlfA')
        with spo2:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJ_MWwRq-XrO2mw28SBQurhfZj2OfROJ3Yeg&s')
            st.write('Basketball')
            if st.button ('Play Video',key='27'):
                webbrowser.open('https://www.youtube.com/watch?v=oyjYgmsM00Q')
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpnv0EB9BGCktQqtE-FUOWvcoFoopfFGpEVg&s')
            st.write('Baseball')
            if st.button ('Play Video',key='28'):
                webbrowser.open('https://www.youtube.com/watch?v=WMA8L5OpuDY')
        with spo3:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPKvbE4YfHHTTi3o405k29zrdGswkYqzt9XA&s')
            st.write('Swimming')
            if st.button ('Play Video',key='29'):
                webbrowser.open('https://www.youtube.com/watch?v=VNdUONyi2hU')
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpalJ09hrLqlAj1RuFUb8AU9sUKDzUVdKRrg&s')
            st.write('Surfing')
            if st.button ('Play Video',key='30'):
                webbrowser.open('https://www.youtube.com/watch?v=EFNM-Gsl8W8')
        with spo4:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTM8cu4-SznjaylkGWMRaIQSRK6xw4tc6UFiw&s')
            st.write('Snowboarding')
            if st.button ('Play Video',key='31'):
                webbrowser.open('https://www.youtube.com/watch?v=7VBalG0IhhI')
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlXdj0hyX4alDWkKI0t80yA_2ocLJFGB1NGw&s')
            st.write('Skiing')
            if st.button ('Play Video',key='32'):
                webbrowser.open('https://www.youtube.com/watch?v=n-UBie4Ioqo&t=93s')
    if videocat == 'All' or videocat == 'Religion':
        st.subheader('Religion Category')

        rel1,rel2,rel3,rel4 = st.columns(4)   
        with rel1:
         st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJOJgXuVsfZ4I_S2TJMkviMSrlvYbvjya03A&s')
         st.write('Jesus')
         if st.button('Play Video',key='33'):
            webbrowser.open('https://www.youtube.com/watch?v=EQXyhM592RU')
         st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWqLMtUxLAS_GDcywic76HjwUZ7_274obgEg&s')
         st.write('Abraham')
         if st.button('Play Video',key='34'):
            webbrowser.open('https://www.youtube.com/watch?v=UhuSolM_zZg')
        with rel2:
         st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRX3O3tnTjwu8WPXNQbTf1CkVZn6kojKB8v2w&s')
         st.write('Joseph')
         if st.button('Play Video',key='35'):
            webbrowser.open('https://www.youtube.com/watch?v=rwNz81tgnl4')
         st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSi2b4lUqvqeV9jYfRVakFZtYkYj4mkkMQf4w&s')
         st.write('Esther')
         if st.button('Play Video',key='36'):
            webbrowser.open('https://www.youtube.com/watch?v=dX3Et-GZr_Q')
        with rel3:
         st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZNyXaGaAXT3YTNlfO3lHEHVcv8AqlNmgkSQ&s')
         st.write('David')
         if st.button('Play Video',key='37'):
            webbrowser.open('https://www.youtube.com/watch?v=32_Izk21ktw')
         st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR05oLt9DNLQDYGsEVMKb7OFf1-CZMsxLfkJQ&s')
         st.write('Ruth')
         if st.button('Play Video',key='38'):
            webbrowser.open('https://www.youtube.com/watch?v=jLhVTd-6oE4')    
        with rel4:
         st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRt9A1BOK03pZDefvDvoA6YArOe9qS53bGnfQ&s')
         st.write('Daniel')
         if st.button('Play Video',key='39'):
            webbrowser.open('https://www.youtube.com/watch?v=qBSTCBSlf9Q')
         st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdkM4vHQecNowGe-EtZ0xgEAQR_zH18W2Tlw&s')
         st.write('Elijah')
         if st.button('Play Video',key='40'):
            webbrowser.open('https://www.youtube.com/watch?v=kF9h7hFngYM')
        