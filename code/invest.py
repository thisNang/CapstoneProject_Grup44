import streamlit as st
import pandas as pd

umkm_data = pd.read_csv("umkm_data.csv")
investment_data = pd.read_csv("pinjaman_data.csv")

st.set_page_config(layout="wide")

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
        st.write("**Analisis Risiko:** (replace with risk assessment data)")
        st.write("**Prospek Usaha:** (replace with business prospect analysis)")

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
