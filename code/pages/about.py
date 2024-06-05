import streamlit as st

cols = st.columns([3,2])
with cols[0]:
    if st.button("<< Home"):
        st.switch_page("app.py")
    st.title("Hai, ada yang bisa kami bantu?")
    search_query = st.chat_input("Cari informasi disini")
    st.write("Topik populer : ")
with cols[1]:
    st.image("pictures/informasi.png")

st.header("Info Penting")
cols = st.columns([1,1,1])
with cols[0]:
    st.write(
            """
            <div style='background-color: lightblue; padding: 10px; border-radius: 10px;'>
            <h1 style='text-align: center; font-size: 20px; font-weight: bold;'>Biaya Admin</h1>
            <h2 style='text-align: center; font-size: 15px;'>Biaya Admin</h2>
            </div>
            """, 
            unsafe_allow_html=True
        )
with cols[1]:
    st.write(
            """
            <div style='background-color: lightblue; padding: 10px; border-radius: 10px;'>
            <h1 style='text-align: center; font-size: 20px; font-weight: bold;'>Biaya Admin</h1>
            <h2 style='text-align: center; font-size: 15px;'>Biaya Admin</h2>
            </div>
            """, 
            unsafe_allow_html=True
        )
with cols[2]:
    st.write(
            """
            <div style='background-color: lightblue; padding: 10px; border-radius: 10px;'>
            <h1 style='text-align: center; font-size: 20px; font-weight: bold;'>Biaya Admin</h1>
            <h2 style='text-align: center; font-size: 15px;'>Biaya Admin</h2>
            </div>
            """, 
            unsafe_allow_html=True
        )
st.divider()
st.markdown("<h1 style='text-align: center; font-size: 15px; font-weight: normal;'>Copyright © 2024 UMKMPriority. All rights reserved.</h1>", unsafe_allow_html=True)