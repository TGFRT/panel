import firebase_admin
from firebase_admin import credentials, auth, db
import streamlit as st

# Inicializar la aplicación de Firebase
cred = credentials.Certificate("credentials.json")  # Asegúrate de que este archivo esté en la ruta correcta
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ingeniar-2bf0f-default-rtdb.firebaseio.com/'
})

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
            user = auth.get_user_by_email(email)
            st.success("Inicio de sesión exitoso")
            # Aquí puedes agregar más lógica según tus necesidades
        except Exception as e:
            st.error(f"Error: {e}")

if choice == 'Registro':
    if st.sidebar.button('Registrar'):
        try:
            user = auth.create_user(email=email, password=password)
            st.success("Registro exitoso")
        except Exception as e:
            st.error(f"Error: {e}")
