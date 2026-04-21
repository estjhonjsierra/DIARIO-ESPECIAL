import streamlit as st
import datetime
import base64

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Mi Diario Especial", page_icon="🌸", layout="wide")

# 2. RELOJ COLOMBIA (UTC-5)
ahora_utc = datetime.datetime.utcnow()
hoy = ahora_utc + datetime.timedelta(hours=-5)

dias_es = {"Monday": "Lunes", "Tuesday": "Martes", "Wednesday": "Miércoles", "Thursday": "Jueves", "Friday": "Viernes", "Saturday": "Sábado", "Sunday": "Domingo"}
meses_es = {"April": "Abril", "May": "Mayo", "June": "Junio", "July": "Julio", "August": "Agosto", "September": "Septiembre", "October": "Octubre", "November": "Noviembre", "December": "Diciembre"}
fecha_hoy = f"{dias_es.get(hoy.strftime('%A'))}, {hoy.day} de {meses_es.get(hoy.strftime('%B'))}"

# 3. FUNCIÓN PARA IMAGEN
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        return base64.b64encode(f.read()).decode()

try:
    bin_str = get_base64('fondo_carolina.jpg.png')
    foto_html = f"data:image/png;base64,{bin_str}"
except:
    foto_html = ""

# 4. DISEÑO CSS PROFESIONAL (RESPONSIVE INVERTIDO)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Quicksand:wght@400;700&display=swap');
    
    /* Fondo con movimiento suave de colores */
    .stApp {{
        background: linear-gradient(-45deg, #fce4ec, #f3e5f5, #e1f5fe, #fff9c4);
        background-size: 400% 400%;
        animation: animarFondo 15s ease infinite;
    }}

    @keyframes animarFondo {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    .titulo-principal {{
        font-family: 'Dancing Script', cursive;
        color: #d81b60;
        font-size: 55px;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }}

    /* Contenedor Triple Columna en PC, Invertido en Móvil */
    .contenedor-app {{
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        gap: 20px;
        max-width: 1200px;
        margin: 0 auto;
    }}

    @media (max-width: 768px) {{
        .contenedor-app {{
            flex-direction: column; /* Alineación vertical */
        }}
        .seccion-mensaje {{ order: 1; }} /* Mensaje arriba */
        .seccion-foto {{ order: 2; }}    /* Foto debajo del mensaje */
        .seccion-boton {{ order: 3; }}   /* Botón al final */
        .titulo-principal {{ font-size: 40px; }}
    }}

    .seccion-foto {{
        flex: 1;
        max-width: 380px;
        min-width: 300px;
        border-radius: 30px;
        border: 6px solid white;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        overflow: hidden;
        animation: flotar 4s ease-in-out infinite;
    }}

    @keyframes flotar {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-15px); }}
    }}

    .seccion-mensaje {{
        flex: 1.5;
        background: rgba(255, 255, 255, 0.95);
        padding: 35px;
        border-radius: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        min-width: 320px;
        border: 2px solid #fce4ec;
    }}

    .seccion-boton {{
        flex: 0.5;
        min-width: 150px;
        text-align: center;
    }}

    .titulo-carta {{ font-family: 'Dancing Script', cursive; color: #d81b60; font-size: 45px; margin: 0; }}
    .fecha-tag {{ background: #d81b60; color: white; font-family: 'Quicksand', sans-serif; padding: 5px 15px; border-radius: 20px; font-size: 14px; display: inline-block; margin-bottom: 20px; }}
    .texto-cuerpo {{ font-family: 'Quicksand', sans-serif; font-size: 19px; color: #444; line-height: 1.6; }}
    .firma {{ font-family: 'Dancing Script', cursive; color: #d81b60; font-size: 32px; text-align: right; margin-top: 20px; }}

    /* Botón circular elegante */
    div.stButton > button {{
        background-color: #d81b60 !important;
        color: white !important;
        border-radius: 50% !important;
        width: 130px !important;
        height: 130px !important;
        border: 5px solid white !important;
        font-weight: bold !important;
        box-shadow: 0 10px 20px rgba(216, 27, 96, 0.4) !important;
        transition: 0.4s;
    }}
    div.stButton > button:hover {{ transform: scale(1.1); background-color: #ad1457 !important; }}

    header, footer {{ visibility: hidden; }}
    </style>
    """, unsafe_allow_html=True)

# 5. LOS 30 MENSAJES (LISTA COMPLETA)
mensajes_diarios = {
    "20-04": "Carolina, hoy te pienso y quiero decirte que iniciamos este diario para reconocer la gran mujer que eres. Tu elegancia y tu inteligencia son admirables, pero ver cómo te esfuerzas cada día por el bienestar de tu hija me demuestra la nobleza de tu corazón. Eres una madre ejemplar.",
    "21-04": "Hay una sofisticación única en ti, Carolina. Me impresiona cómo logras equilibrar tu vida con tanta madurez. Tu hija tiene el mejor ejemplo de lo que significa ser una mujer valiente y decidida.",
    "22-04": "Mitad de semana, Carolina. Tienes una fortaleza interna que te permite enfrentar los retos con calma. Admiro tu tenacidad y el amor infinito que le entregas a tu pequeña; esa dedicación te hace especial.",
    "23-04": "Tu mirada proyecta una sabiduría que va más allá de las palabras. Tienes un estilo propio y una autenticidad que te hace destacar. Hoy te pienso y reconozco el valor de tu esfuerzo diario.",
    "24-04": "¡Viernes! Tu energía transforma cualquier ambiente. Tienes un carisma genuino que se complementa con tu madurez. Eres de esas personas que dejan huella simplemente por ser consistentes.",
    "25-04": "Sábado. Hoy resalto tu disciplina admirable, Carolina. Mientras muchos descansan, tú sigues adelante con tus responsabilidades. Tu hija tiene en ti el mejor ejemplo de constancia.",
    "26-04": "La verdadera distinción está en tu trato y en la profundidad de tus pensamientos. Admiro tu criterio y cómo defiendes tus valores. Eres una mujer de gran corazón.",
    "27-04": "Nueva semana. Tu potencial es inmenso y tu capacidad de aprendizaje es algo que siempre destaca. Tienes una mente curiosa que te llevará muy lejos. Eres motor de sueños.",
    "28-04": "Tu presencia es sinónimo de equilibrio. La forma en la que gestionas tus responsabilidades dice mucho de ti. Tu belleza es innegable, pero tu carácter te hace invencible.",
    "29-04": "Brillas por tu intelecto y tu bondad. Eres una mujer con mucha sustancia. Tu hija es muy afortunada de tenerte como guía y apoyo incondicional.",
    "30-04": "Cerrando abril. Eres una inspiración constante de superación. Has demostrado que se puede ser firme y dulce al mismo tiempo. Gracias por permitirme admirarte.",
    "01-05": "¡Bienvenido mayo! Tu determinación es tu mejor carta. Admiro cómo te exiges para ser mejor cada día. Que este mes te traiga la paz que tanto mereces.",
    "02-05": "Sábado. Admiro esa capacidad que tienes para enfrentar el trabajo con una profesionalidad impecable. Eres una mujer todoterreno, capaz de cumplir cualquier meta.",
    "03-05": "Domingo de paz. Tu tranquilidad se nota y se contagia. Admiro cómo cuidas de tu espacio personal y cómo valoras a tu familia por sobre todo.",
    "04-05": "Lunes de metas. Tu capacidad de organización es digna de aplauso. Tienes una mente estratégica que sabe identificar oportunidades donde otros no ven nada.",
    "05-05": "Tu belleza cautiva, pero tu conversación es lo que realmente atrapa. Eres una mujer integral: inteligente, preparada y con un corazón enorme.",
    "06-05": "Resalto tu valentía, Carolina. No cualquiera es tan honesta y transparente como tú. Tu sinceridad es un rasgo valioso que hoy reconozco con mucho respeto.",
    "07-05": "Un recordatorio de lo mucho que vales. Tu impacto en los demás es siempre positivo. Tu magnetismo personal nace de la seguridad que proyectas.",
    "08-05": "¡Viernes! Admiro la pasión que le pones a cada proyecto. Eres una mujer que no se rinde y que inspira a los que tenemos la suerte de conocerte.",
    "09-05": "Sábado. Tu compromiso con el trabajo y tu responsabilidad me hacen admirarte más. Eres brillante y constante, una combinación ganadora.",
    "10-05": "La elegancia es ser recordada por la calidad humana, y tú lo eres. Hoy reconozco lo increíble que eres como madre y como mujer.",
    "11-05": "Nueva semana. Tu potencial no tiene límites. Tienes una visión de futuro clara y ambiciosa. Sigue adelante con esa convicción que te caracteriza.",
    "12-05": "Tu sonrisa refleja una mente que encuentra belleza en lo cotidiano. Admiro tu resiliencia; eres una mujer que sabe levantarse con más fuerza siempre.",
    "13-05": "Elogio tu criterio hoy. Tienes una capacidad crítica fundamental para tomar buenas decisiones. Confío plenamente en tu gran sabiduría.",
    "14-05": "Tu estilo es impecable, pero tu ética es lo que más admiro. Eres una persona íntegra y eso te da una autoridad moral inmensa.",
    "15-05": "Viernes de satisfacción. Tu esfuerzo diario siempre rinde frutos. Tu inteligencia es la mejor guía que podrías tener para tus sueños.",
    "16-05": "Tu capacidad de trabajo es admirable. Eres una mujer que enfrenta cada reto con la frente en alto, sin miedo al éxito.",
    "17-05": "Domingo. Que la tranquilidad te acompañe hoy. Admiro tu capacidad de estar en armonía contigo misma, es algo difícil de lograr.",
    "18-05": "Tu inteligencia es tu mayor activo. Tienes la combinación perfecta de cerebro y corazón. Gracias por ser esa mujer tan increíble.",
    "19-05": "Cerramos este primer ciclo de 30 días. Espero que te sientas muy valorada, porque tu esencia te hace única. Jhon te admira profundamente."
}

# 6. RENDERIZADO FINAL
st.markdown('<h1 class="titulo-principal">🌸 Mi Diario Especial para Carolina 🌸</h1>', unsafe_allow_html=True)

llave_hoy = hoy.strftime("%d-%m")
mensaje_de_hoy = mensajes_diarios.get(llave_hoy, "Carolina, eres una mujer excepcional. Que tengas un día maravilloso.")

# Layout principal
st.markdown('<div class="contenedor-app">', unsafe_allow_html=True)

# SECCIÓN MENSAJE (Orden 1 en móvil)
st.markdown(f"""
    <div class="seccion-mensaje">
        <div class="titulo-carta">Para Carolina ✨</div>
        <div class="fecha-tag">{fecha_hoy.upper()}</div>
        <div class="texto-cuerpo">"{mensaje_de_hoy}"</div>
        <div class="firma">Con mucho cariño, Jhon</div>
    </div>
""", unsafe_allow_html=True)

# SECCIÓN FOTO (Orden 2 en móvil)
st.markdown(f'<div class="seccion-foto"><img src="{foto_html}" style="width:100%;"></div>', unsafe_allow_html=True)

# SECCIÓN BOTÓN (Orden 3 en móvil)
with st.container():
    st.markdown('<div class="seccion-boton">', unsafe_allow_html=True)
    if st.button("💖\nConfirmar\nLectura"):
        st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
