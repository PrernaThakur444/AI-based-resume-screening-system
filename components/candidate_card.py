import streamlit as st

def show_candidate(candidate):

    st.markdown(f"""
    <div style="
        background:#1e293b;
        padding:20px;
        border-radius:12px;
        margin-bottom:15px;
    ">
    <h3 style='color:#38bdf8;'>👤 {candidate['Name']}</h3>

    <p>
    📧 {candidate['Email']} <br>
    📞 {candidate['Phone']} <br>
    🎓 {candidate['Education']} <br>
    💼 {candidate['Experience']} yrs
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.progress(int(candidate["Total Score"]))

    st.success(candidate["Why Selected"])