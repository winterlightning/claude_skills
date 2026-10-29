// The pair page's layout editor saves the pick it edits (side-fill-data.js subFor): its "fill" sub is the fill the
// combination uses, not a sub's first fill. No goldens needed.
//   node --test icon_set/tests/js/side-fill-pick.test.mjs
import test from 'node:test';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';

const require = createRequire(import.meta.url);
const {subFor} = require('../../scripts/templates/side-fill-data.js');
const fills = [{key: 'sub/b--fill', name: 'fill'}, {key: 'sub/b--fill-custom', name: 'custom'}];

test('placement-only editing keeps the selected sub fill', () => {
  assert.equal(subFor('fill', 'sub/b--fill-custom', 'sub/b', fills), 'sub/b--fill-custom');
  assert.equal(subFor('fill', 'sub/b--fill', 'sub/b', fills), 'sub/b--fill');
});

test('switching between outline and fill', () => {
  assert.equal(subFor('outline', 'sub/b--fill-custom', 'sub/b', fills), 'sub/b');
  assert.equal(subFor('fill', 'sub/b', 'sub/b', fills), 'sub/b--fill');       // from the outline: the sub's first fill
  assert.equal(subFor('fill', 'sub/b', 'sub/b', []), undefined);              // a sub without a fill has none to switch to
});
