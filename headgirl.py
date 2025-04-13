#Create a voting app for a school:
#8 contestants are going for the position of the head girl
#Create 4 columns with each picture of the contestant and the names
#Place a button each to vote for each of them
#When any contestant is clicked it adds to the points in the csv
#In another page, show the pie chart of the voting poll
import streamlit as st
import pandas as pd 
import plotly.express as px
csvlink = 'winner.csv'
try:
    readcsv = pd.read_csv(csvlink)
except:
    readcsv = pd.DataFrame()
menu= st.sidebar.selectbox('Choose Page',['Voting Page','See Votes'])
if menu== 'See Votes':
    st.title('Voting Results')
    melt_tables = readcsv.melt(var_name='Contestant',value_name='Votes')
    fig = px.pie(melt_tables,values='Votes',names='Contestant')
    st.plotly_chart(fig)
if menu== 'Voting Page':
    st.title('Voting Page')
    head1,head2,head3,head4 = st.columns(4)
    with head1:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqgqeqTlWxd_J8vjVd42LHaUoooumSQQiIsg&s')
        st.write('Avery')
        if st.button ('Cast Vote',key=1):
            try:
                readcsv.loc[0,'Avery'] +=1
            except KeyError:
                readcsv.loc[0,'Avery'] =1
            readcsv.to_csv(csvlink,index=False)
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOUVP86M9OFHjUVCdnXh3tXAdF1R5p5qguAA&s')
        st.write('Reyna')
        if st.button ('Cast Vote',key=2):
            try:
                readcsv.loc[0,'Reyna'] +=1
            except KeyError:
                readcsv.loc[0,'Reyna'] =1
            readcsv.to_csv(csvlink,index=False)
    with head2:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTObXpxHQ9uZuwb-4AznXnUdFeyrwNiFPYyqA&s')
        st.write('Claire')
        if st.button('Cast Vote',key=3):
            try:
             readcsv.loc[0,'Claire'] +=1
            except KeyError:
                readcsv.loc[0,'Claire'] =1
        readcsv.to_csv(csvlink,index=False)
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6pYI7R5e7mEhI-wNzII-6zBHLH7GcYcZlrA&s')
        st.write('Gigi')
        if st.button('Cast Vote',key=4):
          try:
             readcsv.loc[0,'Gigi'] +=1
          except KeyError:
             readcsv.loc[0,'Gigi'] =1
        readcsv.to_csv(csvlink,index=False)
    with head3:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzbvEsOMS-jbCS2RLYeypGJUhpW0F-2T0Uvg&s') 
        st.write('Eve')
        if st.button('Cast Vote',key=5):
          try:
             readcsv.loc[0,'Eve'] +=1
          except KeyError:
             readcsv.loc[0,'Eve '] =1
        readcsv.to_csv(csvlink,index=False)
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-jIS9ghPSQXTD7ZPJzEqzOBMlh7xsS8WmSw&s') 
        st.write('Maya')
        if st.button('Cast Vote',key=6):
          try:
             readcsv.loc[0,'Maya'] +=1
          except KeyError:
             readcsv.loc[0,'Maya'] =1
        readcsv.to_csv(csvlink,index=False)
    with head4:
       st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEtW0INsnOoPFwwdmsRPF_vJGRdSg2ZZdP8A&s') 
       st.write('Rose')
       if st.button('Cast Vote',key=7):
          try:
             readcsv.loc[0,'Rose'] +=1
          except KeyError:
             readcsv.loc[0,'Rose '] =1
       readcsv.to_csv(csvlink,index=False)
       st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmziJI8fEgxkpp3R5QA7tLViQCtd55CfjzDg&s') 
       st.write('Leah')
       if st.button('Cast Vote',key=8):
          try:
             readcsv.loc[0,'Leah'] +=1
          except KeyError:
             readcsv.loc[0,'Leah '] =1
       readcsv.to_csv(csvlink,index=False)