import streamlit as st
import pandas as pd
import plotly_express as px
import time
from streamlit_lottie import st_lottie
import requests

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

    st.title("plot based on your requirement")
    st.markdown('<head><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>',unsafe_allow_html=True)
    st.markdown('---')
    df=pd.read_csv('sample.csv')
    st.sidebar.header("customplot")
    st.sidebar.write("classify based on")
    g=st.sidebar.radio("what's your choice",('roll_no','totalmarks','percent'))
    if g=='roll_no':
        try:
            st.subheader("based on roll_no")
            k=df['roll_no'].unique().tolist()
            select=st.multiselect('select',k)
            k=df['roll_no'].isin(select)
            k=df[k].reset_index()
            del k['index']
            g1=px.bar(
            k,
            x=k['roll_no'],
            y=[k['totalmarks'],k['percent']],
            )
            st.plotly_chart(g1)

        except:
            def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()

            lottie_url = "https://assets6.lottiefiles.com/datafiles/aba45c7b75d547282b2dbdc97969412b/progress_bar.json"
            lottie_json = load_lottieurl(lottie_url)
            st_lottie(lottie_json)

    elif g=='percent':
        st.subheader("based on percent")
        min=st.slider('select min percent',1,100,1)
        max=st.slider('select max percent',1,100,1)
        try:
            k=df[df['percent']>=min]
            k=k[k['percent']<=max]
            k=k.reset_index()
            del k['index']
            g1=px.bar(
            k,
            x=k['roll_no'],
            y=[k['percent'],k['totalmarks']],
            )
            st.plotly_chart(g1)
        
        except:
            def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()

            lottie_url = "https://assets8.lottiefiles.com/private_files/lf30_cc9cxym5.json"
            lottie_json = load_lottieurl(lottie_url)
            st_lottie(lottie_json)
    
    elif g=='totalmarks':
        try:
            st.subheader("based on marks")
            min=st.slider('select min marks',1,150,1)
            max=st.slider('select max marks',1,150,1)
            k=df[df['totalmarks']>=min]
            k=k[k['totalmarks']<=max]
            k=k.reset_index()
            del k['index']
            g1=px.bar(
            k,
            x=k['roll_no'],
            y=[k['totalmarks'],k['percent']],
            )
            st.plotly_chart(g1)

        except:
            def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()

            lottie_url = "https://assets8.lottiefiles.com/private_files/lf30_cc9cxym5.json"
            lottie_json = load_lottieurl(lottie_url)
            st_lottie(lottie_json)
    