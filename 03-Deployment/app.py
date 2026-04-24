import streamlit as st

# Mengatur tampilan halaman web
st.set_page_config(page_title="JDM Car Predictor", page_icon="🏎️", layout="centered")

# Header Website
st.title("🏎️ JDM Used Car Price Predictor")
st.write("Selamat datang! Masukkan spesifikasi mobil JDM impianmu di bawah ini untuk melihat estimasi harganya di pasaran.")

# Membuat garis pemisah
st.markdown("---")

# Membuat Form Input dibagi menjadi 2 kolom agar rapi
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
# Tombol Prediksi (Logikanya akan kita bangun besok)
if st.button("Hitung Estimasi Harga! 💸", use_container_width=True):
    st.info("Tombol ditekan! Logika AI sedang dalam proses pembangunan...")