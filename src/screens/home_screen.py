import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout
from src.ui.base_layout import style_background_dashbroard



def home_screen():

    header_home()

    style_background_dashbroard()

    style_base_layout()

    col1, col2 = st.columns([1, 2], gap='Large')
    with col1:
        if st.button("Student Login", key='btn1'):
           st.session_state['login_type'] = 'student'
           st.rerun()
    with col2:
        if st.button("Teacher Login", key='btn2'):
           st.session_state['login_type'] = 'teacher'
           st.rerun()



