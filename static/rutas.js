/* Menú móvil y líneas de ruta (vasos con flujo) de la portada y del plano. Sin dependencias. */
(function () {
  var NS = 'http://www.w3.org/2000/svg';

  // Menú móvil
  var boton = document.querySelector('.menu-btn'), menu = document.getElementById('menu');
  if (boton && menu) {
    boton.addEventListener('click', function () {
      var abierto = boton.getAttribute('aria-expanded') === 'true';
      boton.setAttribute('aria-expanded', String(!abierto));
      menu.classList.toggle('abierto', !abierto);
    });
    document.addEventListener('keydown', function (ev) {
      if (ev.key === 'Escape' && boton.getAttribute('aria-expanded') === 'true') { boton.click(); boton.focus(); }
    });
  }

  function ruta(svg, d, extra, id) {
    var g = document.createElementNS(NS, 'g');
    g.setAttribute('class', 'ruta ' + (extra || ''));
    if (id !== undefined) g.setAttribute('data-ruta', id);
    ['ruta-tubo', 'ruta-flujo'].forEach(function (c) {
      var p = document.createElementNS(NS, 'path');
      p.setAttribute('d', d); p.setAttribute('class', c); g.appendChild(p);
    });
    svg.appendChild(g);
    return g;
  }

  function caja(el, base) {
    var r = el.getBoundingClientRect();
    return { x: r.left - base.left, y: r.top - base.top, w: r.width, h: r.height };
  }

  /* Portada: de cada fila del tótem sale una línea que gira y baja */
  function trazarPortada() {
    var hero = document.querySelector('[data-rutas] .hero-grid');
    var svg = hero && hero.querySelector('.rutas');
    if (!svg || getComputedStyle(svg).display === 'none') return;
    svg.innerHTML = '';
    var base = hero.getBoundingClientRect();
    var totem = caja(hero.querySelector('.totem'), base);
    var filas = hero.querySelectorAll('.fila');
    var n = filas.length, derecha = base.width, abajo = base.height + 40;
    var ini = totem.x + totem.w, hueco = (derecha - ini - 40) / (n + 0.5), r = 34;
    svg.setAttribute('viewBox', '0 0 ' + base.width + ' ' + base.height);
    filas.forEach(function (f, i) {
      var b = caja(f, base), y = b.y + b.h / 2;
      var giro = ini + 30 + hueco * (n - i - 0.5);
      var d = 'M' + (ini - 2) + ' ' + y + 'H' + (giro - r) + 'Q' + giro + ' ' + y + ' ' + giro + ' ' + (y + r) + 'V' + abajo;
      ruta(svg, d, f.classList.contains('fila-urgente') ? 'ruta-urgente' : '', i);
    });
  }

  /* Plano: desde "Usted está aquí" una ruta llega a cada sala */
  function trazarPlano() {
    var plano = document.querySelector('[data-plano]');
    var svg = plano && plano.querySelector('.plano-rutas');
    if (!svg || getComputedStyle(svg).display === 'none') return;
    svg.innerHTML = '';
    var base = plano.getBoundingClientRect(), r = 18;
    svg.setAttribute('viewBox', '0 0 ' + base.width + ' ' + base.height);
    var p = caja(plano.querySelector('.aqui-punto'), base);
    var ox = p.x + p.w / 2, oy = p.y;
    plano.querySelectorAll('[data-sala]').forEach(function (s) {
      var b = caja(s, base), tipo = s.getAttribute('data-sala'), d, cls = '';
      if (tipo === 'centro') {
        d = 'M' + ox + ' ' + oy + 'V' + (b.y + b.h);
      } else if (tipo === 'urgente') {
        var cy = p.y + p.h / 2;
        d = 'M' + p.x + ' ' + cy + 'H' + (b.x + b.w); cls = 'ruta-urgente';
      } else {
        var izq = tipo === 'vena', eco = caja(plano.querySelector('.sala-eco'), base);
        var tx = izq ? eco.x - 26 : eco.x + eco.w + 26, y = b.y + b.h / 2;
        var fin = izq ? b.x + b.w : b.x, dir = izq ? -1 : 1;
        d = 'M' + ox + ' ' + (oy + 6) + 'H' + (tx - dir * r) + 'Q' + tx + ' ' + (oy + 6) + ' ' + tx + ' ' + (oy + 6 - r) +
            'V' + (y + r) + 'Q' + tx + ' ' + y + ' ' + (tx + dir * r) + ' ' + y + 'H' + fin;
        cls = izq ? '' : 'ruta-arteria';
      }
      ruta(svg, d, cls);
    });
  }

  function trazar() { trazarPortada(); trazarPlano(); }

  // Resalta la ruta de la fila señalada
  var hero = document.querySelector('[data-rutas]');
  if (hero) {
    var svg = hero.querySelector('.rutas');
    function foco(i) {
      svg.classList.toggle('enfocada', i !== null);
      svg.querySelectorAll('.ruta').forEach(function (g) { g.classList.toggle('activa', g.getAttribute('data-ruta') === i); });
    }
    hero.querySelectorAll('.fila').forEach(function (f) {
      var i = f.getAttribute('data-ruta');
      f.addEventListener('pointerenter', function () { foco(i); });
      f.addEventListener('pointerleave', function () { foco(null); });
      f.addEventListener('focus', function () { foco(i); });
      f.addEventListener('blur', function () { foco(null); });
    });
  }

  var pendiente = false;
  function programar() {
    if (pendiente) return;
    pendiente = true;
    requestAnimationFrame(function () { pendiente = false; trazar(); });
  }
  if ('ResizeObserver' in window) {
    var ro = new ResizeObserver(programar);
    document.querySelectorAll('[data-rutas] .hero-grid, [data-plano]').forEach(function (el) { ro.observe(el); });
  }
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(programar);
  programar();
})();
