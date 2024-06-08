import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("**My Cash Flow**")
st.divider()

st.markdown("<h1 style='text-align: center; font-size: 30px;'>Analisis Tahun 2024</h1>", unsafe_allow_html=True)

# Generate random data
np.random.seed(42)
dates = pd.date_range(start='2024-01-01', periods=12, freq='M')
income = np.random.randint(10000, 500000, size=12)
age = np.random.randint(20, 60, size=12)
credit_score = np.random.choice(['Excellent', 'Good', 'Fair', 'Poor'], size=12, p=[0.2, 0.3, 0.3, 0.2])

df = pd.DataFrame({'Income Update': dates, 'Income': income, 'Age': age, 'Credit Score': credit_score})

# Mapping nilai credit score yang ada ke kategori baru
credit_score_mapping = {
    'Excellent': 'High',
    'Good': 'Average',
    'Fair': 'Average',
    'Poor': 'Low'
}
df['Credit Score'] = df['Credit Score'].map(credit_score_mapping)

# Line chart
st.write("### Pendapatan Bulanan")
st.line_chart(df.set_index('Income Update')['Income'])

cols = st.columns([1, 1])
with cols[0]:
    st.markdown("<h3 style='text-align: center;'>Persentase Resiko</h3>", unsafe_allow_html=True)
    # Data untuk pie chart
    labels = ['Income', 'Riwayat Kredit', 'Data Pendukung', 'Keterampilan']
    sizes = [30, 12.5, 12.5, 20]
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
    explode = (0.1, 0, 0, 0)  
    # Pie chart
    fig, ax = plt.subplots(figsize=(5, 5))  
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

with cols[1]:
    st.markdown("<h3 style='text-align: center;'>Distribusi Skor Kredit</h3>", unsafe_allow_html=True)
    credit_score_counts = df['Credit Score'].value_counts()
    fig, ax = plt.subplots(figsize=(5, 5))  
    ax.pie(credit_score_counts, labels=credit_score_counts.index, autopct='%1.1f%%', startangle=60, colors=['#ff9999', '#66b3ff', '#99ff99'])
    ax.axis('equal')
    st.pyplot(fig)

# Bar chart 
st.write("### Pendapatan Berdasarkan Usia")
st.bar_chart(df.set_index('Age')['Income'])

st.markdown("<h1 style='text-align: center; font-size: 20px;'>Dokumentasi</h1>", unsafe_allow_html=True)
cols = st.columns([1, 1, 1])
with cols[0]:
    st.image('pictures/bgdepan.jpg')
with cols[1]:
    st.image('pictures/bgdepan.jpg')
with cols[2]:
    st.image('pictures/bgdepan.jpg')
st.divider()
st.markdown("<h1 style='text-align: center; font-size: 15px; font-weight: normal;'>Copyright © 2024 UMKMPriority. All rights reserved.</h1>", unsafe_allow_html=True)
