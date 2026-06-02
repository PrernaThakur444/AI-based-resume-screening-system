import streamlit as st

def show_header():
    st.markdown("""
    <div style='text-align:center; padding:20px;'>
        <h1 style='color:#38bdf8;'>🚀 AI Resume Dashboard</h1>
        <p style='color:#94a3b8;'>Smart Hiring • AI Powered • Explainable Results</p>
    </div>
    """, unsafe_allow_html=True)