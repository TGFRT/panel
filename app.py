import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# Credenciales de Google
CREDENTIALS = {
    "type": "service_account",
    "project_id": "login-437414",
    "private_key_id": "fca9d2d40464832cbb43bceab36b36c3abdd592b",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC2NzAc+ud3Nygb\n...\n-----END PRIVATE KEY-----\n",
    "client_email": "ingeniar@login-437414.iam.gserviceaccount.com",
    "client_id": "116651559499176329974",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/ingeniar%40login-437414.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

# Configuración de credenciales
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# Cargar las credenciales desde el diccionario
creds = ServiceAccountCredentials.from_json_keyfile_dict(CREDENTIALS, scope)
client = gspread.authorize(creds)

# Abre la hoja de cálculo
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1prl2yPkqMDeUdA7Gi0NoSz6aqnORsRMDNou36yFbpbA/edit"
sheet = client.open_by_url(spreadsheet_url).worksheet("Registros de Usuarios")

# Formulario de registro
st.title("Registro de Usuarios")
name = st.text_input("Nombre")
email = st.text_input("Correo Electrónico")

if st.button("Registrar"):
    if name and email:
        sheet.append_row([name, email])
        st.success("Registro exitoso!")
    else:
        st.error("Por favor completa todos los campos.")

# Opcional: Mostrar los registros existentes
st.subheader("Registros Existentes")
records = sheet.get_all_records()
if records:
    st.write(records)
else:
    st.write("No hay registros disponibles.")
