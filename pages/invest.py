import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.page_link("app.py", label="Home")
st.page_link("pages/signIn.py", label="Sign In")
st.page_link("pages/about.py", label="About")
st.page_link("pages/invest.py", label="Invest")
st.page_link("pages/admin.py", label="Admin")

umkm_data = pd.read_csv("umkm_data.csv")
investment_data = pd.read_csv("pinjaman_data.csv")

#st.set_page_config(layout="centered")

st.title("Platform Invest UMKM Priority")
st.subheader("Mempertemukan Investor dan UMKM")

with st.sidebar:
    menu = st.sidebar.selectbox('**Menu Bank/Investor**', options=['Data Pengajuan', 'Riwayat Pengajuan', 'Profil'])

if menu == 'Data Pengajuan':
    umkm_names = umkm_data["Nama UMKM"].unique()
    selected_umkm_name = st.selectbox("Pilih Nama UMKM", umkm_names)

    if selected_umkm_name:
        selected_umkm_info = umkm_data[umkm_data["Nama UMKM"] == selected_umkm_name]
        st.subheader(f"Profil UMKM: {selected_umkm_name}")
        st.write(selected_umkm_info.iloc[0].to_dict())

        st.subheader("Analisis UMKM")
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

        approval_confirmed = st.button("Setujui Pinjaman")
        rejection_confirmed = st.button("Tolak Pinjaman")

        if approval_confirmed:
            if st.button("Konfirmasi Setujui Pinjaman"):
                st.success(f"Pinjaman UMKM {selected_umkm_name} telah disetujui!")

        if rejection_confirmed:
            if st.button("Konfirmasi Tolak Pinjaman"):
                st.warning(f"Pinjaman UMKM {selected_umkm_name} telah ditolak!")

elif menu == 'Riwayat Pengajuan':
    approved_applications = investment_data[investment_data["Status"] == "Disetujui"]
    st.table(approved_applications[['Nama UMKM', 'Tanggal Persetujuan', 'Tanggal Pelunasan']])

elif menu == 'Profil':
    bank_info = {
        "Nama Bank/Investor": "Bank Contoh",
        "Alamat": "Jalan Contoh No. 1",
        "Email": "bankcontoh@example.com",
        "Telepon": "+628123456789"
    }

    for key, value in bank_info.items():
        st.write(f"{key}: {value}")

    with st.form("Edit Profil"):
        updated_bank_info = {}
        for key, value in bank_info.items():
            updated_value = st.text_input(key, value)
            updated_bank_info[key] = updated_value

        if st.form_submit_button("Simpan"):
            bank_info.update(updated_bank_info)
            st.success("Profil telah diperbarui!")
