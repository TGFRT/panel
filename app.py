import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth

# Configuración de Firebase usando las credenciales
firebaseConfig = {
    "type": "service_account",
    "project_id": "ingeniar-2bf0f",
    "private_key_id": "71f1751645314523029c41f0030c380e6fffd721",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCnVJNW+8P68hkT\n...\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-lh4m1@ingeniar-2bf0f.iam.gserviceaccount.com",
    "client_id": "107021846106332628800",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-lh4m1%40ingeniar-2bf0f.iam.gserviceaccount.com",
}

cred = credentials.Certificate(firebaseConfig)
firebase_admin.initialize_app(cred)

# Funciones de autenticación
def register_user(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        return user.uid
    except Exception as e:
        return str(e)

def login_user(email, password):
    try:
        user = auth.get_user_by_email(email)
        # Aquí puedes agregar lógica para verificar la contraseña con un token o similar
        return user.uid
    except Exception as e:
        return str(e)

# Interfaz de usuario
st.title("Bienvenido a IngenIAr")

# Selección de acción
choice = st.sidebar.selectbox("Selecciona una opción", ["Inicio de sesión", "Registro"])

if choice == "Registro":
    email = st.text_input("Correo electrónico")
    password = st.text_input("Contraseña", type="password")
    
    if st.button("Registrar"):
        result = register_user(email, password)
        if isinstance(result, str):
            st.error(f"Error al registrar: {result}")
        else:
            st.success("¡Registro exitoso! Usuario creado.")

elif choice == "Inicio de sesión":
    email = st.text_input("Correo electrónico")
    password = st.text_input("Contraseña", type="password")
    
    if st.button("Iniciar sesión"):
        result = login_user(email, password)
        if isinstance(result, str):
            st.error(f"Error al iniciar sesión: {result}")
        else:
            st.success("¡Inicio de sesión exitoso!")
            # Aquí puedes redirigir al usuario a la página principal de la aplicación

# Enlaces adicionales
st.markdown("¿No tienes una cuenta? [Regístrate aquí](https://www.example.com/signup)")
st.markdown("¿Olvidaste tu contraseña? [Restablecer contraseña](https://www.example.com/reset-password)")
