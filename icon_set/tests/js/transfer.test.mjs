// combine-side.js `transfer` (Apply layout to pairs with the same main) against the Python
// combination_layouts.transfer it replaces: transfer-goldens.json (make_transfer_goldens.py).
//   node --test icon_set/tests/js/*.test.mjs
import test from 'node:test';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {readFileSync} from 'node:fs';

const require = createRequire(import.meta.url);
const Side = require('../../scripts/templates/combine-side.js');
const cases = JSON.parse(readFileSync(new URL('./transfer-goldens.json', import.meta.url)));

test('transfer moves a layout to another pair exactly as the Python engine did', () => {
  for (const {args, out} of cases) {
    const got = Side.transfer(args.layout, args.source_position, args.source_sub, args.target_position, args.target_sub,
                              args.target_canvas, args.target_sub_groups);
    assert.deepEqual(got, out, JSON.stringify({position: args.target_position, sub: args.target_sub, canvas: args.target_canvas}));
  }
});

test('element markup and names come with the pieces', () => {
  const svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="4">'
    + '<g stroke-linecap="round"><path id="stem" d="M4 4L20 20"/></g><circle cx="30" cy="30" r="6"/></svg>';
  const parts = Side.elementParts(svg);
  assert.deepEqual(parts.names, ['stem', 'circle']);
  assert.equal(parts.markup[0], '<path xmlns="http://www.w3.org/2000/svg" d="M4 4L20 20" stroke-linecap="round" />');
  assert.equal(parts.markup[1], '<circle xmlns="http://www.w3.org/2000/svg" cx="30" cy="30" r="6" />');
});
