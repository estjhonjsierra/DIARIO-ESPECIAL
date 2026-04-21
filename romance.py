import streamlit as st
import datetime
import base64

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Para Carolina", page_icon="💖", layout="centered")

# 2. HORA COLOMBIA (UTC-5)
ahora_utc = datetime.datetime.utcnow()
bogota_offset = datetime.timedelta(hours=-5)
hoy = ahora_utc + bogota_offset

dias_semana = {"Monday": "Lunes", "Tuesday": "Martes", "Wednesday": "Miércoles", "Thursday": "Jueves", "Friday": "Viernes", "Saturday": "Sábado", "Sunday": "Domingo"}
meses_anio = {"April": "Abril", "May": "Mayo", "June": "Junio", "July": "Julio", "August": "Agosto", "September": "Septiembre", "October": "Octubre", "November": "Noviembre", "December": "Diciembre"}

dia_nombre = dias_semana.get(hoy.strftime('%A'))
fecha_visual = f"{dia_nombre}, {hoy.day} de {meses_anio.get(hoy.strftime('%B'))}"

# 3. FUNCIÓN PARA LA IMAGEN (GitHub: fondo_carolina.jpg.png)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

try:
    bin_str = get_base64('fondo_carolina.jpg.png')
    fondo_css = f"""
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center 20%;
        animation: zoom_suave 20s infinite alternate;
    }}
    """
except:
    fondo_css = ".stApp { background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); }"

# 4. DISEÑO "VIDRIO" PARA INTEGRAR EL ROSTRO
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Quicksand:wght@400;700&display=swap');
    
    {fondo_css}

    @keyframes zoom_suave {{
        0% {{ transform: scale(1); }}
        100% {{ transform: scale(1.05); }}
    }}

    .main .block-container {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 100vh;
    }}

    .contenedor-carta {{
        background: rgba(255, 255, 255, 0.65); /* Transparencia para ver el rostro */
        backdrop-filter: blur(10px); /* Efecto vidrio esmerilado */
        padding: 40px;
        border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0px 15px 35px rgba(0,0,0,0.2);
        max-width: 600px;
        margin: 0 auto;
        text-align: center;
    }}
    
    .titulo {{ font-family: 'Dancing Script', cursive; color: #d81b60; font-size: 50px; margin-bottom: 10px; text-shadow: 1px 1px 2px white; }}
    .fecha-tag {{ background: rgba(216, 27, 96, 0.9); color: white; font-family: 'Quicksand', sans-serif; padding: 6px 20px; border-radius: 20px; font-size: 15px; display: inline-block; margin-bottom: 25px; }}
    .texto-cuerpo {{ font-family: 'Quicksand', sans-serif; font-size: 20px; color: #1a1a1a; line-height: 1.6; font-weight: 600; text-shadow: 0px 0px 1px white; }}
    .firma-jhon {{ font-family: 'Dancing Script', cursive; color: #d81b60; font-size: 38px; text-align: right; margin-top: 25px; }}
    
    header, footer {{ visibility: hidden; }}
    
    /* Estilo del botón para que no tape */
    .stButton > button {{
        background-color: #d81b60 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 10px 25px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# 5. MENSAJES AUTOMATIZADOS (30 DÍAS)
mensajes = {
    "20-04": "Carolina, hoy te pienso y quiero decirte que iniciamos este diario para reconocer la gran mujer que eres. Tu elegancia y tu inteligencia son admirables, pero ver cómo te esfuerzas cada día por el bienestar de tu hija me demuestra la nobleza de tu corazón. Eres una madre ejemplar y una mujer excepcional.",
    "21-04": "Hay una sofisticación única en ti, Carolina. Me impresiona cómo logras equilibrar tu vida con tanta madurez. Hoy te pienso y celebro esa fuerza que tienes para salir adelante; tu hija tiene el mejor ejemplo de lo que significa ser una mujer valiente y decidida.",
    "22-04": "Mitad de semana, Carolina. Es el momento perfecto para resaltar tu resiliencia. Tienes una fortaleza interna que te permite enfrentar los retos con calma. Admiro tu tenacidad y el amor infinito que le entregas a tu hija.",
    "23-04": "Carolina, tu mirada proyecta una sabiduría que va mucho más allá de las palabras. Tienes un estilo propio y una autenticidad que te hace destacar. Hoy te pienso y reconozco el valor de tu esfuerzo diario.",
    "24-04": "¡Viernes! Un día para reconocer que tu energía transforma cualquier ambiente. Tienes un carisma genuino que se complementa con tu madurez. Eres de esas personas que dejan huella simplemente por ser consistentes.",
    "25-04": "Sábado. Hoy te pienso y quiero resaltar esa disciplina admirable que tienes, Carolina. Mientras muchos descansan, tú sigues adelante con tus responsabilidades. Tu hija tiene en ti el mejor ejemplo de constancia.",
    "26-04": "Domingo de reflexión. La verdadera distinción, Carolina, está en tu trato y en la profundidad de tus pensamientos. Admiro tu criterio y cómo defiendes tus valores. Eres una mujer de gran corazón.",
    "27-04": "Nueva semana, Carolina. Tu potencial es inmenso y tu capacidad de aprendizaje es algo que siempre destaca. Tienes una mente curiosa que te llevará muy lejos. Eres el motor que impulsa grandes sueños.",
    "28-04": "Carolina, tu presencia es sinónimo de equilibrio. Hoy te pienso y elogio tu madurez; la forma en la que gestionas tus responsabilidades dice mucho de ti. Tu belleza es innegable, pero tu carácter es lo que te hace invencible.",
    "29-04": "Hay personas que brillan por fuera, pero tú brillas por tu intelecto y tu bondad. Hoy te pienso y me doy cuenta de que eres una mujer con mucha sustancia. Tu hija es muy afortunada de tenerte.",
    "30-04": "Cerrando abril con éxito. Carolina, hoy te pienso y te agradezco por ser una inspiración constante de superación. Has demostrado que se puede ser firme y dulce al mismo tiempo.",
    "01-05": "¡Bienvenido mayo! Un nuevo mes para verte brillar. Carolina, tu determinación es tu mejor carta. Hoy te pienso y admiro cómo te exiges para ser mejor cada día. Que este mes te traiga mucha paz.",
    "02-05": "Sábado. Carolina, hoy te pienso y admiro esa capacidad que tienes para enfrentar el trabajo con una profesionalidad impecable. Eres una mujer todoterreno, capaz de cumplir con todo.",
    "03-05": "Domingo de tranquilidad. Carolina, tu paz interior se nota. Admiro cómo cuidas de tu espacio personal y cómo valoras a tu hija por sobre todo. Espero que hoy recargues muchas energías.",
    "04-05": "Lunes de metas. Carolina, tu capacidad de organización es digna de aplauso. Tienes una mente estratégica que sabe identificar oportunidades. Confío plenamente en tu talento.",
    "05-05": "Carolina, tu belleza cautiva, pero tu conversación es lo que realmente atrapa. Hoy te pienso y valoro tu elocuencia natural y tu preparación. Eres una mujer integral en todos los sentidos.",
    "06-05": "Hoy quiero resaltar tu valentía, Carolina. No cualquiera es tan honesta y transparente como tú. Tu sinceridad es un rasgo valioso y hoy te pienso con mucho respeto.",
    "07-05": "Jueves. Un recordatorio de lo mucho que vales, Carolina. Tu impacto en los demás es positivo y constante. Hoy te pienso y reconozco ese magnetismo personal que nace de tu seguridad.",
    "08-05": "¡Viernes! Carolina, que tu fin de semana empiece con la mejor energía. Hoy te pienso e admiro la pasión que le pones a cada proyecto. Eres una mujer simplemente excepcional.",
    "09-05": "Sábado. Hoy te pienso y celebro tu esfuerzo, Carolina. Ver tu compromiso con el trabajo y tu responsabilidad me hace admirarte aún más. Eres una mujer brillante.",
    "10-05": "Domingo. Carolina, la elegancia es ser recordada por la calidad humana, y tú lo eres. Hoy te pienso y reconozco lo increíble que eres como madre. Con mucho cariño y respeto.",
    "11-05": "Iniciando semana. Carolina, hoy te pienso y sé que tu potencial es un motor que no se detiene. Tienes una visión de futuro clara y ambiciosa. Sigue adelante con esa convicción.",
    "12-05": "Carolina, tu sonrisa es el reflejo de una mente que sabe encontrar belleza en lo cotidiano. Hoy te pienso y admiro tu resiliencia; eres una mujer que sabe levantarse con más fuerza.",
    "13-05": "Miércoles. Hoy elogio tu criterio, Carolina. Tienes una capacidad crítica fundamental para tomar buenas decisiones. Hoy te pienso y confío en tu gran sabiduría.",
    "14-05": "Jueves. Carolina, tu estilo es impecable, pero tu ética es lo que más admiro. Eres una persona íntegra y eso te da una autoridad moral inmensa ante los demás.",
    "15-05": "Viernes de logros. Carolina, termina esta semana con satisfacción. Hoy te pienso y reconozco que tu esfuerzo diario siempre rinde frutos. Tu inteligencia es tu mejor guía.",
    "16-05": "Sábado. Carolina, hoy te pienso y reconozco que tu capacidad de trabajo es admirable. Eres una mujer que no se rinde y que enfrenta cada reto con la frente en alto.",
    "17-05": "Domingo de paz. Carolina, hoy te pienso y espero que la tranquilidad te acompañe en cada momento. Admiro tu capacidad de estar en armonía contigo misma.",
    "18-05": "Lunes. Vamos por una semana de éxitos, Carolina. Hoy te pienso y te recuerdo que tu inteligencia es tu mayor activo. Tienes la combinación perfecta de cerebro y corazón.",
    "19-05": "Carolina, hoy cerramos este primer ciclo de 30 días pensando en ti. Espero que te sientas muy valorada, porque tu esencia te hace única. Jhon te admira profundamente."
}

# 6. RENDERIZADO
llave = hoy.strftime("%d-%m")
mensaje_hoy = mensajes.get(llave, "Carolina, eres una mujer excepcional.")

st.markdown(f"""
    <div class="contenedor-carta">
        <div class="titulo">Para Carolina ✨</div>
        <div class="fecha-tag">{fecha_visual.upper()}</div>
        <div class="texto-cuerpo">"{mensaje_hoy}"</div>
        <div class="firma-jhon">Con cariño,<br>Jhon</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button(f"💖 Confirmar lectura"):
        st.balloons()
