import streamlit as st

from src.ui.base_layout import (
    style_background_dashboard,
    style_base_layout
)
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard, line
from src.database.db import check_teacher_exists, create_teacher, teacher_login

def teacher_screen():

    style_background_dashboard()
    style_base_layout()

    if "teacher_login_type" not in st.session_state:
        st.session_state.teacher_login_type = "login"

    if st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()


def teacher_screen_login():

    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")

    with c1:
        header_dashboard()

    with c2:
        if st.button(
            "Go Back to Home",
            type="secondary",
            shortcut='control+backspace',
            key="teacher_login_back"
        ):
            st.session_state["login_type"] = None
            st.rerun()

    st.header("Login using password", text_alignment="center")
    
    st.space()
    st.space()
    st.space()

    teacher_username = st.text_input(
        "Enter username",
        placeholder="prince@123"
    )

    teacher_pass = st.text_input(
        "Enter password",
        type="password",
        placeholder="Enter password"
    )

    line()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button(
            "Login",
            icon=":material/passkey:",
            type="primary",
            width='stretch',
            shortcut='control+enter'
        ):
            if teacher_login(teacher_username, teacher_pass):
                st.toast("welcome back!", icon="👋")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid username and password combo")

    with btnc2:
        if st.button(
            "Register Instead",
            type="primary",
            icon=":material/passkey:",
            width='stretch'
        ):
            st.session_state.teacher_login_type = "register"
            st.rerun()

    footer_dashboard()


def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_confirm_pass):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False, "All fields are required!"
    if check_teacher_exists(teacher_username):
        return False, "Username already taken"
    if teacher_pass != teacher_confirm_pass:
        return False, "Password is Doesn't Match"
        
    try:
        create_teacher(teacher_username, teacher_name, teacher_pass)
        return True, "Successfully Created! Login Now "
    except Exception as e:
        return False, "Unexpected Error!"


def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")

    with c1:
        header_dashboard()

    with c2:
        if st.button(
            "Go Back to Home",
            type="secondary",
            shortcut='control+backspace',
            key="teacher_register_back"
        ):
            st.session_state["login_type"] = None
            st.rerun()

    st.header("Register your teacher profile", text_alignment="center")

    st.write("")

    teacher_username = st.text_input(
        "Enter username",
        placeholder="prince@123",
        key="register_username"
    )

    teacher_name = st.text_input(
        "Enter Name",
        placeholder="Prince",
        key="register_name"
    )

    teacher_pass = st.text_input(
        "Enter password",
        type="password",
        placeholder="Enter password",
        key="register_password"
    )

    teacher_confirm_pass = st.text_input(
        "Confirm your password",
        type="password",
        placeholder="Enter password",
        key="register_confirm_password"
    )

    line()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button(
            "Register now",
            type="primary",
            shortcut='control+enter',
            icon=":material/passkey:",
            width='stretch'
        ):
            success, message = register_teacher(teacher_username, teacher_name, teacher_pass, teacher_confirm_pass)
            if success:
                import time 
                time.sleep(2)
                st.session_state.teacher_login_type = "login"
                st.rerun()
            else:
                st.error(message)

    with btnc2:
        if st.button(
            "Login Instead",
            type="primary",
            icon=":material/passkey:",
            width='stretch'
        ):
            st.session_state.teacher_login_type = "login"
            st.rerun()

    footer_dashboard()