#!/usr/bin/env node
// Snap every side pair's stored layout to the nearest keyshape of its canvas, locally (nothing goes to production).
//
//   node icon_set/scripts/side_keyshape_snap.mjs [--ids a,b,...] [--limit N] [--jobs 8] [--refresh] [--force]
//   SIDE_SIZE=72 node icon_set/scripts/side_keyshape_snap.mjs ...                       (the 72 set)
//
// The combined icon (main + sub together) must sit in one keyshape of the canvas (combine-side.js CANVAS_KEYSHAPES):
//   64 (CONTAINER64): SQUARE 56, HRECT 60x48, HRECT_M 60x44, VRECT 48x60, VRECT_M 44x60
//   72 (same rule: square padding 4, HRECT short side 0.75 x canvas, M = HRECT - 4): SQUARE 64, HRECT 68x54,
//       HRECT_M 68x50, VRECT 54x68, VRECT_M 50x68
// The circle is left out: its box is the whole padded canvas. Parts are measured by their real ink (the engine's
// painted boxes). When main + sub together fit a keyshape they move as one piece, centered, by whole units (the shape
// closest to the pair's, then the smaller one). Otherwise each part moves on its own, by whole units, just enough to get
// inside (least total move). A part larger than every keyshape is shrunk evenly, as little as possible. The keyshape
// recorded is the one the engine reports for the snapped pair, the same one a build stores.
// The snapped pair is composed with the page's engine and checked (side_contact_check + side_overlap flags).
//
// Writes icon_set/work/side-keyshape-snap/<64|72>/:
//   cache/items.json, cache/drawings.json   the pairs and their drawings (downloaded once; --refresh downloads again)
//   pairs/<id>/   the side_layout.mjs work folder (base-layout.json = stored, layout.json = snapped), before@4x.png /
//                 after@4x.png with the keyshape outline, snap.json
//   summary.json, all.tsv, report.html
// Classes: already-fits (no move) · snapped-ok · snapped-flagged (the move added a contact failure or a flag) · no-fit
// (no keyshape holds both parts at their size; stored layout kept) · error.
import {spawn, execFileSync} from 'node:child_process';
import {existsSync, mkdirSync, readFileSync, rmSync, writeFileSync} from 'node:fs';
import path from 'node:path';
import {api, query, savePair} from './side_layout.mjs';
import {SIZE, compose, layoutFor, Side} from './side_compose.mjs';
import {analyze} from './side_overlap.mjs';
import {checkDir} from './side_contact_check.mjs';

const HERE = path.dirname(new URL(import.meta.url).pathname);
const OUT = path.resolve(HERE, '../work/side-keyshape-snap', String(SIZE));
const PAGE = 500, KEYS = 100, RES = 8;
const API = (process.env.PICTOGRAPHIC_API || 'https://pictographic-review-next.pictographic.workers.dev').replace(/\/$/, '');
const readJSON = file => JSON.parse(readFileSync(file, 'utf8'));
const writeJSON = (file, data) => writeFileSync(file, JSON.stringify(data, null, 2) + '\n');
const r2 = v => Math.round(v * 100) / 100;

// The canvas keyshapes as the engine has them (combine-side.js CANVAS_KEYSHAPES: painted boxes, centered, no circle),
// so what the snap aims for is what the engine reports when the pair is built.
export const KEYSHAPES = Side.CANVAS_KEYSHAPES[SIZE];

// A role's painted box from its groups (centerline boxes; the 4-unit stroke adds 2 on each side).
function painted(groups) {
  const b = Side.groupsBox(groups);
  return [b.x - 2, b.y - 2, b.x + b.w + 2, b.y + b.h + 2];
}
// The whole-unit shift that brings `box` inside `k` (null when it cannot fit). Overflow rounds up so the moved box is
// fully inside even when the stored box sits on a fraction.
function shift(box, k) {
  const axis = (a0, a1, k0, k1) => {
    if (a1 - a0 > k1 - k0 + 0.05) return null;
    if (a0 < k0 - 0.05) return Math.ceil(k0 - a0 - 0.05);
    if (a1 > k1 + 0.05) return -Math.ceil(a1 - k1 - 0.05);
    return 0;
  };
  const dx = axis(box[0], box[2], k[0], k[2]), dy = axis(box[1], box[3], k[1], k[3]);
  return dx === null || dy === null ? null : [dx, dy];
}
const moved = (groups, [dx, dy]) => groups.map(g => ({...g, x: g.x + dx, y: g.y + dy}));
// The engine takes an edited part only on whole units: a part placed automatically on a fraction (most 72 parts) has
// its group edges rounded first, as the layout editor does on a part's first edit (under a unit, not a resize).
const whole = groups => groups.map(g => {
  const x0 = Math.round(g.x), y0 = Math.round(g.y), x1 = Math.round(g.x + g.w), y1 = Math.round(g.y + g.h);
  return {...g, x: x0, y: y0, w: g.w > 0 ? x1 - x0 : 0, h: g.h > 0 ? y1 - y0 : 0};
});
const fractional = groups => groups.some(g => [g.x, g.y, g.w, g.h].some(v => Math.abs(v - Math.round(v)) > 1e-9));
// Every ink pixel (cut main + sub) inside the circle, give or take a quarter unit.
function inCircle(analysis, k) {
  const {n, kept, sub} = analysis.masks, cx = (k[0] + k[2]) / 2 * RES, cy = (k[1] + k[3]) / 2 * RES;
  const R = ((k[2] - k[0]) / 2 + 0.25) * RES, R2 = R * R;
  for (let i = 0; i < kept.length; i++) {
    if (!kept[i] && !sub[i]) continue;
    const x = i % n + 0.5, y = (i - (i % n)) / n + 0.5;
    if ((x - cx) ** 2 + (y - cy) ** 2 > R2) return false;
  }
  return true;
}

// The keyshape outline over a combined SVG, as a 4x PNG.
function outlined(svg, k, name, file) {
  const c = SIZE, inner = svg.replace(/<\?xml[^>]*>/, '').replace(/<svg\b[^>]*>/, tag =>
    tag.replace(/\s(width|height|x|y)="[^"]*"/g, '').replace(/<svg\b/, `<svg x="0" y="0" width="${c}" height="${c}"`));
  const shape = name === 'CIRCLE'
    ? `<circle cx="${(k[0] + k[2]) / 2}" cy="${(k[1] + k[3]) / 2}" r="${(k[2] - k[0]) / 2}"`
    : `<rect x="${k[0]}" y="${k[1]}" width="${k[2] - k[0]}" height="${k[3] - k[1]}"`;
  const out = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${c} ${c}" width="${c * 4}" height="${c * 4}">
<rect width="${c}" height="${c}" fill="#fff"/>${inner}
${shape} fill="none" stroke="#e5484d" stroke-width="0.4" stroke-dasharray="1.2 0.8"/></svg>`;
  const tmp = file.replace(/\.png$/, '.svg');
  writeFileSync(tmp, out);
  try { execFileSync('rsvg-convert', ['-o', file, tmp], {timeout: 30000}); } catch { /* picture is a convenience */ }
  rmSync(tmp, {force: true});
}

// Snap one pair whose work folder was just written by savePair.
function snapDir(dir) {
  const base = readJSON(path.join(dir, 'base-layout.json'));
  const item = readJSON(path.join(dir, 'item.json'));
  const nativeText = !!item.parts.find(p => p.role === 'sub')?.form?.native_text;
  const stored = {position: base.position, main: base.main, sub: base.sub};
  const storedComposed = compose(dir, stored);
  // The groups the snap moves: the stored ones, on whole units.
  const grid = {main: whole(base.main), sub: whole(base.sub)};
  const rounded = {main: fractional(base.main), sub: fractional(base.sub)};
  // Each part's painted box as the engine measures it (its real ink: a stroke end can reach past the group box, and a
  // native-text sub's groups are not its ink at all).
  const inkBox = (composed, i) => { const b = composed.result.placements[i].painted_box; return [b.x, b.y, b.x + b.w, b.y + b.h]; };
  const box = {main: inkBox(storedComposed, 0), sub: inkBox(storedComposed, 1)};
  // When rounding to whole units moved a fractional part, measure that too: the shift starts from the rounded part.
  for (const [i, role] of [[0, 'main'], [1, 'sub']]) {
    if (!rounded[role]) continue;
    const off = painted(grid[role]).map((v, j) => v - painted(base[role])[j]);
    box[role] = box[role].map((v, j) => v + off[j]);
  }
  const union = [Math.min(box.main[0], box.sub[0]), Math.min(box.main[1], box.sub[1]), Math.max(box.main[2], box.sub[2]), Math.max(box.main[3], box.sub[3])];
  const aspect = Math.log((union[2] - union[0]) / (union[3] - union[1]));
  const aspectOff = k => Math.abs(aspect - Math.log((k[2] - k[0]) / (k[3] - k[1])));
  // 1. The pair as one piece: when its union fits a keyshape, main and sub move together (same shift, the layout
  //    between them untouched) to sit centered in it. Among the keyshapes that hold it: the shape closest to the pair's
  //    own (a 60x48 pair takes HRECT, not SQUARE), then the smaller one (least empty space), then the least move.
  // 2. Only when no keyshape holds the union: each part moves on its own just enough to get inside (they come closer).
  const area = k => (k[2] - k[0]) * (k[3] - k[1]);
  const candidates = Object.entries(KEYSHAPES).map(([name, k]) => {
    // Whole-unit shifts that keep the union inside, the one nearest the centre.
    const range = (a0, a1, k0, k1) => { const lo = Math.ceil(k0 - a0 - 0.05), hi = Math.floor(k1 - a1 + 0.05);
      return lo <= hi ? Math.min(hi, Math.max(lo, Math.round((k0 + k1 - a0 - a1) / 2))) : null; };
    const tx = range(union[0], union[2], k[0], k[2]), ty = range(union[1], union[3], k[1], k[3]);
    if (tx !== null && ty !== null) {
      const d = [tx, ty];
      return {name, k, possible: true, together: true, main: d, sub: d, cost: Math.abs(d[0]) + Math.abs(d[1]), aspect: aspectOff(k)};
    }
    const m = shift(box.main, k), s = shift(box.sub, k);
    if (!m || !s) return {name, k, possible: false};
    return {name, k, possible: true, together: false, main: m, sub: s, cost: Math.abs(m[0]) + Math.abs(m[1]) + Math.abs(s[0]) + Math.abs(s[1]), aspect: aspectOff(k)};
  });
  const together = candidates.filter(c => c.possible && c.together).sort((a, b) => a.aspect - b.aspect || area(a.k) - area(b.k) || a.cost - b.cost);
  const apart = candidates.filter(c => c.possible && !c.together).sort((a, b) => a.cost - b.cost || a.aspect - b.aspect);
  const order = [...together, ...apart];
  const beforeCheck = checkDir(dir, {current: true});
  const beforeFlags = analyze(storedComposed, layoutFor(dir, stored)).flags;
  const size = b => `${r2(b[2] - b[0])}x${r2(b[3] - b[1])}`;
  const result = {reference_id: path.basename(dir), size: SIZE, position: base.position, hand: base.hand, rounded_to_grid: rounded,
                  stored: {main: box.main, sub: box.sub, union}, before: {contact: beforeCheck.verdict, flags: beforeFlags},
                  candidates: candidates.map(c => ({name: c.name, possible: c.possible, together: c.together ?? null, cost: c.cost ?? null, main_move: c.main ?? null, sub_move: c.sub ?? null}))};
  let pick = null, analysis = null, layout = null, shrunk = null;
  const tryLayout = (c, trial) => {
    // A moved part can be drawn a little larger than measured (a sun's rays past its box once its layout is explicit):
    // measure the composed pair and shift a part again by whatever still sticks out, a few rounds at most.
    let composed = compose(dir, trial);
    for (let round = 0; round < 3; round++) {
      let again = false;
      const next = {...trial};
      composed.result.placements.forEach((p, i) => {
        const role = i ? 'sub' : 'main', b = [p.painted_box.x, p.painted_box.y, p.painted_box.x + p.painted_box.w, p.painted_box.y + p.painted_box.h];
        const d = shift(b, c.k);
        if (d && (d[0] || d[1])) { next[role] = moved(trial[role] === stored[role] ? grid[role] : trial[role], d); again = true; }
      });
      if (!again) break;
      trial = next; composed = compose(dir, trial);
    }
    const a = analyze(composed, layoutFor(dir, trial));
    if (c.name === 'CIRCLE' && !inCircle(a, c.k)) return false;
    pick = c; analysis = a; layout = trial; return true;
  };
  for (const c of order) {
    // A part that needs no move stays exactly as stored (fraction and all).
    const place = role => c[role][0] || c[role][1] ? moved(grid[role], c[role]) : stored[role];
    if (tryLayout(c, {position: base.position, main: place('main'), sub: place('sub')})) break;
  }
  // Too big to move in: a part is larger than every keyshape (a main grown to fill the canvas). Shrink only that part,
  // evenly and as little as possible, to the largest whole-unit box the keyshape takes, then move as usual.
  if (!pick) {
    const fallback = Object.entries(KEYSHAPES).filter(([name]) => name !== 'CIRCLE').map(([name, k]) => {
      const kw = k[2] - k[0], kh = k[3] - k[1], out = {name, k, groups: {}, boxes: {}, scale: 1};
      for (const role of ['main', 'sub']) {
        const b = box[role], w = b[2] - b[0], h = b[3] - b[1];
        if (w <= kw + 1e-6 && h <= kh + 1e-6) { out.groups[role] = grid[role]; out.boxes[role] = b; continue; }
        if (role === 'sub' && nativeText) return null;
        // Painted size w,h -> centerline (w-4, h-4) scaled evenly so the painted box fits.
        const f = Math.min((kw - 4) / (w - 4), (kh - 4) / (h - 4));
        const cw = Math.floor((w - 4) * f), ch = Math.floor((h - 4) * f), cb = Side.groupsBox(grid[role]);
        const target = {x: Math.round(cb.x + (cb.w - cw) / 2), y: Math.round(cb.y + (cb.h - ch) / 2), w: cw, h: ch};
        out.groups[role] = whole(Side.mapGroups(grid[role], cb, target));
        out.boxes[role] = painted(out.groups[role]);
        out.scale = Math.min(out.scale, f);
        out.shrunk = {...(out.shrunk || {}), [role]: {from: size(b), to: size(out.boxes[role])}};
      }
      const m = shift(out.boxes.main, k), s = shift(out.boxes.sub, k);
      if (!m || !s) return null;
      return {...out, main: m, sub: s, cost: Math.abs(m[0]) + Math.abs(m[1]) + Math.abs(s[0]) + Math.abs(s[1]), aspect: aspectOff(k)};
    }).filter(Boolean).sort((a, b) => b.scale - a.scale || a.cost - b.cost || a.aspect - b.aspect);
    for (const c of fallback) {
      if (tryLayout(c, {position: base.position, main: moved(c.groups.main, c.main), sub: moved(c.groups.sub, c.sub)})) { shrunk = c.shrunk; break; }
    }
  }
  const beforeSvg = storedComposed.svg;
  if (!pick) {
    writeJSON(path.join(dir, 'layout.json'), stored);
    outlined(beforeSvg, KEYSHAPES.SQUARE, 'SQUARE', path.join(dir, 'before@4x.png'));
    Object.assign(result, {class: 'no-fit', keyshape: null,
      reason: `no keyshape holds the main ${size(box.main)} and the sub ${size(box.sub)}${nativeText ? ' (native text keeps its size and cannot shrink)' : ''}` +
        (['main', 'sub'].some(r => box[r][2] - box[r][0] > SIZE || box[r][3] - box[r][1] > SIZE) ? `; the stored pair already runs off the ${SIZE} canvas` : '')});
    writeJSON(path.join(dir, 'snap.json'), result);
    return result;
  }
  writeJSON(path.join(dir, 'layout.json'), layout);
  // The keyshape the engine reports for the snapped pair (what a build stores) is the answer.
  const reached = Side.canvasKeyshape(compose(dir, layout).result.placements, SIZE);
  if (reached) pick = {...pick, name: reached.name, k: reached.bounds};
  const after = checkDir(dir);
  const newFlags = analysis.flags.filter(f => !beforeFlags.includes(f));
  const worse = (after.verdict === 'fail' && beforeCheck.verdict !== 'fail') || newFlags.length > 0;
  outlined(beforeSvg, pick.k, pick.name, path.join(dir, 'before@4x.png'));
  outlined(compose(dir, layout).svg, pick.k, pick.name, path.join(dir, 'after@4x.png'));
  const pb = (groups) => painted(groups).map(r2);
  Object.assign(result, {
    class: !reached ? 'snapped-flagged' : pick.cost === 0 && !shrunk ? 'already-fits' : worse ? 'snapped-flagged' : 'snapped-ok',
    ...(reached ? {} : {reason: 'the engine finds no keyshape for the snapped pair'}),
    keyshape: pick.name, keyshape_box: pick.k, move: {main: pick.main, sub: pick.sub, total: pick.cost, together: !!pick.together},
    ...(shrunk ? {shrunk, reason: Object.entries(shrunk).map(([role, v]) => `${role} ${v.from} is larger than every keyshape; shrunk to ${v.to} to fit ${pick.name}`).join('; ')} : {}),
    snapped: {main: pb(layout.main), sub: pb(layout.sub)},
    after: {contact: after.verdict, problems: after.problems || [], flags: analysis.flags, new_flags: newFlags}});
  writeJSON(path.join(dir, 'snap.json'), result);
  return result;
}

// What is wrong with a part's latest drawing, in a few plain words.
function latestProblem(item, drawings, message) {
  const m = String(message), out = [];
  for (const p of item.parts) {
    if (!p.icon) continue;
    if (!drawings[p.icon]) out.push(`${p.role} ${p.icon}: deleted on production`);
    else if (p.built_sha && p.current_sha && p.built_sha !== p.current_sha) {
      const what = /viewBox/.test(m) ? 'redrawn, new file has a wrong viewBox'
        : /arc start equals end/.test(m) ? 'redrawn, new file has a broken arc'
        : /placed exactly once|at least one unit/.test(m) ? 'redrawn, no longer matches the stored hand layout'
        : 'redrawn, new drawing does not build';
      out.push(`${p.role} ${p.icon}: ${what}`);
    }
  }
  return out.length ? out.join('; ') : m;
}

// ---- worker: one job file of pairs ----
async function work(jobFile) {
  for (const {id, dir, item, drawings} of readJSON(jobFile)) {
    try {
      rmSync(dir, {recursive: true, force: true});
      savePair(dir, item, drawings, null);
      const r = snapDir(dir);
      const from = item.parts.filter(p => p.swapped_from);
      if (from.length) {
        Object.assign(r, {swapped: from.map(p => ({role: p.role, from: p.swapped_from, to: p.icon})),
          reason: `Re-picked ${from.map(p => `${p.role} ${p.swapped_from} → ${p.icon}`).join(', ')} (the build refuses the old one: deleted or of the wrong family)`});
        writeJSON(path.join(dir, 'snap.json'), r);
      }
      writeFileSync(path.join(dir, '.facts'), facts(item, drawings));
      console.log(`ok\t${id}\t${r.class}`);
    } catch (e) {
      // Does the stored pair itself build with the latest drawings? If it does, the snap failed.
      let builds = true;
      try { Side.pairRequest(item, new Map(Object.entries(drawings)), {size: SIZE}); } catch { builds = false; }
      if (builds) { fail(dir, {reference_id: id, size: SIZE, class: 'error', reason: 'the snap failed: ' + String(e.message), error: String(e.message)}); continue; }
      // A redrawn part whose stored hand layout was made for its previous drawing: place it automatically (its latest
      // drawing, in the stored position), as the side page does once that layout is cleared.
      const redrawn = item.parts.filter(part => part.icon && drawings[part.icon] && part.built_sha && part.current_sha &&
        part.built_sha !== part.current_sha && Array.isArray(part.layout) && part.layout.some(g => Array.isArray(g.paths)));
      if (redrawn.length) {
        const auto = {...item, parts: item.parts.map(part => redrawn.includes(part) ? {...part, layout: null} : part)};
        try {
          Side.pairRequest(auto, new Map(Object.entries(drawings)), {size: SIZE});
          rmSync(dir, {recursive: true, force: true});
          savePair(dir, auto, drawings, null);
          const r = snapDir(dir);
          Object.assign(r, {layout_reset: redrawn.map(part => part.role),
            reason: `${redrawn.map(part => `${part.role} ${part.icon}`).join(' and ')} was redrawn after the build: its old hand layout no longer fits, so it is placed automatically (latest drawing)`});
          writeJSON(path.join(dir, 'snap.json'), r);
          writeFileSync(path.join(dir, '.facts'), facts(item, drawings));
          console.log(`ok\t${id}\t${r.class} (layout reset)`);
          continue;
        } catch { /* fall through to the older drawing */ }
      }
      // The latest drawing of a changed part is missing or breaks the pair: try again with the drawing the pair was
      // built with (the part's form.document, the version its stored layout was made for).
      // Swap as few parts as possible: one changed part alone first (the other keeps its latest drawing), then both.
      const changed = item.parts.filter(part => part.icon && part.form?.document &&
        (!drawings[part.icon] || (part.built_sha && part.current_sha && part.built_sha !== part.current_sha)));
      const withOlder = parts => { const d = {...drawings}; for (const part of parts) d[part.icon] = {svg: part.form.document, svg_sha256: part.built_sha, review: part.review ?? null}; return d; };
      const sets = [...changed.map(part => [part]), ...(changed.length > 1 ? [changed] : [])];
      let use = sets.find(set => { try { Side.pairRequest(item, new Map(Object.entries(withOlder(set))), {size: SIZE}); return true; } catch { return false; } }) || changed;
      const older = withOlder(use), swapped = use.map(part => `${part.role} ${part.icon}`);
      const why = latestProblem({...item, parts: use}, drawings, e.message);
      try {
        if (!swapped.length) throw e;
        rmSync(dir, {recursive: true, force: true});
        savePair(dir, item, older, null);
        const r = snapDir(dir);
        Object.assign(r, {built_drawing: swapped, latest_problem: why,
          reason: `Used the older drawing (the one the pair was built with). Latest: ${why}`});
        writeJSON(path.join(dir, 'snap.json'), r);
        writeFileSync(path.join(dir, '.facts'), facts(item, drawings));
        console.log(`ok\t${id}\t${r.class} (built drawing)`);
      } catch (e2) {
        fail(dir, {reference_id: id, size: SIZE, class: 'cannot-build', reason: why + (swapped.length ? `; the drawing it was built with fails too (${e2.message})` : ''),
                   error: String(e.message), preview_url: item.icon?.preview_url || null});
      }
    }
  }
  function fail(dir, record) {
    mkdirSync(dir, {recursive: true});
    writeJSON(path.join(dir, 'snap.json'), record);
    console.log(`error\t${record.reference_id}\t${String(record.reason).replace(/\s+/g, ' ')}`);
  }
}

const facts = (item, drawings) => JSON.stringify({
  parts: item.parts.map(p => [p.role, p.icon, p.current_sha, JSON.stringify(p.layout), p.position]),
  drawings: item.parts.map(p => p.icon && drawings[p.icon]?.svg_sha256)});

async function pool(items, size, fn) {
  let next = 0;
  await Promise.all(Array.from({length: size}, async () => { while (next < items.length) await fn(items[next++]); }));
}

// Every built and stale pair of this size with its drawings, cached in cache/.
async function download(opts) {
  const cache = path.join(OUT, 'cache'), itemsFile = path.join(cache, 'items.json'), drawingsFile = path.join(cache, 'drawings.json');
  if (!opts.refresh && existsSync(itemsFile) && existsSync(drawingsFile)) return {items: readJSON(itemsFile), drawings: readJSON(drawingsFile)};
  mkdirSync(cache, {recursive: true});
  let items = [];
  for (const state of ['built', 'stale']) {
    for (let offset = 0; offset !== null && offset !== undefined;) {
      const {data} = await api(query({state, limit: String(PAGE), offset: String(offset)}));
      items.push(...data.items);
      offset = data.items.length ? data.next_offset : null;
      process.stderr.write(`\rlisted ${items.length}`);
    }
  }
  items = items.filter(i => i.parts.every(p => p.icon || p.form?.native_text));
  items.sort((a, b) => a.reference_id.localeCompare(b.reference_id));
  process.stderr.write(`\rlisted ${items.length} pairs with both parts picked\n`);
  const keys = [...new Set(items.flatMap(i => i.parts.map(p => p.icon).filter(Boolean)))], drawings = {}, batches = [];
  for (let i = 0; i < keys.length; i += KEYS) batches.push(keys.slice(i, i + KEYS));
  await pool(batches, 3, async batch => {
    Object.assign(drawings, (await api('/api/combinations/drawings?keys=' + encodeURIComponent(batch.join(',')))).data);
    process.stderr.write(`\rdrawings ${Object.keys(drawings).length} of ${keys.length}`);
  });
  process.stderr.write('\n');
  writeFileSync(itemsFile, JSON.stringify(items));
  writeFileSync(drawingsFile, JSON.stringify(drawings));
  return {items, drawings};
}

async function run(opts) {
  const {items: all, drawings} = await download(opts);
  // fixes.json {swaps: {"<role>:<old icon>": "<new icon>"}}: a part on an icon the build refuses (deleted on production, or of
  // the wrong family, e.g. a solo icon as the sub) is re-picked as the same drawing in the right family. The swapped part
  // is placed automatically (its old hand layout was for the old icon); the build stores the new pick.
  const fixesFile = path.join(OUT, 'fixes.json');
  const swaps = existsSync(fixesFile) ? readJSON(fixesFile).swaps || {} : {};
  const wanted = [...new Set(Object.values(swaps))].filter(k => !drawings[k]);
  for (let i = 0; i < wanted.length; i += KEYS) Object.assign(drawings, (await api('/api/combinations/drawings?keys=' + encodeURIComponent(wanted.slice(i, i + KEYS).join(',')))).data);
  const swapped = item => {
    if (!item.parts.some(p => swaps[`${p.role}:${p.icon}`])) return item;
    return {...item, swapped: true, parts: item.parts.map(p => {
      const to = swaps[`${p.role}:${p.icon}`];
      if (!to || !drawings[to]) return p;
      return {...p, icon: to, layout: null, current_sha: drawings[to].svg_sha256, built_sha: drawings[to].svg_sha256,
              review: drawings[to].review ?? null, swapped_from: p.icon};
    })};
  };
  let items = all.map(swapped);
  if (opts.ids) { const want = new Set(String(opts.ids).split(',')); items = items.filter(i => want.has(i.reference_id)); }
  if (opts.limit) items = items.slice(0, Number(opts.limit));
  const pairsDir = path.join(OUT, 'pairs');
  mkdirSync(pairsDir, {recursive: true});
  const jobs = [];
  let skipped = 0;
  for (const item of items) {
    const id = item.reference_id, dir = path.join(pairsDir, id);
    const own = Object.fromEntries(item.parts.filter(p => p.icon && drawings[p.icon]).map(p => [p.icon, drawings[p.icon]]));
    const f = path.join(dir, '.facts');
    if (!opts.force && existsSync(f) && readFileSync(f, 'utf8') === facts(item, own) && existsSync(path.join(dir, 'snap.json')) && !opts.redo?.split(',').includes(readJSON(path.join(dir, 'snap.json')).class) && readJSON(path.join(dir, 'snap.json')).class !== 'error') { skipped++; continue; }
    jobs.push({id, dir, item, drawings: own});
  }
  process.stderr.write(`${jobs.length} pairs to snap, ${skipped} already done\n`);
  if (jobs.length) {
    const n = Math.max(1, Math.min(Number(opts.jobs || 8), jobs.length)), tmp = path.join(OUT, '.jobs');
    mkdirSync(tmp, {recursive: true});
    let done = 0;
    await Promise.all(Array.from({length: n}, (_, w) => new Promise(resolve => {
      const file = path.join(tmp, `job-${w}.json`);
      writeFileSync(file, JSON.stringify(jobs.filter((_, i) => i % n === w)));
      const child = spawn(process.execPath, [new URL(import.meta.url).pathname, '--work', file], {stdio: ['ignore', 'pipe', 'inherit'], env: process.env});
      let buffer = '';
      child.stdout.on('data', chunk => {
        buffer += chunk;
        let at;
        while ((at = buffer.indexOf('\n')) >= 0) {
          const line = buffer.slice(0, at); buffer = buffer.slice(at + 1);
          if (/^(ok|error)\t/.test(line)) { done++; process.stderr.write(`\rsnapped ${done} of ${jobs.length}`); if (line.startsWith('error')) process.stderr.write(`\n${line}\n`); }
        }
      });
      child.on('close', resolve);
    })));
    process.stderr.write('\n');
    rmSync(tmp, {recursive: true, force: true});
  }
  report(all);
}

// summary.json, all.tsv and report.html over every pair folder of the cached list.
function report(items) {
  const rows = [];
  for (const item of items) {
    const f = path.join(OUT, 'pairs', item.reference_id, 'snap.json');
    if (!existsSync(f)) continue;
    const s = readJSON(f);
    const part = role => item.parts.find(p => p.role === role) || {};
    rows.push({...s, concept: item.concept, main_icon: part('main').icon || '', sub_icon: part('sub').icon || '(text)'});
  }
  const count = key => rows.reduce((m, r) => { const k = r[key] ?? '-'; m[k] = (m[k] || 0) + 1; return m; }, {});
  const byBoth = {};
  for (const r of rows) { const k = r.keyshape || '-'; byBoth[k] ??= {}; byBoth[k][r.class] = (byBoth[k][r.class] || 0) + 1; }
  const summary = {size: SIZE, keyshapes: KEYSHAPES, pairs: rows.length, by_class: count('class'), by_keyshape: count('keyshape'),
                   by_keyshape_class: byBoth, generated_at: new Date().toISOString()};
  writeJSON(path.join(OUT, 'summary.json'), summary);
  const tsv = [['reference_id', 'class', 'keyshape', 'position', 'move_total', 'main_move', 'sub_move', 'contact_before', 'contact_after', 'new_flags', 'concept'].join('\t'),
    ...rows.map(r => [r.reference_id, r.class, r.keyshape || '', r.position || '', r.move?.total ?? '', (r.move?.main || []).join(','), (r.move?.sub || []).join(','),
                      r.before?.contact || '', r.after?.contact || '', (r.after?.new_flags || []).join(','), r.concept || ''].join('\t'))];
  writeFileSync(path.join(OUT, 'all.tsv'), tsv.join('\n') + '\n');
  const data = rows.map(r => ({id: r.reference_id, c: r.class, k: r.keyshape, p: r.position, m: r.move, n: r.concept,
                               b: r.before?.contact, a: r.after?.contact, f: r.after?.new_flags || [], pr: r.after?.problems || [], r: r.reason || null,
                               pv: r.preview_url ? API + r.preview_url : null}));
  writeFileSync(path.join(OUT, 'report.html'), page(summary, data));
  console.log(JSON.stringify({out: OUT, ...summary, keyshapes: undefined}, null, 2));
}

function page(summary, data) {
  const esc = s => String(s).replace(/</g, '\\u003c');
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Side keyshape snap ${SIZE}</title>
<style>
:root{--bg:#fafafa;--fg:#1a1a1a;--muted:#666;--card:#fff;--line:#ddd;--ok:#1a7f37;--warn:#b35900;--bad:#c62828}
@media (prefers-color-scheme:dark){:root{--bg:#141414;--fg:#eee;--muted:#999;--card:#1e1e1e;--line:#333}}
body{margin:0;padding:16px;background:var(--bg);color:var(--fg);font:14px/1.4 system-ui,sans-serif}
h1{font-size:20px;margin:0 0 8px}.bar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:8px 0 16px}
button{border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:6px;padding:4px 10px;cursor:pointer}
button.on{background:var(--fg);color:var(--bg)}#grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}
.card{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:8px}.imgs{display:flex;gap:4px}
.imgs img{width:50%;aspect-ratio:1;border:1px solid var(--line);background:#fff}.meta{font-size:12px;color:var(--muted);margin-top:6px;word-break:break-word}
.tag{display:inline-block;font-size:11px;padding:1px 6px;border-radius:10px;border:1px solid currentColor;margin-right:4px}
.already-fits{color:var(--muted)}.snapped-ok{color:var(--ok)}.snapped-flagged,.shrunk-to-fit{color:var(--warn)}.no-fit,.error,.cannot-build{color:var(--bad)}
.why{font-size:12px;margin-top:6px;font-weight:550}.legend{font-size:13px;color:var(--muted);margin:4px 0 8px;padding-left:18px}.legend b{color:var(--fg)}
#more{margin:16px auto;display:block}
</style></head><body>
<h1>Side keyshape snap · ${SIZE}</h1>
<div class="meta">${summary.pairs} pairs · move only (main and sub keep their size) · left: stored, right: snapped · red dashed: keyshape · generated ${summary.generated_at}</div>
<ul class="legend">
<li><b>already-fits</b>: already inside a keyshape, nothing moved</li>
<li><b>snapped-ok</b>: in the keyshape and contact still passes. When main + sub already fit a keyshape together they move as one piece, centered (nothing between them changes); only when they fit none do they move closer on their own. A part larger than every keyshape (a main grown to 60 wide) is shrunk evenly as little as possible: see its note</li>
<li><b>snapped-flagged</b>: moved in, but moving them closer made the sub cut the main more (a new flag or a contact failure); look at these</li>

<li><b>no-fit</b>: even shrinking cannot fit it (a native-text sub keeps its size); stored layout kept</li>
<li><b>Used the older drawing</b> (red line on a card): the latest main or sub on production does not build (deleted, or redrawn with a broken file / not matching the stored hand layout), so that part uses the drawing the pair was built with. The line says what is wrong with the latest one</li>
<li><b>cannot-build</b>: neither the latest nor the older drawing builds (should be none)</li>
<li><b>error</b>: the snap itself failed (should be none)</li></ul>
<div class="bar" id="classes"></div><div class="bar" id="shapes"></div>
<div id="grid"></div><button id="more">Show more</button>
<script>
const DATA=${esc(JSON.stringify(data))};
let cls=null,shape=null,shown=0;const STEP=120;
function chips(el,key,label){const counts={};DATA.forEach(d=>{const k=d[key]||'-';counts[k]=(counts[k]||0)+1});
 const make=(v,t)=>{const b=document.createElement('button');b.textContent=t;b.onclick=()=>{if(key==='c')cls=v;else shape=v;
  [...el.children].forEach(x=>x.classList.toggle('on',x===b));render(true)};return b};
 const all=make(null,label+' (all '+DATA.length+')');all.classList.add('on');el.append(all);
 Object.entries(counts).sort((a,b)=>b[1]-a[1]).forEach(([k,n])=>el.append(make(k,k+' '+n)))}
chips(document.getElementById('classes'),'c','Class');chips(document.getElementById('shapes'),'k','Keyshape');
function list(){return DATA.filter(d=>(!cls||d.c===cls)&&(!shape||(d.k||'-')===shape))}
function card(d){const el=document.createElement('div');el.className='card';const base='pairs/'+d.id+'/';
 const broken=d.c==='cannot-build'||d.c==='error';
 const before=broken?(d.pv?'<img loading="lazy" src="'+d.pv+'" alt="stored on production">':''):'<img loading="lazy" src="'+base+'before@4x.png" alt="stored">';
 const after=broken||d.c==='no-fit'?'':'<img loading="lazy" src="'+base+'after@4x.png" alt="snapped">';
 el.innerHTML='<div class="imgs">'+before+after+'</div>'+(d.r?'<div class="why '+d.c+'">'+d.r+'</div>':'')+
  '<div class="meta"><span class="tag '+d.c+'">'+d.c+'</span>'+(d.k||'')+' · '+(d.p||'')+(d.m?' · move '+d.m.total+' (main '+d.m.main+' / sub '+d.m.sub+')':'')+
  '<br>'+(d.n||'')+'<br><code>'+d.id+'</code>'+(d.f.length?'<br>new flags: '+d.f.join(', '):'')+(d.a?'<br>contact '+d.b+' → '+d.a:'')+
  (d.pr.length?'<br>'+d.pr.join('; '):'')+'</div>';return el}
function render(reset){const g=document.getElementById('grid'),l=list();if(reset){g.innerHTML='';shown=0}
 l.slice(shown,shown+STEP).forEach(d=>g.append(card(d)));shown=Math.min(l.length,shown+STEP);
 document.getElementById('more').style.display=shown<l.length?'block':'none'}
document.getElementById('more').onclick=()=>render(false);render(true);
</script></body></html>
`;
}

function options(argv) {
  const out = {};
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (!a.startsWith('--')) continue;
    const next = argv[i + 1];
    if (next === undefined || next.startsWith('--')) out[a.slice(2)] = true; else { out[a.slice(2)] = next; i++; }
  }
  return out;
}

if (process.argv[1] && path.resolve(process.argv[1]) === new URL(import.meta.url).pathname) {
  const opts = options(process.argv.slice(2));
  try {
    if (opts.work) await work(opts.work);
    else if (opts['report-only']) report(readJSON(path.join(OUT, 'cache/items.json')));
    else await run(opts);
  } catch (e) { console.error('error: ' + e.message); process.exit(1); }
}
