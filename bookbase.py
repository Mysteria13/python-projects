import streamlit as st
bill=0
st.set_page_config(layout='wide')
st.title('Book App made by Lisa')
col1,col2,col3,col4= st.columns (4)
with col1:
    Book_collections =st. selectbox ("Choose any Category",['Choose an option',"Children's Books","Teen's Books","Family's Books","Christian Books","Science Books"])

if Book_collections == "Children's Books":
    st.subheader("Children's Books")
    child1, child2,child3 , child4 = st.columns(4)
    with child1:
        st.image('https://m.media-amazon.com/images/I/71RrZCD04IL._AC_UL320_.jpg')
    
        if st.checkbox ("The Wonky Donkey: $20"):
            bill+= 20
            st.write ('Ok Done')

    with child2:
        st.image ("https://kreafolk.com/cdn/shop/articles/30-cutest-children-s-book-cover-designs-kreafolk_1f034759-9fe1-4403-b8d2-8316c0d99f42.jpg?v=1717726068&width=2048")


        if st.checkbox ("The Fairy Forest : $15"):
            bill+= 15
            st.write ('Ok Done')

    with child3:
        st.image ("https://m.media-amazon.com/images/I/61kJ6fodnkL._AC_AIweblab1028570,T2_SF218,282_QL85_.jpg?aicid=productui-image-1")


        if st.checkbox ("My Friend the Marshmallow Man: $15"):
            bill+= 15
            st.write ('Ok Done')        

    with child4:
        st.image ("https://m.media-amazon.com/images/I/714s9I3uxlL._AC_AIweblab1028570,T2_SF218,282_QL85_.jpg?aicid=productui-image-1")

        if st.checkbox ("Love You Forever: $25"):
            bill+= 25
            st.write ('Ok Done')                

if Book_collections == "Teen's Books":
    st.subheader("Teen's Books")
    teen1,teen2,teen3,teen4 = st.columns(4)
    with teen1:
        st.image('https://m.media-amazon.com/images/I/61-eg9kdgiL._AC_AIweblab1028570,T2_SF218,282_QL85_.jpg?aicid=productui-image-1')
        
    
        if st.checkbox ("Shadow Jumper: $19"):
            bill+= 19
            st.write ('Ok Done')
    
    with teen2:
        st.image ("https://m.media-amazon.com/images/I/81e2k82EOHL._AC_AIweblab1028570,T2_SF218,282_QL85_.jpg?aicid=productui-image-1")

        if st.checkbox ("What happened to Rachel Riley : $16"):
            bill+= 16
            st.write ('Ok Done')

    with teen3:
        st.image ("https://m.media-amazon.com/images/I/91-fE4Scx8L._AC_AIweblab1028570,T2_SF218,282_QL85_.jpg?aicid=productui-image-1")

        if st.checkbox ("The Lost Hero: $25"):
            bill+= 25
            st.write ('Ok Done')        

    with teen4:
        st.image ("https://m.media-amazon.com/images/I/9101MLPcFTL._AC_AIweblab1028570,T2_SF320,264_QL85_.jpg?aicid=productui-image-1")
        
        if st.checkbox ("Onyx Storm: $20"):
            bill+= 20
            st.write ('Ok Done')    

if Book_collections == "Family's Books":
    st.subheader ("Family's Books")
    fam1,fam2,fam3,fam4 = st.columns(4)
    with fam1:
        st.image ("https://m.media-amazon.com/images/I/816M6LSn4NL._AC_AIweblab1028570,T2_SF218,282_QL85_.jpg?aicid=productui-image-1")
       

        if st.checkbox ("My family,Your family : $12"):
            bill+=12
            st.write ("Ok Done")


    with fam2:
        st.image ("https://m.media-amazon.com/images/I/81mFBsBFYXL._AC_AIweblab1028570,T2_SF218,282_QL85_.jpg?aicid=productui-image-1")

        if st.checkbox ("Hot Mess: $22"):
            bill+=22
            st.write ("Ok Done")        


    with fam3:
        st.image ("https://m.media-amazon.com/images/I/815ErykFVXL._AC_AIweblab1028570,T2_SF218,282_QL85_.jpg?aicid=productui-image-1")
        if st.checkbox (" One and only Family: $20"):
            bill+=20
            st.write ("Ok Done")   


    with fam4:
        st.image ("https://m.media-amazon.com/images/I/71cP-MgoUEL._AC_AIweblab1028570,T2_SF218,282_QL85_.jpg?aicid=productui-image-1")
        if st.checkbox ("I got This: $20"):
         bill+=20
         st.write ("Ok Done")  


if st.button ("check amount "):
    st.write('your final amount is',bill,'dollars')