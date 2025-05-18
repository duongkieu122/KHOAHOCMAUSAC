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
    # CSS để làm ảnh avatar tròn
    st.markdown("""
        <style>
        .avatar img {
            border-radius: 50%;
            width: 100px;
            height: 100px;
            object-fit: cover;
            margin-bottom: 5px;
        }
        .avatar-name {
            text-align: center;
            font-size: 14px;
            color: #444;
        }
        </style>
    """, unsafe_allow_html=True)

    # Hiển thị 2 ảnh thành viên theo chiều ngang
    member_col1, member_col2 = st.columns(2)

    with member_col1:
        st.markdown("<div class='avatar'>", unsafe_allow_html=True)
        st.image("KHDuong.jpg")
        st.markdown("<div class='avatar-name'>Kiều Hồng Dương</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with member_col2:
        st.markdown("<div class='avatar'>", unsafe_allow_html=True)
        st.image("TNHuynh.jpg")
        st.markdown("<div class='avatar-name'>Tống Ngân Huỳnh</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
