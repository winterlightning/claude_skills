/* Profile contracts define the target visible-ink envelope, not the stroke centerline. */
(() => {
  'use strict';
  let contracts = null;
  const NS = 'http://www.w3.org/2000/svg';
  const ready = fetch('laboratory.json').then(response => {
    if (!response.ok) throw Error('Profile guides unavailable');
    return response.json();
  }).then(data => { contracts = data; }).catch(() => {});
  // The keyshape shown is the one of the drawing actually displayed (its preview SVG), measured in the browser: a record's
  // stored keyshape can describe an older drawing (a Browser Edit or an upload picked since). Profiles with contract
  // keyshapes are measured; others (combined icons, whose build stores the keyshape it measured) keep the stored one.
  const measuredByUrl = new Map();
  // Per icon object (never copied by {...icon}, so the editor's keyshape choices stay what they say): 'pending' or
  // the measured {name, bounds}. Only icons the grid mounted or measured are in it.
  const measured = new WeakMap();
  let probe = null;
  function measurable(icon) {
    const profile = icon.profile || contracts?.profile.families[icon.family]?.profile;
    return !!(icon.preview_url && profile && contracts?.keyshapes.resolved[profile] && icon.sizing_mode !== 'text-height32');
  }
  // The drawing's stroke-centerline box on its canvas (getBBox of the whole SVG: geometry only, transforms applied).
  function centerlineBox(text, size) {
    const doc = new DOMParser().parseFromString(text, 'image/svg+xml'), root = doc.documentElement;
    if (!root || root.nodeName.toLowerCase().split(':').pop() !== 'svg' || doc.querySelector('parsererror')) return null;
    if (!probe) {
      probe = document.createElement('div');
      probe.setAttribute('aria-hidden', 'true');
      probe.style.cssText = 'position:absolute;left:-10000px;top:0;width:0;height:0;overflow:hidden;visibility:hidden';
      document.body.append(probe);
    }
    const svg = document.importNode(root, true);
    probe.replaceChildren(svg);
    try {
      const view = (svg.getAttribute('viewBox') || '').trim().split(/[\s,]+/).map(Number);
      const [vx, vy, vw, vh] = view.length === 4 && view.every(Number.isFinite) && view[2] > 0 ? view : [0, 0, size, size];
      const k = size / Math.max(vw, vh), ox = (Math.max(vw, vh) - vw) / 2, oy = (Math.max(vw, vh) - vh) / 2;
      const b = svg.getBBox();
      if (!(b.width > 0 || b.height > 0)) return null;
      return [(b.x - vx + ox) * k, (b.y - vy + oy) * k, (b.x + b.width - vx + ox) * k, (b.y + b.height - vy + oy) * k];
    } catch { return null; } finally { probe.replaceChildren(); }
  }
  // The contract keyshape whose centerline box is the drawing's (within half a unit); the stored name wins among
  // keyshapes that share bounds (CIRCLE / SQUARE on SUB32, the L / XL / S rectangles). None: FREE, the measured box.
  function fit(profile, box, stored, stroke) {
    const shapes = contracts?.keyshapes.resolved[profile] || {};
    const hits = Object.entries(shapes).filter(([, k]) => Array.isArray(k.centerline_bounds) && k.centerline_bounds.every((v, i) => Math.abs(v - box[i]) <= 0.5));
    // XL and S are compatibility names for the L rectangles (icon-profile notes): an L or M name is the one to show.
    const current = ([name]) => !/_(XL|S)$/.test(name);
    const hit = hits.find(([name]) => name === stored) || hits.find(([name]) => name === 'SQUARE') || hits.find(current) || hits[0];
    if (hit) return {name: hit[0], bounds: hit[1].visible_bounds};
    const half = stroke / 2, r = v => Math.round(v * 100) / 100;
    return {name: 'FREE', bounds: [r(box[0] - half), r(box[1] - half), r(box[2] + half), r(box[3] + half)]};
  }
  // → Promise of the icon once its displayed drawing is measured (resolve / label / envelope then show that keyshape).
  function measure(icon) {
    if (!icon || !measurable(icon)) return Promise.resolve(icon);
    const done = measured.get(icon);
    if (done && done !== 'pending') return Promise.resolve(icon);
    measured.set(icon, 'pending');
    const profile = icon.profile || contracts?.profile.families[icon.family]?.profile;
    const size = contracts?.profile.profiles[profile]?.canvas_size || icon.canvas_size;
    const url = icon.preview_url;
    if (!measuredByUrl.has(url)) {
      measuredByUrl.set(url, fetch(url).then(r => r.ok ? r.text() : null).then(text => text ? centerlineBox(text, size) : null).catch(() => null));
    }
    return measuredByUrl.get(url).then(box => {
      measured.set(icon, box ? fit(profile, box, icon.keyshape, icon.style?.stroke_width || 4) : {name: null, bounds: null});
      return icon;
    });
  }
  function resolve(icon) {
    const profile = icon.profile || contracts?.profile.families[icon.family]?.profile;
    const size = contracts?.profile.profiles[profile]?.canvas_size || icon.canvas_size;
    if (!Number.isFinite(size) || size <= 0) return null;
    const m = measured.get(icon);
    // A mounted drawing never shows its stored keyshape: until it is measured there is nothing to show.
    if (m === 'pending') return {profile, size, width:icon.canvas_width||size, name:null, bounds:null, pending:true};
    if (m) return {profile, size, width:icon.canvas_width||size, name:m.name, bounds:m.bounds, measured:true};
    const standard = contracts?.keyshapes.resolved[profile]?.[icon.keyshape];
    const bounds = (icon.keyshape === 'FREE' || icon.sizing_mode === 'text-height32') ? icon.keyshape_bounds : standard?.visible_bounds || icon.keyshape_bounds;
    const valid = Array.isArray(bounds) && bounds.length === 4 && bounds.every(Number.isFinite) && bounds[2] > bounds[0] && bounds[3] > bounds[1];
    return {profile, size, width:icon.canvas_width||size, name:icon.sizing_mode==='text-height32'?'TEXT HEIGHT 32':icon.keyshape, bounds:valid ? bounds : null};
  }
  function label(icon) {
    const spec = resolve(icon);
    if (spec?.pending) return 'Measuring keyshape…';
    if (!spec?.bounds) return 'Keyshape unavailable';
    const [l,t,r,b] = spec.bounds, n = v => Math.round(v * 100) / 100;
    return `${spec.name === 'FREE' ? 'Off keyshape' : spec.name} · ${n(r-l)} × ${n(b-t)} · ${spec.profile || spec.size+' canvas'}`;
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
    // Drawn again once the displayed drawing is measured (the first call may have nothing to show yet).
    if (measurable(icon) && (!measured.has(icon) || measured.get(icon) === 'pending')) {
      const done = measure(icon);
      draw(canvas, icon);
      done.then(() => draw(canvas, icon));
      return done;
    }
    draw(canvas, icon);
    return Promise.resolve(icon);
  }
  function draw(canvas, icon) {
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
  window.IconGuides = {ready,resolve,label,envelope,mount,choices,measure};
})();
