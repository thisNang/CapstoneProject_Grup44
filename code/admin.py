import streamlit as st
import pandas as pd
import hashlib
import numpy as np

# Fungsi untuk hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Sidebar untuk Menu
menu = st.sidebar.selectbox('**Menu Admin**', options=['Data User', 'Pengajuan'])

if menu == 'Data User':
    st.title("Grafik Pertumbuhan User")
    chart_umkm = pd.DataFrame(np.random.randn(20,2), columns=["UMKM", "Penyedia Jasa Keuangan"])
    st.line_chart(chart_umkm)
    col1, col2 = st.columns(2)
    with col1:
        container = st.container (border=True)
        container.write('100 UMKM')
        st.write('**Jumlah UMKM**')
    with col2:
        container = st.container (border=True)
        container.write('100 Investor/Bank')
        st.write('**Jumlah Investor/Bank**')
    st.write('\n\n')
    # FUNGSI INI BELUM BISA MENGHAPUS HANYA BISA MENGECEK SAJA
    st.write('**Hapus User**')
    # Fungsi untuk memeriksa kredensial
    def check_credentials(username, users_df):
        user_row = users_df[(users_df['username'] == username)]
        return not user_row.empty

    # Baca data pengguna dari file CSV
    users_file = 'users.csv'
    try:
        users_df = pd.read_csv(users_file)
    except FileNotFoundError:
        users_df = pd.DataFrame(columns=['username', 'password'])

    username_delete = st.text_input('Username', key='username_delete')
    if st.button('Hapus', key='button_delete'):
        if check_credentials(username_delete, users_df):
            st.success('Penghapusan User berhasil!')
        else:
            st.error('Tidak ada User yang sesuai.')
    st.write('\n\n')

    st.write('**Tambah User**')
    # Fungsi untuk menambah pengguna baru
    def add_user(username, password, users_df, users_file):
        if username in users_df['username'].values:
            st.error('Username sudah ada. Gunakan username lain.')
        else:
            hashed_password = hash_password(password)
            new_user = pd.DataFrame({'username': [username], 'password': [hashed_password]})
            new_user.to_csv(users_file, mode='a', header=False, index=False)
            st.success('Registrasi berhasil.')

    username_add = st.text_input('Username', key='username_add')
    password_add = st.text_input('Password', type='password', key='password_add')
    if st.button('Tambah', key='button_add'):
        add_user(username_add, password_add, users_df, users_file)


elif menu == 'Pengajuan':
    st.title("Grafik Pengajuan")
    chart_umkm = pd.DataFrame(np.random.randn(20,2), columns=["Ditolak", "Diterima"])
    st.line_chart(chart_umkm)
    col1, col2 = st.columns(2)
    with col1:
        st.write('**Diterima:**')
        container = st.container (border=True)
        container.write('40 UMKM')
    with col2:
        st.write('**Ditolak:**')
        container = st.container (border=True)
        container.write('20 UMKM')

