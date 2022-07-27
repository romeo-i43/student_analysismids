import streamlit as st
import pandas as pd
import plotly_express as px
import time
from streamlit_lottie import st_lottie
import requests
@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8')

def app():
    hide_st_style1 = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style1, unsafe_allow_html=True)
    hide_st_style = """
            <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)
    st.title("Classification based on your requirement")
    st.markdown('<head><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>',unsafe_allow_html=True)
    st.markdown('---')
    df=pd.read_csv('sample6.csv',index_col=[0])
    st.sidebar.header("customtable")
    g=st.sidebar.radio("classify based on",('roll_no','percent'))
    if g=='roll_no':
        try:
            st.subheader("based on roll_no")
            k=df['roll_no'].unique().tolist()
            select=st.multiselect('select',k)
            k=df['roll_no'].isin(select)
            k=df[k].reset_index()
            del k['index']
            st.dataframe(k)
            csv = convert_df(k)
            st.download_button("Press to Download",csv,"file.csv","text/csv",key='download-csv')
        
        except:
            pass

    elif g=='percent':
        try:
            st.subheader("based on percentage")
            min=st.slider('select min percent',1,100,1)
            max=st.slider('select max percent',1,100,1)
            k=df[df['percentage']>=min]
            k=k[k['percentage']<=max]
            k=k.reset_index()
            del k['index']
            st.dataframe(k)
            csv = convert_df(k)
            st.download_button("Press to Download",csv,"file.csv","text/csv",key='download-csv')

        except:
            pass
    
