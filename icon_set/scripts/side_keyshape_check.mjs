#!/usr/bin/env node
// Is each part of a side pair on the keyshape system? The layout editor's presets (web/side-pairs/src/lib/editor.svelte.js)
// allow a part only on its own contract keyshape (laboratory.json: SOLO48 for the main, SUB32 for the sub; the keyshape
// whose w - h matches the drawing, since another one stretches it) or its own drawn box scaled evenly, grown or shrunk by the same amount on both axes in steps of 4 (main 32–64, sub 20–44), and sitting in its
// corner of the 64 canvas at the 2-unit padding: the main opposite the sub, the sub at its position.
// A layout that moves or stretches a part off those boxes breaks the keyshape system and is never accepted.
//
//   node icon_set/scripts/side_keyshape_check.mjs <dir> [<dir> ...]   proposed layout (layout.json)
//         --current      the stored layout (base-layout.json)
//         --role main    check one role only (default: main and sub)
//         --json         details
//         --recheck [--since YYYY-MM-DD]   list reviewed pairs whose review breaks the system (no dirs)
//         --fit          print the nearest allowed boxes for a part that is off the system
//         --list main|sub [--position P]   every allowed box (x,y,w,h for side_layout.mjs preview --main / --sub)
//
// Exits 1 if any folder fails.
import {existsSync, readFileSync} from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {SIZE, WORK_NAME} from './side_compose.mjs';

const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const CANVAS = SIZE, PADDING = 2;
// Presets as the layout editor has them (web/side-pairs/src/lib/editor.svelte.js PRESET_SETS): 9 main and 7 sub sizes
// in steps of 4 around the base size.
const ROLES = SIZE === 72
  ? {main: {profile: 'MAIN54', base: 54, sizes: [38, 42, 46, 50, 54, 58, 62, 66, 70]}, sub: {profile: 'SUB36', base: 36, sizes: [24, 28, 32, 36, 40, 44, 48]}}
  : {main: {profile: 'SOLO48', base: 48, sizes: [32, 36, 40, 44, 48, 52, 56, 60, 64]}, sub: {profile: 'SUB32', base: 32, sizes: [20, 24, 28, 32, 36, 40, 44]}};
export const ROLE_PRESETS = ROLES;
const ANCHORS = {br: [1, 1], bl: [0, 1], tr: [1, 0], tl: [0, 0], ri: [1, .5], le: [0, .5], bo: [.5, 1], to: [.5, 0]};

const lab = JSON.parse(readFileSync(path.join(REPO, 'published/gallery/laboratory.json'), 'utf8'));
// Distinct keyshapes of a profile (names that share bounds are one keyshape), as [name, x0, y0, x1, y1].
const shapesOf = profile => {
  const seen = new Map();
  for (const [name, k] of Object.entries(lab.keyshapes.resolved[profile] || {})) {
    const b = k.centerline_bounds; if (!Array.isArray(b)) continue;
    const key = b.join(','); if (!seen.has(key)) seen.set(key, [name, ...b]);
  }
  return [...seen.values()];
};
// The 72 parts are drawn on the tracer's 54 / 36 keyshapes (gridicon/rules.py KEYSHAPES_BY_GRID, outer boxes x, y, w, h,
// as editor.svelte.js KEYSHAPES72 has them); a centerline box is the outer box less half the 4-unit stroke.
const KEYSHAPES72 = {
  main: {CIRCLE: [2, 2, 50, 50], SQUARE: [4, 4, 46, 46], portrait_L: [6, 2, 42, 50], landscape_L: [2, 6, 50, 42], tall_M: [8, 2, 38, 50],
         wide_M: [2, 8, 50, 38], slim_S: [11, 2, 32, 50], flat_S: [2, 11, 50, 32]},
  sub: {CIRCLE: [0, 0, 36, 36], SQUARE: [0, 0, 36, 36], portrait_L: [2, 0, 32, 36], landscape_L: [0, 2, 36, 32], tall_M: [4, 0, 28, 36],
        wide_M: [0, 4, 36, 28], slim_S: [6, 0, 24, 36], flat_S: [0, 6, 36, 24]}};
const shapes72 = role => {
  const seen = new Map();
  for (const [name, [x, y, w, h]] of Object.entries(KEYSHAPES72[role])) {
    const b = [x + 2, y + 2, x + w - 2, y + h - 2], key = b.join(',');
    if (!seen.has(key)) seen.set(key, [name, ...b]);
  }
  return [...seen.values()];
};
const SHAPES = SIZE === 72 ? {main: shapes72('main'), sub: shapes72('sub')} : {main: shapesOf('SOLO48'), sub: shapesOf('SUB32')};

const union = boxes => boxes.reduce((a, b) => [Math.min(a[0], b[0]), Math.min(a[1], b[1]), Math.max(a[2], b[2]), Math.max(a[3], b[3])]);

// Every allowed centerline box [x0, y0, x1, y1] of a role, with its name, as presetBox() places it.
function allowed(role, position, own) {
  const [px, py] = ANCHORS[position] || [1, 1], [ax, ay] = role === 'main' ? [1 - px, 1 - py] : [px, py];
  const {base, sizes} = ROLES[role], out = [];
  const onShape = own && SHAPES[role].some(([, ...b]) => b.every((v, i) => Math.abs(v - own[i]) < .05));
  const place = (w, h, name, size) => {
    if (w < 4 || h < 4 || w + 4 > CANVAS - 2 * PADDING || h + 4 > CANVAS - 2 * PADDING) return;
    const x = Math.round(PADDING + (CANVAS - 2 * PADDING - w - 4) * ax) + 2, y = Math.round(PADDING + (CANVAS - 2 * PADDING - h - 4) * ay) + 2;
    out.push({name, size, box: [x, y, x + w, y + h]});
  };
  for (const size of sizes) {
    // Only the part's own keyshape (the one whose w - h matches the drawing's box): another keyshape stretches it.
    // The part's own keyshape first: where two presets give the same box (a circle at 44 = a square at 48), the own one
    // names it and its size is the one compared.
    const isOwn = b => own && b.every((v, i) => Math.abs(v - own[i]) < .05);
    for (const [name, x0, y0, x1, y1] of [...SHAPES[role]].sort((a, b) => isOwn(b.slice(1)) - isOwn(a.slice(1))))
      if (!own || Math.abs((x1 - x0) - (y1 - y0) - ((own[2] - own[0]) - (own[3] - own[1]))) < .5) place(x1 - x0 + size - base, y1 - y0 + size - base, name, size);
    // 'own' (scaled evenly) only for a drawing on no keyshape, as the editor offers it.
    if (own && !onShape) { const k = size / base; place(Math.round((own[2] - own[0]) * k), Math.round((own[3] - own[1]) * k), 'own', size); }
  }
  // At 72 the engine places a part drawn on its own grid "as drawn": its whole 54 / 36 canvas sits in the corner and the
  // drawing keeps its offset inside it (a flat cloud drawn 8 units down its 36 canvas sits 8 below the padding). That
  // automatic placement is on the system too, at the base size.
  if (SIZE === 72 && own) {
    const cx = Math.round(PADDING + (CANVAS - 2 * PADDING - base) * ax), cy = Math.round(PADDING + (CANVAS - 2 * PADDING - base) * ay);
    out.push({name: 'as drawn', size: base, box: [cx + own[0], cy + own[1], cx + own[2], cy + own[3]].map(v => Math.round(v))});
  }
  return out;
}

const same = (a, b) => a.every((v, i) => Math.abs(v - b[i]) < 1e-6);
const dist = (a, b) => Math.max(...a.map((v, i) => Math.abs(v - b[i])));
const fmt = b => `${b[0]},${b[1]},${b[2] - b[0]},${b[3] - b[1]}`;

// Check one layout ({position, main: groups, sub: groups}) of the work folder `dir` against the keyshape presets.
// Returns {ok, position, roles: {main|sub: {ok, box, preset | problem + nearest}}}.
export function keyshapeCheck(dir, layout, roles = ['main', 'sub']) {
  const elements = existsSync(path.join(dir, 'elements.json')) ? JSON.parse(readFileSync(path.join(dir, 'elements.json'), 'utf8')) : {};
  let item = {};
  try { item = JSON.parse(readFileSync(path.join(dir, 'item.json'), 'utf8')); } catch {}
  const nativeText = (item.parts || []).some(p => p.role === 'sub' && !p.icon) || item.native_text;
  const res = {position: layout.position, roles: {}, ok: true};
  for (const role of roles) {
    const groups = layout[role] || [];
    if (!groups.length) continue;
    if (role === 'sub' && nativeText) { res.roles.sub = {ok: true, note: 'native text: no keyshape presets'}; continue; }
    const box = union(groups.map(g => [g.x, g.y, g.x + g.w, g.y + g.h]));
    const sources = (elements[role] || []).map(e => e.source).filter(Array.isArray);
    const own = sources.length ? union(sources) : null;
    const list = allowed(role, layout.position, own);
    // Several presets can give the same box (a circle at 44 = a square at 48): name it after the part's own keyshape.
    const ownName = own && SHAPES[role].find(([, ...b]) => b.every((v, i) => Math.abs(v - own[i]) < .05))?.[0];
    const hits = list.filter(a => same(a.box, box));
    const hit = hits.find(a => a.name === ownName) || hits.find(a => a.size === ROLES[role].base) || hits[0];
    const r = {box: fmt(box), ok: !!hit};
    if (hit) r.preset = `${hit.name} at ${hit.size}`;
    else {
      r.problem = `the ${role} box ${fmt(box)} is not a keyshape preset at ${layout.position}`;
      r.nearest = list.map(a => ({...a, d: dist(a.box, box)})).sort((a, b) => a.d - b.d).slice(0, 4)
        .map(a => `${a.name} at ${a.size}: ${fmt(a.box)}`);
      res.ok = false;
    }
    res.roles[role] = r;
  }
  return res;
}

// Every allowed box of a role in the work folder `dir` at `position`, for preview --main / --sub (x,y,w,h).
export function presetBoxes(dir, role, position) {
  const elements = existsSync(path.join(dir, 'elements.json')) ? JSON.parse(readFileSync(path.join(dir, 'elements.json'), 'utf8')) : {};
  const sources = (elements[role] || []).map(e => e.source).filter(Array.isArray);
  const own = sources.length ? union(sources) : null, seen = new Set();
  const ownName = own && SHAPES[role].find(([, ...b]) => b.every((v, i) => Math.abs(v - own[i]) < .05))?.[0];
  // One entry per box, named after the own keyshape when several presets give it.
  return allowed(role, position, own).sort((a, b) => (b.name === ownName) - (a.name === ownName))
    .filter(a => !seen.has(a.box.join()) && seen.add(a.box.join())).sort((a, b) => a.size - b.size || a.name.localeCompare(b.name))
    .map(a => ({name: a.name, size: a.size, box: fmt(a.box)}));
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
const args = process.argv.slice(2);
const flag = n => { const i = args.indexOf(n); if (i < 0) return false; args.splice(i, 1); return true; };
const opt = n => { const i = args.indexOf(n); if (i < 0) return null; const v = args[i + 1]; args.splice(i, 2); return v; };
const current = flag('--current'), asJson = flag('--json'), fit = flag('--fit'), only = opt('--role'), list = opt('--list');
if (!args.length && !process.argv.includes('--recheck')) { console.error('usage: side_keyshape_check.mjs <dir> [...] [--current] [--role main|sub] [--json] [--fit]'); process.exit(2); }


// --recheck: reviewed pairs (icon_set/work/side-layout-adjust/*/review.json) whose review breaks the keyshape system, or
// a fix that shrank the sub without a recorded reason (layout first, resize last): a fix whose proposal is off it, or an ok whose stored layout is off it. One reference id per line, for the launcher.
if (flag('--recheck')) {
  // --since YYYY-MM-DD: only reviews recorded on or after that local day.
  const since = opt('--since');
  // --keyshape-only: skip the sub-size rule (list only layouts off the keyshape system).
  const noSub = flag('--keyshape-only');
  // --older-than ISO: also every fix and redraw recorded before that time (made under older skill rules), except pairs
  // the user flagged on the flag page (icon_set/work/side-layout-flags/flags.json) and stored layouts kept on purpose.
  const olderThan = opt('--older-than');
  let userFlags = {};
  try { userFlags = JSON.parse(readFileSync(path.join(REPO, 'icon_set/work/side-layout-flags/flags.json'), 'utf8')); } catch {}
  const day = t => { const d = new Date(t); return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`; };
  const work = path.join(REPO, 'icon_set/work', WORK_NAME);
  const {readdirSync} = await import('node:fs');
  for (const id of readdirSync(work).sort()) {
    const dir = path.join(work, id), file = path.join(dir, 'review.json');
    if (!existsSync(file)) continue;
    let r; try { r = JSON.parse(readFileSync(file, 'utf8')); } catch { continue; }
    if (since && !(r.reviewed_at && day(r.reviewed_at) >= since)) continue;
    // Judge the boxes the review recorded (after for a fix, before for ok / redraw), not layout.json: a later preview
    // that was never recorded (a batch stopped mid-pair) can leave layout.json on the system while the review is not.
    const rec = r.verdict === 'fix' ? r.after : ['ok', 'redraw'].includes(r.verdict) ? r.before : null;
    if (!rec?.main) continue;
    if (olderThan && r.reviewed_at < olderThan && ['fix', 'redraw'].includes(r.verdict) && !r.keep_stored
        && !['fix-good', 'stored-better', 'sub-too-small'].includes(userFlags[id]?.kind)) { console.log(id); continue; }
    // A redraw recorded under the keyshape gate (before.keyshape) already decided that no preset layout works.
    if (r.verdict === 'redraw' && r.before?.keyshape) continue;
    const groups = b => b ? [{x: b[0], y: b[1], w: b[2], h: b[3]}] : [];
    if (!keyshapeCheck(dir, {position: rec.position, main: groups(rec.main), sub: groups(rec.sub)}).ok) { console.log(id); continue; }
    // Layout first, resize last: a fix that shrank the sub with no recorded reason (--sub-smaller), or by more than one
    // step / below 28, is reviewed again.
    if (r.verdict === 'fix' && !noSub) {
      const size = k => Number(String(k || '').match(/ at (\d+)$/)?.[1]) || null;
      const from = size(r.before?.keyshape?.sub), to = size(r.after?.keyshape?.sub);
      if (from && to && to < from && (!r.sub_smaller || to < Math.min(ROLES.sub.base - 4, from) || from - to > 4)) console.log(id);
    }
  }
  process.exit(0);
}
// --list main|sub [--position P]: the allowed boxes, one per line, for preview --main / --sub.
if (list) {
  for (const dir of args) {
    const layout = JSON.parse(readFileSync(path.join(dir, current ? 'base-layout.json' : 'layout.json'), 'utf8'));
    const position = opt('--position') || layout.position;
    console.log(`${path.basename(dir)} ${list} at ${position}:`);
    for (const a of presetBoxes(dir, list, position)) console.log(`  ${a.box.padEnd(14)} ${a.name} at ${a.size}`);
  }
  process.exit(0);
}
let failed = 0;
const results = [];
for (const dir of args) {
  const layoutFile = path.join(dir, current ? 'base-layout.json' : 'layout.json');
  if (!existsSync(layoutFile)) { console.log(`${dir}: no ${path.basename(layoutFile)}`); failed++; continue; }
  const res = {dir, layout: current ? 'stored' : 'proposed', ...keyshapeCheck(dir, JSON.parse(readFileSync(layoutFile, 'utf8')), only ? [only] : ['main', 'sub'])};
  if (!res.ok) failed++;
  results.push(res);
  if (!asJson) {
    const parts = Object.entries(res.roles).map(([role, r]) => r.ok ? `${role} ${r.preset || r.note}` : `${role} OFF ${r.box}`);
    console.log(`${res.ok ? 'PASS' : 'FAIL'} ${path.basename(dir)} ${res.position} (${res.layout}): ${parts.join('; ')}`);
    if (fit) for (const [role, r] of Object.entries(res.roles)) if (!r.ok) console.log(`     ${role} nearest: ${r.nearest.join(' | ')}`);
  }
}
if (asJson) console.log(JSON.stringify(results, null, 2));
process.exit(failed ? 1 : 0);
}
