import streamlit as st
import numpy as np
import joblib
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

scaler = StandardScaler()

# Fungsi untuk load dan fit the scaler
@st.cache_data
def fit_scaler():
    dataset_path = "D:/MSIB batch 6 - project/CapstoneProject_Grup44-main/model-training/dataset/Credit Score Classification Dataset.csv"
    if not os.path.exists(dataset_path):
        st.error(f"Dataset path {dataset_path} does not exist.")
        return None

    # Read dataset
    train_data = pd.read_csv(dataset_path)
    
    # Standarisasi kolom nama
    train_data.columns = [col.strip().lower().replace(" ", "_") for col in train_data.columns]
     
    # Encode categorical_features
    label_encoders = {}
    categorical_features = ['gender', 'education', 'marital_status', 'home_ownership', 'credit_score']
    for feature in categorical_features:
        label_encoders[feature] = LabelEncoder()
        train_data[feature] = label_encoders[feature].fit_transform(train_data[feature])
    
    # Ekstrak fitur numerical
    numerical_features = ["age", "income", "number_of_children", "gender", "education", "marital_status", "home_ownership"]
    
    # Memastikan ada coloumns di DataFrame
    missing_cols = [col for col in numerical_features if col not in train_data.columns]
    if missing_cols:
        st.error(f"Missing columns in the dataset: {missing_cols}")
        return None

    # Fit scaler
    scaler.fit(train_data[numerical_features])
    return scaler

# Load dan fit scaler
scaler = fit_scaler()
if scaler is None:
    st.stop()

def make_prediction(input_data):
    model_path = 'D:/MSIB batch 6 - project/CapstoneProject_Grup44-main/model-training/random_forest_model.pkl'
    if not os.path.exists(model_path):
        st.error(f"Model path {model_path} does not exist.")
        return None

    try:
        model = joblib.load(model_path)
        # Standarisasi input data
        input_data = scaler.transform(input_data)
        prediction = model.predict(input_data)
        return prediction
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def get_prediction_label(prediction):
    if prediction is None:
        return "Prediction error"
    if prediction[0] == 1:
        return "Average"
    elif prediction[0] == 0:
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
    if gender == 0:
        st.write("Jenis Kelamin : **Perempuan**")
    elif gender == 1:
        st.write("Jenis Kelamin : **Laki-Laki**")
    st.write(f'Income Update : **{date_income}**')
    st.write(f'Pendapatan Bulanan: **{income}**')
    if education == 0:
        st.write("Pendidikan : **Gelar Asosiasi**")
    elif education == 1:
        st.write("Pendidikan : **Gelar Sarjana**")
    elif education == 2:
        st.write("Pendidikan : **Gelar Dokter**")
    elif education == 3:
        st.write("Pendidikan : **Tamat SMA**")
    elif education == 4:
        st.write("Pendidikan : **Gelar Master/S2**")
    if marital_status == 0:
        st.write("Status Pernikahan : **Menikah**")
    elif marital_status == 1:
        st.write("Status Pernikahan : **Lajang**")
    st.write(f'Jumlah Pegawai: **{number_of_children}**')
    if home_ownership == 0:
        st.write("Status Kepemilikan : **Owner**")
    elif home_ownership == 1:
        st.write("Status Kepemilikan : **Sewa**")
    st.write(f'Skor Kredit: **{prediction_label}**')

# cols = st.columns([3,1.3,1,1.2,1.2,1.2,1.2,1])
# with cols[0]:
#     st.markdown("<h1 style='text-align: left; font-size: 15px;'>UMKMPriority</h1>", unsafe_allow_html=True)
# with cols[2]:
#     if st.button("Home"):
#         st.switch_page("Home.py")
# with cols[3]:
#     if st.button("Pengajuan"):
#         st.switch_page("pages/Pengajuan.py")
# with cols[4]:
#     if st.button("myCashflow"):
#         st.switch_page("pages/MyCashFlow.py")
# with cols[5]:
#     if st.button("WarungKu"):
#         st.switch_page("pages/WarungKu.py")
# with cols[6]:
#     if st.button("Pengaturan"):
#         st.switch_page("pages/Pengaturan.py")
# st.divider()

st.title("**WarungKu**")
st.divider()

st.markdown("<h1 style='text-align: center; font-size: 25px;'>Profil UMKM</h1>", unsafe_allow_html=True)
cols = st.columns([1.5,2.5,1.5])
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
    gender = st.selectbox("Jenis Kelamin", ("Perempuan", "Laki-Laki"))
    income = st.number_input("Pendapatan Bulanan", min_value=1, max_value=100000000)
    education = st.selectbox("Pendidikan", ("Gelar Asosiasi", "Gelar Sarjana", "Gelar Dokter", "Tamat SMA", "Gelar Master/S2"))
    marital_status = st.selectbox("Status Pernikahan", ("Menikah", "Lajang"))
    number_of_children = st.number_input("Jumlah Pegawai", min_value=0, max_value=10)
    home_ownership = st.selectbox("Status Kepemilikan", ("Owner", "Sewa"))
    submit_button = st.form_submit_button("Predict")

    if submit_button:
        education_mapping = {"Gelar Asosiasi": 0, "Gelar Sarjana": 1, "Gelar Dokter": 2, "Tamat SMA": 3, "Gelar Master/S2": 4}
        marital_status_mapping = {"Menikah": 0, "Lajang": 1}
        home_ownership_mapping = {"Owner": 0, "Sewa": 1}
        gender_mapping = {"Perempuan": 0, "Laki-Laki": 1}

        education_encoded = education_mapping[education]
        marital_status_encoded = marital_status_mapping[marital_status]
        home_ownership_encoded = home_ownership_mapping[home_ownership]
        gender_encoded = gender_mapping[gender]

        input_data = np.array([[age, gender_encoded, income, education_encoded, marital_status_encoded, number_of_children, home_ownership_encoded]])
        
        if not hasattr(scaler, 'mean_'):
            st.error("The scaler is not fitted yet. Please fit the scaler before making predictions.")
        else:
            prediction = make_prediction(input_data)
            display_profile_data(nama_pemilik, nama_usaha, date_income, age, gender_encoded, income, education_encoded, marital_status_encoded, number_of_children, home_ownership_encoded, prediction)

st.divider()
st.markdown("<h1 style='text-align: center; font-size: 15px; font-weight: normal;'>Copyright © 2024 UMKMPriority. All rights reserved.</h1>", unsafe_allow_html=True)