#!/usr/bin/env node
// Download every icon-72 side combination (main-54 + sub-36 on a 72 canvas) for local review:
// icon_set/work/side-72/items.json (every pair, its state and parts) and svg/<reference_id>.svg (the combined icon of
// each built or stale pair). Re-running skips SVGs whose sha is already on disk.
//
//   node icon_set/scripts/side72_fetch.mjs [--concurrency 6]
//   /opt/homebrew/bin/python3 icon_set/work/side-72/server.py   → http://127.0.0.1:8772/
import {existsSync, mkdirSync, readFileSync, writeFileSync} from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const OUT = path.join(REPO, 'icon_set/work/side-72');
const BASE = (process.env.PICTOGRAPHIC_API || 'https://pictographic-review-next.pictographic.workers.dev').replace(/\/$/, '');
const UA = 'pictographic-side-tools';
const args = process.argv.slice(2);
const CONCURRENCY = Number(args[args.indexOf('--concurrency') + 1]) || 6;

async function get(route, asText = false, tries = 3) {
  for (let i = 1; ; i++) {
    try {
      const r = await fetch(BASE + route, {headers: {'User-Agent': UA}, signal: AbortSignal.timeout(60000)});
      if (!r.ok) throw Error(`HTTP ${r.status}`);
      return asText ? r.text() : r.json();
    } catch (e) {
      if (i >= tries) throw Error(`${route.split('?')[0]}: ${e.message}`);
      await new Promise(res => setTimeout(res, 1000 * i));
    }
  }
}

mkdirSync(path.join(OUT, 'svg'), {recursive: true});
const items = [];
let offset = 0, total = 0;
do {
  const d = await get(`/api/combinations?kind=side&size=72&limit=500&offset=${offset}`);
  total = d.total;
  items.push(...d.items);
  offset = d.next_offset;
  process.stdout.write(`\rpairs ${items.length} / ${total}`);
} while (offset != null && items.length < total);
console.log();

const shaFile = path.join(OUT, 'svg-sha.json');
const have = existsSync(shaFile) ? JSON.parse(readFileSync(shaFile, 'utf8')) : {};
const todo = items.filter(i => i.icon?.preview_url && !(have[i.reference_id] === i.icon.svg_sha256 && existsSync(path.join(OUT, 'svg', i.reference_id + '.svg'))));
let done = 0, failed = [];
async function worker() {
  while (todo.length) {
    const i = todo.shift();
    try {
      writeFileSync(path.join(OUT, 'svg', i.reference_id + '.svg'), await get(i.icon.preview_url, true));
      have[i.reference_id] = i.icon.svg_sha256;
    } catch (e) { failed.push(`${i.reference_id}: ${e.message}`); }
    if (++done % 50 === 0) { process.stdout.write(`\rsvgs ${done}`); writeFileSync(shaFile, JSON.stringify(have)); }
  }
}
await Promise.all(Array.from({length: CONCURRENCY}, worker));
writeFileSync(shaFile, JSON.stringify(have));

// Compact list for the page: what a reviewer needs per pair.
const rows = items.map(i => {
  const part = r => i.parts.find(p => p.role === r) || {};
  const m = part('main'), s = part('sub');
  return {id: i.reference_id, concept: i.concept, state: i.state, icon: i.icon?.key || null, review: i.icon?.review || null,
          has_svg: existsSync(path.join(OUT, 'svg', i.reference_id + '.svg')), position: s.position || null,
          main: m.icon || null, main_review: m.review || null, sub: s.icon || null, sub_review: s.review || null,
          main_box: m.layout?.[0] || null, sub_box: s.layout?.[0] || null,
          hand: !!((m.layout && m.layout.length) || (s.layout && s.layout.length))};
});
writeFileSync(path.join(OUT, 'items.json'), JSON.stringify(rows));
writeFileSync(path.join(OUT, 'raw-items.json'), JSON.stringify(items));
const by = rows.reduce((a, r) => (a[r.state] = (a[r.state] || 0) + 1, a), {});
console.log(`\npairs ${rows.length} ${JSON.stringify(by)} · svgs on disk ${rows.filter(r => r.has_svg).length} · failed ${failed.length}`);
if (failed.length) console.log(failed.slice(0, 10).join('\n'));
