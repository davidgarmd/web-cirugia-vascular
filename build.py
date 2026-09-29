#!/usr/bin/env python3
"""Genera la web estática en ./public a partir de contenido.py.

Uso:  python3 build.py
Sin dependencias externas (solo biblioteca estándar de Python 3.8+).
"""
import html
import json
import shutil
from pathlib import Path

from contenido import BLOG, CONFIG, FAQS_HOME, POBLACIONES, SERVICIOS

RAIZ = Path(__file__).parent
SALIDA = RAIZ / "public"
C = CONFIG
D = C["dominio"].rstrip("/")
SERV = {s["slug"]: s for s in SERVICIOS}
AVATAR = "/img/david-garcia-cirujano-vascular.jpg"
TIENE_AVATAR = (RAIZ / "static" / AVATAR.lstrip("/")).exists()


def e(txt):
    return html.escape(str(txt), quote=True)


def es_placeholder(v):
    return isinstance(v, str) and "[" in v


def limpio(obj):
    """Quita del JSON-LD los campos vacíos o con marcadores [PENDIENTE]."""
    if isinstance(obj, dict):
        out = {k: limpio(v) for k, v in obj.items()}
        return {k: v for k, v in out.items() if v not in (None, "", [], {}) and not es_placeholder(v)}
    if isinstance(obj, list):
        out = [limpio(v) for v in obj]
        return [v for v in out if v not in (None, "", [], {}) and not es_placeholder(v)]
    return obj


# ---------------------------------------------------------------------------
# Iconos (SVG en línea, trazo)
# ---------------------------------------------------------------------------
ICONOS = {
    "vena": '<path d="M9 2c0 4 6 4 6 8s-6 4-6 8 3 4 3 4"/><path d="M15 2c0 2-1 3-2 4"/><circle cx="12" cy="10" r="1.2"/>',
    "pie": '<path d="M8 21c-2.5 0-3.5-2-3-4.5L6.5 9C7 6.5 8 5 10 5s2.5 2 2.5 4v3c0 1.5 1 2.5 2.5 3l1.5.5c1.5.5 2 2 1.5 3.5S16.5 21 15 21z"/><circle cx="15" cy="4" r="1"/><circle cx="18" cy="6" r="1"/>',
    "arteria": '<path d="M2 9h6c2 0 2 2 4 2s2-2 4-2h6"/><path d="M2 15h6c2 0 2-2 4-2s2 2 4 2h6"/>',
    "aorta": '<path d="M10 2v9c0 3-2 5-4 8l-1 3"/><path d="M14 2v9c0 3 2 5 4 8l1 3"/><ellipse cx="12" cy="9" rx="3.2" ry="3"/>',
    "trombo": '<path d="M3 8h18M3 16h18"/><circle cx="12" cy="12" r="2.6"/><path d="M5 12h3M16 12h3"/>',
    "herida": '<rect x="3" y="8" width="18" height="8" rx="4" transform="rotate(-35 12 12)"/><path d="M10 11l.01 0M12 13l.01 0M12 11l.01 0M10 13l.01 0"/>',
    "carotida": '<path d="M9 22V13c0-2-2-3-2-6V2"/><path d="M15 22V13c0-2 2-3 2-6V2"/><path d="M9 13h6"/>',
    "eco": '<path d="M8 3h8l-1 7H9z"/><path d="M12 10v3"/><path d="M6 16c3.5-2.5 8.5-2.5 12 0"/><path d="M4 19c4.5-3.5 11.5-3.5 16 0"/>',
    "tel": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    "wa": '<path d="M3 21l1.7-5A8.5 8.5 0 1 1 8 19.3z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5l1-1.5-2-1-1 1a4 4 0 0 1-2-2l1-1-1-2z"/>',
    "cal": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "pin": '<path d="M12 22s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
    "reloj": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "check": '<path d="M5 12l4 4L19 6"/>',
    "alerta": '<path d="M12 3l10 18H2z"/><path d="M12 10v5M12 18v.01"/>',
    "flecha": '<path d="M5 12h14M13 6l6 6-6 6"/>',
}


def icono(nombre, cls="ico"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONOS[nombre]}</svg>')


# Ilustración de portada: vasos como tubos abiertos con flujo pasante (regla de marca).
ARTE_HERO = """<svg class="hero-arte" viewBox="0 0 480 420" aria-hidden="true" focusable="false">
  <defs>
    <linearGradient id="g1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#56CCF2"/><stop offset="1" stop-color="#2F80ED"/></linearGradient>
  </defs>
  <circle cx="250" cy="200" r="175" fill="#12307a"/>
  <circle cx="250" cy="200" r="130" fill="#173a8f" opacity=".7"/>
  <g fill="none" stroke-linecap="round">
    <path d="M40 330 C140 300 150 170 250 160 S380 60 460 40" stroke="#F4F1EA" stroke-width="30" opacity=".95"/>
    <path d="M40 330 C140 300 150 170 250 160 S380 60 460 40" stroke="url(#g1)" stroke-width="16"/>
    <path d="M40 330 C140 300 150 170 250 160 S380 60 460 40" stroke="#fff" stroke-width="3" stroke-dasharray="4 22" class="flujo"/>
    <path d="M60 390 C170 360 200 250 290 240 S400 170 470 160" stroke="#F4F1EA" stroke-width="24" opacity=".6"/>
    <path d="M60 390 C170 360 200 250 290 240 S400 170 470 160" stroke="#0A2463" stroke-width="12"/>
    <path d="M60 390 C170 360 200 250 290 240 S400 170 470 160" stroke="#56CCF2" stroke-width="2.5" stroke-dasharray="3 20" class="flujo lento"/>
  </g>
  <g fill="#F4F1EA">
    <circle cx="250" cy="160" r="7"/><circle cx="360" cy="95" r="4"/><circle cx="150" cy="255" r="5"/>
  </g>
</svg>"""


# ---------------------------------------------------------------------------
# Fragmentos comunes
# ---------------------------------------------------------------------------
def botones_contacto(cls=""):
    b = [f'<a class="btn btn-primario {cls}" href="tel:{e(C["telefono_enlace"])}">{icono("tel")}Llamar{"" if es_placeholder(C["telefono"]) else " · " + e(C["telefono"])}</a>',
         f'<a class="btn btn-wa {cls}" href="https://wa.me/{e(C["whatsapp"])}" rel="noopener">{icono("wa")}WhatsApp</a>']
    if C.get("enlace_reserva"):
        b.append(f'<a class="btn btn-claro {cls}" href="{e(C["enlace_reserva"])}" rel="noopener">{icono("cal")}Reservar online</a>')
    return '<div class="botones">' + "".join(b) + "</div>"


def cabecera(activo):
    items = [("/tratamientos/", "Tratamientos"), ("/eco-doppler-ciudad-real/", "Eco-doppler"),
             ("/sobre-mi/", "Sobre el doctor"), ("/blog/", "Blog"), ("/contacto/", "Contacto")]
    sub = "".join(f'<li><a href="/{s["slug"]}/">{e(s["menu"])}</a></li>' for s in SERVICIOS if s["slug"] != "eco-doppler-ciudad-real")
    links = []
    for url, txt in items:
        cur = ' aria-current="page"' if activo == url else ""
        if url == "/tratamientos/":
            links.append(f'<li class="con-sub"><a href="{url}"{cur}>{txt}</a><ul class="sub">{sub}</ul></li>')
        else:
            links.append(f'<li><a href="{url}"{cur}>{txt}</a></li>')
    return f"""<a class="saltar" href="#contenido">Saltar al contenido</a>
<header class="cabecera">
  <div class="contenedor cab-fila">
    <a class="logo" href="/" aria-label="Inicio · {e(C['nombre'])}, cirujano vascular en Ciudad Real">
      <svg viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="11" fill="#0A2463"/><path d="M8 27c6-1 7-8 12-9s7-6 12-7" fill="none" stroke="#56CCF2" stroke-width="4" stroke-linecap="round"/><path d="M8 27c6-1 7-8 12-9s7-6 12-7" fill="none" stroke="#fff" stroke-width="1.4" stroke-dasharray="1.5 5" stroke-linecap="round"/></svg>
      <span><strong>{e(C['nombre'])}</strong><small>Cirugía Vascular · Ciudad Real</small></span>
    </a>
    <button class="menu-btn" aria-expanded="false" aria-controls="menu"><span></span><span class="sr">Menú</span></button>
    <nav id="menu" class="nav" aria-label="Principal"><ul>{''.join(links)}</ul>
      <a class="btn btn-primario btn-sm" href="/contacto/">{icono("cal")}Pedir cita</a>
    </nav>
  </div>
</header>"""


def pie():
    serv = "".join(f'<li><a href="/{s["slug"]}/">{e(s["menu"])}</a></li>' for s in SERVICIOS)
    redes = "".join(f'<li><a href="{e(u)}" rel="noopener me">{e(n)}</a></li>' for n, u in C["redes"].items() if not es_placeholder(u))
    return f"""<footer class="pie">
  <div class="contenedor pie-grid">
    <div>
      <p class="pie-marca">{e(C['nombre'])}</p>
      <p>{e(C['titulo'])}<br>Especialista en {e(C['especialidad'])}<br>Nº de colegiado: {e(C['colegiado'])}</p>
      <p class="pie-lema">{e(C['eslogan'])}</p>
    </div>
    <div>
      <p class="pie-tit">Consulta</p>
      <address>{e(C['centro'])}<br>{e(C['calle'])}<br>{e(C['cp'])} {e(C['ciudad'])} ({e(C['provincia'])})<br>
      <a href="tel:{e(C['telefono_enlace'])}">{e(C['telefono'])}</a><br><a href="mailto:{e(C['email'])}">{e(C['email'])}</a></address>
      <p>{e(C['horario_texto'])}</p>
    </div>
    <div><p class="pie-tit">Tratamientos</p><ul>{serv}</ul></div>
    <div><p class="pie-tit">Más</p><ul><li><a href="/sobre-mi/">Sobre el doctor</a></li><li><a href="/blog/">Blog</a></li><li><a href="/contacto/">Contacto</a></li>{redes}</ul></div>
  </div>
  <div class="contenedor pie-legal">
    <p>La información de esta web es educativa y no sustituye la valoración de un médico. Ante síntomas, consulta. En caso de urgencia, llama al 112.</p>
    <p>{e(C['registro_sanitario'])} · <a href="/aviso-legal/">Aviso legal</a> · <a href="/privacidad/">Privacidad</a> · <a href="/cookies/">Cookies</a></p>
  </div>
</footer>
<nav class="barra-movil" aria-label="Contacto rápido">
  <a href="tel:{e(C['telefono_enlace'])}">{icono("tel")}Llamar</a>
  <a href="https://wa.me/{e(C['whatsapp'])}" rel="noopener">{icono("wa")}WhatsApp</a>
  <a href="/contacto/">{icono("cal")}Cita</a>
</nav>
<script>
(function(){{var b=document.querySelector('.menu-btn'),n=document.getElementById('menu');
if(!b)return;b.addEventListener('click',function(){{var a=b.getAttribute('aria-expanded')==='true';
b.setAttribute('aria-expanded',!a);n.classList.toggle('abierto',!a);}});}})();
</script>"""


def migas(lista):
    """lista de (nombre, url). Devuelve (html, schema)."""
    items = [("Inicio", "/")] + lista
    h = '<nav class="migas" aria-label="Estás en"><ol>' + "".join(
        f'<li><a href="{u}">{e(n)}</a></li>' if i < len(items) - 1 else f'<li aria-current="page">{e(n)}</li>'
        for i, (n, u) in enumerate(items)) + "</ol></nav>"
    s = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": D + u} for i, (n, u) in enumerate(items)]}
    return h, s


def avatar_html(cls="avatar"):
    if TIENE_AVATAR:
        return f'<img class="{cls}" src="{AVATAR}" width="320" height="320" alt="{e(C["nombre"])}, cirujano vascular en Ciudad Real" loading="lazy" decoding="async">'
    return (f'<div class="{cls} avatar-vacio" role="img" aria-label="Foto de {e(C["nombre"])} (pendiente)">'
            f'<span>DG</span></div>')


# ---------------------------------------------------------------------------
# Schema.org
# ---------------------------------------------------------------------------
ID_CONSULTA = D + "/#consulta"
ID_MEDICO = D + "/#medico"
ID_WEB = D + "/#web"


def schema_consulta():
    return {
        "@type": "MedicalClinic",
        "@id": ID_CONSULTA,
        "name": f'{C["nombre"]} · Cirugía Vascular en Ciudad Real',
        "url": D + "/",
        "image": D + "/img/og-cirujano-vascular-ciudad-real.png",
        "logo": D + "/favicon.svg",
        "telephone": C["telefono_enlace"] if not es_placeholder(C["telefono"]) else "",
        "email": C["email"],
        "priceRange": "€€",
        "medicalSpecialty": ["https://schema.org/Cardiovascular", "https://schema.org/Surgical"],
        "address": {"@type": "PostalAddress", "streetAddress": C["calle"], "postalCode": C["cp"],
                    "addressLocality": C["ciudad"], "addressRegion": C["region"], "addressCountry": "ES"},
        "geo": {"@type": "GeoCoordinates", "latitude": float(C["lat"]), "longitude": float(C["lng"])},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": h["dias"],
                                       "opens": h["abre"], "closes": h["cierra"]} for h in C["horario_schema"]],
        "areaServed": [{"@type": "City", "name": "Ciudad Real"}, {"@type": "AdministrativeArea", "name": "Provincia de Ciudad Real"}]
                      + [{"@type": "City", "name": p} for p in POBLACIONES],
        "hasMap": C["enlace_mapa"],
        "availableService": [{"@type": "MedicalProcedure" if s["condicion"] is None else "MedicalTherapy",
                              "name": s["h1"], "url": f'{D}/{s["slug"]}/'} for s in SERVICIOS],
        "employee": {"@id": ID_MEDICO},
    }


def schema_medico():
    return {
        "@type": "Person",
        "@id": ID_MEDICO,
        "name": C["nombre"],
        "honorificPrefix": "Dr.",
        "jobTitle": C["titulo"],
        "description": f'Especialista en {C["especialidad"]} en Ciudad Real.',
        "url": D + "/sobre-mi/",
        "image": D + AVATAR if TIENE_AVATAR else "",
        "worksFor": {"@id": ID_CONSULTA},
        "affiliation": {"@type": "Hospital", "name": C["hospital"]},
        "hasOccupation": {"@type": "Occupation", "name": "Cirujano vascular",
                          "occupationLocation": {"@type": "City", "name": "Ciudad Real"}},
        "knowsAbout": [s["condicion"] for s in SERVICIOS if s["condicion"]] + ["Eco-doppler vascular", "Cirugía endovascular"],
        "sameAs": [u for u in C["redes"].values()],
    }


def schema_web():
    return {"@type": "WebSite", "@id": ID_WEB, "url": D + "/", "name": f'{C["nombre"]} · Cirujano vascular en Ciudad Real',
            "inLanguage": "es-ES", "publisher": {"@id": ID_CONSULTA}}


# ---------------------------------------------------------------------------
# Plantilla base
# ---------------------------------------------------------------------------
def documento(ruta, title, description, cuerpo, schemas, activo="", og_type="website", noindex=False):
    url = D + ruta
    grafo = limpio({"@context": "https://schema.org", "@graph": schemas})
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large, max-snippet:-1"
    return f"""<!doctype html>
<html lang="es-ES">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta name="geo.region" content="ES-CR">
<meta name="geo.placename" content="Ciudad Real">
<meta name="geo.position" content="{C['lat']};{C['lng']}">
<meta name="ICBM" content="{C['lat']}, {C['lng']}">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="{e(C['nombre'])} · Cirugía Vascular">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{D}/img/og-cirujano-vascular-ciudad-real.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0A2463">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/montserrat-800.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/estilos.css">
<script type="application/ld+json">{json.dumps(grafo, ensure_ascii=False)}</script>
</head>
<body>
{cabecera(activo)}
<main id="contenido">
{cuerpo}
</main>
{pie()}
</body>
</html>
"""


def bloque_faq(faqs, titulo="Preguntas frecuentes"):
    return (f'<section class="faq" aria-labelledby="faq-t"><h2 id="faq-t">{titulo}</h2>' +
            "".join(f'<details><summary>{e(p)}</summary><p>{e(r)}</p></details>' for p, r in faqs) + "</section>")


def tarjeta_servicio(s):
    return (f'<a class="tarjeta-serv" href="/{s["slug"]}/"><span class="tarjeta-ico">{icono(s["icono"])}</span>'
            f'<span class="tarjeta-tit">{e(s["menu"])}</span><span class="tarjeta-txt">{e(s["resumen"])}</span>'
            f'<span class="tarjeta-mas">Saber más {icono("flecha", "ico ico-sm")}</span></a>')


def banda_cta(titulo="¿Hablamos de tu caso?", texto=None):
    texto = texto or f'Consulta en {C["ciudad"]} con estudio eco-doppler en la misma visita. Sin volante.'
    return f"""<section class="banda-cta"><div class="contenedor banda-fila">
<div><h2>{e(titulo)}</h2><p>{e(texto)}</p></div>{botones_contacto("btn-grande")}</div></section>"""


# ---------------------------------------------------------------------------
# Páginas
# ---------------------------------------------------------------------------
def pag_inicio():
    tarjetas = "".join(tarjeta_servicio(s) for s in SERVICIOS)
    pueblos = "".join(f"<li>{e(p)}</li>" for p in POBLACIONES)
    post = BLOG[0]
    cuerpo = f"""
<section class="hero">
  <div class="contenedor hero-grid">
    <div class="hero-txt">
      <p class="kicker">{e(C['especialidad'])} · Ciudad Real</p>
      <h1>Cirujano vascular en Ciudad Real</h1>
      <p class="hero-lead">Varices, mala circulación en las piernas, pie diabético y aneurismas, estudiados con eco-doppler en la propia consulta y explicados sin prisas, para que salgas sabiendo qué te pasa y qué hacer.</p>
      {botones_contacto("btn-grande")}
      <ul class="sellos">
        <li>{icono("check","ico ico-sm")}Especialista en {e(C['especialidad'])}</li>
        <li>{icono("check","ico ico-sm")}Cirujano en el {e(C['hospital'])}</li>
        <li>{icono("check","ico ico-sm")}Eco-doppler en la misma visita</li>
        <li>{icono("check","ico ico-sm")}Sin volante</li>
      </ul>
    </div>
    <div class="hero-visual">{ARTE_HERO}</div>
  </div>
</section>

<section class="seccion" id="tratamientos" aria-labelledby="trat-t">
  <div class="contenedor">
    <p class="kicker">Qué tratamos</p>
    <h2 id="trat-t">Tratamientos de cirugía vascular en Ciudad Real</h2>
    <p class="intro">Un cirujano vascular se ocupa de las arterias y las venas del cuerpo, salvo las del corazón y las del interior del cráneo. Estos son los problemas por los que más se consulta:</p>
    <div class="rejilla-serv">{tarjetas}</div>
  </div>
</section>

<section class="seccion seccion-crema" aria-labelledby="sem-t">
  <div class="contenedor">
    <p class="kicker">Antes de pedir cita</p>
    <h2 id="sem-t">¿Pido cita o voy a urgencias?</h2>
    <div class="semaforo">
      <div class="sem sem-azul"><h3>{icono("cal")}Pide cita si…</h3><ul>
        <li>Te pesan o se te hinchan las piernas al final del día.</li>
        <li>Tienes varices que molestan, pican o se ponen duras.</li>
        <li>Te duele la pantorrilla al caminar y tienes que parar.</li>
        <li>Una herida en la pierna o el pie lleva semanas sin cerrar.</li>
        <li>Te han encontrado la aorta dilatada o placas en las carótidas.</li></ul></div>
      <div class="sem sem-rojo"><h3>{icono("alerta")}Urgencias o 112 si…</h3><ul>
        <li>Una pierna se hincha de golpe, está caliente y duele al apoyar.</li>
        <li>Una pierna se queda fría, pálida, dolorida y sin fuerza.</li>
        <li>Dolor brusco e intenso en abdomen o espalda con aneurisma conocido.</li>
        <li>Boca torcida, brazo sin fuerza o dificultad para hablar, aunque se pase.</li></ul></div>
      <div class="sem sem-verde"><h3>{icono("check")}Lo que ya puedes hacer hoy</h3><ul>
        <li>Caminar a diario, a tu ritmo.</li>
        <li>Dejar el tabaco: es lo que más protege tus arterias.</li>
        <li>Si tienes diabetes, mirarte los pies cada día.</li>
        <li>Elevar las piernas un rato al final de la tarde.</li></ul></div>
    </div>
  </div>
</section>

<section class="seccion" aria-labelledby="pasos-t">
  <div class="contenedor">
    <p class="kicker">Cómo es la consulta</p>
    <h2 id="pasos-t">Tres pasos, una sola visita</h2>
    <ol class="pasos">
      <li><span class="paso-n">1</span><h3>Te escucha y te explora</h3><p>Qué notas, desde cuándo y qué te preocupa. Trae los informes y la lista de medicación.</p></li>
      <li><span class="paso-n">2</span><h3>Eco-doppler en el momento</h3><p>La <a href="/eco-doppler-ciudad-real/">ecografía vascular</a> se hace en la misma visita: sin radiación ni pinchazos.</p></li>
      <li><span class="paso-n">3</span><h3>Sales con un plan</h3><p>Qué tienes, qué opciones hay y cuál encaja contigo, explicado en tu idioma y por escrito.</p></li>
    </ol>
  </div>
</section>

<section class="seccion seccion-azul" aria-labelledby="doc-t">
  <div class="contenedor doc-fila">
    {avatar_html()}
    <div>
      <p class="kicker kicker-claro">Quién te atiende</p>
      <h2 id="doc-t">{e(C['nombre'])}</h2>
      <p class="doc-cargo">{e(C['titulo'])} · Nº col. {e(C['colegiado'])}</p>
      <p>Especialista en {e(C['especialidad'])} y cirujano en el {e(C['hospital'])}. Además de operar, dedica tiempo a explicar la medicina vascular con claridad en redes como <a href="https://www.instagram.com/davidgarmd/" rel="noopener">@davidgarmd</a>, porque un paciente que entiende lo que tiene decide mejor.</p>
      <a class="btn btn-claro" href="/sobre-mi/">Conoce al doctor {icono("flecha","ico ico-sm")}</a>
    </div>
  </div>
</section>

<section class="seccion" aria-labelledby="blog-t">
  <div class="contenedor">
    <p class="kicker">Del blog</p>
    <h2 id="blog-t">Aprende a leer las señales de tus piernas</h2>
    <a class="tarjeta-blog" href="/blog/{post['slug']}/"><span class="tarjeta-tit">{e(post['h1'])}</span><span class="tarjeta-txt">{e(post['description'])}</span><span class="tarjeta-mas">Leer artículo {icono("flecha","ico ico-sm")}</span></a>
  </div>
</section>

<section class="seccion seccion-crema">
  <div class="contenedor dos-col">
    {bloque_faq(FAQS_HOME)}
    <section aria-labelledby="zona-t">
      <h2 id="zona-t">Pacientes de toda la provincia</h2>
      <p>La consulta está en {e(C['ciudad'])} capital y recibe pacientes de toda la provincia de Ciudad Real:</p>
      <ul class="chips">{pueblos}</ul>
      <div class="tarjeta-nap">
        <p>{icono("pin")}<span><strong>{e(C['centro'])}</strong><br>{e(C['calle'])}, {e(C['cp'])} {e(C['ciudad'])}</span></p>
        <p>{icono("reloj")}<span>{e(C['horario_texto'])}</span></p>
        <p>{icono("tel")}<a href="tel:{e(C['telefono_enlace'])}">{e(C['telefono'])}</a></p>
        <a class="btn btn-claro btn-sm" href="{e(C['enlace_mapa'])}" rel="noopener">Cómo llegar {icono("flecha","ico ico-sm")}</a>
      </div>
    </section>
  </div>
</section>
{banda_cta()}"""
    schemas = [schema_web(), schema_consulta(), schema_medico(),
               {"@type": "WebPage", "@id": D + "/#pagina", "url": D + "/", "name": "Cirujano vascular en Ciudad Real",
                "isPartOf": {"@id": ID_WEB}, "about": {"@id": ID_CONSULTA}, "inLanguage": "es-ES"}]
    return documento("/", f'Cirujano vascular en Ciudad Real | {C["nombre"]}',
                     "Cirujano vascular en Ciudad Real: varices, mala circulación, pie diabético, aneurismas y carótidas. Eco-doppler en la misma consulta. Pide cita sin volante.",
                     cuerpo, schemas, activo="/")


def pag_servicio(s):
    m_html, m_schema = migas([("Tratamientos", "/tratamientos/"), (s["menu"], f'/{s["slug"]}/')])
    secciones = "".join(f'<section><h2 id="s{i}">{e(t)}</h2>{h}</section>' for i, (t, h) in enumerate(s["secciones"]))
    indice = "".join(f'<li><a href="#s{i}">{e(t)}</a></li>' for i, (t, _) in enumerate(s["secciones"]))
    mitos = ""
    if s.get("mitos"):
        mitos = ('<section><h2 id="mitos">Mitos y realidades</h2><div class="mitos">' + "".join(
            f'<div class="mito"><p class="mito-m"><span>Se oye</span>«{e(m)}»</p><p class="mito-r"><span>En realidad</span>{e(r)}</p></div>'
            for m, r in s["mitos"]) + "</div></section>")
        indice += '<li><a href="#mitos">Mitos y realidades</a></li>'
    consultar = ('<section><h2 id="cuando">Cuándo consultar</h2><div class="semaforo semaforo-2">'
                 f'<div class="sem sem-azul"><h3>{icono("cal")}Pide cita si…</h3><ul>' +
                 "".join(f"<li>{e(x)}</li>" for x in s["pide_cita"]) + "</ul></div>")
    if s.get("urgencia"):
        consultar += f'<div class="sem sem-rojo"><h3>{icono("alerta")}Esto es de urgencias</h3><p>{e(s["urgencia"])}</p></div>'
    consultar += "</div></section>"
    indice += '<li><a href="#cuando">Cuándo consultar</a></li><li><a href="#faq-t">Preguntas frecuentes</a></li>'
    relacionados = "".join(tarjeta_servicio(SERV[r]) for r in s["relacionados"])
    cuerpo = f"""
<div class="cabecera-pag"><div class="contenedor">
  {m_html}
  <div class="cab-pag-fila">
    <span class="cab-ico">{icono(s['icono'])}</span>
    <div><h1>{e(s['h1'])}</h1><p class="escena">{e(s['escena'])}</p>{botones_contacto()}</div>
  </div>
</div></div>
<div class="contenedor pag-grid">
  <article class="articulo">
    <div class="respuesta" role="note"><p class="respuesta-t">En pocas palabras</p><p>{e(s['respuesta'])}</p></div>
    {secciones}
    {mitos}
    {consultar}
    {bloque_faq(s['faqs'])}
    <div class="llevar"><p class="llevar-t">Para llevar a casa</p><p>{e(s['llevar'])}</p></div>
    <div class="revisado">{avatar_html('avatar avatar-mini')}<p>Contenido revisado por <a href="/sobre-mi/">{e(C['nombre'])}</a>, {e(C['titulo']).lower()} · Última revisión: <time datetime="{C['fecha_revision']}">{fecha_es(C['fecha_revision'])}</time>.<br><small>Información educativa: no sustituye la valoración de un médico. Ante síntomas, consulta.</small></p></div>
  </article>
  <aside class="lateral">
    <div class="caja-cita"><p class="caja-t">Pide cita en {e(C['ciudad'])}</p><p>Estudio eco-doppler en la misma visita. Sin volante.</p>{botones_contacto("btn-bloque")}<p class="caja-h">{icono("reloj","ico ico-sm")}{e(C['horario_texto'])}</p></div>
    <nav class="indice" aria-label="En esta página"><p class="caja-t">En esta página</p><ol>{indice}</ol></nav>
  </aside>
</div>
<section class="seccion seccion-crema"><div class="contenedor"><h2>Otros tratamientos relacionados</h2><div class="rejilla-serv rejilla-3">{relacionados}</div></div></section>
{banda_cta()}"""
    pagina = {"@type": "MedicalWebPage", "@id": f'{D}/{s["slug"]}/#pagina', "url": f'{D}/{s["slug"]}/',
              "name": s["h1"], "description": s["description"], "inLanguage": "es-ES", "isPartOf": {"@id": ID_WEB},
              "audience": {"@type": "Patient"}, "lastReviewed": C["fecha_revision"], "reviewedBy": {"@id": ID_MEDICO},
              "provider": {"@id": ID_CONSULTA}, "breadcrumb": m_schema}
    if s["condicion"]:
        pagina["about"] = {"@type": "MedicalCondition", "name": s["condicion"]}
    else:
        pagina["about"] = {"@type": "MedicalTest", "name": "Eco-doppler vascular"}
    schemas = [pagina, schema_consulta(), schema_medico()]
    return documento(f'/{s["slug"]}/', s["title"], s["description"], cuerpo, schemas, activo="/tratamientos/")


def pag_tratamientos():
    m_html, m_schema = migas([("Tratamientos", "/tratamientos/")])
    cuerpo = f"""<div class="cabecera-pag"><div class="contenedor">{m_html}
<h1>Tratamientos de cirugía vascular en Ciudad Real</h1>
<p class="escena">Cada página explica qué pasa por dentro, cómo se diagnostica, qué opciones hay y cuándo conviene consultar o ir a urgencias.</p></div></div>
<section class="seccion"><div class="contenedor"><div class="rejilla-serv">{''.join(tarjeta_servicio(s) for s in SERVICIOS)}</div></div></section>
{banda_cta()}"""
    schemas = [{"@type": "CollectionPage", "url": D + "/tratamientos/", "name": "Tratamientos de cirugía vascular en Ciudad Real",
                "isPartOf": {"@id": ID_WEB}, "breadcrumb": m_schema,
                "hasPart": [{"@type": "MedicalWebPage", "url": f'{D}/{s["slug"]}/', "name": s["h1"]} for s in SERVICIOS]},
               schema_consulta()]
    return documento("/tratamientos/", "Tratamientos de cirugía vascular en Ciudad Real | Varices, arterias y aorta",
                     "Todos los tratamientos de Angiología y Cirugía Vascular en Ciudad Real: varices, pie diabético, mala circulación, aneurisma de aorta, trombosis, úlceras, carótidas y eco-doppler.",
                     cuerpo, schemas, activo="/tratamientos/")


def pag_sobre_mi():
    m_html, m_schema = migas([("Sobre el doctor", "/sobre-mi/")])
    cuerpo = f"""<div class="cabecera-pag"><div class="contenedor">{m_html}</div></div>
<section class="seccion"><div class="contenedor doc-fila doc-fila-claro">
  {avatar_html('avatar avatar-grande')}
  <div>
    <p class="kicker">Quién te atiende</p>
    <h1>{e(C['nombre'])}, cirujano vascular en Ciudad Real</h1>
    <p class="doc-cargo">{e(C['titulo'])} · Especialista en {e(C['especialidad'])} · Nº col. {e(C['colegiado'])}</p>
    <p>{e(C['nombre'])} es especialista en {e(C['especialidad'])} y trabaja como cirujano vascular en el {e(C['hospital'])}. En su consulta de {e(C['ciudad'])} atiende a pacientes con varices, mala circulación, pie diabético, aneurismas y enfermedad de las carótidas, con el eco-doppler como herramienta central del diagnóstico.</p>
    <p>Su forma de trabajar parte de una idea sencilla: un paciente que entiende lo que le pasa toma mejores decisiones. Por eso dedica la consulta a explicar, con dibujos si hace falta, qué se ha visto en la ecografía, qué opciones hay y qué puede esperar de cada una.</p>
    {botones_contacto()}
  </div>
</div></section>
<section class="seccion seccion-crema"><div class="contenedor dos-col">
  <section><h2>Formación y trayectoria</h2>
    <ul class="lista-cv">
      <li><strong>[Año]</strong> Licenciatura/Grado en Medicina · [Universidad]</li>
      <li><strong>[Año]</strong> Especialidad en {e(C['especialidad'])} (MIR) · [Hospital de residencia]</li>
      <li><strong>[Año]–actualidad</strong> Cirujano vascular · {e(C['hospital'])}</li>
      <li><strong>[Año]</strong> [Máster, fellowship o formación en cirugía endovascular]</li>
      <li>Miembro de [Sociedad Española de Angiología y Cirugía Vascular (SEACV) u otras]</li>
    </ul>
  </section>
  <section><h2>Divulgación y ciencia</h2>
    <p>Además de la actividad clínica, escribe sobre medicina vascular basada en la evidencia y sobre cómo leer los estudios científicos con espíritu crítico. En redes comparte contenido para pacientes con el lema «{e(C['eslogan'])}».</p>
    <ul class="lista-cv"><li>Instagram: <a href="https://www.instagram.com/davidgarmd/" rel="noopener me">@davidgarmd</a></li>
      <li>[Publicaciones científicas destacadas: enlace a PubMed / ORCID / Google Scholar]</li></ul>
  </section>
</div></section>
{banda_cta()}"""
    perfil = {"@type": "ProfilePage", "url": D + "/sobre-mi/", "name": f'{C["nombre"]}, cirujano vascular en Ciudad Real',
              "mainEntity": {"@id": ID_MEDICO}, "isPartOf": {"@id": ID_WEB}, "breadcrumb": m_schema}
    return documento("/sobre-mi/", f'{C["nombre"]} | Cirujano vascular en Ciudad Real',
                     f'Conoce al {C["nombre"]}, especialista en Angiología y Cirugía Vascular y cirujano en el Hospital General Universitario de Ciudad Real.',
                     cuerpo, [perfil, schema_medico(), schema_consulta()], activo="/sobre-mi/", og_type="profile")


def pag_contacto():
    m_html, m_schema = migas([("Contacto", "/contacto/")])
    accion = C["formulario_action"] or f'mailto:{C["email"]}'
    enctype = "" if C["formulario_action"] else ' enctype="text/plain"'
    motivos = "".join(f"<option>{e(s['menu'])}</option>" for s in SERVICIOS) + "<option>Otro motivo</option>"
    cuerpo = f"""<div class="cabecera-pag"><div class="contenedor">{m_html}
<h1>Pedir cita con el cirujano vascular en Ciudad Real</h1>
<p class="escena">Llama, escribe por WhatsApp o déjanos tus datos y te llamamos para darte hora. No necesitas volante.</p>
{botones_contacto("btn-grande")}</div></div>
<section class="seccion"><div class="contenedor dos-col">
  <section class="tarjeta-nap tarjeta-nap-grande">
    <h2>Dónde estamos</h2>
    <p>{icono("pin")}<span><strong>{e(C['centro'])}</strong><br>{e(C['calle'])}<br>{e(C['cp'])} {e(C['ciudad'])} ({e(C['provincia'])})</span></p>
    <p>{icono("reloj")}<span>{e(C['horario_texto'])}</span></p>
    <p>{icono("tel")}<a href="tel:{e(C['telefono_enlace'])}">{e(C['telefono'])}</a></p>
    <p>{icono("mail")}<a href="mailto:{e(C['email'])}">{e(C['email'])}</a></p>
    <a class="btn btn-primario" href="{e(C['enlace_mapa'])}" rel="noopener">{icono("pin")}Abrir en Google Maps</a>
    <div class="sem sem-rojo sem-compacto"><p><strong>Si es una urgencia, no esperes a la cita:</strong> llama al 112 o acude a urgencias.</p></div>
  </section>
  <section>
    <h2>Te llamamos nosotros</h2>
    <form class="formulario" action="{e(accion)}" method="post"{enctype}>
      <label>Nombre<input name="nombre" autocomplete="name" required></label>
      <label>Teléfono<input name="telefono" type="tel" autocomplete="tel" required></label>
      <label>Motivo de la consulta<select name="motivo">{motivos}</select></label>
      <label>Mejor momento para llamarte<select name="franja"><option>Mañana</option><option>Tarde</option><option>Indiferente</option></select></label>
      <p class="nota-form">No incluyas informes ni datos clínicos en este formulario: los revisaremos contigo en consulta.</p>
      <label class="check"><input type="checkbox" name="privacidad" required> He leído y acepto la <a href="/privacidad/">política de privacidad</a>.</label>
      <button class="btn btn-primario btn-grande" type="submit">Solicitar llamada</button>
    </form>
  </section>
</div></section>"""
    schemas = [{"@type": "ContactPage", "url": D + "/contacto/", "name": "Pedir cita", "isPartOf": {"@id": ID_WEB},
                "about": {"@id": ID_CONSULTA}, "breadcrumb": m_schema}, schema_consulta()]
    return documento("/contacto/", "Pedir cita · Cirujano vascular en Ciudad Real | Teléfono y dirección",
                     "Pide cita con el cirujano vascular en Ciudad Real por teléfono, WhatsApp o formulario. Dirección, horario y cómo llegar. Sin volante.",
                     cuerpo, schemas, activo="/contacto/")


def fecha_es(iso):
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    a, m, d = iso.split("-")
    return f"{int(d)} de {meses[int(m) - 1]} de {a}"


def pag_blog():
    m_html, m_schema = migas([("Blog", "/blog/")])
    posts = "".join(f'<a class="tarjeta-blog" href="/blog/{p["slug"]}/"><time datetime="{p["fecha"]}">{fecha_es(p["fecha"])}</time><span class="tarjeta-tit">{e(p["h1"])}</span><span class="tarjeta-txt">{e(p["description"])}</span><span class="tarjeta-mas">Leer {icono("flecha","ico ico-sm")}</span></a>' for p in BLOG)
    cuerpo = f"""<div class="cabecera-pag"><div class="contenedor">{m_html}<h1>Blog de salud vascular</h1>
<p class="escena">Artículos para entender tus arterias y tus venas, escritos para pacientes.</p></div></div>
<section class="seccion"><div class="contenedor rejilla-blog">{posts}</div></section>{banda_cta()}"""
    schemas = [{"@type": "Blog", "url": D + "/blog/", "name": "Blog de salud vascular", "isPartOf": {"@id": ID_WEB},
                "breadcrumb": m_schema, "author": {"@id": ID_MEDICO}}]
    return documento("/blog/", "Blog de salud vascular | Cirujano vascular en Ciudad Real",
                     "Artículos para pacientes sobre varices, circulación, pie diabético, aneurismas y trombosis, escritos por un cirujano vascular de Ciudad Real.",
                     cuerpo, schemas, activo="/blog/")


def pag_post(p):
    m_html, m_schema = migas([("Blog", "/blog/"), (p["h1"], f'/blog/{p["slug"]}/')])
    cuerpo = f"""<div class="cabecera-pag"><div class="contenedor">{m_html}<h1>{e(p['h1'])}</h1>
<p class="meta-post">Por <a href="/sobre-mi/">{e(C['nombre'])}</a> · <time datetime="{p['fecha']}">{fecha_es(p['fecha'])}</time></p></div></div>
<div class="contenedor pag-grid"><article class="articulo">{p['cuerpo']}
<div class="revisado">{avatar_html('avatar avatar-mini')}<p>Escrito por <a href="/sobre-mi/">{e(C['nombre'])}</a>, {e(C['titulo']).lower()}.<br><small>Información educativa: no sustituye la valoración de un médico. Ante síntomas, consulta.</small></p></div></article>
<aside class="lateral"><div class="caja-cita"><p class="caja-t">¿Te has reconocido?</p><p>Pide cita con estudio eco-doppler en la misma visita.</p>{botones_contacto("btn-bloque")}</div></aside></div>
{banda_cta()}"""
    schemas = [{"@type": "BlogPosting", "@id": f'{D}/blog/{p["slug"]}/#post', "headline": p["h1"], "description": p["description"],
                "url": f'{D}/blog/{p["slug"]}/', "datePublished": p["fecha"], "dateModified": p["fecha"], "inLanguage": "es-ES",
                "author": {"@id": ID_MEDICO}, "publisher": {"@id": ID_CONSULTA},
                "image": D + "/img/og-cirujano-vascular-ciudad-real.png", "mainEntityOfPage": f'{D}/blog/{p["slug"]}/',
                "isPartOf": {"@id": ID_WEB}}, m_schema, schema_medico(), schema_consulta()]
    return documento(f'/blog/{p["slug"]}/', p["title"], p["description"], cuerpo, schemas, activo="/blog/", og_type="article")


def pag_legal(ruta, h1, html_cuerpo):
    m_html, _ = migas([(h1, ruta)])
    cuerpo = f'<div class="cabecera-pag"><div class="contenedor">{m_html}<h1>{e(h1)}</h1></div></div><div class="contenedor"><article class="articulo articulo-legal">{html_cuerpo}</article></div>'
    return documento(ruta, f'{h1} | {C["nombre"]}', f'{h1} de la web de {C["nombre"]}, cirujano vascular en Ciudad Real.', cuerpo, [], noindex=True)


AVISO_LEGAL = f"""<p class="aviso">Plantilla orientativa. Debe revisarla un profesional antes de publicar.</p>
<h2>Titular</h2><p>En cumplimiento de la Ley 34/2002 (LSSI-CE): titular {e(C['nombre_completo'])}, NIF [NIF], domicilio profesional en {e(C['calle'])}, {e(C['cp'])} {e(C['ciudad'])}. Correo: {e(C['email'])}. Teléfono: {e(C['telefono'])}.</p>
<h2>Datos profesionales</h2><p>Título: Licenciado/Graduado en Medicina, especialista en {e(C['especialidad'])}, expedido en España. Colegio profesional: Ilustre Colegio Oficial de Médicos de Ciudad Real, nº de colegiado {e(C['colegiado'])}. Normas profesionales: Código de Deontología Médica de la Organización Médica Colegial. Centro sanitario: {e(C['registro_sanitario'])}.</p>
<h2>Contenido</h2><p>La información de esta web tiene carácter divulgativo y no sustituye la consulta médica. No se ofrecen diagnósticos ni tratamientos a distancia.</p>"""

PRIVACIDAD = f"""<p class="aviso">Plantilla orientativa. Debe revisarla un profesional antes de publicar.</p>
<h2>Responsable</h2><p>{e(C['nombre_completo'])}, {e(C['calle'])}, {e(C['cp'])} {e(C['ciudad'])}. Contacto: {e(C['email'])}.</p>
<h2>Qué datos tratamos y para qué</h2><p>Los datos que envías por el formulario, teléfono, correo o WhatsApp (nombre, teléfono y motivo general) se usan solo para gestionar tu cita. Base jurídica: tu consentimiento y la aplicación de medidas precontractuales a petición tuya (art. 6.1.a y 6.1.b RGPD). La historia clínica se rige por la Ley 41/2002 de autonomía del paciente.</p>
<h2>Conservación</h2><p>Los datos de contacto se conservan el tiempo necesario para gestionar tu solicitud; la historia clínica, el plazo legal.</p>
<h2>Destinatarios</h2><p>No se ceden datos a terceros salvo obligación legal. Proveedores: [alojamiento web], [servicio de formularios], [software de gestión de citas], con contrato de encargo de tratamiento.</p>
<h2>Tus derechos</h2><p>Puedes ejercer los derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo a {e(C['email'])}, y reclamar ante la Agencia Española de Protección de Datos (aepd.es).</p>"""

COOKIES = """<p>Esta web no usa cookies propias ni de terceros, ni herramientas de analítica que rastreen a los visitantes. Las fuentes tipográficas están alojadas en el propio servidor.</p>
<p>Si en el futuro se incorpora analítica o contenido de terceros (mapas, vídeos), esta política se actualizará y se pedirá tu consentimiento antes de instalar cookies no necesarias.</p>"""


def pag_404():
    cuerpo = f"""<section class="seccion"><div class="contenedor"><p class="kicker">Error 404</p><h1>Esta página no existe</h1>
<p>Puede que la dirección haya cambiado. Estos son los tratamientos:</p><div class="rejilla-serv">{''.join(tarjeta_servicio(s) for s in SERVICIOS)}</div></div></section>"""
    return documento("/404.html", "Página no encontrada", "Página no encontrada.", cuerpo, [], noindex=True)


# ---------------------------------------------------------------------------
# Archivos auxiliares
# ---------------------------------------------------------------------------
def robots():
    return f"""# Buscadores y asistentes de IA pueden rastrear toda la web.
User-agent: *
Allow: /

# Rastreadores de búsqueda con IA (citan la web en sus respuestas)
User-agent: OAI-SearchBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

Sitemap: {D}/sitemap.xml
"""


def sitemap(rutas):
    filas = "".join(f"  <url><loc>{D}{r}</loc><lastmod>{C['fecha_revision']}</lastmod></url>\n" for r in rutas)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{filas}</urlset>\n'


def llms(rutas_serv):
    lineas = [f"# {C['nombre']} · Cirujano vascular en Ciudad Real", "",
              f"> Consulta de {C['especialidad']} en Ciudad Real (Castilla-La Mancha, España). Diagnóstico con eco-doppler y tratamiento de varices, pie diabético, enfermedad arterial periférica, aneurisma de aorta, trombosis venosa, úlceras y estenosis carotídea.",
              "", "## Tratamientos"]
    lineas += [f"- [{s['h1']}]({D}/{s['slug']}/): {s['resumen']}" for s in SERVICIOS]
    lineas += ["", "## Consulta", f"- [Sobre el doctor]({D}/sobre-mi/)", f"- [Pedir cita]({D}/contacto/)"]
    return "\n".join(lineas) + "\n"


FAVICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="11" fill="#0A2463"/><path d="M8 27c6-1 7-8 12-9s7-6 12-7" fill="none" stroke="#56CCF2" stroke-width="4" stroke-linecap="round"/></svg>'


def escribir(ruta, contenido):
    destino = SALIDA / ruta.lstrip("/")
    if ruta.endswith("/"):
        destino = destino / "index.html"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(contenido, encoding="utf-8")


def main():
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    shutil.copytree(RAIZ / "static", SALIDA)
    indexables = ["/"]
    escribir("/", pag_inicio())
    escribir("/tratamientos/", pag_tratamientos()); indexables.append("/tratamientos/")
    for s in SERVICIOS:
        escribir(f'/{s["slug"]}/', pag_servicio(s)); indexables.append(f'/{s["slug"]}/')
    escribir("/sobre-mi/", pag_sobre_mi()); indexables.append("/sobre-mi/")
    escribir("/contacto/", pag_contacto()); indexables.append("/contacto/")
    escribir("/blog/", pag_blog()); indexables.append("/blog/")
    for p in BLOG:
        escribir(f'/blog/{p["slug"]}/', pag_post(p)); indexables.append(f'/blog/{p["slug"]}/')
    escribir("/aviso-legal/", pag_legal("/aviso-legal/", "Aviso legal", AVISO_LEGAL))
    escribir("/privacidad/", pag_legal("/privacidad/", "Política de privacidad", PRIVACIDAD))
    escribir("/cookies/", pag_legal("/cookies/", "Política de cookies", COOKIES))
    escribir("/404.html", pag_404())
    escribir("/robots.txt", robots())
    escribir("/sitemap.xml", sitemap(indexables))
    escribir("/llms.txt", llms(indexables))
    escribir("/favicon.svg", FAVICON)

    pendientes = sorted({k for k, v in C.items() if es_placeholder(v)})
    print(f"Generadas {len(indexables)} páginas indexables en {SALIDA}")
    if not TIENE_AVATAR:
        print(f"AVISO: falta la foto static{AVATAR} (se muestra un monograma).")
    if pendientes:
        print("AVISO: datos pendientes en CONFIG:", ", ".join(pendientes))


if __name__ == "__main__":
    main()
