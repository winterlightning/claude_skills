#!/usr/bin/env node
// Put every work folder whose stored layout has a part off its keyshape presets back in order (user decision 2026-10-12:
// no search, no AI review):
//   1. centre: when main + sub together (their painted box) have the size of a canvas keyshape, move the whole pair, as
//      one piece and by whole units, into that keyshape (nothing between the parts changes);
//   2. else snap: each off part moves / resizes to the closest box of its own keyshape at a preset size, anchored in a
//      canvas keyshape, taking the nearest combination that passes the keyshape check. Contact is measured and recorded, not used to choose. Writes <dir>/layout.json and
// <dir>/preset-snap.json, and with --push stores the layouts on production (POST /api/combinations/build, the layout
// editor's Save) after checking the pair did not change there.
//
//   node icon_set/scripts/side_snap_presets.mjs [--push]          (SIDE_SIZE=72 for the 72 pairs)
import {existsSync, readFileSync, readdirSync, writeFileSync} from 'node:fs';
import path from 'node:path';
import {api, login, query} from './side_layout.mjs';
import {SIZE, Side, WORK_NAME, compose} from './side_compose.mjs';
import {FRAMES, keyshapeCheck, presetBoxes} from './side_keyshape_check.mjs';
import {checkDir} from './side_contact_check.mjs';

const HERE = path.dirname(new URL(import.meta.url).pathname);
const WORK = path.resolve(HERE, '../work', WORK_NAME);
const push = process.argv.includes('--push');
const read = (dir, f) => JSON.parse(readFileSync(path.join(dir, f), 'utf8'));
const write = (dir, f, d) => writeFileSync(path.join(dir, f), JSON.stringify(d, null, 2) + '\n');
const box = s => { const [x, y, w, h] = s.split(',').map(Number); return {x, y, w, h}; };

const results = [];
for (const id of readdirSync(WORK).sort()) {
  const dir = path.join(WORK, id);
  if (!existsSync(path.join(dir, 'base-layout.json')) || existsSync(path.join(dir, 'review.json'))) continue;
  const base = read(dir, 'base-layout.json');
  const stored = {position: base.position, main: base.main, sub: base.sub};
  const ks = keyshapeCheck(dir, stored);
  if (ks.ok) continue;
  // 1. Centre: the pair's painted box has the size of a canvas keyshape (within half a unit).
  const painted = g => { const b = Side.groupsBox(g); return [b.x - 2, b.y - 2, b.x + b.w + 2, b.y + b.h + 2]; };
  const pm = painted(base.main), ps = painted(base.sub);
  const u = [Math.min(pm[0], ps[0]), Math.min(pm[1], ps[1]), Math.max(pm[2], ps[2]), Math.max(pm[3], ps[3])];
  const match = FRAMES.find(f => Math.abs((f.box[2] - f.box[0]) - (u[2] - u[0])) <= 0.5 && Math.abs((f.box[3] - f.box[1]) - (u[3] - u[1])) <= 0.5);
  if (match) {
    const dx = Math.round(match.box[0] - u[0]), dy = Math.round(match.box[1] - u[1]);
    const shift = gs => gs.map(g => ({...g, x: g.x + dx, y: g.y + dy}));
    const layout = {...stored, main: shift(base.main), sub: shift(base.sub)};
    write(dir, 'layout.json', layout);
    const after = keyshapeCheck(dir, layout);
    let contact = null;
    try { contact = checkDir(dir).verdict; } catch (e) { contact = 'error: ' + e.message; }
    const rec = {status: 'centred', at: new Date().toISOString(), keyshape: match.name, move: [dx, dy], canvas: after.canvas?.keyshape,
                 parts_on_presets: after.ok, parts: Object.fromEntries(Object.entries(after.roles).map(([k, x]) => [k, x.ok ? x.preset : 'off ' + x.box])), contact};
    write(dir, 'preset-snap.json', rec);
    results.push({id, dir, ...rec});
    continue;
  }
  // 2. Snap the off parts to their nearest presets.
  const off = Object.entries(ks.roles).filter(([, r]) => !r.ok).map(([role]) => role);
  const options = {};
  for (const role of off) {
    const cur = Side.groupsBox(base[role]);
    options[role] = presetBoxes(dir, role, base.position).map(p => ({...p, b: box(p.box)}))
      .map(p => ({...p, d: Math.abs(p.b.x - cur.x) + Math.abs(p.b.y - cur.y) + Math.abs(p.b.w - cur.w) + Math.abs(p.b.h - cur.h)}))
      .sort((a, b) => a.d - b.d).slice(0, 10);
  }
  const combos = off.length === 1 ? options[off[0]].map(p => ({[off[0]]: p}))
    : options.main.flatMap(m => options.sub.map(s => ({main: m, sub: s}))).sort((a, b) => a.main.d + a.sub.d - b.main.d - b.sub.d);
  let picked = null;
  for (const combo of combos) {
    const layout = {...stored};
    for (const [role, p] of Object.entries(combo)) layout[role] = Side.mapGroups(base[role], Side.groupsBox(base[role]), p.b);
    if (keyshapeCheck(dir, layout).ok) { picked = {combo, layout}; break; }
  }
  if (!picked) { results.push({id, status: 'no preset fits'}); write(dir, 'preset-snap.json', {status: 'no preset fits'}); continue; }
  write(dir, 'layout.json', picked.layout);
  let contact = null;
  try { contact = checkDir(dir).verdict; } catch (e) { contact = 'error: ' + e.message; }
  const moved = Object.fromEntries(Object.entries(picked.combo).map(([r, p]) => [r, `${p.name} at ${p.size} in ${p.frame}: ${p.box}`]));
  const rec = {status: 'snapped', at: new Date().toISOString(), moved, canvas: keyshapeCheck(dir, picked.layout).canvas?.keyshape, contact};
  write(dir, 'preset-snap.json', rec);
  results.push({id, dir, ...rec});
}
const count = (k) => results.reduce((m, r) => { m[r[k]] = (m[r[k]] || 0) + 1; return m; }, {});
console.log(JSON.stringify({size: SIZE, off: results.length, status: count('status'), contact: count('contact'),
  centred_parts_on_presets: results.filter(r => r.status === 'centred').reduce((m, r) => { const k = r.parts_on_presets ? 'yes' : 'no'; m[k] = (m[k] || 0) + 1; return m; }, {})}, null, 1));
if (!push) { console.error('not pushed: add --push'); process.exit(0); }

// Push: one build per pair, the pair unchanged on production since it was fetched.
const live = new Map();
for (let offset = 0; offset !== null && offset !== undefined;) {
  const {data} = await api(query({state: 'built', limit: '500', offset: String(offset)}));
  for (const i of data.items) live.set(i.reference_id, i);
  offset = data.items.length ? data.next_offset : null;
}
const facts = it => JSON.stringify(it.parts.map(p => [p.role, p.icon, p.current_sha, JSON.stringify(p.layout), p.position]));
const ready = results.filter(r => r.status === 'snapped' || r.status === 'centred').filter(r => { const it = live.get(r.id); return it && facts(it) === facts(read(r.dir, 'item.json')); });
await login();
let ok = 0, failed = 0;
for (let i = 0; i < ready.length; i += 25) {
  const chunk = ready.slice(i, i + 25);
  const builds = chunk.map(r => compose(r.dir, read(r.dir, 'layout.json')).request);
  const {data} = await api('/api/combinations/build', {size: SIZE, builds});
  for (const res of data.results) {
    const r = chunk.find(c => c.id === res.reference_id);
    if (res.ok) { ok++; write(r.dir, 'preset-snap.json', {...read(r.dir, 'preset-snap.json'), pushed_at: new Date().toISOString(), pushed_keyshape: builds.find(b => b.reference_id === r.id)?.keyshape}); }
    else { failed++; console.error(`failed ${res.reference_id}: ${res.error}`); }
  }
  process.stderr.write(`\rpushed ${ok}, failed ${failed} of ${ready.length}`);
}
process.stderr.write('\n');
console.log(JSON.stringify({pushed: ok, failed, changed_on_production: results.filter(r => r.status === 'snapped' || r.status === 'centred').length - ready.length}));
