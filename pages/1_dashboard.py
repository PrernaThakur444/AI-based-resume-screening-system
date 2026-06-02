import streamlit as st
from components.header import show_header

show_header()

st.subheader("📊 Overview")

col1, col2, col3 = st.columns(3)

col1.metric("📄 Jobs", 1)
col2.metric("📑 Resumes", 10)
col3.metric("⭐ Avg Score", "72%")

st.markdown("---")

st.subheader("⚡ Quick Actions")

st.button("➕ New Job")
st.button("📊 View Analytics")