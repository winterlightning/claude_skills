// combine.js against the Python renderer it replaced: container-goldens.json holds real container pairs
// rendered by container_combination_render.py (removed with the graphics route; the file is now fixed), and 40
// with odd sizes and half-unit centres rendered by it as of eb86e8615d.
//   node --test icon_set/tests/js
// The drawings must match: the same elements, commands and attributes, every number within TOLERANCE
// (the JS measures curves exactly, the Python engine from sampled segments).
import test from 'node:test';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {readFileSync} from 'node:fs';

const require = createRequire(import.meta.url);
const Combine = require('../../scripts/templates/combine.js');
const cases = JSON.parse(readFileSync(new URL('./container-goldens.json', import.meta.url)));
const TOLERANCE = 0.05;
const NUMBER = /[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?/g;

// The drawing as comparable parts: its markup without numbers, and the numbers in order.
function shape(svg) {
  // Whitespace between tags is layout only (Python keeps the container's indentation).
  const normal = svg.replace(/>\s+</g, '><').replace(/\s*\/>/g, ' />').replace(/\s+/g, ' ').replace(/ xmlns="[^"]*"/, '');
  return {markup: normal.replace(NUMBER, '#'), numbers: (normal.match(NUMBER) || []).map(Number)};
}

function same(actual, expected, label) {
  const a = shape(actual), e = shape(expected);
  assert.equal(a.markup, e.markup, `${label}: markup differs`);
  assert.equal(a.numbers.length, e.numbers.length, `${label}: number count differs`);
  a.numbers.forEach((n, i) => {
    assert.ok(Math.abs(n - e.numbers[i]) <= TOLERANCE, `${label}: number ${i} is ${n}, Python has ${e.numbers[i]}`);
  });
}

test('golden cases match the Python renderer', () => {
  assert.ok(cases.length >= 100);
  for (const c of cases) {
    const label = `${c.reference_id} center ${c.center} ink ${c.ink}`;
    if (c.error) {
      assert.throws(() => Combine.container(c.main, c.symbol, {center: c.center, ink: c.ink}), Combine.CombineError, label);
      continue;
    }
    const result = Combine.container(c.main, c.symbol, {center: c.center, ink: c.ink});
    same(result.svg, c.python.svg, label);
    for (const [i, p] of c.python.placements.entries()) {
      for (const k of ['x', 'y', 'w', 'h']) {
        assert.ok(Math.abs(result.placements[i].painted_box[k] - p.painted_box[k]) <= TOLERANCE, `${label}: ${p.role} ${k}`);
      }
    }
  }
});

test('a saved box renders the same drawing as the placement it came from', () => {
  for (const c of cases.slice(0, 60)) {
    if (c.error) continue;
    const placed = Combine.container(c.main, c.symbol, {center: c.center, ink: c.ink});
    const again = Combine.container(c.main, c.symbol, {box: placed.layout.symbol[0]});
    assert.equal(again.svg, placed.svg, c.reference_id);
  }
});

const MAIN = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="4"><rect x="6" y="6" width="52" height="52" rx="6"/></svg>';
const PLUS = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="4"><path d="M6 16h20M16 6v20"/></svg>';

test('natural and sized placements', () => {
  const natural = Combine.container(MAIN, PLUS, {center: [32, 32], ink: null});
  assert.deepEqual(natural.layout.symbol, [{paths: [0], x: 22, y: 22, w: 20, h: 20}]);
  assert.match(natural.svg, /<path d="M 22 32 h 20 M 32 22 v 20" \/>/);
  const sized = Combine.container(MAIN, PLUS, {center: [32, 34], ink: [24, 20]});
  assert.deepEqual(sized.layout.symbol, [{paths: [0], x: 22, y: 26, w: 20, h: 16}]);
  assert.deepEqual(natural.layout.container, [{x: 6, y: 6, w: 52, h: 52}]);
});

test('transforms are written into the coordinates', () => {
  const moved = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" stroke="currentColor" stroke-width="4" fill="none"><g transform="translate(2 2) scale(0.5)"><path d="M8 28h40M28 8v40"/></g></svg>';
  const result = Combine.container(MAIN, moved, {center: [32, 32], ink: null});
  assert.doesNotMatch(result.svg, /transform/);
  assert.deepEqual(result.layout.symbol, [{paths: [0], x: 22, y: 22, w: 20, h: 20}]);
});

test('refuses what cannot be combined', () => {
  const rotated = PLUS.replace('<path', '<path transform="rotate(45 16 16)"');
  assert.throws(() => Combine.container(MAIN, rotated, {center: [32, 32]}), /Rotated or skewed/);
  assert.throws(() => Combine.container(MAIN, PLUS, {center: [70, 32]}), /center/);
  // Odd sizes are whole units (a half-unit centre keeps the edges on the grid); fractions and sizes under 4 are not.
  assert.doesNotThrow(() => Combine.container(MAIN, PLUS, {center: [32.5, 32], ink: [25, 20]}));
  assert.throws(() => Combine.container(MAIN, PLUS, {center: [32, 32], ink: [25.5, 20]}), /whole number/);
  assert.throws(() => Combine.container(MAIN, PLUS, {center: [32, 32], ink: [3, 20]}), /whole number/);
  assert.throws(() => Combine.container(MAIN, PLUS, {center: [4, 4], ink: [40, 40]}), /beyond the 64x64 canvas/);
  assert.throws(() => Combine.container(MAIN, '<svg xmlns="http://www.w3.org/2000/svg"/>', {center: [32, 32]}), /no drawable/);
  assert.throws(() => Combine.container(MAIN, '<!DOCTYPE svg><svg/>', {center: [32, 32]}), /entity/);
  assert.throws(() => Combine.container(MAIN, PLUS, {box: {x: 1.5, y: 0, w: 4, h: 4}}), /whole numbers/);
});
