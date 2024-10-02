import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuración de credenciales
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# Asegúrate de que el archivo JSON esté en el mismo directorio que este script
creds = ServiceAccountCredentials.from_json_keyfile_name('path_to_your_json.json', scope)
client = gspread.authorize(creds)

# Abre la hoja de cálculo
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1prl2yPkqMDeUdA7Gi0NoSz6aqnORsRMDNou36yFbpbA/edit"
sheet = client.open_by_url(spreadsheet_url).sheet1

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
