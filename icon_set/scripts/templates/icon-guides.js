/* Profile contracts define the target visible-ink envelope, not the stroke centerline. */
(() => {
  'use strict';
  let contracts = null;
  const NS = 'http://www.w3.org/2000/svg';
  const ready = fetch('laboratory.json').then(response => {
    if (!response.ok) throw Error('Profile guides unavailable');
    return response.json();
  }).then(data => { contracts = data; }).catch(() => {});
  function resolve(icon) {
    const profile = icon.profile || contracts?.profile.families[icon.family]?.profile;
    const size = contracts?.profile.profiles[profile]?.canvas_size || icon.canvas_size;
    const standard = contracts?.keyshapes.resolved[profile]?.[icon.keyshape];
    const bounds = (icon.keyshape === 'FREE' || icon.sizing_mode === 'text-height32') ? icon.keyshape_bounds : standard?.visible_bounds || icon.keyshape_bounds;
    if (!Number.isFinite(size) || size <= 0) return null;
    const valid = Array.isArray(bounds) && bounds.length === 4 && bounds.every(Number.isFinite) && bounds[2] > bounds[0] && bounds[3] > bounds[1];
    return {profile, size, width:icon.canvas_width||size, name:icon.sizing_mode==='text-height32'?'TEXT HEIGHT 32':icon.keyshape, bounds:valid ? bounds : null};
  }
  function label(icon) {
    const spec = resolve(icon);
    if (!spec?.bounds) return 'Keyshape unavailable';
    const [l,t,r,b] = spec.bounds;
    return `${spec.name} · ${r-l} × ${b-t} · ${spec.profile || spec.size+' canvas'}`;
  }
  function node(tag, attributes) {
    const element = document.createElementNS(NS,tag);
    for (const [key,value] of Object.entries(attributes)) element.setAttribute(key,value);
    return element;
  }
  function envelope(icon) {
    const spec = resolve(icon);
    if (!spec?.bounds) return null;
    const [x,y,r,b] = spec.bounds;
    return node(spec.name === 'CIRCLE' ? 'ellipse' : 'rect', {
      ...(spec.name === 'CIRCLE' ? {cx:(x+r)/2,cy:(y+b)/2,rx:(r-x)/2,ry:(b-y)/2} : {x,y,width:r-x,height:b-y}),
      class:'keyshape-envelope',fill:'none',stroke:'#b96b31','stroke-width':.3,
      'stroke-dasharray':'1 .7','pointer-events':'none'
    });
  }
  const grids = new Map();
  function gridImage(size) {
    if (!grids.has(size)) {
      const svg = `<svg xmlns="${NS}" viewBox="0 0 ${size} ${size}"><defs><pattern id="unit" width="1" height="1" patternUnits="userSpaceOnUse"><path d="M1 0H0V1" fill="none" stroke="#b8c7b0" stroke-width=".045"/></pattern><pattern id="major" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="url(#unit)"/><path d="M8 0H0V8" fill="none" stroke="#9dae94" stroke-width=".12"/></pattern></defs><rect width="${size}" height="${size}" fill="#f7f9f4"/><rect width="${size}" height="${size}" fill="url(#major)"/></svg>`;
      grids.set(size,`url("data:image/svg+xml,${encodeURIComponent(svg)}")`);
    }
    return grids.get(size);
  }
  function mount(canvas, icon) {
    canvas.querySelector('.keyshape-overlay')?.remove();
    const spec = resolve(icon);
    if (!spec) return;
    canvas.style.backgroundImage = gridImage(spec.size);
    canvas.setAttribute('aria-label',`${spec.size} by ${spec.size} ${spec.profile || ''} canvas. Keyshape: ${label(icon)}`);
    const shape = envelope(icon);
    if (shape) {
      const overlay = node('svg',{viewBox:`0 0 ${spec.width} ${spec.size}`,class:'keyshape-overlay','aria-hidden':'true'});
      overlay.append(shape); canvas.append(overlay);
    }
  }
  function choices(icon) {
    if(icon.sizing_mode==='text-height32')return [{name:icon.keyshape,label:label(icon)}];
    const spec=resolve(icon), shapes=contracts?.keyshapes.resolved[spec?.profile] || {};
    const names=contracts?.profile.profiles[spec?.profile]?.keyshape_choices || Object.keys(shapes);
    return [...new Set([icon.keyshape,...names].filter(Boolean))].map(name=>({name,label:label({...icon,keyshape:name})}));
  }
  window.IconGuides = {ready,resolve,label,envelope,mount,choices};
})();
