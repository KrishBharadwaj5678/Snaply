import streamlit as st

st.set_page_config(
    page_title="Snaply",
    page_icon="icon.png",
    menu_items={
        "About":
        """Snaply makes taking and downloading selfies a breeze. Snap a photo with ease and save it to your device instantly—quick, simple, and perfect for any occasion."""
    })

st.write(
    "<h2 style=color:#6EACDA;>Capture and Download Your Selfie Instantly.</h2>",
    unsafe_allow_html=True)

cap_photo = st.camera_input('')

if cap_photo:
         image_bytes = cap_photo.read()
         st.download_button("Download Image", image_bytes, "snaply.jpeg")
