#!/usr/bin/env node
// Refresh a side-overlap audit run from production: every side pair's current main and sub drawings, its layout and
// its stored combined icon, downloaded again and re-measured, so the review page shows what production holds now
// (people keep editing the main and sub icons there).
//
//   node icon_set/scripts/side_audit_refresh.mjs icon_set/work/side-overlap-audit/<run> [--force] [--jobs 8] [--limit N]
//
// 1. Lists every built and stale 64 side pair (a stale pair's main or sub was redrawn after it was built).
// 2. Downloads the pairs' main and sub drawings (100 keys a request) and each changed pair's stored icon.
// 3. Rewrites pairs/<id>/ from scratch for every pair whose part, layout, drawing or stored icon changed since the
//    last refresh (all of them with --force), the same files side_layout.mjs fetch writes, plus pairs/<id>.json (the
//    fetch summary), <id>.overlap.json (side_overlap.mjs) and <id>.rebuild.json (what a rebuild with the local engine
//    changes). Unchanged pairs only get item.json rewritten (the parts' Icon review). Pairs gone from production (or now unbuilt) are deleted.
// 4. Rewrites sample.txt and all.tsv, lists in changed-since-review.txt the pairs /side-layout-adjust reviewed whose
//    parts changed since, writes refresh.json, and rebuilds the page with the run's review.py.
//
// Nothing is written to production. --limit takes the first N pairs only (for a test run into another folder).
import {spawn, execFileSync} from 'node:child_process';
import {existsSync, mkdirSync, readFileSync, readdirSync, rmSync, writeFileSync} from 'node:fs';
import path from 'node:path';
import {api, getText, query, savePair} from './side_layout.mjs';
import {Side} from './side_compose.mjs';

const HERE = path.dirname(new URL(import.meta.url).pathname);
const ADJUST = path.resolve(HERE, '../work/side-layout-adjust');
const PYTHON = existsSync('/opt/homebrew/bin/python3') ? '/opt/homebrew/bin/python3' : 'python3';
const PAGE = 500, KEYS = 100, DOWNLOADS = 6;

function fail(message) { console.error('error: ' + message); process.exit(1); }
const readJSON = file => JSON.parse(readFileSync(file, 'utf8'));
const part = (item, role) => item.parts.find(p => p.role === role) || {role};
// What makes a pair's folder out of date: its picked parts, their drawings, the layout and position, the stored icon.
const facts = (item, drawings) => JSON.stringify({
  parts: item.parts.map(p => [p.role, p.icon, p.current_sha, JSON.stringify(p.layout), p.position]),
  drawings: item.parts.map(p => p.icon && drawings[p.icon]?.svg_sha256), icon: item.icon?.svg_sha256 || null});
const partFacts = item => JSON.stringify(item.parts.map(p => [p.role, p.icon, p.current_sha, JSON.stringify(p.layout), p.position]));

// Each worker process rebuilds the folders listed in its job file (CPU bound: the overlap raster and the PNGs).
async function work(jobFile) {
  for (const {id, dir, item, drawings, stored} of readJSON(jobFile)) {
    try {
      rmSync(dir, {recursive: true, force: true});
      for (const ext of ['.json', '.overlap.json', '.rebuild.json', '.err']) rmSync(dir + ext, {force: true});
      const summary = savePair(dir, item, drawings, stored);
      writeFileSync(dir + '.json', JSON.stringify(summary, null, 2) + '\n');
      writeFileSync(dir + '.overlap.json', JSON.stringify(summary.overlap));
      writeFileSync(dir + '.rebuild.json', JSON.stringify({change: summary.rebuild_change ?? 'main'}));
      writeFileSync(path.join(dir, '.facts'), facts(item, drawings));
      console.log('ok\t' + id);
    } catch (e) {
      writeFileSync(dir + '.err', String(e.message) + '\n');
      console.log('error\t' + id + '\t' + e.message);
    }
  }
}

async function pool(items, size, fn) {
  let next = 0;
  await Promise.all(Array.from({length: size}, async () => { while (next < items.length) await fn(items[next++]); }));
}

async function refresh(run, opts) {
  const pairsDir = path.join(run, 'pairs');
  mkdirSync(pairsDir, {recursive: true});
  const started = Date.now();

  // 1. Every built and stale pair, with its parts' forms.
  let items = [];
  for (const state of ['built', 'stale']) {
    for (let offset = 0; offset !== null && offset !== undefined;) {
      const {data} = await api(query({state, limit: String(PAGE), offset: String(offset)}));
      items.push(...data.items);
      offset = data.next_offset;
      process.stderr.write(`\rlisted ${items.length}`);
    }
  }
  const unpicked = items.filter(i => !i.parts.every(p => p.icon || p.form?.native_text)).length;
  items = items.filter(i => i.parts.every(p => p.icon || p.form?.native_text));
  items.sort((a, b) => a.reference_id.localeCompare(b.reference_id));
  if (opts.limit) items = items.slice(0, Number(opts.limit));
  process.stderr.write(`\rlisted ${items.length} pairs (${unpicked} with a part not picked, skipped)\n`);

  // 2. Their drawings, many keys a request.
  const keys = [...new Set(items.flatMap(i => i.parts.map(p => p.icon).filter(Boolean)))];
  const drawings = {};
  const batches = [];
  for (let i = 0; i < keys.length; i += KEYS) batches.push(keys.slice(i, i + KEYS));
  await pool(batches, 3, async batch => {
    Object.assign(drawings, (await api('/api/combinations/drawings?keys=' + encodeURIComponent(batch.join(',')))).data);
    process.stderr.write(`\rdrawings ${Object.keys(drawings).length} of ${keys.length}`);
  });
  process.stderr.write('\n');

  // 3. The pairs whose folder is out of date, with their stored icons.
  const jobs = [];
  let unchanged = 0;
  for (const item of items) {
    const id = item.reference_id, dir = path.join(pairsDir, id);
    const own = Object.fromEntries(item.parts.filter(p => p.icon && drawings[p.icon]).map(p => [p.icon, drawings[p.icon]]));
    const factsFile = path.join(dir, '.facts');
    if (!opts.force && existsSync(factsFile) && readFileSync(factsFile, 'utf8') === facts(item, own) && existsSync(dir + '.json')) {
      // The drawings are the same, but a part's Icon review may have changed: the page leaves out pairs whose main
      // or sub is not approved, so keep item.json current.
      writeFileSync(path.join(dir, 'item.json'), JSON.stringify(item, null, 2) + '\n');
      unchanged++; continue;
    }
    jobs.push({id, dir, item, drawings: own, stored: null});
  }
  let got = 0;
  await pool(jobs, DOWNLOADS, async job => {
    if (job.item.icon?.preview_url) {
      try { job.stored = await getText(job.item.icon.preview_url); }
      catch { job.stored = await getText(job.item.icon.preview_url); }
    }
    process.stderr.write(`\rstored icons ${++got} of ${jobs.length}`);
  });
  process.stderr.write(`\n${jobs.length} pairs to rebuild, ${unchanged} unchanged\n`);

  // Rebuild them in parallel worker processes.
  const counts = {ok: 0, error: 0};
  const errors = [];
  if (jobs.length) {
    const n = Math.max(1, Math.min(Number(opts.jobs || 8), jobs.length));
    const tmp = path.join(run, '.refresh');
    mkdirSync(tmp, {recursive: true});
    let done = 0;
    await Promise.all(Array.from({length: n}, (_, w) => new Promise((resolve, reject) => {
      const file = path.join(tmp, `job-${w}.json`);
      writeFileSync(file, JSON.stringify(jobs.filter((_, i) => i % n === w)));
      const child = spawn(process.execPath, [new URL(import.meta.url).pathname, '--work', file], {stdio: ['ignore', 'pipe', 'inherit']});
      let buffer = '';
      child.stdout.on('data', chunk => {
        buffer += chunk;
        let at;
        while ((at = buffer.indexOf('\n')) >= 0) {
          const [status, id, message] = buffer.slice(0, at).split('\t');
          buffer = buffer.slice(at + 1);
          if (status !== 'ok' && status !== 'error') continue;
          counts[status]++;
          if (status === 'error') errors.push(`${id}\t${message}`);
          process.stderr.write(`\rrebuilt ${++done} of ${jobs.length}`);
        }
      });
      child.on('exit', code => code === 0 ? resolve() : reject(Error(`worker ${w} exited ${code}`)));
    })));
    rmSync(tmp, {recursive: true, force: true});
    process.stderr.write('\n');
  }

  // Folders of pairs production no longer lists.
  const ids = new Set(items.map(i => i.reference_id));
  let removed = 0;
  if (!opts.limit) {
    for (const name of readdirSync(pairsDir)) {
      const id = name.replace(/\.(overlap\.json|rebuild\.json|json|err)$/, '');
      if (!ids.has(id)) { rmSync(path.join(pairsDir, name), {recursive: true, force: true}); if (name === id) removed++; }
    }
  }

  // 4. The run's lists, the reviews that are out of date, and the page.
  writeFileSync(path.join(run, 'sample.txt'), items.map(i => i.reference_id).join('\n') + '\n');
  writeFileSync(path.join(run, 'all.tsv'), items.map(i => [i.reference_id, part(i, 'sub').position || '-',
    Side.handLayout(i) ? 'hand' : 'auto', i.icon?.review || '-', part(i, 'main').icon || '-',
    part(i, 'sub').icon || '(text)', i.concept, i.state].join('\t')).join('\n') + '\n');
  const changedSinceReview = [];
  for (const item of items) {
    const reviewed = path.join(ADJUST, item.reference_id);
    if (!existsSync(path.join(reviewed, 'review.json')) || !existsSync(path.join(reviewed, 'item.json'))) continue;
    if (partFacts(readJSON(path.join(reviewed, 'item.json'))) !== partFacts(item)) changedSinceReview.push(`${item.reference_id}\t${item.concept}`);
  }
  writeFileSync(path.join(run, 'changed-since-review.txt'), changedSinceReview.map(l => l + '\n').join(''));
  const report = {refreshed_at: new Date().toISOString(), seconds: Math.round((Date.now() - started) / 1000),
                  pairs: items.length, built: items.filter(i => i.state === 'built').length,
                  stale: items.filter(i => i.state === 'stale').length, rebuilt: counts.ok, failed: counts.error,
                  unchanged, removed, changed_since_review: changedSinceReview.length, errors};
  writeFileSync(path.join(run, 'refresh.json'), JSON.stringify(report, null, 2) + '\n');
  if (existsSync(path.join(run, 'review.py'))) execFileSync(PYTHON, [path.join(run, 'review.py')], {stdio: 'inherit'});
  console.log(JSON.stringify({...report, errors: errors.length}, null, 2));
}

const args = process.argv.slice(2);
const opts = {};
const positional = [];
for (let i = 0; i < args.length; i++) {
  if (!args[i].startsWith('--')) { positional.push(args[i]); continue; }
  const name = args[i].slice(2), value = args[i + 1];
  if (value === undefined || value.startsWith('--')) opts[name] = true;
  else { opts[name] = value; i++; }
}
try {
  if (opts.work) await work(opts.work);
  else if (positional[0]) await refresh(path.resolve(positional[0]), opts);
  else fail('usage: side_audit_refresh.mjs <run folder> [--force] [--jobs 8] [--limit N]');
} catch (e) { fail(e.message); }
