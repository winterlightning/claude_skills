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

test("the main's filled dots are kept, except under the sub", () => {
  const main = svg(54, '<circle cx="27" cy="27" r="23"/><circle cx="20" cy="24" r="2" fill="currentColor" stroke="none"/>'
    + '<circle cx="44" cy="44" r="2" fill="currentColor" stroke="none"/>');
  const {svg: drawn} = build('br', SUB, main);
  const group = drawn.split('id="main-icon-clipped"')[1].split('</g>')[0];
  const dots = [...group.matchAll(/<circle cx="([\d.]+)" cy="([\d.]+)" r="([\d.]+)" fill="#000000" stroke="none"/g)].map(m => m.slice(1).map(Number));
  assert.equal(dots.length, 1, group);           // the one at (44, 44) of the 54 drawing sits under the sub
  assert.ok(dots[0][2] === 2 && dots[0][0] < 34 && dots[0][1] < 34, String(dots[0]));
});

test('a sub given a preset box at 72 is drawn in that box', () => {
  const item = {reference_id: 'pair', parts: [{role: 'main', icon: 'main-54/m', form: null}, {role: 'sub', icon: 'sub-36/s', position: 'br', form: null}]};
  const drawings = new Map([['main-54/m', {svg: MAIN, svg_sha256: 'm'}], ['sub-36/s', {svg: SUB, svg_sha256: 's'}]]);
  // Sub size 28 on its circle: centerline 32 − 8 = 24 wide, in the bottom-right corner (72 − 2 padding − 2 inset).
  const box = {paths: [0], x: 44, y: 44, w: 24, h: 24};
  const {result, request} = Side.pairRequest(item, drawings, {size: 72, layout: {sub: [box]}});
  assert.equal(result.canvas, 72);
  const painted = result.placements[1].painted_box;
  assert.deepEqual(Object.fromEntries(Object.entries(painted).map(([k, v]) => [k, Math.round(v * 1000) / 1000])), {x: 42, y: 42, w: 28, h: 28});
  assert.deepEqual(request.parts.sub.layout, [box]);
});

// Elements mode (side-pairs.html): a part's pieces, split and moved on their own. Straight-edged shapes, so their
// measured boxes are exact (curves are measured flattened).
const TWO = svg(54, '<rect x="6" y="6" width="20" height="20"/><rect x="30" y="30" width="16" height="16"/><path d="M38 30L38 20"/>');
function twoPieces() {
  const item = {reference_id: 'pair', parts: [{role: 'main', icon: 'main-54/m', form: null}, {role: 'sub', icon: 'sub-36/s', position: 'br', form: null}]};
  const drawings = new Map([['main-54/m', {svg: TWO, svg_sha256: 'm'}], ['sub-36/s', {svg: SUB, svg_sha256: 's'}]]);
  return {item, drawings};
}
// The main as one hand-placed group at scale 1: its source box [6, 6, 46, 46] where it is drawn.
const GROUP = {paths: [0, 1, 2], x: 6, y: 6, w: 40, h: 40};

test('pieces: elements whose strokes touch are one piece', () => {
  const parts = Side.elementParts(TWO);
  assert.deepEqual(parts.sources[0], [6, 6, 26, 26]);
  // the first rect stands alone; the second rect and the line that starts on its top edge touch
  assert.deepEqual(Side.connected(parts.segments, 4), [[0], [1, 2]]);
  // strokes 4 wide touch when their centerlines come within 4 units: 3 apart touch, 8 apart do not
  const near = Side.elementParts(svg(54, '<path d="M0 0L10 0"/><path d="M0 3L10 3"/><path d="M0 11L10 11"/>'));
  assert.deepEqual(Side.connected(near.segments, 4), [[0, 1], [2]]);
  // a curve counts too: a circle whose stroke meets a line
  const round = Side.elementParts(svg(54, '<circle cx="20" cy="20" r="10"/><path d="M33 20L45 20"/>'));
  assert.deepEqual(Side.connected(round.segments, 4), [[0, 1]]);
});

test('pieces: a group splits where its elements are drawn, and builds the same drawing', () => {
  const {item, drawings} = twoPieces();
  const parts = Side.elementParts(TWO);
  const pieces = Side.splitGroups([GROUP], parts.sources, Side.connected(parts.segments, 4));
  assert.deepEqual(pieces, [{paths: [0], x: 6, y: 6, w: 20, h: 20}, {paths: [1, 2], x: 30, y: 20, w: 16, h: 26}]);
  assert.deepEqual(Side.groupsBox(pieces), {x: 6, y: 6, w: 40, h: 40});
  // at scale 1 the split layout draws exactly what the one box drew
  const split = Side.pairRequest(item, drawings, {size: 72, layout: {main: pieces}});
  const oneBox = Side.pairRequest(item, drawings, {size: 72, layout: {main: [GROUP]}});
  assert.equal(split.svg, oneBox.svg);
  assert.deepEqual(split.request.parts.main.layout, pieces);
  // scaled (the automatic placement's box, rounded as the editor rounds it), every piece lands on whole units
  const auto = Side.pairRequest(item, drawings, {size: 72}).request.parts.main.layout[0];
  const box = {paths: [0, 1, 2], x: Math.round(auto.x), y: Math.round(auto.y), w: Math.round(auto.w), h: Math.round(auto.h)};
  const scaled = Side.splitGroups([box], parts.sources, Side.connected(parts.segments, 4));
  for (const p of scaled) for (const k of ['x', 'y', 'w', 'h']) assert.ok(Number.isInteger(p[k]), `${k} ${p[k]}`);
  assert.deepEqual(Side.groupsBox(scaled), {x: box.x, y: box.y, w: box.w, h: box.h});
  Side.pairRequest(item, drawings, {size: 72, layout: {main: scaled}});   // builds
});

test('pieces: moving one piece leaves the others where they are', () => {
  const {item, drawings} = twoPieces();
  const parts = Side.elementParts(TWO);
  const pieces = Side.splitGroups([GROUP], parts.sources, Side.connected(parts.segments, 4));
  const from = Side.groupsBox([pieces[0]]);
  const [moved] = Side.mapGroups([pieces[0]], from, {...from, x: from.x + 3, w: from.w - 2});
  assert.deepEqual(moved, {...pieces[0], x: pieces[0].x + 3, w: pieces[0].w - 2});
  const result = Side.pairRequest(item, drawings, {size: 72, layout: {main: [moved, pieces[1]]}});
  assert.deepEqual(result.request.parts.main.layout, [moved, pieces[1]]);
  assert.notEqual(result.svg, Side.pairRequest(item, drawings, {size: 72, layout: {main: pieces}}).svg);
  // resizing the whole part keeps the pieces' outer edges on the new box
  const all = Side.groupsBox(pieces), to = {x: all.x, y: all.y, w: all.w - 7, h: all.h - 5};
  assert.deepEqual(Side.groupsBox(Side.mapGroups(pieces, all, to)), to);
});

test('pieces: split into single paths keeps each where it is drawn; a straight line stays flat', () => {
  const parts = Side.elementParts(TWO);
  const singles = Side.splitGroups([{paths: [1, 2], x: 30, y: 20, w: 16, h: 26}], parts.sources, [[0], [1], [2]]);
  assert.deepEqual(singles, [{paths: [1], x: 30, y: 30, w: 16, h: 16}, {paths: [2], x: 38, y: 20, w: 0, h: 10}]);
});

test('pieces: a 64 pair builds from pieces too', () => {
  const main48 = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="4" '
    + 'stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="6" width="16" height="16"/><rect x="26" y="26" width="16" height="16"/></svg>';
  const sub32 = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="4" '
    + 'stroke-linecap="round" stroke-linejoin="round"><circle cx="16" cy="16" r="10"/></svg>';
  const item = {reference_id: 'pair64', parts: [{role: 'main', icon: 'solo/m', form: null}, {role: 'sub', icon: 'sub/s', position: 'br', form: null}]};
  const drawings = new Map([['solo/m', {svg: main48, svg_sha256: 'm'}], ['sub/s', {svg: sub32, svg_sha256: 's'}]]);
  const parts = Side.elementParts(main48);
  const pieces = Side.splitGroups([{paths: [0, 1], x: 4, y: 4, w: 36, h: 36}], parts.sources, Side.connected(parts.segments, 4));
  assert.equal(pieces.length, 2);
  const [moved] = Side.mapGroups([pieces[0]], Side.groupsBox([pieces[0]]), {x: 2, y: 2, w: 12, h: 12});
  const result = Side.pairRequest(item, drawings, {layout: {main: [moved, pieces[1]]}});
  assert.equal(result.result.canvas, 64);
  assert.deepEqual(result.request.parts.main.layout, [moved, pieces[1]]);
});
