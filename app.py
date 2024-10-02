import streamlit as st
from google_auth_st import add_auth
st.warning("Inicia sesion para que puedas ver")
add_auth():
st.success("HOlIIIIIIIIIII")
st.write(st.session_state.email)
