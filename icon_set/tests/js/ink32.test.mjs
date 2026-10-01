// normalize-ink32.js against icon_set/scripts/sub_ink32.normalize_ink32 (svgpathtools): real sub drawings.
//   node --test icon_set/tests/js/*.test.mjs
// ink32-goldens.json: sub drawings from a D1 snapshot and the document and ink Python returned for each.
import test from 'node:test';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {readFileSync} from 'node:fs';

const require = createRequire(import.meta.url);
const Normalize = require('../../scripts/templates/normalize-ink32.js');
const cases = JSON.parse(readFileSync(new URL('./ink32-goldens.json', import.meta.url)));

test('sub drawings normalize to SUB32 exactly as Python does', () => {
  const failures = [];
  for (const c of cases) {
    let document, ink, error;
    try { [document, ink] = Normalize.normalize(c.svg, {text: c.text}); } catch (e) { error = e; }
    if (c.error) { if (!error) failures.push(`${c.key}: expected ${c.error}`); continue; }
    if (error) { failures.push(`${c.key}: ${error.message}`); continue; }
    if (document !== c.document) failures.push(`${c.key}: document differs`);
    else if (JSON.stringify(ink) !== JSON.stringify(c.ink)) failures.push(`${c.key}: ink differs`);
  }
  assert.equal(failures.length, 0, `${failures.length} of ${cases.length} differ:\n` + failures.slice(0, 8).join('\n'));
});
