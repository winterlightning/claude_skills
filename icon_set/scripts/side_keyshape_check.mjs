#!/usr/bin/env node
// Is a side pair on the keyshape system? Two rules (canvas keyshape rule since 2026-10-12):
// 1. Each part stays on its own contract keyshape (SOLO48 for the main, SUB32 for the sub at 64; the keyshape whose
//    w - h matches the drawing, since another one stretches it) or its own drawn box scaled evenly, grown or shrunk by
//    the same amount on both axes in steps of 4 (main 32-64, sub 20-44).
// 2. The combined icon sits in one keyshape of the canvas (combine-side.js CANVAS_KEYSHAPES; 64: SQUARE 56, HRECT
//    60x48, HRECT_M 60x44, VRECT 48x60, VRECT_M 44x60). The sub is anchored at its position's corner or side of that
//    canvas keyshape, the main at the opposite one; the main may move by whole units at a preset size, inside it.
//    A pair that fills its canvas keyshape exactly passes even with a part at an in-between size (user, 2026-10-12).
// A layout that stretches a part, or spreads main + sub past every canvas keyshape, is never accepted.
//
//   node icon_set/scripts/side_keyshape_check.mjs <dir> [<dir> ...]   proposed layout (layout.json)
//         --current      the stored layout (base-layout.json)
//         --role main    check one role only (default: main and sub)
//         --json         details
//         --recheck [--since YYYY-MM-DD]   list reviewed pairs whose review breaks the system (no dirs)
//         --fit          print the nearest allowed boxes for a part that is off the system
//         --list main|sub [--position P] [--frame SQUARE|HRECT|HRECT_M|VRECT|VRECT_M]   every allowed box (x,y,w,h for
//                        side_layout.mjs preview --main / --sub), per canvas keyshape (all of them by default)
//
// Exits 1 if any folder fails.
import {existsSync, readFileSync} from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {SIZE, Side, WORK_NAME} from './side_compose.mjs';

const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const CANVAS = SIZE, PADDING = 2;
// The canvas keyshapes (painted boxes), as the engine reports them for a built pair: the frames the parts sit in.
export const FRAMES = Object.entries(Side.CANVAS_KEYSHAPES[SIZE]).map(([name, box]) => ({name, box}));
const EPS = 0.05;
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

// Every allowed centerline box [x0, y0, x1, y1] of a role, with its name, size and canvas keyshape: the part's keyshape
// at each preset size, anchored in `frame` (a canvas keyshape's painted box) at its position (the main opposite the sub).
function allowedIn(role, position, own, frame) {
  const [px, py] = ANCHORS[position] || [1, 1], [ax, ay] = role === 'main' ? [1 - px, 1 - py] : [px, py];
  const {base, sizes} = ROLES[role], out = [];
  const [fx0, fy0, fx1, fy1] = frame.box, fw = fx1 - fx0, fh = fy1 - fy0;
  const onShape = own && SHAPES[role].some(([, ...b]) => b.every((v, i) => Math.abs(v - own[i]) < .05));
  const place = (w, h, name, size) => {
    if (w < 4 || h < 4 || w + 4 > fw + EPS || h + 4 > fh + EPS) return;
    const x = Math.round(fx0 + (fw - w - 4) * ax) + 2, y = Math.round(fy0 + (fh - h - 4) * ay) + 2;
    out.push({name, size, frame: frame.name, box: [x, y, x + w, y + h]});
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
  // drawing keeps its offset inside it. That placement, anchored in the frame, is on the system too, at the base size.
  if (SIZE === 72 && own && base <= Math.min(fw, fh) + EPS) {
    const cx = Math.round(fx0 + (fw - base) * ax), cy = Math.round(fy0 + (fh - base) * ay);
    out.push({name: 'as drawn', size: base, frame: frame.name, box: [cx + own[0], cy + own[1], cx + own[2], cy + own[3]].map(v => Math.round(v))});
  }
  return out;
}
const allowed = (role, position, own, frameName = null) =>
  FRAMES.filter(f => !frameName || f.name === frameName).flatMap(f => allowedIn(role, position, own, f));

// The canvas keyshape the combined painted box (centerline boxes + 2) sits in: of those that hold it, the shape closest
// to the pair's own, then the smaller one (as combine-side.js canvasKeyshape). null when none holds it.
export function canvasFrame(boxes) {
  const u = union(boxes.map(b => [b[0] - 2, b[1] - 2, b[2] + 2, b[3] + 2]));
  const aspect = Math.log((u[2] - u[0]) / (u[3] - u[1]));
  const fits = FRAMES.filter(f => u[0] >= f.box[0] - EPS && u[1] >= f.box[1] - EPS && u[2] <= f.box[2] + EPS && u[3] <= f.box[3] + EPS)
    .map(f => ({...f, off: Math.abs(aspect - Math.log((f.box[2] - f.box[0]) / (f.box[3] - f.box[1]))), area: (f.box[2] - f.box[0]) * (f.box[3] - f.box[1])}))
    .sort((a, b) => a.off - b.off || a.area - b.area);
  return fits.length ? {name: fits[0].name, box: fits[0].box, union: u} : {name: null, box: null, union: u};
}

const same = (a, b) => a.every((v, i) => Math.abs(v - b[i]) < 1e-6);
const dist = (a, b) => Math.max(...a.map((v, i) => Math.abs(v - b[i])));
const fmt = b => `${b[0]},${b[1]},${b[2] - b[0]},${b[3] - b[1]}`;

// Check one layout ({position, main: groups, sub: groups}) of the work folder `dir` against the keyshape system.
// Returns {ok, position, canvas: {ok, keyshape | problem}, roles: {main|sub: {ok, box, preset | problem + nearest}}}.
export function keyshapeCheck(dir, layout, roles = ['main', 'sub']) {
  const elements = existsSync(path.join(dir, 'elements.json')) ? JSON.parse(readFileSync(path.join(dir, 'elements.json'), 'utf8')) : {};
  let item = {};
  try { item = JSON.parse(readFileSync(path.join(dir, 'item.json'), 'utf8')); } catch {}
  const nativeText = (item.parts || []).some(p => p.role === 'sub' && p.form?.native_text) || item.native_text;
  const res = {position: layout.position, roles: {}, ok: true};
  const boxes = {};
  for (const role of ['main', 'sub']) {
    const groups = layout[role] || [];
    if (groups.length) boxes[role] = union(groups.map(g => [g.x, g.y, g.x + g.w, g.y + g.h]));
  }
  // Native text has explicit element groups too: its painted bounds must fit the same canvas frame.
  const frame = boxes.main && boxes.sub ? canvasFrame([boxes.main, boxes.sub]) : null;
  if (frame) {
    const [x0, y0, x1, y1] = frame.union;
    res.canvas = frame.name ? {ok: true, keyshape: frame.name}
      : {ok: false, problem: `main + sub span ${fmt([x0, y0, x1, y1])} (painted): no canvas keyshape holds them (${FRAMES.map(f => `${f.name} ${fmt(f.box)}`).join(', ')})`};
    if (!frame.name) res.ok = false;
  }
  for (const role of roles) {
    if (!boxes[role]) continue;
    if (role === 'sub' && nativeText) {
      const presets = presetBoxes(dir, role, layout.position);
      const hit = presets.find(p => {
        const [x, y, w, h] = p.box.split(',').map(Number);
        return dist(boxes.sub, [x, y, x + w, y + h]) < EPS;
      });
      res.roles.sub = hit ? {ok: true, box: fmt(boxes.sub), preset: 'native text at 32', frame: hit.frame}
        : {ok: false, problem: 'native text must retain its glyph size and anchor in the canvas keyshape', nearest: presets.map(p => p.box)};
      if (!hit) res.ok = false;
      continue;
    }
    const box = boxes[role];
    const sources = (elements[role] || []).map(e => e.source).filter(Array.isArray);
    const own = sources.length ? union(sources) : null;
    const list = allowed(role, layout.position, own);
    // Several presets can give the same box (a circle at 44 = a square at 48): name it after the part's own keyshape,
    // and prefer the canvas keyshape the pair sits in.
    const ownName = own && SHAPES[role].find(([, ...b]) => b.every((v, i) => Math.abs(v - own[i]) < .05))?.[0];
    const hits = list.filter(a => same(a.box, box)).sort((a, b) => (b.frame === frame?.name) - (a.frame === frame?.name));
    let hit = hits.find(a => a.name === ownName) || hits.find(a => a.size === ROLES[role].base) || hits[0];
    // The main may move (user rule 2026-10-12): a preset box of its own keyshape (same w, h), shifted by whole units,
    // inside the canvas keyshape the pair sits in (rule 2 checks that).
    let moved = false;
    if (!hit && role === 'main' && box.every(v => Math.abs(v - Math.round(v)) < 1e-6)) {
      const w = box[2] - box[0], h = box[3] - box[1];
      hit = list.find(a => a.name === ownName && Math.abs(a.box[2] - a.box[0] - w) < 1e-6 && Math.abs(a.box[3] - a.box[1] - h) < 1e-6)
        || list.find(a => Math.abs(a.box[2] - a.box[0] - w) < 1e-6 && Math.abs(a.box[3] - a.box[1] - h) < 1e-6);
      moved = !!hit;
    }
    // A pair that fills its canvas keyshape exactly (centred in it, user decision 2026-10-12) is on the system even when
    // a part sits at an in-between size: the part keeps its own keyshape (named after the nearest preset).
    let fills = false;
    if (!hit && frame?.name && frame.union.every((v, i) => Math.abs(v - frame.box[i]) <= 0.5)) {
      const near = list.filter(a => a.name !== 'as drawn').map(a => ({...a, d: dist(a.box, box)})).sort((a, b) => a.d - b.d)[0];
      if (near) { hit = near; fills = true; }
    }
    const r = {box: fmt(box), ok: !!hit};
    if (hit) r.preset = fills ? `${hit.name} (in-between size, the pair fills ${frame.name})` : `${hit.name} at ${hit.size}`,
      r.frame = moved || fills ? frame?.name || null : hit.frame, moved && (r.moved = true), fills && (r.fills = true);
    else {
      r.problem = `the ${role} box ${fmt(box)} is not a keyshape preset at ${layout.position}`;
      r.nearest = list.map(a => ({...a, d: dist(a.box, box)})).sort((a, b) => a.d - b.d).slice(0, 4)
        .map(a => `${a.name} at ${a.size} in ${a.frame}: ${fmt(a.box)}`);
      res.ok = false;
    }
    res.roles[role] = r;
  }
  return res;
}

// Move a layout's parts into a canvas keyshape by whole units, as side_keyshape_snap.mjs does (sizes never change):
// main + sub that fit one together move as one piece, centred (the shape closest to theirs, then the smaller one);
// otherwise each part moves just enough to get inside the keyshape needing the least total move. Returns the layout
// (unchanged when no keyshape can take both parts at their size).
export function intoCanvasKeyshape(layout) {
  const groupsBox = groups => union(groups.map(g => [g.x, g.y, g.x + g.w, g.y + g.h]));
  const b = {main: groupsBox(layout.main), sub: groupsBox(layout.sub)};
  const painted = r => [b[r][0] - 2, b[r][1] - 2, b[r][2] + 2, b[r][3] + 2];
  const u = union([painted('main'), painted('sub')]), aspect = Math.log((u[2] - u[0]) / (u[3] - u[1]));
  const off = f => Math.abs(aspect - Math.log((f.box[2] - f.box[0]) / (f.box[3] - f.box[1])));
  const range = (a0, a1, k0, k1) => { const lo = Math.ceil(k0 - a0 - EPS), hi = Math.floor(k1 - a1 + EPS);
    return lo <= hi ? Math.min(hi, Math.max(lo, Math.round((k0 + k1 - a0 - a1) / 2))) : null; };
  const clamp = (a0, a1, k0, k1) => a1 - a0 > k1 - k0 + EPS ? null : a0 < k0 - EPS ? Math.ceil(k0 - a0 - EPS) : a1 > k1 + EPS ? -Math.ceil(a1 - k1 - EPS) : 0;
  const together = [], apart = [];
  for (const f of FRAMES) {
    const [k0, k1, k2, k3] = f.box, tx = range(u[0], u[2], k0, k2), ty = range(u[1], u[3], k1, k3);
    if (tx !== null && ty !== null) { together.push({f, main: [tx, ty], sub: [tx, ty], cost: Math.abs(tx) + Math.abs(ty)}); continue; }
    const m = [clamp(painted('main')[0], painted('main')[2], k0, k2), clamp(painted('main')[1], painted('main')[3], k1, k3)];
    const s2 = [clamp(painted('sub')[0], painted('sub')[2], k0, k2), clamp(painted('sub')[1], painted('sub')[3], k1, k3)];
    if ([...m, ...s2].some(v => v === null)) continue;
    apart.push({f, main: m, sub: s2, cost: Math.abs(m[0]) + Math.abs(m[1]) + Math.abs(s2[0]) + Math.abs(s2[1])});
  }
  together.sort((a, c) => off(a.f) - off(c.f) || (a.f.box[2] - a.f.box[0]) * (a.f.box[3] - a.f.box[1]) - (c.f.box[2] - c.f.box[0]) * (c.f.box[3] - c.f.box[1]) || a.cost - c.cost);
  apart.sort((a, c) => a.cost - c.cost || off(a.f) - off(c.f));
  const pick = together[0] || apart[0];
  if (!pick) return layout;
  const shift = (groups, [dx, dy]) => groups.map(g => ({...g, x: Math.round(g.x) + dx, y: Math.round(g.y) + dy,
    w: g.w > 0 ? Math.round(g.x + g.w) - Math.round(g.x) : 0, h: g.h > 0 ? Math.round(g.y + g.h) - Math.round(g.y) : 0}));
  return {...layout, main: shift(layout.main, pick.main), sub: shift(layout.sub, pick.sub)};
}

// Every allowed box of a role in the work folder `dir` at `position`, for preview --main / --sub (x,y,w,h), in every
// canvas keyshape (or only `frameName`).
export function presetBoxes(dir, role, position, frameName = null) {
  const elements = existsSync(path.join(dir, 'elements.json')) ? JSON.parse(readFileSync(path.join(dir, 'elements.json'), 'utf8')) : {};
  const sources = (elements[role] || []).map(e => e.source).filter(Array.isArray);
  const own = sources.length ? union(sources) : null, seen = new Set();
  const item = JSON.parse(readFileSync(path.join(dir, 'item.json'), 'utf8'));
  if (role === 'sub' && item.parts?.some(p => p.role === 'sub' && p.form?.native_text) && own) {
    const [ax, ay] = ANCHORS[position] || [1, 1];
    const w = own[2] - own[0], h = own[3] - own[1];
    return FRAMES.filter(f => !frameName || f.name === frameName).filter(f => w + 4 <= f.box[2] - f.box[0] + EPS && h + 4 <= f.box[3] - f.box[1] + EPS)
      .map(f => ({name: 'native text', size: 32, frame: f.name, box: [
        Math.round(f.box[0] + (f.box[2] - f.box[0] - w - 4) * ax) + 2,
        Math.round(f.box[1] + (f.box[3] - f.box[1] - h - 4) * ay) + 2,
        Math.round(w), Math.round(h)].join(',')}));
  }

  const ownName = own && SHAPES[role].find(([, ...b]) => b.every((v, i) => Math.abs(v - own[i]) < .05))?.[0];
  // One entry per box and canvas keyshape, named after the own keyshape when several presets give it.
  return allowed(role, position, own, frameName).sort((a, b) => (b.name === ownName) - (a.name === ownName))
    .filter(a => !seen.has(a.frame + a.box.join()) && seen.add(a.frame + a.box.join()))
    .sort((a, b) => FRAMES.findIndex(f => f.name === a.frame) - FRAMES.findIndex(f => f.name === b.frame) || a.size - b.size || a.name.localeCompare(b.name))
    .map(a => ({name: a.name, size: a.size, frame: a.frame, box: fmt(a.box)}));
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
    const position = opt('--position') || layout.position, frameName = opt('--frame');
    console.log(`${path.basename(dir)} ${list} at ${position}${frameName ? ' in ' + frameName : ''} (x,y,w,h · keyshape at size · canvas keyshape):`);
    for (const a of presetBoxes(dir, list, position, frameName)) console.log(`  ${a.box.padEnd(14)} ${a.name} at ${a.size}`.padEnd(40) + ` in ${a.frame}`);
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
    const parts = Object.entries(res.roles).map(([role, r]) => r.ok ? `${role} ${r.preset || r.note}${r.moved ? ' (moved)' : ''}` : `${role} OFF ${r.box}`);
    const canvas = res.canvas ? (res.canvas.ok ? `canvas ${res.canvas.keyshape}` : `canvas OFF`) : 'canvas -';
    console.log(`${res.ok ? 'PASS' : 'FAIL'} ${path.basename(dir)} ${res.position} (${res.layout}): ${canvas}; ${parts.join('; ')}`);
    if (res.canvas && !res.canvas.ok) console.log(`     ${res.canvas.problem}`);
    if (fit) for (const [role, r] of Object.entries(res.roles)) if (!r.ok) console.log(`     ${role} nearest: ${r.nearest.join(' | ')}`);
  }
}
if (asJson) console.log(JSON.stringify(results, null, 2));
process.exit(failed ? 1 : 0);
}
