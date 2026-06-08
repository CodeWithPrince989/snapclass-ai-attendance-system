import streamlit as st

def main():
    st.header("This Is title")
    st.text_input('Enter your name', 'Type here...')
    col1, col2, col3 = st.columns(3, gap='large')
    with col1:
        if st.button('Submit 1', type='primary', key='btn1', width=''):
            print("hi prince 1")
    with col2:
        if st.button('Submit 2', type='secondary', key='btn2', width='stretch'):
            print("hi prince 2")
    with col3:
        if st.button('Submit 3', type='tertiary', key='btn3', width='stretch'):
            print("hi prince 3")

    st.markdown("""
        <div>
            <img src='https://i.ibb.co/YTYGn5qV/logo.png' />
            <h1>Snap Classes</h1>
        </div>
        <style>
            button{
                background:orange !important;
            }
    """, unsafe_allow_html=True)
main()


st.title("Hello Streamlit-er 👋")
st.markdown(
    """ 
    This is a playground for you to try Streamlit and have fun. 

    **There's :rainbow[so much] you can build!**
    
    We prepared a few examples for you to get started. Just 
    click on the buttons above and discover what you can do 
    with Streamlit. 
    """
)

if st.button("Send balloons!"):
    st.balloons()