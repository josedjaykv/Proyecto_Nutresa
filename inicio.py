import streamlit as st
import login

st.header(':orange[CroskAI]')
login.generar_login()

if 'usuario' in st.session_state:
    st.markdown('<h5>En esta sección podrá visualizar los módulos que tiene activos para el análisis del impacto financiero de los riesgos climáticos de transición en su organización.</h5>', unsafe_allow_html=True)

    st.header("Mis módulos")
    
    # Lista de módulos con enlaces a las páginas
    modules = [
        ("Banco de :orange[datos]", "Visualiza aquí los datos que tienes cargados en la plataforma.", 'pages/Banco_de_datos.py'),
        (":orange[Pronósticos]", "Proyecciones futuras del impacto de riesgos climáticos.", 'pages/Pronosticos.py'),
        ("Análisis de :orange[costos]", "Evalúa los costos derivados de los riesgos climáticos.", 'pages/Analisis_de_costos.py'),
        ("Análisis de :orange[escenarios]", "Explora escenarios climáticos y su impacto financiero.", 'pages/Analisis_de_escenarios.py')
    ]
    
    # Mostrar módulos como tarjetas
    for title, desc, page in modules:
        with st.container():
            st.markdown(f"### {title}")
            st.write(desc)
            if st.button(f"Ir a {title}", key=page):
                # Cambiar de página con `st.switch_page()`
                st.switch_page(page)
