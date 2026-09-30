/* A sub's drawing normalized to SUB32 in the browser: a port of icon_set/scripts/sub_ink32.normalize_ink32 and
 * the parts of svgpathtools it runs on (Document.paths, Path parsing, bounding boxes, scaling, cropping at the
 * extrema, arcs as cubics, Path.d), so the document it returns is the one Python returns.
 *
 *   NormalizeInk32.normalize(svg, {text}) → [document, ink]
 *
 * Points are [x, y]; complex arithmetic is written out the way CPython computes it. Used by combine-side.js when
 * a side pair's sub was redrawn (side_recombine._normalized_sub); checked by icon_set/tests/js/ink32.test.mjs.
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.NormalizeInk32 = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  const SVG = 'http://www.w3.org/2000/svg';
  const DEG = Math.PI / 180.0;                         // CPython degToRad
  const radians = x => x * DEG, degrees = x => x / DEG;
  class NormalizeError extends Error {}
  const fail = m => { throw new NormalizeError(m); };

  // ---- complex numbers as CPython computes them

  const add = (a, b) => [a[0] + b[0], a[1] + b[1]];
  const sub = (a, b) => [a[0] - b[0], a[1] - b[1]];
  const mul = (a, b) => [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]];
  const muls = (k, z) => mul([k, 0], z);               // float * complex
  const div = (a, b) => {                              // _Py_c_quot (Smith)
    const ar = Math.abs(b[0]), ai = Math.abs(b[1]);
    if (ar >= ai) {
      if (ar === 0) return [0, 0];
      const ratio = b[1] / b[0], denom = b[0] + b[1] * ratio;
      return [(a[0] + a[1] * ratio) / denom, (a[1] - a[0] * ratio) / denom];
    }
    const ratio = b[0] / b[1], denom = b[0] * ratio + b[1];
    return [(a[0] * ratio + a[1]) / denom, (a[1] * ratio - a[0]) / denom];
  };
  const divs = (z, k) => div(z, [k, 0]);               // complex / float
  const same = (a, b) => a[0] === b[0] && a[1] === b[1];

  // Python's str(float) / '{}'.format(float)
  function pyStr(x) {
    if (Number.isInteger(x) && Math.abs(x) < 1e16) return Object.is(x, -0) ? '-0.0' : x.toFixed(1);
    if (Math.abs(x) >= 1e16 || (x !== 0 && Math.abs(x) < 1e-4)) {
      const [m, e] = x.toExponential().split('e');
      return `${m}e${e[0] === '-' ? '-' : '+'}${e.replace(/^[-+]/, '').padStart(2, '0')}`;
    }
    return String(x);
  }
  const pyRound = v => {                               // round(): half to even, an int
    const f = Math.floor(v), d = v - f;
    return d > .5 ? f + 1 : d < .5 ? f : (f % 2 === 0 ? f : f + 1);
  };

  // ---- segments (svgpathtools.path)

  function arc(start, radius, rotation, largeArc, sweep, end, autoscale = true) {
    if (same(start, end)) fail('AssertionError: arc start equals end');
    if (radius[0] === 0 || radius[1] === 0) fail('AssertionError: zero arc radius');
    const a = {type: 'A', start, radius: [Math.abs(radius[0]), Math.abs(radius[1])], rotation, large_arc: !!largeArc,
               sweep: !!sweep, end, autoscale};
    a.phi = radians(rotation);
    a.rot = [Math.cos(a.phi), Math.sin(a.phi)];       // cmath.exp(1j * phi)
    parameterize(a);
    return a;
  }

  function parameterize(a) {
    let [rx, ry] = a.radius;
    let rxs = rx * rx, rys = ry * ry;
    const zp1 = divs(mul(div([1, 0], a.rot), sub(a.start, a.end)), 2);
    const [x1p, y1p] = zp1, x1s = x1p * x1p, y1s = y1p * y1p;
    const check = (x1s / rxs) + (y1s / rys);
    if (check > 1) {
      if (!a.autoscale) fail('No such elliptic arc exists.');
      rx *= Math.sqrt(check); ry *= Math.sqrt(check);
      a.radius = [rx, ry]; rxs = rx * rx; rys = ry * ry;
    }
    const tmp = rxs * y1s + rys * x1s, radicand = (rxs * rys - tmp) / tmp;
    let radical;
    if (Math.abs(radicand) <= 1e-8) radical = 0;
    else { if (radicand < 0) fail('ValueError: math domain error'); radical = Math.sqrt(radicand); }
    const inner = [rx * y1p / ry - 0, 0 - (ry * x1p) / rx];     // rx*y1p/ry - 1j*ry*x1p/rx
    const cp = a.large_arc === a.sweep ? muls(-radical, inner) : muls(radical, inner);
    a.center = add(mul(a.rot, cp), divs(add(a.start, a.end), 2));
    const clip = v => Math.max(-1, Math.min(1, v));
    const u1 = [clip((x1p - cp[0]) / rx), clip((y1p - cp[1]) / ry)];
    const u2 = [clip((-x1p - cp[0]) / rx), clip((-y1p - cp[1]) / ry)];
    if (u1[1] > 0) a.theta = degrees(Math.acos(u1[0]));
    else if (u1[1] < 0) a.theta = -degrees(Math.acos(u1[0]));
    else a.theta = u1[0] > 0 ? 0 : 180;
    const det = u1[0] * u2[1] - u1[1] * u2[0];
    const acosand = clip(u1[0] * u2[0] + u1[1] * u2[1]) + 0;
    if (det > 0) a.delta = degrees(Math.acos(acosand));
    else if (det < 0) a.delta = -degrees(Math.acos(acosand));
    else a.delta = u1[0] * u2[0] + u1[1] * u2[1] > 0 ? 0 : 180;
    if (!a.sweep && a.delta >= 0) a.delta -= 360;
    else if (a.large_arc && a.delta <= 0) a.delta += 360;
  }

  function arcPoint(a, t) {
    const angle = (a.theta + t * a.delta) * Math.PI / 180;
    const [cosphi, sinphi] = a.rot, [rx, ry] = a.radius;
    return [rx * cosphi * Math.cos(angle) - ry * sinphi * Math.sin(angle) + a.center[0],
            rx * sinphi * Math.cos(angle) + ry * cosphi * Math.sin(angle) + a.center[1]];
  }

  function arcBbox(a) {
    let ax, ay;
    if (Math.cos(a.phi) === 0) { ax = Math.PI / 2; ay = 0; }
    else if (Math.sin(a.phi) === 0) { ax = 0; ay = Math.PI / 2; }
    else {
      const [rx, ry] = a.radius;
      ax = Math.atan(-(ry / rx) * Math.tan(a.phi));
      ay = Math.atan((ry / rx) / Math.tan(a.phi));
    }
    const inv = (ang, k) => ((ang + Math.PI * k) * (360 / (2 * Math.PI)) - a.theta) / a.delta;
    const xs = [a.start[0], a.end[0]], ys = [a.start[1], a.end[1]];
    for (let k = -4; k < 5; k++) {
      const tx = inv(ax, k), ty = inv(ay, k);
      if (0 <= tx && tx <= 1) xs.push(arcPoint(a, tx)[0]);
      if (0 <= ty && ty <= 1) ys.push(arcPoint(a, ty)[1]);
    }
    return [Math.min(...xs), Math.max(...xs), Math.min(...ys), Math.max(...ys)];
  }

  const bpoints = s => s.type === 'L' ? [s.start, s.end] : s.type === 'Q' ? [s.start, s.control, s.end] : [s.start, s.control1, s.control2, s.end];
  const bezier = p => p.length === 2 ? {type: 'L', start: p[0], end: p[1]}
    : p.length === 3 ? {type: 'Q', start: p[0], control: p[1], end: p[2]}
    : {type: 'C', start: p[0], control1: p[1], control2: p[2], end: p[3]};

  // bez2poly (highest power first) and polynomial2bezier, in complex arithmetic
  function bez2poly(p) {
    if (p.length === 4) return [add(add([-p[0][0], -p[0][1]], muls(3, sub(p[1], p[2]))), p[3]),
                                muls(3, add(sub(p[0], muls(2, p[1])), p[2])), muls(3, sub(p[1], p[0])), p[0]];
    if (p.length === 3) return [add(sub(p[0], muls(2, p[1])), p[2]), muls(2, sub(p[1], p[0])), p[0]];
    return [sub(p[1], p[0]), p[0]];
  }
  function poly2bez(c) {
    if (c.length === 4) return [c[3], add(divs(c[2], 3), c[3]), add(divs(add(c[1], muls(2, c[2])), 3), c[3]), add(add(add(c[0], c[1]), c[2]), c[3])];
    if (c.length === 3) return [c[2], add(divs(c[1], 2), c[2]), add(add(c[0], c[1]), c[2])];
    return [c[1], add(c[0], c[1])];
  }

  function point(s, t) {
    if (s.type === 'L') return add(s.start, mul(sub(s.end, s.start), [t, 0]));
    if (s.type === 'Q') {
      const tc = 1 - t;
      return add(add(muls(tc * tc, s.start), muls(2 * tc * t, s.control)), muls(t * t, s.end));
    }
    if (s.type === 'C') {
      const {start: p0, control1: p1, control2: p2, end: p3} = s;
      const inner = add(add([-p0[0], -p0[1]], muls(3, sub(p1, p2))), p3);
      const mid = add(sub(muls(3, add(p0, p2)), muls(6, p1)), muls(t, inner));
      return add(p0, muls(t, add(muls(3, sub(p1, p0)), muls(t, mid))));
    }
    return arcPoint(s, t);
  }

  function splitBezier(p, t) {
    const left = [], right = [];
    let pts = p;
    while (true) {
      if (pts.length === 1) { left.push(pts[0]); right.push(pts[0]); break; }
      left.push(pts[0]); right.push(pts[pts.length - 1]);
      const next = [];
      for (let i = 0; i < pts.length - 1; i++) next.push(add(muls(1 - t, pts[i]), muls(t, pts[i + 1])));
      pts = next;
    }
    right.reverse();
    return [left, right];
  }

  // numpy.roots for a degree ≤ 2 real polynomial (highest power first): the eigenvalues LAPACK finds for the
  // balanced companion matrix (dgebal, then dlanv2 on the 2 × 2 block).
  function roots(coeffs) {
    let lead = 0;
    while (lead < coeffs.length && coeffs[lead] === 0) lead++;
    let tail = coeffs.length - 1;
    while (tail >= lead && coeffs[tail] === 0) tail--;
    if (tail < lead) return [];
    const p = coeffs.slice(lead, tail + 1), zeros = coeffs.length - 1 - tail, out = [];
    if (p.length === 2) out.push([-p[1] / p[0], 0]);
    else if (p.length === 3) out.push(...eig2(-p[1] / p[0], -p[2] / p[0], 1, 0));
    else if (p.length > 3) fail('roots of degree > 2 are not needed');
    for (let i = 0; i < zeros; i++) out.push([0, 0]);
    return out;
  }

  // LAPACK dgeev on a 2 × 2 companion matrix: dgebal scales it (powers of 2, the diagonal in the norms,
  // as LAPACK ≥ 3.5 computes them), dlahqr hands the block straight to dlanv2.
  const fsign = (a, b) => (b > 0 || Object.is(b, 0)) ? Math.abs(a) : -Math.abs(a);   // Fortran SIGN
  const dlapy2 = (x, y) => {
    const xa = Math.abs(x), ya = Math.abs(y), w = Math.max(xa, ya), z = Math.min(xa, ya);
    return z === 0 || w > Number.MAX_VALUE ? w : w * Math.sqrt(1 + (z / w) * (z / w));
  };
  function eig2(a, b, c, d) {
    const m = [[a, b], [c, d]];
    let noconv = true;
    while (noconv) {
      noconv = false;
      for (let i = 0; i < 2; i++) {
        let cn = Math.hypot(m[0][i], m[1][i]), rn = Math.hypot(m[i][0], m[i][1]);
        let ca = Math.max(Math.abs(m[0][i]), Math.abs(m[1][i])), ra = Math.max(Math.abs(m[i][0]), Math.abs(m[i][1]));
        if (cn === 0 || rn === 0) continue;
        let g = rn / 2, f = 1;
        const s = cn + rn;
        while (cn < g && Math.max(f, cn, ca) < 1e300 && Math.min(rn, g, ra) > 1e-300) { f *= 2; cn *= 2; ca *= 2; rn /= 2; g /= 2; ra /= 2; }
        g = cn / 2;
        while (g >= rn && Math.max(rn, ra) < 1e300 && Math.min(f, cn, g, ca) > 1e-300) { f /= 2; cn /= 2; g /= 2; ca /= 2; rn *= 2; ra *= 2; }
        if ((cn + rn) >= 0.95 * s) continue;
        noconv = true;
        const inv = 1 / f;
        m[i][0] *= inv; m[i][1] *= inv; m[0][i] *= f; m[1][i] *= f;
      }
    }
    [[a, b], [c, d]] = m;
    const eps = 2 ** -52;                               // DLAMCH('P')
    if (c === 0) { /* upper triangular already */ }
    else if (b === 0) { const t = d; d = a; a = t; b = -c; c = 0; }
    else if ((a - d) === 0 && fsign(1, b) !== fsign(1, c)) { /* complex, diagonal already equal */ }
    else {
      const temp = a - d;
      let p = 0.5 * temp;
      const bcmax = Math.max(Math.abs(b), Math.abs(c)), bcmis = Math.min(Math.abs(b), Math.abs(c)) * fsign(1, b) * fsign(1, c);
      let scale = Math.max(Math.abs(p), bcmax);
      let z = (p / scale) * p + (bcmax / scale) * bcmis;
      if (z >= 4 * eps) {
        z = p + fsign(Math.sqrt(scale) * Math.sqrt(z), p);
        a = d + z;
        d = d - (bcmax / z) * bcmis;
        b = b - c; c = 0;
      } else {
        const sigma = b + c;
        p = 0.5 * temp;
        const tau = dlapy2(sigma, temp);
        const cs = Math.sqrt(0.5 * (1 + Math.abs(sigma) / tau)), sn = -(p / (tau * cs)) * fsign(1, sigma);
        const aa = a * cs + b * sn, bb = -a * sn + b * cs, cc = c * cs + d * sn, dd = -c * sn + d * cs;
        a = aa * cs + cc * sn; b = bb * cs + dd * sn; c = -aa * sn + cc * cs; d = -bb * sn + dd * cs;
        const mid = 0.5 * (a + d);
        a = mid; d = mid;
        if (c !== 0) {
          if (b !== 0) {
            if (fsign(1, b) === fsign(1, c)) {
              const sab = Math.sqrt(Math.abs(b)), sac = Math.sqrt(Math.abs(c));
              p = fsign(sab * sac, c);
              a = mid + p; d = mid - p; b = b - c; c = 0;
            }
          } else { b = -c; c = 0; }
        }
      }
    }
    if (c === 0) return [[a, 0], [d, 0]];
    const im = Math.sqrt(Math.abs(b)) * Math.sqrt(Math.abs(c));
    return [[a, im], [d, -im]];
  }

  function realMinMax(a) {                        // bezier_real_minmax, cubic
    const ext = [0, 1];
    const denom = a[0] - 3 * a[1] + 3 * a[2] - a[3];
    const at = t => a[0] + t * (3 * (a[1] - a[0]) + t * (3 * (a[0] + a[2]) - 6 * a[1] + t * (-a[0] + 3 * (a[1] - a[2]) + a[3])));
    if (Math.abs(denom) > 1e-12) {
      const delta = a[1] * a[1] - (a[0] + a[1]) * a[2] + a[2] * a[2] + (a[0] - a[1]) * a[3];
      if (delta >= 0) {
        const sq = Math.sqrt(delta), tau = a[0] - 2 * a[1] + a[2];
        const r1 = (tau + sq) / denom, r2 = (tau - sq) / denom;
        if (0 < r1 && r1 < 1) ext.push(r1);
        if (0 < r2 && r2 < 1) ext.push(r2);
      }
      const v = ext.map(at);
      return [Math.min(...v), Math.max(...v)];
    }
    // bezier2polynomial(a).deriv(): [3c0, 2c1, c2]; its roots in [0, 1]
    const c = [-a[0] + 3 * (a[1] - a[2]) + a[3], 3 * (a[0] - 2 * a[1] + a[2]), 3 * (a[1] - a[0])];
    const trimmed = c[0] === 0 ? (c[1] === 0 ? [c[2]] : [2 * c[1], c[2]]) : [3 * c[0], 2 * c[1], c[2]];
    for (const [re, im] of roots(trimmed)) if (Math.abs(im) <= 1e-8 && 0 <= re && re <= 1) ext.push(re);
    const v = ext.map(at);
    return [Math.min(...v), Math.max(...v)];
  }

  function bbox(s) {
    if (s.type === 'L') return [Math.min(s.start[0], s.end[0]), Math.max(s.start[0], s.end[0]), Math.min(s.start[1], s.end[1]), Math.max(s.start[1], s.end[1])];
    if (s.type === 'A') return arcBbox(s);
    const p = bpoints(s);
    if (p.length === 4) {
      const [x0, x1] = realMinMax(p.map(q => q[0])), [y0, y1] = realMinMax(p.map(q => q[1]));
      return [x0, x1, y0, y1];
    }
    // quadratic: the derivative's root in (0, 1) on each axis
    const c = bez2poly(p);
    const axis = k => {
      const [a, b, cc] = c.map(z => z[k]);
      const ext = [0, 1];
      for (const [re, im] of roots([2 * a, b])) if (Math.abs(im) <= 1e-8 && 0 < re && re < 1) ext.push(re);
      const v = ext.map(t => (a * t + b) * t + cc);
      return [Math.min(...v), Math.max(...v)];
    };
    const [x0, x1] = axis(0), [y0, y1] = axis(1);
    return [x0, x1, y0, y1];
  }

  function scaleSegment(s, k) {
    if (s.type === 'A') return arc(add(muls(k, sub(s.start, [0, 0])), [0, 0]), muls(k, s.radius), s.rotation, s.large_arc, s.sweep,
                                   add(muls(k, sub(s.end, [0, 0])), [0, 0]), s.autoscale);
    const c = bez2poly(bpoints(s)).map(z => muls(k, z));
    c[c.length - 1] = add(c[c.length - 1], sub([0, 0], muls(k, [0, 0])));
    return bezier(poly2bez(c));
  }
  function translateSegment(s, z) {
    if (s.type === 'A') return arc(add(s.start, z), s.radius, s.rotation, s.large_arc, s.sweep, add(s.end, z), s.autoscale);
    return bezier(bpoints(s).map(p => add(p, z)));
  }
  // transform_segments_together: a joint stays one point (an Arc keeps its parameters when its end moves).
  function together(path, fn) {
    const out = path.map(fn);
    for (let i = 0; i + 1 < path.length; i++) if (same(path[i].end, path[i + 1].start)) out[i].end = out[i + 1].start;
    return out;
  }

  function asCubicCurves(a, curves) {
    const slice = radians(a.delta) / curves;
    let current = radians(a.theta);
    const [rx, ry] = a.radius, theta = radians(a.rotation), [x0, y0] = a.center, ct = Math.cos(theta), st = Math.sin(theta);
    let start = a.start;
    const out = [];
    for (let i = 0; i < curves; i++) {
      const next = current + slice, tn = Math.tan(slice / 2.0);
      const alpha = Math.sin(slice) * (Math.sqrt(4 + 3 * (tn * tn)) - 1) / 3.0;
      const cs = Math.cos(current), ss = Math.sin(current);
      const e1x = -rx * ct * ss - ry * st * cs, e1y = -rx * st * ss + ry * ct * cs;
      const ce = Math.cos(next), se = Math.sin(next);
      let end = [x0 + rx * ce * ct - ry * se * st, y0 + rx * ce * st + ry * se * ct];
      if (i === curves - 1) end = a.end;
      const e2x = -rx * ct * se - ry * st * ce, e2y = -rx * st * se + ry * ct * ce;
      out.push({type: 'C', start, control1: [start[0] + alpha * e1x, start[1] + alpha * e1y], control2: [end[0] - alpha * e2x, end[1] - alpha * e2y], end});
      start = end; current = next;
    }
    return out;
  }

  function crop(s, t0, t1) {
    if (t0 === 0) return bezier(splitBezier(bpoints(s), t1)[0]);
    if (t1 === 1) return bezier(splitBezier(bpoints(s), t0)[1]);
    // svgpathtools finds t1 on the trimmed curve as its closest point to s(t1); that is (t1 - t0) / (1 - t0).
    const trimmed = crop(s, t0, 1);
    return crop(trimmed, 0, (t1 - t0) / (1 - t0));
  }

  // ---- parsing (svgpathtools.parser / svg_to_paths / document)

  function parsePath(d) {
    const tokens = [];
    for (const x of d.split(/([MmZzLlHhVvCcSsQqTtAa])/)) {
      if (/^[MmZzLlHhVvCcSsQqTtAa]$/.test(x)) tokens.push(x);
      for (const t of x.match(/[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?/g) || []) tokens.push(t);
    }
    tokens.reverse();
    const segs = [];
    let current = [0, 0], start = null, command = null, last = null, absolute = true;
    const num = () => { if (!tokens.length) fail('IndexError: pop from empty list'); return Number(tokens.pop()); };
    const pt = () => [num(), num()];
    while (tokens.length) {
      if (/^[MmZzLlHhVvCcSsQqTtAa]$/.test(tokens[tokens.length - 1])) {
        last = command; command = tokens.pop(); absolute = command === command.toUpperCase(); command = command.toUpperCase();
      } else {
        if (command === null) fail('Unallowed implicit command');
        last = command;
      }
      if (command === 'M') {
        const p = pt(); current = absolute ? p : add(current, p); start = current; command = 'L';
      } else if (command === 'Z') {
        if (!(start && same(current, start))) segs.push({type: 'L', start: current, end: start});
        current = start; command = null;
      } else if (command === 'L') {
        let p = pt(); if (!absolute) p = add(p, current);
        segs.push({type: 'L', start: current, end: p}); current = p;
      } else if (command === 'H') {
        let p = [num(), current[1]]; if (!absolute) p = [p[0] + current[0], p[1]];
        segs.push({type: 'L', start: current, end: p}); current = p;
      } else if (command === 'V') {
        let p = [current[0], num()]; if (!absolute) p = [p[0], p[1] + current[1]];
        segs.push({type: 'L', start: current, end: p}); current = p;
      } else if (command === 'C') {
        let c1 = pt(), c2 = pt(), e = pt();
        if (!absolute) { c1 = add(c1, current); c2 = add(c2, current); e = add(e, current); }
        segs.push({type: 'C', start: current, control1: c1, control2: c2, end: e}); current = e;
      } else if (command === 'S') {
        const c1 = !['C', 'S'].includes(last) ? current : sub(add(current, current), segs[segs.length - 1].control2);
        let c2 = pt(), e = pt();
        if (!absolute) { c2 = add(c2, current); e = add(e, current); }
        segs.push({type: 'C', start: current, control1: c1, control2: c2, end: e}); current = e;
      } else if (command === 'Q') {
        let c = pt(), e = pt();
        if (!absolute) { c = add(c, current); e = add(e, current); }
        segs.push({type: 'Q', start: current, control: c, end: e}); current = e;
      } else if (command === 'T') {
        const c = !['Q', 'T'].includes(last) ? current : sub(add(current, current), segs[segs.length - 1].control);
        let e = pt(); if (!absolute) e = add(e, current);
        segs.push({type: 'Q', start: current, control: c, end: e}); current = e;
      } else if (command === 'A') {
        const radius = pt(), rotation = num(), large = num(), sweep = num();
        let e = pt(); if (!absolute) e = add(e, current);
        segs.push(radius[0] === 0 || radius[1] === 0 ? {type: 'L', start: current, end: e} : arc(current, radius, rotation, large, sweep, e));
        current = e;
      }
    }
    return segs;
  }

  // The svg_to_paths converters: each shape as path data, numbers written as Python writes them.
  function shapeData(el) {
    const a = el.attrib, name = el.tag.slice(el.tag.indexOf('}') + 1), f = v => Number(v);
    if (name === 'path') return a.d ?? '';
    if (name === 'circle' || name === 'ellipse') {
      const cx = f(a.cx ?? 0), cy = f(a.cy ?? 0);
      let rx, ry;
      if (a.r !== undefined) rx = ry = f(a.r); else { rx = f(a.rx); ry = f(a.ry); }
      if ([rx, ry, cx, cy].some(Number.isNaN)) fail('ValueError: could not convert string to float');
      return 'M' + pyStr(cx - rx) + ',' + pyStr(cy) + 'a' + pyStr(rx) + ',' + pyStr(ry) + ' 0 1,0 ' + pyStr(2 * rx) + ',0'
        + 'a' + pyStr(rx) + ',' + pyStr(ry) + ' 0 1,0 ' + pyStr(-2 * rx) + ',0' + 'z';
    }
    if (name === 'line') return 'M' + (a.x1 ?? '0') + ' ' + (a.y1 ?? '0') + 'L' + (a.x2 ?? '0') + ' ' + (a.y2 ?? '0');
    if (name === 'polyline' || name === 'polygon') {
      const points = [...(a.points ?? '').matchAll(/([+-]?\d*[.\d]\d*[eE][+-]?\d+|[+-]?\d*[.\d]\d*)(?:\s*,\s*|\s+|(?=-))([+-]?\d*[.\d]\d*[eE][+-]?\d+|[+-]?\d*[.\d]\d*)/g)].map(m => [m[1], m[2]]);
      if (!points.length) return '';
      const closed = Number(points[0][0]) === Number(points[points.length - 1][0]) && Number(points[0][1]) === Number(points[points.length - 1][1]);
      if (name === 'polygon' && closed) points.push(points[0]);
      let d = 'M' + points.map(([x, y]) => `${x} ${y}`).join('L');
      if (name === 'polygon' || closed) d += 'z';
      return d;
    }
    if (name === 'rect') {
      const x = f(a.x ?? 0), y = f(a.y ?? 0), w = f(a.width ?? 0), h = f(a.height ?? 0);
      if ('rx' in a || 'ry' in a) {
        let rx = a.rx ?? null, ry = a.ry ?? null;
        if (rx === null) rx = ry || 0.; if (ry === null) ry = rx || 0.;
        rx = f(rx); ry = f(ry);
        const S = pyStr;
        return `M ${S(x + rx)} ${S(y)} L ${S(x + w - rx)} ${S(y)} A ${S(rx)} ${S(ry)} 0 0 1 ${S(x + w)} ${S(y + ry)} `
          + `L ${S(x + w)} ${S(y + h - ry)} A ${S(rx)} ${S(ry)} 0 0 1 ${S(x + w - rx)} ${S(y + h)} `
          + `L ${S(x + rx)} ${S(y + h)} A ${S(rx)} ${S(ry)} 0 0 1 ${S(x)} ${S(y + h - ry)} `
          + `L ${S(x)} ${S(y + ry)} A ${S(rx)} ${S(ry)} 0 0 1 ${S(x + rx)} ${S(y)} z`;
      }
      const S = pyStr;
      return `M${S(x)} ${S(y)} L ${S(x + w)} ${S(y)} L ${S(x + w)} ${S(y + h)} L ${S(x)} ${S(y + h)} z`;
    }
    return '';
  }

  // parse_transform: the 3 × 3 matrix of a transform attribute.
  function parseTransform(text) {
    let m = [[1, 0, 0], [0, 1, 0], [0, 0, 1]];
    if (!text) return m;
    const dot = (A, B) => A.map((row, i) => B[0].map((_, j) => row[0] * B[0][j] + row[1] * B[1][j] + row[2] * B[2][j]));
    for (const part of text.split(')').slice(0, -1)) {
      const [type, valueText] = part.split('(');
      const values = valueText.replace(/,/g, ' ').split(' ').filter(Boolean).map(Number);
      let t = [[1, 0, 0], [0, 1, 0], [0, 0, 1]];
      if (type.includes('matrix')) { if (values.length === 6) t = [[values[0], values[2], values[4]], [values[1], values[3], values[5]], [0, 0, 1]]; }
      else if (part.includes('translate')) { if ([1, 2].includes(values.length)) { t[0][2] = values[0]; if (values.length > 1) t[1][2] = values[1]; } }
      else if (part.includes('scale')) { if ([1, 2].includes(values.length)) { t[0][0] = values[0]; t[1][1] = values.length > 1 ? values[1] : values[0]; } }
      else if (part.includes('rotate')) {
        if ([1, 3].includes(values.length)) {
          const ang = values[0] * Math.PI / 180.0, [ox, oy] = values.length === 3 ? values.slice(1) : [0, 0];
          const r = [[Math.cos(ang), -Math.sin(ang), 0], [Math.sin(ang), Math.cos(ang), 0], [0, 0, 1]];
          t = dot(dot([[1, 0, ox], [0, 1, oy], [0, 0, 1]], r), [[1, 0, -ox], [0, 1, -oy], [0, 0, 1]]);
        }
      } else if (part.includes('skewX')) { if (values.length === 1) t[0][1] = Math.tan(values[0] * Math.PI / 180.0); }
      else if (part.includes('skewY')) { if (values.length === 1) t[1][0] = Math.tan(values[0] * Math.PI / 180.0); }
      m = dot(m, t);
    }
    return m;
  }
  const isIdentity = m => m.every((row, i) => row.every((v, j) => v === (i === j ? 1 : 0)));
  const matDot = (A, B) => A.map(row => B[0].map((_, j) => row[0] * B[0][j] + row[1] * B[1][j] + row[2] * B[2][j]));

  function transformPath(path, tf) {
    if (isIdentity(tf)) return path;
    const apply = p => [tf[0][0] * p[0] + tf[0][1] * p[1] + tf[0][2] * 1.0, tf[1][0] * p[0] + tf[1][1] * p[1] + tf[1][2] * 1.0];
    return together(path, s => {
      if (s.type !== 'A') return bezier(bpoints(s).map(apply));
      // svgpathtools.transform for an Arc: the ellipse's quadratic form under the inverse transform, and its
      // eigen-decomposition (numpy eigh: eigenvalues ascending). A translate or scale leaves it diagonal.
      const [[t00, t01], [t10, t11]] = [tf[0].slice(0, 2), tf[1].slice(0, 2)];
      // np.linalg.inv = dgesv(A, I): LU with partial pivoting, then the two triangular solves per column.
      let inv;
      if (Math.abs(t10) > Math.abs(t00)) {
        const l = t00 / t10, u = t01 - l * t11;
        const c0x1 = 1 / u, c0x0 = (0 - t11 * c0x1) / t10;            // column e0 → rows swapped: [0, 1]
        const c1x1 = -l / u, c1x0 = (1 - t11 * c1x1) / t10;           // column e1 → [1, -l]
        inv = [[c0x0, c1x0], [c0x1, c1x1]];
      } else {
        const l = t10 / t00, u = t11 - l * t01;
        const c0x1 = -l / u, c0x0 = (1 - t01 * c0x1) / t00;
        const c1x1 = 1 / u, c1x0 = (0 - t01 * c1x1) / t00;
        inv = [[c0x0, c1x0], [c0x1, c1x1]];
      }
      const rx2 = s.radius[0] * s.radius[0], ry2 = s.radius[1] * s.radius[1];
      const Q = [[1 / rx2, 0], [0, 1 / ry2]];
      const mm = (A, B) => [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]];
      const invT = [[inv[0][0], inv[1][0]], [inv[0][1], inv[1][1]]];
      let D = mm(mm(invT, Q), inv);
      D = [[0.5 * (D[0][0] + D[0][0]), 0.5 * (D[0][1] + D[1][0])], [0.5 * (D[1][0] + D[0][1]), 0.5 * (D[1][1] + D[1][1])]];
      let e0, e1, vec;
      if (D[0][1] === 0) {
        if (D[0][0] <= D[1][1]) { e0 = D[0][0]; e1 = D[1][1]; vec = [1, 0]; }
        else { e0 = D[1][1]; e1 = D[0][0]; vec = [0, 1]; }
      } else {
        const mean = (D[0][0] + D[1][1]) / 2, rad = Math.hypot((D[0][0] - D[1][1]) / 2, D[0][1]);
        e0 = mean - rad; e1 = mean + rad;
        vec = [D[0][1], e0 - D[0][0]];
        const n = Math.hypot(vec[0], vec[1]); vec = [vec[0] / n, vec[1] / n];
        if (vec[1] < 0 || (vec[1] === 0 && vec[0] < 0)) vec = [-vec[0], -vec[1]];
      }
      const rx = 1 / Math.sqrt(e0), ry = 1 / Math.sqrt(e1), rot = degrees(Math.atan2(vec[1], vec[0]));
      const start = apply(s.start), end = apply(s.end);
      if (rx === 0 || ry === 0) return {type: 'L', start, end};
      const sweep = tf[0][0] * tf[1][1] >= 0.0 ? s.sweep : !s.sweep;
      return arc(start, [rx, ry], s.rotation + rot, s.large_arc, sweep, end, true);
    });
  }

  // Document(svg).paths(): each group's shapes by type, then its groups, deepest last-pushed first.
  function documentPaths(svgText, parseXml) {
    const rootEl = parseXml(svgText);
    const KEYS = ['path', 'circle', 'ellipse', 'line', 'polyline', 'polygon', 'rect'];
    const stack = [{group: rootEl, tf: matDot([[1, 0, 0], [0, 1, 0], [0, 0, 1]], parseTransform(rootEl.attrib.transform))}];
    const paths = [];
    while (stack.length) {
      const top = stack.pop();
      for (const key of KEYS) {
        for (const el of top.group.children) {
          if (el.tag !== `{${SVG}}${key}`) continue;
          const tf = matDot(top.tf, parseTransform(el.attrib.transform));
          paths.push(transformPath(parsePath(shapeData(el)), tf));
        }
      }
      for (const el of top.group.children) {
        if (el.tag === `{${SVG}}g`) stack.push({group: el, tf: matDot(top.tf, parseTransform(el.attrib.transform))});
      }
    }
    return paths;
  }

  function pathBbox(path) {
    const b = path.map(bbox);
    return [Math.min(...b.map(v => v[0])), Math.max(...b.map(v => v[1])), Math.min(...b.map(v => v[2])), Math.max(...b.map(v => v[3]))];
  }
  function bounds(paths) {
    const b = paths.map(pathBbox);
    return [Math.min(...b.map(v => v[0])), Math.min(...b.map(v => v[2])), Math.max(...b.map(v => v[1])), Math.max(...b.map(v => v[3]))];
  }

  // Path.d(): absolute commands, a move wherever the path jumps.
  function pathD(path) {
    if (!path.length) return '';
    const parts = [];
    let current = null;
    for (const s of path) {
      if (!current || !same(current, s.start)) parts.push(`M ${pyStr(s.start[0])},${pyStr(s.start[1])}`);
      const P = p => `${pyStr(p[0])},${pyStr(p[1])}`;
      if (s.type === 'L') parts.push(`L ${P(s.end)}`);
      else if (s.type === 'C') parts.push(`C ${P(s.control1)} ${P(s.control2)} ${P(s.end)}`);
      else if (s.type === 'Q') parts.push(`Q ${P(s.control)} ${P(s.end)}`);
      else parts.push(`A ${pyStr(s.radius[0])},${pyStr(s.radius[1])} ${pyStr(s.rotation)} ${s.large_arc ? 1 : 0},${s.sweep ? 1 : 0} ${P(s.end)}`);
      current = s.end;
    }
    return parts.join(' ');
  }

  // ---- sub_ink32

  function snap(paths, preserveArcs = true, width = 32, stroke = 4) {
    const pt = z => [Math.max(stroke / 2, Math.min(width - stroke / 2, pyRound(z[0]))), Math.max(stroke / 2, Math.min(32 - stroke / 2, pyRound(z[1])))];
    return paths.map(path => {
      const segs = [];
      for (const original of path) {
        if (preserveArcs && original.type === 'A') {
          const start = pt(original.start), end = pt(original.end);
          if (same(start, end)) { segs.push({type: 'L', start, end}); continue; }
          const radius = [Math.max(1, pyRound(original.radius[0])), Math.max(1, pyRound(original.radius[1]))];
          const snapped = arc(start, radius, original.rotation, original.large_arc, original.sweep, end);
          const b = arcBbox(snapped);
          if (b[0] >= stroke / 2 - 1e-7 && b[1] <= width - stroke / 2 + 1e-7 && b[2] >= stroke / 2 - 1e-7 && b[3] <= 32 - stroke / 2 + 1e-7) { segs.push(snapped); continue; }
        }
        const curves = original.type === 'A' ? asCubicCurves(original, 2) : [original];
        for (const segment of curves) {
          let cuts = [0, 1];
          if (segment.type === 'C' || segment.type === 'Q') {
            const c = bez2poly(bpoints(segment)), n = c.length - 1;
            const deriv = c.slice(0, -1).map((z, i) => muls(n - i, z));          // poly1d.deriv
            for (const k of [0, 1]) {
              const coeffs = deriv.map(z => z[k]);
              for (const [re, im] of roots(coeffs)) if (Math.abs(im) < 1e-9 && 1e-8 < re && re < 1 - 1e-8) cuts.push(re);
            }
          }
          cuts = [...new Set(cuts)].sort((a, b) => a - b);
          for (let i = 0; i + 1 < cuts.length; i++) {
            const lo = cuts[i], hi = cuts[i + 1];
            const part = (lo || hi !== 1) ? (segment.type === 'L' ? {type: 'L', start: point(segment, lo), end: point(segment, hi)} : crop(segment, lo, hi)) : segment;
            if (part.type === 'L') segs.push({type: 'L', start: pt(part.start), end: pt(part.end)});
            else if (part.type === 'C') segs.push({type: 'C', start: pt(part.start), control1: pt(part.control1), control2: pt(part.control2), end: pt(part.end)});
            else segs.push({type: 'Q', start: pt(part.start), control: pt(part.control), end: pt(part.end)});
          }
        }
      }
      return segs;
    });
  }

  function normalize(document, {text = false} = {}, parseXml) {
    parseXml = parseXml || (typeof CombineSide !== 'undefined' ? CombineSide.parseXml : require('./combine-side.js').parseXml);
    const paths = documentPaths(document, parseXml).filter(p => p.length);
    if (!paths.length) fail('No supported paths in artwork');
    const [left, top, right, bottom] = bounds(paths);
    let extent = text ? bottom - top : Math.max(right - left, bottom - top);
    let stroke = 4, scale;
    if (extent <= 1e-12) {
      if (!text) fail('Artwork has no finite fitting extent');
      stroke = 32; scale = 8;
    } else scale = 28 / extent;
    let width = text ? (right - left) * scale + stroke : 32;
    const dx = width / 2 - (left + right) * scale / 2, dy = 16 - (top + bottom) * scale / 2;
    let fitted = paths.map(p => together(together(p, s => scaleSegment(s, scale)), s => translateSegment(s, [dx, dy])));
    if (text) width = pyRound(width);
    const unsnapped = fitted;
    fitted = snap(fitted, true, width, stroke);
    let [l, t, r, b] = bounds(fitted);
    extent = text ? b - t : Math.max(r - l, b - t);
    if (Math.abs(extent + stroke - 32) > 1e-6) fitted = snap(unsnapped, false, width, stroke);
    [l, t, r, b] = bounds(fitted);
    const ink = [l - stroke / 2, t - stroke / 2, r + stroke / 2, b + stroke / 2];
    if (text) {
      if (!(Math.abs(b - t + stroke - 32) < 1e-6) || !(ink[0] >= -1e-7 && ink[2] <= width + 1e-7)) fail('AssertionError');
    } else if (!(Math.min(...ink) >= -1e-7 && Math.max(...ink) <= 32 + 1e-7) || !(Math.abs(Math.max(r - l, b - t) + 4 - 32) < 1e-6)) {
      fail('AssertionError');
    }
    const W = String(width);  // an int: 32, or the rounded text width
    const out = `<svg xmlns="${SVG}" width="${W}" height="32" viewBox="0 0 ${W} 32" fill="none" stroke="currentColor" stroke-width="${stroke}" `
      + `stroke-linecap="round" stroke-linejoin="round">` + fitted.map((p, i) => `<path id="part-${i + 1}" d="${pathD(p)}" />`).join('') + '</svg>';
    return [out, {ink_bounds: ink, ink_width: r - l + stroke, ink_height: b - t + stroke, geometry_scale: scale, stroke, canvas: 32,
                  canvas_width: width, bounds: [l, t, r, b], grid: 1}];
  }

  return {normalize, NormalizeError, internals: {parsePath, bbox, roots, eig2, documentPaths, pathD, snap, crop}};
});
