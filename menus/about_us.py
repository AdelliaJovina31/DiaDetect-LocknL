import streamlit as st
from PIL import Image
import base64

st.title("Tim Kami")
st.subheader("Lock n Luck")

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
    .st-emotion-cache-1xf0csu {
        display: flex;
        # justify-content: center;
        flex-direction: column;
        gap: 20px;
        margin-top: 20px;
    }
    .e115fcil1 img {
        max-width: 80%;
        width: 150px;
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

    .st-emotion-cache-1jicfl2 {
        width: 100%;
        padding: 2.5rem 0 0 0;
    }
    .e1f1d6gn5 {
        position: relative;
        z-index: 10;
        padding: 0 20px;
    }
    div.st-emotion-cache-12w0qpk:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > img:nth-child(1) {
        max-width: 100%;
        width: 200px;
    }
    # .st-emotion-cache-ocqkz7 {
    #     display: flex;
    #     flex-direction: row;
    #     justify-content: center;
    #     align-items: center;
    #     gap: 40px;
    # }
    </style>
    """,
    unsafe_allow_html=True
)

def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

team_images = ["./images/silvia.jpg", "./images/michelle.png", "./images/gabrielle.jpg", "./images/adellia.png"]
team_names = ["Silvia Margareta", "Michelle Velice Patricia", "Gabrielle Whitney Ciputra", "Adellia Jovina"]

cols = st.columns(len(team_images))
st.markdown("""
    <div id="image-container">
""", unsafe_allow_html=True)

for col, image_path, name in zip(cols, team_images, team_names):
    with col:
        img = Image.open(image_path)
        st.image(img, caption=name, use_container_width=True)

st.markdown("""
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2024 Tim Lock n Luck. All rights reserved.</div>', unsafe_allow_html=True)