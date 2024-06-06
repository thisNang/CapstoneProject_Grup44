import streamlit as st

cols = st.columns([3,1.3,1,1.2,1.2,1.2,1.2,1])
with cols[0]:
    st.markdown("<h1 style='text-align: left; font-size: 15px;'>UMKMPriority</h1>", unsafe_allow_html=True)
with cols[2]:
    if st.button("Home"):
        st.switch_page("Home.py")
with cols[3]:
    if st.button("Pengajuan"):
        st.switch_page("pages/Pengajuan.py")
with cols[4]:
    if st.button("myCashflow"):
        st.switch_page("pages/MyCashFlow.py")
with cols[5]:
    if st.button("WarungKu"):
        st.switch_page("pages/WarungKU.py")
with cols[6]:
    if st.button("Pengaturan"):
        st.switch_page("pages/Pengaturan.py")
st.divider()

st.write("**WarungKu**")

st.markdown("<h1 style='text-align: center; font-size: 25px;'>Profil UMKM</h1>", unsafe_allow_html=True)
cols = st.columns([1.5,1,1.5])
with cols[1]:
    st.image('pictures/user.jpg', width=250)
    uploaded_files = st.file_uploader("Upload Photo", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)
            st.write(bytes_data)
with st.form("my_form"):
        nama_pemilik = st.text_input("Nama Pemilik")
        nama_usaha = st.text_input("Nama Usaha")
        age = st.number_input('Umur', min_value=0, max_value=120)
        jenis_kelamin = st.text_input("Jenis Kelamin")
        income = st.number_input("Pendapatan Bulanan", min_value=1, max_value=100000000)
        education = st.text_input("Pendidikan")
        status_pernikahan = st.text_input("Status Pernikahan")
        employee = st.number_input('Jumlah Pegawai', min_value=0, max_value=120)
        status_kepemilikan = st.text_input("Status Kepemilikan")
        submitted = st.form_submit_button("Submit")
if submitted:
        # Tampilkan
        st.write(f'Halo! **{nama_pemilik}** berikut ada data diri Anda.')  
        st.write(f'Nama Usaha: **{nama_usaha}**')
        st.write(f'Umur: **{age}** tahun')
        st.write(f'Jenis Kelamin: **{jenis_kelamin}**')
        st.write(f'Pendapatan Bulanan: **{income}**')
        st.write(f'Pendidikan: **{education}**')
        st.write(f'Status Pernikahan: **{status_pernikahan}**')
        st.write(f'Jumlah Pegawai: **{employee}**')
        st.write(f'Status Kepemilikan: **{status_kepemilikan}**')

st.divider()
st.markdown("<h1 style='text-align: center; font-size: 15px; font-weight: normal;'>Copyright © 2024 UMKMPriority. All rights reserved.</h1>", unsafe_allow_html=True)