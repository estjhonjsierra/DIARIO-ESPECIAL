import streamlit as st
import datetime

# Configuración de la página
st.set_page_config(page_title="Para Carolina", page_icon="❤️")

# Título y estilo
st.title("❤️ Un mensaje para Carolina")
st.subheader("Un detalle para recordarte lo especial que eres.")

# --- TU LISTA DE MENSAJES (Puedes añadir los 365 aquí) ---
mensajes = [
    "Eres lo mejor que me ha pasado, Carolina. ✨",
    "Espero que tu día sea tan brillante como tu sonrisa. 😊",
    "Hoy es un gran día para decirte que te quiero mucho. ❤️",
    "Eres mi pensamiento favorito cada mañana. ☕",
    "Gracias por ser como eres, Carolina. Eres única. 🌟",
    "Un día más para agradecer que coincidimos. 🥰"
]

def obtener_mensaje_del_dia(lista_mensajes):
    # Obtenemos el día del año (1 al 365)
    dia_del_anio = datetime.datetime.now().timetuple().tm_yday
    indice = dia_del_anio % len(lista_mensajes)
    return lista_mensajes[indice]

mensaje_hoy = obtener_mensaje_del_dia(mensajes)

st.markdown("---")
st.markdown(
    f"""
    <div style="
        background-color: #ffe4e1; 
        padding: 30px; 
        border-radius: 15px; 
        border: 2px solid #ffb6c1;
        text-align: center;
    ">
        <h2 style="color: #d87093;">Mensaje de hoy:</h2>
        <p style="font-size: 24px; color: #333; font-style: italic;">
            "{mensaje_hoy}"
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)
st.markdown("---")

if st.button("Haz clic si sonreíste"):
    st.balloons()
    st.success("¡Esa es la idea! Que tengas un lindo día, Caro.")
