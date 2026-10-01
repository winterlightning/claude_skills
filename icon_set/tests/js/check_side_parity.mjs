// Every built side pair rebuilt in JS from its parts' current drawings must give the drawing stored for it
// (the Python engine's, byte for byte, so the same sha). Read-only: GET requests against a Worker.
//   node icon_set/tests/js/check_side_parity.mjs https://pictographic-review-next.pictographic.workers.dev
import {createRequire} from 'node:module';
const require = createRequire(import.meta.url);
const Side = require('../../scripts/templates/combine-side.js');
const base = process.argv[2] || 'http://127.0.0.1:8821';
const get = async path => { const r = await fetch(base + path); if (!r.ok) throw Error(`${path}: ${r.status}`); return r.json(); };

let same = 0, different = [], failed = [], offset = 0;
const drawings = new Map();
while (true) {
  const page = await get(`/api/combinations?kind=side&state=built&forms=1&limit=200&offset=${offset}`);
  const keys = [...new Set(page.items.flatMap(i => i.parts.map(p => p.icon)).filter(k => k && !drawings.has(k)))];
  for (let i = 0; i < keys.length; i += 100) {
    for (const [k, d] of Object.entries(await get('/api/combinations/drawings?keys=' + encodeURIComponent(keys.slice(i, i + 100).join(','))))) drawings.set(k, d);
  }
  for (const item of page.items) {
    try {
      const {svg} = Side.pairRequest(item, drawings);
      if (Side.sha256(svg) === item.icon.svg_sha256) same++; else different.push(item.reference_id);
    } catch (error) { failed.push(`${item.reference_id}: ${error.message}`); }
  }
  if (page.next_offset == null) break;
  offset = page.next_offset;
}
console.log(`built side pairs rebuilt in JS: ${same} identical, ${different.length} different, ${failed.length} could not be drawn`);
if (different.length) console.log('different:', different.slice(0, 10).join(' '));
if (failed.length) console.log('failed:', failed.slice(0, 5).join('\n  '));
process.exitCode = different.length || failed.length ? 1 : 0;
