import streamlit as st
import datetime
import base64

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Mi Diario Especial", page_icon="📖", layout="wide")

# 2. HORA COLOMBIA
ahora_utc = datetime.datetime.utcnow()
hoy = ahora_utc + datetime.timedelta(hours=-5)

dias = {"Monday": "Lunes", "Tuesday": "Martes", "Wednesday": "Miércoles", "Thursday": "Jueves", "Friday": "Viernes", "Saturday": "Sábado", "Sunday": "Domingo"}
meses = {"April": "Abril", "May": "Mayo", "June": "Junio", "July": "Julio", "August": "Agosto", "September": "Septiembre", "October": "Octubre", "November": "Noviembre", "December": "Diciembre"}
fecha_visual = f"{dias.get(hoy.strftime('%A'))}, {hoy.day} de {meses.get(hoy.strftime('%B'))}"

# 3. IMAGEN DE FONDO / FOTO
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        return base64.b64encode(f.read()).decode()

try:
    bin_str = get_base64('fondo_carolina.jpg.png')
    foto_perfil = f"data:image/png;base64,{bin_str}"
except:
    foto_perfil = ""

# 4. ESTILOS CSS (Fondo animado, 3 columnas y diseño premium)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Quicksand:wght@400;700&display=swap');
    
    /* Fondo con movimiento suave */
    .stApp {{
        background: linear-gradient(-45deg, #fce4ec, #f3e5f5, #e1f5fe, #fff9c4);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }}

    @keyframes gradientBG {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    .diario-title {{
        font-family: 'Dancing Script', cursive;
        color: #d81b60;
        font-size: 60px;
        text-align: center;
        margin-top: -30px;
        margin-bottom: 30px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.1);
    }}

    /* Contenedor Triple Columna */
    .contenedor-diario {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
        padding: 20px;
    }}

    /* Estilo Foto con flotación */
    .col-foto {{
        flex: 1;
        max-width: 350px;
        border-radius: 30px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        border: 5px solid white;
        overflow: hidden;
        animation: float 4s ease-in-out infinite;
    }}
    
    @keyframes float {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-15px); }}
    }}

    /* Estilo Mensaje */
    .col-mensaje {{
        flex: 1.5;
        background: rgba(255, 255, 255, 0.9);
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        backdrop-filter: blur(5px);
        border: 2px solid white;
    }}

    /* Estilo Botón */
    .col-confirmar {{
        flex: 0.5;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }}

    .titulo-carta {{ font-family: 'Dancing Script', cursive; color: #d81b60; font-size: 45px; text-align: center; }}
    .fecha-badge {{ background: #d81b60; color: white; font-family: 'Quicksand', sans-serif; padding: 5px 15px; border-radius: 20px; font-size: 14px; display: inline-block; margin-bottom: 20px; }}
    .texto-amor {{ font-family: 'Quicksand', sans-serif; font-size: 19px; color: #444; line-height: 1.6; text-align: center; }}
    .firma {{ font-family: 'Dancing Script', cursive; color: #d81b60; font-size: 32px; text-align: right; margin-top: 20px; }}

    /* Botón Streamlit Personalizado */
    div.stButton > button {{
        background-color: #d81b60 !important;
        color: white !important;
        border-radius: 50% !important;
        width: 120px !important;
        height: 120px !important;
        border: 4px solid white !important;
        font-family: 'Quicksand', sans-serif !important;
        font-weight: bold !important;
        box-shadow: 0 8px 20px rgba(216, 27, 96, 0.4) !important;
        transition: 0.4s !important;
        white-space: normal !important;
        line-height: 1.2 !important;
    }}
    
    div.stButton > button:hover {{
        transform: scale(1.1) rotate(5deg) !important;
        background-color: #ad1457 !important;
    }}

    header, footer {{ visibility: hidden; }}
    </style>
    """, unsafe_allow_html=True)

# 5. TÍTULO PRINCIPAL
st.markdown('<h1 class="diario-title">🌸 Mi Diario Especial para Carolina 🌸</h1>', unsafe_allow_html=True)

# 6. BASE DE DATOS DE MENSAJES (Los 30 días)
mensajes = {
    "20-04": "Carolina, hoy te pienso y quiero decirte que iniciamos este diario para reconocer la gran mujer que eres. Tu elegancia y tu inteligencia son admirables, pero ver cómo te esfuerzas cada día por el bienestar de tu hija me demuestra la nobleza de tu corazón.",
    "21-04": "Hay una sofisticación única en ti, Carolina. Me impresiona cómo logras equilibrar tu vida con tanta madurez. Tu hija tiene el mejor ejemplo de lo que significa ser una mujer valiente y decidida.",
    "22-04": "Mitad de semana, Carolina. Es el momento perfecto para resaltar tu resiliencia. Tienes una fortaleza interna que te permite enfrentar los retos con calma. Admiro tu tenacidad y el amor infinito que le entregas a tu pequeña.",
    "23-04": "Tu mirada proyecta una sabiduría que va mucho más allá de las palabras. Tienes un estilo propio y una autenticidad que te hace destacar. Hoy te pienso y reconozco el valor de tu esfuerzo diario.",
    "24-04": "¡Viernes! Un día para reconocer que tu energía transforma cualquier ambiente. Tienes un carisma genuino que se complementa con tu madurez. Eres de esas personas que dejan huella simplemente por ser consistentes.",
    "25-04": "Sábado. Hoy te pienso y quiero resaltar esa disciplina admirable que tienes, Carolina. Mientras muchos descansan, tú sigues adelante con tus responsabilidades. Tu hija tiene en ti el mejor ejemplo de constancia.",
    "26-04": "Domingo de reflexión. La verdadera distinción, Carolina, está en tu trato y en la profundidad de tus pensamientos. Admiro tu criterio y cómo defiendes tus valores. Eres una mujer de gran corazón.",
    "27-04": "Nueva semana, Carolina. Tu potencial es inmenso y tu capacidad de aprendizaje es algo que siempre destaca. Tienes una mente curiosa que te llevará muy lejos. Eres el motor que impulsa grandes sueños.",
    "28-04": "Carolina, tu presencia es sinónimo de equilibrio. Hoy te pienso y elogio tu madurez; la forma en la que gestionas tus responsabilidades dice mucho de ti. Tu belleza es innegable, pero tu carácter es lo que te hace invencible.",
    "29-04": "Hay personas que brillan por fuera, pero tú brillas por tu intelecto y tu bondad. Hoy te pienso y me doy cuenta de que eres una mujer con mucha sustancia. Tu hija es muy afortunada de tenerte.",
    "30-04": "Cerrando abril con éxito. Carolina, hoy te pienso y te agradezco por ser una inspiración constante de superación. Has demostrado que se puede ser firme y dulce al mismo tiempo.",
    # ... (Sigue agregando hasta completar los 30 días con el mismo formato "DD-MM")
    "19-05": "Carolina, hoy cerramos este ciclo de 30 días pensando en ti. Espero que te sientas muy valorada, porque tu esencia te hace única. Jhon te admira profundamente."
}

# 7. RENDERIZADO DEL DIARIO
llave = hoy.strftime("%d-%m")
msg = mensajes.get(llave, "Carolina, eres una mujer excepcional. Que tengas un día maravilloso.")

# Layout de 3 columnas
c1, c2, c3 = st.columns([1, 1.5, 0.5])

with c1:
    st.markdown(f'<div class="col-foto"><img src="{foto_perfil}" style="width:100%;"></div>', unsafe_allow_html=True)

with c2:
    st.markdown(f"""
        <div class="col-mensaje">
            <div class="titulo-carta">Para Carolina ✨</div>
            <center><div class="fecha-badge">{fecha_visual.upper()}</div></center>
            <div class="texto-amor">"{msg}"</div>
            <div class="firma">Con mucho cariño, Jhon</div>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown('<div style="height: 100px;"></div>', unsafe_allow_html=True) # Espaciador
    if st.button("💖\nConfirmar\nLectura"):
        st.balloons()
        st.success("¡Mensaje leído! ✨")
