'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const PC = require('./profile-config.js');
const source = () => JSON.parse(fs.readFileSync(path.join(__dirname, '../../core/icon_profiles.json'), 'utf8'));

test('canonical profiles resolve inheritance, native aliases and shared validation', () => {
  const raw = source(), before = JSON.stringify(raw), profiles = PC.resolve(raw);
  assert.equal(profiles.container.strokeWidth, 4);
  assert.equal(profiles.container.shipCanvas, 64);
  assert.equal(profiles.container.designCanvas, 64);
  assert.equal(profiles.sub.validation.minimumDistinctCenterlineDistance, 3);
  assert.equal(profiles.normal.validation.minimumDistinctCenterlineDistance, 4);
  assert.deepEqual(profiles.container.center, { x: 32, y: 32 });
  assert.equal(JSON.stringify(raw), before);
});
test('new profiles can inherit, override validation and clear inherited slots', () => {
  const raw = source();
  raw.profiles.badge = { label: 'Badge', extends: 'container', containerSlot: null, validation: { minimumSolidFillDepth: 0 } };
  const resolved = PC.resolve(raw).badge;
  assert.equal(resolved.canvas, 64); assert.equal(resolved.strokeWidth, 4);
  assert.equal(resolved.validation.minimumSolidFillDepth, 0);
  assert.ok(!Object.hasOwn(resolved, 'containerSlot'));
});
test('unknown fields, unsafe names, invalid defaults and inherited cycles are rejected', () => {
  const mutations = [
    raw => { raw.unexpected = true; },
    raw => { raw.defaultIconType = 'missing'; },
    raw => { raw.profiles.constructor = raw.profiles.normal; },
    raw => { raw.profiles.prototype = raw.profiles.normal; },
    raw => { raw.profiles.normal.label = ''; },
    raw => { raw.profiles.normal.canvas = 48.5; },
    raw => { raw.profiles.normal.validation = { gridStep: 0 }; },
    raw => { raw.profiles.normal.validation = { gridStep: 3, majorGridStep: 4 }; },
    raw => { raw.profiles.normal.validation = { gridStep: 1e-300, majorGridStep: 1e300 }; },
    raw => { raw.profiles.normal.extends = 'container'; },
    raw => { delete raw.validationDefaults.geometryTolerance; },
  ];
  for (const mutate of mutations) { const raw = source(); mutate(raw); assert.throws(() => PC.resolve(raw)); }
});
test('keyshape geometry must fit canvas and stroke with matching orientation', () => {
  for (const mutate of [
    token => { token.width = 2; }, token => { token.width = 100; },
    token => { token.orientation = 'portrait'; }, token => { token.diameter = 40; },
    token => { token.shape = 'path'; }, token => { token.style = 'fill:red'; },
  ]) { const raw = source(); mutate(raw.profiles.normal.keyshapes[1]); assert.throws(() => PC.resolve(raw)); }
});
test('slot rejects self acceptance, undersized clear area and off-center geometry', () => {
  for (const mutation of [
    slot => { slot.minimumClearSquare = 31; }, slot => { slot.minimumClearSquare = 33; },
    slot => { slot.x = 16.0000000001; }, slot => { slot.acceptedProfile = 'missing'; },
    slot => { slot.acceptedProfile = 'container'; slot.w = slot.h = slot.minimumClearSquare = 64; slot.x = slot.y = 0; },
  ]) { const raw = source(); mutation(raw.profiles.container.containerSlot); assert.throws(() => PC.resolve(raw)); }
});
test('indirect slot cycles are rejected without unbounded traversal', () => {
  const raw = source(); raw.profiles.frame = { label: 'Frame', extends: 'sub', containerSlot: { x: 0, y: 0, w: 32, h: 32, minimumClearSquare: 32, acceptedProfile: 'sub' } };
  raw.profiles.sub.containerSlot = { x: 0, y: 0, w: 32, h: 32, minimumClearSquare: 32, acceptedProfile: 'frame' };
  assert.throws(() => PC.resolve(raw), /cyclic accepted profile/);
});
test('duplication is detached and deletion protects default and dependent profiles', () => {
  const raw = source(), copy = PC.duplicate(raw, 'normal', 'toolbar');
  copy.profiles.toolbar.keyshapes[0].width = 1;
  assert.equal(raw.profiles.normal.keyshapes[0].width, 44);
  assert.throws(() => PC.remove(raw, 'normal'), /default/);
  assert.throws(() => PC.remove(raw, 'sub'), /dependent/);
  const clean = PC.duplicate(raw, 'normal', 'toolbar');
  assert.ok(!Object.hasOwn(PC.remove(clean, 'toolbar').profiles, 'toolbar'));
  assert.throws(() => PC.duplicate(raw, 'normal', '__proto__'));
});
test('profile preview grid display is bounded and finite', () => {
  assert.deepEqual(PC.gridCoordinates(8, 2), [0, 2, 4, 6, 8]);
  for (const [canvas, step] of [[80, 1e-300], [1e308, 1e-300], [1e308, 1e308], [80, 2]]) {
    const coordinates = PC.gridCoordinates(canvas, step);
    assert.ok(coordinates.length <= 257); assert.ok(coordinates.every(Number.isFinite));
  }
});
