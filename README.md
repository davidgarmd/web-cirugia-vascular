# Web · Dr. David García, cirujano vascular en Ciudad Real

Web estática optimizada para SEO local, con la identidad visual de la marca @davidgarmd y la voz de la línea *Vascular para Pacientes*.

**Mundo visual: señalética hospitalaria.** El menú es un cartel colgante de pasillo; en la portada, un tótem «¿Qué notas?» lista síntomas y de cada fila sale una línea de color (un vaso con flujo) hacia su página; el mapa vascular muestra arterias (azul marino) y venas (celeste) de cuello a pies; Tratamientos es un plano «Usted está aquí». Rojo solo para urgencias. Diseño hecho con las skills de `.claude/skills/` (impeccable, taste-skill, emil-design-eng, frontend-design, ui-ux-pro-max, redesign-skill) a partir de la maqueta aprobada `.impeccable/mocks/comp-d2-hibrida.png`.

- **Análisis SEO y plan de acción:** [`ANALISIS-SEO.md`](ANALISIS-SEO.md)
- **Textos y datos:** [`contenido.py`](contenido.py) (lo único que necesitas editar)
- **Generador:** [`build.py`](build.py) → crea la carpeta `public/`, que es la web lista para subir

## Estructura de la web

| URL | Contenido |
|---|---|
| `/` | Portada: tótem «¿Qué notas?» con rutas, mapa vascular, las tres paradas de la consulta, placa del doctor, pacientes de la provincia, preguntas frecuentes |
| `/tratamientos/` | Plano «Usted está aquí»: venas, arterias, eco-doppler y urgencias |
| `/tratamiento-varices-ciudad-real/` · `/congestion-venosa-pelvica/` · `/pie-diabetico-ciudad-real/` · `/enfermedad-arterial-periferica/` · `/aneurisma-aorta-abdominal/` · `/trombosis-venosa-profunda/` · `/ulceras-vasculares-ciudad-real/` · `/estenosis-carotida/` · `/eco-doppler-ciudad-real/` | Una página por patología |
| `/sobre-mi/` · `/contacto/` · `/blog/` | Biografía, cita y artículos |
| `/aviso-legal/` · `/privacidad/` · `/cookies/` | Páginas legales (plantillas, no indexadas) |

## Antes de publicar

1. Abre `contenido.py` y rellena todo lo que va entre `[corchetes]` en `CONFIG` (colegiado, registro sanitario de la clínica, dominio). Los datos de la Clínica Cardiorreal ya están puestos: confírmalos con la clínica. Horario, coordenadas, WhatsApp y correo están vacíos y no se muestran hasta que los rellenes. Completa también la formación en la página `/sobre-mi/` (en `build.py`, función `pag_sobre_mi`).
2. Revisa que las técnicas de cada tratamiento coincidan con lo que haces de verdad en consulta.
3. Añade tu foto como `static/img/david-garcia-cirujano-vascular.jpg` (cuadrada, mínimo 640×640).
4. Si quieres formulario real, crea uno gratis en Formspree o similar y pon su URL en `formulario_action` (si lo dejas vacío, el formulario abre el correo del paciente).
5. Genera la web:

   ```bash
   python3 build.py
   ```

   El script avisa de los datos que siguen pendientes.

6. Para verla en tu ordenador: `python3 -m http.server 8000 -d public` y abre http://localhost:8000

## Publicar

`public/` es HTML puro: sirve cualquier alojamiento. Opciones gratuitas y sencillas: Cloudflare Pages, Netlify o GitHub Pages (conectando este repositorio, comando de build `python3 build.py`, carpeta de salida `public`). Compra el dominio (p. ej. `cirujanovascularciudadreal.es`) y apúntalo al alojamiento.

Después: sigue la sección 5 de `ANALISIS-SEO.md` (Google Business Profile, Search Console, reseñas, directorios).

## Añadir un artículo al blog

Añade un diccionario a la lista `BLOG` de `contenido.py` (copia el existente) y vuelve a ejecutar `python3 build.py`. El sitemap se actualiza solo.

## Imágenes

- `assets/plates/`: ilustraciones originales generadas con IA (Magnific) a partir de las maquetas aprobadas; llevan su procedencia incrustada.
- `node herramientas/optimizar.js` las convierte a WebP en `static/img/` (requiere Playwright, ya instalado en el entorno).
- **Revisa la anatomía del mapa vascular** (`static/img/mapa-vascular.webp`): es un esquema; si quieres cambiar algo, se regenera.

## Otros

- `herramientas/og.html`: plantilla de la imagen para redes (1200×630). Se renderiza con Chromium/Playwright.
- Tipografías autoalojadas (licencia SIL OFL en `static/fonts/`): Montserrat (titulares), Inter (texto) y Barlow Semi Condensed (rótulos). Iconos: Tabler Icons (MIT) en `iconos.json`.
