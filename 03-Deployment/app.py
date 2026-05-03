import streamlit as st
import pandas as pd
import joblib

# ==========================================
# 1. MEMUAT ARTIFAK AI (Model, Fitur, Scaler)
# ==========================================
# st.cache_resource digunakan agar file berat hanya diload 1x saat web menyala
@st.cache_resource
def load_ai_artifacts():
    model = joblib.load('jdm_rf_model_tuned.joblib')
    fitur = joblib.load('jdm_fitur_kolom.joblib')
    scaler = joblib.load('jdm_scaler.joblib')
    return model, fitur, scaler

model_rf, fitur_kolom, scaler = load_ai_artifacts()

# ==========================================
# 2. ANTARMUKA WEBSITE (UI)
# ==========================================
st.set_page_config(page_title="JDM Car Predictor", page_icon="🏎️", layout="centered")

st.title("🏎️ JDM Used Car Price Predictor")
st.write("Masukkan spesifikasi mobil JDM impianmu di bawah ini untuk melihat estimasi harganya di pasaran.")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Mesin & Tahun")
    year = st.number_input("Tahun Produksi", min_value=1990, max_value=2024, value=2010, step=1)
    mileage = st.number_input("Jarak Tempuh (km)", min_value=0, value=50000, step=5000)
    engine_capacity = st.number_input("Kapasitas Mesin (cc)", min_value=500, max_value=5000, value=1500, step=100)

with col2:
    st.subheader("Spesifikasi Lain")
    mark = st.selectbox("Merek (Brand)", ["nissan", "toyota", "honda", "mazda", "subaru", "mitsubishi"])
    transmission = st.selectbox("Transmisi", ["AT", "MT", "CVT"])
    fuel = st.selectbox("Bahan Bakar", ["gasoline", "diesel", "hybrid"])

st.markdown("---")

# ==========================================
# 3. LOGIKA PREDIKSI AI SAAT TOMBOL DITEKAN
# ==========================================
if st.button("Hitung Estimasi Harga! 💸", use_container_width=True):
    
    # a. Membungkus input user menjadi DataFrame 1 baris
    user_input = pd.DataFrame({
        'year': [year],
        'mileage': [mileage],
        'engine_capacity': [engine_capacity],
        'mark': [mark],
        'transmission': [transmission],
        'fuel': [fuel]
    })
    
    # b. One-Hot Encoding input user (mengubah teks jadi kolom)
    input_encoded = pd.get_dummies(user_input)
    
    # c. MENYAMAKAN KOLOM: Pastikan kolom input = kolom saat model ditraining!
    # Kolom merek/bahan bakar lain yang tidak dipilih user akan diisi dengan angka 0
    input_final = input_encoded.reindex(columns=fitur_kolom, fill_value=0)
    
    # d. Menggunakan SCALER yang diselamatkan tadi untuk mengecilkan angka numerik
    kolom_numerik = ['year', 'mileage', 'engine_capacity']
    input_final[kolom_numerik] = scaler.transform(input_final[kolom_numerik])
    
    # e. Minta AI menebak harganya!
    prediksi_harga = model_rf.predict(input_final)
    
    # f. Menampilkan hasil ke layar
    st.success(f"### 🎯 Estimasi Harga Pasaran: Rp {int(prediksi_harga[0]):,}")
    st.balloons() # Efek animasi balon sebagai perayaan!