#!/usr/bin/env node
// Try every keyshape-preset layout of one side pair in a single run and rank them in the skill's order, so the agent
// looks once instead of previewing dozens of layouts by hand (/side-layout-adjust).
//
//   node icon_set/scripts/side_layout_search.mjs <dir> [--top 8] [--positions br,tr,...] [--json]
//
// Candidates: every position, every main preset size, the sub at its stored size (and one step smaller, ranked last).
// Each is composed with the same engine as the page and measured with side_overlap.mjs + side_contact_check.mjs.
// Kept: contact passes (knockout or clear) and the keyshape check passes. Ranked by the skill's order:
//   0 stored · 1 resize main: stored position, main resized · 2 move sub: same sizes, another position ·
//   3 move sub + resize main · 4 resize sub: one step smaller (last resort).
// The main never moves on its own: it stays in the corner opposite the sub, on its keyshape presets (user rule 2026-10-10).
// A layout that damages the main (lost_feature, lost_part, erased_whole_piece, fragmented, stub) ranks after every
// layout that keeps it whole, whatever the tier.
// (the user's priority flow: 1 resize the main, 2 move the sub, 3 move the sub with the main resized, 4 resize the sub),
// then by flags / penalty, low-damage knockouts before clear space. A smaller sub (step 4) is listed only when steps 1-3 found nothing:
// the sub stays at its stored size (32) whenever any other layout works. Writes <dir>/search.png: the stored layout and the top
// candidates side by side, labelled with their rank number. Preview the one you pick with the printed command.
import {existsSync, mkdirSync, writeFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import path from 'node:path';
import {PARTS, SIZE, Side, compose, drawingMap, layoutFor, readJSON} from './side_compose.mjs';
import {analyze, summary} from './side_overlap.mjs';
import {contact} from './side_contact_check.mjs';
import {keyshapeCheck, presetBoxes} from './side_keyshape_check.mjs';

const POSITIONS = ['br', 'tr', 'bl', 'tl', 'ri', 'le', 'bo', 'to'];
const args = process.argv.slice(2);
const opt = n => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : undefined; };
const dir = path.resolve(args.find(a => !a.startsWith('--') && a !== opt('--top') && a !== opt('--positions')) || '');
if (!existsSync(path.join(dir, 'item.json'))) { console.error('usage: side_layout_search.mjs <work dir> [--top 8] [--positions br,tr] [--json]'); process.exit(2); }
const TOP = Number(opt('--top') || 8);
const positions = (opt('--positions') || POSITIONS.join(',')).split(',');

const item = readJSON(path.join(dir, 'item.json'));
const drawings = drawingMap(readJSON(path.join(dir, 'drawings.json')));
const base = readJSON(path.join(dir, 'base-layout.json'));
const size = s => Number(String(s || '').match(/ at (\d+)$/)?.[1]) || null;
const ksBase = keyshapeCheck(dir, base);
const storedMain = size(ksBase.roles.main?.preset) || PARTS.main, storedSub = size(ksBase.roles.sub?.preset) || PARTS.sub;

// The automatic groups of a role at a position (as side_layout.mjs preview --auto builds them).
function autoGroups(position) {
  const composed = Side.pairRequest(item, drawings, {position, layout: null, size: SIZE});
  const out = {};
  for (const role of ['main', 'sub']) {
    const form = composed.current.row[role === 'main' ? 'mains' : 'subs'][0];
    const parts = Side.elementParts(form.engine_document ?? form.document);
    const placed = composed.result.placements[role === 'main' ? 0 : 1].painted_box;
    const auto = {paths: parts.sources.map((b, i) => b ? i : null).filter(i => i !== null), x: placed.x + 2, y: placed.y + 2, w: placed.w - 4, h: placed.h - 4};
    const {sx, sy} = Side.groupTransform(auto, parts.sources);
    out[role] = Side.splitGroups([auto], parts.sources, Side.connected(parts.segments, 4 / ((sx + sy) / 2)));
  }
  return out;
}
const box = s => { const [x, y, w, h] = s.split(',').map(Number); return {x, y, w, h}; };

function measure(layout) {
  const composed = compose(dir, layout);
  const a = analyze(composed, layoutFor(dir, layout)), s = summary(a), c = contact(a);
  return {svg: composed.svg, flags: s.flags, penalty: s.penalty, reach: s.reach, erased: s.erased_pct,
          lost: s.parts.lost, contact: c.verdict, problems: c.problems};
}

const stored = {tier: 0, position: base.position, main: storedMain, sub: storedSub, layout: base, ...measure(base)};
const seen = new Set(), found = [];
for (const position of positions) {
  let groups;
  try { groups = autoGroups(position); } catch { continue; }
  const subs = presetBoxes(dir, 'sub', position).filter(b => b.size === storedSub || b.size === storedSub - 4 && b.size >= PARTS.sub - 4);
  for (const m of presetBoxes(dir, 'main', position)) for (const s of subs) {
    const key = `${position} ${m.box} ${s.box}`;
    if (seen.has(key)) continue;
    seen.add(key);
    const layout = {...base, position, main: Side.mapGroups(groups.main, Side.groupsBox(groups.main), box(m.box)),
                    sub: Side.mapGroups(groups.sub, Side.groupsBox(groups.sub), box(s.box))};
    if (!keyshapeCheck(dir, layout).ok) continue;
    let r;
    try { r = measure(layout); } catch { continue; }
    if (r.contact === 'fail') continue;
    const same = position === base.position && m.size === storedMain && s.size === storedSub;
    if (same) continue; // that is the stored layout
    const moved = position !== base.position, mainResized = m.size !== storedMain;
    const tier = s.size < storedSub ? 4 : !moved ? 1 : !mainResized ? 2 : 3;
    found.push({tier, position, main: m.size, sub: s.size, mainBox: m.box, subBox: s.box, layout, ...r});
  }
}
// Skill order: a layout that damages the main (loses a feature or part, cuts it into pieces, leaves crumbs) ranks after
// every layout that keeps the main whole, whatever its tier: the Luggage Cart's tr knockout (sub moved) took the cart's
// handle while a moved-and-resized layout kept it. Then tier, then clean (no flags), then low-damage knockout before clear, then
// penalty, then closest main size.
const DAMAGE = ['lost_feature', 'lost_part', 'erased_whole_piece', 'fragmented', 'stub'];
const damaged = c => c.flags.some(f => DAMAGE.includes(f)) ? 1 : 0;
const score = c => [damaged(c), c.tier, c.flags.length, c.contact === 'knockout' && c.erased <= 15 ? 0 : c.contact === 'clear' ? 1 : 2,
                    c.penalty, Math.abs(c.main - storedMain), c.erased];
found.sort((a, b) => { const x = score(a), y = score(b); for (let i = 0; i < x.length; i++) if (x[i] !== y[i]) return x[i] - y[i]; return 0; });
// Resize the sub only as the last step: drop the smaller-sub layouts whenever any full-size layout keeps the main whole.
const full = found.filter(c => c.tier < 4 && (!damaged(c) || !found.some(d => d.tier === 4 && !damaged(d))));
const top = (full.length ? full : found).slice(0, TOP);

const TIER = ['stored', '1 main size', '2 sub moved', '3 sub+main', '4 sub size'];
const line = (n, c) => `${String(n).padStart(2)}  ${TIER[c.tier].padEnd(12)} ${c.position.padEnd(3)} main ${String(c.main).padEnd(3)} sub ${String(c.sub).padEnd(3)} `
  + `${c.contact.padEnd(8)} reach ${String(c.reach).padEnd(6)} erased ${String(c.erased).padEnd(5)} ${c.flags.length ? 'flags ' + c.flags.join(',') : 'no flags'}`;

// Contact sheet: stored + the top candidates, numbered.
const sheet = path.join(dir, 'search');
mkdirSync(sheet, {recursive: true});
const tiles = [];
[stored, ...top].forEach((c, i) => {
  const svg = path.join(sheet, `${i}.svg`), png = path.join(sheet, `${i}.png`);
  writeFileSync(svg, c.svg);
  try { execFileSync('rsvg-convert', ['-w', '192', '-h', '192', '-b', 'white', '-o', png, svg], {timeout: 30000}); tiles.push([png, i ? `${i} ${TIER[c.tier]} ${c.position} m${c.main} s${c.sub}` : `stored ${c.contact}`]); } catch {}
});
try {
  execFileSync('magick', ['montage', ...tiles.flatMap(([f, l]) => ['-label', l, f]), '-tile', '5x', '-geometry', '192x192+6+6', '-pointsize', '13', path.join(dir, 'search.png')], {timeout: 60000});
} catch {}

if (args.includes('--json')) {
  console.log(JSON.stringify({stored: {...stored, svg: undefined, layout: undefined}, candidates: top.map(c => ({...c, svg: undefined, layout: undefined}))}, null, 2));
} else {
  console.log(`${item.concept} · stored ${base.position} main ${storedMain} sub ${storedSub}: ${stored.contact}${stored.flags.length ? ' · flags ' + stored.flags.join(',') : ''}${stored.problems?.length ? ' · ' + stored.problems[0] : ''}`);
  console.log(`${seen.size} preset layouts tried, ${found.length} pass contact + keyshape (${full.length} with the sub at its stored size ${storedSub}). Best ${top.length} (picture: ${path.join(dir, 'search.png')}):`);
  if (!full.length && top.length) console.log(`  No layout keeps the sub at ${storedSub}: these shrink it one step (step 4, hard case only; record --sub-smaller).`);
  top.forEach((c, i) => console.log(line(i + 1, c) + `\n      preview: --position ${c.position} --auto, then --main ${c.mainBox} --sub ${c.subBox}`));
  if (!top.length) console.log('  none: keep the stored layout (ok --keep-stored if it reads well, else No layout fits).');
}
