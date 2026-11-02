// combine-side.js against the Python side engine, stroke for stroke.
//   node --test icon_set/tests/js/*.test.mjs
// side-goldens.json: real side pairs (every sizing mode, native text, hand-adjusted layouts) rendered by
// combination_experiment.render (make_side_goldens.py). The JS must return the same SVG, character for
// character, or refuse with the same error.
import test from 'node:test';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {existsSync, readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';

const require = createRequire(import.meta.url);
const Side = require('../../scripts/templates/combine-side.js');
const file = process.env.SIDE_GOLDENS || new URL('./side-goldens.json', import.meta.url).pathname;
const cases = existsSync(file) ? JSON.parse(readFileSync(file)) : [];

test('native text builds carry the hash of the embedded form drawing', () => {
  const c = cases.find(c => !c.error && c.row.subs.some(s => s.native_text));
  assert.ok(c, 'native text fixture is required');
  const main = c.row.mains.find(m => m.icon === c.request.main) || c.row.mains[0];
  const sub = c.row.subs.find(s => s.native_text);
  const key = main.model_key || `${main.family}/${main.icon}`;
  const hash = svg => createHash('sha256').update(svg).digest('hex');
  const item = {reference_id: c.row.id, parts: [
    {role: 'main', icon: key, form: main},
    {role: 'sub', icon: null, form: {...sub, sha256: hash(sub.document)}, position: c.row.position},
  ]};
  const drawings = new Map([[key, {svg: main.document, svg_sha256: hash(main.document)}]]);
  const built = Side.pairRequest(item, drawings);
  assert.equal(built.request.parts.sub.icon, null);
  assert.equal(built.request.parts.sub.svg_sha256, hash(sub.document));
  assert.equal(built.request.parts.main.svg_sha256, hash(main.document));
  assert.equal(built.svg, Side.render(c.row, {main: main.icon, sub: sub.icon}).svg);
});

// Where two SVGs first differ, for the failure message.
function firstDifference(a, b) {
  let i = 0;
  while (i < a.length && a[i] === b[i]) i++;
  return `at ${i}:\n  js: …${a.slice(Math.max(0, i - 80), i + 80)}\n  py: …${b.slice(Math.max(0, i - 80), i + 80)}`;
}

test('side pairs match the Python engine exactly', () => {
  assert.ok(cases.length >= 50, `side goldens missing (${file})`);
  const failures = [];
  for (const c of cases) {
    const label = `${c.row.id}${c.request.layout ? ' (layout)' : ''}`;
    let result, error;
    try { result = Side.render(c.row, c.request); } catch (e) { error = e; }
    if (c.error) {
      if (!error || error.message !== c.error) failures.push(`${label}: expected error "${c.error}", got ${error ? `"${error.message}"` : 'a drawing'}`);
      continue;
    }
    if (error) { failures.push(`${label}: ${error.stack.split('\n').slice(0, 3).join(' ')}`); continue; }
    if (result.svg !== c.python.svg) failures.push(`${label}: ${firstDifference(result.svg, c.python.svg)}`);
  }
  assert.equal(failures.length, 0, `${failures.length} of ${cases.length} differ:\n` + failures.slice(0, 8).join('\n'));
});

// Stale pairs rebuilt from their parts' current drawings (make_stale_goldens.py): measured like
// side_recombine.pair_with_documents, then combined.
const staleFile = process.env.STALE_GOLDENS || new URL('./stale-goldens.json', import.meta.url).pathname;
const stale = existsSync(staleFile) ? JSON.parse(readFileSync(staleFile)) : [];

test('stale pairs rebuilt from current drawings match the Python engine exactly', {skip: !stale.length && 'no stale goldens'}, () => {
  const failures = [];
  for (const c of stale) {
    let result, error;
    try {
      const current = Side.withDocuments(c.row, c.main, c.sub, c.documents);
      result = Side.render(current.row, {main: current.main, sub: current.sub});
    } catch (e) { error = e; }
    if (c.error) {
      if (!error || error.message !== c.error) failures.push(`${c.row_id}: expected error "${c.error}", got ${error ? `"${error.message}"` : 'a drawing'}`);
      continue;
    }
    if (error) { failures.push(`${c.row_id}: ${error.message}`); continue; }
    if (result.svg !== c.python.svg) failures.push(`${c.row_id}: ${firstDifference(result.svg, c.python.svg)}`);
  }
  assert.equal(failures.length, 0, `${failures.length} of ${stale.length} differ:\n` + failures.slice(0, 8).join('\n'));
});
