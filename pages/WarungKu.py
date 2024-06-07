import streamlit as st
import numpy as np
import joblib
import os
import pandas as pd

def make_prediction(input_data):
    model_path = 'model-training/random_forest_model.pkl'
    if not os.path.exists(model_path):
        st.error(f"Model path {model_path} does not exist.")
        return None

    try:
        model = joblib.load(model_path)
        prediction = model.predict(input_data)
        return prediction
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def get_prediction_label(prediction):
    if prediction is None:
        return "Prediction error"
    if prediction[0] == 0:
        return "Average"
    elif prediction[0] == 1:
        return "High"
    elif prediction[0] == 2:
        return "Low"
    else:
        return "Unknown"

def display_profile_data(nama_pemilik, nama_usaha, date_income, age, gender, income, education, marital_status, number_of_children, home_ownership, prediction):
    prediction_label = get_prediction_label(prediction)
    st.write(f'Halo! **{nama_pemilik}** berikut adalah data diri Anda.')  
    st.write(f'Nama Usaha: **{nama_usaha}**')
    st.write(f'Umur: **{age}** tahun')
    # Jenis Kelamin
    if gender == 0:
        st.write("Jenis Kelamin : **Perempuan**")
    elif gender == 1:
        st.write("Jenis Kelamin : **Laki-Laki**")
    # month
    st.write(f'Income Update : **{date_income}**')
    st.write(f'Pendapatan Bulanan: **{income}**')
    # Pendidikan
    if education == 0:
        st.write("Pendidikan : **Gelar Asosiasi**")
    elif education == 1:
        st.write("Pendidikan : **Gelar Sarjana**")
    elif education == 2:
        st.write("Pendidikan : **Gelar Doktor**")
    elif education == 3:
        st.write("Pendidikan : **Tamat SMA**")
    elif education == 4:
        st.write("Pendidikan : **Gelar Master/S2**")
    # Status Pernikahan
    if marital_status == 0:
        st.write("Status Pernikahan : **Menikah**")
    elif marital_status == 1:
        st.write("Status Pernikahan : **Lajang**")
    st.write(f'Jumlah Pegawai: **{number_of_children}**')
    # Status Kepemilikan
    if home_ownership == 0:
        st.write("Status Kepemilikan : **Owner**")
    elif home_ownership == 1:
        st.write("Status Kepemilikan : **Sewa**")
    st.write(f'Skor Kredit: **{prediction_label}**')

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
        st.switch_page("pages/WarungKu.py")
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
    date_income = st.date_input("Tanggal Income", value=None)
    age = st.number_input('Umur', min_value=0, max_value=120)
    gender = st.selectbox("Jenis Kelamin (perempuan : 0, laki-laki : 1)", (1, 0))
    income = st.number_input("Pendapatan Bulanan", min_value=1, max_value=100000000)
    education = st.number_input("Pendidikan (Gelar Asosiasi : 0, Gelar Sarjana : 1, Gelar Dokter : 2, Tamat SMA : 3, Gelar Master/S2 : 4)", min_value=0, max_value=10)  # Angka untuk Pendidikan
    marital_status = st.number_input("Status Pernikahan (married : 0, single : 1)", min_value=0, max_value=1)
    number_of_children = st.number_input('Jumlah Pegawai', min_value=0, max_value=120)
    home_ownership = st.number_input("Status Kepemilikan (Owner : 0, Rented : 1)", min_value=0, max_value=1)
    submitted = st.form_submit_button("Submit")

if submitted:
    # Prepare the input data
    input_data = np.array([[age, gender, income, education, marital_status, number_of_children, home_ownership]])
    prediction = make_prediction(input_data)
    
    # Save input data to CSV
    new_data = pd.DataFrame({
        'Nama User': [nama_pemilik],
        'Nama Usaha': [nama_usaha],
        'Income Update': [date_income],
        'Age': [age],
        'Gender': [gender],
        'Income': [income],
        'Education': [education],
        'Marital Status': [marital_status],
        'Number of Children': [number_of_children],
        'Home Ownership': [home_ownership],
        'Credit Score': [get_prediction_label(prediction)]
    })
    
    if os.path.exists('data_umkm.csv'):
        new_data.to_csv('data_umkm.csv', mode='a', header=False, index=False)
    else:
        new_data.to_csv('data_umkm.csv', index=False)
    
    display_profile_data(nama_pemilik, nama_usaha, date_income, age, gender, income, education, marital_status, number_of_children, home_ownership, prediction)

st.divider()
st.markdown("<h1 style='text-align: left; font-size: 15px; font-weight: normal;'>Copyright © 2024 UMKMPriority. All rights reserved.</h1>", unsafe_allow_html=True)