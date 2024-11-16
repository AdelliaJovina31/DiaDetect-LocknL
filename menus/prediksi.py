import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load / muat model
model = joblib.load('models/model1fix.pkl')
print(type(model))

# CSS styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, white, #D7C8DF);
    }
    .css-1aumxhk {
        font-size: 24px;
        font-weight: bold;
        color: #3b3b3b;
    }
    .css-145kmo2 {
        font-size: 20px;
        color: #4c4c4c;
    }
    .stButton>button {
        color: white;
        background-color: #4CAF50;
        font-size: 18px;
        font-weight: bold;
    }

    /* input field */
    input {
        border: 1px solid white;
        border-radius: 8px;
        padding: 8px;
        font-size: 16px;
        background-input: white;
    }

    /* input border */
    .st-emotion-cache-6v4t1a {
        border-width: 1px;
    }

    /* input focus */
    .st-emotion-cache-6v4t1a.focused {
        border-color: #B17BAC;
    }

    /* combobox */
    .stSelectbox>div>div {
        border: 2px solid white;
        border-radius: 8px;
        font-size: 16px;
    }

    /* combobox focus */
    .stSelectbox:focus-within > div > div {
        border: 2px solid #A3A9E5;
        border-radius: 8px;
    }

    /* button */
    .st-emotion-cache-1vs7lf5 {
        border: 1px solid white;
        border-radius: 8px;
    }
    .st-emotion-cache-1vs7lf5:hover {
        border-color: #B17BAC;
        color: #B17BAC;
    }
    .st-emotion-cache-1vs7lf5:focus:not(:active) {
        background-color: #B17BAC;
        color: white;
        border-color: white;
    }
    .st-emotion-cache-1vs7lf5:active {
        border-color: #B17BAC;
        color: white;
        background-color: #B17BAC;
    }
    .st-emotion-cache-1jicfl2 {
        width: 100%;
        padding: 2.5rem 0 2.5rem 0;
    }
    @media (min-width: 576px) {
        .st-emotion-cache-7tauuy {
            padding-left: 5rem;
            padding-right: 5rem;
        }
    }
    h1 {
        text-align: center;
        padding: 1.25rem 0px 2.5rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


layoutPage1, layoutPage2, layoutPage3 = st.columns([1,7,1])

# Inisialisasi session_state 
if "model1_data" not in st.session_state:
    st.session_state.model1_data = {}
if "model2_data" not in st.session_state:
    st.session_state.model2_data = {}
if "lanjut" not in st.session_state:
    st.session_state.lanjut = False

def model1_form():
    with layoutPage2:
        # Buat form untuk user input
        with st.form("gb_model_form"):
            # Kelompokkan input dalam container
            with st.container():
                st.title("Prediksi Diabetes")

                # Definisikan columns dalam form
                col1, col2 = st.columns(2) 
                
                # Input field di col1
                with col1:
                    gender = st.selectbox("Jenis Kelamin:", [1, 0], format_func=lambda x: "Laki-laki" if x == 1 else "Perempuan")
                    bmi = st.number_input("BMI (Batas input 12.0 - 39.0):", min_value=12.0, max_value=39.0, step=0.1)
                    heart_disease = st.selectbox("Penyakit Jantung:", [0, 1], format_func=lambda x: "Ada" if x == 1 else "Tidak Ada")
                    smoking_history = st.selectbox(
                        "Riwayat Merokok:",
                        [0, 1, 2, 3, 4, 5], 
                        format_func=lambda x: {
                            0: "Tidak ada informasi",
                            1: "Merokok saat ini",
                            2: "Pernah merokok",
                            3: "Berhenti merokok",
                            4: "Tidak pernah merokok",
                            5: "Tidak merokok saat ini"
                        }.get(x, "Unknown")
                    )
                    blood_pressure = st.number_input("Tekanan Darah Sistolik (mmHg) (Batas input 60.0 - 149.0):", min_value=60.0,  max_value=149.0, step=0.1)
                    blood_glucose_level = st.number_input("Kadar Gula Darah (mg/dL) (Batas input 80.0 - 299.0):", min_value=80.0,  max_value=299.0, step=0.1)
                    hba1c_level = st.number_input("HbA1c Level (%):", min_value=0.0, step=0.1)
                    
                # Input field di col2
                with col2:
                    age = st.number_input("Usia (Batas input 1 - 79):", min_value=1,  max_value=79, step=1)
                    waist_circumference = st.number_input("Lebar Pinggang (cm) (Batas input 20.0 - 54.0):", min_value=20.0,  max_value=54.0, step=0.1)
                    hypertension = st.selectbox("Hipertensi:", [0, 1], format_func=lambda x: "Ada" if x == 1 else "Tidak Ada")
                    family_history = st.selectbox("Riwayat Keluarga Diabetes:", [0, 1], format_func=lambda x: "Ada" if x == 1 else "Tidak Ada")         
                    cholesterol_levels = st.number_input("Kadar Kolesterol (mg/dL) (Batas input 100.0 - 299.0):", min_value=100.0, max_value=299.0, step=0.1)
                    insulin_levels = st.number_input("Kadar Insulin (µU/mL) (Batas input 5.0 - 49.0):", min_value=5.0, max_value=49.0, step=0.1)
                    
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([3, 2, 3])  # Adjust proportions to shift the button right
            with col2:
                submit_button = st.form_submit_button("Prediksi", use_container_width=True) 
            
    # Handle form submission
    if submit_button:
        print("Cek pressed.")
        
        # Simpan user_data FOR session_state FOR model1
        st.session_state.model1_data['gender'] = gender
        st.session_state.model1_data['hypertension'] = hypertension
        st.session_state.model1_data['heart_disease'] = heart_disease
        st.session_state.model1_data['smoking_history'] = smoking_history
        st.session_state.model1_data['HbA1c_level'] = hba1c_level
        
        # Simpan user_data FOR session_state FOR model2
        st.session_state.model2_data['bmi'] = bmi
        st.session_state.model2_data['age'] = age
        st.session_state.model2_data['waist_circumference'] = waist_circumference
        st.session_state.model2_data['cholesterol_levels'] = cholesterol_levels
        st.session_state.model2_data['blood_glucose_level'] = blood_glucose_level
        st.session_state.model2_data['blood_pressure'] = blood_pressure
        st.session_state.model2_data['insulin_levels'] = insulin_levels
        st.session_state.model2_data['family_history'] = family_history
        print(st.session_state.model2_data)
        
        # Buat user data dalam 2D numpy array for MODEL
        user_data = np.array([[gender, age, hypertension, heart_disease, smoking_history, hba1c_level, blood_glucose_level]])
        print(f"User Data: {user_data}")

        with layoutPage2:
            # Ensure the input matches the expected number of features
            if user_data.shape[1] != model.n_features_in_:
                st.error(f"Error: Model expects {model.n_features_in_} features, but got {user_data.shape[1]}.")
            else:
                # Lakukan prediksi
                prediction = model.predict(user_data)
                
                # Format dan tampilkan hasilnya
                if prediction[0] == 1:
                    output("Pasien terindikasi memiliki diabetes.")
                    st.error("Pasien terindikasi memiliki diabetes.")
                else:
                    st.success("Pasien tidak terindikasi memiliki diabetes.")
                    st.session_state.lanjut = False

# Popup
@st.dialog(" ", width="small")
def output(result):
    st.markdown("<div style='height: 3px;'></div>", unsafe_allow_html=True)
    st.error(result)
    st.write("Apakah Anda ingin lanjut?")
    
    # Posisikan button di samping kanan
    col1, col2, col3 = st.columns([2, 2, 1])
    with col3:
        if st.button("Lanjut"):
            st.session_state.lanjut = True
            st.rerun()
            
# Inisialisasi halaman
rekomendasi_page = st.Page("menus/hasil.py", title="Hasil", default=(st.session_state.lanjut == True))   

if st.session_state.lanjut:
    # Navigasi ke rekomendasi_page
    pg = st.navigation([rekomendasi_page])
else:
    # Tetap di halaman sekarang
    pg = st.navigation([st.Page(model1_form)])
    
pg.run()
