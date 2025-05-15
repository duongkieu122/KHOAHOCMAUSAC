import streamlit as st
st.set_page_config(
    page_title="Khoa học Màu sắc", layout="wide"
)

col1, col2 = st.columns([4, 1])
with col1:
    st.markdown("<div class='title'>Chào mừng bạn đến với project <i>Khoa học Màu sắc</i>!</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Dự án này được thực hiện bởi nhóm sinh viên HCMUTE.</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='info-box'>
        <h4>Thành viên nhóm:</h4>
        <ul>
            <li><b>Kiều Hồng Dương</b> - MSSV: 22158050</li>
            <li><b>Tống Ngân Huỳnh</b> - MSSV: 22158061</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("logo-hcmute.jpg", width=140)
