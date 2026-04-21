import streamlit as st
import datetime
import base64

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Mi Diario Especial", page_icon="📖", layout="wide")

# 2. HORA COLOMBIA
ahora_utc = datetime.datetime.utcnow()
hoy = ahora_utc + datetime.timedelta(hours=-5)

dias = {"Monday": "Lunes", "Tuesday": "Martes", "Wednesday": "Miércoles", "Thursday": "Jueves", "Friday": "Viernes", "Saturday": "Sábado", "Sunday": "Domingo"}
meses = {"April": "Abril", "May": "Mayo", "June": "Junio", "July": "Julio", "August": "Agosto", "September": "Septiembre", "October": "Octubre", "November": "Noviembre", "December": "Diciembre"}
fecha_visual = f"{dias.get(hoy.strftime('%A'))}, {hoy.day} de {meses.get(hoy.strftime('%B'))}"

# 3. PROCESAMIENTO DE IMAGEN
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        return base64.b64encode(f.read()).decode()

try:
    bin_str = get_base64('fondo_carolina.jpg.png')
    fondo_img = f"data:image/png;base64,{bin_str}"
except:
    fondo_img = ""

# 4. ESTILOS CSS (DISEÑO LADO A LADO)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Quicksand:wght@400;700&display=swap');
    
    .stApp {{
        background: linear-gradient(135deg, #fce4ec 0%, #f3e5f5 100%);
    }}

    .header-diario {{
        font-family: 'Dancing Script', cursive;
        color: #d81b60;
        font-size: 50px;
        text-align: center;
        padding-bottom: 20px;
    }}

    .contenedor-horizontal {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 40px;
        padding: 20px;
        flex-wrap: nowrap;
    }}

    .foto-seccion {{
        flex: 1;
        max-width: 400px;
        border-radius: 30px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        border: 5px solid white;
        overflow: hidden;
    }}

    .foto-seccion img {{ width: 100%; display: block; }}

    .mensaje-seccion {{
        flex: 1.2;
        max-width: 500px;
        background: white;
        padding: 35px;
        border-radius: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        text-align: center;
    }}

    .titulo-carta {{ font-family: 'Dancing Script', cursive; color: #d81b60; font-size: 40px; }}
    .fecha-badge {{ background: #d81b60; color: white; font-family: 'Quicksand', sans-serif; padding: 5px 15px; border-radius: 20px; font-size: 13px; display: inline-block; margin-bottom: 20px; }}
    .texto-amor {{ font-family: 'Quicksand', sans-serif; font-size: 18px; color: #444; line-height: 1.6; margin-bottom: 15px; }}
    .firma {{ font-family: 'Dancing Script', cursive; color: #d81b60; font-size: 32px; text-align: right; margin-bottom: 25px; }}

    div.stButton > button {{
        background-color: #d81b60 !important;
        color: white !important;
        border-radius: 25px !important;
        border: none !important;
        padding: 10px 20px !important;
        font-family: 'Quicksand', sans-serif !important;
        font-weight: 700 !important;
        width: 100%;
        box-shadow: 0 4px 15px rgba(216, 27, 96, 0.3);
    }}

    header, footer {{ visibility: hidden; }}
    </style>
    """, unsafe_allow_html=True)

# 5. MENSAJES DEL MES
mensajes = {
    "20-04": "Carolina, hoy te pienso y quiero decirte que iniciamos este diario para reconocer la gran mujer que eres. Tu elegancia y tu inteligencia son admirables, pero ver cómo te esfuerzas cada día por el bienestar de tu hija me demuestra la nobleza de tu corazón.",
    "21-04": "Hay una sofisticación única en ti, Carolina. Me impresiona cómo logras equilibrar tu vida con tanta madurez. Tu hija tiene el mejor ejemplo de lo que significa ser una mujer valiente y decidida.",
    "22-04": "Es el momento perfecto para resaltar tu resiliencia. Tienes una fortaleza interna que te permite enfrentar los retos con calma. Admiro tu tenacidad y el amor infinito que le entregas a tu pequeña.",
    "23-04": "Tu mirada proyecta una sabiduría que va mucho más allá de las palabras. Tienes un estilo propio y una autenticidad que te hace destacar sobre los demás.",
    "24-04": "¡Viernes! Tienes un carisma genuino que se complementa con tu madurez. Eres de esas personas que dejan huella simplemente por ser consistentes en lo que hacen.",
    "25-04": "Admiro esa disciplina impecable que tienes, Carolina. Mientras muchos descansan, tú sigues adelante con tus responsabilidades con una sonrisa.",
    "26-04": "La verdadera distinción está en tu trato y en la profundidad de tus pensamientos. Eres una mujer de gran corazón y principios firmes.",
    "27-04": "Tu potencial es inmenso y tu capacidad de aprendizaje es algo que siempre destaca. Tienes una mente curiosa que te llevará muy lejos.",
    "28-04": "Tu presencia es sinónimo de equilibrio. La forma en la que gestionas tus responsabilidades dice mucho de tu gran calidad humana.",
    "29-04": "Brillas por tu intelecto y tu bondad. Eres una mujer con mucha sustancia y valores claros. Tu hija es muy afortunada de tenerte.",
    "30-04": "Cerrando el mes. Eres una inspiración constante de superación. Has demostrado que se puede ser firme y dulce al mismo tiempo.",
    "01-05": "¡Bienvenido mayo! Tu determinación es tu mejor carta. Admiro cómo te exiges para ser mejor cada día. Que este mes te traiga mucha paz.",
    "02-05": "Admiro esa capacidad que tienes para enfrentar el trabajo con una profesionalidad impecable. Eres una mujer todoterreno.",
    "03-05": "Tu paz interior se nota. Admiro cómo cuidas de tu espacio personal y cómo valoras a tu familia por sobre todo.",
    "04-05": "Tu capacidad de organización es digna de aplauso. Tienes una mente estratégica que sabe identificar las mejores oportunidades.",
    "05-05": "Tu belleza cautiva, pero tu conversación es lo que realmente atrapa. Eres una mujer integral en todos los sentidos.",
    "06-05": "Hoy quiero resaltar tu valentía. No cualquiera es tan honesta y transparente como tú. Tu sinceridad es un rasgo muy valioso.",
    "07-05": "Un recordatorio de lo mucho que vales. Tu impacto en los demás es siempre positivo. Tienes un magnetismo personal único.",
    "08-05": "Admiro la pasión que le pones a cada proyecto. Eres una mujer que no hace nada a medias, siempre das lo mejor de ti.",
    "09-05": "Ver tu compromiso con el trabajo y tu responsabilidad me hace admirarte aún más. Eres una mujer brillante y constante.",
    "10-05": "La elegancia es ser recordada por la calidad humana, y tú lo eres. Reconozco lo increíble que eres en cada rol de tu vida.",
    "11-05": "Tu potencial es un motor que no se detiene. Tienes una visión de futuro clara y ambiciosa. Sigue adelante con esa convicción.",
    "12-05": "Tu sonrisa es el reflejo de una mente que sabe encontrar belleza en lo cotidiano. Eres una mujer que sabe levantarse con fuerza.",
    "13-05": "Elogio tu criterio, Carolina. Tienes una capacidad crítica fundamental para tomar siempre las mejores decisiones.",
    "14-05": "Tu estilo es impecable, pero tu ética es lo que más admiro. Eres una persona íntegra y eso te da un valor inmenso.",
    "15-05": "Termina esta semana con satisfacción. Tu esfuerzo diario siempre rinde frutos. Tu inteligencia es tu mejor guía.",
    "16-05": "Reconozco que tu capacidad de trabajo es admirable. Eres una mujer que no se rinde y que enfrenta cada reto con la frente en alto.",
    "17-05": "Espero que la tranquilidad te acompañe hoy. Admiro tu capacidad de estar en armonía contigo misma y con tu entorno.",
    "18-05": "Tu inteligencia es tu mayor activo. Tienes la combinación perfecta de cerebro y un corazón lleno de bondad.",
    "19-05": "Hoy cerramos este ciclo de 30 días. Espero que te sientas muy valorada, porque tu esencia te hace única. Te admiro profundamente."
}

# 6. ESTRUCTURA VISUAL
st.markdown('<div class="header-diario">🌸 MI DIARIO ESPECIAL 🌸</div>', unsafe_allow_html=True)

llave = hoy.strftime("%d-%m")
msg = mensajes.get(llave, "Carolina, eres una mujer excepcional.")

# Contenedor Lado a Lado
st.markdown('<div class="contenedor-horizontal">', unsafe_allow_html=True)

# Lado 1: La Foto
st.markdown(f'<div class="foto-seccion"><img src="{fondo_img}"></div>', unsafe_allow_html=True)

# Lado 2: El Mensaje
st.markdown(f"""
    <div class="mensaje-seccion">
        <div class="titulo-carta">Para Carolina ✨</div>
        <div class="fecha-badge">{fecha_visual.upper()}</div>
        <div class="texto-amor">"{msg}"</div>
        <div class="firma">Con cariño, Jhon</div>
""", unsafe_allow_html=True)

# Botón dentro del cuadro del mensaje
if st.button("💖 Confirmar lectura"):
    st.balloons()

st.markdown('</div></div>', unsafe_allow_html=True)
