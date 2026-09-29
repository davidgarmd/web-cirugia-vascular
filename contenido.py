"""Contenido de la web: datos de la consulta, tratamientos, preguntas frecuentes y blog.

Edita aquí los textos y ejecuta `python3 build.py` para regenerar la carpeta `public/`.
Todo lo que aparece entre corchetes [ASÍ] es un dato que tienes que completar.

Voz: línea "Vascular para Pacientes" (tú, analogías cotidianas, el especialista en tercera
persona, rojo solo para urgencias, cierre en una conducta concreta).
"""

# ---------------------------------------------------------------------------
# 1. DATOS DE LA CONSULTA  (rellenar antes de publicar)
# ---------------------------------------------------------------------------
CONFIG = {
    # Dominio definitivo, sin barra final.
    "dominio": "https://www.cirujanovascularciudadreal.es",
    "marca": "David García · Cirugía Vascular",
    "nombre": "Dr. David García",
    "nombre_completo": "David García [Segundo apellido]",
    "titulo": "Cirujano Vascular y Endovascular",
    "especialidad": "Angiología y Cirugía Vascular",
    "eslogan": "Cirugía vascular, ciencia y preguntas incómodas: medicina bien contada",
    "colegiado": "[Nº de colegiado]",
    "registro_sanitario": "[Nº de inscripción en el Registro de Centros Sanitarios de Castilla-La Mancha]",
    "telefono": "[Teléfono]",            # formato visible, ej.: "926 00 00 00"
    "telefono_enlace": "+34000000000",   # formato tel: internacional sin espacios
    "whatsapp": "34000000000",           # sin + ni espacios, para wa.me
    "email": "[email de la consulta]",
    "centro": "[Nombre del centro o clínica]",
    "calle": "[Calle y número]",
    "cp": "[13001]",
    "ciudad": "Ciudad Real",
    "provincia": "Ciudad Real",
    "region": "Castilla-La Mancha",
    "lat": "38.98480",  # ajusta a la puerta de la consulta (5 decimales)
    "lng": "-3.92740",
    "horario_texto": "[Lunes a viernes, de 16:00 a 20:00]",
    "horario_schema": [{"dias": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "abre": "16:00", "cierra": "20:00"}],
    "enlace_mapa": "https://www.google.com/maps/search/?api=1&query=Cirujano+vascular+Ciudad+Real",
    "enlace_reserva": "",  # Doctoralia / Top Doctors / agenda propia. Vacío = se oculta el botón.
    "hospital": "Hospital General Universitario de Ciudad Real",
    "hospital_url": "https://sanidad.castillalamancha.es/",
    "redes": {
        "Instagram": "https://www.instagram.com/davidgarmd/",
        # "LinkedIn": "https://www.linkedin.com/in/...",
        # "TikTok": "https://www.tiktok.com/@davidgarmd",
    },
    "fecha_revision": "2026-09-29",
    "formulario_action": "",  # URL de Formspree/Getform/etc. Vacío = el formulario abre el correo.
}

POBLACIONES = [
    "Miguelturra", "Puertollano", "Valdepeñas", "Tomelloso", "Alcázar de San Juan",
    "Manzanares", "Daimiel", "Almagro", "Bolaños de Calatrava", "Almadén",
    "La Solana", "Villarrubia de los Ojos", "Malagón", "Campo de Criptana", "Argamasilla de Calatrava",
]

# ---------------------------------------------------------------------------
# 2. TRATAMIENTOS  (una página por patología = una intención de búsqueda)
# ---------------------------------------------------------------------------
# Revisa que las técnicas listadas coincidan con lo que ofreces de verdad en la consulta.
SERVICIOS = [
    {
        "slug": "tratamiento-varices-ciudad-real",
        "menu": "Varices",
        "icono": "vena",
        "title": "Tratamiento de varices en Ciudad Real | Cirujano vascular",
        "description": "Tratamiento de varices en Ciudad Real: estudio con eco-doppler, escleroterapia, láser endovenoso y microcirugía ambulatoria. Valoración por cirujano vascular.",
        "h1": "Tratamiento de varices en Ciudad Real",
        "resumen": "Piernas cansadas, arañas vasculares y varices: estudio con eco-doppler y tratamiento a medida.",
        "condicion": "Varices (insuficiencia venosa crónica)",
        "escena": "Llega la tarde y las piernas te pesan como si hubieras cargado sacos. Los tobillos marcan el calcetín, por la noche aparece algún calambre y, cuando te miras, hay venas que antes no estaban. Le pasa a alrededor de 1 de cada 4 adultos, y casi todos tardan años en consultarlo.",
        "respuesta": "Las varices son venas dilatadas porque sus válvulas ya no cierran bien y la sangre se estanca en la pierna. Se estudian con un eco-doppler, una ecografía indolora que muestra qué vena falla. Según el caso se tratan con medias, escleroterapia, láser o radiofrecuencia endovenosa o microcirugía, casi siempre con anestesia local y volviendo a casa el mismo día.",
        "secciones": [
            ("Qué está pasando dentro de tu pierna",
             "<p>La sangre de las piernas tiene que subir hasta el corazón contra la gravedad. Para no caer hacia abajo, las venas tienen <strong>válvulas</strong>, unas compuertas que se abren al subir la sangre y se cierran detrás. Cuando esas compuertas fallan, la sangre se queda embalsada, la vena se estira y aparece la variz.</p>"
             "<p>El nombre médico es <strong>insuficiencia venosa crónica</strong>. La vena que más a menudo falla es la safena, la carretera principal de retorno de la sangre por debajo de la piel. Influyen la herencia familiar, los embarazos, trabajar muchas horas de pie o sentado, el sobrepeso y los años.</p>"),
            ("Cómo se diagnostica",
             "<p>Con un <a href=\"/eco-doppler-ciudad-real/\">eco-doppler venoso</a>. Es una ecografía que, además de ver la vena, escucha y mide hacia dónde va la sangre. Con ella el cirujano vascular dibuja un mapa de tus venas y decide qué hay que tratar y qué conviene dejar tranquilo. Tratar varices sin ese mapa es una de las causas más frecuentes de que vuelvan a salir.</p>"),
            ("Tratamientos",
             "<ul>"
             "<li><strong>Medias de compresión y hábitos</strong>. Alivian la pesadez y son la base en casos leves.</li>"
             "<li><strong>Escleroterapia</strong> (líquida o en espuma). Se inyecta un medicamento que cierra la vena por dentro. Útil en arañas vasculares y varices pequeñas, sin quirófano.</li>"
             "<li><strong>Ablación endovenosa con láser o radiofrecuencia</strong>. A través de una punción se introduce una fibra que sella la vena enferma con calor, con anestesia local. Se camina desde el primer momento.</li>"
             "<li><strong>Flebectomía ambulatoria</strong>. Se retiran las varices por incisiones de pocos milímetros que apenas dejan marca.</li>"
             "<li><strong>Cirugía convencional</strong>, para casos concretos.</li>"
             "</ul>"
             "<p>La técnica se elige según tu mapa venoso, tus síntomas y lo que esperas del tratamiento, y se decide contigo en consulta.</p>"),
            ("Qué puedes hacer tú (y qué no funciona)",
             "<ul class=\"lista-check\">"
             "<li>Caminar a diario: la pantorrilla funciona como una bomba que empuja la sangre hacia arriba.</li>"
             "<li>Elevar las piernas un rato al final del día.</li>"
             "<li>Evitar el calor directo prolongado (saunas, depilación con cera caliente, tumbarse al sol).</li>"
             "<li>Mantener un peso saludable.</li>"
             "</ul>"
             "<p>No hay pastilla milagro ni crema que cierre una variz. Algunos fármacos y geles alivian la sensación de pesadez, y está bien usarlos para eso, pero la vena seguirá ahí.</p>"),
        ],
        "mitos": [
            ("Cruzar las piernas provoca varices.", "No hay pruebas de que las cause. Lo que sí influye es pasar muchas horas quieto, de pie o sentado."),
            ("Si me quitan la safena, la sangre no tendrá por dónde volver.", "La vena enferma ya no estaba ayudando: la sangre iba hacia abajo. Casi toda la sangre de la pierna vuelve por las venas profundas, que siguen funcionando."),
            ("Las varices son solo un tema estético.", "A veces lo son, pero pueden dar pesadez, flebitis, manchas en la piel y úlceras. Merece la pena que las mire un especialista."),
        ],
        "pide_cita": [
            "Pesadez, hinchazón o calambres que se repiten.",
            "Varices que duelen, pican o se ponen duras.",
            "Manchas oscuras o piel endurecida en los tobillos.",
            "Una herida cerca del tobillo que no termina de cerrar.",
        ],
        "urgencia": "Si una pierna se hincha de golpe, se pone caliente y te duele al apoyarla, puede ser una trombosis: acude a urgencias hoy, no pidas cita para la semana que viene.",
        "faqs": [
            ("¿El tratamiento de varices duele?", "Las técnicas actuales se hacen con anestesia local. La mayoría de las personas notan pequeñas molestias durante unos días y caminan desde el primer momento."),
            ("¿Las varices vuelven a salir?", "La tendencia a tener varices es crónica y con los años pueden aparecer otras. Un buen estudio con eco-doppler antes de tratar reduce mucho las recaídas, y las revisiones permiten tratar a tiempo lo nuevo."),
            ("¿Cuál es la mejor época para tratar las varices?", "Cualquiera. En otoño e invierno resulta más cómodo llevar medias de compresión y evitar el sol en la zona tratada."),
            ("¿Cuánto tiempo tengo que estar de baja?", "Con las técnicas mínimamente invasivas, muchas personas vuelven a su actividad en uno o dos días. Depende del trabajo y del tratamiento, y se concreta en consulta."),
        ],
        "llevar": "Si te pesan las piernas cada tarde, no es algo con lo que haya que aprender a vivir: con un eco-doppler se sabe qué vena falla y cómo arreglarla.",
        "relacionados": ["eco-doppler-ciudad-real", "ulceras-vasculares-ciudad-real", "trombosis-venosa-profunda"],
    },
    {
        "slug": "congestion-venosa-pelvica",
        "menu": "Congestión pélvica",
        "icono": "pelvis",
        "title": "Congestión venosa pélvica en Ciudad Real | Varices pélvicas y vulvares",
        "description": "Dolor pélvico crónico, varices vulvares o varices que vuelven tras tratarlas: congestión venosa pélvica. Diagnóstico con eco-doppler y embolización. Ciudad Real.",
        "h1": "Congestión venosa pélvica",
        "resumen": "Dolor pélvico que empeora de pie, varices vulvares o varices de las piernas que vuelven.",
        "condicion": "Síndrome de congestión venosa pélvica",
        "escena": "Es un dolor sordo en la parte baja de la tripa que va a más a lo largo del día, sobre todo si pasas horas de pie, y que mejora al tumbarte. A veces molesta en las relaciones o después de ellas. Has pasado por varias consultas, las pruebas salen normales y nadie termina de darte una explicación.",
        "respuesta": "La congestión venosa pélvica es la dilatación de las venas de la pelvis, casi siempre de la vena ovárica, porque sus válvulas no cierran y la sangre se embalsa. Produce dolor pélvico crónico que empeora de pie, varices en la vulva, el periné o la cara posterior del muslo, y varices de las piernas que reaparecen tras tratarlas. Se estudia con eco-doppler y pruebas de imagen, y se trata cerrando las venas enfermas desde dentro (embolización), sin cirugía abierta.",
        "secciones": [
            ("Qué está pasando por dentro",
             "<p>Las venas de la pelvis recogen la sangre del útero, los ovarios y la zona genital y la devuelven hacia el corazón. Igual que en las piernas, tienen válvulas que impiden que la sangre retroceda. Cuando esas válvulas fallan, sobre todo tras varios embarazos, la sangre se estanca y las venas se dilatan, como una tubería que se va dando de sí por el peso del agua que no avanza.</p>"
             "<p>Esa sangre embalsada busca salida hacia abajo. Por eso muchas mujeres con congestión pélvica tienen también varices en la vulva, en el periné o en la parte de atrás del muslo, y varices de las piernas que vuelven a aparecer aunque se hayan tratado bien.</p>"),
            ("Cómo se diagnostica",
             "<p>Empieza por una buena historia clínica, porque el patrón del dolor orienta mucho. Después, el <a href=\"/eco-doppler-ciudad-real/\">eco-doppler</a> estudia el reflujo en las venas pélvicas y en las de las piernas, y ayuda a entender de dónde vienen las varices que reaparecen. Para planificar el tratamiento se completa con angio-TAC o resonancia, y la confirmación final se hace con una flebografía, que es ver las venas por dentro con contraste en el mismo momento del tratamiento.</p>"
             "<p>Es importante descartar antes otras causas de dolor pélvico junto a tu ginecólogo: la congestión venosa es una causa más, no la única.</p>"),
            ("Tratamiento",
             "<ul>"
             "<li><strong>Embolización de las venas pélvicas</strong>: a través de una punción en una vena del cuello, el brazo o la ingle, se llega a la vena enferma y se cierra desde dentro con espirales metálicas muy finas o con espuma esclerosante. Se hace con anestesia local y, en general, sin ingreso o con un ingreso corto.</li>"
             "<li><strong>Tratamiento de las varices vulvares y de las piernas</strong> que dependen de ese reflujo, una vez cerrado el origen, con escleroterapia o las técnicas habituales de <a href=\"/tratamiento-varices-ciudad-real/\">varices</a>.</li>"
             "<li><strong>Medidas generales</strong> mientras tanto: evitar estar mucho tiempo de pie seguido, descansar tumbada con las piernas algo elevadas y usar ropa de compresión si ayuda.</li>"
             "</ul>"
             "<p>En casos concretos hay otras situaciones que comprimen las venas de la pelvis, como la compresión de la vena renal izquierda o de la vena ilíaca, que tienen su propio tratamiento endovascular. Se valoran en el mismo estudio.</p>"),
        ],
        "mitos": [
            ("Es normal que la regla o el embarazo dejen dolores para siempre.", "Un dolor pélvico que dura más de seis meses y empeora de pie merece estudio. Tiene causas concretas y algunas, como esta, tienen tratamiento."),
            ("Si las varices de las piernas vuelven, es que se trataron mal.", "A veces el origen está más arriba, en la pelvis. Si no se busca, las varices vuelven por mucho que se traten las de la pierna."),
        ],
        "pide_cita": [
            "Dolor en la parte baja del abdomen de más de seis meses que empeora al final del día o de pie.",
            "Varices en la vulva, el periné o la parte de atrás del muslo.",
            "Varices en las piernas que han vuelto a salir tras tratarlas.",
            "Molestias durante o después de las relaciones sexuales, sin otra causa encontrada.",
        ],
        "urgencia": None,
        "faqs": [
            ("¿Solo afecta a mujeres?", "Es mucho más frecuente en mujeres que han tenido embarazos. En hombres, el reflujo de las venas pélvicas se manifiesta más a menudo como varicocele."),
            ("¿La embolización afecta a la fertilidad o a la regla?", "Se cierran venas que ya no funcionan; los órganos siguen recibiendo sangre por otras vías. Aun así, si planeas un embarazo, coméntalo antes para decidir el mejor momento."),
            ("¿Duele la embolización?", "Se hace con anestesia local y sedación si hace falta. Es frecuente notar molestias pélvicas unos días después, que se controlan con analgésicos habituales."),
            ("¿Cuándo se nota la mejoría?", "Muchas pacientes notan alivio en las semanas siguientes, aunque la mejoría completa puede tardar unos meses."),
        ],
        "llevar": "Si llevas tiempo con dolor pélvico que empeora de pie o tus varices vuelven una y otra vez, pide que miren también las venas de la pelvis.",
        "relacionados": ["tratamiento-varices-ciudad-real", "eco-doppler-ciudad-real", "trombosis-venosa-profunda"],
    },
    {
        "slug": "pie-diabetico-ciudad-real",
        "menu": "Pie diabético",
        "icono": "pie",
        "title": "Pie diabético en Ciudad Real | Valoración de la circulación",
        "description": "Pie diabético en Ciudad Real: estudio de la circulación por cirujano vascular, heridas que no cicatrizan y revascularización para salvar la pierna.",
        "h1": "Pie diabético: revisar la circulación a tiempo",
        "resumen": "Heridas que no curan, dedos fríos o de color oscuro: revisar el riego salva piernas.",
        "condicion": "Pie diabético",
        "escena": "Una rozadura del zapato nuevo. No duele, así que se deja estar. Pasan dos semanas y sigue igual, quizá algo más oscura. En una persona con diabetes, esa herida pequeña es el aviso más importante que puede dar el pie.",
        "respuesta": "El pie diabético aparece cuando la diabetes daña a la vez los nervios del pie, que deja de avisar con dolor, y las arterias, que llevan menos sangre. Una herida que no cura en una o dos semanas necesita que se revise la circulación. Si el riego es escaso, abrir la arteria con un balón o un bypass permite que la herida cicatrice y evita muchas amputaciones.",
        "secciones": [
            ("Qué está pasando por dentro",
             "<p>La diabetes hace dos cosas al pie. Por un lado apaga poco a poco los nervios, como una alarma a la que le fallan las pilas: la herida está, pero no avisa. Por otro, estrecha las arterias, que son las tuberías que llevan el oxígeno. Una herida sin riego suficiente no tiene con qué curarse, y si se infecta, avanza rápido.</p>"
             "<p>Por eso muchas de las amputaciones relacionadas con la diabetes se pueden evitar si se detecta a tiempo la <a href=\"/enfermedad-arterial-periferica/\">enfermedad arterial</a> y se devuelve la sangre al pie.</p>"),
            ("Qué se hace en la consulta",
             "<p>El cirujano vascular explora los pulsos del pie, mide el <strong>índice tobillo-brazo</strong> (compara la tensión del tobillo con la del brazo, como mirar si llega la misma presión al final de la manguera) y estudia las arterias con <a href=\"/eco-doppler-ciudad-real/\">eco-doppler</a>. Si hace falta, se completa con un angio-TAC o una arteriografía.</p>"),
            ("Tratamientos",
             "<ul>"
             "<li><strong>Angioplastia</strong>: desde una punción en la ingle se lleva un balón hasta la arteria estrechada y se abre, a veces dejando un stent (un pequeño muelle que la mantiene abierta).</li>"
             "<li><strong>Bypass</strong>: un puente con una vena del propio paciente o una prótesis que rodea la arteria cerrada.</li>"
             "<li><strong>Curas y control de la infección</strong>, junto a enfermería, endocrinología y podología.</li>"
             "</ul>"
             "<p>El pie diabético se trata en equipo. La parte vascular consiste en asegurarse de que llegue sangre para que todo lo demás funcione.</p>"),
            ("Qué puedes hacer tú",
             "<ul class=\"lista-check\">"
             "<li>Mirarte los pies cada día, también entre los dedos (un espejo en el suelo ayuda).</li>"
             "<li>Usar calzado cómodo y revisar su interior antes de ponértelo.</li>"
             "<li>Dejar el tabaco: estrecha las arterias más que cualquier otra cosa.</li>"
             "<li>Mantener la glucosa lo más controlada posible y acudir a las revisiones del pie.</li>"
             "</ul>"),
        ],
        "mitos": [
            ("Si no duele, no es grave.", "En el pie diabético suele ser al revés: la falta de dolor es parte del problema, porque los nervios ya no avisan."),
            ("Andar descalzo por casa fortalece el pie.", "Con diabetes, andar descalzo multiplica las pequeñas heridas que no se notan. Mejor zapatilla cerrada."),
        ],
        "pide_cita": [
            "Una herida, ampolla o rozadura que no mejora en una o dos semanas.",
            "Un pie claramente más frío que el otro.",
            "Dolor en el pie al estar tumbado que mejora al bajar la pierna de la cama.",
            "Pies con piel brillante, sin vello y uñas que apenas crecen.",
        ],
        "urgencia": "Si tienes diabetes y aparece fiebre, un pie rojo e hinchado, mal olor en una herida o una zona negra en un dedo, acude a urgencias hoy mismo.",
        "faqs": [
            ("¿Cada cuánto debe revisarse el pie una persona con diabetes?", "Al menos una vez al año con tu médico o enfermera de familia, y más a menudo si ya hay pérdida de sensibilidad, mala circulación o heridas previas."),
            ("¿Siempre hace falta operar?", "No. Muchas heridas curan con buen control de la diabetes, descarga del apoyo y curas. La revascularización se plantea cuando las pruebas demuestran que el riego no llega para cicatrizar."),
            ("¿Se puede evitar una amputación?", "En muchos casos sí, sobre todo cuando se actúa pronto. Recuperar la circulación a tiempo es uno de los factores que más influyen en salvar la pierna."),
        ],
        "llevar": "Si tienes diabetes, una herida en el pie que no mejora en dos semanas merece que alguien mire cómo llega la sangre.",
        "relacionados": ["enfermedad-arterial-periferica", "ulceras-vasculares-ciudad-real", "eco-doppler-ciudad-real"],
    },
    {
        "slug": "enfermedad-arterial-periferica",
        "menu": "Mala circulación en piernas",
        "icono": "arteria",
        "title": "Mala circulación en las piernas y dolor al caminar | Ciudad Real",
        "description": "Dolor en la pantorrilla al caminar que obliga a parar: enfermedad arterial periférica. Índice tobillo-brazo, eco-doppler y tratamiento por cirujano vascular en Ciudad Real.",
        "h1": "Mala circulación en las piernas y dolor al caminar",
        "resumen": "Dolor en la pantorrilla al caminar que te obliga a parar: las arterias piden atención.",
        "condicion": "Enfermedad arterial periférica",
        "escena": "Sales a andar y, a las pocas calles, la pantorrilla se agarrota. Te paras delante de un escaparate como quien mira algo, esperas un par de minutos y el dolor se va. Vuelves a andar y, a la misma distancia, vuelve. Ese patrón tiene nombre, y no es la edad.",
        "respuesta": "El dolor en la pierna al caminar que obliga a parar y se alivia en reposo se llama claudicación intermitente. Lo produce el estrechamiento de las arterias de las piernas por placas de colesterol y calcio (enfermedad arterial periférica). Se diagnostica con el índice tobillo-brazo y un eco-doppler, y se trata dejando de fumar, caminando a diario, con medicación y, si hace falta, con angioplastia o bypass.",
        "secciones": [
            ("Qué está pasando por dentro",
             "<p>Las arterias son las tuberías que llevan la sangre con oxígeno. Con los años, el tabaco, la diabetes, la tensión alta y el colesterol van dejando placas en su pared, como la cal que estrecha una cañería. En reposo pasa sangre suficiente; al caminar, el músculo pide más y la tubería no da para tanto. De ahí el dolor.</p>"
             "<p>Es una señal que importa más allá de las piernas: las arterias del corazón y del cerebro suelen tener el mismo problema.</p>"),
            ("Cómo se diagnostica",
             "<p>Con el <strong>índice tobillo-brazo</strong>, que compara la tensión en el tobillo con la del brazo. Es rápido, indoloro y se hace en consulta. El <a href=\"/eco-doppler-ciudad-real/\">eco-doppler arterial</a> localiza dónde está el estrechamiento. Si se plantea un procedimiento, se completa con un angio-TAC o una arteriografía.</p>"),
            ("Tratamientos",
             "<ul>"
             "<li><strong>Medicación</strong> para frenar la enfermedad y proteger corazón y cerebro (antiagregantes, estatinas y control de tensión y azúcar), siempre pautada por tu médico.</li>"
             "<li><strong>Angioplastia y stent</strong>, cuando el dolor limita tu vida o la pierna está en riesgo. Se hace por una punción, sin abrir.</li>"
             "<li><strong>Cirugía</strong> (bypass o endarterectomía, que es limpiar la placa de la arteria), en obstrucciones largas o cuando la vía por punción no es posible.</li>"
             "</ul>"),
            ("Qué puedes hacer tú (y qué no funciona)",
             "<ul class=\"lista-check\">"
             "<li>Dejar de fumar. Es, con diferencia, lo que más cambia el pronóstico de la pierna.</li>"
             "<li>Caminar cada día hasta notar molestia, parar, y seguir. Con semanas de constancia, la distancia sin dolor aumenta.</li>"
             "<li>Controlar tensión, azúcar y colesterol con tu médico de familia.</li>"
             "</ul>"
             "<p>Las medias de compresión no sirven para este problema, y si la obstrucción es importante pueden hacer daño. Son para las venas, no para las arterias.</p>"),
        ],
        "mitos": [
            ("Es cosa de la edad, a todo el mundo le pasa.", "Un dolor que aparece siempre a la misma distancia y se va al parar no es normal a ninguna edad. Merece estudio."),
            ("Si me duele al andar, mejor andar menos.", "Es al revés: caminar a diario es parte del tratamiento, porque ayuda a que se formen pequeños caminos alternativos para la sangre."),
        ],
        "pide_cita": [
            "Dolor, calambre o cansancio en pantorrilla, muslo o glúteo al caminar, que cede al parar.",
            "Pies fríos, pérdida de vello en las piernas o uñas que apenas crecen.",
            "Eres fumador o diabético y nunca te han medido el índice tobillo-brazo.",
        ],
        "urgencia": "Si una pierna se queda de repente fría, pálida, dolorida y sin fuerza, llama al 112 o acude a urgencias de inmediato: puede ser una obstrucción aguda de la arteria.",
        "faqs": [
            ("¿Tiene cura la mala circulación en las piernas?", "Las placas no desaparecen, pero la enfermedad se puede frenar, los síntomas mejoran mucho y se previenen complicaciones con hábitos, medicación y, cuando hace falta, un procedimiento."),
            ("¿Qué diferencia hay entre mala circulación arterial y venosa?", "La arterial es falta de sangre que llega (duele al caminar, pies fríos). La venosa es sangre que no vuelve bien (pesadez, hinchazón, varices). Se tratan de forma distinta y por eso el diagnóstico es clave."),
            ("¿La angioplastia necesita ingreso?", "A menudo es un ingreso corto, de un día o ninguno, según la zona tratada y tu situación."),
        ],
        "llevar": "Si te paras siempre en el mismo escaparate, no es por las ofertas: pide que te midan el índice tobillo-brazo.",
        "relacionados": ["pie-diabetico-ciudad-real", "estenosis-carotida", "aneurisma-aorta-abdominal"],
    },
    {
        "slug": "aneurisma-aorta-abdominal",
        "menu": "Aneurisma de aorta",
        "icono": "aorta",
        "title": "Aneurisma de aorta abdominal en Ciudad Real | Cirujano vascular",
        "description": "Aneurisma de aorta abdominal: detección con ecografía, seguimiento y reparación con endoprótesis (EVAR) o cirugía abierta. Cirujano vascular en Ciudad Real.",
        "h1": "Aneurisma de aorta abdominal",
        "resumen": "Una dilatación silenciosa de la arteria principal. Se detecta con una ecografía sencilla.",
        "condicion": "Aneurisma de aorta abdominal",
        "escena": "Casi nunca empieza con un susto. Suele aparecer de refilón, en una ecografía que te hicieron por el riñón o la vesícula, en una línea del informe que dice \"aorta dilatada\". No duele, no se nota, no te cambia el día. Y aun así conviene tomárselo en serio.",
        "respuesta": "Un aneurisma de aorta abdominal es una dilatación de la arteria principal del abdomen, que normalmente tiene más o menos el grosor de un pulgar, unos 2 cm. Casi nunca da síntomas y se detecta con una ecografía. Los pequeños se vigilan con ecografías periódicas; cuando alcanzan unos 5,5 cm en hombres o unos 5 cm en mujeres, o crecen rápido, se reparan con endoprótesis o con cirugía abierta.",
        "secciones": [
            ("Qué está pasando por dentro",
             "<p>La aorta es la tubería principal del cuerpo: sale del corazón y baja por el abdomen repartiendo sangre. Cuando su pared se debilita, se va abombando, como la cámara de una rueda vieja que hace un bulto por donde está más fina. Eso es un aneurisma. Cuanto más grande, más tensión soporta la pared.</p>"),
            ("¿Quién debería hacerse una ecografía de aorta?",
             "<ul>"
             "<li>Hombres de 65 años o más, sobre todo si fuman o han fumado.</li>"
             "<li>Personas con un padre, madre o hermano con aneurisma de aorta.</li>"
             "<li>Quien ya tiene aneurismas en otras arterias o enfermedad arterial en las piernas.</li>"
             "</ul>"
             "<p>Coméntalo con tu médico de familia o pide valoración: la <a href=\"/eco-doppler-ciudad-real/\">ecografía de aorta</a> no tiene radiación ni pinchazos.</p>"),
            ("Vigilar y, cuando toca, reparar",
             "<p>Para un aneurisma pequeño existe algo muy poco dramático: vigilarlo. El cirujano vascular es quien lo mide, quien decide cada cuánto revisarlo y quien marca el momento en que el riesgo de dejarlo supera al de repararlo. Entonces hay dos caminos:</p>"
             "<ul>"
             "<li><strong>Endoprótesis (EVAR)</strong>: un tubo forrado que se coloca por dentro de la aorta desde las arterias de la ingle. Recuperación más rápida.</li>"
             "<li><strong>Cirugía abierta</strong>: se sustituye el tramo dilatado por una prótesis. Muy duradera y con menos controles a largo plazo.</li>"
             "</ul>"
             "<p>Qué opción encaja depende de la forma del aneurisma, la edad y la salud general, y se decide contigo.</p>"),
            ("Qué puedes hacer tú",
             "<ul class=\"lista-check\">"
             "<li>Dejar de fumar: el tabaco hace que el aneurisma crezca más rápido.</li>"
             "<li>Controlar la tensión arterial.</li>"
             "<li>No saltarte las revisiones, aunque te encuentres perfectamente.</li>"
             "</ul>"
             "<p>No existe una pastilla que lo haga encoger. Lo que funciona es vigilarlo y cuidar los factores de riesgo.</p>"),
        ],
        "mitos": [
            ("Si no me duele, no está creciendo.", "El aneurisma crece sin avisar. Solo la ecografía dice si ha cambiado."),
            ("Con un aneurisma no puedo hacer ejercicio.", "Caminar, nadar o ir en bici a ritmo cómodo es recomendable. Lo que conviene evitar son los esfuerzos bruscos de mucha carga, y eso se concreta en consulta."),
        ],
        "pide_cita": [
            "Te han dicho en un informe que tienes la aorta dilatada o un aneurisma.",
            "Eres hombre, mayor de 65 y fumas o has fumado.",
            "Tienes un familiar directo con aneurisma de aorta.",
        ],
        "urgencia": "Un dolor brusco e intenso en el abdomen o la zona lumbar, con mareo o sudor frío, en alguien con aneurisma conocido es una emergencia: llama al 112.",
        "faqs": [
            ("¿Un aneurisma de aorta da síntomas?", "Casi nunca. Suele descubrirse de forma casual en una ecografía o un TAC hechos por otro motivo."),
            ("¿Cada cuánto hay que revisarlo?", "Depende del tamaño. Los más pequeños se controlan cada varios años y los más grandes cada pocos meses. El intervalo lo marca el cirujano vascular."),
            ("¿Qué es mejor, la endoprótesis o la cirugía abierta?", "Ninguna es mejor para todo el mundo. La endoprótesis se recupera antes; la cirugía abierta necesita menos revisiones a largo plazo. Se elige según tu anatomía y tu salud."),
        ],
        "llevar": "Con un aneurisma pequeño, lo importante no es el susto, es el seguimiento.",
        "relacionados": ["eco-doppler-ciudad-real", "enfermedad-arterial-periferica", "estenosis-carotida"],
    },
    {
        "slug": "trombosis-venosa-profunda",
        "menu": "Trombosis venosa",
        "icono": "trombo",
        "title": "Trombosis venosa profunda: síntomas y seguimiento | Ciudad Real",
        "description": "Trombosis venosa profunda en la pierna: síntomas, cuándo ir a urgencias, anticoagulación y seguimiento para evitar secuelas. Cirujano vascular en Ciudad Real.",
        "h1": "Trombosis venosa profunda en la pierna",
        "resumen": "Pierna hinchada, caliente y dolorosa de repente: diagnóstico urgente y seguimiento después.",
        "condicion": "Trombosis venosa profunda",
        "escena": "Vuelves de un viaje largo, o llevas unos días en cama tras una operación, y notas la pantorrilla tirante. A la mañana siguiente la pierna está más gorda que la otra, caliente y te duele al apoyar. No es un tirón.",
        "respuesta": "La trombosis venosa profunda es un coágulo dentro de una vena profunda, casi siempre de la pierna. Da hinchazón de una sola pierna, dolor y calor, y hay que acudir a urgencias porque el coágulo puede viajar al pulmón. Se confirma con eco-doppler y se trata con anticoagulantes. Después conviene un seguimiento vascular para prevenir secuelas como la hinchazón crónica.",
        "secciones": [
            ("Qué está pasando por dentro",
             "<p>La sangre de las venas de la pierna sube despacio. Si se queda quieta mucho tiempo (inmovilidad, viajes largos, posoperatorio) o coagula con más facilidad de lo normal (embarazo, posparto, anticonceptivos hormonales, cáncer), puede formar un tapón dentro de la vena, como un atasco que cierra un carril. La sangre se acumula detrás y la pierna se hincha.</p>"),
            ("Diagnóstico y tratamiento",
             "<p>Se confirma con un <a href=\"/eco-doppler-ciudad-real/\">eco-doppler venoso</a>. El tratamiento es la <strong>anticoagulación</strong>: medicamentos que impiden que el coágulo crezca mientras el propio cuerpo lo va deshaciendo. Cuánto tiempo se mantiene depende de la causa, normalmente un mínimo de tres meses.</p>"),
            ("Después de la trombosis",
             "<p>Aproximadamente 1 de cada 3 personas desarrolla con los años el <strong>síndrome postrombótico</strong>: pesadez, hinchazón que no se va, manchas en la piel y a veces heridas. Aquí entra el cirujano vascular: revisa cómo se recupera la vena, ajusta las medias de compresión y valora tratamientos específicos en casos seleccionados.</p>"),
        ],
        "mitos": [
            ("Con una trombosis hay que hacer reposo absoluto.", "Una vez empezada la anticoagulación, caminar es recomendable y ayuda a bajar la hinchazón."),
            ("Un masaje en la pantorrilla alivia el dolor.", "Si se sospecha una trombosis, nada de masajes. Lo que toca es ir a urgencias."),
        ],
        "pide_cita": [
            "Ya tuviste una trombosis y la pierna sigue pesada o hinchada.",
            "Estás terminando el tratamiento anticoagulante y quieres saber cómo ha quedado la vena.",
            "Tienes antecedentes de trombosis y varices.",
        ],
        "urgencia": "Si sospechas una trombosis, acude a urgencias hoy. Si además te falta el aire, te duele el pecho o toses con sangre, llama al 112: puede ser una embolia de pulmón.",
        "faqs": [
            ("¿Qué diferencia hay entre flebitis y trombosis?", "La flebitis superficial afecta a una vena bajo la piel y se nota como un cordón duro y rojo. La trombosis profunda afecta a las venas de dentro del músculo y tiene más riesgo. Las dos deben mirarse con eco-doppler."),
            ("¿Cuánto tiempo tendré que tomar anticoagulantes?", "Normalmente un mínimo de tres meses. Si la trombosis no tuvo una causa clara o persisten los factores de riesgo, puede alargarse. Lo decide tu médico."),
            ("¿Tengo que llevar medias después?", "En muchos casos ayudan a controlar la hinchazón. Si las necesitas, el tipo y la presión se ajustan en consulta."),
        ],
        "llevar": "Una sola pierna hinchada, caliente y dolorosa es motivo de urgencias, no de cita: pasado el susto, el seguimiento evita secuelas.",
        "relacionados": ["tratamiento-varices-ciudad-real", "eco-doppler-ciudad-real", "ulceras-vasculares-ciudad-real"],
    },
    {
        "slug": "ulceras-vasculares-ciudad-real",
        "menu": "Úlceras en las piernas",
        "icono": "herida",
        "title": "Úlceras en las piernas que no cicatrizan | Ciudad Real",
        "description": "Úlceras venosas y arteriales en las piernas: por qué no cicatrizan y cómo se tratan. Estudio con eco-doppler y tratamiento de la causa en Ciudad Real.",
        "h1": "Úlceras en las piernas que no cicatrizan",
        "resumen": "Heridas crónicas venosas o arteriales: tratar la causa para que cierren y no vuelvan.",
        "condicion": "Úlcera vascular de la pierna",
        "escena": "Llevas meses de curas. La herida mejora un poco, luego se estanca, luego vuelve a abrirse. Has probado pomadas, apósitos, dejarla al aire. Cuando una herida en la pierna se comporta así, casi siempre hay un problema de circulación debajo.",
        "respuesta": "Una úlcera vascular es una herida en la pierna que no cicatriza en más de cuatro a seis semanas por un problema de circulación. Las más frecuentes son las venosas, por encima del tobillo, causadas por varices o insuficiencia venosa; las arteriales se deben a falta de riego. Se estudian con eco-doppler e índice tobillo-brazo, y cierran cuando se trata la causa además de hacer curas.",
        "secciones": [
            ("Tipos de úlcera",
             "<ul>"
             "<li><strong>Úlcera venosa</strong>: la más frecuente. Suele estar por encima del tobillo, en la cara interna, con la piel de alrededor oscura. Detrás hay <a href=\"/tratamiento-varices-ciudad-real/\">insuficiencia venosa</a>: sangre embalsada que encharca la piel hasta que se rompe.</li>"
             "<li><strong>Úlcera arterial</strong>: en dedos, talón o empeine, muy dolorosa, con la piel pálida y fría. Detrás hay <a href=\"/enfermedad-arterial-periferica/\">falta de riego</a>.</li>"
             "<li><strong>Úlcera neuropática</strong>: típica del <a href=\"/pie-diabetico-ciudad-real/\">pie diabético</a>, en zonas de apoyo.</li>"
             "</ul>"),
            ("Cómo se tratan",
             "<p>Primero se averigua qué tipo de úlcera es, con exploración, índice tobillo-brazo y eco-doppler. Luego:</p>"
             "<ul>"
             "<li>En la úlcera venosa, <strong>compresión</strong> bien ajustada y tratamiento de las venas enfermas, que acelera la cicatrización y reduce que vuelva a abrirse.</li>"
             "<li>En la úlcera arterial, <strong>devolver el riego</strong> con angioplastia o bypass.</li>"
             "<li>En todas, curas adecuadas, control de la infección y del dolor, de la mano de enfermería.</li>"
             "</ul>"),
        ],
        "mitos": [
            ("Dejarla al aire ayuda a que se seque y cure.", "Las heridas cicatrizan mejor en un ambiente húmedo y protegido, con el apósito que indique tu enfermera."),
            ("El agua oxigenada o el alcohol limpian mejor.", "Dañan el tejido nuevo. Para limpiar suele bastar suero o agua y jabón, según te indiquen."),
        ],
        "pide_cita": [
            "Una herida en la pierna que lleva más de cuatro semanas sin cerrar.",
            "Una úlcera que se cierra y vuelve a abrirse en el mismo sitio.",
            "Manchas oscuras y piel dura alrededor del tobillo.",
        ],
        "urgencia": "Si la úlcera se acompaña de fiebre, enrojecimiento que se extiende por la pierna o una zona negra, consulta en urgencias hoy.",
        "faqs": [
            ("¿Por qué mi úlcera no se cura con las curas?", "Porque las curas atienden la herida, no la causa. Si hay sangre que no vuelve o sangre que no llega, la úlcera no cierra o reaparece hasta que se corrige eso."),
            ("¿Puedo llevar medias de compresión con una úlcera?", "En la úlcera venosa, la compresión es el pilar del tratamiento. Antes hay que descartar una obstrucción arterial importante, porque en ese caso podría hacer daño."),
        ],
        "llevar": "Una herida en la pierna que no cierra en un mes no necesita otra pomada: necesita saber qué le pasa a la circulación.",
        "relacionados": ["tratamiento-varices-ciudad-real", "pie-diabetico-ciudad-real", "enfermedad-arterial-periferica"],
    },
    {
        "slug": "estenosis-carotida",
        "menu": "Carótidas",
        "icono": "carotida",
        "title": "Estenosis de carótida y prevención del ictus | Ciudad Real",
        "description": "Estenosis carotídea: estudio con eco-doppler de troncos supraaórticos, tratamiento médico, endarterectomía o stent para prevenir el ictus. Cirujano vascular en Ciudad Real.",
        "h1": "Estenosis de carótida y prevención del ictus",
        "resumen": "Estrechamiento de las arterias del cuello que puede causar un ictus. Se estudia con eco-doppler.",
        "condicion": "Estenosis carotídea",
        "escena": "Durante diez minutos, la mano derecha no te respondía bien y te costaba encontrar las palabras. Luego, nada, como si no hubiera pasado. Ese aviso que se va solo es de los que más importa contar.",
        "respuesta": "La estenosis de carótida es el estrechamiento de las arterias del cuello que llevan sangre al cerebro, por placas de colesterol que pueden soltar fragmentos y causar un ictus. Se estudia con un eco-doppler de troncos supraaórticos. Todos los pacientes necesitan tratamiento médico; en estenosis importantes, sobre todo si ya han dado síntomas, se valora retirar la placa (endarterectomía) o colocar un stent.",
        "secciones": [
            ("Qué está pasando por dentro",
             "<p>Las carótidas son las dos arterias del cuello que llevan la sangre al cerebro. Si en ellas se forma una placa, además de estrechar el paso puede desprender pequeños trocitos que viajan hasta el cerebro y tapan una arteria más fina. Eso es un ictus. Cuando el tapón se deshace solo y los síntomas desaparecen en minutos, se llama <strong>accidente isquémico transitorio</strong>: un aviso.</p>"),
            ("Cómo se diagnostica",
             "<p>Con el <a href=\"/eco-doppler-ciudad-real/\">eco-doppler de troncos supraaórticos</a>, que mide cuánto se ha estrechado la arteria sin pinchazos ni radiación. Si se plantea tratamiento, se completa con angio-TAC o angio-resonancia.</p>"),
            ("Tratamientos",
             "<ul>"
             "<li><strong>Tratamiento médico</strong> para todos, pautado por tu médico: antiagregantes, estatinas, control de tensión y azúcar, y dejar el tabaco.</li>"
             "<li><strong>Endarterectomía carotídea</strong>: una operación en el cuello para retirar la placa, indicada sobre todo en estenosis importantes que ya han dado síntomas.</li>"
             "<li><strong>Stent carotídeo</strong>: una alternativa en pacientes seleccionados.</li>"
             "</ul>"
             "<p>Cuando la placa ya ha dado un aviso, el beneficio de actuar es mayor en las primeras semanas, por eso no conviene dejarlo para más adelante.</p>"),
        ],
        "mitos": [
            ("Si el síntoma se pasó solo, no fue nada.", "Un síntoma de ictus que desaparece es un aviso de que puede venir otro. Hay que consultar ese mismo día."),
            ("Todas las estenosis de carótida se operan.", "La mayoría de las que no han dado síntomas se controlan con tratamiento médico y revisiones."),
        ],
        "pide_cita": [
            "Te han oído un soplo en el cuello o te han dicho que tienes placas en las carótidas.",
            "Tienes enfermedad arterial en las piernas o un aneurisma y nunca te han mirado las carótidas.",
        ],
        "urgencia": "Boca torcida, pérdida de fuerza en un brazo o una pierna, dificultad para hablar o pérdida de visión en un ojo son síntomas de ictus: llama al 112 inmediatamente, aunque se pasen solos.",
        "faqs": [
            ("¿La operación de carótida es peligrosa?", "Como toda cirugía tiene riesgos, pero en pacientes bien seleccionados el beneficio para prevenir un ictus supera claramente al riesgo de la intervención."),
            ("¿Cada cuánto hay que revisar una estenosis de carótida?", "Depende del grado de estrechamiento y de si ha dado síntomas. El cirujano vascular fija el intervalo de las ecografías."),
        ],
        "llevar": "Un síntoma de ictus que se va solo no es un alivio, es un aviso: 112 ese mismo día.",
        "relacionados": ["eco-doppler-ciudad-real", "enfermedad-arterial-periferica", "aneurisma-aorta-abdominal"],
    },
    {
        "slug": "eco-doppler-ciudad-real",
        "menu": "Eco-doppler",
        "icono": "eco",
        "title": "Eco-doppler en Ciudad Real | Venoso, arterial, carótidas y aorta",
        "description": "Eco-doppler vascular en consulta en Ciudad Real: estudio de varices, circulación arterial, carótidas y aorta. Sin radiación, sin pinchazos y con resultado en el momento.",
        "h1": "Eco-doppler vascular en Ciudad Real",
        "resumen": "La prueba clave de la cirugía vascular: sin radiación, sin pinchazos y con resultado en el momento.",
        "condicion": None,
        "escena": "Te tumbas en la camilla, notas el gel frío y durante unos minutos oyes un sonido rítmico que parece viento. Es tu sangre. Esa prueba tan tranquila es la que decide casi todo lo que viene después en cirugía vascular.",
        "respuesta": "El eco-doppler es una ecografía que, además de ver arterias y venas, mide la velocidad y la dirección de la sangre. No tiene radiación ni pinchazos y dura entre 15 y 40 minutos. Sirve para estudiar varices, trombosis, mala circulación, carótidas y aorta. Cuando lo hace el propio cirujano vascular en consulta, sales con un diagnóstico y un plan.",
        "secciones": [
            ("Tipos de estudio",
             "<ul>"
             "<li><strong>Eco-doppler venoso</strong> de piernas: <a href=\"/tratamiento-varices-ciudad-real/\">varices</a>, insuficiencia venosa y <a href=\"/trombosis-venosa-profunda/\">trombosis</a>.</li>"
             "<li><strong>Eco-doppler arterial</strong> de piernas: <a href=\"/enfermedad-arterial-periferica/\">mala circulación</a> y <a href=\"/pie-diabetico-ciudad-real/\">pie diabético</a>.</li>"
             "<li><strong>Eco-doppler de troncos supraaórticos</strong>: <a href=\"/estenosis-carotida/\">carótidas</a> y arterias vertebrales.</li>"
             "<li><strong>Ecografía de aorta abdominal</strong>: detección y seguimiento del <a href=\"/aneurisma-aorta-abdominal/\">aneurisma de aorta</a>.</li>"
             "</ul>"),
            ("Cómo prepararte",
             "<p>Para los estudios de piernas y cuello no hace falta preparación; ven con ropa cómoda. Para la ecografía de aorta ayuda venir en ayunas de unas 6 horas, porque los gases del intestino tapan la imagen. Trae los informes que tengas y la lista de medicación.</p>"),
            ("Por qué importa quién lo hace",
             "<p>Si el mismo especialista que va a proponer el tratamiento es quien hace la prueba, la ecografía responde justo a las preguntas que importan: si hay que tratar, qué tramo y con qué técnica.</p>"),
        ],
        "mitos": [
            ("Es lo mismo que una ecografía normal.", "Utiliza el mismo aparato, pero el doppler añade el estudio del flujo: hacia dónde va la sangre y a qué velocidad. Eso es lo que permite ver una válvula que falla o una arteria estrechada."),
        ],
        "pide_cita": [
            "Tu médico te ha recomendado un estudio vascular.",
            "Tienes síntomas de varices, mala circulación o un aneurisma en seguimiento.",
        ],
        "urgencia": None,
        "faqs": [
            ("¿El eco-doppler duele?", "No. Solo se nota el gel y algo de presión. En el estudio de venas a veces se aprieta la pantorrilla o se pide soplar con la boca cerrada para ver cómo responden las válvulas."),
            ("¿Tiene radiación?", "No. Usa ultrasonidos, se puede repetir las veces que haga falta y es segura en el embarazo."),
            ("¿Me dan el resultado en el momento?", "Sí. Al terminar se explica lo que se ha visto y se entrega el informe con las recomendaciones."),
        ],
        "llevar": "Antes de tratar una vena o una arteria, hay que verla funcionar: para eso está el eco-doppler.",
        "relacionados": ["tratamiento-varices-ciudad-real", "enfermedad-arterial-periferica", "aneurisma-aorta-abdominal"],
    },
]

FAQS_HOME = [
    ("¿Qué trata un cirujano vascular?", "Las enfermedades de arterias, venas y vasos linfáticos fuera del corazón y del interior del cráneo: varices, mala circulación en las piernas, pie diabético, aneurismas, carótidas, trombosis y úlceras."),
    ("¿Es lo mismo angiólogo que cirujano vascular?", "Sí. En España es una única especialidad, Angiología y Cirugía Vascular. El mismo especialista diagnostica, pauta tratamiento médico y realiza los procedimientos por punción y las operaciones."),
    ("¿Necesito volante para pedir cita?", "No. En la consulta privada puedes pedir cita directamente. Si tienes informes o pruebas previas, tráelos."),
    ("¿Atiendes a pacientes de fuera de Ciudad Real capital?", "Sí. Acuden pacientes de toda la provincia, desde Puertollano, Valdepeñas, Tomelloso, Alcázar de San Juan, Manzanares, Daimiel o Almagro, entre otras localidades."),
]

# ---------------------------------------------------------------------------
# 3. BLOG
# ---------------------------------------------------------------------------
BLOG = [
    {
        "slug": "cuando-ir-al-cirujano-vascular",
        "title": "¿Cuándo ir al cirujano vascular? 7 señales en tus piernas",
        "description": "Siete señales en las piernas que indican que conviene consultar a un cirujano vascular, de la pesadez y las varices al dolor al caminar o las heridas que no curan.",
        "h1": "¿Cuándo ir al cirujano vascular? 7 señales en tus piernas",
        "resumen": "De la pesadez al dolor al caminar: señales que merecen una consulta.",
        "fecha": "2026-09-29",
        "cuerpo": (
            "<p>Mucha gente llega tarde a la consulta de cirugía vascular porque ha ido colocando cada molestia en el cajón de \"cosas de la edad\" o \"es que estoy mucho de pie\", y así pasan los años hasta que aparece algo que ya no se puede ignorar. Estas son siete señales que conviene sacar de ese cajón.</p>"
            "<h2>1. Te duele la pantorrilla al caminar y tienes que parar</h2>"
            "<p>Si aparece siempre tras la misma distancia y se va en un par de minutos de descanso, es el síntoma típico de la <a href=\"/enfermedad-arterial-periferica/\">mala circulación arterial</a>.</p>"
            "<h2>2. Tienes varices que se hinchan, duelen o pican</h2>"
            "<p>Las <a href=\"/tratamiento-varices-ciudad-real/\">varices</a> con molestias tienen hoy tratamientos sencillos, con anestesia local y sin ingreso en la mayoría de los casos.</p>"
            "<h2>3. La piel de los tobillos se ha oscurecido o endurecido</h2>"
            "<p>Es la huella de años de sangre embalsada. Suele ser el paso previo a una herida.</p>"
            "<h2>4. Una herida en la pierna o el pie no termina de cerrar</h2>"
            "<p>Más de cuatro a seis semanas sin cicatrizar justifica un estudio de la circulación. Lo explicamos en <a href=\"/ulceras-vasculares-ciudad-real/\">úlceras en las piernas</a>.</p>"
            "<h2>5. Tienes diabetes y notas un pie más frío o de otro color</h2>"
            "<p>En el <a href=\"/pie-diabetico-ciudad-real/\">pie diabético</a>, revisar el riego a tiempo cambia el pronóstico.</p>"
            "<h2>6. Eres hombre, pasas de los 65 y fumas o has fumado</h2>"
            "<p>Aquí no hay síntoma que buscar, y justo por eso merece la pena una ecografía para descartar un <a href=\"/aneurisma-aorta-abdominal/\">aneurisma de aorta</a>.</p>"
            "<h2>7. Te han dicho que tienes placas en las carótidas</h2>"
            "<p>Conviene que un especialista mida el estrechamiento y decida el seguimiento. Más información en <a href=\"/estenosis-carotida/\">estenosis de carótida</a>.</p>"
            "<div class=\"aviso aviso-urgencia\" role=\"note\"><strong>Esto no es para pedir cita, es para urgencias:</strong> una pierna que se hincha de golpe, caliente y dolorosa; una pierna fría, pálida y sin fuerza; o síntomas de ictus aunque se pasen solos (en ese caso, 112).</div>"
            "<h2>Para llevar a casa</h2>"
            "<p>Las enfermedades vasculares avisan en voz baja. Si te has reconocido en alguna de estas señales, una consulta con <a href=\"/eco-doppler-ciudad-real/\">eco-doppler</a> suele bastar para saber qué pasa y qué hacer.</p>"
        ),
    },
]

# ---------------------------------------------------------------------------
# 4. TÓTEM "¿Qué notas?" (portada) y MAPA VASCULAR
# ---------------------------------------------------------------------------
# Cada fila: (lo que nota el paciente, a dónde lleva, slug, pictograma, urgente)
TOTEM = [
    ("Me pesan las piernas", "Varices", "tratamiento-varices-ciudad-real", "vena", False),
    ("Dolor pélvico o varices vulvares", "Congestión pélvica", "congestion-venosa-pelvica", "pelvis", False),
    ("Me duele al caminar", "Mala circulación", "enfermedad-arterial-periferica", "caminar", False),
    ("Una herida en el pie que no cura", "Pie diabético", "pie-diabetico-ciudad-real", "pie", False),
    ("Me han encontrado algo en una prueba", "Aorta dilatada, placas en la carótida", "aneurisma-aorta-abdominal", "informe", False),
    ("Pierna hinchada de golpe", "Urgencias", "trombosis-venosa-profunda", "alarma", True),
]

# Anotaciones del mapa vascular: (texto, slug, tipo de vaso, posición vertical en % del dibujo)
MAPA = [
    ("Carótidas: estenosis", "estenosis-carotida", "arteria", 6),
    ("Aorta: aneurisma", "aneurisma-aorta-abdominal", "arteria", 27),
    ("Venas pélvicas: congestión", "congestion-venosa-pelvica", "vena", 40),
    ("Arteria femoral: mala circulación", "enfermedad-arterial-periferica", "arteria", 55),
    ("Safena: varices", "tratamiento-varices-ciudad-real", "vena", 70),
    ("Pie diabético", "pie-diabetico-ciudad-real", "arteria", 92),
]
