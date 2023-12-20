import os
import streamlit as st
# import pandas as pd

from streamlit import components
# from urllib.error import URLError

MAIN_PATH = os.getcwd()
WEB_DATA = os.path.join(MAIN_PATH, 'website_data')
LDA_PATH = os.path.join(WEB_DATA, 'lda.html')

st.write(
    """
    This demo shows how to use `st.write` to visualize Pandas DataFrames.
    """
)

with open(LDA_PATH, 'r', encoding='utf-8') as f:
    html_string = f.read()
components.v1.html(html_string, width=1000, height=600, scrolling=True)
