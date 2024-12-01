import streamlit as st 
st.set_page_config(layout='wide')

st.title('Eletronic order App made by Lisa')
st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Ffr.123rf.com%2Fphoto_43149221_d%25C3%25A9finir-des-appareils-%25C3%25A9lectrom%25C3%25A9nagers-et-des-appareils-%25C3%25A9lectroniques-ic%25C3%25B4nes-isol%25C3%25A9s-vector.html&psig=AOvVaw2aZh3nQyj4xqWRyWyKRGVb&ust=1727387232821000&source=images&cd=vfe&opi=89978449&ved=0CBcQjhxqFwoTCODYqYeJ34gDFQAAAAAdAAAAABAR")
bill = 0
st.subheader("Home Category")
Home1,Home2,Home3,Home4= st.columns(4)

with Home1:
   if st.checkbox("Lamp: $30"):
    bill += 30
   st.write("Ok Done")

with Home2:
    if st.checkbox("Blender: $45"):
      bill += 45 
      st.write("Ok Done")

with Home3:
    if st.checkbox("Vaccum: $25"):
      bill += 25
      st.write("Ok Done") 

with Home4:
  if st.checkbox("TV : $70"):
     bill +=70
     st.write("Ok Done")



st.subheader("School Category")
school1,school2,school3,school4= st.columns(4)

with school1:
    if st.checkbox("Laptop: $43"):
      bill += 43
    st.write("Ok Done")

with school2:
       if st.checkbox("Electric Whiteboard: $65"):
        bill += 65
        st.write("Ok Done")

with school3:
      if st.checkbox("Projector: $75"):
         bill += 75
         st.write("Ok Done") 

with school4:
      if st.checkbox(" Printer: $85"):
            bill += 85
      st.write("Ok Done")


st.subheader("Office Category")
office1,office2,office3, office4= st.columns(4)

with office1:
    if st.checkbox("Printer: $85"):
      bill += 85
    st.write("Ok Done")

with office2:
       if st.checkbox("Wifi Router: $30"):
          bill += 30
       st.write("Ok Done")

with office3:
      if st.checkbox("Copier: $25"):
         bill += 25
         st.write("Ok Done") 

with office4:
      if st.checkbox(" Projectors: $30"):
         bill += 30
         st.write("Ok Done")
            

if st.button("Check Bill"):
    st.write("Your Bill is", bill," dollars")
                                         
