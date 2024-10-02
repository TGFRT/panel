
import pyrebase
import streamlit as st
from datatime import datetime

firebaseConfig = {
    'apiKey': "AIzaSyAhLyQavE-w86x-iZE-hOsdZjIBgMD1uME",
    'authDomain': "ingeniar-2bf0f.firebaseapp.com",
    'projectId': "ingeniar-2bf0f",
    'databaseURL': "https://ingeniar-2bf0f-default-rtdb.firebaseio.com/"
    'storageBucket': "ingeniar-2bf0f.appspot.com",
    'messagingSenderId': "460609687453",
    'appId': "1:460609687453:web:e4c39499a399f0011e6974",
    'measurementId': "G-178TVKQJX9"
  }

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

db = firebase.databse()
storage = firebase.storage()


st.sidebar.title("IngenIAr")


choice = st.sidebar.selectbox('Inicio de sesión/Registro',['Inicio de sesión','Registro'])
email = st.sidebar.text_input('Ingrese su correo')
password = st.sidebar.text_input('Ingrese su contraseña')

