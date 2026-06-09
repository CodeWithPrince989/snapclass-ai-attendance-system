import streamlit as st

def footer_home():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center;">
        <p style="font-weight:bold; color:black;"> Created With ❤️ by Prince </p>
        </div>

    """, unsafe_allow_html=True)

def footer_dashboard():
        st.markdown("""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center;">
        <p style="font-weight:bold; color:black;"> Created With ❤️ by Prince </p>
        </div>

    """, unsafe_allow_html=True)
        
def line():
    st.markdown(
    "<hr style='border:0.5px solid gray;'>",
    unsafe_allow_html=True
)