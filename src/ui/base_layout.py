import streamlit as st


def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: linear-gradient(135deg, #5865F2 0%, #3f4fe8 100%) !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color: white !important;
                    color: #1e293b !important;
                    padding: 2.5rem !important;
                    border-radius: 2rem !important;
                    box-shadow: 0 10px 30px rgba(88, 101, 242, 0.15) !important;
                    border: 1px solid rgba(88, 101, 242, 0.1) !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: linear-gradient(135deg, #f8f9ff 0%, #f0f3ff 100%) !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
# UI styling for consistent color scheme
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top: 1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
                color: #1e293b !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                color: #5865F2 !important;
                line-height: 0.9 !important;
                margin-bottom: 0rem !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;
                color: #1e293b !important;
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: all 0.25s ease-in-out !important;
                font-weight: 600 !important;
                }

            button:hover {
                background-color: #3f4fe8 !important;
                transform: scale(1.05) !important;
            }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: all 0.25s ease-in-out !important;
                font-weight: 600 !important;
                }

            button[kind="secondary"]:hover {
                background-color: #d63089 !important;
                transform: scale(1.05) !important;
            }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: #64748b !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: all 0.25s ease-in-out !important;
                font-weight: 600 !important;
                }

            button[kind="tertiary"]:hover {
                background-color: #475569 !important;
                transform: scale(1.05) !important;
            }

            /* Divider styling */
            hr {
                border-color: rgba(88, 101, 242, 0.2) !important;
            }

            /* Input styling */
            input {
                border: 2px solid rgba(88, 101, 242, 0.3) !important;
                border-radius: 0.75rem !important;
                padding: 0.75rem !important;
            }

            input:focus {
                border-color: #5865F2 !important;
            }
        </style>  

                """
            ,unsafe_allow_html=True)