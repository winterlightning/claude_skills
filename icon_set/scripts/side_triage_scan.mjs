#!/usr/bin/env node
// Score every recorded side review (/side-layout-adjust) for the triage page, without an agent: the stored layout and
// the AI's final layout (the proposal for a fix, the stored one otherwise) are each composed and measured with
// side_overlap.mjs (including lost_feature) and side_contact_check.mjs, and the pair gets a suspicion score with reasons.
//
//   node icon_set/scripts/side_triage_scan.mjs [--since 2026-10-09] [--jobs 8] [--ids a,b]   (--ids merges into triage.json)
//   → icon_set/work/side-triage/triage.json, final/<id>.png (the AI result as recorded)
//
// A fix's layout is rebuilt from request.json (written with the proposal) and checked against the boxes recorded in
// review.json; layout.json is the fallback. A pair whose recorded layout cannot be rebuilt is marked `unverified`.
import {execFileSync, spawn} from 'node:child_process';
import {existsSync, mkdirSync, readdirSync, writeFileSync} from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {PARTS, SIZE, Side, WORK_NAME, compose, layoutFor, readJSON} from './side_compose.mjs';
import {analyze, summary} from './side_overlap.mjs';
import {contact} from './side_contact_check.mjs';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const WORK = path.join(ROOT, 'icon_set/work', WORK_NAME);
const OUT = path.join(ROOT, 'icon_set/work', SIZE === 72 ? 'side-triage-72' : 'side-triage');
const args = process.argv.slice(2);
const opt = (n, d) => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : d; };
const SINCE = opt('--since', '2026-10-09');
const JOBS = Number(opt('--jobs', Math.max(2, os.cpus().length - 2)));
const CHUNK = opt('--chunk');

const size = k => Number(String(k || '').match(/ at (\d+)$/)?.[1]) || null;
const near = (a, b) => a && b && a.every((v, i) => Math.abs(v - b[i]) <= 0.6);
const boxOf = groups => { const b = Side.groupsBox(groups); return [b.x, b.y, b.w, b.h]; };

function measure(dir, layout) {
  const composed = compose(dir, layout);
  const a = analyze(composed, layoutFor(dir, layout)), s = summary(a), c = contact(a);
  return {svg: composed.svg, flags: s.flags, penalty: s.penalty, reach: s.reach, erased: s.erased_pct,
          lost_parts: s.parts.lost, lost_features: s.lost_features.map(f => `${f.element} ${f.feature}`),
          contact: c.verdict, problems: c.problems};
}

// The layouts that match what the review recorded as its result (layout.json first, then request.json).
function recordedLayout(dir, review, base) {
  const want = review.after || {};
  const tries = [];
  if (existsSync(path.join(dir, 'layout.json'))) tries.push(['layout', readJSON(path.join(dir, 'layout.json'))]);
  if (existsSync(path.join(dir, 'request.json'))) {
    const q = readJSON(path.join(dir, 'request.json'));
    if (q.parts?.main?.layout && q.parts?.sub?.layout)
      tries.push(['request', {...base, position: q.parts.sub.position || want.position, main: q.parts.main.layout, sub: q.parts.sub.layout}]);
  }
  const out = [];
  for (const [source, layout] of tries) {
    try { if (layout.position === want.position && near(boxOf(layout.main), want.main) && near(boxOf(layout.sub), want.sub)) out.push({layout, source}); } catch {}
  }
  return out;
}

// Suspicion: the higher, the sooner a person should look. Reasons are short and plain.
function score(review, stored, final) {
  let s = 0;
  const why = [];
  const add = (n, text) => { s += n; why.push(text); };
  const r = final || stored;
  if (!r) return {score: 50, why: ['could not be measured']};
  if (r.flags.includes('lost_feature')) add(40, `loses a feature: ${r.lost_features.join(', ')}`);
  if (r.flags.includes('lost_part')) add(25, `loses a part: ${r.lost_parts.join(', ')}`);
  if (r.flags.includes('erased_whole_piece')) add(20, 'erases a whole piece');
  if (r.flags.includes('fragmented')) add(12, 'cuts the main into pieces');
  if (r.flags.includes('stub')) add(12, 'leaves a crumb');
  if (r.flags.includes('detached')) add(15, 'the parts float apart');
  if (r.flags.includes('container')) add(20, 'main surrounds the sub');
  if (r.flags.includes('shaved')) add(10, 'nicks the main without touching');
  if (r.flags.includes('heavy_cut')) add(10, `heavy cut (${r.erased}% erased)`);
  if (r.contact === 'fail') add(15, 'contact check fails');
  if (review.verdict === 'fix') {
    const b = review.before?.keyshape || {}, a = review.after?.keyshape || {};
    const sb = size(b.sub), sa = size(a.sub), mb = size(b.main), ma = size(a.main);
    if (sb && sa && sa < sb) add(15, `sub shrunk ${sb} → ${sa}`);
    if (mb && ma && mb - ma >= 8) add(5, `main shrunk ${mb} → ${ma}`);
    if (final && stored && final.penalty > stored.penalty) add(15, `fix measures worse than stored (${stored.penalty} → ${final.penalty})`);
    if (final && stored && !stored.flags.length && stored.contact !== 'fail') add(20, 'stored had no problems');
  }
  if (review.verdict === 'redraw') add(5, 'AI says redraw');
  if (review.keep_stored) s = Math.max(0, s - 10);
  return {score: s, why};
}

function scanOne(id) {
  const dir = path.join(WORK, id);
  const review = readJSON(path.join(dir, 'review.json'));
  const base = readJSON(path.join(dir, 'base-layout.json'));
  let stored = null, final = null, source = 'stored', error = null;
  try { stored = measure(dir, base); } catch (e) { error = 'stored: ' + e.message; }
  if (review.verdict === 'fix') {
    source = 'unverified';
    for (const rec of recordedLayout(dir, review, base)) {
      try { final = measure(dir, rec.layout); source = rec.source; error = null; break; } catch (e) { error = 'final: ' + e.message; }
    }
  }
  const picture = (final || stored)?.svg;
  if (picture) {
    const svg = path.join(OUT, 'final', id + '.svg');
    writeFileSync(svg, picture);
    try { execFileSync('rsvg-convert', ['-w', '256', '-h', '256', '-b', 'white', '-o', path.join(OUT, 'final', id + '.png'), svg], {timeout: 30000}); } catch {}
  }
  const strip = m => m && {flags: m.flags, penalty: m.penalty, contact: m.contact, reach: m.reach, erased: m.erased,
                           lost_parts: m.lost_parts, lost_features: m.lost_features};
  const {score: sc, why} = score(review, stored, final);
  return {id, concept: review.concept, verdict: review.verdict, reviewed_at: review.reviewed_at, keep_stored: review.keep_stored || '',
          note: review.note || '', before: review.before?.keyshape || null, after: review.after?.keyshape || null,
          position: [review.before?.position || base.position, review.after?.position || base.position],
          source, stored: strip(stored), final: strip(final), score: sc, why, error};
}

const ids = (opt('--ids') ? opt('--ids').split(',') : readdirSync(WORK)).filter(id => {
  const f = path.join(WORK, id, 'review.json');
  if (!existsSync(f) || !existsSync(path.join(WORK, id, 'base-layout.json'))) return false;
  return (readJSON(f).reviewed_at || '') >= SINCE;
}).sort();
mkdirSync(path.join(OUT, 'final'), {recursive: true});

if (CHUNK) {
  // Worker: scan every JOBS-th id and print the rows as JSON lines.
  const [k, of] = CHUNK.split('/').map(Number);
  for (let i = k; i < ids.length; i += of) {
    let row;
    try { row = scanOne(ids[i]); } catch (e) { row = {id: ids[i], error: e.message, score: 50, why: ['scan failed: ' + e.message]}; }
    process.stdout.write(JSON.stringify(row) + '\n');
  }
} else {
  const started = Date.now(), rows = [];
  let done = 0;
  await Promise.all(Array.from({length: JOBS}, (_, k) => new Promise(res => {
    const child = spawn(process.execPath, [fileURLToPath(import.meta.url), ...args, '--chunk', `${k}/${JOBS}`], {stdio: ['ignore', 'pipe', 'inherit'], env: process.env});
    let buf = '';
    child.stdout.on('data', d => {
      buf += d;
      let i;
      while ((i = buf.indexOf('\n')) >= 0) {
        rows.push(JSON.parse(buf.slice(0, i)));
        buf = buf.slice(i + 1);
        if (++done % 100 === 0) process.stderr.write(`\r${done} / ${ids.length}`);
      }
    });
    child.on('close', res);
  })));
  // --ids rescans a few pairs: merge them into the existing triage.json instead of replacing it.
  const file = path.join(OUT, 'triage.json');
  if (opt('--ids') && existsSync(file)) {
    const fresh = new Set(rows.map(r => r.id));
    rows.push(...readJSON(file).rows.filter(r => !fresh.has(r.id)));
  }
  rows.sort((a, b) => b.score - a.score || (a.concept || '').localeCompare(b.concept || ''));
  writeFileSync(path.join(OUT, 'triage.json'), JSON.stringify({scanned_at: new Date().toISOString(), since: SINCE, size: SIZE, rows}));
  const by = (f) => rows.reduce((m, r) => (m[f(r)] = (m[f(r)] || 0) + 1, m), {});
  console.log(`\n${rows.length} pairs in ${((Date.now() - started) / 1000).toFixed(0)} s → ${path.join(OUT, 'triage.json')}`);
  console.log('verdicts', by(r => r.verdict), 'source', by(r => r.source));
  console.log('score ≥40', rows.filter(r => r.score >= 40).length, '· 20–39', rows.filter(r => r.score >= 20 && r.score < 40).length,
              '· <20', rows.filter(r => r.score < 20).length, '· lost_feature', rows.filter(r => (r.final || r.stored)?.flags?.includes('lost_feature')).length,
              '· errors', rows.filter(r => r.error).length);
}
