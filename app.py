import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
st.set_page_config(
    page_title = "Teste do Streamlit por Gabriel Alves",
    layout = "wide",
    menu_items = {
        'About': "TESTE DO ABOUT"
    }
)

df = pd.read_csv("dataset/acidentes2015.csv",encoding="UTF-8")

print(df.head())

