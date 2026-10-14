#!/usr/bin/env node
// Store the AI review fixes on production and put each new version to "ready" in Icon review.
//   - takes every work folder whose review.json is an AI fix (not your "good" marks) not pushed yet;
//   - skips a fix you flagged on the report as "Stored is better" (or "sub too small") for this very review;
//   - pushes with `side_layout.mjs push <dir>` (all its checks: keyshape system, contact, pair unchanged since fetch);
//     when only the shared sub position changed on production (a push of the other size moved it), it adopts the fresh
//     item.json / drawings.json, keeps the fix and pushes again;
//   - then POST /api/reviews {status: ready} on the new version.
// Dry run unless --go. Log: <work>-push-ready.json.
//
//   node icon_set/scripts/side_review_push_ready.mjs [--go]            (SIDE_SIZE=72 for 72)
// Env: PICTOGRAPHIC_SESSION, or PICTOGRAPHIC_ADMIN_USER + PICTOGRAPHIC_ADMIN_PASSWORD.
import {execFile} from 'node:child_process';
import {existsSync, readFileSync, readdirSync, writeFileSync} from 'node:fs';
import path from 'node:path';
import {promisify} from 'node:util';
import {api, itemOf, login} from './side_layout.mjs';
import {SIZE, WORK_NAME} from './side_compose.mjs';

const run = promisify(execFile);
const HERE = path.dirname(new URL(import.meta.url).pathname);
const WORK = path.resolve(HERE, '../work', WORK_NAME);
const FLAGS = path.resolve(HERE, '../work/side-layout-flags', SIZE === 72 ? 'flags-72.json' : 'flags.json');
const LOG = WORK + '-push-ready.json';
const go = process.argv.includes('--go');
const onlyIds = (process.argv.find(a => a.startsWith('--ids=')) || '').slice(6).split(',').filter(Boolean);
const read = f => { try { return JSON.parse(readFileSync(f, 'utf8')); } catch { return null; } };
const write = (f, d) => writeFileSync(f, JSON.stringify(d, null, 2) + '\n');
const box = gs => { const x0 = Math.min(...gs.map(g => g.x)), y0 = Math.min(...gs.map(g => g.y));
  return [x0, y0, Math.max(...gs.map(g => g.x + g.w)) - x0, Math.max(...gs.map(g => g.y + g.h)) - y0]; };

const flags = read(FLAGS) || {};
const todo = [], skipped = {};
const skip = (why, id) => (skipped[why] ||= []).push(id);
for (const id of readdirSync(WORK).sort()) {
  const dir = path.join(WORK, id), r = read(path.join(dir, 'review.json'));
  if (onlyIds.length && !onlyIds.includes(id)) continue;
  if (!r || r.user_marked || r.verdict !== 'fix') continue;
  if (r.result === 'pushed') { skip('already pushed', id); continue; }
  const f = flags[id];
  if (f && ['stored-better', 'sub-too-small'].includes(f.kind) && (!f.review_reviewed_at || f.review_reviewed_at === r.reviewed_at)) { skip(`flagged ${f.kind}`, id); continue; }
  const layout = read(path.join(dir, 'layout.json'));
  if (!layout || !r.after || layout.position !== r.after.position || JSON.stringify(box(layout.main)) !== JSON.stringify(r.after.main)
      || JSON.stringify(box(layout.sub)) !== JSON.stringify(r.after.sub)) { skip('layout.json is not the recorded fix', id); continue; }
  todo.push({id, dir});
}
console.log(JSON.stringify({size: SIZE, to_push: todo.length, skipped: Object.fromEntries(Object.entries(skipped).map(([k, v]) => [k, v.length]))}, null, 1));
if (!go) { console.error('dry run: add --go'); process.exit(0); }

await login();
const session = process.env.PICTOGRAPHIC_SESSION;
const env = {...process.env, SIDE_SIZE: String(SIZE)};
const pushOnce = async dir => {
  try { const {stdout} = await run(process.execPath, [path.join(HERE, 'side_layout.mjs'), 'push', dir], {env, maxBuffer: 1 << 26}); return {ok: true, out: stdout}; }
  catch (e) { return {ok: false, error: (e.stderr || e.message).trim().split('\n').slice(-3).join(' ')}; }
};
const log = read(LOG) || {};
let n = 0;
const counts = {pushed: 0, ready: 0, failed: 0};
async function one({id, dir}) {
  let p = await pushOnce(dir);
  if (!p.ok && /changed on production since fetch/.test(p.error)) {
    // Adopt the fresh pair when only the shared position moved, then push again.
    const old = read(path.join(dir, 'item.json'));
    const fresh = await itemOf(id).catch(() => null);
    const facts = it => JSON.stringify(it.parts.map(q => [q.role, q.icon, q.current_sha, JSON.stringify(q.layout)]));
    if (fresh?.parts && facts(fresh) === facts(old)) { write(path.join(dir, 'item.json'), fresh); p = await pushOnce(dir); }
  }
  const entry = {at: new Date().toISOString()};
  if (!p.ok) { counts.failed++; Object.assign(entry, {result: 'push failed', error: p.error}); }
  else {
    counts.pushed++;
    const res = JSON.parse(p.out.slice(p.out.indexOf('{')));
    const key = read(path.join(dir, 'item.json')).icon.key;
    entry.svg_sha256 = res.svg_sha256;
    try { await api('/api/reviews', {icon: key, svg_sha256: res.svg_sha256, status: 'ready'}); counts.ready++; entry.result = 'pushed + ready'; }
    catch (e) { entry.result = 'pushed, ready failed'; entry.error = e.message; }
    const r = read(path.join(dir, 'review.json'));
    if (r) write(path.join(dir, 'review.json'), {...r, review_status: entry.result === 'pushed + ready' ? 'ready' : null});
  }
  log[id] = entry;
  process.stderr.write(`\r${++n} of ${todo.length}: pushed ${counts.pushed}, ready ${counts.ready}, failed ${counts.failed}`);
}
let i = 0;
await Promise.all(Array.from({length: 4}, async () => { while (i < todo.length) await one(todo[i++]); }));
process.stderr.write('\n');
write(LOG, log);
console.log(JSON.stringify({size: SIZE, ...counts, session: Boolean(session),
  failures: Object.entries(log).filter(([, e]) => e.error).slice(0, 15).map(([id, e]) => `${id}: ${e.result}: ${e.error}`)}, null, 1));
