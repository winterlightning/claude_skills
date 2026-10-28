/* The 64px grid and keyshape overlay of a fill side pair tile.

   keyshape(mainLayout, subLayout) measures where a pick's parts sit (their boxes, the placed centerline, plus the 4px
   stroke): {box, main, sub, ok, name, off_by}. The pair should fill a 56 square, 60×44 or 44×60 (±1). */
(function () {
  'use strict';
  const NS = 'http://www.w3.org/2000/svg';
  const KEYSHAPES = {SQUARE: [4, 4, 60, 60], HRECT: [2, 10, 62, 54], VRECT: [10, 2, 54, 62]};
  const LABEL = {SQUARE: 'SQUARE 56', HRECT: 'RECT 60×44', VRECT: 'VRECT 44×60'};
  const el = (tag, attrs) => { const e = document.createElementNS(NS, tag); for (const [a, v] of Object.entries(attrs)) e.setAttribute(a, v); return e; };
  const rect = (cls, [x0, y0, x1, y1]) => el('rect', {class: cls, x: x0, y: y0, width: x1 - x0, height: y1 - y0});

  function overlay(keyshape) {
    const svg = el('svg', {class: 'sf-guide', viewBox: '0 0 64 64', 'aria-hidden': 'true'});
    for (let v = 4; v < 64; v += 4) {
      const cls = 'g' + (v % 16 === 0 ? ' major' : '');
      svg.append(el('line', {class: cls, x1: v, y1: 0, x2: v, y2: 64}), el('line', {class: cls, x1: 0, y1: v, x2: 64, y2: v}));
    }
    if (keyshape?.box) {
      for (const part of [keyshape.main, keyshape.sub]) if (part) svg.append(rect('part', part));
      const target = KEYSHAPES[keyshape.name] || keyshape.box;
      svg.append(rect('ks ' + (keyshape.ok ? 'ok' : 'bad'), target));
      if (!keyshape.ok) svg.append(rect('box', keyshape.box));
    }
    return svg;
  }
  function keyshape(mainLayout, subLayout) {
    const placed = layout => {
      if (!layout || !layout.length) return null;
      const x0 = Math.min(...layout.map(b => b.x)), y0 = Math.min(...layout.map(b => b.y));
      const x1 = Math.max(...layout.map(b => b.x + b.w)), y1 = Math.max(...layout.map(b => b.y + b.h));
      return [x0 - 2, y0 - 2, x1 + 2, y1 + 2];
    };
    const main = placed(mainLayout), sub = placed(subLayout);
    if (!main || !sub) return {ok: null};
    const box = [Math.min(main[0], sub[0]), Math.min(main[1], sub[1]), Math.max(main[2], sub[2]), Math.max(main[3], sub[3])];
    let name = null, off = Infinity;
    for (const [n, k] of Object.entries(KEYSHAPES)) {
      const e = Math.max(...k.map((v, i) => Math.abs(v - box[i])));
      if (e < off) { off = e;name = n; }
    }
    return {box, main, sub, ok: off <= 1, name, off_by: off};
  }
  function label(keyshape) {
    if (!keyshape?.box) return '';
    const [x0, y0, x1, y1] = keyshape.box;
    return keyshape.ok ? `${LABEL[keyshape.name]} · ${x1 - x0}×${y1 - y0}`
      : `off keyshape · ${x1 - x0}×${y1 - y0} (nearest ${LABEL[keyshape.name]})`;
  }
  window.SideFillOverlay = {overlay, label, keyshape};
})();
