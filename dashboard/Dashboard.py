import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import os

st.set_page_config(
    page_title="E-Commerce Data Analysis",
    page_icon="📊",
)

st.title("DASHBOARD E-COMMERCE PUBLIC DATASET")

with st.sidebar:
    selected = option_menu(
        menu_title="DASHBOARD",
        options=["About Projects","Dataset Overview"],
    )

if selected == "About Projects":
    path = os.path.dirname(__file__)
    my_file = path+'/images/gambar1.jpg'
    image = Image.open(my_file)
    resized_image = image.resize((650, 350))
    st.image(resized_image, caption='E-Comerce Analysis Dashboard')

    st.write("Dashboard ini menggunakan Brazilian E-Commerce Public Dataset sebagai sumber datanya. Dataset ini berisi informasi tentang transaksi e-commerce di Brazil dan memberikan gambaran tentang tren dan pola pembelian online di negara tersebut.")

    

if selected == "Dataset Overview":

    st.write("Dataset yang digunakan adalah E-Commerce Public Dataset.")
    st.write("Dataset ini mencakup informasi yang dikumpulkan dari transaksi e-commerce di Brazil dalam rentang waktu tertentu. Dataset tersebut terdiri dari beberapa file yang terkait satu sama lain dan memberikan wawasan yang komprehensif tentang industri e-commerce di Brazil.")
    st.write("Beberapa file utama dalam dataset ini termasuk:")
    st.write("- Orders: File ini berisi informasi tentang pesanan, seperti ID pesanan, status pesanan, waktu pembelian, waktu persetujuan, dan waktu pengiriman pesanan.")
    st.write("- Order Items: File ini berisi informasi terperinci tentang setiap item yang dibeli dalam pesanan, seperti ID produk, harga produk, jumlah yang dibeli, dan biaya pengiriman.")
    st.write("- Products: File ini berisi informasi tentang produk, termasuk ID produk, kategori produk, dan nama produk.")
    st.write("- Sellers: File ini berisi informasi tentang penjual, seperti ID penjual, nama penjual, dan lokasi penjual (kota dan negara bagian).")
    st.write("- Customers: File ini berisi informasi tentang pelanggan, seperti ID pelanggan, nama pelanggan, dan lokasi pelanggan (kota dan negara bagian).")
    st.write("- Geolocation: File ini menyediakan informasi geografis tentang kota dan negara bagian di Brazil. Ini membantu dalam analisis berdasarkan lokasi geografis.")
    
