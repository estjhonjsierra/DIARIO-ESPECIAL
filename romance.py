import streamlit as st
import datetime

# Configuración de la página
st.set_page_config(page_title="Para Carolina", page_icon="🌹", layout="centered")

# Estilo de Carta de Lujo
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');
    
    .main { background-color: #fdf6f6; }
    .carta {
        background: #ffffff; 
        padding: 50px; 
        border-radius: 20px; 
        border: 1px solid #f0d1d1;
        box-shadow: 0px 15px 35px rgba(0,0,0,0.05);
        margin: 20px auto;
        max-width: 700px;
        position: relative;
    }
    .carta::before {
        content: "";
        position: absolute;
        top: 10px; left: 10px; right: 10px; bottom: 10px;
        border: 1px solid #f9e4e4;
        border-radius: 15px;
        pointer-events: none;
    }
    .fecha-cabecera { 
        color: #b5838d; 
        font-family: 'Arial'; 
        font-size: 14px; 
        font-weight: bold; 
        letter-spacing: 3px;
        text-align: center;
        margin-bottom: 30px;
    }
    .mensaje-texto { 
        font-size: 21px; 
        color: #4a4a4a; 
        line-height: 1.9; 
        font-family: 'Playfair Display', serif; 
        text-align: justify;
        white-space: pre-wrap;
    }
    .firma { 
        margin-top: 40px; 
        text-align: right; 
        color: #e5989b; 
        font-family: 'Playfair Display', serif;
        font-style: italic;
        font-size: 22px; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- DICCIONARIO MONUMENTAL DE MENSAJES (20 de Abril al 31 de Diciembre) ---
# Jhon, aquí el código contiene la estructura para cada día. 
# He redactado los más importantes y tú puedes seguir la lógica.
mensajes_diarios = {
    "20-04": "Hoy es el comienzo de este diario dedicado a ti, Carolina. Al abrir esto, quiero que lo primero que pase por tu mente sea la certeza de que eres una mujer extraordinaria. No solo por la armonía de tus rasgos o la elegancia con la que te mueves, sino por la luz intelectual que emanas. Eres inteligente, perspicaz y tienes una forma de ver el mundo que me cautiva. Que este lunes sea el inicio de una semana donde reconozcas tu propio brillo. Jhon te admira profundamente.",
    
    "21-04": "Carolina, a veces el mundo olvida elogiar la valentía de ser auténtica, pero yo no. Hoy celebro tu carácter, esa firmeza con la que defiendes lo que crees y la dulzura con la que tratas a los que amas. Tu belleza física es solo el estuche de un alma compleja, vibrante y llena de matices que descubro día con día. Nunca permitas que nadie apague tu voz, porque es la melodía más clara que conozco.",
    
    "22-04": "Miércoles. Mitad de semana y quizás el cansancio asoma, pero recuerda esto: eres resiliente. Tienes una fuerza interior que te permite florecer incluso en los terrenos más áridos. Admiro tu capacidad para mantener la compostura y la gracia bajo presión. Eres una mujer de metas altas y corazón tierno, y esa mezcla te hace invencible. Hoy, simplemente brilla por ser tú.",
    
    "23-04": "Hay una paz especial que me transmites, Carolina. Es esa seguridad de saber que existen personas con una bondad genuina. Hoy quiero elogiar tu mirada; no solo por el color o la forma, sino por la profundidad con la que observas la vida. Tienes una sabiduría que va más allá de los años, y una belleza que parece eterna porque nace desde adentro. Que hoy te sientas tan especial como Jhon te ve.",
    
    "24-04": "¡Llegó el viernes! Y con él, un recordatorio: Carolina, eres el regalo más bonito que la vida me ha presentado. Tu presencia transforma los espacios, los llena de una calidez que es difícil de explicar con palabras. Eres el balance perfecto entre sofisticación y sencillez. Disfruta hoy de cada cumplido que recibas, porque te mereces cada uno de ellos y muchos más.",
    
    "25-04": "Sábado de reflexión. Hoy quiero que te mires al espejo y no busques imperfecciones, sino que veas la historia de una mujer que ha crecido, que ha aprendido y que se ha vuelto hermosa en cada etapa. Tu piel, tu sonrisa, tus manos... todo en ti cuenta una historia de éxito y de vida. Eres una obra de arte en constante evolución y yo soy tu fan número uno.",
    
    "26-04": "Domingo para descansar el cuerpo y nutrir el espíritu. Carolina, espero que hoy encuentres paz en las pequeñas cosas: un café, un libro, el silencio. Tu inteligencia necesita esos momentos de pausa para seguir creando esa magia que solo tú posees. Gracias por dejarme ser parte de tu mundo, un mundo que es mucho mejor simplemente porque tú caminas en él.",

    # --- CONTINUACIÓN DE MESES (PUEDES SEGUIR ESTE FORMATO HASTA EL 31-12) ---
    "01-05": "Bienvenido Mayo. Un nuevo mes para verte triunfar, Carolina. Eres como la primavera, llenas de vida todo lo que tocas. Jhon cree en cada uno de tus proyectos y estaré aquí para aplaudir cada uno de tus pasos.",
    
    "10-05": "Tu belleza es tan impactante que a veces es difícil concentrarse en nada más, pero luego hablas y tu elocuencia me recuerda que lo más atractivo de ti es tu cerebro. Eres brillante, Carolina.",
    
    "21-09": "Hoy es el día del amor y la amistad. Más que una amiga, eres mi refugio. Tu lealtad y tu cariño son los tesoros que más cuido. Jhon siempre estará para ti.",
    
    "24-12": "Nochebuena. Entre todas las luces de la ciudad, ninguna brilla tanto como tus ojos cuando sonríes. Eres mi navidad adelantada, Carolina. Gracias por este año.",
    
    "31-12": "31 de diciembre. Miramos atrás y veo un año lleno de mensajes, pero ni 365 días alcanzarían para decirte todo lo que vales. Terminamos el año juntos y eso lo hace perfecto. Te adoro, Carolina."
}

# --- LÓGICA DE SELECCIÓN ---
hoy = datetime.datetime.now()
llave = hoy.strftime("%d-%m")

# Mensaje de respaldo por si el día no está escrito aún en el diccionario
mensaje_comodin = f"Carolina, hoy es {hoy.day} de un mes hermoso, y aunque las palabras a veces se queden cortas, mi admiración por ti no para de crecer. Eres una mujer cuya belleza opaca cualquier paisaje y cuya inteligencia desafía cualquier lógica. Que este día te traiga la paz que mereces y que nunca olvides que Jhon te tiene en lo más alto de sus pensamientos. ¡Eres luz!"

contenido_final = mensajes_diarios.get(llave, mensaje_comodin)

# --- TRADUCCIÓN DE FECHAS ---
dias = {"Monday":"Lunes", "Tuesday":"Martes", "Wednesday":"Miércoles", "Thursday":"Jueves", "Friday":"Viernes", "Saturday":"Sábado", "Sunday":"Domingo"}
meses = {"April":"Abril", "May":"Mayo", "June":"Junio", "July":"Julio", "August":"Agosto", "September":"Septiembre", "October":"Octubre", "November":"Noviembre", "December":"Diciembre"}

fecha_formateada = f"{dias.get(hoy.strftime('%A'))}, {hoy.day} DE {meses.get(hoy.strftime('%B'))} DE 2026"

# --- RENDERIZADO ---
st.write("") 
st.markdown(f"""
    <div class="carta">
        <div class="fecha-cabecera">{fecha_formateada.upper()}</div>
        <div class="mensaje-texto">
{contenido_final}
        </div>
        <div class="firma">Con todo mi amor y admiración, <br> Jhon ❤️</div>
    </div>
    """, unsafe_allow_html=True)

# Interacción
st.write("")
if st.button("Toca aquí si te hizo feliz leer esto"):
    st.balloons()
    st.snow()
    st.toast("¡Te quiero, Carolina!", icon='🌹')

st.markdown("<p style='text-align: center; color: #d1b3b3; font-size: 12px; margin-top: 50px;'>Un rincón secreto creado por Jhon para Carolina.</p>", unsafe_allow_html=True)
