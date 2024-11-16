import random
import time
import joblib
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_extras.bottom_container import bottom 

if "lanjut" not in st.session_state:
    st.session_state.lanjut = True
if "history" not in st.session_state:
    st.session_state.history = []
if "show_chatbot" not in st.session_state:
    st.session_state.show_chatbot = False

with st.container():
    col1, col2 = st.columns([1, 11])
       
    with col2:
        if st.button("Cek Lagi"):
            st.session_state.lanjut = False
            st.session_state.history = []
            st.rerun()
    
st.divider()

st.markdown(
    """
    <style>
    .st-emotion-cache-12w0qpk {
        display: flex;
        justify-content: center;
    }
    #tim-kami {
        text-align: center;
    }
    #lock-n-luck {
        text-align: center;
        color: #6c6c6c;
    }
    .stColumn {
        display: flex;
        # align-items: center;
        # justify-content: center;
    }
    h1 {
        padding: 0;
    }
    h3 {
        padding: 1px 0 3rem 0;
    }
    hr {
        margin: 0;
    }
    .st-emotion-cache-qdbtli.ea3mdgi2 {
      padding-bottom: 100px !important;
      padding-top: 10px !important;
      padding-left: 16px !important;
      padding-right: 10px !important;
    }
    /* button Cek Lagi */
    .st-emotion-cache-qd6iyk > div:nth-child(1) > button:nth-child(1) {
        border: 1px solid #B17BAC;
        background-color: #B17BAC !important;
        color: white;
    }
    .st-emotion-cache-qd6iyk > div:nth-child(1) > button:nth-child(1):hover {
        border: 1px solid #B17BAC !important;
        background-color: white !important;
        color: #B17BAC;
    }
    .st-emotion-cache-41yyj8 {
        gap: 0.5rem;
    }
    .st-emotion-cache-1igbibe {
        margin-top: 15px;
    }
    .team-container {
        gap: 20px;
        margin-top: 20px 110px;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: white;
        padding: 10px;
        position: relative;
        width: 100%;
        bottom: 0;
        left: 0;
        background-color: #B17BAC;
    }
    @media (min-width: 576px) {
        .st-emotion-cache-7tauuy {
            padding: 0 0 2rem 0;
        }
    }
    .st-emotion-cache-1jicfl2 {
        width: 100%;
        padding: 2.5rem 0 0 0;
    }
    .st-emotion-cache-7tauuy {
        width: 100%;
        padding: 2.5rem 1rem 1rem;
        min-width: auto;
        max-width: initial;
    }
    .st-emotion-cache-1xf0csu {
        display: flex;
        # justify-content: center;
        flex-direction: column;
        gap: 20px;
        margin-top: 20px;
    }
    .st-emotion-cache-1xf0csu img {
        width: 200px;
        # height: 250px;
        object-fit: cover;
        border-radius: 8px;
    }
    .team-caption {
        text-align: center;
        color: #6c6c6c;
    }
    .e1f1d6gn3 {
        position: relative;
        z-index: 10;
    }
    .st-emotion-cache-1igbibe {
        background-color: transparent !important;
        border-color: transparent;
    }
    .st-emotion-cache-1igbibe:hover {
        border-color: transparent !important;
        background-color: #B17BAC !important;
        color: white;
    }

    # @media (min-width: 576px) {
    #         .st-emotion-cache-7tauuy {
    #             padding-left: 5rem;
    #             padding-right: 5rem;
    #         }
    #     }
    # .st-emotion-cache-1jicfl2 {
    #     padding: 0;
    # }
    # .stHorizontalBlock  {
    #     margin: 0 100px 2.5rem;
    # }
    # h1 {
    #     padding: 0;
    # }
    # h3 {
    #     padding: 2px 0 3rem 0;
    # }
    .stElementContainer .stButton button {
        border: 1px solid transparent;
    }
    .st-emotion-cache-p5msec:hover {
        color: #B17BAC;
    }
    .st-emotion-cache-p5msec:hover svg {
        fill: #B17BAC;
    }
    .stElementContainer .stButton button {
        border: 1px solid transparent;
        border-radius: 8px;
        background-color: white;
        color: black;
    }
    .st-emotion-cache-1igbibe:hover, .stElementContainer .stButton button:hover {
        border: 1px solid transparent;
        color: white;
        background-color: #B17BAC;
    }
    .st-emotion-cache-1igbibe:focus:not(:active), .stElementContainer .stButton button:focus:not(:active) {
        background-color: #B17BAC !important;
        color: white;
        border: 1px solid white;
    }
    .st-emotion-cache-1igbibe:active, .stElementContainer .stButton button:active {
        border: 1px solid white;
        color: white;
        background-color: #B17BAC;
    }
    .stTooltipHoverTarget button {
        background-color: transparent;
        border-color: transparent;
    }
    .stTooltipHoverTarget button:hover {
        border-color: transparent;
        background-color: #B17BAC;
        color: white;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > section > div.stMainBlockContainer.block-container.st-emotion-cache-7tauuy.ea3mdgi5 > div > div > div > div.st-emotion-cache-0.e1f1d6gn0 > div > div > div > div.stColumn.st-emotion-cache-ajjk9q.e1f1d6gn3 > div > div > div > div > div > button {
        background-color: #B17BAC !important;
        border-color: #B17BAC !important;
        color: white;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > section > div.stMainBlockContainer.block-container.st-emotion-cache-7tauuy.ea3mdgi5 > div > div > div > div.st-emotion-cache-0.e1f1d6gn0 > div > div > div > div.stColumn.st-emotion-cache-ajjk9q.e1f1d6gn3 > div > div > div > div > div > button:hover {
        background-color: white !important;
        border-color: #B17BAC !important;
        color: #B17BAC;
    }
    .stButton button {
        color: white;
        background-color: #B17BAC;
        font-size: 18px;
        font-weight: bold;
        border: 1px solid white;
    }
    .stButton button:hover {
        border: 1px solid #B17BAC;
        color: #B17BAC;
    }
    .stButton > button:active {
        border: 1px solid white;
        color: white;
        background-color: #B17BAC;
    }
    .st-emotion-cache-1m02ktg {
        width: 1280px;
        position: relative;
        display: flex;
        flex: 1 1 0%;
        flex-direction: column;
        gap: 1rem;
    }

    /* button chatbot */
    .stElementContainer .stButton button {
        border: 1px solid transparent;
        border-radius: 8px;
        background-color: #B17BAC;
    }
    .stElementContainer .stButton button:hover {
        border: 1px solid #B17BAC;
        border-radius: 8px;
        background-color: white;
    }
    h1 {
        text-align: center;
    }
    #hasil-body {
        @media (min-width: 576px) {
            .st-emotion-cache-7tauuy {
                padding-left: 5rem;
                padding-right: 5rem;
            }
        }
    }
    .st-emotion-cache-128upt6 {
        background-color: transparent;
    }

    /* combobox pilih lokasi */
    .stSelectbox > div > div {
        width: 700px
    }
    </style>
    """,
    unsafe_allow_html=True
)

paddingTitle1, layoutPadTitle, paddingTitle2 = st.columns([0.5, 9, 0.5])

st.markdown("<div id='hasil-body'>", unsafe_allow_html=True)

with paddingTitle1:  # Left padding/empty space
    pass

with layoutPadTitle:
    st.title("Hasil Deteksi")

    # =============================== MODELLING  ===============================
    model1_data = st.session_state.model1_data
    model2_data = st.session_state.model2_data

    # Load (muat) model
    model = joblib.load('models/gb_file.pkl')

    # Cek tipe model yang dimuat
    print(f"Type of model: {type(model)}")
    print(f"Number of features expected by the model: {model.n_features_in_}")
    try:
        print("Feature names: ", model.feature_names_in_)
    except AttributeError:
        print("Feature names are not stored in the model.")

    # Buat user data dalam 2D numpy array untuk MODEL
    user_data = np.array([[model2_data['waist_circumference'], model2_data['bmi'], model2_data['cholesterol_levels'], model2_data['age'], model2_data['blood_pressure'], model2_data['blood_glucose_level'], model2_data['insulin_levels'], model2_data['family_history'],]])
    print(f"User Data: {user_data}")

    # Lakukan prediksi
    prediction = model.predict(user_data)

    # =============================== HASIL PREDIKSI ===============================
    diabetes_type = ''

    # Format dan display hasil
    if prediction[0] == 0:
        print("Diabetes Tipe 1")
        diabetes_type = "Diabetes Tipe 1"
        st.error("Diabetes Tipe 1")
    elif prediction[0] == 1:
        print("Diabetes Tipe 2")
        diabetes_type = "Diabetes Tipe 2"
        st.error("Diabetes Tipe 2")

with paddingTitle2:
    pass

#  =============================== PAGE  ===============================
# layoutCol
padding1, layoutCol1, layoutPad1, layoutCol3, padding2 = st.columns([0.5, 7, 0.5, 5, 0.5])

with padding1:  # Left padding/empty space
    pass

# =============================== SHOW DATA INPUT ===============================
def showValue(data, range1, range2=None):
    """
    Display a value with a condition:
    - If the value is above/below the given range(s), color it red.
    - If within the range(s), display it normally.
    """
    if range2 is None:
        if (data > range1):
            st.write(f":red[{data}]")
        else:
            st.write(f"{data}")     
    else:
        if (data > range2 or data < range1):
            st.write(f":red[{data}]")
        else:
            st.write(f"{data}")   

with layoutCol1:  
    # Kelompokkan input dalam kontainer
    st.header("Data Diri")

    # Divider / garis pembatas
    st.markdown("""
        <hr style="margin: 0px 0; border: 0.20px solid #ccc;" />
    """, unsafe_allow_html=True)
        
        
    # ============= [Section Informasi Umum] =============
    with st.expander("Informasi Umum", expanded=True):
        col1, col2, col3, col4 = st.columns([2, 0.5, 2, 2]) 
        
        with col1:
            st.text("Jenis Kelamin")
            st.text("Usia")
            st.text("BMI")
            st.text("Lebar pinggang (cm)")
        
        with col2:
            st.text(":")
            st.text(":")
            st.text(":")
            st.text(":")
        
        with col3:
            st.text(f"{('Laki-laki' if model1_data['gender'] == 1 else 'Perempuan')}")
            st.text(f"{model2_data['age']}")
            st.text(f"{model2_data['bmi']}")
            st.text(f"{model2_data['waist_circumference']}") 
    
    
    # ============= [Section Tes] =============
    with st.expander("Tes", expanded=True):
        # Define columns
        col1, pad1, col2, pad2, col3, pad3, col4 = st.columns([1.5, 0.1, 0.8, 0.1, 1.5, 0.1, 0.9]) 
        
        with col1:
            st.markdown(
                """
                <h5>PEMERIKSAAN</h5>
                """,
                unsafe_allow_html=True
            )
            st.text("Tekanan Darah")
            st.text("Kadar Gula Darah")
            st.text("HbA1c Level")
            st.text("Kadar Kolesterol")
            st.text("Kadar Insulin")
        
        with col2:
            st.markdown(
                """
                <h5>HASIL</h5>
                """,
                unsafe_allow_html=True
            )
            # Blood pressure / tekanan darah
            showValue(model2_data['blood_pressure'], 120)   
            # Blood glucose level
            showValue(model2_data['blood_glucose_level'], 200)
            # HbA1c
            showValue(model1_data['HbA1c_level'], 5.7)
            # Cholesterol
            showValue(model2_data['cholesterol_levels'], 200)
            # Insulin
            showValue(model2_data['insulin_levels'], 2.6, 24.9)
                
        with col3:
            # Nilai rujukan itu nilai normalnya
            st.markdown(
                """
                <h5>NILAI RUJUKAN</h5>
                """,
                unsafe_allow_html=True
            )
            st.write("[ < 120.0 ]") # Tekanan darah
            st.write("[ < 200 ]") # Kadar gula darah
            st.write("[ < 5.7 ]") # HbA1c Level
            st.write("[ < 200 ]") # Kadar kolesterol
            st.write("[ 2.6 - 24.9 ]") # Kadar insulin
        
        with col4:
            st.markdown(
                """
                <h5>UNIT</h5>
                """,
                unsafe_allow_html=True
            )
            st.text("(/80 mmHg)") # Tekanan darah
            st.text("(mg/dL)") # Kadar gula darah
            st.text("(%)") # HbA1c Level
            st.text("(mg/dL)") # Kadar kolesterol
            st.text("(µU/mL)") # Kadar insulin
            
            
    # ============= [Section Riwayat Penyakit] =============
    with st.expander("Riwayat Kesehatan", expanded=True):
        col1, col2, col3, col4 = st.columns([2, 0.5, 2, 2]) 
        
        with col1:
            st.text("Penyakit Jantung")
            st.text("Hipertensi")
            st.text("Riwayat Merokok")
            st.text("Riwayat Keluarga Diabetes")
        
        with col2:
            st.text(":")
            st.text(":")
            st.text(":")
            st.text(":")
        
        with col3:
            st.text(f"{('Ada' if model1_data['heart_disease'] == 1 else 'Tidak Ada')}")
            st.text(f"{('Ada' if model1_data['hypertension'] == 1 else 'Tidak Ada')}")
            st.text(f"{(lambda x: {0: 'Tidak ada informasi', 1: 'Merokok saat ini', 2: 'Pernah merokok', 3: 'Berhenti merokok', 4: 'Tidak pernah merokok', 5: 'Tidak merokok saat ini'}.get(x, 'Unknown'))(model1_data['smoking_history'])}")
            st.text(f"{('Ada' if model2_data['family_history'] == 1 else 'Tidak Ada')}") 
    
#  =============================== CHATBOT ===============================
# Streamed response emulator
def response_generator(message):
    response = random.choice(
        [
            message
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)
            
# Chatbot pop-up
@st.dialog("Chatbot", width="large")
def showChatbot():
    messages = st.container(height=500)

    option = st.selectbox(
        " ",
        ["Apa yang dimaksud dengan diabetes?", "Bisa jelaskan apa itu diabetes tipe 1?", "Bisa jelaskan apa itu diabetes tipe 2?", "Gejala diabetes itu apa saja, ya?", "Apa sih yang menyebabkan diabetes?", "Apa saja bahaya yang bisa ditimbulkan oleh diabetes?", "Gimana pola hidup yang sehat untuk penderita diabetes?"],
        index = None,
        placeholder = "Tanya saya",
        label_visibility="collapsed",
    )

    answer1 = "Diabetes adalah kondisi medis kronis di mana kadar gula darah terlalu tinggi karena tubuh tidak bisa memproduksi insulin yang cukup atau tidak menggunakannya secara efektif. Di Indonesia, tipe diabetes yang paling umum adalah Diabetes Tipe 1 dan Diabetes Tipe 2."
    answer2 = "Diabetes tipe 1 adalah jenis diabetes autoimun dimana sistem kekebalan tubuh menyerang sel-sel di pankreas yang memproduksi insulin. Akibatnya, tubuh tidak dapat memproduksi insulin, yang diperlukan untuk mengontrol kadar gula darah. Diabetes tipe 1 biasanya muncul pada usia muda, tetapi dapat terjadi pada usia berapa pun."
    answer3 = "Diabetes tipe 2 adalah jenis diabetes yang paling umum, di mana tubuh menjadi resisten terhadap insulin atau tidak menghasilkan cukup insulin. Hal ini sering dikaitkan dengan faktor gaya hidup seperti obesitas, kurang aktivitas fisik, dan pola makan tidak sehat. Diabetes tipe 2 lebih umum terjadi pada orang dewasa, meskipun kini semakin sering didiagnosis pada anak-anak dan remaja."
    answer4 = "Gejala diabetes yang umum meliputi sering merasa haus, sering buang air kecil, penurunan berat badan tanpa sebab yang jelas, rasa lelah yang berlebihan, dan penglihatan kabur. Pada diabetes tipe 1, gejala sering muncul secara tiba-tiba, sedangkan pada diabetes tipe 2, gejala dapat berkembang perlahan dan mungkin tidak disadari selama bertahun-tahun."
    answer5 = "Penyebab diabetes tipe 1 belum diketahui secara pasti, tetapi faktor genetik dan lingkungan diduga berperan dalam memicu respons autoimun. Diabetes tipe 2 lebih dipengaruhi oleh gaya hidup, seperti pola makan tinggi gula, obesitas, dan kurangnya aktivitas fisik. Faktor genetik juga dapat meningkatkan risiko seseorang terkena diabetes tipe 2."
    answer6 = "Diabetes yang tidak terkontrol dapat menyebabkan berbagai komplikasi serius, seperti penyakit jantung, stroke, kerusakan ginjal, kerusakan saraf, dan masalah penglihatan, termasuk kebutaan. Selain itu, diabetes juga dapat menyebabkan luka yang sulit sembuh, yang berisiko menyebabkan infeksi serius dan amputasi pada kasus yang parah."
    answer7 = "Pola hidup sehat untuk penderita diabetes mencakup mengatur pola makan yang seimbang dan rendah gula, rutin berolahraga untuk meningkatkan sensitivitas insulin, menjaga berat badan ideal, dan memantau kadar gula darah secara rutin. Menghindari merokok dan membatasi konsumsi alkohol juga sangat dianjurkan untuk menjaga kesehatan jangka panjang."
            
    with messages:
        # Display chat message dari history app rerun
        for history in st.session_state.history:
            with st.chat_message(history["role"]):
                st.markdown(history["content"])
            
        if option == "Apa yang dimaksud dengan diabetes?":
            # Tambah user message ke chat history
            st.session_state.history.append({"role": "user", "content": option})
            # Tambah message dari user
            st.chat_message("user").write(option)
            
            # Tambah respons chatbot dalam container
            with st.chat_message("assistant"):
                response = st.write_stream(response_generator(answer1))
            # Tambah respons chatbot ke chat history
            st.session_state.history.append({"role": "assistant", "content": response})
        elif option == "Bisa jelaskan apa itu diabetes tipe 1?":
            # Tambah user message ke chat history
            st.session_state.history.append({"role": "user", "content": option})
           # Tambah message dari user
            st.chat_message("user").write(option)
            
            # Tambah respons chatbot dalam container
            with st.chat_message("assistant"):
                response = st.write_stream(response_generator(answer2))
            # Tambah respons chatbot ke chat history
            st.session_state.history.append({"role": "assistant", "content": response})
        elif option == "Bisa jelaskan apa itu diabetes tipe 2?":
            # Tambah user message ke chat history
            st.session_state.history.append({"role": "user", "content": option})
            # Tambah message dari user
            st.chat_message("user").write(option)
            
            # Tambah respons chatbot dalam container
            with st.chat_message("assistant"):
                response = st.write_stream(response_generator(answer3))
            # Tambah respons chatbot ke chat history
            st.session_state.history.append({"role": "assistant", "content": response})
        elif option == "Gejala diabetes itu apa saja, ya?":
            # Tambah user message ke chat history
            st.session_state.history.append({"role": "user", "content": option})
            # Tambah message dari user
            st.chat_message("user").write(option)
            
            # Tambah respons chatbot dalam container
            with st.chat_message("assistant"):
                response = st.write_stream(response_generator(answer4))
            # Tambah respons chatbot ke chat history
            st.session_state.history.append({"role": "assistant", "content": response})
        elif option == "Apa sih yang menyebabkan diabetes?":
            # Tambah user message ke chat history
            st.session_state.history.append({"role": "user", "content": option})
            # Tambah message dari user
            st.chat_message("user").write(option)
            
            # Tambah respons chatbot dalam container
            with st.chat_message("assistant"):
                response = st.write_stream(response_generator(answer5))
            # Tambah respons chatbot ke chat history
            st.session_state.history.append({"role": "assistant", "content": response})
        elif option == "Apa saja bahaya yang bisa ditimbulkan oleh diabetes?":
            # Tambah user message ke chat history
            st.session_state.history.append({"role": "user", "content": option})
            # Tambah message dari user
            st.chat_message("user").write(option)
            
            # Tambah respons chatbot dalam container
            with st.chat_message("assistant"):
                response = st.write_stream(response_generator(answer6))
            # Tambah respons chatbot ke chat history
            st.session_state.history.append({"role": "assistant", "content": response})
        elif option == "Gimana pola hidup yang sehat untuk penderita diabetes?":
            # Tambah user message ke chat history
            st.session_state.history.append({"role": "user", "content": option})
            # Tambah message dari user
            st.chat_message("user").write(option)
            
            # Tambah respons chatbot dalam container
            with st.chat_message("assistant"):
                response = st.write_stream(response_generator(answer7))
            # Tambah respons chatbot ke chat history
            st.session_state.history.append({"role": "assistant", "content": response})
        
    st.session_state.show_chatbot = False

# CSS styling untuk tambahkan padding di bawah container
st.markdown("""
    <style>
        /* Reduce padding in the bottom container */
        .st-emotion-cache-qdbtli.ea3mdgi2 {
            padding-bottom: 20px !important; /* Adjust the padding-bottom value */
            padding-top: 10px !important; /* Adjust the padding-bottom value */
            padding-left: 16px !important; /* Adjust the padding-bottom value */
            padding-right: 10px !important; /* Adjust the padding-bottom value */  
        }
        /* button chatbot */
        .st-emotion-cache-1g5xx45 {
            border-radius: 50% !important;
            padding: 10px 12px !important;
        }
    </style>
""", unsafe_allow_html=True)

with bottom():
    col1, col2 = st.columns([16, 1])
    # Streamlit-native circular button
    with col2:
        circular_button = st.button(
            "💬",  # Material Icon or emoji untuk ikon chat
            help="Open Chatbot",
            type="primary"
        )

# cek apakah circular button diklik
if circular_button:
    st.session_state.show_chatbot = not st.session_state.show_chatbot

# Jalankan chatbot logic
if st.session_state.show_chatbot:
    showChatbot()
    
    
#  =============================== REKOMENDASI OBAT ===============================
# https://raw.githubusercontent.com/slviamrgrta/Dataset/refs/heads/main/Obat%20Diabetes%20Tipe%201%20dan%20Tipe%202.csv

# Load/muat dataset rekomendasi obat
rekomendasi_data_path = 'https://raw.githubusercontent.com/slviamrgrta/Dataset/refs/heads/main/Obat%20Diabetes%20Tipe%201%20dan%20Tipe%202.csv'  
rekomendasi_data = pd.read_csv(rekomendasi_data_path)

# Fungsi untuk rekomendasi obat
def recommendMedication(diabetes_type):
    # Filter dataset berdasarkan tipe diabetes
    recommendations = rekomendasi_data[rekomendasi_data['Target'] == diabetes_type]
    return recommendations[['Nama Obat', 'Nama Generik', 'Harga', 'Bintang', 'RX/OTC', 'Alkohol']]

with layoutCol3:
    st.header("Rekomendasi Obat")
    # divider
    st.markdown("""
        <hr style="margin: 0px 0; border: 0.20px solid #ccc;" />
    """, unsafe_allow_html=True)
    
    # Tampilkan dataset dalam tabel
    medication = recommendMedication(diabetes_type)
    st.dataframe(medication, hide_index=True)
    
    #  ========= Note RX/OTC =========
    st.markdown("""
        <p style="margin: 0;"><b>Note:</b></p>
        <p style="margin: 0;"><i>RX:</i> Dibutuhkan resep dokter</p>
        <p style="margin: 0;"><i>OTC:</i> Dapat dibeli tanpa resep dokter</p>
    """, unsafe_allow_html=True)

with padding2:
    pass

paddingRujukan1, layoutPadRujukan, paddingRujukan2 = st.columns([0.5, 9, 0.5])

with paddingRujukan1:
    pass

with layoutPadRujukan:

    #  =============================== Layanan Rujukan  ===============================
    # Load/muat dataset layanan rujukan
    layanan_rujukan_path = 'https://raw.githubusercontent.com/chellecia/Dataset/refs/heads/main/data_rumahsakitBPJS.csv'
    layanan_rujukan = pd.read_csv(layanan_rujukan_path)

    # Drop the 'KodeFaskes' column
    layanan_rujukan = layanan_rujukan.drop(columns=["KodeFaskes"])

    # Get distinct values for 'Provinsi'
    distinct_provinsi = ["-- Pilih Provinsi --"] + layanan_rujukan["Provinsi"].drop_duplicates().tolist()


    st.header("Layanan Rujukan")
    # divider
    st.markdown("""
        <hr style="margin: 0px 0; border: 0.20px solid #ccc;" />
    """, unsafe_allow_html=True)

    # Pilih provinsi
    selected_provinsi = st.selectbox("Provinsi:", options=distinct_provinsi)

    # Tampilkan dataframe hanya jika provinsi yang dipilih valid
    if selected_provinsi != "-- Pilih Provinsi --":
        st.write(f"Daftar Fasilitas Kesehatan untuk Provinsi: {selected_provinsi}")
        # Filter rumah sakit berdasarkan provinsi yang dipilih
        filtered_hospitals = layanan_rujukan[layanan_rujukan["Provinsi"] == selected_provinsi].drop(columns=["Provinsi"])

        layanan_rujukan.rename(columns={"TipeFaskes": "Tipe", "NamaFaskes": "Nama", "AlamatFaskes": "Alamat"})

        # Tampilkan rumah sakit yang sudah difilter dalam tabel
        st.dataframe(filtered_hospitals, hide_index=True)
    else:
        st.write("Silakan pilih provinsi terlebih dahulu.")

with paddingRujukan2:
    pass

st.markdown("</div>", unsafe_allow_html=True)
