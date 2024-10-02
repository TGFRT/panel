import streamlit as st
from google_auth_st import add_auth

# Configurar la página
st.set_page_config(page_title="Mi App", page_icon="🔒")

# Advertencia antes de iniciar sesión
st.warning("Inicia sesión para continuar.")

# Obtener los secretos
client_id = st.secrets["google"]["client_id"]
client_secret = st.secrets["google"]["client_secret"]
redirect_uri = st.secrets["google"]["redirect_uris"][0]

# Agregar autenticación
add_auth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

if 'email' in st.session_state:
    st.success("¡Bienvenido de nuevo!")
    st.write(f"Tu correo: {st.session_state.email}")
else:
    st.warning("Por favor, inicia sesión.")
