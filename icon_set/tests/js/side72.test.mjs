// combine-side.js at size 72: a 54 main and a 36 sub on the 72 canvas, the sub placed exactly as drawn on its grid.
//   node --test icon_set/tests/js/*.test.mjs
import test from 'node:test';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';

const require = createRequire(import.meta.url);
const Side = require('../../scripts/templates/combine-side.js');

const svg = (size, body) => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${size} ${size}" fill="none" stroke="currentColor" `
  + `stroke-width="4" stroke-linecap="round" stroke-linejoin="round">${body}</svg>`;
const MAIN = svg(54, '<rect x="6" y="6" width="42" height="42" rx="6"/><path d="M6 17L48 17"/>');
const SUB = svg(36, '<circle cx="18" cy="18" r="12"/>');

function build(position, sub = SUB, main = MAIN) {
  const item = {reference_id: 'pair', parts: [{role: 'main', icon: 'main-54/m', form: null}, {role: 'sub', icon: 'sub-36/s', position, form: null}]};
  const drawings = new Map([['main-54/m', {svg: main, svg_sha256: 'm'}], ['sub-36/s', {svg: sub, svg_sha256: 's'}]]);
  return Side.pairRequest(item, drawings, {size: 72});
}

test('a 72 pair is drawn on a 72 canvas', () => {
  const {result, svg} = build('br');
  assert.equal(result.canvas, 72);
  assert.match(svg, /viewBox="0 0 72 72"/);
  assert.equal(result.subSizeLock, 'exact');
});

test('the sub keeps its 36 drawing: its grid at the anchor, unscaled', () => {
  for (const [position, x, y] of [['br', 34, 34], ['tl', 2, 2], ['tr', 34, 2], ['bl', 2, 34], ['ri', 34, 18], ['bo', 18, 34]]) {
    const {svg, result} = build(position);
    assert.match(svg, new RegExp(`id="state-icon" transform="translate\\(${x} ${y}\\) scale\\(1\\)"`), position);
    const sub = result.placements[1];
    assert.deepEqual(sub.canvas_box, {x, y, w: 36, h: 36}, position);
  }
});

test('a sub drawn off-centre on its grid stays where it was drawn', () => {
  const {svg: drawn} = build('br', svg(36, '<path d="M4 4L12 12"/>'));
  assert.match(drawn, /id="state-icon" transform="translate\(34 34\) scale\(1\)"/);
});

test('the main is erased around the sub with the 64 spacing (8 units from the sub centreline)', () => {
  const {svg} = build('br');
  const main = svg.split('id="main-icon-clipped"')[1].split('</g>')[0];
  const points = [...main.matchAll(/([\d.]+),([\d.]+)/g)].map(m => [Number(m[1]), Number(m[2])]);
  // the sub circle: centre (52, 52), radius 12
  for (const [x, y] of points) assert.ok(Math.hypot(x - 52, y - 52) >= 12 + 8 - 0.02 || Math.hypot(x - 52, y - 52) <= 12 - 8 + 0.02, `${x},${y}`);
});

test('a sub not drawn on the 36 grid is refused', () => {
  assert.throws(() => build('br', svg(32, '<circle cx="16" cy="16" r="12"/>')), /drawn on the 36 grid/);
});

test('64 pairs are unchanged by the size setting', () => {
  assert.deepEqual(Side.SIZES[64], {canvas: 64, main: 48, sub: 32});
  assert.deepEqual(Side.SIZES[72], {canvas: 72, main: 54, sub: 36});
});
