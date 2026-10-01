/* Side pairs built in the browser: a port of the side combination engine, stroke for stroke.
 *
 *   CombineSide.render(row, request) → {svg, placements, canvas, position}
 *
 * is combination_experiment.render + vendor/combination (run_combine, box_combine.fold, the icon_combination
 * erasure) + restore_original_sub: the same placement, the same flattening of every drawing into two-point
 * segments, the same clearance area (each sub segment buffered the way GEOS buffers a line, joined with the
 * sub's convex hull), the same clipping of the main against it and the same writer, so the SVG it returns is
 * the one the Python engine returns (icon_set/tests/js/side.test.mjs checks real pairs).
 *
 * `row` is a side pair row (experiment-combination.json shape: id, position, mains, subs) and `request` the
 * render request ({main, sub, layout, margin, padding, subSizeLock, subBoundSize, mainX, mainY, subX, subY}).
 * No DOM: the page and Node run the same code.
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.CombineSide = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  const SVG = 'http://www.w3.org/2000/svg';
  const POSITIONS = {br: [1, 1], bl: [0, 1], tr: [1, 0], tl: [0, 0], ri: [1, .5], le: [0, .5], bo: [.5, 1], to: [.5, 0]};
  const GRID = 24, STROKE = 4, QUADRANT_SEGMENTS = 16;
  // The two side pair sizes: a 48 main and a 32 sub on 64 (the original), and the 72 set's 54 main and 36 sub on 72.
  // At 72 the sub is placed exactly as drawn on its 36 grid (sizeLock 'exact'); spacing is the same at both sizes.
  const SIZES = {64: {canvas: 64, main: 48, sub: 32}, 72: {canvas: 72, main: 54, sub: 36}};
  const sizeOf = size => SIZES[size ?? 64] || fail('A side pair is 64 or 72.');
  const SHAPES = ['path', 'circle', 'ellipse', 'rect', 'line', 'polyline', 'polygon'];
  const GEOM = ['path', 'circle', 'ellipse', 'rect', 'line', 'polygon', 'polyline'];
  const SKIP = ['defs', 'clipPath', 'mask', 'title', 'desc', 'metadata', 'style'];
  const INHERITED = ['fill', 'stroke', 'stroke-width', 'stroke-linecap', 'stroke-linejoin', 'stroke-miterlimit',
                     'fill-rule', 'opacity', 'stroke-opacity', 'fill-opacity'];
  const NUMBER = /[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?/g;

  class CombineError extends Error {}
  const fail = message => { throw new CombineError(message); };

  // ======== ElementTree, as far as the engine uses it ========
  // An element is {tag: '{uri}local' | 'local', attrib: {…}, text, tail, children}; comments and processing
  // instructions are dropped the way ET.fromstring drops them.

  const ENTITIES = {amp: '&', lt: '<', gt: '>', quot: '"', apos: "'"};
  const decode = s => s.replace(/&(#x[0-9a-f]+|#\d+|\w+);/gi, (m, e) => e[0] === '#'
    ? String.fromCodePoint(e[1] === 'x' || e[1] === 'X' ? parseInt(e.slice(2), 16) : +e.slice(1)) : (ENTITIES[e] ?? m));

  function parseXml(text) {
    if (/<!(DOCTYPE|ENTITY)/i.test(text)) fail('SVG with entity declarations cannot be combined.');
    const token = /<!--[\s\S]*?-->|<\?[\s\S]*?\?>|<!\[CDATA\[([\s\S]*?)\]\]>|<\/\s*([\w:.-]+)\s*>|<([\w:.-]+)((?:\s+[\w:.-]+\s*=\s*(?:"[^"]*"|'[^']*'))*)\s*(\/?)>|([^<]+)/g;
    const stack = [];
    let top = null, m, last = 0, current = null;  // `current`: the element whose text or tail grows next
    const addText = s => {
      if (!current) return;
      if (current.closed) current.el.tail = (current.el.tail ?? '') + s;
      else current.el.text = (current.el.text ?? '') + s;
    };
    while ((m = token.exec(text))) {
      if (m.index !== last) fail('The SVG could not be read.');
      last = token.lastIndex;
      if (m[2]) {
        const el = stack.pop();
        if (!el) fail('The SVG could not be read.');
        current = {el: el.node, closed: true};
      } else if (m[3]) {
        const scope = {...(stack.length ? stack[stack.length - 1].scope : {xml: 'http://www.w3.org/XML/1998/namespace'})};
        const raw = [];
        for (const a of m[4].matchAll(/([\w:.-]+)\s*=\s*(?:"([^"]*)"|'([^']*)')/g)) raw.push([a[1], decode(a[2] ?? a[3])]);
        for (const [k, v] of raw) {
          if (k === 'xmlns') scope[''] = v;
          else if (k.startsWith('xmlns:')) scope[k.slice(6)] = v;
        }
        const qualify = (name, isAttr) => {
          const i = name.indexOf(':');
          if (i < 0) return isAttr || !scope[''] ? name : `{${scope['']}}${name}`;
          const uri = scope[name.slice(0, i)];
          return uri ? `{${uri}}${name.slice(i + 1)}` : name;
        };
        const attrib = {};
        for (const [k, v] of raw) if (k !== 'xmlns' && !k.startsWith('xmlns:')) attrib[qualify(k, true)] = v;
        const node = {tag: qualify(m[3], false), attrib, text: null, tail: null, children: []};
        if (stack.length) stack[stack.length - 1].node.children.push(node);
        else if (!top) top = node;
        else fail('The SVG could not be read.');
        if (m[5]) current = {el: node, closed: true};
        else { stack.push({node, scope}); current = {el: node, closed: false}; }
      } else if (m[1] !== undefined) {
        addText(m[1]);
      } else if (m[6] !== undefined) {
        if (stack.length || top) addText(decode(m[6]));
      }
    }
    if (last !== text.length || stack.length || !top) fail('The SVG could not be read.');
    top.tail = null;
    return top;
  }

  const local = tag => tag.slice(tag.lastIndexOf('}') + 1);
  const deepcopy = el => ({tag: el.tag, attrib: {...el.attrib}, text: el.text, tail: el.tail, children: el.children.map(deepcopy)});
  function* iter(el) { yield el; for (const c of el.children) yield* iter(c); }
  const element = (tag, attrib = {}) => ({tag, attrib, text: null, tail: null, children: []});

  // ET.tostring with the SVG namespace registered as the default one.
  const escapeAttrib = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')
    .replace(/\r/g, '&#13;').replace(/\n/g, '&#10;').replace(/\t/g, '&#09;');
  const escapeText = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const WELL_KNOWN = {'http://www.w3.org/XML/1998/namespace': 'xml', 'http://www.w3.org/1999/xhtml': 'html',
                      'http://www.w3.org/1999/02/22-rdf-syntax-ns#': 'rdf', 'http://schemas.xmlsoap.org/wsdl/': 'wsdl',
                      'http://www.w3.org/2001/XMLSchema': 'xs', 'http://www.w3.org/2001/XMLSchema-instance': 'xsi',
                      'http://purl.org/dc/elements/1.1/': 'dc'};

  function tostring(rootEl) {
    const prefixes = {}, qnames = {};
    const qname = name => {
      if (name in qnames) return qnames[name];
      let out = name;
      if (name[0] === '{') {
        const uri = name.slice(1, name.indexOf('}')), tag = name.slice(name.indexOf('}') + 1);
        let prefix = uri === SVG ? '' : WELL_KNOWN[uri];
        if (prefix === undefined) prefix = prefixes[uri] ?? `ns${Object.keys(prefixes).filter(u => u !== SVG).length}`;
        if (uri !== 'http://www.w3.org/XML/1998/namespace') prefixes[uri] = prefix;
        out = prefix ? `${prefix}:${tag}` : tag;
      }
      return (qnames[name] = out);
    };
    for (const el of iter(rootEl)) { qname(el.tag); for (const k of Object.keys(el.attrib)) qname(k); }
    const declarations = Object.entries(prefixes).sort((a, b) => a[1] < b[1] ? -1 : a[1] > b[1] ? 1 : 0)
      .map(([uri, prefix]) => ` xmlns${prefix ? ':' + prefix : ''}="${escapeAttrib(uri)}"`).join('');
    const write = (el, isRoot) => {
      let out = `<${qnames[el.tag]}`;
      if (isRoot) out += declarations;
      for (const [k, v] of Object.entries(el.attrib)) out += ` ${qnames[k]}="${escapeAttrib(String(v))}"`;
      if (el.text || el.children.length) {
        out += '>' + (el.text ? escapeText(el.text) : '') + el.children.map(c => write(c, false)).join('') + `</${qnames[el.tag]}>`;
      } else {
        out += ' />';
      }
      return out + (el.tail ? escapeText(el.tail) : '');
    };
    return write(rootEl, true);
  }

  // ET path queries the engine uses: './/{uri}tag', './/tag' (no namespace), './/{*}tag'.
  function findall(rootEl, kind, name) {
    const out = [];
    for (const el of iter(rootEl)) {
      if (el === rootEl) continue;
      const tag = el.tag, i = tag.indexOf('}');
      if (kind === 'svg' ? tag === `{${SVG}}${name}` : kind === 'none' ? tag === name : (i < 0 ? tag : tag.slice(i + 1)) === name) out.push(el);
    }
    return out;
  }
  function removeChild(parent, el) {
    const i = parent.children.indexOf(el);
    if (i < 0) fail('The SVG could not be read.');
    parent.children.splice(i, 1);
  }

  // ======== Python number formatting ========

  function pyFixed2(x) {  // f"{x:.2f}": exact ties (odd eighths) round half to even
    if (Object.is(x, -0)) return '-0.00';
    const e = x * 8;
    if (Number.isInteger(e) && e % 2 !== 0) {
      const lo = Math.floor(x * 100), pick = lo % 2 === 0 ? lo : lo + 1;
      const s = (Math.abs(pick) / 100).toFixed(2);
      return (x < 0 ? '-' : '') + s;
    }
    const s = x.toFixed(2);
    return s === '0.00' && x < 0 ? '-0.00' : s;
  }

  function pyG12(x) {  // f"{x:.12g}"
    if (x === 0) return Object.is(x, -0) ? '-0' : '0';
    const [mantissa, exp] = x.toExponential(11).split('e');
    const e = +exp;
    if (e < -4 || e >= 12) {
      const m = mantissa.replace(/\.?0+$/, '');
      return `${m}e${e < 0 ? '-' : '+'}${String(Math.abs(e)).padStart(2, '0')}`;
    }
    return x.toFixed(Math.max(0, 11 - e)).replace(/(\.\d*?)0+$/, '$1').replace(/\.$/, '');
  }

  function pyStr(x) {  // str(float)
    if (Number.isInteger(x) && Math.abs(x) < 1e16) return x.toFixed(1);
    if (Math.abs(x) >= 1e16 || (x !== 0 && Math.abs(x) < 1e-4)) {
      const [m, e] = x.toExponential().split('e');
      return `${m}e${e[0] === '-' ? '-' : '+'}${e.replace(/^[-+]/, '').padStart(2, '0')}`;
    }
    return String(x);
  }

  function fmt(n) {  // round(n, 6) then '%.6f' without trailing zeros: exact ties (odd 128ths) round half to even
    let s = n.toFixed(6);
    if (Number.isInteger(n * 128) && (n * 128) % 2 !== 0) {
      const scaled = n * 1e6, lo = Math.floor(scaled), pick = lo % 2 === 0 ? lo : lo + 1;
      s = (pick / 1e6).toFixed(6);
    }
    return Number(s) === 0 ? '0' : s.replace(/0+$/, '').replace(/\.$/, '');
  }

  // ======== the engine's flattening (icon_combination/utils.py) ========

  // x ** 2 and x ** 3 as Python computes them (libm pow, correctly rounded but for rare cases): V8's `**` is
  // not, and a curve point landing on a 2-decimal tie then rounds the other way.
  const split = a => { const c = 134217729 * a, hi = c - (c - a); return [hi, a - hi]; };
  const twoProduct = (a, b) => {
    const p = a * b, [ah, al] = split(a), [bh, bl] = split(b);
    return [p, ((ah * bh - p) + ah * bl + al * bh) + al * bl];
  };
  const square = x => x * x;
  const cube = x => { const [s, se] = twoProduct(x, x), [p, pe] = twoProduct(s, x); return p + (pe + se * x); };

  function parseSvgPath(d, curveSegments = 20) {
    const lines = [];
    let current = [0, 0], start = [0, 0];
    const cubic = (t, p0, p1, p2, p3) => [
      cube(1 - t) * p0[0] + 3 * square(1 - t) * t * p1[0] + 3 * (1 - t) * square(t) * p2[0] + cube(t) * p3[0],
      cube(1 - t) * p0[1] + 3 * square(1 - t) * t * p1[1] + 3 * (1 - t) * square(t) * p2[1] + cube(t) * p3[1]];
    const quadratic = (t, p0, p1, p2) => [
      square(1 - t) * p0[0] + 2 * (1 - t) * t * p1[0] + square(t) * p2[0],
      square(1 - t) * p0[1] + 2 * (1 - t) * t * p1[1] + square(t) * p2[1]];
    const arc = (sx, sy, rx, ry, rotation, large, sweep, ex, ey, segments) => {
      if ((sx === ex && sy === ey) || rx === 0 || ry === 0) return [[[sx, sy], [ex, ey]]];
      rx = Math.abs(rx); ry = Math.abs(ry);
      const phi = rotation * (Math.PI / 180), cosPhi = Math.cos(phi), sinPhi = Math.sin(phi);
      const dx = (sx - ex) / 2.0, dy = (sy - ey) / 2.0;
      const x1p = cosPhi * dx + sinPhi * dy, y1p = -sinPhi * dx + cosPhi * dy;
      const lambda = (x1p * x1p) / (rx * rx) + (y1p * y1p) / (ry * ry);
      if (lambda > 1) { rx *= Math.sqrt(lambda); ry *= Math.sqrt(lambda); }
      const sign = large === sweep ? -1 : 1;
      let sq = ((rx * rx) * (ry * ry) - (rx * rx) * (y1p * y1p) - (ry * ry) * (x1p * x1p));
      if (sq < 0) sq = 0;
      const coeff = sign * Math.sqrt(sq / ((rx * rx) * (y1p * y1p) + (ry * ry) * (x1p * x1p)));
      const cxp = coeff * ((rx * y1p) / ry), cyp = coeff * (-(ry * x1p) / rx);
      const cx = cosPhi * cxp - sinPhi * cyp + (sx + ex) / 2, cy = sinPhi * cxp + cosPhi * cyp + (sy + ey) / 2;
      const between = (ux, uy, vx, vy) => Math.atan2(ux * vy - uy * vx, ux * vx + uy * vy);
      const ux = (x1p - cxp) / rx, uy = (y1p - cyp) / ry, vx = (-x1p - cxp) / rx, vy = (-y1p - cyp) / ry;
      const theta1 = between(1, 0, ux, uy);
      let dtheta = between(ux, uy, vx, vy);
      if (sweep === 0 && dtheta > 0) dtheta -= 2 * Math.PI;
      else if (sweep === 1 && dtheta < 0) dtheta += 2 * Math.PI;
      const out = [];
      for (let i = 0; i < segments; i++) {
        const a1 = theta1 + (i / segments) * dtheta, a2 = theta1 + ((i + 1) / segments) * dtheta;
        const x1 = rx * Math.cos(a1), y1 = ry * Math.sin(a1), x2 = rx * Math.cos(a2), y2 = ry * Math.sin(a2);
        out.push([[cosPhi * x1 - sinPhi * y1 + cx, sinPhi * x1 + cosPhi * y1 + cy],
                  [cosPhi * x2 - sinPhi * y2 + cx, sinPhi * x2 + cosPhi * y2 + cy]]);
      }
      return out;
    };
    for (const [, cmd, params] of d.matchAll(/([MLHVZCQTSAmlhvzcqtsa])\s*([^MLHVZCQTSAmlhvzcqtsa]*)/g)) {
      const n = (params.match(NUMBER) || []).map(Number);
      const rel = cmd === cmd.toLowerCase();
      switch (cmd.toUpperCase()) {
        case 'M':
          for (let i = 0; i + 1 < n.length; i += 2) {
            current = rel ? [current[0] + n[i], current[1] + n[i + 1]] : [n[i], n[i + 1]];
            start = current;
          }
          break;
        case 'L':
          for (let i = 0; i + 1 < n.length; i += 2) {
            const prev = current;
            current = rel ? [current[0] + n[i], current[1] + n[i + 1]] : [n[i], n[i + 1]];
            lines.push([prev, current]);
          }
          break;
        case 'H':
          for (const x of n) { const prev = current; current = rel ? [current[0] + x, current[1]] : [x, current[1]]; lines.push([prev, current]); }
          break;
        case 'V':
          for (const y of n) { const prev = current; current = rel ? [current[0], current[1] + y] : [current[0], y]; lines.push([prev, current]); }
          break;
        case 'C':
          for (let i = 0; i + 5 < n.length; i += 6) {
            const c1 = rel ? [current[0] + n[i], current[1] + n[i + 1]] : [n[i], n[i + 1]];
            const c2 = rel ? [current[0] + n[i + 2], current[1] + n[i + 3]] : [n[i + 2], n[i + 3]];
            const end = rel ? [current[0] + n[i + 4], current[1] + n[i + 5]] : [n[i + 4], n[i + 5]];
            const s = current;
            for (let j = 0; j < curveSegments; j++) lines.push([cubic(j / curveSegments, s, c1, c2, end), cubic((j + 1) / curveSegments, s, c1, c2, end)]);
            current = end;
          }
          break;
        case 'Q':
          for (let i = 0; i + 3 < n.length; i += 4) {
            const c = rel ? [current[0] + n[i], current[1] + n[i + 1]] : [n[i], n[i + 1]];
            const end = rel ? [current[0] + n[i + 2], current[1] + n[i + 3]] : [n[i + 2], n[i + 3]];
            const s = current;
            for (let j = 0; j < curveSegments; j++) lines.push([quadratic(j / curveSegments, s, c, end), quadratic((j + 1) / curveSegments, s, c, end)]);
            current = end;
          }
          break;
        case 'A':
          for (let i = 0; i + 6 < n.length; i += 7) {
            const end = rel ? [current[0] + n[i + 5], current[1] + n[i + 6]] : [n[i + 5], n[i + 6]];
            lines.push(...arc(current[0], current[1], n[i], n[i + 1], n[i + 2], Math.trunc(n[i + 3]), Math.trunc(n[i + 4]), end[0], end[1], curveSegments));
            current = end;
          }
          break;
        case 'Z':
          if (current[0] !== start[0] || current[1] !== start[1]) { lines.push([current, start]); current = start; }
          break;
        // S and T are ignored by the engine.
      }
    }
    return lines;
  }

  function lineSegments(x1, y1, x2, y2, spacing = 1.0) {
    const distance = Math.sqrt(square(x2 - x1) + square(y2 - y1));
    if (distance <= spacing) return [[[x1, y1], [x2, y2]]];
    const count = Math.max(1, Math.trunc(distance / spacing)), out = [];
    for (let i = 0; i < count; i++) {
      const t1 = i / count, t2 = (i + 1) / count;
      out.push([[x1 + t1 * (x2 - x1), y1 + t1 * (y2 - y1)], [x1 + t2 * (x2 - x1), y1 + t2 * (y2 - y1)]]);
    }
    return out;
  }
  function circleSegments(cx, cy, r, spacing = 1.0) {
    const count = Math.max(8, Math.trunc(2 * Math.PI * r / spacing)), step = 2 * Math.PI / count, out = [];
    for (let i = 0; i < count; i++) {
      const a1 = i * step, a2 = (i + 1) * step;
      out.push([[cx + r * Math.cos(a1), cy + r * Math.sin(a1)], [cx + r * Math.cos(a2), cy + r * Math.sin(a2)]]);
    }
    return out;
  }
  function ellipseSegments(cx, cy, rx, ry, spacing = 1.0) {
    const h = square((rx - ry) / (rx + ry));
    const perimeter = Math.PI * (rx + ry) * (1 + (3 * h) / (10 + Math.sqrt(4 - 3 * h)));
    const count = Math.max(8, Math.trunc(perimeter / spacing)), step = 2 * Math.PI / count, out = [];
    for (let i = 0; i < count; i++) {
      const a1 = i * step, a2 = (i + 1) * step;
      out.push([[cx + rx * Math.cos(a1), cy + ry * Math.sin(a1)], [cx + rx * Math.cos(a2), cy + ry * Math.sin(a2)]]);
    }
    return out;
  }
  function arcSegments(cx, cy, rx, ry, a0, a1, spacing = 1.0) {
    const count = Math.max(4, Math.trunc(Math.abs(a1 - a0) * ((rx + ry) / 2) / Math.max(spacing, 0.5))), out = [];
    for (let i = 0; i < count; i++) {
      const t1 = a0 + (a1 - a0) * (i / count), t2 = a0 + (a1 - a0) * ((i + 1) / count);
      out.push([[cx + rx * Math.cos(t1), cy + ry * Math.sin(t1)], [cx + rx * Math.cos(t2), cy + ry * Math.sin(t2)]]);
    }
    return out;
  }
  function rectSegments(x, y, w, h, spacing, rx, ry) {
    rx = Math.min(Math.max(0.0, rx || 0.0), w / 2);
    ry = Math.min(Math.max(0.0, ry || 0.0), h / 2);
    if (rx === 0 || ry === 0) {
      return [...lineSegments(x, y, x + w, y, spacing), ...lineSegments(x + w, y, x + w, y + h, spacing),
              ...lineSegments(x + w, y + h, x, y + h, spacing), ...lineSegments(x, y + h, x, y, spacing)];
    }
    return [...lineSegments(x + rx, y, x + w - rx, y, spacing), ...arcSegments(x + w - rx, y + ry, rx, ry, -Math.PI / 2, 0.0, spacing),
            ...lineSegments(x + w, y + ry, x + w, y + h - ry, spacing), ...arcSegments(x + w - rx, y + h - ry, rx, ry, 0.0, Math.PI / 2, spacing),
            ...lineSegments(x + w - rx, y + h, x + rx, y + h, spacing), ...arcSegments(x + rx, y + h - ry, rx, ry, Math.PI / 2, Math.PI, spacing),
            ...lineSegments(x, y + h - ry, x, y + ry, spacing), ...arcSegments(x + rx, y + ry, rx, ry, Math.PI, 3 * Math.PI / 2, spacing)];
  }
  function pointsOf(text) {
    const c = text.match(/[-+]?(?:\d*\.?\d+)/g) || [];
    if (c.length < 4) return null;
    const pts = [];
    for (let i = 0; i < c.length - 1; i += 2) pts.push([+c[i], +c[i + 1]]);
    return pts;
  }
  const pyFloat = (value, fallback = 0.0) => {
    if (value == null || !String(value).trim()) return fallback;
    const n = Number(String(value).trim());
    return Number.isNaN(n) ? fallback : n;
  };
  const pyFloatStrict = value => {  // float(x) with no fallback: a bad value fails the whole parse
    const n = Number(String(value).trim());
    if (String(value).trim() === '' || Number.isNaN(n)) fail('The SVG has a number that cannot be read.');
    return n;
  };

  function removeClipPathElements(rootEl) {
    for (const el of iter(rootEl)) delete el.attrib['clip-path'];
    const preserved = [];
    for (const container of ['defs', 'clipPath', 'mask']) {
      for (const holder of findall(rootEl, 'svg', container)) {
        for (const geom of ['circle', 'ellipse', 'rect', 'line', 'polygon', 'polyline', 'path']) {
          preserved.push(...findall(holder, 'svg', geom), ...findall(holder, 'none', geom));
        }
      }
    }
    for (const el of preserved) rootEl.children.push(el);
    for (const container of ['defs', 'clipPath', 'mask']) {
      for (const holder of findall(rootEl, 'svg', container)) {
        for (const parent of iter(rootEl)) if (parent.children.includes(holder)) { removeChild(parent, holder); break; }
      }
    }
  }

  function stripUnstroked(rootEl) {
    const inherited = (el, stroke) => {
      const s = 'stroke' in el.attrib ? el.attrib.stroke : stroke;
      return (s || 'none').trim().toLowerCase() === 'none' ? null : s;
    };
    const prune = (parent, stroke) => {
      for (const el of [...parent.children]) {
        const s = inherited(el, stroke);
        if (GEOM.includes(local(el.tag).toLowerCase())) { if (s === null) removeChild(parent, el); continue; }
        prune(el, s);
      }
    };
    prune(rootEl, inherited(rootEl, null));
  }

  function parseGeometry(rootEl, spacing = 1.0) {
    for (const style of findall(rootEl, 'svg', 'style')) {
      // root.find('.//{svg}style/..'): the parent of the first style left, in document order.
      const first = findall(rootEl, 'svg', 'style')[0];
      const parent = first && [...iter(rootEl)].find(el => el.children.includes(first));
      removeChild(parent || rootEl, style);
    }
    removeClipPathElements(rootEl);
    for (const el of iter(rootEl)) delete el.attrib.style;
    const segments = [];
    const both = name => [...findall(rootEl, 'svg', name), ...findall(rootEl, 'none', name), ...findall(rootEl, 'any', name)];
    for (const path of both('path')) {
      const d = path.attrib.d;
      if (d) segments.push(...parseSvgPath(d));
    }
    const once = name => {
      const seen = new Set(), out = [];
      for (const el of [...findall(rootEl, 'svg', name), ...findall(rootEl, 'none', name), ...findall(rootEl, 'any', name)]) {
        if (!seen.has(el)) { seen.add(el); out.push(el); }
      }
      return out;
    };
    for (const c of once('circle')) {
      const r = pyFloat(c.attrib.r ?? '0');
      if (r > 0) segments.push(...circleSegments(pyFloat(c.attrib.cx ?? '0'), pyFloat(c.attrib.cy ?? '0'), r, spacing));
    }
    for (const r of once('rect')) {
      const x = pyFloat(r.attrib.x), y = pyFloat(r.attrib.y), w = pyFloat(r.attrib.width), h = pyFloat(r.attrib.height);
      let rx = 'rx' in r.attrib ? pyFloat(r.attrib.rx) : null, ry = 'ry' in r.attrib ? pyFloat(r.attrib.ry) : null;
      if (rx === null && ry === null) { rx = 0.0; ry = 0.0; } else if (rx === null) rx = ry; else if (ry === null) ry = rx;
      if (w > 0 && h > 0) segments.push(...rectSegments(x, y, w, h, spacing, rx, ry));
    }
    for (const e of both('ellipse')) {
      const cx = pyFloatStrict(e.attrib.cx ?? 0), cy = pyFloatStrict(e.attrib.cy ?? 0), rx = pyFloatStrict(e.attrib.rx ?? 0), ry = pyFloatStrict(e.attrib.ry ?? 0);
      if (rx > 0 && ry > 0) segments.push(...ellipseSegments(cx, cy, rx, ry, spacing));
    }
    for (const p of both('polygon')) {
      const text = p.attrib.points || '';
      const pts = text.trim() ? pointsOf(text) : null;
      if (pts) for (let i = 0; i < pts.length; i++) { const a = pts[i], b = pts[(i + 1) % pts.length]; segments.push(...lineSegments(a[0], a[1], b[0], b[1], spacing)); }
    }
    for (const p of both('polyline')) {
      const text = p.attrib.points || '';
      const pts = text.trim() ? pointsOf(text) : null;
      if (pts) for (let i = 0; i + 1 < pts.length; i++) segments.push(...lineSegments(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], spacing));
    }
    for (const l of both('line')) {
      segments.push(...lineSegments(pyFloatStrict(l.attrib.x1 ?? 0), pyFloatStrict(l.attrib.y1 ?? 0), pyFloatStrict(l.attrib.x2 ?? 0), pyFloatStrict(l.attrib.y2 ?? 0), spacing));
    }
    return segments;
  }

  // box_combine.parse_segments: the engine's reading of one drawing.
  function engineSegments(svgText) {
    const rootEl = parseXml(svgText);
    removeClipPathElements(rootEl);
    stripUnstroked(rootEl);
    const segments = parseGeometry(rootEl, 1);
    if (!segments.length) fail('combine failed: no drawable geometry');
    return segments;
  }

  // combination_layout_svg.segments_of: one element on its own, as the engine flattens it.
  function segmentsOf(el, strokeAttrs) {
    const rootEl = element(`{${SVG}}svg`, {stroke: 'currentColor', ...strokeAttrs});
    rootEl.children.push(deepcopy(el));
    return parseGeometry(rootEl, 1);
  }

  function bbox(segments) {
    if (!segments.length) return null;
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    for (const [a, b] of segments) {
      if (a[0] < x0) x0 = a[0]; if (b[0] < x0) x0 = b[0]; if (a[0] > x1) x1 = a[0]; if (b[0] > x1) x1 = b[0];
      if (a[1] < y0) y0 = a[1]; if (b[1] < y0) y0 = b[1]; if (a[1] > y1) y1 = a[1]; if (b[1] > y1) y1 = b[1];
    }
    return [x0, y0, x1, y1];
  }
  const union = boxes => {
    const b = boxes.filter(Boolean);
    return b.length ? [Math.min(...b.map(v => v[0])), Math.min(...b.map(v => v[1])), Math.max(...b.map(v => v[2])), Math.max(...b.map(v => v[3]))] : null;
  };

  // ======== placement (combination_experiment.py) ========

  function number(value, fallback = 0) {
    if (value === null || value === undefined || value === '') return fallback;
    const n = typeof value === 'number' ? value : typeof value === 'boolean' ? +value : Number(String(value).trim());
    if (!Number.isFinite(n)) fail('Offsets must be numbers.');
    if (Math.abs(n) > 64) fail('Offsets must be between -64 and 64.');
    return n;
  }

  function placement(item, size, anchor, offset, padding = 2, sizeLock = 'none', boundSize = null, canvas = 64) {
    const [x0, y0, x1, y1] = item.bounds;
    const [ax, ay] = anchor;
    const mode = item.sizing_mode;
    if (mode === 'typeface-native') {
      if (!['none', 'auto'].includes(sizeLock) || !(boundSize === null || boundSize === undefined || boundSize === '')) fail('Native typeface keeps its original size.');
      const w = x1 - x0 + 4, h = y1 - y0 + 4;
      if (Math.max(w, h) > canvas - 2 * padding + 1e-8) fail('Native text needs a larger combination canvas.');
      const x = padding + (canvas - 2 * padding - w) * ax + offset[0], y = padding + (canvas - 2 * padding - h) * ay + offset[1];
      return {size_lock: 'none', locked_axis: null, rounded_box: false, locked_size: null,
              canvas_box: {x, y, w, h}, painted_box: {x, y, w, h},
              box: {x: (x + 2) * 24 / canvas, y: (y + 2) * 24 / canvas, w: (w - 4) * 24 / canvas, h: (h - 4) * 24 / canvas}};
    }
    if (mode === 'container-content-resize') {
      const cw = item.canvas_width, ch = item.canvas_height;
      if (size !== 32 || [cw, ch].some(v => !Number.isInteger(v) || !(4 <= v && v <= 60))) fail('Container resize artwork requires its declared integer dimensions.');
      if (!['none', 'auto'].includes(sizeLock) || !(boundSize === null || boundSize === undefined || boundSize === '')) fail('Resize variants keep their authored dimensions; select another model to change size.');
      const w = x1 - x0 + 4, h = y1 - y0 + 4;
      if (Math.abs(w - cw) > 1e-8 || Math.abs(h - ch) > 1e-8) fail('Resize artwork does not match its declared ink dimensions.');
      const x = pyRound(padding + (canvas - 2 * padding - cw) * ax + offset[0]), y = pyRound(padding + (canvas - 2 * padding - ch) * ay + offset[1]);
      return {size_lock: 'none', locked_axis: null, rounded_box: false, locked_size: null,
              canvas_box: {x, y, w: cw, h: ch}, painted_box: {x, y, w, h},
              box: {x: (x + 2) * 24 / canvas, y: (y + 2) * 24 / canvas, w: (w - 4) * 24 / canvas, h: (h - 4) * 24 / canvas}};
    }
    if (['side-32x48', 'side-one-axis32', 'side-source-fit'].includes(mode)) {
      const cw = item.canvas_width, ch = item.canvas_height;
      if (size !== 32 || !Number.isInteger(cw) || !Number.isInteger(ch) || Math.min(cw, ch) < 32 || (mode !== 'side-source-fit' && cw !== 32 && ch !== 32)) {
        fail('Side artwork requires one 32px canvas dimension.');
      }
      if (!['none', 'auto'].includes(sizeLock) || !(boundSize === null || boundSize === undefined || boundSize === '')) fail('Side artwork keeps its original 32×48 or declared exception size.');
      if (cw > canvas - 2 * padding || ch > canvas - 2 * padding) fail('Source-faithful artwork needs a larger combination canvas; it cannot be shrunk to fit.');
      const w = x1 - x0 + 4, h = y1 - y0 + 4;
      if (w > cw || h > ch) fail('Tall side artwork exceeds its 32×48 canvas.');
      const bx = padding + (canvas - 2 * padding - cw) * ax, by = padding + (canvas - 2 * padding - ch) * ay;
      const x = bx + (cw - w) * ax + offset[0], y = by + (ch - h) * ay + offset[1];
      return {size_lock: 'none', locked_axis: null, rounded_box: false, locked_size: null,
              canvas_box: {x: bx, y: by, w: cw, h: ch}, painted_box: {x, y, w, h},
              box: {x: (x + 2) * 24 / canvas, y: (y + 2) * 24 / canvas, w: (w - 4) * 24 / canvas, h: (h - 4) * 24 / canvas}};
    }
    if (sizeLock === 'exact') {
      // As drawn: its own grid placed at the anchor, the drawing where it sits on that grid, not scaled.
      if (item.canvas !== size) fail(`The sub must be drawn on the ${size} grid to be placed as drawn.`);
      const bx = padding + (canvas - 2 * padding - size) * ax, by = padding + (canvas - 2 * padding - size) * ay;
      const x = bx + x0 - 2 + offset[0], y = by + y0 - 2 + offset[1], w = x1 - x0 + 4, h = y1 - y0 + 4;
      return {size_lock: 'exact', locked_axis: null, rounded_box: false, locked_size: null,
              canvas_box: {x: bx, y: by, w: size, h: size}, painted_box: {x, y, w, h},
              box: {x: (x + 2) * 24 / canvas, y: (y + 2) * 24 / canvas, w: (w - 4) * 24 / canvas, h: (h - 4) * 24 / canvas}};
    }
    let scale = size / item.canvas;
    let w = (x1 - x0) * scale, h = (y1 - y0) * scale;
    if (!['none', 'auto', 'width', 'height'].includes(sizeLock)) fail('Choose automatic, width, height, or original sub sizing.');
    let lockedAxis = null;
    const roundedAuto = size === 32 && sizeLock === 'auto' && (boundSize === null || boundSize === undefined || boundSize === '');
    if (roundedAuto) {
      const width = x1 - x0, height = y1 - y0, longest = Math.max(width, height);
      if (longest <= 0) fail('Cannot normalize empty sub geometry.');
      scale = (size - 4) / longest;
      w = width * scale; h = height * scale;
      lockedAxis = w >= h ? 'width' : 'height';
    } else if (sizeLock !== 'none') {
      lockedAxis = sizeLock === 'auto' ? (w >= h ? 'width' : 'height') : sizeLock;
      const extent = lockedAxis === 'width' ? (x1 - x0) : (y1 - y0);
      if (extent <= 0) fail('Cannot lock an empty dimension; choose the other axis.');
      const maxTarget = 4 + (size - 4) * extent / Math.max(x1 - x0, y1 - y0);
      const current = (lockedAxis === 'width' ? w : h) + 4;
      let target;
      if (boundSize === null || boundSize === undefined || boundSize === '') {
        target = Math.max(5, Math.min(Math.floor(current + .5), Math.floor(maxTarget + 1e-9)));
      } else {
        target = number(boundSize);
        if (target !== Math.trunc(target) || !(5 <= target && target <= size)) fail(`Locked visible size must be a whole number from 5 to ${size}.`);
      }
      scale = (target - 4) / extent;
      w = (x1 - x0) * scale; h = (y1 - y0) * scale;
    }
    if (Math.max(w, h) + 4 > size + .01) fail(`Artwork exceeds its ${size}×${size} component canvas.`);
    const bx = padding + (canvas - 2 * padding - size) * ax, by = padding + (canvas - 2 * padding - size) * ay;
    const x = bx + (size - w - 4) * ax + offset[0], y = by + (size - h - 4) * ay + offset[1];
    return {size_lock: sizeLock, locked_axis: lockedAxis, rounded_box: false,
            locked_size: lockedAxis ? (lockedAxis === 'width' ? w + 4 : h + 4) : null,
            canvas_box: {x: bx, y: by, w: size, h: size}, painted_box: {x, y, w: w + 4, h: h + 4},
            box: {x: (x + 2) * 24 / canvas, y: (y + 2) * 24 / canvas, w: w * 24 / canvas, h: h * 24 / canvas}};
  }

  function pyRound(v) {  // round(): half to even
    const f = Math.floor(v), d = v - f;
    if (d > .5) return f + 1;
    if (d < .5) return f;
    return f % 2 === 0 ? f : f + 1;
  }

  function layoutPlacement(bounds, canvas = 64) {
    const [x0, y0, x1, y1] = bounds;
    return {size_lock: 'none', locked_axis: null, rounded_box: false, locked_size: null,
            canvas_box: {x: 0, y: 0, w: canvas, h: canvas},
            painted_box: {x: x0 - 2, y: y0 - 2, w: x1 - x0 + 4, h: y1 - y0 + 4},
            box: {x: x0 * 24 / canvas, y: y0 * 24 / canvas, w: (x1 - x0) * 24 / canvas, h: (y1 - y0) * 24 / canvas}};
  }

  function checkLayout(layout) {
    if (layout === null || layout === undefined) return null;
    if (typeof layout !== 'object' || Array.isArray(layout) || !Object.keys(layout).every(k => k === 'main' || k === 'sub')) {
      fail('A layout lists groups for the main and/or the sub.');
    }
    const clean = {};
    for (const [role, groups] of Object.entries(layout)) {
      if (groups === null || groups === undefined) continue;
      if (!Array.isArray(groups) || !groups.length || groups.length > 64) fail(`List the ${role} element groups.`);
      clean[role] = groups.map(g => {
        if (!g || typeof g !== 'object' || !Array.isArray(g.paths) || !g.paths.length || g.paths.some(i => !Number.isInteger(i) || i < 0)) {
          fail(`Each ${role} group needs its element numbers.`);
        }
        const values = {};
        for (const k of ['x', 'y', 'w', 'h']) {
          const v = g[k];
          if (typeof v !== 'number' || !Number.isFinite(v) || v !== Math.trunc(v)) fail(`${role} ${k} must snap to a whole grid unit.`);
          values[k] = Math.trunc(v);
        }
        if (!(-64 <= values.x && values.x <= 256) || !(-64 <= values.y && values.y <= 256) || !(0 <= values.w && values.w <= 256) || !(0 <= values.h && values.h <= 256)) {
          fail(`The ${role} layout is outside the canvas.`);
        }
        return {paths: [...g.paths], ...values};
      });
    }
    return Object.keys(clean).length ? clean : null;
  }

  // ======== baking a hand-adjusted layout (combination_layout_svg.component) ========

  function drawables(rootEl) {
    const found = [];
    const walk = (node, inherited) => {
      for (const child of node.children) {
        const name = local(child.tag);
        if (SKIP.includes(name)) continue;
        if (child.attrib.transform) fail('Artwork with transforms cannot be adjusted.');
        const own = {...inherited};
        for (const k of INHERITED) if (k in child.attrib) own[k] = child.attrib[k];
        if (SHAPES.includes(name)) found.push([child, own]);
        else if (name === 'g') walk(child, own);
      }
    };
    walk(rootEl, {});
    return found;
  }

  function transformPath(d, sx, sy, tx, ty) {
    const ARGS = {M: 2, L: 2, T: 2, H: 1, V: 1, C: 6, S: 4, Q: 4, A: 7, Z: 0};
    const tokens = d.match(new RegExp('[MmLlHhVvCcSsQqTtAaZz]|' + NUMBER.source, 'g')) || [];
    const out = [];
    let i = 0, command = null;
    while (i < tokens.length) {
      if (/^[a-z]$/i.test(tokens[i])) {
        command = tokens[i++];
        out.push(command);
        if (command === 'Z' || command === 'z') continue;
      } else if (command === null) fail('Path data must start with a command.');
      const upper = command.toUpperCase(), relative = command !== upper, count = ARGS[upper];
      const values = tokens.slice(i, i + count).map(Number);
      if (values.length !== count) fail('Incomplete path data.');
      i += count;
      if (upper === 'A') {
        let [rx, ry, rotation, large, sweep, x, y] = values;
        [x, y] = relative ? [x * sx, y * sy] : [x * sx + tx, y * sy + ty];
        const turn = ((rotation % 180) + 180) % 180;
        if (Math.abs(sx - sy) > 1e-9 && Math.min(turn, 180 - turn) > 1e-9 && Math.abs(turn - 90) > 1e-9) fail('A rotated arc can only be scaled evenly; keep the proportions.');
        [rx, ry] = Math.abs(turn - 90) <= 1e-9 ? [rx * sy, ry * sx] : [rx * sx, ry * sy];
        out.push([rx, ry, rotation, large, sweep, x, y].map(fmt).join(' '));
      } else if (upper === 'H') out.push(fmt(values[0] * sx + (relative ? 0 : tx)));
      else if (upper === 'V') out.push(fmt(values[0] * sy + (relative ? 0 : ty)));
      else {
        const moved = [];
        for (let n = 0; n < count; n += 2) { const x = values[n] * sx, y = values[n + 1] * sy; moved.push(...(relative ? [x, y] : [x + tx, y + ty])); }
        out.push(moved.map(fmt).join(' '));
      }
      if (upper === 'M') command = relative ? 'l' : 'L';
    }
    return out.map(part => /^[a-z]$/i.test(part) ? part : ' ' + part + ' ').join('').trim();
  }

  function transformElement(el, sx, sy, tx, ty) {
    const a = el.attrib, name = local(el.tag);
    const point = (xk, yk) => { if (xk in a) a[xk] = fmt(parseFloat(a[xk]) * sx + tx); if (yk in a) a[yk] = fmt(parseFloat(a[yk]) * sy + ty); };
    const length = (scale, ...keys) => { for (const k of keys) if (k in a) a[k] = fmt(parseFloat(a[k]) * scale); };
    if (name === 'path') a.d = transformPath(a.d || '', sx, sy, tx, ty);
    else if (name === 'circle' || name === 'ellipse') {
      if (!('cx' in a)) a.cx = '0';
      if (!('cy' in a)) a.cy = '0';
      point('cx', 'cy');
      if (name === 'circle' && Math.abs(sx - sy) > 1e-9) {
        el.tag = el.tag.slice(0, -'circle'.length) + 'ellipse';
        const r = a.r ?? '0'; delete a.r; a.rx = r; a.ry = r;
      }
      if ('r' in a) length(sx, 'r');
      length(sx, 'rx'); length(sy, 'ry');
    } else if (name === 'rect') {
      if (!('x' in a)) a.x = '0';
      if (!('y' in a)) a.y = '0';
      point('x', 'y'); length(sx, 'width', 'rx'); length(sy, 'height', 'ry');
    } else if (name === 'line') { point('x1', 'y1'); point('x2', 'y2'); }
    else {
      const values = (a.points || '').match(NUMBER) || [];
      a.points = values.map((v, n) => fmt(n % 2 === 0 ? +v * sx + tx : +v * sy + ty)).join(' ');
    }
  }

  function bake(role, documentText, layout, canvas) {
    const rootEl = parseXml(documentText);
    const base = parseFloat(rootEl.attrib['stroke-width'] || String(STROKE)) || STROKE;
    const found = drawables(rootEl);
    if (!found.length) fail('The artwork has no drawable elements.');
    const strokeAttrs = Object.fromEntries(Object.entries(rootEl.attrib).filter(([k]) => INHERITED.includes(k)));
    const source = found.map(([el, own]) => bbox(segmentsOf(el, {...strokeAttrs, ...own})));
    const drawable = source.map((b, i) => b ? i : null).filter(i => i !== null);
    const seen = layout.flatMap(g => g.paths).sort((a, b) => a - b);
    if (seen.length !== drawable.length || seen.some((v, i) => v !== drawable[i])) fail(`Each element of the ${role} must be placed exactly once.`);
    const out = element(`{${SVG}}svg`, {width: String(canvas), height: String(canvas), viewBox: `0 0 ${canvas} ${canvas}`,
      fill: rootEl.attrib.fill ?? 'none', stroke: rootEl.attrib.stroke ?? 'currentColor', 'stroke-width': String(STROKE),
      'stroke-linecap': rootEl.attrib['stroke-linecap'] ?? 'round', 'stroke-linejoin': rootEl.attrib['stroke-linejoin'] ?? 'round'});
    const placed = new Map();
    for (const group of layout) {
      const [x0, y0, x1, y1] = union(group.paths.map(i => source[i]));
      const scales = [[x1 - x0, group.w], [y1 - y0, group.h]].map(([extent, target]) => {
        if (extent <= 1e-9) { if (target !== 0) fail('A flat element keeps zero size along its flat axis.'); return 1.0; }
        if (target < 1) fail('An element must stay at least one unit on each axis.');
        return target / extent;
      });
      let [sx, sy] = scales;
      if (x1 - x0 <= 1e-9 && y1 - y0 > 1e-9) sx = sy;
      if (y1 - y0 <= 1e-9 && x1 - x0 > 1e-9) sy = sx;
      for (const i of group.paths) placed.set(i, [sx, sy, group.x - x0 * sx, group.y - y0 * sy]);
    }
    const boxes = [];
    found.forEach(([el, own], i) => {
      if (!placed.has(i)) return;
      const [sx, sy, dx, dy] = placed.get(i);
      const copy = deepcopy(el);
      copy.tail = null;
      for (const [k, v] of Object.entries(own)) copy.attrib[k] = v;
      if (copy.attrib['stroke-width'] != null) copy.attrib['stroke-width'] = fmt(parseFloat(copy.attrib['stroke-width']) / base * STROKE);
      delete copy.attrib.id;
      transformElement(copy, sx, sy, dx, dy);
      out.children.push(copy);
      boxes.push(bbox(segmentsOf(copy, {'stroke-width': String(STROKE)})));
    });
    return {document: tostring(out), bounds: union(boxes)};
  }

  // ======== the clearance area (GEOS buffers and a convex hull) ========

  // Robust orientation of q relative to p1 → p2 (GEOS CGAlgorithmsDD::orientationIndex), exact on doubt.
  function orientation(p1x, p1y, p2x, p2y, qx, qy) {
    const detleft = (p1x - qx) * (p2y - qy), detright = (p1y - qy) * (p2x - qx), det = detleft - detright;
    let detsum;
    if (detleft > 0.0) { if (detright <= 0.0) return Math.sign(det); detsum = detleft + detright; }
    else if (detleft < 0.0) { if (detright >= 0.0) return Math.sign(det); detsum = -detleft - detright; }
    else return Math.sign(det);
    if (det >= 1e-15 * detsum || -det >= 1e-15 * detsum) return Math.sign(det);
    return exactOrientation(p1x, p1y, p2x, p2y, qx, qy);
  }
  function exactOrientation(p1x, p1y, p2x, p2y, qx, qy) {
    const big = v => { // exact value of a double as a BigInt over 2^1100
      if (v === 0) return 0n;
      const buf = new DataView(new ArrayBuffer(8)); buf.setFloat64(0, v);
      const hi = buf.getUint32(0), lo = buf.getUint32(4);
      const sign = hi >>> 31 ? -1n : 1n, exp = (hi >>> 20) & 0x7ff;
      let mant = (BigInt(hi & 0xfffff) << 32n) | BigInt(lo);
      let e = exp - 1075;
      if (exp === 0) e = -1074; else mant |= 1n << 52n;
      return sign * (mant << BigInt(e + 1100));
    };
    const [ax, ay, bx, by, cx, cy] = [p1x, p1y, p2x, p2y, qx, qy].map(big);
    const d = (bx - ax) * (cy - by) - (by - ay) * (cx - bx);
    return d > 0n ? 1 : d < 0n ? -1 : 0;
  }

  // One segment buffered by `r` with round caps, vertex for vertex as GEOS builds it (OffsetCurveBuilder,
  // quadrant segments 16): the ring of a capsule, or a circle for a zero-length segment.
  function capsule(p0, p1, r) {
    const ring = [], min = r * 1e-6, quantum = Math.PI / 2 / QUADRANT_SEGMENTS;
    const add = pt => {
      if (ring.length) { const q = ring[ring.length - 1]; if (Math.hypot(pt[0] - q[0], pt[1] - q[1]) < min) return; }
      ring.push(pt);
    };
    const fillet = (p, start, end, direction) => {
      const total = Math.abs(start - end), count = Math.trunc(total / quantum + 0.5);
      if (count < 1) return;
      const inc = total / count;
      for (let i = 0; i < count; i++) {
        // Angle::sinCosSnap (GEOS 3.13): values within 5e-16 of zero are zero.
        const angle = start + direction * i * inc;
        let sin = Math.sin(angle), cos = Math.cos(angle);
        if (Math.abs(sin) < 5e-16) sin = 0.0;
        if (Math.abs(cos) < 5e-16) cos = 0.0;
        add([p[0] + r * cos, p[1] + r * sin]);
      }
    };
    if (p0[0] === p1[0] && p0[1] === p1[1]) {
      add([p0[0] + r, p0[1]]);
      fillet(p0, 0.0, 2.0 * Math.PI, -1);
    } else {
      const offset = (a, b, side) => {
        const dx = b[0] - a[0], dy = b[1] - a[1], len = Math.sqrt(dx * dx + dy * dy);
        const ux = side * r * dx / len, uy = side * r * dy / len;
        return [[a[0] - uy, a[1] + ux], [b[0] - uy, b[1] + ux]];
      };
      const cap = (a, b) => {
        const left = offset(a, b, 1), right = offset(a, b, -1), angle = Math.atan2(b[1] - a[1], b[0] - a[0]);
        add(left[1]);
        fillet(b, angle + Math.PI / 2, angle - Math.PI / 2, -1);
        add(right[1]);
      };
      add(offset(p0, p1, 1)[1]);      // left side, then the cap round p1
      cap(p0, p1);
      add(offset(p1, p0, 1)[1]);      // right side, then the cap round p0
      cap(p1, p0);
    }
    if (ring.length && (ring[0][0] !== ring[ring.length - 1][0] || ring[0][1] !== ring[ring.length - 1][1])) ring.push(ring[0]);
    return ring;
  }

  // scipy ConvexHull of the points (collinear or fewer than three: no hull).
  function hull(points) {
    if (points.length < 3) return null;
    const pts = [...new Map(points.map(p => [p[0] + ',' + p[1], p])).values()].sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    if (pts.length < 3) return null;
    const turn = (o, a, b) => orientation(o[0], o[1], a[0], a[1], b[0], b[1]);
    const lower = [], upper = [];
    for (const p of pts) { while (lower.length >= 2 && turn(lower[lower.length - 2], lower[lower.length - 1], p) <= 0) lower.pop(); lower.push(p); }
    for (let i = pts.length - 1; i >= 0; i--) { const p = pts[i]; while (upper.length >= 2 && turn(upper[upper.length - 2], upper[upper.length - 1], p) <= 0) upper.pop(); upper.push(p); }
    const ring = lower.slice(0, -1).concat(upper.slice(0, -1));
    if (ring.length < 3) return null;
    ring.push(ring[0]);
    return ring;
  }

  function boundsOf(ring) {
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    for (const [x, y] of ring) { if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y; }
    return [x0, y0, x1, y1];
  }

  // Where a point is in a convex ring: 1 inside, 0 on the boundary, -1 outside.
  function locate(ring, sign, p) {
    let onEdge = false;
    for (let i = 0; i + 1 < ring.length; i++) {
      const o = orientation(ring[i][0], ring[i][1], ring[i + 1][0], ring[i + 1][1], p[0], p[1]);
      if (o === -sign) return -1;
      if (o === 0) {
        const [a, b] = [ring[i], ring[i + 1]];
        if (p[0] >= Math.min(a[0], b[0]) && p[0] <= Math.max(a[0], b[0]) && p[1] >= Math.min(a[1], b[1]) && p[1] <= Math.max(a[1], b[1])) onEdge = true;
        else return -1;
      }
    }
    return onEdge ? 0 : 1;
  }

  // Whether p is inside a convex ring by more than `eps` from every edge. Rings that share a cap (two sub
  // strokes meeting at one point) have the same edges up to rounding; GEOS merges those when it unions them.
  function deepInside(ring, sign, p, eps) {
    for (let i = 0; i + 1 < ring.length; i++) {
      const [a, b] = [ring[i], ring[i + 1]];
      const dx = b[0] - a[0], dy = b[1] - a[1], len = Math.hypot(dx, dy);
      if (!len) continue;
      if (sign * (dx * (p[1] - a[1]) - dy * (p[0] - a[0])) / len <= eps) return false;
    }
    return true;
  }

  function ringSign(ring) {  // +1 counter-clockwise (y up), -1 clockwise
    let area = 0;
    for (let i = 0; i + 1 < ring.length; i++) area += ring[i][0] * ring[i + 1][1] - ring[i + 1][0] * ring[i][1];
    return area > 0 ? 1 : -1;
  }

  // GEOS LineIntersector: the intersection point of p1p2 and q1q2 (null if none), exact endpoints when they touch.
  function intersect(p1, p2, q1, q2) {
    if (Math.max(q1[0], q2[0]) < Math.min(p1[0], p2[0]) || Math.min(q1[0], q2[0]) > Math.max(p1[0], p2[0])
        || Math.max(q1[1], q2[1]) < Math.min(p1[1], p2[1]) || Math.min(q1[1], q2[1]) > Math.max(p1[1], p2[1])) return [];
    const Pq1 = orientation(p1[0], p1[1], p2[0], p2[1], q1[0], q1[1]), Pq2 = orientation(p1[0], p1[1], p2[0], p2[1], q2[0], q2[1]);
    if ((Pq1 > 0 && Pq2 > 0) || (Pq1 < 0 && Pq2 < 0)) return [];
    const Qp1 = orientation(q1[0], q1[1], q2[0], q2[1], p1[0], p1[1]), Qp2 = orientation(q1[0], q1[1], q2[0], q2[1], p2[0], p2[1]);
    if ((Qp1 > 0 && Qp2 > 0) || (Qp1 < 0 && Qp2 < 0)) return [];
    if (Pq1 === 0 && Pq2 === 0 && Qp1 === 0 && Qp2 === 0) {  // collinear: the overlap's ends
      const on = (p, a, b) => p[0] >= Math.min(a[0], b[0]) && p[0] <= Math.max(a[0], b[0]) && p[1] >= Math.min(a[1], b[1]) && p[1] <= Math.max(a[1], b[1]);
      const pts = [];
      for (const p of [q1, q2]) if (on(p, p1, p2)) pts.push(p);
      for (const p of [p1, p2]) if (on(p, q1, q2)) pts.push(p);
      return pts;
    }
    const same = (a, b) => a[0] === b[0] && a[1] === b[1];
    if (Pq1 === 0 || Pq2 === 0 || Qp1 === 0 || Qp2 === 0) {
      if (same(p1, q1) || same(p1, q2)) return [p1];
      if (same(p2, q1) || same(p2, q2)) return [p2];
      if (Pq1 === 0) return [q1];
      if (Pq2 === 0) return [q2];
      if (Qp1 === 0) return [p1];
      return [p2];
    }
    // Intersection::intersection, conditioned on the middle of the envelopes' overlap.
    const minX = Math.max(Math.min(p1[0], p2[0]), Math.min(q1[0], q2[0])), maxX = Math.min(Math.max(p1[0], p2[0]), Math.max(q1[0], q2[0]));
    const minY = Math.max(Math.min(p1[1], p2[1]), Math.min(q1[1], q2[1])), maxY = Math.min(Math.max(p1[1], p2[1]), Math.max(q1[1], q2[1]));
    const mx = (minX + maxX) / 2.0, my = (minY + maxY) / 2.0;
    const p1x = p1[0] - mx, p1y = p1[1] - my, p2x = p2[0] - mx, p2y = p2[1] - my;
    const q1x = q1[0] - mx, q1y = q1[1] - my, q2x = q2[0] - mx, q2y = q2[1] - my;
    const px = p1y - p2y, py = p2x - p1x, pw = p1x * p2y - p2x * p1y;
    const qx = q1y - q2y, qy = q2x - q1x, qw = q1x * q2y - q2x * q1y;
    const x = py * qw - qy * pw, y = qx * pw - px * qw, w = px * qy - qx * py;
    let pt = [x / w + mx, y / w + my];
    if (!Number.isFinite(pt[0]) || !Number.isFinite(pt[1]) || !inEnvelopes(pt, p1, p2, q1, q2)) pt = nearestEndpoint(p1, p2, q1, q2);
    return [pt];
  }
  function inEnvelopes(pt, p1, p2, q1, q2) {
    const inside = (a, b) => pt[0] >= Math.min(a[0], b[0]) && pt[0] <= Math.max(a[0], b[0]) && pt[1] >= Math.min(a[1], b[1]) && pt[1] <= Math.max(a[1], b[1]);
    return inside(p1, p2) && inside(q1, q2);
  }
  function nearestEndpoint(p1, p2, q1, q2) {
    const dist = (p, a, b) => {  // Distance::pointToSegment
      const dx = b[0] - a[0], dy = b[1] - a[1], len2 = dx * dx + dy * dy;
      if (len2 === 0) return Math.hypot(p[0] - a[0], p[1] - a[1]);
      const r = ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / len2;
      if (r <= 0) return Math.hypot(p[0] - a[0], p[1] - a[1]);
      if (r >= 1) return Math.hypot(p[0] - b[0], p[1] - b[1]);
      return Math.abs(((a[1] - p[1]) * dx - (a[0] - p[0]) * dy) / len2) * Math.sqrt(len2);
    };
    let best = p1, min = dist(p1, q1, q2);
    for (const [p, a, b] of [[p2, q1, q2], [q1, p1, p2], [q2, p1, p2]]) { const d = dist(p, a, b); if (d < min) { min = d; best = p; } }
    return best;
  }

  class Area {
    // The union of the rings (buffered sub segments and the sub's hull): where the main is erased.
    constructor(rings) {
      this.rings = rings.map(ring => ({ring, sign: ringSign(ring), box: boundsOf(ring)}));
      this.box = this.rings.length ? union(this.rings.map(r => r.box)) : null;
    }
    get empty() { return !this.rings.length; }
    // 1 inside, 0 on the boundary, -1 outside the union.
    locate(p) {
      let best = -1;
      for (const r of this.rings) {
        if (p[0] < r.box[0] || p[0] > r.box[2] || p[1] < r.box[1] || p[1] > r.box[3]) continue;
        const l = locate(r.ring, r.sign, p);
        if (l === 1) return 1;
        if (l === 0) best = 0;
      }
      return best;
    }
    // Whether a ring other than `own` holds p strictly inside (then p is inside the union, not on its boundary).
    within(p, own) {
      for (const r of this.rings) {
        if (r === own || p[0] < r.box[0] || p[0] > r.box[2] || p[1] < r.box[1] || p[1] > r.box[3]) continue;
        if (deepInside(r.ring, r.sign, p, 1e-9)) return true;
      }
      return false;
    }
    // The points where segment a → b meets the union's boundary, in order along it.
    nodes(a, b) {
      const box = [Math.min(a[0], b[0]), Math.min(a[1], b[1]), Math.max(a[0], b[0]), Math.max(a[1], b[1])];
      const found = [];
      for (const r of this.rings) {
        if (r.box[0] > box[2] || r.box[2] < box[0] || r.box[1] > box[3] || r.box[3] < box[1]) continue;
        for (let i = 0; i + 1 < r.ring.length; i++) {
          for (const pt of intersect(a, b, r.ring[i], r.ring[i + 1])) if (!this.within(pt, r)) found.push(pt);
        }
      }
      const dx = b[0] - a[0], dy = b[1] - a[1];
      const t = p => Math.abs(dx) >= Math.abs(dy) ? (p[0] - a[0]) / dx : (p[1] - a[1]) / dy;
      found.sort((p, q) => t(p) - t(q));
      return found.filter((p, i) => i === 0 || Math.abs(p[0] - found[i - 1][0]) > 1e-9 || Math.abs(p[1] - found[i - 1][1]) > 1e-9);
    }
  }

  // icon_combination.utils.clip_segments_outside_state_area_enhanced: the main segments outside the area,
  // and how many pieces each input segment left (for the bottom layer's count).
  function clip(segments, area, minLength) {
    if (area.empty) return {kept: segments, pieces: segments.map(() => 1)};
    const kept = [], pieces = [];
    const inside = p => area.locate(p) >= 0;
    for (const segment of segments) {
      const [s, e] = segment;
      if (s[0] === e[0] && s[1] === e[1]) {
        if (inside(s)) pieces.push(0); else { kept.push(segment); pieces.push(1); }
        continue;
      }
      const length = Math.sqrt(square(e[0] - s[0]) + square(e[1] - s[1]));
      if (length < minLength) {
        if (inside([(s[0] + e[0]) / 2, (s[1] + e[1]) / 2])) pieces.push(0); else { kept.push(segment); pieces.push(1); }
        continue;
      }
      const nodes = area.nodes(s, e);
      const stops = [s, ...nodes.filter(p => !(p[0] === s[0] && p[1] === s[1]) && !(p[0] === e[0] && p[1] === e[1])), e];
      const outside = [];
      for (let i = 0; i + 1 < stops.length; i++) {
        const a = stops[i], b = stops[i + 1];
        if (area.locate([(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]) < 0) outside.push([a, b]);
      }
      const startIn = inside(s), endIn = inside(e);
      if (!outside.length || (startIn && endIn)) { pieces.push(0); continue; }        // contained, or both ends in
      if (!nodes.length && !startIn && !endIn) { kept.push(segment); pieces.push(1); continue; }  // never meets it
      const made = [];
      for (const [a, b] of outside) {
        if (Math.sqrt(square(b[0] - a[0]) + square(b[1] - a[1])) >= minLength) made.push([[a[0], a[1]], [b[0], b[1]]]);
      }
      kept.push(...made);
      pieces.push(made.length);
    }
    return {kept, pieces};
  }

  // ======== the fold (box_combine.fold with manual, geometry-preserving boxes) ========

  // How a drawing's segments are fitted into a box: scale s, then move by (dx, dy).
  function fitTransform(segments, box) {
    const b = bbox(segments);
    if (!b) fail('combine failed: cannot place an empty symbol');
    const [x0, y0, x1, y1] = b, w = x1 - x0, h = y1 - y0, [bx, by, bw, bh] = box;
    const votes = [[w, bw], [h, bh]].filter(([s, d]) => s > 1e-9 && d > 1e-9).map(([s, d]) => d / s);
    const s = votes.length ? Math.min(...votes) : 1.0;
    return {s, dx: bx + (bw - w * s) / 2 - x0 * s, dy: by + (bh - h * s) / 2 - y0 * s};
  }
  function fitInto(segments, box) {
    const {s, dx, dy} = fitTransform(segments, box);
    return segments.map(seg => seg.map(p => [p[0] * s + dx, p[1] * s + dy]));
  }

  // The filled dots of a drawing (circles painted with no stroke: eyes, bullets), which the engine's stroke reading
  // leaves out: [{cx, cy, r}].
  function filledDots(svgText) {
    const rootEl = parseXml(svgText);
    removeClipPathElements(rootEl);
    const dots = [];
    const walk = (el, fill, stroke) => {
      const f = 'fill' in el.attrib ? el.attrib.fill : fill, k = 'stroke' in el.attrib ? el.attrib.stroke : stroke;
      const none = v => (v ?? 'none').trim().toLowerCase() === 'none';
      if (local(el.tag) === 'circle' && none(k) && !none(f ?? 'black')) {
        const r = pyFloat(el.attrib.r ?? '0');
        if (r > 0) dots.push({cx: pyFloat(el.attrib.cx ?? '0'), cy: pyFloat(el.attrib.cy ?? '0'), r});
      }
      for (const child of el.children) walk(child, f, k);
    };
    walk(rootEl, undefined, undefined);
    return dots;
  }
  const boxToCanvas = (box, canvas) => { const k = canvas / GRID; return [box.x * k, box.y * k, box.w * k, box.h * k]; };

  function fold(mainSvg, mainBox, subSvg, subBox, margin, canvas, keepDots = false) {
    const minLength = canvas * (1.0 / 1024);
    const mainSegments = engineSegments(mainSvg), fit = fitTransform(mainSegments, boxToCanvas(mainBox, canvas));
    const main = fitInto(mainSegments, boxToCanvas(mainBox, canvas));
    const placed = fitInto(engineSegments(subSvg), boxToCanvas(subBox, canvas));
    const rings = [];
    const seen = new Set();
    for (const [a, b] of placed) {
      const key = a.join(',') + ';' + b.join(',');
      if (!seen.has(key)) { seen.add(key); rings.push(capsule(a, b, margin)); }
    }
    const shell = hull(placed.flat());
    if (shell) rings.push(shell);
    const area = new Area(rings);
    const {kept} = clip(main, area, minLength);
    const state = placed.map(seg => seg.map(p => [p[0] + 0.0, p[1] + 0.0]));
    // At 72 the main's filled dots move with its strokes (their own size, as strokes keep their width); one whose
    // centre is in the erased area goes, like a stroke under the sub.
    const dots = !keepDots ? [] : filledDots(mainSvg).map(d => ({cx: d.cx * fit.s + fit.dx, cy: d.cy * fit.s + fit.dy, r: d.r}))
      .filter(d => area.locate([d.cx, d.cy]) === -1);
    return {main: kept, state, dots};
  }

  // save_clipped_result_to_svg, read back by ElementTree the way restore_original_sub reads it.
  function engineDocument(main, state, canvas, dots = []) {
    const d = segs => segs.map(([a, b]) => `M${pyFixed2(a[0])},${pyFixed2(a[1])}L${pyFixed2(b[0])},${pyFixed2(b[1])}`).join(' ');
    const group = (id, segs) => {
      const g = element(`{${SVG}}g`, {id, stroke: '#000000', 'stroke-width': String(STROKE), fill: 'none', 'stroke-linecap': 'round', 'stroke-linejoin': 'round'});
      if (segs.length) {
        g.text = '\n    ';
        const path = element(`{${SVG}}path`, {d: d(segs)});
        path.tail = '\n  ';
        g.children.push(path);
      } else {
        g.text = '\n  ';
      }
      return g;
    };
    const withDots = g => {
      if (!dots.length) return g;
      const last = g.children[g.children.length - 1];
      if (last) last.tail = '\n    '; else g.text = '\n    ';
      dots.forEach((d, i) => {
        const c = element(`{${SVG}}circle`, {cx: pyFixed2(d.cx), cy: pyFixed2(d.cy), r: pyG12(d.r), fill: '#000000', stroke: 'none'});
        c.tail = i === dots.length - 1 ? '\n  ' : '\n    ';
        g.children.push(c);
      });
      return g;
    };
    const rootEl = element(`{${SVG}}svg`, {width: String(canvas), height: String(canvas), viewBox: `0 0 ${canvas} ${canvas}`});
    rootEl.text = '\n  \n  \n  ';
    const mainGroup = withDots(group('main-icon-clipped', main)), stateGroup = group('state-icon', state);
    mainGroup.tail = '\n  \n  \n  ';
    stateGroup.tail = '\n';
    rootEl.children.push(mainGroup, stateGroup);
    return rootEl;
  }

  // combination_experiment.restore_original_sub: the clipped main, with the sub's own curves put back.
  function restoreOriginalSub(target, item, placed) {
    const index = target.children.findIndex(e => e.attrib.id === 'state-icon');
    target.children.splice(index, 1);
    const source = parseXml(item.document);
    const [x0, y0, x1, y1] = item.bounds, box = placed.painted_box;
    const scale = x1 !== x0 ? (box.w - 4) / (x1 - x0) : (box.h - 4) / (y1 - y0);
    const tx = box.x + 2 - x0 * scale, ty = box.y + 2 - y0 * scale;
    const attrs = {};
    for (const [k, v] of Object.entries(source.attrib)) if (!['width', 'height', 'viewBox', 'id', 'transform'].includes(k)) attrs[k] = v;
    if (!('stroke-width' in attrs)) attrs['stroke-width'] = '4';
    delete attrs.id; attrs.id = 'state-icon';
    delete attrs.transform; attrs.transform = `translate(${pyG12(tx)} ${pyG12(ty)}) scale(${pyG12(scale)})`;
    const group = element(`{${SVG}}g`, attrs);
    let content = group;
    if (source.attrib.transform) { content = element(`{${SVG}}g`, {transform: source.attrib.transform}); group.children.push(content); }
    for (const child of source.children) if (!['title', 'desc'].includes(local(child.tag))) content.children.push(deepcopy(child));
    const ids = new Map();
    for (const el of iter(group)) if (el !== group && el.attrib.id) ids.set(el.attrib.id, 'sub-source-' + el.attrib.id);
    for (const el of iter(group)) {
      for (const [key, value0] of Object.entries(el.attrib)) {
        if (key === 'id' && ids.has(value0)) { el.attrib[key] = ids.get(value0); continue; }
        let value = value0;
        for (const [oldId, newId] of ids) {
          value = value.split(`url(#${oldId})`).join(`url(#${newId})`);
          if (value === '#' + oldId) value = '#' + newId;
        }
        el.attrib[key] = value;
      }
      delete el.attrib['vector-effect'];
      if ('stroke-width' in el.attrib) el.attrib['stroke-width'] = pyStr(parseFloat(el.attrib['stroke-width']) / scale);
    }
    target.children.splice(index, 0, group);
    return tostring(target);
  }

  // ======== a changed drawing, measured the way the side pages measure it (side_recombine.py) ========

  // SHA-256 of a string's UTF-8 bytes, hex (synchronous, so a whole page of pairs builds in one pass).
  function sha256(text) {
    const bytes = new TextEncoder().encode(text);
    const K = new Uint32Array([0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
      0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786,
      0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
      0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb,
      0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
      0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3, 0x748f82ee, 0x78a5636f,
      0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]);
    const H = new Uint32Array([0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]);
    const length = bytes.length, padded = new Uint8Array(((length + 9 + 63) >> 6) << 6);
    padded.set(bytes); padded[length] = 0x80;
    const view = new DataView(padded.buffer);
    view.setUint32(padded.length - 4, length * 8 >>> 0); view.setUint32(padded.length - 8, Math.floor(length / 0x20000000));
    const W = new Uint32Array(64), rot = (x, n) => (x >>> n) | (x << (32 - n));
    for (let off = 0; off < padded.length; off += 64) {
      for (let i = 0; i < 16; i++) W[i] = view.getUint32(off + i * 4);
      for (let i = 16; i < 64; i++) {
        const s0 = rot(W[i - 15], 7) ^ rot(W[i - 15], 18) ^ (W[i - 15] >>> 3), s1 = rot(W[i - 2], 17) ^ rot(W[i - 2], 19) ^ (W[i - 2] >>> 10);
        W[i] = (W[i - 16] + s0 + W[i - 7] + s1) >>> 0;
      }
      let [a, b, c, d, e, f, g, h] = H;
      for (let i = 0; i < 64; i++) {
        const t1 = (h + (rot(e, 6) ^ rot(e, 11) ^ rot(e, 25)) + ((e & f) ^ (~e & g)) + K[i] + W[i]) >>> 0;
        const t2 = ((rot(a, 2) ^ rot(a, 13) ^ rot(a, 22)) + ((a & b) ^ (a & c) ^ (b & c))) >>> 0;
        h = g; g = f; f = e; e = (d + t1) >>> 0; d = c; c = b; b = a; a = (t1 + t2) >>> 0;
      }
      H[0] += a; H[1] += b; H[2] += c; H[3] += d; H[4] += e; H[5] += f; H[6] += g; H[7] += h;
    }
    return [...H].map(v => v.toString(16).padStart(8, '0')).join('');
  }

  // build_combination_previews._inline_class_styles: simple `.class {…}` rules become attributes.
  function inlineClassStyles(document) {
    const rootEl = parseXml(document);
    const styles = {};
    for (const parent of iter(rootEl)) {
      for (const child of [...parent.children]) {
        if (local(child.tag) !== 'style') continue;
        const css = child.text || '';
        const rules = [...css.matchAll(/([^{}]+)\{([^{}]*)\}/g)];
        if (css.replace(/[^{}]+\{[^{}]*\}/g, '').trim()) return document;
        for (const [, selectors, declarations] of rules) {
          const attrs = {};
          for (const declaration of declarations.split(';')) {
            if (!declaration.trim()) continue;
            if (!declaration.includes(':')) return document;
            const i = declaration.indexOf(':');
            attrs[declaration.slice(0, i).trim()] = declaration.slice(i + 1).trim();
          }
          for (let selector of selectors.split(',')) {
            selector = selector.trim();
            if (!/^\.[a-zA-Z_][\w-]*$/.test(selector)) return document;
            styles[selector.slice(1)] = Object.assign(styles[selector.slice(1)] || {}, attrs);
          }
        }
        removeChild(parent, child);
      }
    }
    if (!Object.keys(styles).length) return document;
    for (const el of iter(rootEl)) {
      const names = (el.attrib.class ?? '').split(/\s+/).filter(Boolean);
      delete el.attrib.class;
      for (const name of names) for (const [k, v] of Object.entries(styles[name] || {})) el.attrib[k] = v;
    }
    return tostring(rootEl);
  }

  // icon_artwork.safe_svg (profile canvas): the allowed tags and attributes, re-serialized. Its last check —
  // that cairosvg renders visible ink — is left to the build (the combined icon is reviewed as drawn).
  function safeSvg(text, canvas) {
    if (typeof text !== 'string' || !text.trim() || new TextEncoder().encode(text).length > 1024 * 1024) fail('Choose an SVG file up to 1 MB.');
    if (/<!(DOCTYPE|ENTITY)/i.test(text)) fail('Export SVG without a DOCTYPE or entity declarations.');
    let rootEl;
    try { rootEl = parseXml(text); } catch { fail('This file is not valid SVG.'); }
    if (rootEl.tag !== 'svg' && rootEl.tag !== `{${SVG}}svg`) fail('Choose an SVG file.');
    const view = (rootEl.attrib.viewBox ?? '').trim().split(/[\s,]+/).map(v => v === '' ? NaN : Number(v));
    if (view.length !== 4 || view.some(Number.isNaN) || view[0] !== 0 || view[1] !== 0 || view[2] !== canvas || view[3] !== canvas) {
      fail(`Export with a 0 0 ${pyNumber(canvas)} ${pyNumber(canvas)} viewBox to keep the icon on its profile canvas.`);
    }
    const tags = ['svg', 'g', 'path', 'rect', 'circle', 'ellipse', 'line', 'polyline', 'polygon', 'defs', 'clipPath', 'mask',
                  'linearGradient', 'radialGradient', 'stop', 'use', 'title', 'desc', 'style'];
    const paint = ['fill', 'fill-rule', 'fill-opacity', 'stroke', 'stroke-width', 'stroke-linecap', 'stroke-linejoin', 'stroke-miterlimit',
                   'stroke-dasharray', 'stroke-dashoffset', 'stroke-opacity', 'opacity', 'clip-path', 'clip-rule', 'mask', 'color',
                   'stop-color', 'stop-opacity', 'display', 'visibility'];
    const attrs = new Set([...paint, 'id', 'class', 'd', 'points', 'transform', 'viewBox', 'width', 'height', 'x', 'y', 'x1', 'x2', 'y1', 'y2',
      'cx', 'cy', 'r', 'rx', 'ry', 'fx', 'fy', 'offset', 'gradientUnits', 'gradientTransform', 'spreadMethod', 'clipPathUnits',
      'maskUnits', 'maskContentUnits', 'preserveAspectRatio', 'version', 'vector-effect']);
    const valueOk = value => {
      if (/[\\<>]|\/\*|@/.test(value)) return false;
      const clean = value.replace(/url\(\s*['"]?#[a-zA-Z_][\w:.-]*['"]?\s*\)/gi, '');
      return !/url\s*\(|expression\s*\(|javascript:|data:|https?:|file:/i.test(clean);
    };
    const declarations = css => {
      const pairs = [];
      for (const declaration of css.split(';')) {
        if (!declaration.trim()) continue;
        if (!declaration.includes(':')) fail('Unsupported SVG styling. Export with inline presentation attributes.');
        const i = declaration.indexOf(':'), key = declaration.slice(0, i).trim(), value = declaration.slice(i + 1).trim();
        if (!paint.includes(key) || !valueOk(value)) fail('Unsupported SVG styling. Export vector paths with fill and stroke styles.');
        pairs.push(`${key}:${value}`);
      }
      return pairs.join(';');
    };
    let count = 0;
    for (const node of iter(rootEl)) {
      if (++count > 10000) fail('SVG is too complex; simplify it before uploading.');
      const tag = local(node.tag);
      if (!tags.includes(tag) || (node.tag.startsWith('{') && !node.tag.startsWith(`{${SVG}}`))) {
        fail(`Unsupported SVG element: ${tag}. Export text as outlines and use vector shapes.`);
      }
      if (tag === 'style') {
        const css = (node.text || '').replace(/\/\*[\s\S]*?\*\//g, '');
        const blocks = [...css.matchAll(/([^{}]+)\{([^{}]*)\}/g)];
        if (css.replace(/[^{}]+\{[^{}]*\}/g, '').trim()) fail('Unsupported SVG stylesheet. Export with inline styles.');
        const output = [];
        for (const [, selector, body] of blocks) {
          if (!/^[\w.#,\s>+-]+$/.test(selector)) fail('Unsupported SVG selector. Export with inline styles.');
          output.push(selector + '{' + declarations(body) + '}');
        }
        node.text = output.join('\n');
      }
      for (const [key, value] of Object.entries(node.attrib)) {
        if (key === 'style') node.attrib[key] = declarations(value);
        else if (key === 'href' || key === '{http://www.w3.org/1999/xlink}href') {
          if (!/^#[a-zA-Z_][\w:.-]*$/.test(value)) fail('SVG references must stay inside this file.');
        } else if (key.startsWith('{') || key.startsWith('data-') || key.startsWith('aria-')) delete node.attrib[key];
        else if (!attrs.has(key) || !valueOk(value)) fail(`Unsupported SVG attribute: ${key}. Export a static vector SVG.`);
      }
    }
    rootEl.attrib.width = pyNumber(canvas); rootEl.attrib.height = pyNumber(canvas);
    if (rootEl.tag === 'svg') rootEl.attrib.xmlns = SVG;
    return tostring(rootEl) + '\n';
  }
  const pyNumber = v => pyStr(v);  // the canvas is a float here (a viewBox size): str(48.0) is '48.0'

  // combination_experiment.custom_item: a drawing measured for combining (its bounds and canvas).
  function customItem(text, role, pairSize = 64) {
    if (new TextEncoder().encode(text).length > 1024 * 1024 || /<!(DOCTYPE|ENTITY)/i.test(text)) fail('Upload a plain SVG up to 1 MB without entity declarations.');
    let view;
    try {
      view = (parseXml(text).attrib.viewBox ?? '').trim().split(/[\s,]+/).map(v => { const n = v === '' ? NaN : Number(v); if (Number.isNaN(n)) throw Error(); return n; });
    } catch { fail('Upload an SVG with a square viewBox starting at 0,0.'); }
    if (view.length !== 4 || view[0] !== 0 || view[1] !== 0 || view[2] !== view[3] || !(0 < view[2] && view[2] <= 4096)) {
      fail('Upload an SVG with a square viewBox starting at 0,0 (up to 4096 units).');
    }
    const safe = safeSvg(text, view[2]);
    let bounds;
    try { bounds = bbox(engineSegments(safe)); } catch { fail('No supported stroke geometry. Upload an SVG with stroked paths or shapes.'); }
    const sizes = sizeOf(pairSize), size = sizes[role === 'main' ? 'main' : 'sub'], extent = Math.max(bounds[2] - bounds[0], bounds[3] - bounds[1]);
    // A 72 pair's sub is placed as drawn: its canvas is its own grid.
    if (role !== 'main' && sizes.canvas !== 64) return {icon: 'custom-' + role, document: safe, canvas: view[2], bounds};
    return {icon: 'custom-' + role, document: safe, canvas: Math.max(view[2], extent * size / (size - 4)), bounds};
  }

  // side_recombine.pair_with_documents: the pair with its main and sub measured from their current drawings.
  // `documents` maps 'main' / 'sub' to the current SVG; one the item was made from combines as published.
  function withDocuments(row, main, sub, documents = {}, size = 64) {
    const current = JSON.parse(JSON.stringify(row)), chosen = {};
    for (const [role, group, wanted] of [['main', 'mains', main], ['sub', 'subs', sub]]) {
      const name = wanted || current[group][0].icon;
      const item = current[group].find(i => i.icon === name);
      if (!item) fail('The ' + role + ' does not belong to this pair.');
      const svg = documents[role];
      const published = new Set([item.sha256, item.source_sha256].filter(Boolean));
      if (svg && svg !== item.document && !published.has(sha256(svg)) && !item.native_text) {
        if (role === 'sub' && item.ink32 && item.family !== 'text' && size === 64) {
          normalizedSub(item, inlineClassStyles(svg));
        } else {
          const measured = customItem(inlineClassStyles(svg), role, size);
          for (const field of ['engine_document', 'ink32', 'sizing_kind', 'sub32_status']) delete item[field];
          Object.assign(item, measured, {icon: name});
        }
      }
      chosen[role] = name;
    }
    return {row: current, main: chosen.main, sub: chosen.sub};
  }

  // Sizing modes that place a sub 1:1 at its authored canvas_width × canvas_height (placement).
  const EXCEPTION_SIZES = ['side-source-fit', 'side-32x48', 'side-one-axis32'];
  function normalizedSub(item, svg) {
    if (typeof NormalizeInk32 === 'undefined' && typeof require !== 'function') fail('The SUB32 normalizer is not loaded.');
    const normalize = (typeof NormalizeInk32 !== 'undefined' ? NormalizeInk32 : require('./normalize-ink32.js')).normalize;
    const [document, ink] = normalize(svg, {text: item.sizing_kind === 'text'});
    const bounds = ink.bounds, extent = Math.max(bounds[2] - bounds[0], bounds[3] - bounds[1]);
    delete item.engine_document;
    // A redrawn sub is a plain SUB32 now: the old drawing's 1:1 exception size no longer applies.
    if (EXCEPTION_SIZES.includes(item.sizing_mode)) { delete item.sizing_mode; delete item.canvas_width; delete item.canvas_height; }
    Object.assign(item, {document, bounds, ink32: ink, canvas: Math.max(32, extent * 32 / 28), sha256: sha256(document), source_sha256: sha256(svg)});
  }

  // ======== render (combination_experiment.render) ========

  function pairCanvas(row, sub, padding = 2) {
    const wanted = sub || (row.subs[0] && row.subs[0].icon);
    const native = row.subs.find(s => s.icon === wanted);
    if (native && native.sizing_mode === 'typeface-native') {
      return Math.max(64, Math.ceil(Math.max(native.canvas_width, native.canvas_height) + 2 * padding - 1e-8));
    }
    return 64;
  }

  function render(row, data = {}) {
    const position = data.position || row.position;
    if (!(position in POSITIONS)) fail('Choose one of the eight positions.');
    const [ax, ay] = POSITIONS[position];
    const margin = number(data.margin, 8), padding = number(data.padding, 2);
    if (!(0 <= padding && padding <= 8)) fail('Canvas padding must be between 0 and 8.');
    if (margin < 0) fail('Erasure margin must be between 0 and 64.');
    const sizes = sizeOf(data.size), large = sizes.canvas !== 64;
    const canvas = large ? sizes.canvas : pairCanvas(row, data.sub, padding);
    const layout = checkLayout(data.layout);
    const chosen = [];
    for (const [role, group, size, anchor] of [['main', 'mains', sizes.main, [1 - ax, 1 - ay]], ['sub', 'subs', sizes.sub, [ax, ay]]]) {
      const choices = row[group] || [];
      const wanted = data[role] || (choices[0] && choices[0].icon);
      let item = choices.find(i => i.icon === wanted);
      const upload = data[role + 'Upload'];
      if (upload !== undefined && upload !== null) {
        if (!upload || typeof upload.document !== 'string') fail('Choose an SVG for ' + role + '.');
        item = customItem(upload.document, role, sizes.canvas);
      }
      if (!item) fail('The selected component does not belong to this pair.');
      const p = placement(item, size, anchor, [number(data[role + 'X']), number(data[role + 'Y'])], padding,
                          role === 'sub' ? (large ? 'exact' : (data.subSizeLock ?? 'auto')) : 'none', role === 'sub' && !large ? (data.subBoundSize ?? null) : null, canvas);
      chosen.push({role, size, item, p});
    }
    if (layout) {
      for (const entry of chosen) {
        const groups = layout[entry.role];
        if (!groups) {
          // Measured too: its artwork must be adjustable (layout_components refuses it otherwise).
          if (!drawables(parseXml(entry.item.engine_document ?? entry.item.document)).length) fail('The artwork has no drawable elements.');
          continue;
        }
        const baked = bake(entry.role, entry.item.engine_document ?? entry.item.document, groups, canvas);
        entry.item = {icon: entry.item.icon, document: baked.document, canvas, bounds: baked.bounds};
        entry.p = layoutPlacement(baked.bounds, canvas);
        const b = entry.p.painted_box;
        if (b.x < -1e-6 || b.y < -1e-6 || b.x + b.w > canvas + 1e-6 || b.y + b.h > canvas + 1e-6) {
          fail(`The adjusted ${entry.role} extends beyond the ${canvas}×${canvas} canvas.`);
        }
      }
    }
    const [main, sub] = chosen;
    const folded = fold(main.item.engine_document ?? main.item.document, main.p.box,
                        sub.item.engine_document ?? sub.item.document, sub.p.box, margin, canvas, large);
    const placements = chosen.map(c => ({...c.p, role: c.role, icon: c.item.icon}));
    const svg = restoreOriginalSub(engineDocument(folded.main, folded.state, canvas, folded.dots), sub.item, placements[1]);
    const warnings = [];
    for (const p of placements) {
      const b = p.painted_box;
      if (b.x < 0 || b.y < 0 || b.x + b.w > canvas + .01 || b.y + b.h > canvas + .01) {
        warnings.push(`Adjusted artwork extends beyond the ${canvas}×${canvas} canvas and may be clipped.`);
        break;
      }
    }
    return {svg, placements, position, canvas, filename: row.id + '.svg', warnings, margin, padding,
            subSizeLock: large ? 'exact' : (data.subSizeLock ?? 'auto'), subBoundSize: data.subBoundSize ?? '', ...(layout ? {layout} : {})};
  }

  // ======== one combination from /api/combinations (with forms), built the way side-pairs.html builds it ========

  const partOf = (item, role) => item.parts.find(p => p.role === role) || {role};
  const formKey = f => f && !f.native_text ? (f.model_key || `${f.family}/${f.icon}`) : null;

  // A hand-adjusted layout: groups that list their elements (`paths`); boxes without them only record where the
  // automatic placement put a part.
  function handLayout(item) {
    const out = {};
    for (const role of ['main', 'sub']) {
      const layout = partOf(item, role).layout;
      if (Array.isArray(layout) && layout.length && layout.every(g => Array.isArray(g.paths))) out[role] = layout;
    }
    return Object.keys(out).length ? out : null;
  }

  // The engine's pair row with `icons` ({main, sub}: keys) as its parts: the stored form when the icon is the one
  // it describes, else an item measured from the icon's drawing.
  function pairRow(item, icons, position) {
    const itemFor = role => {
      const p = partOf(item, role), key = icons[role];
      if (p.form && (key ? formKey(p.form) === key : p.form.native_text)) return p.form;
      if (!key) return null;
      const [family, name] = key.split('/');
      return role === 'sub' ? {icon: name, family, model_key: key, sizing_kind: 'symbol'} : {icon: name, family, model_key: key};
    };
    const main = itemFor('main'), sub = itemFor('sub');
    if (!main || !sub) fail('Pick both icons first.');
    return {id: item.reference_id, position: position || partOf(item, 'sub').position, mains: [main], subs: [sub]};
  }

  // → {svg, result, current, request}: the combined drawing and the POST /api/combinations/build entry that stores it.
  // `drawings` answers get(key) → {svg, svg_sha256} for the parts' current drawings.
  function pairRequest(item, drawings, {icons, position, layout, size = 64} = {}) {
    icons = icons || {main: partOf(item, 'main').icon, sub: partOf(item, 'sub').icon};
    const row = pairRow(item, icons, position);
    const documents = {};
    for (const role of ['main', 'sub']) {
      if (!icons[role]) continue;
      const d = drawings.get(icons[role]);
      if (!d || !d.svg) fail(`The ${role} ${icons[role]} has no drawing.`);
      documents[role] = d.svg;
    }
    const current = withDocuments(row, row.mains[0].icon, row.subs[0].icon, documents, size);
    const hand = layout === undefined ? handLayout(item) : layout;
    const result = render(current.row, {main: current.main, sub: current.sub, position: row.position, layout: hand, size});
    const box = p => [{x: p.painted_box.x + 2, y: p.painted_box.y + 2, w: p.painted_box.w - 4, h: p.painted_box.h - 4}];
    const part = (role, i) => ({icon: icons[role] || null, svg_sha256: icons[role] ? drawings.get(icons[role]).svg_sha256 : null,
                                layout: (hand && hand[role]) || box(result.placements[i]), ...(role === 'sub' ? {position: row.position} : {})});
    return {svg: result.svg, result, current,
            request: {reference_id: item.reference_id, svg: result.svg, parts: {main: part('main', 0), sub: part('sub', 1)}}};
  }

  // The elements of a drawing that a layout places (bake): every drawable one, by index.
  function drawableIndices(documentText) {
    const found = drawables(parseXml(documentText));
    return found.map(([el, own], i) => bbox(segmentsOf(el, own)) ? i : null).filter(i => i !== null);
  }

  return {SIZES, render, withDocuments, drawableIndices, pairRequest, handLayout, sha256, safeSvg, inlineClassStyles, customItem, CombineError, placement, capsule, engineSegments, pyFixed2, pyG12, pyStr, parseXml, tostring,
          internals: {Area, hull, clip, fitInto, intersect, orientation}};
});
