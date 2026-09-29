---
name: Dr. David García · Cirugía Vascular
description: Hospital wayfinding for a vascular surgery practice in Ciudad Real; name what you feel, follow the line, call.
colors:
  navy: "#0A2463"
  navy-hover: "#123285"
  navy-deep: "#061A4A"
  light-blue: "#56CCF2"
  light-blue-hover: "#7AD8F6"
  light-blue-ink: "#0E6E96"
  light-blue-veil: "#E6F6FC"
  urgent-red: "#EB5757"
  urgent-red-hover: "#DC4848"
  urgent-red-ink: "#B3261E"
  urgent-red-veil: "#FDEDEC"
  whatsapp-green: "#187A43"
  whatsapp-green-hover: "#136636"
  ink: "#15204A"
  ink-soft: "#46507A"
  hairline: "#DADDE6"
  floor: "#F4F6F5"
  wall: "#FFFFFF"
typography:
  display:
    fontFamily: "Montserrat, Inter, system-ui, sans-serif"
    fontSize: "clamp(2.5rem, 5.25vw, 5.1rem)"
    fontWeight: 800
    lineHeight: 1.02
    letterSpacing: "-0.03em"
  headline:
    fontFamily: "Montserrat, Inter, system-ui, sans-serif"
    fontSize: "clamp(1.7rem, 3.2vw, 2.5rem)"
    fontWeight: 800
    lineHeight: 1.08
    letterSpacing: "-0.015em"
  title:
    fontFamily: "Montserrat, Inter, system-ui, sans-serif"
    fontSize: "1.2rem"
    fontWeight: 800
    lineHeight: 1.25
    letterSpacing: "-0.015em"
  sign:
    fontFamily: "Barlow Semi Condensed, Arial Narrow, system-ui, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 700
    lineHeight: 1.1
  sign-row:
    fontFamily: "Barlow Semi Condensed, Arial Narrow, system-ui, sans-serif"
    fontSize: "clamp(1.15rem, 1.8vw, 1.75rem)"
    fontWeight: 700
    lineHeight: 1.04
  sign-sub:
    fontFamily: "Barlow Semi Condensed, Arial Narrow, system-ui, sans-serif"
    fontSize: "clamp(0.95rem, 1.1vw, 1.1rem)"
    fontWeight: 600
    lineHeight: 1.15
  body:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 400
    lineHeight: 1.65
  lead:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "clamp(1.15rem, 1.75vw, 1.65rem)"
    fontWeight: 500
    lineHeight: 1.35
rounded:
  panel: "12px"
  plinth: "4px"
  round: "50%"
spacing:
  gutter: "16px"
  actions-gap: "14px"
  grid-gap: "18px"
  section: "clamp(64px, 8vw, 110px)"
  container: "1240px"
  measure: "46rem"
components:
  button-call:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.wall}"
    typography: "{typography.sign}"
    rounded: "{rounded.panel}"
    padding: "0.7em 1.3em"
    height: "52px"
  button-call-hover:
    backgroundColor: "{colors.navy-hover}"
  button-whatsapp:
    backgroundColor: "{colors.whatsapp-green}"
    textColor: "{colors.wall}"
    typography: "{typography.sign}"
    rounded: "{rounded.panel}"
    padding: "0.7em 1.3em"
    height: "52px"
  button-whatsapp-hover:
    backgroundColor: "{colors.whatsapp-green-hover}"
  button-appointment:
    backgroundColor: "{colors.light-blue}"
    textColor: "{colors.navy}"
    typography: "{typography.sign}"
    rounded: "{rounded.panel}"
    padding: "0.5em 1em"
    height: "56px"
  button-appointment-hover:
    backgroundColor: "{colors.light-blue-hover}"
  corridor-sign:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.wall}"
    typography: "{typography.sign}"
    rounded: "{rounded.panel}"
    padding: "0 20px 0 34px"
    height: "94px"
  directory-row:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.wall}"
    typography: "{typography.sign-row}"
    padding: "0.45em 0.2em"
  directory-row-urgent:
    backgroundColor: "{colors.urgent-red}"
    textColor: "{colors.wall}"
    typography: "{typography.sign-row}"
  directory-row-urgent-hover:
    backgroundColor: "{colors.urgent-red-hover}"
  plaque:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.wall}"
    typography: "{typography.sign}"
    rounded: "{rounded.panel}"
    padding: "1.1rem 1.2rem"
  plaque-hover:
    backgroundColor: "{colors.navy-hover}"
  summary-box:
    backgroundColor: "{colors.light-blue-veil}"
    textColor: "{colors.ink}"
    rounded: "{rounded.panel}"
    padding: "1.4rem 1.6rem"
  urgent-panel:
    backgroundColor: "{colors.urgent-red-veil}"
    textColor: "{colors.ink}"
    rounded: "{rounded.panel}"
  input:
    backgroundColor: "{colors.wall}"
    textColor: "{colors.ink}"
    padding: "0.7rem 1rem"
    height: "52px"
---

# Design System: Dr. David García · Cirugía Vascular

## Overview

**Creative North Star: "The Wayfinding Corridor"**

The site is a hospital corridor, not a clinic brochure. The page ground is the corridor floor (a cool off-white), navy panels are the signs that hang from the ceiling and stand on plinths, and light blue route lines run along the floor from each sign to its destination. A visitor who arrives worried reads the directory the way they would in the Hospital General: they find the line that says what they feel, see at once whether it is "pide cita" or "urgencias", and follow it. The route lines are drawn as open vessels with flow inside them, which is where the vascular subject and the wayfinding world meet.

Density is low and sizes are generous, because the reader is often 60 or older and on a phone: body text never drops below 18px, touch targets hold 44px and most hold 52px. Authority comes from order and plainness: clear signs, one radius, one set of line icons, colours that mean one thing each. Illustration is limited to the brand's warm flat editorial style (a patient following the floor line); no stock doctor photography, no teal clinic hero, no grid of white service cards.

The direction contract predates the approved comp (comp D2, hybrid). Where they differ, the build is recorded here: navigation is a hanging corridor sign rather than a plain header, the directory totem carries six symptom rows rather than five, sign lettering is Barlow Semi Condensed rather than Montserrat, the single radius is 12px rather than 10px, and the route tube is 14px rather than 12px.

**Key Characteristics:**
- Navy sign panels on a pale corridor floor; light blue route lines with a moving white flow dash.
- Three typefaces with strict jobs: Montserrat 800 headings, Barlow Semi Condensed sign lettering, Inter for reading.
- Semantic colour is absolute: red is urgency, green is WhatsApp (and healthy-habit checks), nothing else.
- One radius (12px) for every panel, button and plaque.
- Tabler line icons plus three authored pictograms (varicose leg, uterus and ovaries, foot with wound) in the same 2px round stroke.
- Large type and targets for older readers; motion is ambient and stops under reduced motion.

## Colors

A two-colour signage palette (navy and light blue) on a cool off-white floor, with red and green held back as signals that each mean exactly one thing.

### Primary
- **Corridor Sign Navy** (navy): every sign surface: the hanging navigation sign, the directory totem, door plaques, the treatments floor plan, the closing band; also heading colour on light ground and the "Llamar" button. Hover lifts to **Lit Sign Navy** (navy-hover); the footer and totem plinth sit on **Plinth Navy** (navy-deep).

### Secondary
- **Route Line Blue** (light-blue): the floor lines and route tubes (veins), the "Pedir cita" button, focus rings, text selection, link underlines, the active-nav underline. Too light to carry text on white; when light blue must be text on a pale ground, use **Legible Route Blue** (light-blue-ink). **Route Veil** (light-blue-veil) fills the "En pocas palabras" summary box.

### Tertiary (semantic, not decorative)
- **Urgency Red** (urgent-red): only the urgency route. The red totem row "Pierna hinchada o fría de golpe: Urgencias", its red route line, the "Esto es de urgencias" panel header, the urgent room on the floor plan, the red legend swatch. **Urgency Ink** (urgent-red-ink) for red text on the **Urgency Veil** (urgent-red-veil) panel ground.
- **WhatsApp Green** (whatsapp-green): the WhatsApp button and the WhatsApp slot of the mobile bar; also the round tick of healthy-habit check lists. It is the brand green (#27AE60) deepened so white text passes AA.

### Neutral
- **Corridor Floor** (floor): page background.
- **Wall White** (wall): alternating section bands, the appointment box, form fields.
- **Sign Ink** (ink): body text, a navy-leaning near-black.
- **Soft Ink** (ink-soft): secondary text, captions, breadcrumbs, myths.
- **Hairline** (hairline): section rules, list dividers, 1px rings around light panels.

### Named Rules
**The Red Means Urgencias Rule.** Urgency Red appears only on the one route that means "go to A&E today". No red for errors styling, sale badges, emphasis or decoration. If a screen has red on it, the visitor must be able to say which symptom sends them to urgencias.

**The Green Is WhatsApp Rule.** Green is the WhatsApp action and the healthy-habit tick, nothing else. Success states, "available" dots and generic confirmations do not borrow it.

**The Signs Are Navy Rule.** Anything the visitor navigates by (directory, plaque, door sign, floor plan, nav) is a navy panel with white lettering. Short sign-like messages (the take-away box, the closing call band, the doctor's door plaque) may also sit on navy; articles, lists and FAQ answers sit on floor or wall.

## Typography

**Display Font:** Montserrat 800 (with Inter, system-ui)
**Sign Font:** Barlow Semi Condensed 600/700 (with Arial Narrow, system-ui)
**Body Font:** Inter variable (with system-ui, -apple-system, Segoe UI, Roboto)

**Character:** Montserrat at extra-bold is the voice of the headline; Barlow Semi Condensed is the lettering you would find on the corridor signs themselves, compact and upright; Inter does the patient reading at a large, calm size. All three are self-hosted.

### Hierarchy
- **Display** (display): the home H1 "Cirujano vascular en Ciudad Real" only; tight, near-solid leading.
- **Headline** (headline): section H2s; balanced wrap. Inside a navy panel the same face turns white.
- **Title** (title): H3s, FAQ questions, box titles such as "En pocas palabras".
- **Sign** (sign): buttons, nav links, plaque titles, the "Usted está aquí" marker, the mobile bar.
- **Sign Row** / **Sign Sub** (sign-row, sign-sub): the two lines of a directory row: what you feel, then where it leads (sub in a pale blue on navy, #D6E6FA).
- **Body** (body): all reading text, max measure 46rem for articles and 65ch for FAQ answers.
- **Lead** (lead): the hero subline and the doctor lead, in navy.

### Named Rules
**The Sign Lettering Rule.** If it would be painted on a hospital sign (a destination, an action, a room), set it in Barlow Semi Condensed 700. If it is a heading, Montserrat 800. If it is to be read, Inter. Never mix jobs.

**The 18px Floor Rule.** Body text is 1.125rem (18px) minimum; secondary text may go to 0.95rem only for metadata (dates, collegiate number, legal).

## Layout

A single 1240px container with a 16px side gutter at every width. Sections breathe on a fluid rhythm (64px to 110px vertical padding) and alternate floor and wall grounds separated by a hairline, so the page reads as successive stretches of corridor rather than stacked cards.

The home hero is a composed scene above 1100px: headline and actions on the left, the illustrated patient standing on the light blue floor line at the base, the navy totem at about 54% from the left, and one route line per totem row leaving the panel, turning with a 34px radius and running down the page (drawn in script from live row positions and redrawn on resize and font load). Below 1100px the hero becomes one column (max 720px): copy, illustration, totem, then the floor line full-bleed; route lines collapse to short stubs leaving each row (red for the last). Below 720px the illustration drops out and buttons share the row equally.

Inner condition pages are a reading column plus a 330px sticky side column (appointment box and index), collapsing to one column below 1100px. On phones a fixed three-slot bar (Llamar, WhatsApp, Pedir cita) sits at the bottom.

Breakpoints: 1100px (scene vs. stacked) and 720px (phone).

## Elevation & Depth

Mostly flat, with physical signage depth where a panel is a real object. Sign panels (totem, door plaque, floor plan, appointment box, open mobile menu) carry one soft two-layer drop so they read as mounted signs; the hanging nav sign has its own tighter drop plus two metallic hangers. Light content panels (warning panels, address block) use a 1px hairline ring instead of a shadow. Depth also comes from ground alternation (floor vs. wall) and the navy plinth under the totem.

### Shadow Vocabulary
- **Mounted sign** (`box-shadow: 0 2px 4px rgba(16,20,32,.08), 0 12px 28px -12px rgba(16,20,32,.3)`): totem, door plaque, floor plan, appointment box, mobile menu.
- **Hanging sign** (`box-shadow: 0 14px 24px -14px rgba(16,20,32,.45)`): the corridor navigation sign only.
- **Hairline ring** (`box-shadow: 0 0 0 1px #DADDE6`): light panels that need an edge without lift.

### Named Rules
**The Only Signs Lift Rule.** A shadow means "this is a physical sign". Text blocks, lists and links stay flat on the floor.

## Shapes

One corner: 12px on every panel, button, plaque, room and summary box. Exceptions are structural, not stylistic: the totem's bottom corners and plinth are 4px (it stands on the floor), stop markers and step numbers are circles, and the floor line ends in a rounded cap. Route lines are 14px tubes (9px on the floor plan) with round caps and round joins, turning on generous radii, carrying a 3px white dash (14 on, 16 off) that flows toward the destination. Sign panels may carry small bolt heads or hangers (the door plaque's two screws, the floor plan's two rivets) as mounting hardware. Icons are 24px line drawings with a 2px round stroke (1.6 at 40px and above).

**The One Radius Rule.** 12px, everywhere a corner is rounded. If a new component wants another radius, it is not yet a sign.

**The Open Vessel Rule.** A route line is always a tube with flow inside it, never a flat stroke or dotted guide: tube colour plus a moving white dash, round caps, and it must end at a destination.

## Components

### Buttons
Sign-lettered, square-shouldered and large: they read like the action plates at a hospital desk.
- **Shape:** gently rounded (12px), 52px minimum height, 2px transparent border reserved for the outline variant.
- **Llamar (navy):** navy with white Barlow 700 at 1.25rem, phone icon leading; the number appears beside it in Inter 500 when known.
- **WhatsApp (green):** WhatsApp Green, white lettering, WhatsApp icon.
- **Pedir cita (light blue):** light blue with navy lettering; used in the nav sign, the mobile bar and the closing band.
- **Outline:** wall white, navy border and text (online booking, when a link exists).
- **Hover / Focus / Active:** hover deepens the fill (160ms); press scales to 0.97 with the out-curve; focus is a 3px light blue outline at 3px offset. In the hero, buttons scale up with the headline (up to 2.2rem, 64px tall).

### Corridor Sign (navigation)
A navy 12px panel hanging from two metallic rods. Left: the monogram mark and the name in sign lettering with a light blue separator. Right: four destinations in white sign lettering (hover turns them light blue; the current page gets a 3px light blue underline) and the light blue "Pedir cita" button. Below 1100px it shrinks to 68px and the menu drops down as a second navy panel.

### Directory Totem ("¿Qué notas?")
The signature component. A navy standing panel titled "¿Qué notas?" over a white rule, with six rows separated by faint white hairlines. Each row: a line pictogram (40 to 60px), the symptom in Sign Row lettering, its destination in Sign Sub, and an arrow. Hover tints the row light blue at 14%, nudges the arrow 4px right and, on the home hero, dims every other route line to 28% while the chosen line's flow speeds up. The last row is the urgency row: full-bleed red across the panel. The totem stands on a darker navy plinth. A compact variant (no route lines) serves as the directory on inner pages.

### Route Lines and Floor Line
Drawn at runtime from the rows' real positions: one line per totem row on the home hero, and on the treatments floor plan one line from "Usted está aquí" to every room (light blue for veins, white with navy flow for arteries, red for urgencias). The floor line is a 30px light blue band with a round end and a white dashed flow. All flow animations stop under reduced motion.

### Plaques and Rooms
- **Plaque:** navy 12px, light blue line icon spanning two lines, title in sign lettering, one-line summary in pale blue; hover lifts to Lit Sign Navy, press scales to 0.98. Used for related conditions.
- **Door sign:** navy panel carrying a condition page's H1 in white with its pictogram in light blue.
- **Room (floor plan):** navy with a 2.5px white border (light blue for venous rooms, red for urgencias) and sign lettering.

### Content Panels
- **Summary box:** Route Veil ground, 12px, title in Montserrat 800 navy.
- **Take-away:** navy 12px, light blue title, white text at 1.2rem.
- **Warning panels:** paired; "Pide cita si…" has a navy header, "Esto es de urgencias" has a red header on the Urgency Veil ground.
- **Healthy-habit list:** round WhatsApp Green tick with a white check.

### Inputs / Fields
- **Style:** wall white, 1.5px #9AA3BD stroke, 52px tall, Inter at body size.
- **Focus:** stroke turns navy plus a 3px light blue outline at 1px offset.

## Do's and Don'ts

### Do:
- **Do** send every navigation choice through a sign: a navy panel with white sign lettering, a line icon and an arrow.
- **Do** draw every route as an open vessel: 14px tube, round caps, moving white dash, ending at its destination.
- **Do** keep body text at 18px or more and every tap target at 44px or more (52px for buttons).
- **Do** use 12px for every rounded corner.
- **Do** pair every destination with a Tabler line icon or one of the authored pictograms, all in the same 2px round stroke.
- **Do** stop the flow animations and transitions under `prefers-reduced-motion`.

### Don't:
- **Don't** use Urgency Red for anything but the route to urgencias.
- **Don't** use green for anything but WhatsApp and healthy-habit ticks.
- **Don't** build page structure from grids of white shadowed service cards; destinations are directory rows, plaques or rooms.
- **Don't** use stock photos of doctors, surgery, wounds or clinics; illustration stays in the brand's flat editorial style.
- **Don't** set long-form reading (articles, FAQ answers, lists of more than a few lines) on navy.
- **Don't** set sign lettering in Inter or body text in Barlow.
