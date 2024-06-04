import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def buat_header():
    cols = st.columns([1,1])
    with cols[0]:
        st.markdown("<h1 style='text-align: left; font-size: 15px;'>UMKMPriority</h1>", unsafe_allow_html=True)
    with cols[1]:
        menu=st.radio('', options=['Home', 'Pengajuan', 'myCashFlow', 'WarungKu', 'Pengaturan'], horizontal=True, key='menu')
        return menu
 
pilih_menu = buat_header()
st.divider()
if pilih_menu == 'Home':
    cols = st.columns([1,50,1])
    with cols[1]:
        st.image('pictures/bgdepan.jpg', width=1100)
    st.markdown("<h1 style='text-align: center; font-size: 25px;'>UMKM PRIORITY</h1>", unsafe_allow_html=True)
    st.divider()
    cols = st.columns([3,2])
    with cols[0]:
        st.markdown("<h1 style='text-align: left; font-size: 20px;'>Apa itu UMKM Priority?</h1>", unsafe_allow_html=True)
        st.write("<h1 style='text-align: justify; font-size: 15px; font-weight: normal; '>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fermentum odio eu feugiat pretium nibh ipsum consequat. Non tellus orci ac auctor. At erat pellentesque adipiscing commodo. In egestas erat imperdiet sed euismod nisi. Tempor commodo ullamcorper a lacus vestibulum sed arcu non odio. Et netus et malesuada fames ac turpis egestas maecenas pharetra. Malesuada bibendum arcu vitae elementum curabitur vitae nunc.</h1>", unsafe_allow_html=True)
        with cols[1]:
            st.image('pictures\Depan1.jpg', width=400)
    st.write(
            """
            <div style='background-color: lightblue; padding: 10px; border-radius: 10px;'>
            <h1 style='text-align: center; font-size: 15px; font-weight: bold;'>Berkolaborasi dengan :</h1>
            </div>
            """, 
            unsafe_allow_html=True
        )
    st.text('')
    st.text('')
    st.markdown("<h1 style='text-align: center; font-size: 25px;'>Apa kata mereka?</h1>", unsafe_allow_html=True)
    cols = st.columns([1,1,1])
    with cols[0]:
        container = st.container(border=True)
        container.write("Review dari pelanggan")
    with cols[1]:
        container = st.container(border=True)
        container.write("Review dari pelanggan")
    with cols[2]:
        container = st.container(border=True)
        container.write("Review dari pelanggan")
    st.text('')
    st.text('')

    cols = st.columns([1,1.3])
    with cols[0]:
        st.markdown("<h1 style='text-align: left; font-size: 15px;'>UMKMPriority</h1>", unsafe_allow_html=True)
    with cols[1]:
        review = st.chat_input("Say something")
    st.divider()
    cols = st.columns([1,1,1,1])
    with cols[0]:
        st.write('**Contact Us**')
        st.write('Twenty One')
        st.write('Twenty One')
        st.write('Twenty One')
        st.write('Twenty One')
    with cols[1]:
        st.write('**Column Two**')
        st.write('Twenty One')
        st.write('Twenty One')
        st.write('Twenty One')
        st.write('Twenty One')
    with cols[2]:
        st.write('**Column Three**')
        st.write('Twenty One')
        st.write('Twenty One')
        st.write('Twenty One')
        st.write('Twenty One')
    with cols[3]:
        st.write('**Available On**')
        st.write(
                """
                <div style='text-align: left'>
                    <a href="https://www.apple.com/app-store/" target="_blank" style="margin-right: 10px;">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/6/67/App_Store_%28iOS%29.svg" width="30" alt="Download on the App Store">
                    </a>
                    <a href="https://play.google.com/store" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/7/78/Google_Play_Store_badge_EN.svg" width="100" alt="Get it on Google Play">
                    </a>
                </div>
                """, 
                unsafe_allow_html=True
            )
        st.text('')
        st.write('**Join Us**')
        st.write(
                """
                <div style='text-align: left;'>
                    <a href="https://www.facebook.com" target="_blank" style="margin-right: 10px;">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" width="30" alt="Facebook">
                    </a>
                    <a href="https://www.youtube.com" target="_blank" style="margin-right: 10px;">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" width="30" alt="YouTube">
                    </a>
                    <a href="https://www.instagram.com" target="_blank" style="margin-right: 10px;">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="30" alt="Instagram">
                    </a>
                    <a href="https://www.linkedin.com" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/LinkedIn_Logo.svg" width="50" alt="LinkedIn">
                    </a>
                </div>
                """, 
                unsafe_allow_html=True
            )
    st.divider()
    st.markdown("<h1 style='text-align: left; font-size: 15px; font-weight: normal;'>Copyright © 2024 UMKMPriority. All rights reserved.</h1>", unsafe_allow_html=True)
elif pilih_menu == 'Pengajuan':
    cols = st.columns([1,50,1])
    with cols[1]:
        st.image('pictures/bgdepan.jpg', width=1100)
    st.markdown("<h1 style='text-align: center; font-size: 25px;'>Data Pengajuan</h1>", unsafe_allow_html=True)
    cols = st.columns([1,2])
    with cols[0]:
        st.image('pictures/user.jpg', width=300)    
    with cols[1]:
        with st.form("my_form"):
            nama_pemilik = st.text_input("Nama Pemilik")
            nama_usaha = st.text_input("Nama Usaha")
            d = st.date_input("Didirikan pada Tahun", value=None)
            deskripsi = st.text_input("Deskripsi Usaha")
            pinjaman = st.number_input("Jumlah Pinjaman", min_value=1, max_value=100000000)
            uploaded_files = st.file_uploader("Dokumen Jaminan", accept_multiple_files=True)
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.read()
                st.write("filename:", uploaded_file.name)
                st.write(bytes_data)
            ajukan = st.form_submit_button("Ajukan")
    if ajukan:
        st.write("**Berikut keterangan pengajuan Anda. Mohon tunggu balasan dari penyedia jasa keuangan.**")
        st.write("Nama Pemilik : ", nama_pemilik)
        st.write("Nama Usaha : ", nama_usaha)
        st.write("Didirikan pada Tahun : ", d)
        st.write("Deskripsi Usaha : ", deskripsi)
        st.write("Jumlah Pinjaman : ", pinjaman)
    st.divider()
    st.markdown("<h1 style='text-align: center; font-size: 15px; font-weight: normal;'>Copyright © 2024 UMKMPriority. All rights reserved.</h1>", unsafe_allow_html=True)
elif pilih_menu == 'myCashFlow':
    cols = st.columns([1,50,1])
    with cols[1]:
        st.image('pictures/bgdepan.jpg', width=1100)
    st.markdown("<h1 style='text-align: center; font-size: 25px;'>Analisis Tahun 2024</h1>", unsafe_allow_html=True)
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)
    
    cols = st.columns([1,0.7])
    with cols[0]:
        st.text('')
        st.write('**Persentase Resiko**')
        # data
        labels = ['Income', 'Riwayat Kredit', 'Data Pendukung', 'Keterampilan']
        sizes = [30, 12.5, 12.5, 20]
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
        explode = (0.1, 0, 0, 0)  # explode the 1st slice (Income)
        # process
        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax.axis('equal')
        st.pyplot(fig)
    with cols[1]:
        st.write('**Income**')
        # Data 
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        income = [5000, 6000, 5500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000]
        # process
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(months, income, color='skyblue')  # Use bar() for vertical bars
        ax.set_xlabel('Months')
        ax.set_ylabel('Income ($)')
        ax.set_title('Income per Month')
        plt.xticks(rotation=45)
        st.pyplot(fig)

        st.write('**Riwayat Kredit**')
        # Data 
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        income = [5000, 6000, 5500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000]
        # process
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(months, income, color='skyblue')  # Use bar() for vertical bars
        ax.set_xlabel('Months')
        ax.set_ylabel('Income ($)')
        ax.set_title('Income per Month')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    st.markdown("<h1 style='text-align: center; font-size: 20px;'>Dokumentasi Pengajuan</h1>", unsafe_allow_html=True)
    cols = st.columns([1,1,1])
    with cols[0]:
        st.image('pictures/bgdepan.jpg')
    with cols[1]:
        st.image('pictures/bgdepan.jpg')
    with cols[2]:
        st.image('pictures/bgdepan.jpg')
    st.divider()
    st.markdown("<h1 style='text-align: center; font-size: 15px; font-weight: normal;'>Copyright © 2024 UMKMPriority. All rights reserved.</h1>", unsafe_allow_html=True)
elif pilih_menu == 'WarungKu':
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
            d = st.date_input("Didirikan pada Tahun", value=None)
            deskripsi = st.text_input("Deskripsi Usaha")
            income = st.number_input("Pendapatan Bulanan", min_value=1, max_value=100000000)
            uploaded_files = st.file_uploader("Dokumen UMKM", accept_multiple_files=True)
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.read()
                st.write("filename:", uploaded_file.name)
                st.write(bytes_data)
            submitted = st.form_submit_button("Submit")
    if submitted:
            # Tampilkan
            st.write(f'Halo! **{nama_pemilik}** berikut ada data diri Anda.')  
            st.write(f'Nama Usaha: **{nama_usaha}**')
            st.write(f'Umur: **{age}** tahun')
            st.write(f'Didirikan pada Tahun: **{d}**')
            st.write(f'Deskripsi Usaha: **{deskripsi}**')
            st.write(f'Pendapatan Bulanan: **{income}**')
            st.write(f'Dokumen UMKM: {uploaded_files}')
elif pilih_menu == 'Pengaturan':
    cols = st.columns([1,4.5,1])
    with cols[2]:
        on = st.toggle("Pemberitahuan")
        if on:
            st.write("Pemberitahuan Aktif!")
    settings_options = {
        "Perbaharui Kontak Pribadi": ["Username", "Password", "No. Hp"],
        "Pilih Bahasa": ["Indonesia", "Inggris"],
        "Kebijakan Privasi": ["Kebijakan Privasi", "Baca Kebijakan Privasi"],
        "Syarat dan Ketentuan": ["Syarat dan Ketentuan", "Setuju", "Tidak Setuju"], 
        "Hubungi Kami": ["Hubungi Kami", "Informasi Kontak"],
    }

    # Define functions for setting actions (replace with actual implementation)
    def update_contact_info(username, password, phone_number):
        # update informasi kontak di database
        pass

    def change_language(language):
        # update bahasa
        pass


    for setting_name, setting_options in settings_options.items():
        with st.expander(setting_name):
            if setting_name == "Perbaharui Kontak Pribadi":
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                phone_number = st.text_input("No. Hp")
                if st.button("Simpan"):
                    update_contact_info(username, password, phone_number)
            elif setting_name == "Pilih Bahasa":
                selected_language = st.selectbox("Pilih Bahasa", setting_options)
                if selected_language == "Inggris":
                    # implementasikan logika untuk merubah bahasa
                    pass  
            elif setting_name == "Kebijakan Privasi":
                st.write("**Isi Kebijakan Privasi UMKM Priority akan ditampilkan disini.**")
            elif setting_name == "Syarat dan Ketentuan":
                st.write("**Isi Syarat dan Ketentuan UMKM Priority akan ditampilkan disini.**")
                agree_to_terms = st.checkbox("Saya setuju dengan Syarat dan Ketentuan")
                if st.button("Setuju"):
                    if agree_to_terms:
                        # implementasikan logika untuk persetujuan
                        pass  
                    else:
                        st.warning("Anda harus menyetujui Syarat dan Ketentuan untuk melanjutkan.")
            elif setting_name == "Hubungi Kami":
                st.write("**Informasi kontak UMKM Priority akan ditampilkan disini.**")
            elif len(setting_options) == 2:
                if setting_options[1] == "Open in new tab":
                    st.markdown(f"[Link]({setting_options[0]})", unsafe_allow_html=True)
                else:
                    st.write(setting_options[0])
                    # (e.g., update username, password, etc.)
            else:
                # (e.g., language selection)
                selected_option = st.selectbox("Pilih", setting_options)
                if selected_option == "Indonesia":
                    change_language("Indonesia")
                elif selected_option == "Inggris":
                    change_language("Inggris")