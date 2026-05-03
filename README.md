# 🏎️ JDM Used Car Price Predictor & Market Segmentation

Sebuah proyek *End-to-End Machine Learning* untuk menganalisis, memprediksi, dan mengklasifikasikan pasar mobil bekas JDM (Japanese Domestic Market).

## 🛠️ Tech Stack & Skills Demonstrated
* **Data Preprocessing & EDA:** Pandas, Matplotlib, Seaborn
* **Supervised Learning (Regression & Classification):** Scikit-Learn (Linear Regression, Random Forest, Logistic Regression)
* **Unsupervised Learning:** K-Means Clustering, PCA (Principal Component Analysis)
* **Deep Learning:** TensorFlow & Keras (Multi-Layer Perceptron)
* **Deployment:** Streamlit Web Application
* **Environment:** Python 3.11, Jupyter Notebook

## 📂 Project Structure
1. `01-Data-Preprocessing/`: Pembersihan dataset dan Exploratory Data Analysis.
2. `02-Supervised-Learning/`: Prediksi harga mobil berkesinambungan (Regression).
3. `03-Deployment/`: Aplikasi web interaktif berbasis Streamlit untuk melayani prediksi secara *real-time*.
4. `04-Unsupervised-Learning/`: Segmentasi pasar mobil menggunakan K-Means dan visualisasi PCA.
5. `05-Classification/`: Mengklasifikasikan segmen mobil (Premium vs Standar) menggunakan evaluasi ROC-AUC.
6. `06-Deep-Learning/`: Eksperimen arsitektur Jaringan Saraf Tiruan dengan TensorFlow.

## 🚀 How to Run the App locally
```bash
git clone https://github.com/zippynx/ml-journey.git
cd ml-journey/03-Deployment
pip install -r requirements.txt
streamlit run app.py