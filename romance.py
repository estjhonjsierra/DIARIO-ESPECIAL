import streamlit as st
import datetime

# 1. Configuración de la página
st.set_page_config(page_title="Para Carolina", page_icon="💖", layout="centered")

# 2. Corrección de Hora para Colombia (UTC-5)
ahora_utc = datetime.datetime.utcnow()
bogota_offset = datetime.timedelta(hours=-5)
hoy = ahora_utc + bogota_offset

# Traducción de fechas
dias_semana = {
    "Monday": "Lunes", "Tuesday": "Martes", "Wednesday": "Miércoles", 
    "Thursday": "Jueves", "Friday": "Viernes", "Saturday": "Sábado", "Sunday": "Domingo"
}
meses_anio = {
    "April": "Abril", "May": "Mayo", "June": "Junio", "July": "Julio",
    "August": "Agosto", "September": "Septiembre", "October": "Octubre",
    "November": "Noviembre", "December": "Diciembre"
}

dia_nombre = dias_semana.get(hoy.strftime('%A'))
mes_nombre = meses_anio.get(hoy.strftime('%B'))
fecha_visual = f"{dia_nombre}, {hoy.day} de {mes_nombre}"

# 3. Diseño Visual Premium con Sorpresas
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Quicksand:wght@400;700&display=swap');
    
    /* Fondo con degradado animado */
    .stApp {{
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }}

    @keyframes gradient {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    /* Contenedor de la carta con efecto de brillo */
    .contenedor-carta {{
        background: rgba(255, 255, 255, 0.92);
        padding: 50px;
        border-radius: 30px;
        border: 4px solid #ffffff;
        box-shadow: 0px 15px 35px rgba(0,0,0,0.2);
        margin-top: 20px;
        position: relative;
        overflow: hidden;
    }}

    .contenedor-carta::before {{
        content: "";
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, transparent 70%);
        animation: rotate 10s linear infinite;
    }}

    @keyframes rotate {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
    }}
    
    .titulo-principal {{
        font-family: 'Dancing Script', cursive;
        color: #d81b60;
        font-size: 60px;
        text-align: center;
        margin-bottom: 5px;
        position: relative;
    }}

    .fecha-badge {{
        background: #d81b60;
        color: white;
        font-family: 'Quicksand', sans-serif;
        font-weight: bold;
        text-align: center;
        padding: 10px 30px;
        border-radius: 50px;
        display: block;
        margin: 0 auto 30px auto;
        width: fit-content;
        font-size: 18px;
        position: relative;
    }}
    
    .texto-mensaje {{ 
        font-size: 24px; 
        color: #2d3436; 
        line-height: 1.6; 
        font-family: 'Quicksand', sans-serif; 
        text-align: center;
        position: relative;
        font-weight: 500;
    }}
    
    .firma-jhon {{ 
        margin-top: 40px; 
        text-align: right; 
        color: #d81b60; 
        font-family: 'Dancing Script', cursive;
        font-size: 45px; 
        position: relative;
    }}
    </style>
    """, unsafe_allow_html=True)

# 4. Diccionario de Mensajes (20 Abril - 19 Mayo)
mensajes_diarios = {
    "20-04": "Carolina, hoy te pienso y quiero decirte que iniciamos este diario para reconocer la gran mujer que eres. Tu elegancia y tu inteligencia son admirables, pero ver cómo te esfuerzas cada día también por el bienestar de tu hija me demuestra la nobleza de tu corazón. Eres una madre ejemplar y una mujer excepcional. Que este lunes sea brillante para ti.",
    "21-04": "Hay una sofisticación única en ti, Carolina. Me impresiona cómo logras equilibrar tu vida con tanta madurez. Hoy te pienso y celebro esa fuerza que tienes para salir adelante; tu hija tiene el mejor ejemplo de lo que significa ser una mujer valiente y decidida. Tienes una luz propia que ilumina cualquier lugar donde estés.",
    "22-04": "Mitad de semana, Carolina. Es el momento perfecto para resaltar tu resiliencia. Tienes una fortaleza interna que te permite enfrentar los retos con calma. Admiro tu tenacidad y el amor infinito que le entregas a tu hija; esa dedicación es parte de lo que te hace tan especial. Eres una mujer de pies a cabeza.",
    "23-04": "Carolina, tu mirada proyecta una sabiduría que va mucho más allá de las palabras. Tienes un estilo propio y una autenticidad que te hace destacar. Hoy te pienso y reconozco el valor de tu esfuerzo diario por construir un futuro hermoso para ti y para tu hija.",
    "24-04": "¡Viernes! Un día para reconocer que tu energía transforma cualquier ambiente. Tienes un carisma genuino que se complementa con tu madurez. Eres de esas personas que dejan huella simplemente por ser consistentes. Hoy te pienso y te deseo un cierre de semana laboral excelente.",
    "25-04": "Sábado. Hoy te pienso y quiero resaltar esa disciplina admirable que tienes, Carolina. Mientras muchos descansan, tú sigues adelante con tus responsabilidades, demostrando la mujer trabajadora que eres. Tu hija tiene en ti el mejor ejemplo de constancia.",
    "26-04": "Domingo de reflexión. La verdadera distinción, Carolina, está en tu trato y en la profundidad de tus pensamientos. Admiro tu criterio y cómo defiendes tus valores. Hoy te pienso y valoro enormemente el hogar lleno de valores que estás formando para tu hija.",
    "27-04": "Nueva semana, Carolina. Tu potencial es inmenso y tu capacidad de aprendizaje es algo que siempre destaca. Tienes una mente curiosa que te llevará muy lejos. Hoy te pienso y te recuerdo que eres el motor que impulsa los sueños de tu hija.",
    "28-04": "Carolina, tu presencia es sinónimo de equilibrio. Hoy te pienso y elogio tu madurez; la forma en la que gestionas tus responsabilidades dice mucho de ti. Tu belleza es innegable, pero tu carácter y la protección que le das a tu hija es lo que te hace invencible.",
    "29-04": "Hay personas que brillan por fuera, pero tú brillas por tu intelecto y tu bondad. Hoy te pienso y me doy cuenta de que eres una mujer con mucha sustancia. Tu hija es muy afortunada de tenerte como guía.",
    "30-04": "Cerrando abril con éxito. Carolina, hoy te pienso y te agradezco por ser una inspiración constante de superación. Has demostrado que se puede ser firme y dulce al mismo tiempo. Eres una líder en tu propio camino y el pilar fundamental para tu hija.",
    "01-05": "¡Bienvenido mayo! Un nuevo mes para verte brillar. Carolina, tu determinación es tu mejor carta. Hoy te pienso y admiro cómo te exiges para ser mejor cada día, no solo por ti, sino por el futuro de tu hija. Que este mes te traiga paz.",
    "02-05": "Sábado. Carolina, hoy te pienso y admiro esa capacidad que tienes para enfrentar el trabajo con una profesionalidad impecable. Eres una mujer todoterreno, capaz de cumplir con tus metas laborales sin descuidar el amor por tu hija.",
    "03-05": "Domingo de tranquilidad. Carolina, tu paz interior se nota a kilómetros. Admiro cómo cuidas de tu espacio personal y cómo valoras a tu hija por sobre todo. Hoy te pienso y espero que recargues energías.",
    "04-05": "Lunes de metas. Carolina, tu capacidad de organización es digna de aplauso. Tienes una mente estratégica que sabe identificar oportunidades. Hoy te pienso y confío en tu talento; eres el ejemplo de superación que tu hija seguirá.",
    "05-05": "Carolina, tu belleza cautiva, pero tu conversación es lo que realmente atrapa. Hoy te pienso y valoro tu elocuencia natural y tu preparación. Eres una mujer integral y tu hija crecerá admirando cada uno de tus pasos.",
    "06-05": "Hoy quiero resaltar tu valentía, Carolina. No cualquiera es tan honesta y transparente como tú. Tu sinceridad es un rasgo valioso y hoy te pienso con mucho respeto. Tu hija tiene en ti a una mujer de principios claros.",
    "07-05": "Jueves. Un recordatorio de lo mucho que vales, Carolina. Tu impacto en los demás es positivo y constante. Hoy te pienso y reconozco ese magnetismo personal que nace de tu seguridad. Eres la roca de tu hija.",
    "08-05": "¡Viernes! Carolina, que tu fin de semana empiece con la mejor energía. Hoy te pienso y admiro la pasión que le pones a cada proyecto, especialmente a la crianza de tu hija. Eres una mujer excepcional.",
    "09-05": "Sábado. Hoy te pienso y celebro tu esfuerzo, Carolina. Ver tu compromiso con el trabajo y tu responsabilidad me hace admirarte aún más. Eres una mujer brillante que sabe que el esfuerzo de hoy es la tranquilidad de su hija.",
    "10-05": "Domingo. Carolina, la elegancia es ser recordada por la calidad humana, y tú lo eres. Hoy te pienso y reconozco lo increíble que eres como madre; tu hija es el reflejo de tu dedicación. Con mucho cariño y respeto.",
    "11-05": "Iniciando semana. Carolina, hoy te pienso y sé que tu potencial es un motor que no se detiene. Tienes una visión de futuro clara para ti y para tu hija. Sigue adelante con esa convicción.",
    "12-05": "Carolina, tu sonrisa es el reflejo de una mente que sabe encontrar belleza en lo cotidiano. Hoy te pienso y admiro tu resiliencia; eres una mujer que sabe levantarse con más fuerza por el amor que le tiene a su hija.",
    "13-05": "Miércoles. Hoy elogio tu criterio, Carolina. Tienes una capacidad crítica fundamental para tomar buenas decisiones. Hoy te pienso y confío en tu sabiduría; tu hija está en las mejores manos posibles.",
    "14-05": "Jueves. Carolina, tu estilo es impecable, pero tu ética es lo que más admiro. Eres una persona íntegra y eso te da una autoridad moral inmensa. Esa integridad es el legado más valioso que le dejas a tu hija.",
    "15-05": "Viernes de logros. Carolina, termina esta semana con satisfacción. Hoy te pienso y reconozco que tu esfuerzo diario rinde frutos. Tu inteligencia es tu mejor guía y tu amor por tu hija es tu combustible.",
    "16-05": "Sábado laboral. Carolina, hoy te pienso y reconozco que tu capacidad de trabajo es admirable. Eres una mujer que no se rinde y que enfrenta cada sábado con la frente en alto. Tu hija tiene mucha suerte.",
    "17-05": "Domingo de paz. Carolina, hoy te pienso y espero que la tranquilidad te acompañe. Jhon admira tu capacidad de estar en armonía contigo misma y con tu pequeña. Que este día sea para disfrutar.",
    "18-05": "Lunes. Vamos por una semana de éxitos, Carolina. Hoy te pienso y te recuerdo que tu inteligencia es tu mayor activo. Tienes la combinación perfecta de cerebro y corazón, lo que te hace una madre y mujer imparable.",
    "19-05": "Carolina, hoy cerramos este ciclo de 30 días pensando en ti. Espero que te sientas valorada, porque tu esencia y la dedicación que le pones a tu hija te hacen única. Jhon te tiene en un concepto de admiración total."
}

# 5. Lógica de selección del mensaje
llave_hoy = hoy.strftime("%d-%m")
contenido_final = mensajes_diarios.get(llave_hoy, f"Carolina, hoy {fecha_visual} te pienso y te recuerdo lo especial que eres.")

# 6. Renderizado de la App
st.markdown(f"""
    <div class="contenedor-carta">
        <div class="titulo-principal">Para Carolina</div>
        <div class="fecha-badge">{fecha_visual.upper()}</div>
        <div class="texto-mensaje">
            "{contenido_final}"
        </div>
        <div class="firma-jhon">Con mucho cariño, Jhon ✨</div>
    </div>
    """, unsafe_allow_html=True)

# 7. Botón de Interacción con Efectos
st.write("")
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button(f"💖 Confirmar lectura del {dia_nombre}"):
        st.balloons()
        st.snow()  # Efecto extra visual
        st.toast(f"¡Que tengas un día maravilloso, Carolina!", icon='✨')

st.markdown("<p style='text-align: center; color: white; font-size: 14px; margin-top: 50px; font-weight: bold;'>Cada día un mensaje nuevo para ti.</p>", unsafe_allow_html=True)
