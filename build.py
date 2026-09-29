#!/usr/bin/env python3
"""Genera la web estática en ./public a partir de contenido.py.

Uso:  python3 build.py
Sin dependencias externas (solo biblioteca estándar de Python 3.8+).

Mundo visual: señalética hospitalaria. El paciente elige lo que nota en un tótem
y una línea de color (un vaso con flujo) le lleva a su página.
"""
import html
import json
import shutil
from pathlib import Path

from contenido import BLOG, CONFIG, FAQS_HOME, MAPA, POBLACIONES, SERVICIOS, TOTEM

RAIZ = Path(__file__).parent
SALIDA = RAIZ / "public"
C = CONFIG
D = C["dominio"].rstrip("/")
SERV = {s["slug"]: s for s in SERVICIOS}
AVATAR = "/img/david-garcia-cirujano-vascular.jpg"
TIENE_AVATAR = (RAIZ / "static" / AVATAR.lstrip("/")).exists()

# Venas y arterias: agrupa las consultas en el plano de Tratamientos
VENAS = ["tratamiento-varices-ciudad-real", "congestion-venosa-pelvica", "trombosis-venosa-profunda", "ulceras-vasculares-ciudad-real"]
ARTERIAS = ["enfermedad-arterial-periferica", "pie-diabetico-ciudad-real", "aneurisma-aorta-abdominal", "estenosis-carotida"]


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


def fecha_es(iso):
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
             "septiembre", "octubre", "noviembre", "diciembre"]
    a, m, d = iso.split("-")
    return f"{int(d)} de {meses[int(m) - 1]} de {a}"


# ---------------------------------------------------------------------------
# Iconos: Tabler Icons (MIT) + dos pictogramas propios con el mismo trazo
# ---------------------------------------------------------------------------
ICONOS = json.loads((RAIZ / "iconos.json").read_text(encoding="utf-8"))
ICONOS.update({
    # pictogramas propios, mismo trazo que Tabler
    # pierna con varices
    "vena": '<path d="M8.5 2c-.6 3.2-1 5.6-.4 8.2.5 2.2.3 4.2-.6 6.2-.8 1.8-.3 3.6 1.5 3.6h2c1.6 0 2-1.5 1.4-3-.8-2-.7-4 .2-6.3 1-2.6 1.4-5.4 1.4-8.7" /><path d="M10.3 4.5c1.2.7-.6 1.6.4 2.5s-.7 1.7.4 2.6" /><path d="M9.8 12.2c.9.6-.4 1.3.3 2" />',
    # útero y ovarios
    "pelvis": '<path d="M9 8.5h6c0 3.5-1.2 5.9-2.2 6.9V20h-1.6v-4.6C10.2 14.4 9 12 9 8.5z" /><path d="M9 9.2C7.6 8 6 7.8 5 9" /><path d="M15 9.2c1.4-1.2 3-1.4 4-.2" /><circle cx="4.6" cy="11" r="1.6" /><circle cx="19.4" cy="11" r="1.6" />',
    # pie con herida
    "pie": '<path d="M3 17.5c0-2 1.2-3.4 3.4-3.9l5.4-1.2c1.1-.3 2-.9 2.6-1.8L16 8h3v6.5c0 .9.4 1.6 1 2.1.8.7.4 2.4-.8 2.4H4.5A1.5 1.5 0 0 1 3 17.5z" /><path d="M19 8V4" /><path d="M8.5 16.2h.01" /><path d="M10.5 15.8l1-1" />',
})


def icono(nombre, cls="ico"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONOS[nombre]}</svg>')


ICONO_SERV = {
    "tratamiento-varices-ciudad-real": "vena", "congestion-venosa-pelvica": "pelvis",
    "enfermedad-arterial-periferica": "caminar", "pie-diabetico-ciudad-real": "pie",
    "aneurisma-aorta-abdominal": "aorta", "trombosis-venosa-profunda": "trombo",
    "ulceras-vasculares-ciudad-real": "herida", "estenosis-carotida": "carotida",
    "eco-doppler-ciudad-real": "eco",
}

LOGO = ('<svg class="logo-marca" viewBox="0 0 56 48" aria-hidden="true">'
        '<path d="M4 42c9-1 12-6 20-6s14-4 28-5" fill="none" stroke="#56CCF2" stroke-width="4" stroke-linecap="round"/>'
        ''
        '<text x="29" y="24" text-anchor="middle" font-family="Montserrat, sans-serif" font-weight="800" font-size="21" fill="#fff" letter-spacing="-1">DG</text>'
        '</svg>')


# ---------------------------------------------------------------------------
# Fragmentos comunes
# ---------------------------------------------------------------------------
def tel_visible():
    return "" if es_placeholder(C["telefono"]) else f'<span class="btn-extra">{e(C["telefono"])}</span>'


def botones(cls=""):
    return (f'<div class="acciones {cls}">'
            f'<a class="btn btn-navy" href="tel:{e(C["telefono_enlace"])}">{icono("tel")}<span>Llamar</span>{tel_visible()}</a>'
            f'<a class="btn btn-wa" href="https://wa.me/{e(C["whatsapp"])}" rel="noopener">{icono("wa")}<span>WhatsApp</span></a>'
            + (f'<a class="btn btn-borde" href="{e(C["enlace_reserva"])}" rel="noopener">{icono("cal")}<span>Reservar online</span></a>' if C.get("enlace_reserva") else "")
            + "</div>")


def cabecera(activo):
    items = [("/tratamientos/", "Tratamientos"), ("/eco-doppler-ciudad-real/", "Eco-doppler"),
             ("/sobre-mi/", "El doctor"), ("/blog/", "Blog")]
    actual = ' aria-current="page"'
    links = "".join(f'<li><a href="{u}"{actual if activo == u else ""}>{t}</a></li>' for u, t in items)
    return f"""<a class="saltar" href="#contenido">Saltar al contenido</a>
<header class="cartel-wrap">
  <div class="cartel">
    <a class="marca" href="/" aria-label="{e(C['nombre'])}, cirujano vascular en Ciudad Real. Inicio">{LOGO}<span>{e(C['nombre'])} <span class="marca-sep">·</span> <span class="marca-esp">Cirugía Vascular</span></span></a>
    <nav id="menu" class="nav" aria-label="Principal">
      <ul>{links}</ul>
      <a class="btn btn-celeste" href="/contacto/">Pedir cita</a>
    </nav>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu">{icono("menu", "ico ico-abrir")}{icono("cerrar", "ico ico-cerrar")}<span class="sr">Menú</span></button>
  </div>
</header>"""


def pie():
    serv = "".join(f'<li><a href="/{s["slug"]}/">{e(s["menu"])}</a></li>' for s in SERVICIOS)
    redes = "".join(f'<li><a href="{e(u)}" rel="noopener me">{e(n)}</a></li>' for n, u in C["redes"].items() if not es_placeholder(u))
    return f"""<footer class="pie">
  <div class="contenedor pie-grid">
    <div class="pie-marca">
      <p class="pie-nombre">{e(C['nombre'])}</p>
      <p>{e(C['titulo'])}<br>Especialista en {e(C['especialidad'])}<br>n.º de colegiado {e(C['colegiado'])}</p>
    </div>
    <div>
      <h2 class="pie-t">Consulta</h2>
      <address>{e(C['centro'])}<br>{e(C['calle'])}<br>{e(C['cp'])} {e(C['ciudad'])}<br>
      <a href="tel:{e(C['telefono_enlace'])}">{e(C['telefono'])}</a><br><a href="mailto:{e(C['email'])}">{e(C['email'])}</a></address>
      <p>{e(C['horario_texto'])}</p>
    </div>
    <div><h2 class="pie-t">Consultas</h2><ul>{serv}</ul></div>
    <div><h2 class="pie-t">Más</h2><ul><li><a href="/sobre-mi/">El doctor</a></li><li><a href="/blog/">Blog</a></li><li><a href="/contacto/">Pedir cita</a></li>{redes}</ul></div>
  </div>
  <div class="contenedor pie-legal">
    <p>La información de esta web es educativa y no sustituye la valoración de un médico. En caso de urgencia, llama al 112.</p>
    <p>{e(C['registro_sanitario'])} · <a href="/aviso-legal/">Aviso legal</a> · <a href="/privacidad/">Privacidad</a> · <a href="/cookies/">Cookies</a></p>
  </div>
</footer>
<nav class="barra-movil" aria-label="Contacto rápido">
  <a href="tel:{e(C['telefono_enlace'])}">{icono("tel")}Llamar</a>
  <a class="bm-wa" href="https://wa.me/{e(C['whatsapp'])}" rel="noopener">{icono("wa")}WhatsApp</a>
  <a class="bm-cita" href="/contacto/">{icono("cal")}Pedir cita</a>
</nav>
<script src="/rutas.js" defer></script>"""


def migas(lista):
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
    return ""


# ---------------------------------------------------------------------------
# Schema.org
# ---------------------------------------------------------------------------
ID_CONSULTA = D + "/#consulta"
ID_MEDICO = D + "/#medico"
ID_WEB = D + "/#web"


def schema_consulta():
    return {
        "@type": "MedicalClinic", "@id": ID_CONSULTA,
        "name": f'{C["nombre"]} · Cirugía Vascular en Ciudad Real', "url": D + "/",
        "image": D + "/img/og-cirujano-vascular-ciudad-real.png", "logo": D + "/favicon.svg",
        "telephone": "" if es_placeholder(C["telefono"]) else C["telefono_enlace"],
        "email": C["email"], "priceRange": "€€",
        "medicalSpecialty": ["https://schema.org/Cardiovascular", "https://schema.org/Surgical"],
        "address": {"@type": "PostalAddress", "streetAddress": C["calle"], "postalCode": C["cp"],
                    "addressLocality": C["ciudad"], "addressRegion": C["region"], "addressCountry": "ES"},
        "geo": {"@type": "GeoCoordinates", "latitude": float(C["lat"]), "longitude": float(C["lng"])},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": h["dias"],
                                       "opens": h["abre"], "closes": h["cierra"]} for h in C["horario_schema"]],
        "areaServed": [{"@type": "City", "name": "Ciudad Real"}, {"@type": "AdministrativeArea", "name": "Provincia de Ciudad Real"}]
                      + [{"@type": "City", "name": p} for p in POBLACIONES],
        "hasMap": C["enlace_mapa"],
        "availableService": [{"@type": "MedicalTest" if s["condicion"] is None else "MedicalTherapy",
                              "name": s["h1"], "url": f'{D}/{s["slug"]}/'} for s in SERVICIOS],
        "employee": {"@id": ID_MEDICO},
    }


def schema_medico():
    return {
        "@type": "Person", "@id": ID_MEDICO, "name": C["nombre"], "honorificPrefix": "Dr.",
        "jobTitle": C["titulo"], "description": f'Especialista en {C["especialidad"]} en Ciudad Real.',
        "url": D + "/sobre-mi/", "image": D + AVATAR if TIENE_AVATAR else "",
        "worksFor": {"@id": ID_CONSULTA}, "affiliation": {"@type": "Hospital", "name": C["hospital"]},
        "hasOccupation": {"@type": "Occupation", "name": "Cirujano vascular",
                          "occupationLocation": {"@type": "City", "name": "Ciudad Real"}},
        "knowsAbout": [s["condicion"] for s in SERVICIOS if s["condicion"]] + ["Eco-doppler vascular", "Cirugía endovascular"],
        "sameAs": list(C["redes"].values()),
    }


def schema_web():
    return {"@type": "WebSite", "@id": ID_WEB, "url": D + "/", "name": f'{C["nombre"]} · Cirujano vascular en Ciudad Real',
            "inLanguage": "es-ES", "publisher": {"@id": ID_CONSULTA}}


# ---------------------------------------------------------------------------
# Plantilla base
# ---------------------------------------------------------------------------
def documento(ruta, title, description, cuerpo, schemas, activo="", og_type="website", noindex=False, clase=""):
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
<link rel="preload" href="/fonts/montserrat-800.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/barlow-sc-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/estilos.css">
<script type="application/ld+json">{json.dumps(grafo, ensure_ascii=False)}</script>
</head>
<body class="{clase}">
{cabecera(activo)}
<main id="contenido">
{cuerpo}
</main>
{pie()}
</body>
</html>
"""


def bloque_faq(faqs, titulo="Preguntas frecuentes", id_="faq"):
    return (f'<section class="faq" aria-labelledby="{id_}"><h2 id="{id_}">{titulo}</h2>' +
            "".join(f'<details><summary>{e(p)}</summary><p>{e(r)}</p></details>' for p, r in faqs) + "</section>")


def placa(s, cls=""):
    """Placa de puerta: enlace a una consulta."""
    return (f'<a class="placa {cls}" href="/{s["slug"]}/">{icono(ICONO_SERV[s["slug"]])}'
            f'<span class="placa-t">{e(s["menu"])}</span><span class="placa-r">{e(s["resumen"])}</span></a>')


def banda_final():
    return f"""<section class="final"><div class="contenedor final-fila">
<h2>¿Hablamos de lo que notas?</h2>
<p>Consulta en {e(C['ciudad'])} con eco-doppler en la misma visita. Sin volante.</p>
{botones()}</div></section>"""


# ---------------------------------------------------------------------------
# Portada
# ---------------------------------------------------------------------------
def totem_html():
    filas = []
    for i, (nota, destino, slug, ico, urgente) in enumerate(TOTEM):
        cls = "fila fila-urgente" if urgente else "fila"
        filas.append(f'<li><a class="{cls}" href="/{slug}/" data-ruta="{i}">{icono(ico, "ico fila-ico")}'
                     f'<span class="fila-txt"><span class="fila-t">{e(nota)}</span><span class="fila-d">{e(destino)}</span></span>'
                     f'{icono("flecha", "ico fila-flecha")}</a></li>')
    return (f'<nav class="totem" aria-labelledby="totem-t"><h2 id="totem-t">¿Qué notas?</h2>'
            f'<ol class="totem-filas">{"".join(filas)}</ol><div class="totem-plinto" aria-hidden="true"></div></nav>')


def mapa_html():
    notas = "".join(
        f'<li class="nota nota-{tipo}" style="--y:{y}%"><a href="/{slug}/">{e(txt)}</a></li>'
        for txt, slug, tipo, y in MAPA)
    return f"""<section class="mapa" aria-labelledby="mapa-t">
  <div class="contenedor mapa-grid">
    <div class="mapa-texto">
      <h2 id="mapa-t">De cuello a pies, arterias y venas</h2>
      <p>Un cirujano vascular se ocupa de todo el recorrido de la sangre fuera del corazón y del cerebro. Señala en el mapa la zona que te preocupa.</p>
      <ul class="leyenda" aria-label="Leyenda"><li class="ley-arteria">Arterias</li><li class="ley-vena">Venas</li></ul>
    </div>
    <figure class="mapa-fig">
      <img src="/img/mapa-vascular.webp" width="700" height="1050" alt="Dibujo del cuerpo de cuello a pies con las arterias principales en azul marino y las venas en celeste" decoding="async">
      <ol class="mapa-notas">{notas}</ol>
    </figure>
  </div>
</section>"""


def pag_inicio():
    pueblos = "".join(f"<li>{e(p)}</li>" for p in POBLACIONES)
    post = BLOG[0]
    cuerpo = f"""
<section class="hero" data-rutas>
  <div class="hero-grid">
    <div class="hero-copy">
      <h1>Cirujano vascular en Ciudad Real</h1>
      <p class="hero-sub">Varices, congestión pélvica y mala circulación. Eco-doppler en la misma visita.</p>
      {botones("acciones-hero")}
    </div>
    <img class="hero-mujer" src="/img/mujer-caminando.webp" width="500" height="750" alt="" decoding="async" fetchpriority="high">
    {totem_html()}
    <svg class="rutas" aria-hidden="true" focusable="false"></svg>
    <div class="suelo" aria-hidden="true"></div>
  </div>
</section>

{mapa_html()}

<section class="consulta" aria-labelledby="consulta-t">
  <div class="contenedor">
    <h2 id="consulta-t">Una sola visita, tres paradas</h2>
    <ol class="paradas">
      <li><span class="parada-n" aria-hidden="true">1</span><h3>Te escucha y te explora</h3><p>Qué notas, desde cuándo y qué te preocupa. Trae informes y la lista de tu medicación.</p></li>
      <li><span class="parada-n" aria-hidden="true">2</span><h3>Eco-doppler en el momento</h3><p>La <a href="/eco-doppler-ciudad-real/">ecografía vascular</a> la hace el propio cirujano. Sin radiación ni pinchazos.</p></li>
      <li><span class="parada-n" aria-hidden="true">3</span><h3>Sales con un plan</h3><p>Qué tienes, qué opciones hay y cuál encaja contigo, explicado claro y por escrito.</p></li>
    </ol>
  </div>
</section>

<section class="doctor" aria-labelledby="doctor-t">
  <div class="contenedor doctor-grid">
    <div class="placa-puerta">
      <h2 id="doctor-t">{e(C['nombre'])}</h2>
      <p class="pp-esp">Angiología y Cirugía Vascular</p>
      <p class="pp-col">Cirujano vascular y endovascular · n.º col. {e(C['colegiado'])}</p>
    </div>
    <div class="doctor-texto">
      <p class="doctor-lead">El mismo cirujano vascular del {e(C['hospital'])}, también en consulta privada.</p>
      <ul class="doctor-puntos">
        <li><strong>Especialista vía MIR en Angiología y Cirugía Vascular</strong>, con formación endovascular: técnicas mínimamente invasivas y cirugía compleja.</li>
        <li><strong>Centrado en la insuficiencia venosa crónica</strong> y la congestión venosa pélvica.</li>
        <li><strong>Diagnóstico en una visita</strong>, con el eco-doppler hecho por él mismo.</li>
        <li><strong>Te lo explica claro</strong>: divulga salud vascular como <a href="https://www.instagram.com/davidgarmd/" rel="noopener">@davidgarmd</a>.</li>
      </ul>
      <a class="enlace-flecha" href="/sobre-mi/">Conoce al doctor {icono("flecha", "ico ico-sm")}</a>
    </div>
  </div>
</section>

<section class="provincia" aria-labelledby="prov-t">
  <div class="contenedor">
    <h2 id="prov-t">Pacientes de toda la provincia</h2>
    <p class="prov-sub">La consulta está en {e(C['ciudad'])} capital. Llegan pacientes de:</p>
    <ol class="linea-pueblos">{pueblos}<li class="destino">{e(C['ciudad'])}</li></ol>
    <div class="nap">
      <p>{icono("pin")}<span><strong>{e(C['centro'])}</strong><br>{e(C['calle'])}, {e(C['cp'])} {e(C['ciudad'])}</span></p>
      <p>{icono("reloj")}<span>{e(C['horario_texto'])}</span></p>
      <p>{icono("tel")}<a href="tel:{e(C['telefono_enlace'])}">{e(C['telefono'])}</a></p>
      <a class="enlace-flecha" href="{e(C['enlace_mapa'])}" rel="noopener">Cómo llegar {icono("flecha", "ico ico-sm")}</a>
    </div>
  </div>
</section>

<section class="preguntas">
  <div class="contenedor preguntas-grid">
    {bloque_faq(FAQS_HOME)}
    <aside class="blog-destacado" aria-labelledby="blog-t">
      <h2 id="blog-t">Para leer con calma</h2>
      <a class="articulo-enlace" href="/blog/{post['slug']}/"><span class="ae-t">{e(post['h1'])}</span><span class="ae-d">{e(post['description'])}</span><span class="enlace-flecha">Leer {icono("flecha", "ico ico-sm")}</span></a>
    </aside>
  </div>
</section>
{banda_final()}"""
    schemas = [schema_web(), schema_consulta(), schema_medico(),
               {"@type": "WebPage", "@id": D + "/#pagina", "url": D + "/", "name": "Cirujano vascular en Ciudad Real",
                "isPartOf": {"@id": ID_WEB}, "about": {"@id": ID_CONSULTA}, "inLanguage": "es-ES"}]
    return documento("/", f'Cirujano vascular en Ciudad Real | {C["nombre"]}',
                     "Cirujano vascular en Ciudad Real: varices, congestión pélvica, mala circulación, pie diabético, aneurismas y carótidas. Eco-doppler en la misma consulta. Sin volante.",
                     cuerpo, schemas, activo="/", clase="p-inicio")


# ---------------------------------------------------------------------------
# Páginas de consulta
# ---------------------------------------------------------------------------
def cabecera_puerta(s, m_html):
    return f"""<div class="entrada"><div class="contenedor">
  {m_html}
  <div class="entrada-grid">
    <div>
      <div class="puerta">
        <span class="puerta-ico">{icono(ICONO_SERV[s['slug']])}</span>
        <h1>{e(s['h1'])}</h1>
      </div>
      <p class="escena">{e(s['escena'])}</p>
    </div>
    <div class="caja-cita"><h2 class="caja-t">Pide cita en {e(C['ciudad'])}</h2><p>Eco-doppler en la misma visita. Sin volante.</p>{botones("acciones-col")}<p class="caja-h">{icono("reloj", "ico ico-sm")}{e(C['horario_texto'])}</p></div>
  </div>
</div></div>"""


def directorio(slugs, titulo):
    filas = "".join(
        f'<li><a class="fila" href="/{x}/">{icono(ICONO_SERV[x], "ico fila-ico")}<span class="fila-txt"><span class="fila-t">{e(SERV[x]["menu"])}</span>'
        f'<span class="fila-d">{e(SERV[x]["resumen"])}</span></span>{icono("flecha", "ico fila-flecha")}</a></li>' for x in slugs)
    return f'<nav class="totem totem-lista" aria-labelledby="dir-t"><h2 id="dir-t">{e(titulo)}</h2><ol class="totem-filas">{filas}</ol></nav>'


def pag_servicio(s):
    m_html, m_schema = migas([("Tratamientos", "/tratamientos/"), (s["menu"], f'/{s["slug"]}/')])
    secciones = "".join(f'<section><h2 id="s{i}">{e(t)}</h2>{h}</section>' for i, (t, h) in enumerate(s["secciones"]))
    indice = "".join(f'<li><a href="#s{i}">{e(t)}</a></li>' for i, (t, _) in enumerate(s["secciones"]))
    mitos = ""
    if s.get("mitos"):
        mitos = ('<section><h2 id="mitos">Lo que se oye y lo que pasa</h2><dl class="mitos">' + "".join(
            f'<div class="mito"><dt>«{e(m)}»</dt><dd>{e(r)}</dd></div>' for m, r in s["mitos"]) + "</dl></section>")
        indice += '<li><a href="#mitos">Lo que se oye y lo que pasa</a></li>'
    consultar = ('<section><h2 id="cuando">Cuándo consultar</h2><div class="avisos">'
                 f'<div class="aviso-panel aviso-cita"><h3>{icono("cal")}Pide cita si…</h3><ul>' +
                 "".join(f"<li>{e(x)}</li>" for x in s["pide_cita"]) + "</ul></div>")
    if s.get("urgencia"):
        consultar += f'<div class="aviso-panel aviso-urgente"><h3>{icono("alarma")}Esto es de urgencias</h3><p>{e(s["urgencia"])}</p></div>'
    consultar += "</div></section>"
    indice += '<li><a href="#cuando">Cuándo consultar</a></li><li><a href="#faq">Preguntas frecuentes</a></li>'
    relacionados = directorio(s["relacionados"], "Otras consultas en esta planta")
    cuerpo = f"""{cabecera_puerta(s, m_html)}
<div class="contenedor pag-grid">
  <article class="articulo">
    <div class="en-pocas"><h2 class="en-pocas-t">En pocas palabras</h2><p>{e(s['respuesta'])}</p></div>
    {secciones}
    {mitos}
    {consultar}
    {bloque_faq(s['faqs'])}
    <div class="llevar"><h2 class="llevar-t">Para llevar a casa</h2><p>{e(s['llevar'])}</p></div>
    <p class="revisado">Revisado por <a href="/sobre-mi/">{e(C['nombre'])}</a>, {e(C['titulo']).lower()}. Última revisión: <time datetime="{C['fecha_revision']}">{fecha_es(C['fecha_revision'])}</time>. Información educativa: no sustituye la valoración de un médico.</p>
  </article>
  <aside class="lateral">
    <nav class="indice" aria-label="En esta página"><h2 class="caja-t">En esta página</h2><ol>{indice}</ol></nav>
  </aside>
</div>
<section class="otras"><div class="contenedor">{relacionados}</div></section>
{banda_final()}"""
    pagina = {"@type": "MedicalWebPage", "@id": f'{D}/{s["slug"]}/#pagina', "url": f'{D}/{s["slug"]}/',
              "name": s["h1"], "description": s["description"], "inLanguage": "es-ES", "isPartOf": {"@id": ID_WEB},
              "audience": {"@type": "Patient"}, "lastReviewed": C["fecha_revision"], "reviewedBy": {"@id": ID_MEDICO},
              "provider": {"@id": ID_CONSULTA}, "breadcrumb": m_schema,
              "about": {"@type": "MedicalCondition", "name": s["condicion"]} if s["condicion"] else {"@type": "MedicalTest", "name": "Eco-doppler vascular"}}
    return documento(f'/{s["slug"]}/', s["title"], s["description"], cuerpo, [pagina, schema_consulta(), schema_medico()],
                     activo="/eco-doppler-ciudad-real/" if s["slug"] == "eco-doppler-ciudad-real" else "/tratamientos/")


def pag_tratamientos():
    m_html, m_schema = migas([("Tratamientos", "/tratamientos/")])

    def sala(slug, grupo):
        s = SERV[slug]
        return (f'<li><a class="sala sala-{grupo}" href="/{slug}/" data-sala="{grupo}">{icono(ICONO_SERV[slug])}'
                f'<span>{e(s["menu"])}</span></a></li>')

    venas = "".join(sala(x, "vena") for x in VENAS)
    arterias = "".join(sala(x, "arteria") for x in ARTERIAS)
    cuerpo = f"""<div class="entrada"><div class="contenedor">{m_html}
<h1 class="h1-plano">Tratamientos de cirugía vascular en Ciudad Real</h1>
<p class="escena">Si ya sabes lo que tienes, busca tu consulta en el plano. Si no lo sabes, empieza por <a href="/#totem-t">lo que notas</a>.</p></div></div>
<section class="plano-wrap"><div class="contenedor">
  <div class="plano" data-plano>
    <div class="ala ala-venas"><h2>Venas</h2><ul>{venas}</ul></div>
    <div class="ala-centro">
      <a class="sala sala-eco" href="/eco-doppler-ciudad-real/" data-sala="centro">{icono("eco")}<span>Eco-doppler</span></a>
    </div>
    <div class="ala ala-arterias"><h2>Arterias</h2><ul>{arterias}</ul></div>
    <div class="plano-base">
      <a class="sala sala-urgente" href="/trombosis-venosa-profunda/" data-sala="urgente">{icono("alarma")}<span>Urgencias: pierna hinchada o fría de golpe</span></a>
      <p class="aqui"><span class="aqui-punto" aria-hidden="true"></span>Estás aquí</p>
    </div>
    <svg class="plano-rutas" aria-hidden="true" focusable="false"></svg>
    <ul class="plano-leyenda" aria-label="Leyenda"><li class="ley-vena">Venas</li><li class="ley-arteria-b">Arterias</li><li class="ley-urgente">Urgencias</li></ul>
  </div>
</div></section>
{banda_final()}"""
    schemas = [{"@type": "CollectionPage", "url": D + "/tratamientos/", "name": "Tratamientos de cirugía vascular en Ciudad Real",
                "isPartOf": {"@id": ID_WEB}, "breadcrumb": m_schema,
                "hasPart": [{"@type": "MedicalWebPage", "url": f'{D}/{s["slug"]}/', "name": s["h1"]} for s in SERVICIOS]},
               schema_consulta()]
    return documento("/tratamientos/", "Tratamientos de cirugía vascular en Ciudad Real | Venas y arterias",
                     "Todas las consultas de Angiología y Cirugía Vascular en Ciudad Real: varices, congestión pélvica, trombosis, úlceras, mala circulación, pie diabético, aneurisma de aorta, carótidas y eco-doppler.",
                     cuerpo, schemas, activo="/tratamientos/")


def pag_sobre_mi():
    m_html, m_schema = migas([("El doctor", "/sobre-mi/")])
    foto = avatar_html("foto-doctor")
    cuerpo = f"""<div class="entrada"><div class="contenedor">{m_html}
  <div class="doctor-grid doctor-grid-pag">
    <div class="placa-puerta">
      <h1>{e(C['nombre'])}, cirujano vascular en Ciudad Real</h1>
      <p class="pp-esp">Angiología y Cirugía Vascular</p>
      <p class="pp-col">Cirujano vascular y endovascular · n.º col. {e(C['colegiado'])}</p>
    </div>
    {foto}
  </div>
</div></div>
<div class="contenedor texto-largo">
  <p class="doctor-lead">{e(C['nombre'])} es especialista en {e(C['especialidad'])} y trabaja como cirujano vascular en el {e(C['hospital'])}. En su consulta de {e(C['ciudad'])} atiende varices, congestión venosa pélvica, mala circulación, pie diabético, aneurismas y enfermedad de las carótidas.</p>
  <p>Maneja tanto las técnicas mínimamente invasivas (ablación endovenosa, escleroterapia, embolización y procedimientos endovasculares) como la cirugía abierta compleja, y dedica una atención especial a la insuficiencia venosa crónica y a la congestión venosa pélvica. El eco-doppler lo hace él mismo en la consulta: quien interpreta la prueba es quien propone el tratamiento.</p>
  <p>Parte de una idea sencilla: un paciente que entiende lo que le pasa decide mejor. Por eso la consulta se dedica a explicar, con dibujos si hace falta, qué se ha visto y qué opciones hay.</p>
  {botones()}
  <h2>Formación y trayectoria</h2>
  <ul class="lista-cv">
    <li><strong>[Año]</strong> Licenciatura o Grado en Medicina, [Universidad]</li>
    <li><strong>[Año]</strong> Especialidad en {e(C['especialidad'])} (MIR), [Hospital de residencia]</li>
    <li><strong>[Año] a hoy</strong> Cirujano vascular, {e(C['hospital'])}</li>
    <li><strong>[Año]</strong> [Formación en cirugía endovascular o congestión pélvica]</li>
    <li>Miembro de [Sociedad Española de Angiología y Cirugía Vascular (SEACV) u otras]</li>
  </ul>
  <h2>Divulgación</h2>
  <p>Escribe sobre medicina vascular basada en la evidencia y explica salud vascular a pacientes con el lema «{e(C['eslogan'])}». Instagram: <a href="https://www.instagram.com/davidgarmd/" rel="noopener me">@davidgarmd</a>.</p>
</div>
{banda_final()}"""
    perfil = {"@type": "ProfilePage", "url": D + "/sobre-mi/", "name": f'{C["nombre"]}, cirujano vascular en Ciudad Real',
              "mainEntity": {"@id": ID_MEDICO}, "isPartOf": {"@id": ID_WEB}, "breadcrumb": m_schema}
    return documento("/sobre-mi/", f'{C["nombre"]} | Cirujano vascular en Ciudad Real',
                     f'{C["nombre"]}, especialista en Angiología y Cirugía Vascular y Endovascular en Ciudad Real. Insuficiencia venosa, congestión pélvica y cirugía endovascular.',
                     cuerpo, [perfil, schema_medico(), schema_consulta()], activo="/sobre-mi/", og_type="profile")


def pag_contacto():
    m_html, m_schema = migas([("Pedir cita", "/contacto/")])
    accion = C["formulario_action"] or f'mailto:{C["email"]}'
    enctype = "" if C["formulario_action"] else ' enctype="text/plain"'
    motivos = "".join(f"<option>{e(s['menu'])}</option>" for s in SERVICIOS) + "<option>Otro motivo</option>"
    cuerpo = f"""<div class="entrada"><div class="contenedor">{m_html}
<h1 class="h1-plano">Pedir cita con el cirujano vascular en Ciudad Real</h1>
<p class="escena">Llama, escribe por WhatsApp o déjanos tus datos y te llamamos para darte hora. No necesitas volante.</p>
{botones()}</div></div>
<section class="contacto"><div class="contenedor contacto-grid">
  <div class="nap nap-grande">
    <h2>Dónde está la consulta</h2>
    <p>{icono("pin")}<span><strong>{e(C['centro'])}</strong><br>{e(C['calle'])}<br>{e(C['cp'])} {e(C['ciudad'])} ({e(C['provincia'])})</span></p>
    <p>{icono("reloj")}<span>{e(C['horario_texto'])}</span></p>
    <p>{icono("tel")}<a href="tel:{e(C['telefono_enlace'])}">{e(C['telefono'])}</a></p>
    <p>{icono("mail")}<a href="mailto:{e(C['email'])}">{e(C['email'])}</a></p>
    <a class="enlace-flecha" href="{e(C['enlace_mapa'])}" rel="noopener">Abrir en Google Maps {icono("flecha", "ico ico-sm")}</a>
    <div class="aviso-panel aviso-urgente aviso-mini"><p><strong>Si es una urgencia, no esperes a la cita:</strong> llama al 112 o acude a urgencias.</p></div>
  </div>
  <form class="formulario" action="{e(accion)}" method="post"{enctype}>
    <h2>Te llamamos</h2>
    <label for="f-nombre">Nombre</label><input id="f-nombre" name="nombre" autocomplete="name" required>
    <label for="f-tel">Teléfono</label><input id="f-tel" name="telefono" type="tel" autocomplete="tel" required>
    <label for="f-motivo">Motivo de la consulta</label><select id="f-motivo" name="motivo">{motivos}</select>
    <label for="f-franja">Mejor momento para llamarte</label><select id="f-franja" name="franja"><option>Mañana</option><option>Tarde</option><option>Indiferente</option></select>
    <p class="nota-form">No incluyas informes ni datos clínicos: los vemos contigo en la consulta.</p>
    <label class="check"><input type="checkbox" name="privacidad" required> He leído y acepto la <a href="/privacidad/">política de privacidad</a>.</label>
    <button class="btn btn-navy" type="submit">Solicitar llamada</button>
  </form>
</div></section>"""
    schemas = [{"@type": "ContactPage", "url": D + "/contacto/", "name": "Pedir cita", "isPartOf": {"@id": ID_WEB},
                "about": {"@id": ID_CONSULTA}, "breadcrumb": m_schema}, schema_consulta()]
    return documento("/contacto/", "Pedir cita con el cirujano vascular en Ciudad Real | Teléfono y dirección",
                     "Pide cita con el cirujano vascular en Ciudad Real por teléfono, WhatsApp o formulario. Dirección, horario y cómo llegar. Sin volante.",
                     cuerpo, schemas, activo="/contacto/")


def pag_blog():
    m_html, m_schema = migas([("Blog", "/blog/")])
    posts = "".join(f'<li><a class="articulo-enlace" href="/blog/{p["slug"]}/"><time datetime="{p["fecha"]}">{fecha_es(p["fecha"])}</time><span class="ae-t">{e(p["h1"])}</span><span class="ae-d">{e(p["description"])}</span></a></li>' for p in BLOG)
    cuerpo = f"""<div class="entrada"><div class="contenedor">{m_html}<h1 class="h1-plano">Blog de salud vascular</h1>
<p class="escena">Artículos para entender tus arterias y tus venas, escritos para pacientes.</p></div></div>
<section class="contenedor lista-blog"><ul>{posts}</ul></section>{banda_final()}"""
    schemas = [{"@type": "Blog", "url": D + "/blog/", "name": "Blog de salud vascular", "isPartOf": {"@id": ID_WEB},
                "breadcrumb": m_schema, "author": {"@id": ID_MEDICO}}]
    return documento("/blog/", "Blog de salud vascular | Cirujano vascular en Ciudad Real",
                     "Artículos para pacientes sobre varices, congestión pélvica, circulación, pie diabético, aneurismas y trombosis, escritos por un cirujano vascular de Ciudad Real.",
                     cuerpo, schemas, activo="/blog/")


def pag_post(p):
    m_html, m_schema = migas([("Blog", "/blog/"), (p["h1"], f'/blog/{p["slug"]}/')])
    cuerpo = f"""<div class="entrada"><div class="contenedor">{m_html}<h1 class="h1-plano">{e(p['h1'])}</h1>
<p class="meta-post">Por <a href="/sobre-mi/">{e(C['nombre'])}</a>, <time datetime="{p['fecha']}">{fecha_es(p['fecha'])}</time></p></div></div>
<div class="contenedor pag-grid"><article class="articulo">{p['cuerpo']}
<p class="revisado">Escrito por <a href="/sobre-mi/">{e(C['nombre'])}</a>, {e(C['titulo']).lower()}. Información educativa: no sustituye la valoración de un médico.</p></article>
<aside class="lateral"><div class="caja-cita"><h2 class="caja-t">¿Te has reconocido?</h2><p>Pide cita con eco-doppler en la misma visita.</p>{botones("acciones-col")}</div></aside></div>
{banda_final()}"""
    schemas = [{"@type": "BlogPosting", "@id": f'{D}/blog/{p["slug"]}/#post', "headline": p["h1"], "description": p["description"],
                "url": f'{D}/blog/{p["slug"]}/', "datePublished": p["fecha"], "dateModified": p["fecha"], "inLanguage": "es-ES",
                "author": {"@id": ID_MEDICO}, "publisher": {"@id": ID_CONSULTA},
                "image": D + "/img/og-cirujano-vascular-ciudad-real.png", "mainEntityOfPage": f'{D}/blog/{p["slug"]}/',
                "isPartOf": {"@id": ID_WEB}}, m_schema, schema_medico(), schema_consulta()]
    return documento(f'/blog/{p["slug"]}/', p["title"], p["description"], cuerpo, schemas, activo="/blog/", og_type="article")


def pag_legal(ruta, h1, html_cuerpo):
    m_html, _ = migas([(h1, ruta)])
    cuerpo = f'<div class="entrada"><div class="contenedor">{m_html}<h1 class="h1-plano">{e(h1)}</h1></div></div><div class="contenedor texto-largo">{html_cuerpo}</div>'
    return documento(ruta, f'{h1} | {C["nombre"]}', f'{h1} de la web de {C["nombre"]}, cirujano vascular en Ciudad Real.', cuerpo, [], noindex=True)


AVISO_LEGAL = f"""<p class="nota-plantilla">Plantilla orientativa. Debe revisarla un profesional antes de publicar.</p>
<h2>Titular</h2><p>En cumplimiento de la Ley 34/2002 (LSSI-CE): titular {e(C['nombre_completo'])}, NIF [NIF], domicilio profesional en {e(C['calle'])}, {e(C['cp'])} {e(C['ciudad'])}. Correo: {e(C['email'])}. Teléfono: {e(C['telefono'])}.</p>
<h2>Datos profesionales</h2><p>Título: Licenciado o Graduado en Medicina, especialista en {e(C['especialidad'])}, expedido en España. Colegio profesional: Ilustre Colegio Oficial de Médicos de Ciudad Real, nº de colegiado {e(C['colegiado'])}. Normas profesionales: Código de Deontología Médica. Centro sanitario: {e(C['registro_sanitario'])}.</p>
<h2>Contenido</h2><p>La información de esta web tiene carácter divulgativo y no sustituye la consulta médica. No se ofrecen diagnósticos ni tratamientos a distancia.</p>"""

PRIVACIDAD = f"""<p class="nota-plantilla">Plantilla orientativa. Debe revisarla un profesional antes de publicar.</p>
<h2>Responsable</h2><p>{e(C['nombre_completo'])}, {e(C['calle'])}, {e(C['cp'])} {e(C['ciudad'])}. Contacto: {e(C['email'])}.</p>
<h2>Qué datos tratamos y para qué</h2><p>Los datos que envías por el formulario, teléfono, correo o WhatsApp (nombre, teléfono y motivo general) se usan solo para gestionar tu cita. Base jurídica: tu consentimiento y la aplicación de medidas precontractuales a petición tuya (art. 6.1.a y 6.1.b RGPD). La historia clínica se rige por la Ley 41/2002 de autonomía del paciente.</p>
<h2>Conservación</h2><p>Los datos de contacto se conservan el tiempo necesario para gestionar tu solicitud; la historia clínica, el plazo legal.</p>
<h2>Destinatarios</h2><p>No se ceden datos a terceros salvo obligación legal. Proveedores: [alojamiento web], [servicio de formularios], [software de gestión de citas], con contrato de encargo de tratamiento.</p>
<h2>Tus derechos</h2><p>Puedes ejercer los derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo a {e(C['email'])}, y reclamar ante la Agencia Española de Protección de Datos (aepd.es).</p>"""

COOKIES = """<p>Esta web no usa cookies propias ni de terceros, ni herramientas de analítica que rastreen a los visitantes. Las fuentes tipográficas están alojadas en el propio servidor.</p>
<p>Si en el futuro se incorpora analítica o contenido de terceros (mapas, vídeos), esta política se actualizará y se pedirá tu consentimiento antes de instalar cookies no necesarias.</p>"""


def pag_404():
    cuerpo = f"""<div class="entrada"><div class="contenedor"><h1 class="h1-plano">Esta puerta no lleva a ningún sitio</h1>
<p class="escena">Puede que la dirección haya cambiado. Vuelve al <a href="/tratamientos/">plano de consultas</a> o a la <a href="/">entrada</a>.</p></div></div>"""
    return documento("/404.html", "Página no encontrada", "Página no encontrada.", cuerpo, [], noindex=True)


# ---------------------------------------------------------------------------
# Archivos auxiliares
# ---------------------------------------------------------------------------
def robots():
    return f"""User-agent: *
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


def llms():
    lineas = [f"# {C['nombre']}, cirujano vascular en Ciudad Real", "",
              f"> Consulta de {C['especialidad']} en Ciudad Real (Castilla-La Mancha, España). Diagnóstico con eco-doppler y tratamiento de varices, congestión venosa pélvica, enfermedad arterial periférica, pie diabético, aneurisma de aorta, trombosis venosa, úlceras y estenosis carotídea.",
              "", "## Consultas"]
    lineas += [f"- [{s['h1']}]({D}/{s['slug']}/): {s['resumen']}" for s in SERVICIOS]
    lineas += ["", "## Consulta", f"- [El doctor]({D}/sobre-mi/)", f"- [Pedir cita]({D}/contacto/)"]
    return "\n".join(lineas) + "\n"


FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="10" fill="#0A2463"/>'
           '<path d="M9 31c5-1 6-9 11-10s7-7 11-8" fill="none" stroke="#56CCF2" stroke-width="4.5" stroke-linecap="round"/></svg>')


def escribir(ruta, contenido):
    destino = SALIDA / ruta.lstrip("/")
    if ruta.endswith("/"):
        destino = destino / "index.html"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(contenido, encoding="utf-8")


def main():
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    shutil.copytree(RAIZ / "static", SALIDA, ignore=shutil.ignore_patterns("*.json"))
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
    escribir("/llms.txt", llms())
    escribir("/favicon.svg", FAVICON)

    pendientes = sorted({k for k, v in C.items() if es_placeholder(v)})
    print(f"Generadas {len(indexables)} páginas indexables en {SALIDA}")
    if not TIENE_AVATAR:
        print(f"AVISO: falta la foto static{AVATAR} (la página del doctor se muestra sin foto).")
    if pendientes:
        print("AVISO: datos pendientes en CONFIG:", ", ".join(pendientes))


if __name__ == "__main__":
    main()
