'use strict';

// Run: node --test frontend/js/geometry.test.js
const test = require('node:test');
const assert = require('node:assert/strict');
const G = require('./geometry.js');
const element = (tag, attrs) => ({ id: 'contour', tag, attrs });

test('seven starters are independent editable native geometry', () => {
  assert.equal(G.STARTERS.length, 7);
  for (const starter of G.STARTERS) {
    const checked = G.validateElement(element(starter.tag, starter.attrs));
    assert.equal(checked.tag, starter.tag);
    assert.notEqual(checked.attrs, starter.attrs);
    assert.ok(!Object.hasOwn(checked, 'shapeId'));
  }
});
test('independent radii, arbitrary coordinates, cubic control points, and zero-length dots', () => {
  assert.deepEqual(G.validateElement(element('rect', { x: '1.25', y: -2, width: 5, height: 6, rx: 1, ry: 2 })).attrs,
    { x: 1.25, y: -2, width: 5, height: 6, rx: 1, ry: 2 });
  assert.doesNotThrow(() => G.validateElement(element('path', { d: 'M.2-.3C1.4 2.5 3.6 4.7 5.8 6.9' })));
  assert.doesNotThrow(() => G.validateElement(element('line', { x1: 3, y1: 4, x2: 3, y2: 4 })));
});
test('all SVG path commands and implicit repetitions parse', () => {
  const commands = G.pathCommands('m1 2 3 4 l5 6 h7 v8 c1 2 3 4 5 6 s7 8 9 10 q1 2 3 4 t5 6 a2 3 45 0 1 7 8 z M20 20 L30 30 H40 V30 C1 2 3 4 5 6 S7 8 9 10 Q1 2 3 4 T5 6 A2 3 45 1 0 7 8 Z');
  assert.deepEqual(commands.slice(0, 11).map(item => item.command), ['m', 'l', 'l', 'h', 'v', 'c', 's', 'q', 't', 'a', 'z']);
});
test('translations preserve relative curves, subpaths, arc radii and rotations', () => {
  const d = 'm1 2 3 4 h5 v6 c1 2 3 4 5 6 s1 2 3 4 q1 2 3 4 t5 6 a2 3 45 0 1 7 8 z m1 1';
  const moved = G.translate(element('path', { d }), 10, -2);
  assert.equal(moved.attrs.d, 'M 11 0 L 14 4 H 19 V 10 C 20 12 22 14 24 16 S 25 18 27 20 Q 28 22 30 24 T 35 30 A 2 3 45 0 1 42 38 Z M 12 1');
  assert.equal(d.startsWith('m1 2'), true);
});
test('native and points translations produce no transforms', () => {
  assert.deepEqual(G.translate(element('circle', { r: 2 }), 3, 4).attrs, { r: 2, cx: 3, cy: 4 });
  assert.deepEqual(G.translate(element('rect', { width: 8, height: 6, rx: 1, ry: 2 }), 3, 4).attrs, { width: 8, height: 6, rx: 1, ry: 2, x: 3, y: 4 });
  assert.equal(G.translate(element('polygon', { points: '1,2 3,4 5,6' }), -1, 2).attrs.points, '0 4 2 6 4 8');
});
test('unsafe SVG, styles, markup, transforms and prototype fields are rejected', () => {
  for (const tag of ['script', 'image', 'use', 'foreignObject', '__proto__']) assert.throws(() => G.validateElement(element(tag, {})));
  for (const key of ['onload', 'onclick', 'href', 'xlink:href', 'style', 'fill', 'stroke', 'transform', '__proto__']) {
    assert.throws(() => G.validateElement(element('circle', JSON.parse(`{"r":2,"${key}":"url(https://example.com)"}`))));
  }
  assert.throws(() => G.validateElement({ ...element('circle', { r: 2 }), transform: 'rotate(10)' }));
  assert.throws(() => G.validateElement(element('path', { d: 'M0 0<image href="remote"/>' })));
});
test('invalid and nonfinite geometry never reaches rendering', () => {
  for (const value of [Infinity, NaN, null, true, '', '0x10', '1e999', 'url(test)', [], {}]) assert.throws(() => G.validateElement(element('circle', { r: value })));
  for (const d of ['M0', 'L0 0', 'M0 0 L', 'M0 0 Z 1 2', 'M0 0X1 2', 'M0,,0', 'M0 0,', 'M,0 0', 'M0 0 A-2 3 0 0 1 4 5', 'M0 0 A2 3 0 2 1 4 5']) assert.throws(() => G.pathCommands(d), d);
  for (const attrs of [{ width: 0, height: 2 }, { width: 2, height: 3, rx: -1 }]) assert.throws(() => G.validateElement(element('rect', attrs)));
  assert.throws(() => G.validateElement(element('polyline', { points: '1 2 3' })));
  assert.throws(() => G.validateElement(element('polygon', { points: '1 2 3 4' })));
  assert.throws(() => G.translate(element('circle', { cx: 1e308, r: 2 }), 1e308, 0));
});
test('ids are safe and unique; optional roles are plain text', () => {
  assert.throws(() => G.validateElements([element('line', {}), element('line', {})]));
  assert.throws(() => G.validateElement({ ...element('line', {}), id: 'unsafe"' }));
  assert.throws(() => G.validateElement({ ...element('line', {}), role: { bad: 'object' } }));
  assert.equal(G.validateElement({ ...element('line', {}), role: '<script>not markup</script>' }).role, '<script>not markup</script>');
});
