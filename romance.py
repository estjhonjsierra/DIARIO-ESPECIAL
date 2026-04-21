import streamlit as st
import datetime

# Configuración de la página
st.set_page_config(page_title="Para Carolina", page_icon="💖", layout="centered")

# --- LÓGICA DE FECHA EXACTA ---
hoy = datetime.datetime.now()
# Forzamos la zona horaria o el ajuste si el servidor marca otro día
# Pero con esta lógica estándar debería marcar Lunes 20 de Abril correctamente
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

# --- DISEÑO COLORIDO Y DINÁMICO ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Quicksand:wght@400;700&display=swap');
    
    .stApp {{
        background: linear-gradient(135deg, #6dd5ed 0%, #2193b0 100%);
    }}
    
    .contenedor-carta {{
        background: white;
        padding: 40px;
        border-radius: 30px;
        border: 4px solid #ffd700;
        box-shadow: 0px 20px 40px rgba(0,0,0,0.2);
        margin-top: 30px;
        position: relative;
        overflow: hidden;
    }}

    .decoracion {{
        position: absolute;
        top: -10px;
        right: -10px;
        font-size: 50px;
        opacity: 0.2;
    }}
    
    .titulo-principal {{
        font-family: 'Dancing Script', cursive;
        color: #0077b6;
        font-size: 45px;
        text-align: center;
        margin-bottom: 10px;
    }}

    .fecha-badge {{
        background: #ffd700;
        color: #003049;
        font-family: 'Quicksand', sans-serif;
        font-weight: bold;
        text-align: center;
        padding: 5px 20px;
        border-radius: 50px;
        width: fit-content;
        margin: 0 auto 25px auto;
        font-size: 16px;
        letter-spacing: 1px;
    }}
    
    .texto-mensaje {{ 
        font-size: 20px; 
        color: #2c3e50; 
        line-height: 1.7; 
        font-family: 'Quicksand', sans-serif; 
        text-align: justify;
        padding: 10px;
    }}
    
    .firma-jhon {{ 
        margin-top: 30px; 
        text-align: right; 
        color: #0077b6; 
        font-family: 'Dancing Script', cursive;
        font-size: 32px; 
    }}
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS DE MENSAJES (20 ABR - 19 MAY) ---
mensajes_diarios = {
    "20-04": "Carolina, hoy te pienso y quiero decirte que iniciamos este diario para reconocer la gran mujer que eres. Tu elegancia y tu inteligencia son admirables, pero ver cómo te esfuerzas cada día también por el bienestar de tu hija me demuestra la nobleza de tu corazón. Eres una madre ejemplar y una mujer excepcional. Que este lunes sea brillante para ti.",
    "21-04": "Hay una sofisticación única en ti, Carolina. Me impresiona cómo logras equilibrar tu vida con tanta madurez. Hoy te pienso y celebro esa fuerza que tienes para salir adelante; tu hija tiene el mejor ejemplo de lo que significa ser una mujer valiente y decidida. Tienes una luz propia que ilumina cualquier lugar donde estés.",
    "22-04": "Mitad de semana, Carolina. Es el momento perfecto para resaltar tu resiliencia. Tienes una fortaleza interna que te permite enfrentar los retos con calma. Admiro tu tenacidad y el amor infinito que le entregas a tu hija; esa dedicación es parte de lo que te hace tan especial. Eres una mujer de pies a cabeza y hoy te pienso con mucho respeto.",
    "23-04": "Carolina, tu mirada proyecta una sabiduría que va mucho más allá de las palabras. Tienes un estilo propio y una autenticidad que te hace destacar por mérito propio. Hoy te pienso y reconozco el valor de tu esfuerzo diario por construir un futuro hermoso para ti y para tu hija. Sigue confiando en tu intuición, es tu mejor guía.",
    "24-04": "¡Viernes! Un día para reconocer que tu energía transforma cualquier ambiente. Tienes un carisma genuino que se complementa con tu madurez. Eres de esas personas que dejan huella simplemente por ser consistentes con lo que piensan. Hoy te pienso y te deseo un cierre de semana laboral excelente.",
    "25-04": "Sábado. Hoy te pienso y quiero resaltar esa disciplina admirable que tienes, Carolina. Mientras muchos descansan, tú sigues adelante con tus responsabilidades, demostrando la mujer trabajadora y enfocada que eres. Tu hija tiene en ti el mejor ejemplo de constancia. Que tu jornada sea productiva y exitosa.",
    "26-04": "Domingo de reflexión. La verdadera distinción, Carolina, está en tu trato y en la profundidad de tus pensamientos. Admiro tu criterio y cómo defiendes tus valores. Hoy te pienso y valoro enormemente el hogar lleno de valores que estás formando para tu hija. Eres una mujer fascinante y digna de toda mi admiración.",
    "27-04": "Nueva semana, Carolina. Tu potencial es inmenso y tu capacidad de aprendizaje es algo que siempre destaca. Tienes una mente curiosa que te llevará muy lejos. Hoy te pienso y te recuerdo que eres el motor que impulsa los sueños de tu hija; tu fuerza es el regalo más grande que ella tiene.",
    "28-04": "Carolina, tu presencia es sinónimo de equilibrio. Hoy te pienso y elogio tu madurez; la forma en la que gestionas tus responsabilidades dice mucho de ti. Tu belleza es innegable, pero tu carácter y la forma en que proteges y amas a tu hija es lo que realmente te hace una mujer invencible.",
    "29-04": "Hay personas que brillan por fuera, pero tú brillas por tu intelecto y tu bondad. Hoy te pienso y me doy cuenta de que eres una mujer con mucha sustancia. Tu hija es muy afortunada de tenerte como guía y madre. Nunca dejes de cultivar esa mente maravillosa que tienes.",
    "30-04": "Cerrando abril con éxito. Carolina, hoy te pienso y te agradezco por ser una inspiración constante de superación. Has demostrado que se puede ser firme y dulce al mismo tiempo. Eres una líder en tu propio camino y el pilar fundamental para tu hija.",
    "01-05": "¡Bienvenido mayo! Un nuevo mes para verte brillar. Carolina, tu determinación es tu mejor carta. Hoy te pienso y admiro cómo te exiges para ser mejor cada día, no solo por ti, sino por el futuro de tu hija. Que este mes te traiga los resultados y la paz que tanto mereces.",
    "02-05": "Sábado. Carolina, hoy te pienso y admiro esa capacidad que tienes para enfrentar el trabajo con una profesionalidad impecable. Eres una mujer todoterreno, capaz de cumplir con tus metas laborales sin descuidar el amor por tu hija. Tu dedicación es inspiradora y habla de tu gran calidad humana.",
    "03-05": "Domingo de tranquilidad. Carolina, tu paz interior se nota a kilómetros. Admiro cómo cuidas de tu espacio personal y cómo valoras a tu hija por sobre todo. Hoy te pienso y espero que recargues energías para seguir proyectando esa luz tan especial que tienes.",
    "04-05": "Lunes de metas. Carolina, tu capacidad de organización es digna de aplauso. Tienes una mente estratégica que sabe identificar oportunidades. Hoy te pienso y confío en tu talento; eres el ejemplo de superación que tu hija seguirá con orgullo.",
    "05-05": "Carolina, tu belleza cautiva, pero tu conversación es lo que realmente atrapa. Hoy te pienso y valoro tu elocuencia natural y tu preparación. Eres una mujer integral, capaz de destacar en cualquier ámbito, y tu hija crecerá admirando cada uno de tus pasos.",
    "06-05": "Hoy quiero resaltar tu valentía, Carolina. No cualquiera es tan honesta y transparente como tú. Tu sinceridad es un rasgo valioso y hoy te pienso con mucho respeto. Tu hija tiene en ti a una mujer de principios claros.",
    "07-05": "Jueves. Un recordatorio de lo mucho que vales, Carolina. Tu impacto en los demás es positivo y constante. Hoy te pienso y reconozco ese magnetismo personal que nace de tu seguridad. Eres la roca de tu hija y la inspiración de quienes te conocemos.",
    "08-05": "¡Viernes! Carolina, que tu fin de semana empiece con la mejor energía. Hoy te pienso y admiro la pasión que le pones a cada proyecto, especialmente a la crianza de tu hija. Eres una mujer excepcional con una fuerza vital que contagia optimismo.",
    "09-05": "Sábado. Hoy te pienso y celebro tu esfuerzo, Carolina. Ver tu compromiso con el trabajo y tu responsabilidad me hace admirarte aún más. No todos tienen esa garra para mantenerse firmes. Eres una mujer brillante que sabe que el esfuerzo de hoy es la tranquilidad de su hija mañana.",
    "10-05": "Domingo. Carolina, la elegancia es ser recordada por la calidad humana, y tú lo eres. Tu distinción nace de tu educación. Hoy te pienso y reconozco lo increíble que eres como madre; tu hija es el reflejo de tu dedicación. Con mucho cariño y respeto.",
    "11-05": "Iniciando semana. Carolina, hoy te pienso y sé que tu potencial es un motor que no se detiene. Tienes una visión de futuro clara para ti y para tu hija. Sigue adelante con esa convicción; tienes la inteligencia necesaria para lograr lo que te propongas.",
    "12-05": "Carolina, tu sonrisa es el reflejo de una mente que sabe encontrar belleza en lo cotidiano. Hoy te pienso y admiro tu resiliencia; eres una mujer que sabe levantarse con más fuerza por el amor que le tiene a su hija.",
    "13-05": "Miércoles. Hoy elogio tu criterio, Carolina. Tienes una capacidad crítica fundamental para tomar buenas decisiones. Hoy te pienso y confío en tu sabiduría; tu hija está en las mejores manos posibles porque tú eres una mujer brillante.",
    "14-05": "Jueves. Carolina, tu estilo es impecable, pero tu ética es lo que más admiro. Eres una persona íntegra y eso te da una autoridad moral inmensa. Hoy te pienso y te recuerdo que esa integridad es el legado más valioso que le dejas a tu hija.",
    "15-05": "Viernes de logros. Carolina, termina esta semana con satisfacción. Hoy te pienso y reconozco que tu esfuerzo diario rinde frutos. Tu inteligencia es tu mejor guía y tu amor por tu hija es tu combustible.",
    "16-05": "Sábado laboral. Carolina, hoy te pienso y reconozco que tu capacidad de trabajo es admirable. Eres una mujer que no se rinde y que enfrenta cada sábado con la frente en alto. Tu hija tiene mucha suerte de tener un ejemplo como el tuyo.",
    "17-05": "Domingo de paz. Carolina, hoy te pienso y espero que la tranquilidad te acompañe. Jhon admira tu capacidad de estar en armonía contigo misma y con tu pequeña. Que este día sea para disfrutar lo verdaderamente importante.",
    "18-05": "Lunes. Vamos por una semana de éxitos, Carolina. Hoy te pienso y te recuerdo que tu inteligencia es tu mayor activo. Tienes la combinación perfecta de cerebro y corazón, lo que te hace la mejor madre y una mujer imparable.",
    "19-05": "Carolina, hoy cerramos este ciclo de 30 días pensando en ti. Espero que te sientas valorada, porque tu esencia, tu mente y la dedicación que le pones a tu hija te hacen única. Jhon te tiene en un concepto de admiración total."
}

# Obtención del mensaje
llave = hoy.strftime("%d-%m")
contenido_final = mensajes_diarios.get(llave, f"Carolina, hoy {fecha_visual} te pienso y te recuerdo que eres una mujer increíble. ¡Ten un día maravilloso!")

# --- RENDERIZADO ---
st.markdown(f"""
    <div class="contenedor-carta">
        <div class="decoracion">✨</div>
        <div class="titulo-principal">Para Carolina</div>
        <div class="fecha-badge">{fecha_visual.upper()}</div>
        <div class="texto-mensaje">
            {contenido_final}
        </div>
        <div class="firma-jhon">Con mucho cariño y respeto, Jhon</div>
    </div>
    """, unsafe_allow_html=True)

# --- BOTÓN DE INTERACCIÓN ---
st.write("")
if st.button(f"Haz clic para terminar tu {dia_nombre}"):
    st.balloons()
    st.toast(f"¡Feliz {dia_nombre}, Carolina! ✨", icon='💖')

st.markdown("<p style='text-align: center; color: white; font-size: 12px; margin-top: 30px;'>Hecho con cariño para Carolina.</p>", unsafe_allow_html=True)
