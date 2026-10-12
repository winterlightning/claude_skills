#!/usr/bin/env node
// Measure the keyshape of every icon's displayed drawing (contract profiles, and the 72 parts main-54 / sub-36 on the
// tracer's keyshapes) and store the ones the server lists wrongly
// (POST /api/icons/keyshape), the same rule as the gallery (icon-guides.js measure): the drawing's stroke-centerline
// box on its profile canvas against the profile's contract keyshapes (within half a unit; the listed name, then SQUARE,
// then an L / M name over its XL / S alias), else FREE with the measured visible box (centerline box + half the stroke).
//
//   node icon_set/scripts/measure_keyshapes.mjs [--families solo,sub,container,symbol] [--limit N] [--go] [--jobs 8]
//
// Dry run unless --go (prints the counts and writes <scratch>/measured-keyshapes.json). --go needs PICTOGRAPHIC_SESSION or
// PICTOGRAPHIC_ADMIN_USER + PICTOGRAPHIC_ADMIN_PASSWORD. PICTOGRAPHIC_API picks the Worker (default production).
import {readFileSync, writeFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {createRequire} from 'node:module';
import path from 'node:path';
import {api, login} from './side_layout.mjs';

const HERE = path.dirname(new URL(import.meta.url).pathname);
const Side = createRequire(import.meta.url)('./templates/combine-side.js');
const lab = JSON.parse(readFileSync(path.resolve(HERE, '../../published/gallery/laboratory.json'), 'utf8'));
const BASE = (process.env.PICTOGRAPHIC_API || 'https://pictographic-review-next.pictographic.workers.dev').replace(/\/$/, '');
const UA = {'User-Agent': 'pictographic-work-queue/1.0'};

const args = process.argv.slice(2);
const opt = (n, d) => { const i = args.indexOf('--' + n); return i < 0 ? d : (args[i + 1] && !args[i + 1].startsWith('--') ? args[i + 1] : true); };
const families = String(opt('families', 'solo,sub,container,symbol,combination_main,symbol24,main-54,sub-36')).split(',');
const limit = Number(opt('limit', 0)) || Infinity, jobs = Number(opt('jobs', 8)), go = !!opt('go', false);

// The 72 side parts (families main-54, sub-36) are drawn on the tracer's 54 / 36 keyshapes (gridicon/rules.py
// KEYSHAPES_BY_GRID, as side_keyshape_check.mjs / the layout editor have them): outer boxes x, y, w, h. Stored under the
// contract-style names: portrait/landscape L -> VRECT_L / HRECT_L, tall/wide M -> VRECT_M / HRECT_M, slim/flat S ->
// VRECT_S / HRECT_S.
const TRACER = {
  54: {CIRCLE: [2, 2, 50, 50], SQUARE: [4, 4, 46, 46], VRECT_L: [6, 2, 42, 50], HRECT_L: [2, 6, 50, 42], VRECT_M: [8, 2, 38, 50],
       HRECT_M: [2, 8, 50, 38], VRECT_S: [11, 2, 32, 50], HRECT_S: [2, 11, 50, 32]},
  36: {CIRCLE: [0, 0, 36, 36], SQUARE: [0, 0, 36, 36], VRECT_L: [2, 0, 32, 36], HRECT_L: [0, 2, 36, 32], VRECT_M: [4, 0, 28, 36],
       HRECT_M: [0, 4, 36, 28], VRECT_S: [6, 0, 24, 36], HRECT_S: [0, 6, 36, 24]}};
const TRACER_FAMILIES = {'main-54': 54, 'sub-36': 36};
// name -> {centerline_bounds, visible_bounds} for an icon: its profile's contract keyshapes, or the tracer set.
function shapesFor(icon) {
  const grid = TRACER_FAMILIES[icon.family];
  if (grid) return Object.fromEntries(Object.entries(TRACER[grid]).map(([n, [x, y, w, h]]) =>
    [n, {visible_bounds: [x, y, x + w, y + h], centerline_bounds: [x + 2, y + 2, x + w - 2, y + h - 2]}]));
  return lab.keyshapes.resolved[icon.profile] || null;
}
const canvasOf = icon => TRACER_FAMILIES[icon.family] || lab.profile.profiles[icon.profile]?.canvas_size || icon.canvas_size;

// The keyshape a centerline box is on (icon-guides.js fit): within half a unit; the listed name, then SQUARE, then an
// L / M name over its XL / S alias; else FREE around the measured visible box.
function fit(shapes, box, listed, stroke) {
  const hits = Object.entries(shapes).filter(([, k]) => Array.isArray(k.centerline_bounds) && k.centerline_bounds.every((v, i) => Math.abs(v - box[i]) <= 0.5));
  const hit = hits.find(([n]) => n === listed) || hits.find(([n]) => n === 'SQUARE') || hits.find(([n]) => !/_(XL|S)$/.test(n)) || hits[0];
  if (hit) return {name: hit[0], bounds: hit[1].visible_bounds};
  const half = stroke / 2, r = v => Math.round(v * 100) / 100;
  return {name: 'FREE', bounds: [r(box[0] - half), r(box[1] - half), r(box[2] + half), r(box[3] + half)]};
}
// The drawing's centerline box on its canvas (the engine's sampled geometry: curves tight, like getBBox), scaled from
// its own viewBox (squared the way a browser shows it) to the canvas size.
function centerline(svg, size) {
  const squared = Side.squareViewBox(Side.inlineClassStyles(svg));
  const view = (squared.match(/viewBox="([^"]*)"/) || [])[1]?.trim().split(/[\s,]+/).map(Number);
  const side = view && view.length === 4 && view[2] > 0 ? view[2] : size;
  const item = Side.customItem(squared, 'main', 64);
  return item.bounds.map(v => v * size / side);
}

async function pool(items, n, fn) { let i = 0; await Promise.all(Array.from({length: n}, async () => { while (i < items.length) await fn(items[i++]); })); }

const icons = [];
for (const family of families) {
  // The list pages by offset / limit (it answers with the limit it used); stop at the family's total.
  for (let offset = 0; ; ) {
    const {data} = await api(`/api/icons?family=${family}&offset=${offset}&limit=200&sort=name`);
    icons.push(...data.items.filter(i => shapesFor(i)));
    offset += data.items.length;
    process.stderr.write(`\rlisted ${icons.length} (${family} ${offset} of ${data.total})`);
    if (!data.items.length || offset >= data.total || icons.length >= limit) break;
  }
  if (icons.length >= limit) break;
}
process.stderr.write('\n');
const list = icons.slice(0, limit === Infinity ? icons.length : limit);
const counts = {measured: 0, same: 0, differ: 0, failed: 0}, differ = [], failures = [];
let done = 0;
await pool(list, jobs, async icon => {
  try {
    const r = await fetch(BASE + '/api/icon-artwork/svg?icon=' + encodeURIComponent(icon.key), {headers: UA, signal: AbortSignal.timeout(60000)});
    if (!r.ok) throw Error('HTTP ' + r.status);
    const svg = await r.text();
    const m = fit(shapesFor(icon), centerline(svg, canvasOf(icon)), icon.keyshape, icon.style?.stroke_width || 4);
    counts.measured++;
    const same = icon.keyshape === m.name && Array.isArray(icon.keyshape_bounds) && icon.keyshape_bounds.every((v, i) => Math.abs(v - m.bounds[i]) < 0.01);
    if (same) counts.same++;
    else { counts.differ++; differ.push({key: icon.key, svg_sha256: createHash('sha256').update(svg).digest('hex'), keyshape: m.name, keyshape_bounds: m.bounds, listed: icon.keyshape}); }
  } catch (e) { counts.failed++; failures.push(`${icon.key}: ${e.message}`); }
  if (++done % 100 === 0) process.stderr.write(`\rmeasured ${done} of ${list.length}`);
});
process.stderr.write('\n');
const out = path.resolve(process.env.MEASURE_OUT || '/tmp', 'measured-keyshapes.json');
writeFileSync(out, JSON.stringify({counts, differ, failures}, null, 1));
const changes = {};
for (const d of differ) { const k = `${d.listed} -> ${d.keyshape}`; changes[k] = (changes[k] || 0) + 1; }
console.log(JSON.stringify({counts, top_changes: Object.entries(changes).sort((a, b) => b[1] - a[1]).slice(0, 15), out}, null, 1));
if (!go) { console.error('dry run: add --go to store the differing measurements'); process.exit(0); }
await login();
let stored = 0;
for (let i = 0; i < differ.length; i += 200) {
  const {data} = await api('/api/icons/keyshape', {measurements: differ.slice(i, i + 200).map(({listed, ...m}) => m)});
  stored += data.stored;
  process.stderr.write(`\rstored ${stored} of ${differ.length}`);
}
process.stderr.write('\n');
console.log(JSON.stringify({stored}));
