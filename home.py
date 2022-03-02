import streamlit as st
from streamlit_lottie import st_lottie
import requests

def app():
    hide_st_style1 = """
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            header {visibility:hidden;}
            </style>
            """
    st.markdown(hide_st_style1, unsafe_allow_html=True)
    hide_st_style = """
            <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_url = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json"
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json)

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_url = "https://assets6.lottiefiles.com/private_files/lf30_ovxvpeuq.json"
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json)

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_url = "https://assets9.lottiefiles.com/private_files/lf30_eaigvcxb.json"
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json)


