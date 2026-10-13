#!/usr/bin/env node
// Bring the /side-layout-adjust work folders up to date with production (read-only on production):
//   - a pair whose main or sub was redrawn or re-picked, or whose layout / position changed, gets its folder rebuilt
//     from the current drawings (an earlier review moves to review-history.json as superseded: the parts changed);
//   - a pair that is no longer reviewable (a part not approved now, the pair stale or gone) has its folder moved to
//     <work>-removed/ (kept, not deleted);
//   - a reviewable pair with no folder yet (its parts were approved since) gets one;
//   - every other folder only gets item.json refreshed.
// New and rebuilt folders get fetch.json (as side_prefetch.mjs writes it) and the 2026-10-12 snap block.
//
//   node icon_set/scripts/side_sync_folders.mjs [--dry-run]
//   SIDE_SIZE=72 node icon_set/scripts/side_sync_folders.mjs [--dry-run]
import {existsSync, mkdirSync, readFileSync, readdirSync, renameSync, rmSync, writeFileSync} from 'node:fs';
import path from 'node:path';
import {api, getText, query, savePair, unapprovedParts} from './side_layout.mjs';
import {SIZE, WORK_NAME} from './side_compose.mjs';

const HERE = path.dirname(new URL(import.meta.url).pathname);
const WORK = path.resolve(HERE, '../work', WORK_NAME);
const REMOVED = WORK + '-removed';
const SNAP = path.resolve(HERE, '../work/side-keyshape-snap', String(SIZE), 'pairs');
const dry = process.argv.includes('--dry-run');
const read = f => { try { return JSON.parse(readFileSync(f, 'utf8')); } catch { return null; } };
const write = (f, d) => writeFileSync(f, JSON.stringify(d, null, 2) + '\n');
const facts = (item, drawings) => JSON.stringify({
  parts: item.parts.map(p => [p.role, p.icon, p.current_sha, JSON.stringify(p.layout), p.position]),
  drawings: item.parts.map(p => p.icon && drawings?.[p.icon]?.svg_sha256 || null)});
async function pool(items, n, fn) { let i = 0; await Promise.all(Array.from({length: n}, async () => { while (i < items.length) await fn(items[i++]); })); }

// 1. Production: every built pair of this size, and which are reviewable (both parts picked and approved).
const live = new Map();
for (let offset = 0; offset !== null && offset !== undefined;) {
  const {data} = await api(query({state: 'built', limit: '500', offset: String(offset)}));
  for (const i of data.items) live.set(i.reference_id, i);
  offset = data.items.length ? data.next_offset : null;
  process.stderr.write(`\rlisted ${live.size}`);
}
process.stderr.write('\n');
const reviewable = new Map([...live].filter(([, i]) => i.parts.every(p => p.icon || p.form?.native_text) && !unapprovedParts(i).length));

// 2. The parts' current drawings.
const keys = [...new Set([...reviewable.values()].flatMap(i => i.parts.map(p => p.icon).filter(Boolean)))];
const drawings = {};
for (let i = 0; i < keys.length; i += 100) {
  Object.assign(drawings, (await api('/api/combinations/drawings?keys=' + encodeURIComponent(keys.slice(i, i + 100).join(',')))).data);
  process.stderr.write(`\rdrawings ${Object.keys(drawings).length} of ${keys.length}`);
}
process.stderr.write('\n');
const own = item => Object.fromEntries(item.parts.filter(p => p.icon && drawings[p.icon]).map(p => [p.icon, drawings[p.icon]]));

// 3. Compare every folder with production.
const local = existsSync(WORK) ? readdirSync(WORK).filter(id => existsSync(path.join(WORK, id, 'item.json'))) : [];
const plan = {unchanged: [], rebuild: [], remove: [], create: []};
for (const id of local) {
  const item = reviewable.get(id);
  if (!item) { plan.remove.push({id, why: live.has(id) ? 'a part is not approved now (or not picked)' : 'no longer built (stale or gone)'}); continue; }
  const before = read(path.join(WORK, id, 'item.json')), oldDrawings = read(path.join(WORK, id, 'drawings.json'));
  if (facts(before, oldDrawings) !== facts(item, own(item))) {
    const changed = item.parts.filter(p => { const b = before.parts.find(q => q.role === p.role) || {};
      return b.icon !== p.icon ? true : (oldDrawings?.[p.icon]?.svg_sha256 !== drawings[p.icon]?.svg_sha256) || JSON.stringify(b.layout) !== JSON.stringify(p.layout) || b.position !== p.position; })
      .map(p => { const b = before.parts.find(q => q.role === p.role) || {};
        if (b.icon !== p.icon) return `${p.role} re-picked ${b.icon} → ${p.icon}`;
        if (oldDrawings?.[p.icon]?.svg_sha256 !== drawings[p.icon]?.svg_sha256) return `${p.role} ${p.icon} drawing changed`;
        return `${p.role} layout changed`; });
    plan.rebuild.push({id, item, why: changed.join('; ') || 'layout or position changed'});
  } else plan.unchanged.push({id, item});
}
for (const [id, item] of reviewable) if (!local.includes(id)) plan.create.push({id, item, why: 'reviewable now, no folder yet'});
console.log(JSON.stringify({size: SIZE, folders: local.length, reviewable: reviewable.size,
  unchanged: plan.unchanged.length, rebuild: plan.rebuild.length, remove: plan.remove.length, create: plan.create.length,
  examples: {rebuild: plan.rebuild.slice(0, 5).map(x => `${x.id}: ${x.why}`), remove: plan.remove.slice(0, 5).map(x => `${x.id}: ${x.why}`)}}, null, 1));
if (dry) process.exit(0);

// 4. Apply.
for (const {id, item} of plan.unchanged) write(path.join(WORK, id, 'item.json'), item);
mkdirSync(REMOVED, {recursive: true});
for (const {id, why} of plan.remove) {
  const to = path.join(REMOVED, id);
  rmSync(to, {recursive: true, force: true});
  renameSync(path.join(WORK, id), to);
  write(path.join(to, 'removed.json'), {removed_at: new Date().toISOString(), why});
}
const jobs = [...plan.rebuild.map(x => ({...x, kind: 'rebuild'})), ...plan.create.map(x => ({...x, kind: 'create'}))];
const counts = {ok: 0, error: 0}, errors = [];
await pool(jobs, 6, async ({id, item, kind, why}) => {
  const dir = path.join(WORK, id), tmp = path.join(WORK, '.sync', id);
  try {
    const stored = item.icon?.preview_url ? await getText(item.icon.preview_url) : null;
    rmSync(tmp, {recursive: true, force: true});
    const summary = savePair(tmp, item, own(item), stored);
    // Earlier reviews: the old history, and a review of the old parts as superseded.
    let history = [], keep = null;
    if (existsSync(dir)) {
      history = read(path.join(dir, 'review-history.json')) || [];
      const r = read(path.join(dir, 'review.json'));
      // A pushed fix changes the stored layout itself: when the only change is the layout and it now holds the boxes the
      // review recorded, the review stays (it is the reason for the change), else it moves to the history.
      const after = r?.after, b = summary.metrics ? read(path.join(tmp, 'base-layout.json')) : null;
      const box = gs => { const x0 = Math.min(...gs.map(g => g.x)), y0 = Math.min(...gs.map(g => g.y));
        return [x0, y0, Math.max(...gs.map(g => g.x + g.w)) - x0, Math.max(...gs.map(g => g.y + g.h)) - y0]; };
      const same = after && b && r.result === 'pushed' && b.position === after.position &&
        JSON.stringify(box(b.main)) === JSON.stringify(after.main) && JSON.stringify(box(b.sub)) === JSON.stringify(after.sub);
      if (same && !/drawing changed|re-picked/.test(why)) keep = r;
      else if (r && !history.some(h => h.reviewed_at === r.reviewed_at)) history.push({...r, superseded: `parts changed on production: ${why}`});
    }
    if (history.length) write(path.join(tmp, 'review-history.json'), history);
    if (keep) write(path.join(tmp, 'review.json'), keep);
    const s = read(path.join(SNAP, id, 'snap.json'));
    const snap = s ? {class: s.class, keyshape: s.keyshape ?? null, move: s.move ?? null, pushed_at: s.pushed_at ?? null, new_flags: s.after?.new_flags ?? [],
      contact_before: s.before?.contact ?? null, contact_after: s.after?.contact ?? null} : null;
    write(path.join(tmp, 'fetch.json'), {...summary, dir, ...(snap ? {snap} : {}), synced: {at: new Date().toISOString(), kind, why}});
    rmSync(dir, {recursive: true, force: true});
    renameSync(tmp, dir);
    counts.ok++;
  } catch (e) { counts.error++; errors.push(`${id}: ${e.message}`); rmSync(tmp, {recursive: true, force: true}); }
  process.stderr.write(`\rbuilt ${counts.ok + counts.error} of ${jobs.length}`);
});
rmSync(path.join(WORK, '.sync'), {recursive: true, force: true});
process.stderr.write('\n');
console.log(JSON.stringify({applied: true, ...counts, errors: errors.slice(0, 10)}));
