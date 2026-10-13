#!/usr/bin/env node
// Find side pairs laid out as container combinations (/side-layout-adjust): the main surrounds the sub (a hierarchy
// inside a head, a remote standing in a house's doorway) instead of the sub sitting at its corner or side.
//
//   node icon_set/scripts/side_container_scan.mjs [<DIR> ...] [--container 80] [--json]
//
// Without DIRs it scans every reviewed folder in icon_set/work/side-layout-adjust. Each folder is measured twice:
// the stored layout (base-layout.json) and, for a `fix` review, the proposal (layout.json). A layout is a container
// when side_overlap.mjs flags it (inside_pct, the share of the sub's ink inside the uncut main's ink box, at or over
// --container). Lists every hit with its verdict; exits 1 when any reviewed `ok` or `fix` is a container.
import {existsSync, readdirSync} from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {compose, layoutFor, readJSON} from './side_compose.mjs';
import {analyze} from './side_overlap.mjs';

const WORK = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../work/side-layout-adjust');
const args = process.argv.slice(2);
const opt = name => { const i = args.indexOf('--' + name); return i >= 0 ? args[i + 1] : undefined; };
const limits = opt('container') ? {container: Number(opt('container'))} : {};
const valueArgs = new Set(['--container']);
const named = args.filter((a, i) => !a.startsWith('--') && !valueArgs.has(args[i - 1]));
const dirs = named.length ? named.map(d => path.resolve(d))
  : readdirSync(WORK).map(d => path.join(WORK, d)).filter(d => existsSync(path.join(d, 'review.json')));

const measure = (dir, layout) => {
  const a = analyze(compose(dir, layout), layoutFor(dir, layout), limits);
  return {container: a.flags.includes('container'), inside_pct: a.inside_pct};
};
const hits = [];
for (const dir of dirs) {
  try {
    const base = readJSON(path.join(dir, 'base-layout.json')), layout = readJSON(path.join(dir, 'layout.json'));
    const review = existsSync(path.join(dir, 'review.json')) ? readJSON(path.join(dir, 'review.json')) : null;
    const stored = measure(dir, {position: base.position, main: base.main, sub: base.sub});
    const proposal = review?.verdict === 'fix' ? measure(dir, layout) : null;
    if (stored.container || proposal?.container)
      hits.push({dir: path.basename(dir), concept: readJSON(path.join(dir, 'item.json')).concept, verdict: review?.verdict ?? null,
                 stored_inside_pct: stored.inside_pct, proposal_inside_pct: proposal?.inside_pct ?? null,
                 // what is wrong: a proposal that builds a container, or a stored container recorded ok
                 wrong: (review?.verdict === 'fix' && proposal.container) || (review?.verdict === 'ok' && stored.container)});
  } catch (e) { console.error(`${path.basename(dir)}: ${e.message}`); }
}
if (args.includes('--json')) console.log(JSON.stringify(hits, null, 2));
else {
  for (const h of hits)
    console.log(`${h.wrong ? 'WRONG' : '     '} ${h.dir}  ${h.verdict ?? '-'}  stored ${h.stored_inside_pct}%  proposal ${h.proposal_inside_pct ?? '-'}%  ${h.concept}`);
  console.log(`${hits.length} container layouts in ${dirs.length} folders, ${hits.filter(h => h.wrong).length} reviewed wrong`);
}
process.exit(hits.some(h => h.wrong) ? 1 : 0);
