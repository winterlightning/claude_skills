#!/usr/bin/env node
// Push snapped side pairs (side_keyshape_snap.mjs) to production: each pair is rebuilt with its snapped layout through
// POST /api/combinations/build, the way the side page's Save layout stores it, carrying the canvas keyshape the engine
// found (request.keyshape), so Icon review shows the combined icon's keyshape instead of "Keyshape unavailable".
//
//   node icon_set/scripts/side_keyshape_snap_push.mjs [--classes snapped-ok,already-fits] [--ids a,b] [--limit N]
//        [--batch 25] [--go]
//   SIDE_SIZE=72 node icon_set/scripts/side_keyshape_snap_push.mjs ...
//
// Dry run unless --go: lists what would be pushed and why the rest is skipped. Skipped: pairs of other classes,
// pairs snapped with an older drawing (production only takes a part's current drawing), pairs whose engine keyshape
// is missing, and pairs changed on production since the snap (re-run the snap for those). --go needs
// PICTOGRAPHIC_ADMIN_USER + PICTOGRAPHIC_ADMIN_PASSWORD (or PICTOGRAPHIC_SESSION). Each pushed pair gets
// pushed_at / pushed_sha256 in its snap.json; every result is appended to push-log.jsonl.
import {appendFileSync, existsSync, readFileSync, writeFileSync} from 'node:fs';
import path from 'node:path';
import {api, login, query} from './side_layout.mjs';
import {SIZE, compose} from './side_compose.mjs';

const HERE = path.dirname(new URL(import.meta.url).pathname);
const OUT = path.resolve(HERE, '../work/side-keyshape-snap', String(SIZE));
const readJSON = file => JSON.parse(readFileSync(file, 'utf8'));
const facts = item => JSON.stringify(item.parts.map(p => [p.role, p.icon, p.current_sha, JSON.stringify(p.layout), p.position]));

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

async function productionItems() {
  const items = new Map();
  for (const state of ['built', 'stale']) {
    for (let offset = 0; offset !== null && offset !== undefined;) {
      const {data} = await api(query({state, limit: '500', offset: String(offset)}));
      for (const i of data.items) items.set(i.reference_id, i);
      offset = data.items.length ? data.next_offset : null;
    }
  }
  return items;
}

async function main(opts) {
  const classes = new Set(String(opts.classes || 'snapped-ok,already-fits').split(','));
  const cached = readJSON(path.join(OUT, 'cache/items.json'));
  let ids = cached.map(i => i.reference_id);
  if (opts.ids) { const want = new Set(String(opts.ids).split(',')); ids = ids.filter(id => want.has(id)); }
  const skipped = {}, skip = (why, id) => { (skipped[why] ??= []).push(id); };
  const now = await productionItems();
  const cachedById = new Map(cached.map(i => [i.reference_id, i]));
  const ready = [];
  for (const id of ids) {
    const dir = path.join(OUT, 'pairs', id), f = path.join(dir, 'snap.json');
    if (!existsSync(f)) { skip('not snapped', id); continue; }
    const snap = readJSON(f);
    if (!classes.has(snap.class)) { skip(`class ${snap.class}`, id); continue; }
    if (snap.built_drawing) { skip('snapped with an older drawing (fix the part first)', id); continue; }
    if (snap.pushed_at && !opts.again) { skip('already pushed', id); continue; }
    const live = now.get(id);
    if (!live || facts(live) !== facts(cachedById.get(id))) { skip('changed on production since the snap', id); continue; }
    const {request} = compose(dir, readJSON(path.join(dir, 'layout.json')));
    if (!request.keyshape) { skip('engine finds no keyshape', id); continue; }
    ready.push({id, dir, snap, request});
    if (opts.limit && ready.length >= Number(opts.limit)) break;
  }
  const byKeyshape = ready.reduce((m, r) => { m[r.request.keyshape] = (m[r.request.keyshape] || 0) + 1; return m; }, {});
  console.log(JSON.stringify({size: SIZE, to_push: ready.length, by_keyshape: byKeyshape,
                              skipped: Object.fromEntries(Object.entries(skipped).map(([k, v]) => [k, v.length])), go: !!opts.go}, null, 2));
  if (!opts.go) { console.error('dry run: add --go to push'); return; }

  await login();
  const batch = Number(opts.batch || 25), log = path.join(OUT, 'push-log.jsonl');
  let ok = 0, failed = 0;
  for (let i = 0; i < ready.length; i += batch) {
    const chunk = ready.slice(i, i + batch);
    let results;
    try { results = (await api('/api/combinations/build', {size: SIZE, builds: chunk.map(r => r.request)})).data.results; }
    catch (e) { results = chunk.map(r => ({reference_id: r.id, ok: false, error: e.message})); }
    const at = new Date().toISOString();
    for (const res of results) {
      const r = chunk.find(c => c.id === res.reference_id);
      appendFileSync(log, JSON.stringify({at, size: SIZE, keyshape: r?.request.keyshape, ...res}) + '\n');
      if (res.ok && r) {
        ok++;
        writeFileSync(path.join(r.dir, 'snap.json'), JSON.stringify({...r.snap, pushed_at: at, pushed_sha256: res.svg_sha256, pushed_keyshape: r.request.keyshape}, null, 2) + '\n');
      } else { failed++; console.error(`failed ${res.reference_id}: ${res.error || (res.errors || []).join('; ')}`); }
    }
    process.stderr.write(`\rpushed ${ok}, failed ${failed} of ${ready.length}`);
  }
  process.stderr.write('\n');
}

try { await main(options(process.argv.slice(2))); } catch (e) { console.error('error: ' + e.message); process.exit(1); }
