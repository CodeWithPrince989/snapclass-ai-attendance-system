import streamlit as st


def footer_home():
    st.markdown(f"""
        <div style="margin-top: 2rem; display: flex; gap: 10px; justify-content: center; align-items: center; padding: 1.5rem; background: rgba(255, 255, 255, 0.1); border-radius: 1rem;">
        <p style="font-weight: 600; color: white; margin: 0;"> Created with ❤️ by Prince</p>  
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():    
    st.markdown(f"""
        <div style="margin-top: 2rem; display: flex; gap: 10px; justify-content: center; align-items: center; padding: 1.5rem; background: linear-gradient(135deg, #f0f3ff 0%, #fef3f8 100%); border-radius: 1rem; border: 1px solid #e0e7ff;">
        <p style="font-weight: 600; color: #1e293b; margin: 0;"> Created with ❤️ by Prince</p>  
        </div>
                
                """, unsafe_allow_html=True)
