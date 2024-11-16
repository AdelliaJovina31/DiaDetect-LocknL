import streamlit as st
import importlib.util
import os

st.set_page_config(page_title="WebApps", layout="wide")

if "to_prediksi" not in st.session_state:
    st.session_state.to_prediksi = False
if "about" not in st.session_state:
    st.session_state.about = False

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, white, #D7C8DF);
    }
    # .st-emotion-cache-1jicfl2 {
    #     width: 100%;
    #     padding: 0;
    # }
    .centered-image img {
        width: 80% !important;
        max-width: 600px;
        height: auto;
    }
    .st-emotion-cache-0 {
        display: flex;
        align-items: center;
    }
    .st-emotion-cache-phe2gf #selamat-datang {
        font-weight: bold;
        font-size: 20px;
    }
    
    .st-emotion-cache-pgf13w #solusi-pintar-pendeteksi-diabetes {
        font-weight: 705;
        color: #D31345;
        font-size: 70px;
        font-family: Arial;
    }
    img {
        border-radius: 10px;
    }
    .st-emotion-cache-1igbibe {
        border: 1px solid white;
        border-radius: 8px;
        margin-top: 15px;
    }
    .st-emotion-cache-1igbibe:hover {
        border-color: #B17BAC;
        color: #B17BAC;
    }
    .st-emotion-cache-1igbibe:focus:not(:active) {
        background-color: #B17BAC;
        color: white;
        border-color: white;
    }
    .st-emotion-cache-1igbibe:active {
        border-color: #B17BAC;
        color: white;
        background-color: #B17BAC;
    }
    @media (min-width: 576px) {
        .st-emotion-cache-1jicfl2 {
            padding-left: 0;
            padding-right: 0;
        }
    }
    .st-emotion-cache-1jicfl2 {
        width: 100%;
        padding: 2.5rem;
    }
    .e1f1d6gn3 {
        display: flex;
        position: relative;
        z-index: 10;
    }

    /* button bawah */
    .st-emotion-cache-7a8fbc > div:nth-child(1) > button:nth-child(1) > div:nth-child(1) > p:nth-child(1) {
        font-weight: bold;
    }
    .st-emotion-cache-1igbibe {
        background-color: #D31345; 
        border:1px solid transparent;
        color: white;
    }
    .st-emotion-cache-1igbibe:hover {
        border-color: #D31345;
        color: #D31345;
        background-color: white; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

def load_beranda():

    st.markdown("<div class='centered-content'>", unsafe_allow_html=True)

    col1, spacer, col2 = st.columns([1, 0.1, 2])

    with col1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.image("images/dokter.png")

    with col2:
        st.markdown("""
            <p id="selamat-datang">Selamat Datang di DiaDetect</p>
            <h2>Solusi Pintar Pendeteksi Diabetes</h2>
            <h4>Kenali Tipe Diabetes Anda Lebih Cepat dan Temukan Rekomendasi Obat yang Sesuai Hanya di Sini!</h4>
            <p>Layanan AI inovatif untuk mengetahui tipe diabetes Anda dan mendapatkan rekomendasi obat yang sesuai. Cepat, sederhana, dan dirancang untuk mendukung kesehatan Anda dengan solusi yang tepat.</p>
        """, unsafe_allow_html=True)

        # Centered button
        _, button_col, _ = st.columns([2, 2, 1])
        with button_col:
            if st.button("Deteksi Sekarang"):
                st.session_state.to_prediksi = True
                st.rerun()
            
    st.markdown("</div>", unsafe_allow_html=True)


def load_prediksi_page():
    prediksi_path = os.path.join("menus", "prediksi.py")
    if os.path.exists(prediksi_path):
        # Import file prediksi.py
        spec = importlib.util.spec_from_file_location("prediksi", prediksi_path)
        prediksi = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(prediksi)
    else:
        st.error("Halaman Prediksi tidak ditemukan.")


def load_about_page():
    about_us_path = os.path.join("menus", "about_us.py")
    if os.path.exists(about_us_path):
        spec = importlib.util.spec_from_file_location("about_us", about_us_path)
        prediksi = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(prediksi)
    else:
        st.error("Halaman Tentang Kami tidak ditemukan.")

# Top navbar
def top_navbar():
    st.markdown(
        """
        <style>
        .e1f1d6gn5 {
            position: relative;
            z-index: 10;
        }
        .logo-text {
            font-size: 32px;
            color: #8A4E9D;
            font-weight: bold;
        }
        .stTooltipHoverTarget button {
            background-color: transparent;
            border-color: transparent;
            color: black;
        }
        .stTooltipHoverTarget button:hover {
            border-color: transparent;
            background-color: #B17BAC;
            color: white;
        }
        .st-emotion-cache-1jicfl2 {
            width: 100%;
            padding: 2.5rem;
        }
        .e1f1d6gn3 {
            display: block !important;
            position: relative;
            z-index: 10;
            justify-content: center;
        }
        @media (min-width: 576px) {
            .st-emotion-cache-7tauuy {
                padding-left: 5rem;
                padding-right: 5rem;
            }
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

    # Navbar container
    st.markdown('<div class="custom-navbar">', unsafe_allow_html=True)

    _, logo, _, col1, col2, col3 = st.columns([0.5, 5, 1, 1, 0.8, 1.5])

    with logo:
        st.markdown('<div class="logo-text">Lock n Luck</div>', unsafe_allow_html=True)

    with col1:
        if st.button("Beranda", key="beranda_btn", help="Halaman Utama", args=(True,)):
            st.session_state.to_prediksi = False
            st.session_state.about = False
            st.rerun()
    
    with col2:
        if st.button("Prediksi", key="prediksi_btn", help="Halaman Prediksi", args=(True,)):
            st.session_state.to_prediksi = True
            st.session_state.about = False
            st.rerun()
    
    with col3:
        if st.button("Tentang Kami", key="about_btn", help="Halaman Tentang Kami", args=(True,)):
            st.session_state.to_prediksi = False
            st.session_state.about = True
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

def main():
    top_navbar()

    if st.session_state.to_prediksi:
        load_prediksi_page()
    elif st.session_state.about:
        load_about_page()
    else:
        load_beranda()

main()
