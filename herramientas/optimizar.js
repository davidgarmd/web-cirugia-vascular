// Convierte las ilustraciones de assets/plates a WebP para la web usando Chromium (Playwright).
// Uso: node herramientas/optimizar.js
const path = require('path'), fs = require('fs');
const { chromium } = require(require('module').createRequire(path.join(__dirname, '..', 'package.json')).resolve('playwright'));
const trabajos = [
  ['assets/plates/woman.png', 'static/img/mujer-caminando.webp', 500],
  ['assets/plates/mapa-vascular.png', 'static/img/mapa-vascular.webp', 700],
];
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const [src, dst, w] of trabajos) {
    const data = 'data:image/png;base64,' + fs.readFileSync(path.join(__dirname, '..', src)).toString('base64');
    const out = await p.evaluate(async ([data, w]) => {
      const img = new Image(); img.src = data; await img.decode();
      const c = document.createElement('canvas'); c.width = w; c.height = Math.round(img.height * w / img.width);
      c.getContext('2d').drawImage(img, 0, 0, c.width, c.height);
      return c.toDataURL('image/webp', 0.88);
    }, [data, w]);
    fs.writeFileSync(path.join(__dirname, '..', dst), Buffer.from(out.split(',')[1], 'base64'));
    console.log(dst, fs.statSync(path.join(__dirname, '..', dst)).size, 'bytes');
  }
  await b.close();
})();
