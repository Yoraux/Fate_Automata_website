import streamlit as st

def load_style():
    page_bg = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: rgb(33, 33, 33); /* dark background */
        color: white; /* make text readable */
    }

    [data-testid="stHeader"] {
        background: rgba(0,0,0,0); /* transparent header */
    }

    [data-testid="stSidebar"] {
        background-color: rgb(24, 24, 24); /* dark sidebar */
        color: white;
    }

    /* Optional: center titles and add spacing */
    h1, h2, h3 {
        text-align: center;
    }
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)
