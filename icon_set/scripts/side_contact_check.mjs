#!/usr/bin/env node
// Contact check for a side pair (/side-layout-adjust): the main and sub either sit in a real overlap, where the sub's
// knockout takes a plain chunk out of the main, or stand clear of each other with nothing erased. Anything between
// is not allowed: a tiny clearance (the sub sits inside the engine's 4-unit cut margin and shaves the main) or a tiny
// overlap (the sub grazes the main and nicks a speck or a thin sliver off its edge).
//
//   node icon_set/scripts/side_contact_check.mjs <DIR> [<DIR> ...] [--current] [--json]
//                                                [--clear-min 4] [--clear-max 4.5] [--overlap-min 2] [--chunk 1.5] [--noise 0.25] [--speck 0.1]
//
// DIR is a side_layout.mjs work folder. Measures layout.json (the proposal), or base-layout.json (the stored layout)
// with --current. Writes DIR/contact.png (or contact-current.png): kept main black, erased chunks red, nicks
// magenta, sub blue. Exits 1 when any DIR fails.
//
// The erased main (uncut main minus kept main) is split into 8-connected patches after peeling --noise units off
// every edge (the 2-decimal rounding of the stored path). Each patch is then:
//   chunk  some pixel lies at least --chunk units inside it: the knockout cut through the full 4-unit stroke
//   nick   it does not: a speck or a sliver shaved off the stroke's edge, which reads as a drawing mistake
// Verdict:
//   clear     no patch, and reach (clear space from the uncut main to the sub) between --clear-min and --clear-max
//   knockout  patches, every one a chunk, and the sub's ink sits at least --overlap-min units into the main's ink
//             (reach <= -overlap-min, half the 4-unit stroke): plainly on it, not grazing it
//   fail      a nick; a cut while the sub does not touch the main (reach > 0: tiny clearance, the cut margin shaves);
//             a cut from a sub that only grazes the main (-overlap-min < reach <= 0: tiny overlap); reach below
//             --clear-min with nothing cut; reach above --clear-max (detached: the parts float apart); or the main
//             surrounds the sub (side_overlap.mjs `container`: a container combination, not a side one)
import {execFileSync} from 'node:child_process';
import {existsSync, rmSync, writeFileSync} from 'node:fs';
import path from 'node:path';
import {compose, layoutFor, readJSON} from './side_compose.mjs';
import {analyze} from './side_overlap.mjs';

const RES = 8;               // raster pixels a grid unit (side_overlap.mjs)
const DEFAULTS = {clearMin: 4, clearMax: 4.5, overlapMin: 2, chunk: 1.5, noise: 0.25, speck: 0.1};

// Distance in pixels from each mask pixel to the nearest pixel outside it (chamfer 3-4, divided by 3).
function insideDistance(mask, n) {
  const d = new Float32Array(n * n);
  const big = 1e9;
  for (let i = 0; i < d.length; i++) d[i] = mask[i] ? big : 0;
  const at = (x, y) => (x < 0 || y < 0 || x >= n || y >= n) ? 0 : d[y * n + x];
  for (let y = 0; y < n; y++) for (let x = 0; x < n; x++) {
    const i = y * n + x;
    if (!d[i]) continue;
    d[i] = Math.min(d[i], at(x - 1, y) + 3, at(x, y - 1) + 3, at(x - 1, y - 1) + 4, at(x + 1, y - 1) + 4);
  }
  for (let y = n - 1; y >= 0; y--) for (let x = n - 1; x >= 0; x--) {
    const i = y * n + x;
    if (!d[i]) continue;
    d[i] = Math.min(d[i], at(x + 1, y) + 3, at(x, y + 1) + 3, at(x + 1, y + 1) + 4, at(x - 1, y + 1) + 4);
  }
  for (let i = 0; i < d.length; i++) d[i] /= 3;
  return d;
}

// 8-connected patches of a mask: [{px: [indices], depth: max inside distance in units, box: [x0, y0, x1, y1] units}].
function patches(mask, depth, n) {
  const seen = new Uint8Array(n * n), out = [], stack = [];
  for (let start = 0; start < mask.length; start++) {
    if (!mask[start] || seen[start]) continue;
    const px = [], box = [n, n, -1, -1];
    let deepest = 0;
    seen[start] = 1;
    stack.push(start);
    while (stack.length) {
      const i = stack.pop(), x = i % n, y = (i - x) / n;
      px.push(i);
      deepest = Math.max(deepest, depth[i]);
      box[0] = Math.min(box[0], x); box[1] = Math.min(box[1], y); box[2] = Math.max(box[2], x); box[3] = Math.max(box[3], y);
      for (let dy = -1; dy <= 1; dy++) for (let dx = -1; dx <= 1; dx++) {
        const xx = x + dx, yy = y + dy;
        if (xx < 0 || yy < 0 || xx >= n || yy >= n) continue;
        const j = yy * n + xx;
        if (mask[j] && !seen[j]) { seen[j] = 1; stack.push(j); }
      }
    }
    out.push({px, depth: deepest / RES, box: [box[0] / RES, box[1] / RES, (box[2] + 1) / RES, (box[3] + 1) / RES]});
  }
  return out;
}

export function contact(analysis, limits = {}) {
  const {clearMin, clearMax, overlapMin, chunk, noise, speck} = {...DEFAULTS, ...limits};
  const {n, main, kept} = analysis.masks;
  const erased = new Uint8Array(n * n);
  for (let i = 0; i < erased.length; i++) erased[i] = main[i] && !kept[i] ? 1 : 0;
  // Peel the rounding noise off every edge; what survives is erased ink, grown back to its full extent below.
  // When the sub does not reach the main (reach > 0) nothing may be erased at all, so peel nothing: a sliver one
  // pixel deep is still a visible shave. Only raster specks under --speck units² are dropped.
  const reach0 = analysis.reach, clearCase = reach0 !== null && reach0 > 0;
  const depth = insideDistance(erased, n), core = new Uint8Array(n * n);
  for (let i = 0; i < core.length; i++) core[i] = clearCase ? erased[i] : (depth[i] > noise * RES ? 1 : 0);
  const found = patches(core, depth, n).filter(p => !clearCase || p.px.length >= speck * RES * RES).map(p => {
    const kind = p.depth >= chunk ? 'chunk' : 'nick';
    return {kind, depth: +p.depth.toFixed(2), area: +(p.px.length / (RES * RES)).toFixed(1),
            box: p.box.map(v => +v.toFixed(1)), px: p.px};
  });
  const nicks = found.filter(p => p.kind === 'nick'), chunks = found.filter(p => p.kind === 'chunk');
  const reach = analysis.reach, problems = [];
  let verdict;
  if (nicks.length) {
    problems.push(...nicks.map(p => `nick: ${p.area} unit² shaved off the main at ${p.box.join(',')} (deepest ${p.depth}, a knockout reaches ${chunk})`));
  }
  if (!found.length) {
    if (reach !== null && reach < clearMin) problems.push(`tiny clearance: reach ${reach} is inside the cut margin (want ${clearMin} to ${clearMax})`);
    if (reach !== null && reach > clearMax) problems.push(`detached: reach ${reach} floats apart (want ${clearMin} to ${clearMax})`);
    verdict = problems.length ? 'fail' : 'clear';
  } else {
    if (reach !== null && reach > 0) problems.push(`tiny clearance: the sub does not touch the main (reach ${reach}), yet the cut margin erases it; move the main clear to reach ${clearMin} to ${clearMax}, or into the sub`);
    else if (reach !== null && reach > -overlapMin) problems.push(`tiny overlap: the sub only grazes the main (reach ${reach}, want ${-overlapMin} or less for a knockout, or ${clearMin} to ${clearMax} clear)`);
    verdict = problems.length ? 'fail' : 'knockout';
  }
  // A main around the sub (side_overlap.mjs `container`) is a container combination, whatever the contact.
  if (analysis.flags.includes('container')) {
    problems.push(`container: ${analysis.inside_pct}% of the sub's ink lies inside the main's ink box; the main surrounds the sub instead of standing beside it (keep the sub at its corner or side)`);
    verdict = 'fail';
  }
  return {verdict, reach, chunks: chunks.length, nicks: nicks.length,
          patches: found.map(({px, ...rest}) => rest), problems, masks: {n, main, kept, sub: analysis.masks.sub, found}};
}

// contact.png: kept main black, erased chunks red, nicks magenta, sub blue (over everything).
function picture(result, file) {
  const {n, main, kept, sub, found} = result.masks;
  const rgb = Buffer.alloc(n * n * 3, 255);
  const kind = new Uint8Array(n * n);
  for (const p of found) for (const i of p.px) kind[i] = p.kind === 'chunk' ? 1 : 2;
  for (let i = 0; i < n * n; i++) {
    let c = null;
    if (main[i] && !kept[i]) c = kind[i] === 2 ? [230, 0, 200] : [230, 60, 50];
    if (kept[i]) c = [20, 20, 20];
    if (sub[i]) c = [70, 130, 240];
    if (c) rgb.set(c, i * 3);
  }
  // Grow each nick's pixels so a speck shows at a glance.
  for (const p of found.filter(q => q.kind === 'nick')) {
    for (const i of p.px) {
      const x = i % n, y = (i - x) / n;
      for (let dy = -6; dy <= 6; dy++) for (let dx = -6; dx <= 6; dx++) {
        const xx = x + dx, yy = y + dy;
        if (xx < 0 || yy < 0 || xx >= n || yy >= n || dx * dx + dy * dy > 36) continue;
        const j = yy * n + xx;
        if (!kept[j] && !sub[j]) rgb.set([230, 0, 200], j * 3);
      }
    }
  }
  const raw = file + '.ppm';
  try {
    writeFileSync(raw, Buffer.concat([Buffer.from(`P6\n${n} ${n}\n255\n`), rgb]));
    execFileSync('magick', [raw, file], {timeout: 30000});
    return file;
  } catch { return null; } finally { rmSync(raw, {force: true}); }
}

export function checkDir(dir, {current = false, ...limits} = {}) {
  const layout = readJSON(path.join(dir, current ? 'base-layout.json' : 'layout.json'));
  const analysis = analyze(compose(dir, layout), layoutFor(dir, layout));
  const result = contact(analysis, limits);
  result.picture = picture(result, path.join(dir, current ? 'contact-current.png' : 'contact.png'));
  delete result.masks;
  return result;
}

if (process.argv[1] && path.resolve(process.argv[1]) === new URL(import.meta.url).pathname) {
  const args = process.argv.slice(2);
  const valued = new Set(['--clear-min', '--clear-max', '--overlap-min', '--chunk', '--noise', '--speck']);
  const dirs = args.filter((a, i) => !a.startsWith('--') && !valued.has(args[i - 1]));
  const value = name => { const i = args.indexOf('--' + name); return i >= 0 ? Number(args[i + 1]) : undefined; };
  if (!dirs.length) {
    console.error('usage: side_contact_check.mjs <DIR> [<DIR> ...] [--current] [--json] [--clear-min 4] [--clear-max 4.5] [--overlap-min 2] [--chunk 1.5] [--noise 0.25] [--speck 0.1]');
    process.exit(2);
  }
  const options = {current: args.includes('--current'), ...Object.fromEntries(
    [['clearMin', value('clear-min')], ['clearMax', value('clear-max')], ['overlapMin', value('overlap-min')], ['chunk', value('chunk')], ['noise', value('noise')], ['speck', value('speck')]]
      .filter(([, v]) => v !== undefined && Number.isFinite(v)))};
  let failed = 0;
  const results = [];
  for (const dir of dirs) {
    const root = path.resolve(dir);
    try {
      if (!existsSync(path.join(root, 'item.json'))) throw new Error('not a side_layout.mjs work folder (fetch the pair first)');
      const r = checkDir(root, options);
      if (r.verdict === 'fail') failed++;
      results.push({dir: path.basename(root), ...r});
    } catch (e) { failed++; results.push({dir: path.basename(root), verdict: 'error', problems: [e.message]}); }
  }
  if (args.includes('--json')) console.log(JSON.stringify(results, null, 2));
  else for (const r of results) {
    console.log(`${r.verdict === 'fail' || r.verdict === 'error' ? 'FAIL' : 'PASS'} ${r.dir}  ${r.verdict}  reach ${r.reach ?? '-'}  chunks ${r.chunks ?? '-'}  nicks ${r.nicks ?? '-'}`);
    for (const p of r.problems) console.log('     ' + p);
  }
  process.exit(failed ? 1 : 0);
}
