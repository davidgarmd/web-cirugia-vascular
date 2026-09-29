# Análisis SEO local: cirujano vascular en Ciudad Real

Web: Dr. David García, Angiología y Cirugía Vascular · Fecha: 29/09/2026
Método: auditoría de SEO local, schema, SEO técnico y visibilidad en buscadores con IA (criterios de las skills `seo-local`, `seo-schema`, `seo-technical` y `seo-geo` del repositorio *claude-seo*), aplicada a una web nueva que todavía no está publicada.

---

## 1. Diagnóstico de partida

| Aspecto | Situación |
|---|---|
| Tipo de negocio | Presencial (consulta física en Ciudad Real capital) con área de influencia provincial |
| Sector | Sanitario (YMYL: Google exige máxima experiencia, autoría y fiabilidad) |
| Web previa | No existe: se parte de cero, sin historial ni enlaces |
| Competencia observada | Cadenas de varices con clínica en la ciudad (p. ej. Varicentro Ciudad Real), directorios médicos (Doctoralia, Top Doctors) y hospitales o clínicas privadas con páginas genéricas de "cirugía vascular" |
| Oportunidad | Hay pocas webs de cirujanos vasculares **individuales** en la provincia con contenido específico por patología. Los directorios posicionan por autoridad de dominio, no por calidad del contenido local |

**Conclusión:** el nicho local tiene poca competencia de contenido, pero la batalla del **mapa de Google (local pack)** se gana sobre todo fuera de la web: con la ficha de Google Business Profile, las reseñas y la cercanía. La web es la base que alimenta esa ficha y que convierte las visitas en llamadas.

> Limitación: no tengo acceso a herramientas de volumen de búsqueda (Keyword Planner, DataForSEO, Semrush) y el buscador disponible en esta sesión devuelve resultados de EE. UU. (mezcla "Ciudad Real" con "Ciudad de México"). Los volúmenes de la sección 2 son estimaciones cualitativas. Valídalos con Google Keyword Planner o, mejor aún, con los datos reales de Search Console a los 2-3 meses de publicar.

---

## 2. Mapa de palabras clave (una intención = una página)

| Página | Palabra clave principal | Secundarias | Intención | Volumen estimado |
|---|---|---|---|---|
| Inicio `/` | cirujano vascular Ciudad Real | angiólogo Ciudad Real, cirugía vascular Ciudad Real, especialista en circulación Ciudad Real | Local / transaccional | Medio |
| `/tratamiento-varices-ciudad-real/` | tratamiento varices Ciudad Real | quitar varices Ciudad Real, láser varices, escleroterapia, esclerosis de varices | Transaccional | **Alto** (la más rentable) |
| `/congestion-venosa-pelvica/` | congestión venosa pélvica | síndrome de congestión pélvica, varices pélvicas, varices vulvares, dolor pélvico crónico, embolización de varices pélvicas | Informativa → cita | Medio (nacional, poca competencia de especialistas en la zona) |
| `/eco-doppler-ciudad-real/` | eco doppler Ciudad Real | doppler de piernas, ecografía de venas, eco doppler carótidas | Transaccional | Medio |
| `/enfermedad-arterial-periferica/` | mala circulación piernas | dolor en las piernas al caminar, claudicación intermitente | Informativa → cita | Alto (nacional) |
| `/pie-diabetico-ciudad-real/` | pie diabético Ciudad Real | herida pie diabético que no cura, dedo negro diabetes | Mixta, urgente | Medio |
| `/ulceras-vasculares-ciudad-real/` | úlcera en la pierna que no cicatriza | úlcera venosa, herida en el tobillo | Informativa → cita | Medio |
| `/aneurisma-aorta-abdominal/` | aneurisma de aorta abdominal | aorta dilatada, endoprótesis EVAR | Informativa | Medio (nacional) |
| `/trombosis-venosa-profunda/` | trombosis venosa profunda síntomas | pierna hinchada y dolorida, flebitis | Informativa / urgencia | Alto (nacional) |
| `/estenosis-carotida/` | estenosis de carótida | placas en la carótida, endarterectomía | Informativa | Bajo-medio |
| `/blog/...` | cuándo ir al cirujano vascular | síntomas de mala circulación | Informativa | Medio |

Criterio: las páginas con **"Ciudad Real" en URL, título y H1** atacan búsquedas transaccionales locales (varices, eco-doppler, pie diabético). Las patologías que se buscan sobre todo como duda de salud (trombosis, aneurisma) llevan URL genérica para competir a nivel nacional y atraer tráfico que luego se convierte por la mención local en título y contenido.

---

## 3. Lo que ya está implementado en la web

### SEO on-page
- Título (≤ 65 caracteres aprox.) y meta descripción únicos en cada página, con servicio + ciudad.
- Un único H1 por página con la intención local; jerarquía H2 limpia.
- URLs limpias y descriptivas, con barra final coherente y `canonical` absoluto.
- Enlazado interno en estrella: portada (tótem «¿Qué notas?» y mapa vascular) → plano `/tratamientos/` → 9 páginas de patología, que se enlazan entre sí con anclas descriptivas y con el eco-doppler como página pivote. Todas a ≤ 2 clics de la portada.
- Migas de pan visibles y en schema.
- NAP (nombre, dirección y teléfono) visible en el pie de todas las páginas, en contacto y en la portada, idéntico al del schema.
- Botón de llamada (`tel:`), WhatsApp y barra fija de contacto en móvil.
- Lista de poblaciones atendidas en la portada, **sin crear páginas "puerta" por municipio** (penalizables desde la actualización de marzo de 2024).

### Contenido (E-E-A-T para salud)
- Contenido original y distinto en cada página (sin plantillas intercambiables), escrito con la voz de la línea *Vascular para Pacientes*: tú, analogías cotidianas, mitos y realidades, semáforo "pide cita / urgencias / lo que puedes hacer hoy".
- Bloque **"En pocas palabras"** al inicio de cada página: una respuesta autocontenida de 50-80 palabras, que es el formato que citan Google AI Overviews, ChatGPT y otros buscadores con IA.
- Firma "Contenido revisado por… · Última revisión" en cada página médica, con enlace a la biografía.
- Aviso educativo y criterios de urgencia explícitos (rojo reservado solo para urgencias).

### Datos estructurados (JSON-LD, validado)
- `MedicalClinic` con dirección, coordenadas, horario (`openingHoursSpecification`), área atendida y servicios.
- `Person` (el médico) con cargo, afiliación hospitalaria, `knowsAbout` y `sameAs` a redes: conecta autor, consulta y contenido como una sola entidad.
- `MedicalWebPage` en cada patología con `about` → `MedicalCondition`, `reviewedBy`, `lastReviewed` y `audience: Patient`.
- `BreadcrumbList`, `WebSite`, `ProfilePage`, `ContactPage`, `Blog` y `BlogPosting`.
- Deliberadamente **sin** `FAQPage` (Google retiró los resultados enriquecidos de FAQ en mayo de 2026) y **sin** `aggregateRating` (las reseñas propias no son elegibles y las inventadas están prohibidas).
- El generador elimina del schema cualquier dato con `[marcador]` pendiente, para no publicar información falsa.

### SEO técnico y rendimiento
- HTML estático: sin frameworks, sin JavaScript salvo 5 líneas para el menú móvil. Core Web Vitals excelentes esperables (LCP de texto, sin CLS).
- Tipografías Inter y Montserrat **alojadas en el propio servidor** (evita la transferencia de IP a Google Fonts, conflictiva con el RGPD) y precargadas.
- Sin cookies ni analítica de terceros → no necesita banner de cookies mientras siga así.
- `robots.txt` que permite los rastreadores de búsqueda con IA (OAI-SearchBot, Claude-SearchBot, PerplexityBot), `sitemap.xml`, `llms.txt` opcional, página 404, imagen Open Graph 1200×630, `lang="es-ES"`, metaetiquetas geográficas.
- Accesible: contraste AA, enlace "saltar al contenido", foco visible, tamaño de letra base de 18 px pensado para pacientes mayores, respeta `prefers-reduced-motion`.

---

## 4. Puntuación estimada (SEO local, tras publicar y completar datos)

| Dimensión (peso) | Web sola | Con acciones de la sección 5 |
|---|---|---|
| Google Business Profile (25%) | 0/25 (no existe aún) | 20-25 |
| Reseñas y reputación (20%) | 0/20 | 12-18 |
| SEO on-page local (20%) | 18/20 | 19/20 |
| NAP y citaciones (15%) | 6/15 (NAP interno coherente, sin directorios) | 12-14 |
| Schema local (10%) | 9/10 | 10/10 |
| Enlaces y autoridad local (10%) | 1/10 | 5-7 |
| **Total** | **~34/100** | **~78-93/100** |

La web está prácticamente al máximo de lo que puede aportar por sí sola. Más de la mitad del resultado depende de la ficha de Google y de las reseñas.

---

## 5. Diez acciones priorizadas

**Críticas (antes o el mismo día de publicar)**
1. **Completar los datos de `contenido.py`**: teléfono, dirección, nº de colegiado, nº de registro sanitario del centro, horario, coordenadas exactas. Sin NAP real, no hay SEO local.
2. **Crear y verificar Google Business Profile.** Categoría principal: *Cirujano vascular* (es el factor nº 1 del mapa; una categoría equivocada es el factor negativo nº 1). Secundarias: *Clínica de varices*, *Médico*, *Servicio de ecografía*. Nombre = tu nombre real, sin palabras clave añadidas (penalizable). Enlaza la ficha a la página `/contacto/` o `/tratamiento-varices-ciudad-real/` en lugar de a la portada, para no canibalizar el posicionamiento orgánico de la home.
3. **Foto profesional real** en `static/img/david-garcia-cirujano-vascular.jpg` (cuadrada, ≥ 640 px) y 10-15 fotos de la consulta, la sala de ecografía y la fachada en la ficha de Google.
4. **Dar de alta el dominio en Google Search Console y Bing Webmaster Tools** y enviar el sitemap. Bing alimenta a ChatGPT y Copilot.

**Altas (primer mes)**
5. **Sistema de reseñas constante**: tarjeta o QR en consulta con el enlace directo de reseña, pidiéndola a *todos* los pacientes (pedirla solo a los satisfechos está prohibido por Google). Objetivo: superar 10 reseñas cuanto antes y mantener un goteo sin huecos de más de 2-3 semanas. Al responder, nunca confirmes que la persona es paciente ni menciones datos clínicos (secreto profesional y RGPD).
6. **Perfiles coherentes en directorios** con NAP idéntico carácter a carácter: Doctoralia, Top Doctors, Apple Business Connect (Apple Maps), Bing Places, Páginas Amarillas, directorio del Colegio de Médicos y de la SEACV, y el hospital si tiene fichas de profesionales.
7. **Enlazar la web desde tus redes** (Instagram @davidgarmd, LinkedIn, TikTok) y añadir esos perfiles a `CONFIG["redes"]` para reforzar la entidad.

**Medias (meses 2-6)**
8. **Blog: dos artículos al mes** reutilizando lo que ya produces en la línea *Vascular para Pacientes* (cada carrusel o post se convierte en un artículo de 800-1200 palabras que enlaza a su página de tratamiento). Temas con demanda: "¿las varices vuelven tras el láser?", "medias de compresión: cuándo sí y cuándo no", "calambres nocturnos en las piernas", "piernas hinchadas en verano", "¿es grave una flebitis?", "diabetes y pies fríos", "cribado de aneurisma de aorta en hombres de 65".
9. **Enlaces locales**: prensa local (Lanza, La Tribuna de Ciudad Real, Cadena SER Ciudad Real) con piezas de divulgación estacional (varices en verano, pie diabético en el Día Mundial de la Diabetes, 14 de noviembre); asociaciones de diabéticos de la provincia; charlas en centros de mayores o farmacias con enlace a la web; universidad (UCLM).
10. **Publicaciones semanales en la ficha de Google** (reciclando el contenido de redes) y respuesta a todas las reseñas en menos de 48 h.

---

## 6. Cumplimiento normativo (imprescindible en publicidad sanitaria)

- **Número de registro del centro sanitario** visible en la web y en la publicidad (normativa de Castilla-La Mancha y Real Decreto 1907/1996 de publicidad sanitaria). Confirma con la Consejería de Sanidad si tu publicidad requiere autorización previa.
- **Aviso legal LSSI-CE** con titulación, colegio y nº de colegiado (plantilla incluida en `/aviso-legal/`).
- **Código de Deontología Médica**: publicidad objetiva y prudente, sin promesas de resultados, sin testimonios de curación, sin precios gancho. Los textos de la web evitan todo esto a propósito.
- **RGPD**: el formulario solo pide nombre, teléfono y motivo general, y avisa de no enviar datos clínicos. Si añades un servicio de formularios o un gestor de citas, firma el contrato de encargado del tratamiento.
- Las plantillas de aviso legal y privacidad son orientativas: que las revise un asesor, idealmente el del Colegio de Médicos.

---

## 7. Métricas a seguir (KPI)

| KPI | Herramienta | Objetivo a 6 meses |
|---|---|---|
| Posición media de "cirujano vascular Ciudad Real" | Search Console | Top 3 orgánico |
| Aparición en el mapa (local pack) para "varices Ciudad Real" | Ficha de Google / búsqueda de incógnito desde varios puntos de la ciudad | Top 3 |
| Llamadas y clics en "Cómo llegar" | Estadísticas de la ficha de Google | Crecimiento mes a mes |
| Nº de reseñas y nota | Ficha de Google | ≥ 25 reseñas, ≥ 4,7 |
| Clics orgánicos | Search Console | Crecimiento sostenido |
| Citas atribuidas a web/Google | Pregunta "¿cómo nos conociste?" al pedir cita | Registro mensual |

Si más adelante quieres analítica en la web, usa una opción sin cookies (Plausible, Umami o Matomo sin cookies) para no necesitar banner.

---

## 8. Plan de 90 días

| Semana | Tareas |
|---|---|
| 1 | Completar datos, foto, dominio y alojamiento. Publicar. Search Console y Bing. Crear la ficha de Google y pedir la verificación |
| 2-3 | Ficha verificada con fotos, horario y servicios. Directorios (acción 6). Primeras reseñas |
| 4-6 | Dos artículos de blog. Publicaciones semanales en la ficha. Primera nota de prensa local |
| 7-12 | Dos artículos al mes, revisión de Search Console: reforzar las páginas que asoman en posiciones 5-15 con más contenido y enlaces internos. Contactos con asociaciones de pacientes |

---

## 9. Qué no puede evaluar este análisis

Rankings reales por cuadrícula geográfica, autoridad de dominio de la competencia, volúmenes exactos de búsqueda, perfil de enlaces de los competidores y datos de la ficha de Google (aún inexistente). Para cubrirlo: Google Keyword Planner (gratis), Search Console (gratis, tras publicar) y, si quieres ir más allá, Local Falcon o BrightLocal para el seguimiento del mapa.
