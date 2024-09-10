import streamlit as st
import login

login.generar_login()
if 'usuario' in st.session_state:
    st.header('Banco de :orange[datos]')

##############################################


uploaded_files = st.file_uploader(
    "Cargar datos", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)


##############################################


col1, col2 = st.columns(2)
with col1:
    st.subheader("Product & Address Info...")
    col21, col22 = st.columns(2)
    with col21:
        length = st.number_input("Product Length (cm)",value=0)
        width = st.number_input("Product Width (cm)",value=0)   
        height = st.number_input("Product Height (cm)",value=0)
        weight = st.number_input("Weight (Piece)",value=0)
    with col22:
        item_quantity = st.number_input("Item Quantity (pieces)",value=0)
        box_quantity = st.number_input("Box Quantity (pieces)",value=0)
        total_weight = st.number_input("Total Weight (kgs)",value=weight*box_quantity)
        cbm = st.number_input("CBM (m3)",value=(((length*width*height)/1000000)*box_quantity))

with col2.container():
    st.write("You can use this column space for anything else...")