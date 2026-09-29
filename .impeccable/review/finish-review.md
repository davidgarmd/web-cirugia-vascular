disposition: recapture

Inline role (no subagent) disclosed. Unread: `.impeccable/review/diff/final/` (does not exist; only `diff/hero/`), `.impeccable/build/spec.json`, QUALITY BAR card (none named in packet), `static/rutas.js`, `contenido.py` beyond visible-text extraction.

## recapture

- `.impeccable/review/mobile.png` is invalid: the "De cuello a pies" body map is a blank ~330px region (capture y≈1150-1500). The box is reserved but unpainted because `<img src="/img/mapa-vascular.webp" loading="lazy">` (build.py:307) never loaded during the full-page capture; at 1440 it did. A valid capture shows the navy/celeste body figure centred above the six labels. Recapture after scrolling the page to the bottom (or with `loading="eager"` forced in the capture script), same 390 width.
- Every other capture (`desktop.png`, `desktop-tratamientos.png`, `desktop-pelvica.png`, `mobile-pelvica.png`, `diff/hero/side-by-side.png`) is valid.

---

The procedure says a failed capture ends the review. The failure is confined to one lazy-loaded image, and the rest of the evidence is valid, so the provisional review below is built only on that valid evidence, with the mobile body-map region left unjudged. It is **not a verdict**. After a valid recapture, the expected disposition is **fix** unless the recapture shows something new.

## persistence (provisional)

- PRODUCT.md: pass.
- Approval: pass. `comp-d2-hibrida.png.json` has `"approved": true`. `comps: skipped` has a note saying approval came before state.
- **Fail:** `.impeccable/build/state.json` still shows `hero` as `open`, with `gate.ok: false` and 10 attempts. `sections`, `motion`, `responsive` and `review` are all `pending`. The hero score of 0.806 clears 0.72, but 8 regions are still `contradicted`: logo-mark, brand-name, btn-llamar, btn-whatsapp, totem-panel and 4 of the 6 rows. `hero-repro.png` exists.

## fidelity (provisional; against my own inventory of comp D2)

| Element | Verdict | Evidence |
|---|---|---|
| Hanging nav sign with rods, brand line, 4 links, celeste "Pedir cita" | match | side-by-side |
| Logo mark | **contradicted** | Comp: a DG monogram with a branching vessel. Build: a rounded square with one diagonal celeste stroke, which reads as a generic app icon. report: contradicted. |
| Headline "Cirujano vascular en Ciudad Real" (TYPE: Montserrat 800, tight, 2 lines) | match | |
| Sign lettering (nav, rows, buttons) in Barlow Semi Condensed | adaptation | user-approved deviation (packet) |
| Subtext (2 lines) | match | |
| Llamar / WhatsApp | adaptation | green darkened to #187A43 for contrast (a11y, cited) |
| Walking-woman plate at the base, on the floor line | match desktop / **missing mobile** | `.hero-mujer{display:none}` at ≤720 (estilos.css ~l.416). The removal cites no evidence. |
| Totem panel: title, rule, 6 rows, plinth | match in topology | |
| Totem pictograms | **contradicted** | Comp: large (≈60px) bespoke pictograms (leg with varicose marks, uterus and ovaries, walker with motion ticks, foot, report sheet with check, siren). Build: ≈32px thin Tabler glyphs. The "leg" is a boot-like stroke and the pelvis glyph reads as a crown. This drives the 4 contradicted row scores. |
| Row rhythm | drift | Comp rows are taller and evenly spaced, with sub-labels larger in proportion. Build rows are compressed and sub-labels read at ≈12-14px. |
| Red urgency row, bleeding past the panel edges | match | |
| Route lines exiting each row, flow dashes, red last | match desktop / **missing mobile** | `.rutas{display:none}` at <1100px. At 390 the page's signature (rows emitting vessels) is gone; only the floor stripe remains. The removal cites no evidence. |
| Floor line under the woman into the plinth | match | |
| MATERIAL (flat editorial vector, raster woman plate) | match | |
| GROUND | adaptation | Comp #f8f7ea (warm). Build `--suelo:#F4F6F5` (cool). Cited in OWN-WORLD ("cool off-white"). |
| Below-fold sections | not in comp, judged against the world | Body map, stops line, door plate, provinces "line", FAQ, blog, CTA band |

## ceiling (provisional)

- The route lines stop at the hero's bottom border and never arrive anywhere. The contract says a line "leads them to their page", yet no line continues into the body-map section or ends at its label.
- The pictogram set is the world's main native device, and it is borrowed rather than drawn.
- Condition pages use the navy door-sign title (`.puerta`) but leave the rest of the first viewport empty (see fix 7).
- The "Otras consultas en esta planta" block reverts to three identical icon cards where the world has a native answer: a directory list with route stubs.

## material_fixes (ordered)

1. **Fidelity: totem pictograms and row rhythm** (build.py totem row icons, static/estilos.css).
   - produce: the 6 row pictograms as authored one-stroke SVGs, re-derived from comp regions `row-varices` … `row-urgencias` (leg with varicose marks, uterus and ovaries, walker, foot, report with check, siren).
   - CSS: `.fila-ico{width:clamp(40px,4.2vw,64px);height:clamp(40px,4.2vw,64px);stroke-width:1.75}` and `.fila-d{font-size:clamp(1.05rem,1.2vw,1.2rem)}`.
   - Re-run hero comp-diff until those regions leave `contradicted`.
2. **Fidelity: logo mark.**
   - produce: the DG monogram with branching vessel as an authored SVG from comp region `logo-mark`, or David's real @davidgarmd mark if one exists.
   - Replace the inline `<svg class="logo-marca">` markup in build.py.
3. **Contract/mobile: route lines and patient plate missing below 1100 / 720px** (estilos.css).
   - Route stubs: in the `max-width:1099.98px` block add `.totem{margin-right:22px}` `.totem-filas li{position:relative}` `.totem-filas li::after{content:"";position:absolute;right:-32px;top:50%;width:32px;height:10px;margin-top:-5px;border-radius:0 5px 5px 0;background:var(--celeste)}` `.totem-filas li:last-child::after{background:var(--rojo)}`. Each row then still emits its vessel.
   - Patient plate: in the ≤720 block, replace `.hero-mujer{display:none}` with `.hero-mujer{display:block;width:92px;grid-row:auto;justify-self:start;margin:-4px 0 -22px 24px}`, placed directly above `.suelo`.
4. **Mobile first viewport: the red urgency row is hidden under the fixed `.barra-movil`** at 390×844 (the row starts at y≈775; the bar covers 780-844).
   - Compact the ≤720 hero: `.hero-grid{padding-top:14px;gap:16px}` `.acciones-hero{margin-top:14px}` `.totem h2{font-size:1.6rem}` `.fila{padding:.32em .2em}`.
   - Verify in the recapture that the whole red row sits above y=780. Principle 3 ("urgency unmistakable") depends on it.
5. **Floor: kicker.** `<p class="pp-consulta">Consulta</p>` above "Dr. David García" on the door plate (build.py:348 and build.py:501). Delete both lines and the `.pp-consulta` rule.
6. **Legibility (PRODUCT: base text ≥18px for a 60+ audience)** in static/estilos.css:
   - Delete `body{font-size:1.07rem}` in the ≤720 block (it drops body text to 17.1px).
   - Raise `.pie-legal` .87rem → 1rem, `.pie` .97rem → 1.05rem, `.caja-h` .92rem → 1rem and `.migas ol` .95rem → 1rem.
7. **Condition page (desktop-pelvica) first viewport leaves the right ~40% empty** from y≈210 to 700 at 1440. The "Pide cita" card starts only at y≈720.
   - In the condition-page template in build.py, start `.pag-grid` at the breadcrumb so `<aside class="lateral">` sits beside the door sign and intro.
   - Replace "Otras consultas en esta planta" (three equal navy icon cards: a craft-floor and taste 9.C ban) with a directory list reusing the totem `.fila` markup (icon, title, sub-label, arrow, route stub).
8. **Persistence:** close the `hero` phase (re-gate after fixes 1-2) and the pending `sections`/`motion`/`responsive` phases in `.impeccable/build/state.json`, or record the user's acceptance of the remaining contradicted regions in words.

## keep

Keep the desktop hero composition exactly: the hanging nav sign, the navy totem with one red row, the six vessel routes with moving flow bleeding off the right edge, and red reserved for urgency alone (the Tratamientos "plano" follows the same rule and should stay).

## Content, medical and Spanish (visible text)

- **Em-dashes:** none found in any `public/**/*.html`.
- **Voice:** build.py:479 "Usted está aquí" breaks the tú voice. Change it to "Estás aquí".
- **Medical safety:** the home totem urgency is "Pierna hinchada de golpe", which covers DVT but not acute limb ischaemia. The Tratamientos plan already says "pierna hinchada o fría de golpe". Use "Pierna hinchada o fría de golpe" on the totem too (a small text change from the comp, justified by content truth).
- **Specialty naming is inconsistent.** The doctor section says "Especialista vía MIR en Angiología y Cirugía Vascular y Endovascular", but the FAQ correctly says the single specialty is "Angiología y Cirugía Vascular". Suggested doctor line: "Especialista vía MIR en Angiología y Cirugía Vascular, con formación endovascular".
- **Capitalisation:** in the footer, change "Cirujano Vascular y Endovascular" to "Cirujano vascular y endovascular" (common nouns). The specialty name stays capitalised.
- **Abbreviation:** RAE form "n.º", not "Nº", in "Nº col.", "Nº de colegiado" and "Nº de inscripción".
- **Wording:** the pelvic page says "casi siempre de la vena ovárica". "Con frecuencia de la vena ovárica" is more accurate, since internal iliac tributaries are often involved. Optional.
- **Placeholders:** phone, address, centre name, colegiado and registry numbers are still bracketed placeholders. They are marked correctly, but launch-blocking, and the Llamar/WhatsApp links must point to real numbers before going live.
