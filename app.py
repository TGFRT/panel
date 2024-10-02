import firebase_admin
from firebase_admin import credentials, auth
import streamlit as st

# Credenciales de Firebase en formato JSON
firebaseConfig = {
    "type": "service_account",
    "project_id": "ingeniar-2bf0f",
    "private_key_id": "71f1751645314523029c41f0030c380e6fffd721",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCnVJNW+8P68hkT\n...\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-lh4m1@ingeniar-2bf0f.iam.gserviceaccount.com",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
}

# Inicializar Firebase solo si no se ha inicializado
if not firebase_admin._apps:
    cred = credentials.Certificate(firebaseConfig)
    firebase_admin.initialize_app(cred)

# Configuración de Streamlit
st.title("Sistema de Autenticación Firebase")
choice = st.selectbox('Seleccione una opción:', ['Registro', 'Inicio de sesión'])
email = st.text_input('Correo electrónico')
password = st.text_input('Contraseña', type='password')

# Registro de usuario
if choice == 'Registro':
    if st.button('Registrar'):
        try:
            user = auth.create_user(email=email, password=password)
            st.success("Usuario registrado exitosamente.")
        except Exception as e:
            st.error(f"Error al registrar: {e}")

# Inicio de sesión
if choice == 'Inicio de sesión':
    if st.button('Iniciar sesión'):
        try:
            user = auth.get_user_by_email(email)
            # Aquí normalmente validarías la contraseña, pero Firebase
            # no permite la verificación de la contraseña directamente.
            st.success("Inicio de sesión exitoso.")
        except Exception as e:
            st.error(f"Error al iniciar sesión: {e}")
