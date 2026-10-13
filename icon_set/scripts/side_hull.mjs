#!/usr/bin/env node
// How a side pair's main and sub sit together, seen as two convex hulls (/side-layout-adjust helper; a reference for the
// eye, never the judge).
//
//   node icon_set/scripts/side_hull.mjs <DIR> [<DIR> ...] [--current] [--json]
//
// DIR is a side_layout.mjs work folder; the pair is composed from layout.json (the proposal), or base-layout.json with
// --current (the stored layout). The main's ink (uncut, where it was placed) and the sub's ink come from the same
// rasters as side_overlap.mjs; each gets its convex hull, the outline a rubber band would make around it. Measured, in
// grid units:
//   main / sub      hull area, ink share of the hull (solidity: low for an open shape such as a hand or a cart), and
//                   hull centroid
//   sub_to_main     sub hull area over main hull area (hierarchy: the sub reads secondary, about 0.3 to 0.6)
//   hull_gap        clear space between the two hulls (0 when they overlap)
//   overlap         area where the hulls overlap, and its share of the sub hull (sub_in_main_pct): how far the sub sits
//                   into the main's silhouette; near 100 the main surrounds the sub (a container, not a side pair)
//   direction       compass direction from the main's centroid to the sub's centroid (should agree with the position)
//   combined        hull of both parts: area, share of the canvas, and how far its centroid sits off the canvas centre
//                   (balance; a large offset leaves an empty side)
// Writes DIR/hull.png (hull-current.png with --current): the combination, the main hull red, the sub hull blue, their
// overlap purple, the combined hull dashed, the centroids as dots and the canvas centre as a cross.
import {execFileSync} from 'node:child_process';
import {existsSync, rmSync, writeFileSync} from 'node:fs';
import path from 'node:path';
import {compose, layoutFor, readJSON} from './side_compose.mjs';
import {analyze} from './side_overlap.mjs';

const RES = 8; // raster pixels a grid unit, as side_overlap.mjs

// ---- geometry ----

// Corner points of every ink pixel at the left and right end of each row (enough for the hull), in grid units.
function inkPoints(mask, n) {
  const pts = [];
  for (let y = 0; y < n; y++) {
    let x0 = -1, x1 = -1;
    for (let x = 0; x < n; x++) if (mask[y * n + x]) { if (x0 < 0) x0 = x; x1 = x; }
    if (x0 < 0) continue;
    pts.push([x0 / RES, y / RES], [x0 / RES, (y + 1) / RES], [(x1 + 1) / RES, y / RES], [(x1 + 1) / RES, (y + 1) / RES]);
  }
  return pts;
}
// Andrew's monotone chain: the convex hull, counter-clockwise in y-down space order as returned, no repeated point.
function hull(points) {
  const p = [...points].sort((a, b) => a[0] - b[0] || a[1] - b[1]);
  if (p.length < 3) return p;
  const cross = (o, a, b) => (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
  const lower = [], upper = [];
  for (const q of p) { while (lower.length >= 2 && cross(lower.at(-2), lower.at(-1), q) <= 0) lower.pop(); lower.push(q); }
  for (const q of p.reverse()) { while (upper.length >= 2 && cross(upper.at(-2), upper.at(-1), q) <= 0) upper.pop(); upper.push(q); }
  return lower.slice(0, -1).concat(upper.slice(0, -1));
}
const area = poly => Math.abs(poly.reduce((s, [x, y], i) => { const [u, v] = poly[(i + 1) % poly.length]; return s + x * v - u * y; }, 0)) / 2;
function centroid(poly) {
  let a = 0, cx = 0, cy = 0;
  poly.forEach(([x, y], i) => { const [u, v] = poly[(i + 1) % poly.length], c = x * v - u * y; a += c; cx += (x + u) * c; cy += (y + v) * c; });
  return a ? [cx / (3 * a), cy / (3 * a)] : poly[0] || [0, 0];
}
// Sutherland-Hodgman: the overlap of two convex polygons.
function clip(subject, clipper) {
  const sign = Math.sign(area2(clipper)) || 1;
  let out = subject;
  for (let i = 0; i < clipper.length && out.length; i++) {
    const a = clipper[i], b = clipper[(i + 1) % clipper.length], input = out;
    const inside = p => sign * ((b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])) >= 0;
    const cut = (p, q) => {
      const d = (b[0] - a[0]) * (q[1] - p[1]) - (b[1] - a[1]) * (q[0] - p[0]);
      const t = ((b[0] - a[0]) * (a[1] - p[1]) - (b[1] - a[1]) * (a[0] - p[0])) / d;
      return [p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])];
    };
    out = [];
    input.forEach((p, j) => {
      const q = input[(j + 1) % input.length];
      if (inside(q)) { if (!inside(p)) out.push(cut(p, q)); out.push(q); } else if (inside(p)) out.push(cut(p, q));
    });
  }
  return out;
}
function area2(poly) { return poly.reduce((s, [x, y], i) => { const [u, v] = poly[(i + 1) % poly.length]; return s + x * v - u * y; }, 0); }
const pointSeg = ([px, py], [ax, ay], [bx, by]) => {
  const dx = bx - ax, dy = by - ay, l = dx * dx + dy * dy, t = l ? Math.max(0, Math.min(1, ((px - ax) * dx + (py - ay) * dy) / l)) : 0;
  return Math.hypot(px - ax - t * dx, py - ay - t * dy);
};
// Clear space between two separate convex polygons (0 when they overlap).
function gap(a, b, overlapArea) {
  if (overlapArea > 1e-6) return 0;
  let best = Infinity;
  for (const [P, Q] of [[a, b], [b, a]]) for (const p of P) for (let i = 0; i < Q.length; i++) best = Math.min(best, pointSeg(p, Q[i], Q[(i + 1) % Q.length]));
  return best;
}
const COMPASS = ['ri', 'br', 'bo', 'bl', 'le', 'tl', 'to', 'tr'];
const direction = ([ax, ay], [bx, by]) => COMPASS[(Math.round(Math.atan2(by - ay, bx - ax) / (Math.PI / 4)) + 8) % 8];
const r1 = v => +v.toFixed(1), r2 = v => +v.toFixed(2), pt = p => p.map(r1);

// ---- one folder ----

export function hullOf(dir, {current = false} = {}) {
  const layout = readJSON(path.join(dir, current ? 'base-layout.json' : 'layout.json'));
  const composed = compose(dir, layout);
  const a = analyze(composed, layoutFor(dir, layout));
  const {n, main, sub} = a.masks, canvas = composed.result.canvas || 64, unit = RES * RES;
  const ink = mask => mask.reduce((s, v) => s + v, 0) / unit;
  const mh = hull(inkPoints(main, n)), sh = hull(inkPoints(sub, n)), all = hull([...mh, ...sh]);
  const ov = mh.length > 2 && sh.length > 2 ? clip(sh, mh) : [];
  const ma = area(mh), sa = area(sh), oa = ov.length > 2 ? area(ov) : 0, ca = area(all);
  const mc = centroid(mh), sc = centroid(sh), cc = centroid(all);
  const res = {
    dir, layout: current ? 'stored' : 'proposed', position: layout.position, canvas,
    main: {hull_area: r1(ma), solidity: r2(ink(main) / ma), centroid: pt(mc)},
    sub: {hull_area: r1(sa), solidity: r2(ink(sub) / sa), centroid: pt(sc)},
    sub_to_main: r2(sa / ma),
    hull_gap: r2(gap(mh, sh, oa)),
    overlap: {area: r1(oa), sub_in_main_pct: r1(sa ? 100 * oa / sa : 0)},
    direction: direction(mc, sc),
    combined: {hull_area: r1(ca), canvas_pct: r1(100 * ca / (canvas * canvas)), centroid: pt(cc),
               off_centre: pt([cc[0] - canvas / 2, cc[1] - canvas / 2])},
  };
  res.picture = picture(dir, composed.svg, canvas, {mh, sh, ov, all, mc, sc, cc}, current ? 'hull-current.png' : 'hull.png');
  return res;
}

function picture(dir, svg, canvas, {mh, sh, ov, all, mc, sc, cc}, name) {
  const poly = (p, style) => p.length > 2 ? `<polygon points="${p.map(q => q.map(r2).join(',')).join(' ')}" ${style}/>` : '';
  const dot = ([x, y], fill) => `<circle cx="${r2(x)}" cy="${r2(y)}" r="1.2" fill="${fill}"/>`;
  // The combination nested at canvas size: its own width / height (pixel size) give way to the canvas's.
  const inner = svg.replace(/<\?xml[^>]*>/, '').replace(/<svg\b[^>]*>/, tag =>
    tag.replace(/\s(width|height|x|y)="[^"]*"/g, '').replace(/<svg\b/, `<svg x="0" y="0" width="${canvas}" height="${canvas}"`));
  const c = canvas / 2;
  const out = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${canvas} ${canvas}" width="${canvas * 4}" height="${canvas * 4}">
<rect width="${canvas}" height="${canvas}" fill="#fff"/>
<g opacity="0.45">${inner}</g>
${poly(mh, 'fill="#e63c32" fill-opacity="0.12" stroke="#e63c32" stroke-width="0.4"')}
${poly(sh, 'fill="#285ae6" fill-opacity="0.12" stroke="#285ae6" stroke-width="0.4"')}
${poly(ov, 'fill="#8a2be2" fill-opacity="0.35" stroke="none"')}
${poly(all, 'fill="none" stroke="#555" stroke-width="0.3" stroke-dasharray="1 1"')}
<path d="M${c - 1.5} ${c}h3M${c} ${c - 1.5}v3" stroke="#555" stroke-width="0.3"/>
${dot(mc, '#e63c32')}${dot(sc, '#285ae6')}${dot(cc, '#555')}
</svg>`;
  const file = path.join(dir, name), tmp = file + '.svg';
  try { writeFileSync(tmp, out); execFileSync('rsvg-convert', ['-o', file, tmp], {timeout: 30000}); return file; }
  catch { return null; } finally { rmSync(tmp, {force: true}); }
}

if (process.argv[1] && path.resolve(process.argv[1]) === new URL(import.meta.url).pathname) {
  const args = process.argv.slice(2), current = args.includes('--current'), asJson = args.includes('--json');
  const dirs = args.filter(a => !a.startsWith('--'));
  if (!dirs.length) { console.error('usage: side_hull.mjs <dir> [<dir> ...] [--current] [--json]'); process.exit(2); }
  const out = [];
  for (const d of dirs) {
    const dir = path.resolve(d);
    if (!existsSync(path.join(dir, 'item.json'))) { console.error(`${d}: not a work folder`); continue; }
    try { out.push(hullOf(dir, {current})); } catch (e) { console.error(`${d}: ${e.message}`); }
  }
  if (asJson) console.log(JSON.stringify(out, null, 2));
  else for (const r of out) console.log(`${path.basename(r.dir)} ${r.position} (${r.layout}): sub→ ${r.direction} · sub/main ${r.sub_to_main}`
    + ` · ${r.hull_gap ? `hull gap ${r.hull_gap}` : `hulls overlap ${r.overlap.area} (${r.overlap.sub_in_main_pct}% of the sub)`}`
    + ` · solidity main ${r.main.solidity} sub ${r.sub.solidity} · combined ${r.combined.canvas_pct}% of canvas, off centre ${r.combined.off_centre.join(',')}`
    + `\n     ${r.picture || 'no picture'}`);
}
