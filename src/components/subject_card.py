import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background: white; border-left: 6px solid #5865F2; padding: 25px; border-radius: 12px; border: 1px solid #e0e7ff; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(88, 101, 242, 0.08);">
        <h3 style="margin: 0; color: #1e293b; font-size: 1.5rem;">{name}</h3>
        <p style="color: #64748b; margin: 10px 0;">Code : <span style="background: #f0f3ff; color: #5865F2; padding: 4px 10px; border-radius: 6px; font-weight: 600;">{code}</span> | Section : {section}</p>
        
        """
    
    if stats:
        html+= """
        <div style="display:flex; gap:12px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: #f0f3ff; padding: 8px 14px; border-radius: 8px; font-size: 0.9rem; color: #1e293b; border: 1px solid #e0e7ff;">{icon} <b style="color: #5865F2;">{value}</b> {label}</div>'
        
        html+= "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
