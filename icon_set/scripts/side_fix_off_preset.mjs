#!/usr/bin/env node
// Put a side pair whose stored layout has a part off its keyshape presets back on the keyshape system (one work folder):
//   1. the nearest preset: each off part moves / resizes to the closest box of its own keyshape at a preset size inside a
//      canvas keyshape (the main may also keep a moved preset box), kept when the keyshape check and the contact check
//      pass and no damage flag is added;
//   2. else the best candidate of side_layout_search.mjs (every preset layout, ranked in the skill's order);
//   3. else nothing (reported).
// Writes <dir>/layout.json (the fix, for side_layout.mjs push) and <dir>/off-preset-fix.json. Never pushes.
//
//   node icon_set/scripts/side_fix_off_preset.mjs <dir>        (SIDE_SIZE=72 for the 72 pairs)
import {execFileSync} from 'node:child_process';
import {readFileSync, writeFileSync} from 'node:fs';
import path from 'node:path';
import {Side} from './side_compose.mjs';
import {keyshapeCheck, presetBoxes} from './side_keyshape_check.mjs';
import {checkDir} from './side_contact_check.mjs';
import {analyzeDir, summary} from './side_overlap.mjs';

const HERE = path.dirname(new URL(import.meta.url).pathname);
const dir = path.resolve(process.argv[2] || '');
const read = f => JSON.parse(readFileSync(path.join(dir, f), 'utf8'));
const write = (f, d) => writeFileSync(path.join(dir, f), JSON.stringify(d, null, 2) + '\n');
const DAMAGE = ['lost_feature', 'lost_part', 'erased_whole_piece', 'fragmented', 'stub', 'heavy_cut', 'container'];
const damage = flags => flags.filter(f => DAMAGE.includes(f)).length;
const box = s => { const [x, y, w, h] = s.split(',').map(Number); return {x, y, w, h}; };

const base = read('base-layout.json');
const stored = {position: base.position, main: base.main, sub: base.sub};
const ksBefore = keyshapeCheck(dir, stored);
const before = read('fetch.json').overlap || {flags: []};
const result = {reference_id: path.basename(dir), before: {flags: before.flags || [], keyshape: ksBefore.ok}};
if (ksBefore.ok) { write('off-preset-fix.json', {...result, status: 'already on the system'}); console.log('on'); process.exit(0); }

// Measure layout.json as it stands: keyshape, contact, flags.
function judge(layout) {
  write('layout.json', layout);
  const ks = keyshapeCheck(dir, layout);
  if (!ks.ok) return {ok: false, why: 'off the keyshape system'};
  const c = checkDir(dir), o = summary(analyzeDir(dir, {}, 'overlap.png'));
  if (c.verdict === 'fail') return {ok: false, why: 'contact fails: ' + (c.problems || [])[0]};
  if (damage(o.flags) > damage(before.flags || [])) return {ok: false, why: 'adds damage: ' + o.flags.join(',')};
  return {ok: true, contact: c.verdict, flags: o.flags, erased: o.erased_pct, canvas: ks.canvas?.keyshape, parts: ks.roles};
}

// 1. Nearest preset for each off part (same position), trying the canvas keyshapes nearest first.
const off = Object.entries(ksBefore.roles).filter(([, r]) => !r.ok).map(([role]) => role);
const options = {};
for (const role of off) {
  const cur = Side.groupsBox(base[role]);
  options[role] = presetBoxes(dir, role, base.position).filter(p => p.name !== 'as drawn').map(p => ({...p, b: box(p.box)}))
    .map(p => ({...p, d: Math.abs(p.b.x - cur.x) + Math.abs(p.b.y - cur.y) + Math.abs(p.b.w - cur.w) + Math.abs(p.b.h - cur.h)}))
    .sort((a, b) => a.d - b.d).slice(0, 6);
}
const combos = off.length === 1 ? options[off[0]].map(p => ({[off[0]]: p}))
  : options.main.flatMap(m => options.sub.map(s => ({main: m, sub: s}))).sort((a, b) => a.main.d + a.sub.d - b.main.d - b.sub.d).slice(0, 12);
let fixed = null;
for (const combo of combos) {
  const layout = {...stored};
  for (const [role, p] of Object.entries(combo)) layout[role] = Side.mapGroups(base[role], Side.groupsBox(base[role]), p.b);
  const j = judge(layout);
  if (j.ok) { fixed = {method: 'nearest preset', moved: Object.fromEntries(Object.entries(combo).map(([r, p]) => [r, `${p.name} at ${p.size} in ${p.frame}: ${p.box}`])), ...j}; break; }
}

// 2. The layout search's best candidate.
if (!fixed) {
  let top = null;
  try {
    const out = execFileSync(process.execPath, [path.join(HERE, 'side_layout_search.mjs'), dir, '--top', '3', '--json'], {encoding: 'utf8', timeout: 600000, env: process.env});
    top = JSON.parse(out.slice(out.indexOf('{'))).candidates || [];
  } catch (e) { top = []; }
  for (const c of top) {
    try {
      execFileSync(process.execPath, [path.join(HERE, 'side_layout.mjs'), 'preview', dir, '--position', c.position, '--auto'], {stdio: 'ignore', env: process.env});
      execFileSync(process.execPath, [path.join(HERE, 'side_layout.mjs'), 'preview', dir, '--main', c.mainBox, '--sub', c.subBox], {stdio: 'ignore', env: process.env});
    } catch { continue; }
    const j = judge(read('layout.json'));
    if (j.ok) { fixed = {method: 'layout search', candidate: `${c.position} ${c.frame} main ${c.main} sub ${c.sub}`, ...j}; break; }
  }
}

if (!fixed) write('layout.json', stored);
write('off-preset-fix.json', {...result, status: fixed ? 'fixed' : 'no layout found', ...(fixed || {}),
  ...(fixed ? {} : {note: 'every nearest preset and search candidate failed the keyshape, contact or damage check'})});
console.log(fixed ? `fixed (${fixed.method})` : 'no layout found');
