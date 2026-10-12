#!/usr/bin/env node
// Which reviewed side pairs does a combine-engine change affect? Composes every reviewed pair's stored layout and its
// recorded result (the fix proposal, else stored) with an OLD copy of combine-side.js and with the current one, and
// measures (side_overlap + contact, current engine) every pair whose picture changed. Local only.
//
//   SIDE_SIZE=72 node icon_set/scripts/side_engine_scan.mjs --old <old combine-side.js> [--out icon_set/work/side-engine-scan]
//   → <out>/scan-<size>.json and <out>/img/<size>/<id>-{old,new}.png for the changed pairs
import {existsSync, mkdirSync, readdirSync, writeFileSync} from 'node:fs';
import {createRequire} from 'node:module';
import {execFileSync} from 'node:child_process';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {SIZE, WORK_NAME, Side, drawingMap, layoutFor, readJSON} from './side_compose.mjs';
import {analyze, summary} from './side_overlap.mjs';
import {contact} from './side_contact_check.mjs';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const args = process.argv.slice(2), opt = n => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : undefined; };
if (!opt('--old')) { console.error('usage: side_engine_scan.mjs --old <old combine-side.js>'); process.exit(2); }
const Old = createRequire(import.meta.url)(path.resolve(opt('--old')));
const OUT = path.resolve(opt('--out') || path.join(ROOT, 'icon_set/work/side-engine-scan'));
const IMG = path.join(OUT, 'img', String(SIZE));
mkdirSync(IMG, {recursive: true});
const WORK = path.join(ROOT, 'icon_set/work', WORK_NAME);

const rows = [];
let n = 0;
for (const id of readdirSync(WORK).sort()) {
  const dir = path.join(WORK, id);
  if (!existsSync(path.join(dir, 'review.json')) || !existsSync(path.join(dir, 'base-layout.json'))) continue;
  const review = readJSON(path.join(dir, 'review.json')), base = readJSON(path.join(dir, 'base-layout.json'));
  const item = readJSON(path.join(dir, 'item.json')), drawings = drawingMap(readJSON(path.join(dir, 'drawings.json')));
  const result = review.verdict === 'fix' && existsSync(path.join(dir, 'layout.json')) ? readJSON(path.join(dir, 'layout.json')) : base;
  const run = (engine, layout) => engine.pairRequest(item, drawings, {position: layout.position, layout: layoutFor(dir, layout), size: SIZE});
  const row = {id, concept: review.concept, verdict: review.verdict, keep_stored: !!review.keep_stored};
  try {
    const so = run(Old, base).svg, sn = run(Side, base).svg;
    const ro = result === base ? so : run(Old, result).svg, rn = result === base ? sn : run(Side, result).svg;
    row.stored_changed = so !== sn; row.result_changed = ro !== rn;
    if (row.stored_changed || row.result_changed) {
      const m = composed => { const a = analyze(composed, layoutFor(dir, result)); const s = summary(a), c = contact(a);
        return {flags: s.flags, reach: s.reach, erased: s.erased_pct, contact: c.verdict, problems: c.problems, lost_parts: s.parts.lost}; };
      row.after = m(run(Side, result));
      row.before_review = {flags: review.after?.flags || review.before?.flags || [], contact: review.after?.contact || review.before?.contact};
      for (const [tag, svg] of [['old', ro], ['new', rn]]) {
        const f = path.join(IMG, `${id}-${tag}.svg`);
        writeFileSync(f, svg);
        execFileSync('rsvg-convert', ['-w', '200', '-h', '200', '-b', 'white', '-o', f.replace(/\.svg$/, '.png'), f]);
      }
      rows.push(row);
    }
  } catch (e) { rows.push({...row, error: e.message}); }
  if (++n % 250 === 0) process.stderr.write(`\r${n}`);
}
writeFileSync(path.join(OUT, `scan-${SIZE}.json`), JSON.stringify({size: SIZE, scanned: n, rows}, null, 1));
const bad = rows.filter(r => r.after && r.after.contact === 'fail');
console.log(`\n${SIZE}: ${n} reviewed pairs, ${rows.filter(r => !r.error).length} change with the new engine, ${bad.length} of them now fail contact, ${rows.filter(r => r.error).length} errors`);
