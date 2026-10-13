#!/usr/bin/env node
// Download every unreviewed side pair's work folder in one go, so /side-layout-adjust(-72) windows skip
// `side_layout.mjs fetch` and start from the local folder. Read-only: nothing is written to production.
//
//   SIDE_SIZE=72 node icon_set/scripts/side_prefetch.mjs [--jobs 6] [--limit N] [--skip-ids file]
//
// Writes the same files `side_layout.mjs fetch` writes (savePair) plus fetch.json, the summary fetch prints
// (rebuild_change, overlap flags, metrics). Skips pairs that already have a folder (being reviewed or done), pairs
// with an unapproved part, and the ids listed in --skip-ids (the ones running windows hold).
import {spawn} from 'node:child_process';
import {existsSync, mkdirSync, readFileSync, readdirSync, renameSync, rmSync, writeFileSync} from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {api, getText, query, savePair, unapprovedParts} from './side_layout.mjs';
import {WORK_NAME} from './side_compose.mjs';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const WORK = path.join(ROOT, 'icon_set/work', WORK_NAME);
const args = process.argv.slice(2);
const opt = (n, d) => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : d; };
const PAGE = 500, KEYS = 100, DOWNLOADS = 6;

async function pool(items, size, fn) {
  let next = 0;
  await Promise.all(Array.from({length: size}, async () => { while (next < items.length) await fn(items[next++]); }));
}

// Worker: build the folders in a job file. A folder that appeared meanwhile (a window fetched it) is left alone.
if (opt('--work')) {
  for (const {id, item, drawings, stored} of JSON.parse(readFileSync(opt('--work'), 'utf8'))) {
    const dir = path.join(WORK, id);
    if (existsSync(dir)) { console.log('skip\t' + id); continue; }
    const tmp = path.join(WORK, '.prefetch', id);
    try {
      rmSync(tmp, {recursive: true, force: true});
      const summary = savePair(tmp, item, drawings, stored);
      writeFileSync(path.join(tmp, 'fetch.json'), JSON.stringify({...summary, dir}, null, 2) + '\n');
      if (existsSync(dir)) { rmSync(tmp, {recursive: true, force: true}); console.log('skip\t' + id); continue; }
      // Built in a temp folder and moved in whole, so a window never sees a half-written folder.
      renameSync(tmp, dir);
      console.log('ok\t' + id);
    } catch (e) {
      rmSync(tmp, {recursive: true, force: true});
      console.log('error\t' + id + '\t' + String(e.message).replace(/\s+/g, ' '));
    }
  }
  process.exit(0);
}

const started = Date.now();
const skip = new Set(opt('--skip-ids') && existsSync(opt('--skip-ids')) ? readFileSync(opt('--skip-ids'), 'utf8').split(/\s+/).filter(Boolean) : []);
let items = [];
for (let offset = 0; offset !== null && offset !== undefined;) {
  const {data} = await api(query({state: 'built', limit: String(PAGE), offset: String(offset)}));
  items.push(...data.items);
  offset = data.items.length ? data.next_offset : null;
  process.stderr.write(`\rlisted ${items.length}`);
}
const have = new Set(readdirSync(WORK));
const counts = {listed: items.length, have_folder: 0, unapproved: 0, unpicked: 0, held: 0};
items = items.filter(i => {
  if (have.has(i.reference_id)) return counts.have_folder++, false;
  if (skip.has(i.reference_id)) return counts.held++, false;
  if (!i.parts.every(p => p.icon || p.form?.native_text)) return counts.unpicked++, false;
  if (unapprovedParts(i).length) return counts.unapproved++, false;
  return true;
}).sort((a, b) => a.reference_id.localeCompare(b.reference_id));
if (opt('--limit')) items = items.slice(0, Number(opt('--limit')));
process.stderr.write(`\n${JSON.stringify(counts)} → ${items.length} to download\n`);

const keys = [...new Set(items.flatMap(i => i.parts.map(p => p.icon).filter(Boolean)))];
const drawings = {};
const batches = [];
for (let i = 0; i < keys.length; i += KEYS) batches.push(keys.slice(i, i + KEYS));
await pool(batches, 3, async batch => {
  Object.assign(drawings, (await api('/api/combinations/drawings?keys=' + encodeURIComponent(batch.join(',')))).data);
  process.stderr.write(`\rdrawings ${Object.keys(drawings).length} of ${keys.length}`);
});
process.stderr.write('\n');

const jobs = items.map(item => ({id: item.reference_id, item, stored: null,
  drawings: Object.fromEntries(item.parts.filter(p => p.icon && drawings[p.icon]).map(p => [p.icon, drawings[p.icon]]))}));
let got = 0;
await pool(jobs, DOWNLOADS, async job => {
  const url = job.item.icon?.preview_url;
  if (url) {
    try { job.stored = await getText(url); } catch { try { job.stored = await getText(url); } catch {} }
  }
  process.stderr.write(`\rstored icons ${++got} of ${jobs.length}`);
});
process.stderr.write('\n');

const tmp = path.join(WORK, '.prefetch');
mkdirSync(tmp, {recursive: true});
const n = Math.max(1, Math.min(Number(opt('--jobs', Math.max(2, Math.floor(os.cpus().length / 2)))), jobs.length));
const result = {ok: 0, skip: 0, error: 0}, errors = [];
let done = 0;
await Promise.all(Array.from({length: n}, (_, w) => new Promise(resolve => {
  const file = path.join(tmp, `job-${w}.json`);
  writeFileSync(file, JSON.stringify(jobs.filter((_, i) => i % n === w)));
  const child = spawn(process.execPath, [fileURLToPath(import.meta.url), '--work', file], {stdio: ['ignore', 'pipe', 'inherit'], env: process.env});
  let buf = '';
  child.stdout.on('data', d => {
    buf += d;
    let at;
    while ((at = buf.indexOf('\n')) >= 0) {
      const [status, id, message] = buf.slice(0, at).split('\t');
      buf = buf.slice(at + 1);
      if (!(status in result)) continue;
      result[status]++;
      if (status === 'error') errors.push(`${id}\t${message}`);
      process.stderr.write(`\rbuilt ${++done} of ${jobs.length}`);
    }
  });
  child.on('close', () => { rmSync(file, {force: true}); resolve(); });
})));
if (errors.length) writeFileSync(path.join(tmp, 'errors.tsv'), errors.join('\n') + '\n');
console.log(`\n${JSON.stringify(result)} in ${((Date.now() - started) / 1000).toFixed(0)} s` + (errors.length ? ` · errors in ${path.join(tmp, 'errors.tsv')}` : ''));
