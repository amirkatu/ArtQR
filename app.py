import streamlit as st
import qrcode
from PIL import Image
import io

st.set_page_config(page_title="ArtQR", page_icon="🎨", layout="centered")

st.title("🎨 ArtQR")
st.caption(" By AMIRREZA")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🌈 Colored QR")
    text1 = st.text_input("Text or URL", placeholder="https://github.com/AMIRREZA", key="c")
    fill = st.color_picker("QR Color", "#0066FF", key="f")
    back = st.color_picker("Background", "#FFFFFF", key="b")
    
    if st.button("Generate Colored QR", type="primary", use_container_width=True):
        qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
        qr.add_data(text1 or " ")
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill, back_color=back)
        buf = io.BytesIO()
        img.save(buf, "PNG")
        buf.seek(0)
        st.image(buf, use_container_width=True)
        st.download_button("Download PNG", buf, "colored-qr.png", "image/png", use_container_width=True)

with col2:
    st.markdown("### 🖼️ QR with Logo")
    text2 = st.text_input("URL or Text", placeholder="https://t.me", key="l")
    logo = st.file_uploader("Upload Logo", ["png", "jpg", "jpeg"], key="up")
    
    if st.button("Generate with Logo", type="primary", use_container_width=True) and text2:
        qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
        qr.add_data(text2)
        qr.make(fit=True)
        img = qr.make_image(fill_color="#000000", back_color="#FFFFFF").convert("RGBA")
        
        if logo:
            logo_img = Image.open(logo).convert("RGBA")
            size = img.size[0] // 5
            logo_img = logo_img.resize((size, size))
            pos = ((img.size[0] - size) // 2, (img.size[1] - size) // 2)
            img.paste(logo_img, pos, logo_img)
        
        buf = io.BytesIO()
        img.save(buf, "PNG")
        buf.seek(0)
        st.image(buf, use_container_width=True)
        st.download_button("Download with Logo", buf, "logo-qr.png", "image/png", use_container_width=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #888; font-size: 14px;'>Made with ❤️ by <b>AMIRREZA</b></p>", unsafe_allow_html=True)