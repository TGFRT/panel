import pyrebase
import streamlit as st
from datetime import datetime  # Corrección aquí

# Configuración de Firebase
firebaseConfig = {
    'apiKey': "AIzaSyAhLyQavE-w86x-iZE-hOsdZjIBgMD1uME",
    'authDomain': "ingeniar-2bf0f.firebaseapp.com",
    'projectId': "ingeniar-2bf0f",
    'databaseURL': "https://ingeniar-2bf0f-default-rtdb.firebaseio.com/",  # Coma añadida
    'storageBucket': "ingeniar-2bf0f.appspot.com",
    'messagingSenderId': "460609687453",
    'appId': "1:460609687453:web:e4c39499a399f0011e6974",
    'measurementId': "G-178TVKQJX9"
}

# Inicializar Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Inicializar base de datos y almacenamiento
db = firebase.database()  # Corrección aquí
storage = firebase.storage()

# Título de la barra lateral
st.sidebar.title("IngenIAr")

# Selección de inicio de sesión o registro
choice = st.sidebar.selectbox('Inicio de sesión/Registro', ['Inicio de sesión', 'Registro'])
email = st.sidebar.text_input('Ingrese su correo')
password = st.sidebar.text_input('Ingrese su contraseña', type='password')  # Mejorar la seguridad

# Aquí puedes agregar la lógica para el inicio de sesión o el registro.
