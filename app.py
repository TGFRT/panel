import firebase_admin
from firebase_admin import credentials, auth, db
import streamlit as st

# Credenciales de Firebase directamente en el código
firebaseConfig = {
    "type": "service_account",
    "project_id": "ingeniar-2bf0f",
    "private_key_id": "71f1751645314523029c41f0030c380e6fffd721",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCnVJNW+8P68hkT\nkK0MnyrHusXOI5LIOYB3UGszc+iMRHcpOKvnOAvtxgkPPOm3FwZXNRaCbXfwe4dD\nkVAykF+jFA/slNGkRxmG4k/3kygksR2wT3/0PXVjpdaHCmXQjK3+mVIhcgIcMkys\nG1xx4gLJ9/oVeKfs+uTu+w8zopJczotslB0plPZNo3rs8FTxxJCIytIV0GPvkTMn\nuwQI6nD3qNUB65hHYNWsMENSDF+e3gUzZnuS6RW2i+CLYLyZ+GHyz9q+rXJb+7Zw\n/Agq3qsjDbLlMXOoSgF+jBvBO9HkZpD0QqiNddA1wl82keqPwujd7GAq5jojZlTS\nUMbIULGLAgMBAAECggEAG3gEWf6pjPwKRs50wgItDS2phC4NzgW2g5+1gXRRJBmn\nMCKoAaSPPMDKQvCec1p5xX4nDFE5I8a7jUmBD1PpB0XnWVCS27N6SszDEOLc760N\nsSBT4n3mU+3o+jEoRqSZeZakx23GT+en84boVZ+jEpG9QaIVew8y3tJjC/hvq4FO\nnfzuIq78YoVTXLKK8wFBNi4sMcujjo84OtHnv0/nV7tuPJoG3GUofTGhbN5+VJ0U\nEY56NLfcnxq1eQCnvupcPWG46h+oKZhLBJT+ddeToPpR/cDnYcINH1I4YZe99nMY\nDUViVxkE/dHAcbegvYgCKOJanZ1wWMU20gOMMERAcQKBgQDWfIIvn+4edVfamelR\nt39h4eogOnq8ZTW9qxdMq2XZc2tFWAZPIMxPUdsTW2ydM1HRP3R6HWKgySN7uf7U\np3UlqfbxQRQfXjM6oX3ivaN8Jt3or7yCFMOZNTiQm8mCo9lK+dBpzAY2yQt1phBi\nYUD07R5D7xVrN4bxX4cBIAMlOwKBgQDHt44x7yKWkBJ5HwyWzc6hNAV2En7lGwyG\nCRNBH0Ed979aPigpsgTshVPmSyuNF7g1LNaikkGY8S7wSb9CpxdndIAaACxMyWYx\n9BDLbOvEmIKS60comULhLkBP77/2tLTbRbAiNrm7H1a87/t1kfEMP/utkC4WDU2n\nKfde5AGf8QKBgGMg3kZGgxXeo8DrW1MiHKRPdhZ5EJqbqC/FsBoGKSdL2asN2LSf\ncu3B5h9XJKauvkSYMCv0As5Ox7B6MNV1o4XJvNCZhERPFBwn4Pd3L+TETdEpz1TL\nZe8cEs16wrI3KckmFfWfjsupNTuliXL+gbfxEwjQqbSI0DwkK1AQzINbAoGBAIJr\nVps7K14hFT8tTH5KRa41l39kUqNwR3xb/svfChn0yGu4/WdFDjwaURCpc/Y+UBfB\ngSRG2Dl0/o8ByblP/lOb22+fP06hkm/6juEY7tnCMjqZFC3p76e3GV5aFQSZOyWZ\n24xsKluM+oqFOLOtKzkxqzvLVJ0n8NbB6/12ba0xAoGAKSihFLMXDdwG26g/JYpE\nEXZbeW95NAJfu6HnzTAV4pi1jxmtSHtvBrRZFhP2jJ1Ax36Rvqc3EAxKxqybfpOh\nGvU/CpEF1cWBrPuwy1x08FW/8dpyKOGwhj+sMdghfaYiXCIoZqlWad11mXLEVRox\n64s39dHz+tsg2uIfd/SfVBg=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-lh4m1@ingeniar-2bf0f.iam.gserviceaccount.com",
    "client_id": "107021846106332628800",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-lh4m1%40ingeniar-2bf0f.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

# Inicializar la aplicación de Firebase
cred = credentials.Certificate(firebaseConfig)
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
