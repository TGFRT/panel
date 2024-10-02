import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configura el alcance y las credenciales
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Asegúrate de que el JSON de credenciales esté en la misma carpeta que este script
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Abre la hoja de cálculo
spreadsheet = client.open("Registros de Usuarios")  # Nombre de tu hoja
sheet = spreadsheet.sheet1  # Accede a la primera hoja

# Crea el formulario de registro
st.title("Registro de Usuarios")

nombre = st.text_input("Nombre")
correo = st.text_input("Correo Electrónico")

if st.button("Registrar"):
    if nombre and correo:
        # Añade una nueva fila a la hoja
        sheet.append_row([nombre, correo])
        st.success("Registro exitoso!")
    else:
        st.error("Por favor completa todos los campos.")

# Agrega un enlace a la página de inicio de sesión
st.markdown("¿Ya tienes una cuenta? [Inicia sesión aquí](https://www.example.com/login)")
