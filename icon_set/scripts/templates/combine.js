/* Combinations built in the browser: the SVG a combination stores is made here and uploaded
 * (POST /api/combinations/build); the server only checks and stores it.
 *
 * Combine.container(mainSvg, symbolSvg, placement) replaces container_combination_render.py: the container as
 * drawn, with its symbol baked onto the 64 grid (coordinates rewritten, stroke kept at 4). `placement` is
 * {center: [x, y], ink: [w, h] | null} (ink: the painted box, even, 8..64; null keeps the symbol's
 * natural size in the standard 32 box) or {box: {x, y, w, h}}: the symbol's centreline box itself, as a
 * saved layout stores it.
 *
 * No DOM: it parses and writes the SVG itself, so the page and the Node tests
 * (icon_set/tests/js/combine.test.mjs) run the same code.
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.Combine = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  const NS = 'http://www.w3.org/2000/svg';
  const CANVAS = 64, BOX = 32, STROKE = 4;
  const SHAPES = new Set(['path', 'circle', 'ellipse', 'rect', 'line', 'polyline', 'polygon']);
  const SKIP = new Set(['defs', 'clipPath', 'mask', 'title', 'desc', 'metadata', 'style']);
  const INHERITED = ['fill', 'stroke', 'stroke-width', 'stroke-linecap', 'stroke-linejoin', 'stroke-miterlimit',
                     'fill-rule', 'opacity', 'stroke-opacity', 'fill-opacity'];
  const PRESENTATION = ['fill', 'stroke', 'stroke-width', 'stroke-linecap', 'stroke-linejoin'];
  const NUMBER = /[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?/g;
  const ARGS = {M: 2, L: 2, T: 2, H: 1, V: 1, C: 6, S: 4, Q: 4, A: 7, Z: 0};

  class CombineError extends Error {}
  const fail = message => { throw new CombineError(message); };

  // ---- SVG as a small tree: {tag, attrs, children} or {text}

  const ENTITIES = {amp: '&', lt: '<', gt: '>', quot: '"', apos: "'"};
  const decode = s => s.replace(/&(#x[0-9a-f]+|#\d+|\w+);/gi, (m, e) => e[0] === '#'
    ? String.fromCodePoint(e[1] === 'x' || e[1] === 'X' ? parseInt(e.slice(2), 16) : +e.slice(1)) : (ENTITIES[e] ?? m));
  const escapeAttr = s => String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;');
  const escapeText = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

  function parse(text) {
    if (/<!(DOCTYPE|ENTITY)/i.test(text)) fail('SVG with entity declarations cannot be combined.');
    const top = {tag: '#document', attrs: {}, children: []};
    const stack = [top];
    const token = /<!--[\s\S]*?-->|<\?[\s\S]*?\?>|<!\[CDATA\[([\s\S]*?)\]\]>|<\/\s*([\w:.-]+)\s*>|<([\w:.-]+)((?:\s+[\w:.-]+\s*=\s*(?:"[^"]*"|'[^']*'))*)\s*(\/?)>|([^<]+)/g;
    let m, last = 0;
    while ((m = token.exec(text))) {
      if (m.index !== last) fail('The SVG could not be read.');
      last = token.lastIndex;
      const parent = stack[stack.length - 1];
      if (m[2]) {
        if (stack.length < 2 || parent.tag !== m[2]) fail('The SVG could not be read.');
        stack.pop();
      } else if (m[3]) {
        const attrs = {};
        for (const a of m[4].matchAll(/([\w:.-]+)\s*=\s*(?:"([^"]*)"|'([^']*)')/g)) attrs[a[1]] = decode(a[2] ?? a[3]);
        const node = {tag: m[3], attrs, children: []};
        parent.children.push(node);
        if (!m[5]) stack.push(node);
      } else if (m[1] !== undefined) {
        parent.children.push({text: m[1]});
      } else if (m[6] !== undefined && stack.length > 1 && m[6].trim()) {
        parent.children.push({text: decode(m[6])});
      }
    }
    if (last !== text.length || stack.length !== 1) fail('The SVG could not be read.');
    const svg = top.children.find(n => n.tag && local(n.tag) === 'svg');
    if (!svg) fail('The artwork is not an SVG.');
    return svg;
  }

  function serialize(node) {
    if (node.text !== undefined) return escapeText(node.text);
    const attrs = Object.entries(node.attrs).map(([k, v]) => ` ${k}="${escapeAttr(v)}"`).join('');
    const tag = local(node.tag);
    return node.children.length ? `<${tag}${attrs}>${node.children.map(serialize).join('')}</${tag}>` : `<${tag}${attrs} />`;
  }

  const local = tag => tag.slice(tag.lastIndexOf(':') + 1);
  const clone = node => node.text !== undefined ? {text: node.text}
    : {tag: node.tag, attrs: {...node.attrs}, children: node.children.map(clone)};
  const elementsOf = node => node.children.filter(c => c.tag);

  // ---- numbers and transforms (combination_layout_svg.py, container_combination_render.py)

  function fmt(n) {  // round(n, 6) then '%.6f' without trailing zeros: exact ties (odd 128ths) round half to even
    let s = n.toFixed(6);
    if (Number.isInteger(n * 128) && (n * 128) % 2 !== 0) {
      const scaled = n * 1e6, lo = Math.floor(scaled), pick = lo % 2 === 0 ? lo : lo + 1;
      s = (pick / 1e6).toFixed(6);
    }
    return Number(s) === 0 ? '0' : s.replace(/0+$/, '').replace(/\.$/, '');
  }

  function affine(text) {
    // (sx, sy, tx, ty) of translate / scale / axis-aligned matrix steps.
    const TRANSFORM = /(translate|scale|matrix)\s*\(([^)]*)\)/g;
    if (text.replace(TRANSFORM, '').replace(/^[\s,]+|[\s,]+$/g, '')) {
      fail('Rotated or skewed artwork cannot be combined; redraw it without transforms.');
    }
    let sx = 1, sy = 1, tx = 0, ty = 0;
    for (const [, name, args] of text.matchAll(TRANSFORM)) {
      const v = args.trim().split(/[\s,]+/).filter(Boolean).map(Number);
      let a, b, c, d, e, f;
      if (name === 'translate') [a, b, c, d, e, f] = [1, 0, 0, 1, v[0], v.length > 1 ? v[1] : 0];
      else if (name === 'scale') [a, b, c, d, e, f] = [v[0], 0, 0, v.length > 1 ? v[1] : v[0], 0, 0];
      else [a, b, c, d, e, f] = v;
      if (Math.abs(b) > 1e-9 || Math.abs(c) > 1e-9) fail('Rotated or skewed artwork cannot be combined; redraw it without transforms.');
      tx += sx * e; ty += sy * f; sx *= a; sy *= d;
    }
    return [sx, sy, tx, ty];
  }

  function transformPath(d, sx, sy, tx, ty) {
    const tokens = d.match(new RegExp('[MmLlHhVvCcSsQqTtAaZz]|' + NUMBER.source, 'g')) || [];
    const out = [];
    let i = 0, command = null;
    while (i < tokens.length) {
      if (/^[a-z]$/i.test(tokens[i])) {
        command = tokens[i++];
        out.push(command);
        if (command === 'Z' || command === 'z') continue;
      } else if (command === null) {
        fail('Path data must start with a command.');
      }
      const upper = command.toUpperCase(), relative = command !== upper, count = ARGS[upper];
      const values = tokens.slice(i, i + count).map(Number);
      if (values.length !== count) fail('Incomplete path data.');
      i += count;
      if (upper === 'A') {
        let [rx, ry, rotation, large, sweep, x, y] = values;
        [x, y] = relative ? [x * sx, y * sy] : [x * sx + tx, y * sy + ty];
        const turn = ((rotation % 180) + 180) % 180;
        if (Math.abs(sx - sy) > 1e-9 && Math.min(turn, 180 - turn) > 1e-9 && Math.abs(turn - 90) > 1e-9) {
          fail('A rotated arc can only be scaled evenly; keep the proportions.');
        }
        [rx, ry] = Math.abs(turn - 90) <= 1e-9 ? [rx * sy, ry * sx] : [rx * sx, ry * sy];
        out.push([rx, ry, rotation, large, sweep, x, y].map(fmt).join(' '));
      } else if (upper === 'H') {
        out.push(fmt(values[0] * sx + (relative ? 0 : tx)));
      } else if (upper === 'V') {
        out.push(fmt(values[0] * sy + (relative ? 0 : ty)));
      } else {
        const moved = [];
        for (let n = 0; n < count; n += 2) {
          const x = values[n] * sx, y = values[n + 1] * sy;
          moved.push(...(relative ? [x, y] : [x + tx, y + ty]));
        }
        out.push(moved.map(fmt).join(' '));
      }
      if (upper === 'M') command = relative ? 'l' : 'L';  // extra pairs after M are line-tos
    }
    return out.map(part => /^[a-z]$/i.test(part) ? part : ' ' + part + ' ').join('').trim();
  }

  function transformElement(el, sx, sy, tx, ty) {
    const a = el.attrs, name = local(el.tag);
    const point = (xk, yk) => {
      if (xk in a) a[xk] = fmt(parseFloat(a[xk]) * sx + tx);
      if (yk in a) a[yk] = fmt(parseFloat(a[yk]) * sy + ty);
    };
    const length = (scale, ...keys) => { for (const k of keys) if (k in a) a[k] = fmt(parseFloat(a[k]) * scale); };
    if (name === 'path') {
      a.d = transformPath(a.d || '', sx, sy, tx, ty);
    } else if (name === 'circle' || name === 'ellipse') {
      if (!('cx' in a)) a.cx = '0';
      if (!('cy' in a)) a.cy = '0';
      point('cx', 'cy');
      if (name === 'circle' && Math.abs(sx - sy) > 1e-9) {
        el.tag = 'ellipse';  // a stretched circle is an ellipse
        a.rx = a.ry = a.r ?? '0';
        delete a.r;
      }
      if ('r' in a) length(sx, 'r');
      length(sx, 'rx');
      length(sy, 'ry');
    } else if (name === 'rect') {
      if (!('x' in a)) a.x = '0';
      if (!('y' in a)) a.y = '0';
      point('x', 'y');
      length(sx, 'width', 'rx');
      length(sy, 'height', 'ry');
    } else if (name === 'line') {
      point('x1', 'y1');
      point('x2', 'y2');
    } else {
      const values = (a.points || '').match(NUMBER) || [];
      a.points = values.map((v, n) => fmt(n % 2 === 0 ? +v * sx + tx : +v * sy + ty)).join(' ');
    }
  }

  function flatten(svg) {
    // Group and element transforms written into the coordinates.
    const walk = (node, t) => {
      for (const child of elementsOf(node)) {
        const own = affine(child.attrs.transform || '');
        delete child.attrs.transform;
        const [sx, sy, tx, ty] = t;
        const here = [sx * own[0], sy * own[1], tx + sx * own[2], ty + sy * own[3]];
        if (SHAPES.has(local(child.tag))) {
          if (here[0] !== 1 || here[1] !== 1 || here[2] !== 0 || here[3] !== 0) transformElement(child, ...here);
        } else {
          walk(child, here);
        }
      }
    };
    walk(svg, [1, 1, 0, 0]);
    return svg;
  }

  function drawables(svg) {
    // Drawable elements in document order, each with the attributes inherited from its groups.
    const found = [];
    const walk = (node, inherited) => {
      for (const child of elementsOf(node)) {
        const name = local(child.tag);
        if (SKIP.has(name)) continue;
        if (child.attrs.transform) fail('Artwork with transforms cannot be adjusted.');
        const own = {...inherited};
        for (const k of INHERITED) if (k in child.attrs) own[k] = child.attrs[k];
        if (SHAPES.has(name)) found.push({el: child, own});
        else if (name === 'g') walk(child, own);
      }
    };
    walk(svg, {});
    return found;
  }

  // ---- centreline bounding boxes

  function pathBox(d) {
    const tokens = d.match(new RegExp('[MmLlHhVvCcSsQqTtAaZz]|' + NUMBER.source, 'g')) || [];
    const pts = [];
    let i = 0, command = null, x = 0, y = 0, sx = 0, sy = 0, cx = null, cy = null, prev = '';
    const add = (px, py) => pts.push([px, py]);
    const cubic = (x0, y0, x1, y1, x2, y2, x3, y3) => {
      add(x3, y3);
      for (const [p0, p1, p2, p3, axis] of [[x0, x1, x2, x3, 0], [y0, y1, y2, y3, 1]]) {
        const a = -p0 + 3 * p1 - 3 * p2 + p3, b = 2 * (p0 - 2 * p1 + p2), c = p1 - p0;
        const roots = Math.abs(a) < 1e-12 ? (Math.abs(b) < 1e-12 ? [] : [-c / b])
          : (() => { const disc = b * b - 4 * a * c; if (disc < 0) return []; const s = Math.sqrt(disc); return [(-b + s) / (2 * a), (-b - s) / (2 * a)]; })();
        for (const t of roots) if (t > 0 && t < 1) {
          const mt = 1 - t;
          const px = mt ** 3 * x0 + 3 * mt * mt * t * x1 + 3 * mt * t * t * x2 + t ** 3 * x3;
          const py = mt ** 3 * y0 + 3 * mt * mt * t * y1 + 3 * mt * t * t * y2 + t ** 3 * y3;
          add(px, py);
        }
      }
    };
    const arc = (x0, y0, rx, ry, phi, large, sweep, x1, y1) => {
      add(x1, y1);
      rx = Math.abs(rx); ry = Math.abs(ry);
      if (!rx || !ry || (x0 === x1 && y0 === y1)) return;
      const r = phi * Math.PI / 180, cos = Math.cos(r), sin = Math.sin(r);
      const dx = (x0 - x1) / 2, dy = (y0 - y1) / 2;
      const xp = cos * dx + sin * dy, yp = -sin * dx + cos * dy;
      const lambda = xp * xp / (rx * rx) + yp * yp / (ry * ry);
      if (lambda > 1) { rx *= Math.sqrt(lambda); ry *= Math.sqrt(lambda); }
      const sign = large === sweep ? -1 : 1;
      const num = rx * rx * ry * ry - rx * rx * yp * yp - ry * ry * xp * xp;
      const k = sign * Math.sqrt(Math.max(0, num / (rx * rx * yp * yp + ry * ry * xp * xp)));
      const cxp = k * rx * yp / ry, cyp = -k * ry * xp / rx;
      const ccx = cos * cxp - sin * cyp + (x0 + x1) / 2, ccy = sin * cxp + cos * cyp + (y0 + y1) / 2;
      const angle = (ux, uy, vx, vy) => Math.atan2(ux * vy - uy * vx, ux * vx + uy * vy);
      const t1 = angle(1, 0, (xp - cxp) / rx, (yp - cyp) / ry);
      let dt = angle((xp - cxp) / rx, (yp - cyp) / ry, (-xp - cxp) / rx, (-yp - cyp) / ry);
      if (!sweep && dt > 0) dt -= 2 * Math.PI;
      if (sweep && dt < 0) dt += 2 * Math.PI;
      const steps = 64;
      for (let s = 1; s < steps; s++) {
        const t = t1 + dt * s / steps;
        add(ccx + rx * Math.cos(t) * cos - ry * Math.sin(t) * sin, ccy + rx * Math.cos(t) * sin + ry * Math.sin(t) * cos);
      }
    };
    while (i < tokens.length) {
      if (/^[a-z]$/i.test(tokens[i])) {
        command = tokens[i++];
        if (command === 'Z' || command === 'z') { x = sx; y = sy; prev = 'Z'; continue; }
      } else if (command === null) {
        fail('Path data must start with a command.');
      }
      const upper = command.toUpperCase(), rel = command !== upper, count = ARGS[upper];
      const v = tokens.slice(i, i + count).map(Number);
      if (v.length !== count) fail('Incomplete path data.');
      i += count;
      const ox = rel ? x : 0, oy = rel ? y : 0;
      if (upper === 'M') {
        x = v[0] + ox; y = v[1] + oy; sx = x; sy = y; add(x, y);
        command = rel ? 'l' : 'L';
      } else if (upper === 'L') {
        x = v[0] + ox; y = v[1] + oy; add(x, y);
      } else if (upper === 'H') {
        x = v[0] + (rel ? x : 0); add(x, y);
      } else if (upper === 'V') {
        y = v[0] + (rel ? y : 0); add(x, y);
      } else if (upper === 'C' || upper === 'S') {
        let x1, y1;
        if (upper === 'C') { x1 = v[0] + ox; y1 = v[1] + oy; }
        else if (prev === 'C' || prev === 'S') { x1 = 2 * x - cx; y1 = 2 * y - cy; }
        else { x1 = x; y1 = y; }
        const o = upper === 'C' ? 2 : 0;
        const x2 = v[o] + ox, y2 = v[o + 1] + oy, x3 = v[o + 2] + ox, y3 = v[o + 3] + oy;
        cubic(x, y, x1, y1, x2, y2, x3, y3);
        cx = x2; cy = y2; x = x3; y = y3;
      } else if (upper === 'Q' || upper === 'T') {
        let qx, qy;
        if (upper === 'Q') { qx = v[0] + ox; qy = v[1] + oy; }
        else if (prev === 'Q' || prev === 'T') { qx = 2 * x - cx; qy = 2 * y - cy; }
        else { qx = x; qy = y; }
        const o = upper === 'Q' ? 2 : 0;
        const x3 = v[o] + ox, y3 = v[o + 1] + oy;
        cubic(x, y, x + 2 / 3 * (qx - x), y + 2 / 3 * (qy - y), x3 + 2 / 3 * (qx - x3), y3 + 2 / 3 * (qy - y3), x3, y3);
        cx = qx; cy = qy; x = x3; y = y3;
      } else if (upper === 'A') {
        const x1 = v[5] + ox, y1 = v[6] + oy;
        arc(x, y, v[0], v[1], v[2], v[3], v[4], x1, y1);
        x = x1; y = y1;
      }
      prev = upper;
    }
    return pts;
  }

  function box(el) {
    const a = el.attrs, n = k => parseFloat(a[k] ?? '0') || 0;
    let pts;
    switch (local(el.tag)) {
      case 'path': pts = pathBox(a.d || ''); break;
      case 'circle': { const r = n('r'); pts = r > 0 ? [[n('cx') - r, n('cy') - r], [n('cx') + r, n('cy') + r]] : []; break; }
      case 'ellipse': { const rx = n('rx'), ry = n('ry'); pts = rx > 0 && ry > 0 ? [[n('cx') - rx, n('cy') - ry], [n('cx') + rx, n('cy') + ry]] : []; break; }
      case 'rect': { const w = n('width'), h = n('height'); pts = w > 0 && h > 0 ? [[n('x'), n('y')], [n('x') + w, n('y') + h]] : []; break; }
      case 'line': pts = [[n('x1'), n('y1')], [n('x2'), n('y2')]]; break;
      default: { const v = (a.points || '').match(NUMBER) || []; pts = []; for (let i = 0; i + 1 < v.length; i += 2) pts.push([+v[i], +v[i + 1]]); }
    }
    if (!pts.length) return null;
    const xs = pts.map(p => p[0]), ys = pts.map(p => p[1]);
    return [Math.min(...xs), Math.min(...ys), Math.max(...xs), Math.max(...ys)];
  }

  function union(boxes) {
    const b = boxes.filter(Boolean);
    return b.length ? [Math.min(...b.map(v => v[0])), Math.min(...b.map(v => v[1])),
                       Math.max(...b.map(v => v[2])), Math.max(...b.map(v => v[3]))] : null;
  }

  // ---- the container combination

  function fit(svg, size = BOX) {
    // (scale, tx, ty) fitting the viewBox into a size x size box, centred (preserveAspectRatio meet).
    let [vx, vy, vw, vh] = (svg.attrs.viewBox || '').replace(/,/g, ' ').trim().split(/\s+/).map(Number);
    if (!(vw > 0 && vh > 0) || [vx, vy].some(Number.isNaN)) {
      vx = 0; vy = 0;
      vw = parseFloat(svg.attrs.width) || size; vh = parseFloat(svg.attrs.height) || size;
    }
    const k = Math.min(size / vw, size / vh);
    return [k, (size - vw * k) / 2 - vx * k, (size - vh * k) / 2 - vy * k];
  }

  function checkPlacement(placement) {
    const {center, ink, box: target} = placement || {};
    if (target) {
      const ok = ['x', 'y', 'w', 'h'].every(k => Number.isFinite(target[k]) && Number.isInteger(target[k]))
        && target.w >= 0 && target.h >= 0;
      if (!ok) fail('The symbol box must be whole numbers {x, y, w, h}.');
      return;
    }
    if (!(Array.isArray(center) && center.length === 2 && center.every(v => Number.isFinite(v) && v >= 0 && v <= CANVAS))) {
      fail('The symbol center must be [x, y] inside the 64x64 canvas.');
    }
    if (ink != null && !(Array.isArray(ink) && ink.length === 2
                         && ink.every(v => Number.isInteger(v) && v % 2 === 0 && v >= 8 && v <= CANVAS))) {
      fail('The symbol size must be [width, height], each an even number from 8 to 64.');
    }
  }

  const halfUp = v => Math.floor(v + 0.5);  // Math.round, as Python's render rounds

  function symbolBox(sources, natural, center, ink) {
    const [x0, y0, x1, y1] = union(sources);
    const axis = (start, end, extent, c, size) => {
      if (extent <= 1e-9) return [halfUp(start), 0];  // a flat axis (a straight rule) keeps zero extent
      if (size == null) return [halfUp(start), Math.max(2, 2 * halfUp((end - start) / 2))];
      return [Math.trunc(c - size / 2 + STROKE / 2), Math.trunc(size - STROKE)];
    };
    const [x, w] = axis(natural[0], natural[2], x1 - x0, center[0], ink ? ink[0] : null);
    const [y, h] = axis(natural[1], natural[3], y1 - y0, center[1], ink ? ink[1] : null);
    return {x, y, w, h};
  }

  function bake(svg, found, sources, target) {
    // Every drawable element scaled on each axis and moved so the group's centreline box is `target`.
    const [x0, y0, x1, y1] = union(sources);
    const scales = [[x1 - x0, target.w], [y1 - y0, target.h]].map(([extent, size]) => {
      if (extent <= 1e-9) {
        if (size !== 0) fail('A flat element keeps zero size along its flat axis.');
        return 1;
      }
      if (size < 1) fail('An element must stay at least one unit on each axis.');
      return size / extent;
    });
    let [sx, sy] = scales;
    if (x1 - x0 <= 1e-9 && y1 - y0 > 1e-9) sx = sy;
    if (y1 - y0 <= 1e-9 && x1 - x0 > 1e-9) sy = sx;
    const dx = target.x - x0 * sx, dy = target.y - y0 * sy;
    const base = parseFloat(svg.attrs['stroke-width']) || STROKE;
    const out = [], boxes = [];
    found.forEach(({el, own}, i) => {
      if (!sources[i]) return;
      const copy = clone(el);
      Object.assign(copy.attrs, own);
      // The stroke never scales: a width other than the drawing's own keeps its ratio to it.
      if (copy.attrs['stroke-width'] != null) copy.attrs['stroke-width'] = fmt(parseFloat(copy.attrs['stroke-width']) / base * STROKE);
      delete copy.attrs.id;
      transformElement(copy, sx, sy, dx, dy);
      out.push(copy);
      boxes.push(box(copy));
    });
    const attrs = {fill: svg.attrs.fill ?? 'none', stroke: svg.attrs.stroke ?? 'currentColor', 'stroke-width': String(STROKE),
                   'stroke-linecap': svg.attrs['stroke-linecap'] ?? 'round', 'stroke-linejoin': svg.attrs['stroke-linejoin'] ?? 'round'};
    return {attrs, children: out, bounds: union(boxes)};
  }

  function container(mainSvg, symbolSvg, placement) {
    checkPlacement(placement);
    const main = flatten(parse(mainSvg)), symbol = flatten(parse(symbolSvg));
    const found = drawables(symbol);
    if (!found.length) fail('The artwork has no drawable elements.');
    const sources = found.map(f => box(f.el));
    if (!sources.some(Boolean)) fail('The artwork has no drawable elements.');
    let target = placement.box;
    if (!target) {
      const [k, fx, fy] = fit(symbol);
      const tx = placement.center[0] - BOX / 2 + fx, ty = placement.center[1] - BOX / 2 + fy;
      const [x0, y0, x1, y1] = union(sources);
      target = symbolBox(sources, [x0 * k + tx, y0 * k + ty, x1 * k + tx, y1 * k + ty], placement.center, placement.ink ?? null);
    }
    const baked = bake(symbol, found, sources, target);
    const b = baked.bounds;
    if (b[0] - STROKE / 2 < -1e-6 || b[1] - STROKE / 2 < -1e-6 || b[2] + STROKE / 2 > CANVAS + 1e-6 || b[3] + STROKE / 2 > CANVAS + 1e-6) {
      fail('The symbol extends beyond the 64x64 canvas.');
    }
    const mainFound = drawables(main);
    const mainBox = union(mainFound.map(f => box(f.el)));
    if (!mainBox) fail('The container has no drawable elements.');
    const presentation = attrs => Object.fromEntries(PRESENTATION.filter(a => attrs[a]).map(a => [a, attrs[a]]));
    const out = {tag: 'svg', attrs: {xmlns: NS, width: String(CANVAS), height: String(CANVAS), viewBox: `0 0 ${CANVAS} ${CANVAS}`,
      fill: 'none', stroke: 'currentColor', 'stroke-width': String(STROKE), 'stroke-linecap': 'round', 'stroke-linejoin': 'round'},
      children: [
        {tag: 'g', attrs: {id: 'container', ...presentation(main.attrs)},
         children: main.children.filter(c => !(c.tag && ['title', 'desc', 'metadata'].includes(local(c.tag))))},
        {tag: 'g', attrs: {id: 'symbol', ...presentation(baked.attrs)}, children: baked.children},
      ]};
    const centreline = v => ({x: v[0], y: v[1], w: v[2] - v[0], h: v[3] - v[1]});
    const painted = v => ({x: v[0] - STROKE / 2, y: v[1] - STROKE / 2, w: v[2] - v[0] + STROKE, h: v[3] - v[1] + STROKE});
    const drawn = sources.map((s, i) => s ? i : null).filter(i => i !== null);
    return {
      svg: serialize(out),
      // What reference_parts.layout stores for each part.
      layout: {container: [centreline(mainBox)], symbol: [{paths: drawn, ...target}]},
      placements: [{role: 'main', painted_box: painted(mainBox)}, {role: 'sub', painted_box: painted(b)}],
    };
  }

  return {container, CombineError, parse, serialize, transformPath, box, fmt, CANVAS, BOX, STROKE};
});
