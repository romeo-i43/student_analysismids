import streamlit as st
import pandas as pd
import plotly_express as px
import base64
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
    st.title('ploty')
    st.subheader('table')
    st.markdown('<head><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>',unsafe_allow_html=True)
    st.markdown('---')
    df=pd.read_csv('sample6.csv',index_col=[0])
    st.dataframe(df)
    csv = convert_df(df)
    st.download_button("Press to Download",csv,"file.csv","text/csv",key='download-csv')
