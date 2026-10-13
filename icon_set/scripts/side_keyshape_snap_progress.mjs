#!/usr/bin/env node
// Live progress page for side_keyshape_snap.mjs runs: rewrites icon_set/work/side-keyshape-snap/index.html every 20 s
// (pairs done, rate, time left per size, class counts so far) and the partial report.html of each size every minute.
// Stops by itself once both sizes are done and idle.
//
//   node icon_set/scripts/side_keyshape_snap_progress.mjs
import {execFileSync} from 'node:child_process';
import {existsSync, readFileSync, readdirSync, writeFileSync} from 'node:fs';
import path from 'node:path';

const HERE = path.dirname(new URL(import.meta.url).pathname);
const ROOT = path.resolve(HERE, '../work/side-keyshape-snap');
const SCRIPT = path.join(HERE, 'side_keyshape_snap.mjs');
const SIZES = [64, 72], TICK = 20000;
const samples = {64: [], 72: []};
let ticks = 0;

function state(size) {
  const dir = path.join(ROOT, String(size)), items = path.join(dir, 'cache/items.json');
  const total = existsSync(items) ? JSON.parse(readFileSync(items, 'utf8')).length : 0;
  const classes = {};
  let done = 0;
  const pairs = path.join(dir, 'pairs');
  for (const id of existsSync(pairs) ? readdirSync(pairs) : []) {
    const f = path.join(pairs, id, 'snap.json');
    if (!existsSync(f)) continue;
    try { const c = JSON.parse(readFileSync(f, 'utf8')).class; classes[c] = (classes[c] || 0) + 1; done++; } catch { /* being written */ }
  }
  const now = Date.now(), s = samples[size];
  s.push([now, done]);
  while (s.length > 2 && now - s[0][0] > 180000) s.shift();
  const [t0, d0] = s[0], rate = now > t0 ? (done - d0) / ((now - t0) / 1000) : 0;
  const left = total - done, eta = rate > 0 ? left / rate : null;
  return {size, total, done, classes, rate, eta, finished: total > 0 && left <= 0};
}

const fmtTime = sec => sec === null ? (ticks < 2 ? 'measuring…' : 'waiting') : sec < 60 ? `${Math.round(sec)} s` : `${Math.floor(sec / 60)} min ${Math.round(sec % 60)} s`;
const clock = sec => sec === null ? '—' : new Date(Date.now() + sec * 1000).toLocaleTimeString([], {hour: '2-digit', minute: '2-digit'});
const COLORS = {'already-fits': 'var(--muted)', 'snapped-ok': 'var(--ok)', 'snapped-flagged': 'var(--warn)', 'no-fit': 'var(--bad)', error: 'var(--bad)'};

function html(rows, finished) {
  const cards = rows.map(r => {
    const pct = r.total ? 100 * r.done / r.total : 0;
    const cls = Object.entries(r.classes).sort((a, b) => b[1] - a[1])
      .map(([k, n]) => `<li><span class="dot" style="background:${COLORS[k] || 'var(--muted)'}"></span>${k}<b>${n}</b></li>`).join('');
    return `<section class="card">
  <h2>${r.size} canvas <span class="state">${r.finished ? 'done' : 'running'}</span></h2>
  <div class="big">${r.done.toLocaleString()} <small>/ ${r.total.toLocaleString()} pairs</small></div>
  <div class="track"><div class="fill" style="width:${pct.toFixed(1)}%"></div></div>
  <dl><div><dt>Progress</dt><dd>${pct.toFixed(1)}%</dd></div>
      <div><dt>Rate</dt><dd>${r.rate.toFixed(1)} pairs/s</dd></div>
      <div><dt>Time left</dt><dd>${r.finished ? '—' : fmtTime(r.eta)}</dd></div>
      <div><dt>Finishes at</dt><dd>${r.finished ? 'done' : clock(r.eta)}</dd></div></dl>
  <ul class="classes">${cls}</ul>
  <a href="${r.size}/report.html">Open the ${r.size} report${r.finished ? '' : ' (partial, refreshed every minute)'} →</a>
</section>`;
  }).join('\n');
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
${finished ? '' : '<meta http-equiv="refresh" content="20">'}<title>Keyshape snap progress</title>
<style>
:root{--bg:#f6f6f4;--fg:#1b1b1b;--muted:#77756f;--card:#fff;--line:#e2e0da;--ok:#1a7f37;--warn:#c26a00;--bad:#c62828;--accent:#2f6fde}
@media (prefers-color-scheme:dark){:root{--bg:#131313;--fg:#ececea;--muted:#9a9890;--card:#1d1d1c;--line:#323230}}
*{box-sizing:border-box}body{margin:0;padding:24px 16px;background:var(--bg);color:var(--fg);font:15px/1.45 system-ui,-apple-system,sans-serif}
main{max-width:920px;margin:0 auto}h1{font-size:22px;margin:0 0 4px}.sub{color:var(--muted);margin:0 0 20px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px}
h2{font-size:16px;margin:0 0 10px;display:flex;justify-content:space-between}.state{font-size:12px;color:var(--muted);font-weight:500}
.big{font-size:32px;font-weight:650;font-variant-numeric:tabular-nums}.big small{font-size:15px;color:var(--muted);font-weight:400}
.track{height:8px;background:var(--line);border-radius:4px;margin:10px 0 14px;overflow:hidden}.fill{height:100%;background:var(--accent)}
dl{display:grid;grid-template-columns:1fr 1fr;gap:8px 16px;margin:0 0 14px}dt{font-size:12px;color:var(--muted)}dd{margin:0;font-variant-numeric:tabular-nums;font-weight:550}
.classes{list-style:none;padding:0;margin:0 0 14px;display:grid;gap:4px}.classes li{display:flex;align-items:center;gap:8px;font-size:14px}
.classes b{margin-left:auto;font-variant-numeric:tabular-nums}.dot{width:9px;height:9px;border-radius:50%}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
.note{margin-top:20px;color:var(--muted);font-size:13px}
</style></head><body><main>
<h1>Side keyshape snap: progress</h1>
<p class="sub">Updated ${new Date().toLocaleTimeString()}${finished ? ' · finished' : ' · reloads every 20 s'} · local only, nothing pushed</p>
<div class="grid">${cards}</div>
<p class="note">Move only: the main and the sub keep their stored size and shift by whole units into the nearest canvas keyshape
(64: circle 60, square 56, hrect 60×48, hrect-m 60×44, vrect 48×60, vrect-m 44×60 · 72: circle 68, square 64, hrect 68×54, hrect-m 68×50, vrect 54×68, vrect-m 50×68).
Time left is measured over the last 3 minutes.</p>
</main></body></html>
`;
}

function reports() {
  for (const size of SIZES) {
    if (!existsSync(path.join(ROOT, String(size), 'cache/items.json'))) continue;
    try { execFileSync(process.execPath, [SCRIPT, '--report-only'], {env: {...process.env, SIDE_SIZE: String(size)}, stdio: 'ignore', timeout: 120000}); }
    catch { /* next tick */ }
  }
}

let idle = 0;
while (true) {
  const rows = SIZES.map(state);
  const finished = rows.every(r => r.finished);
  if (ticks % 3 === 0 || finished) reports();
  writeFileSync(path.join(ROOT, 'index.html'), html(rows, finished));
  ticks++;
  if (finished && ++idle > 1) break;
  await new Promise(r => setTimeout(r, TICK));
}
console.log('both sizes done');
