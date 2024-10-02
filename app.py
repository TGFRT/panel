import pyrebase4 as pyrebase
import streamlit as st
from datetime import datetime

# Configuración de Firebase
firebaseConfig = {
    'apiKey': "AIzaSyAhLyQavE-w86x-iZE-hOsdZjIBgMD1uME",
    'authDomain': "ingeniar-2bf0f.firebaseapp.com",
    'projectId': "ingeniar-2bf0f",
    'databaseURL': "https://ingeniar-2bf0f-default-rtdb.firebaseio.com/",
    'storageBucket': "ingeniar-2bf0f.appspot.com",
    'messagingSenderId': "460609687453",
    'appId': "1:460609687453:web:e4c39499a399f0011e6974",
    'measurementId': "G-178TVKQJX9"
}

# Inicializar Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

# Título de la barra lateral
st.sidebar.title("IngenIAr")

# Selección de inicio de sesión o registro
choice = st.sidebar.selectbox('Inicio de sesión/Registro', ['Inicio de sesión', 'Registro'])
email = st.sidebar.text_input('Ingrese su correo')
password = st.sidebar.text_input('Ingrese su contraseña', type='password')  # Seguridad mejorada

# Lógica de inicio de sesión y registro
if choice == 'Inicio de sesión':
    if st.sidebar.button('Iniciar sesión'):
        try:
            auth.sign_in_with_email_and_password(email, password)
            st.success("Inicio de sesión exitoso")
        except Exception as e:
            st.error(f"Error: {e}")

if choice == 'Registro':
    if st.sidebar.button('Registrar'):
        try:
            auth.create_user_with_email_and_password(email, password)
            st.success("Registro exitoso")
        except Exception as e:
            st.error(f"Error: {e}")
