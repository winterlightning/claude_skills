// container-placement.js: which placement a container pair's symbol takes, and the layouts the page stores.
//   node --test icon_set/tests/js/*.test.mjs
import test from 'node:test';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';

const require = createRequire(import.meta.url);
const P = require('../../scripts/templates/container-placement.js');

const pair = (layout, {container = 'container/box', symbol = 'symbol/plus'} = {}) => ({reference_id: 'r', parts: [
  {role: 'container', icon: container}, {role: 'symbol', icon: symbol, layout, updated_by: 'ray'}]});
const BOX = {x: 20, y: 20, w: 24, h: 24};
const DEFAULTS = {containers: {box: {center: [30, 34], source: 'anchor'}}, pairs: {box: {star: [28, 28]}}};

test('a box saved before placements had scopes stays the pair\'s own', () => {
  const p = P.placementOf(pair([BOX]), {}, true, DEFAULTS);
  assert.deepEqual(p.box, BOX);
  assert.equal(p.pinned, true);
  assert.equal(p.scope, 'pair');
});

test('a box built on the defaults or on the container follows them', () => {
  assert.deepEqual(P.placementOf(pair([{...BOX, scope: 'default'}]), {}, true, DEFAULTS).center, [30, 34]);
  const target = {center: [32, 40], size: [20, 20]};
  const p = P.placementOf(pair([{...BOX, scope: 'container', container: target}]), {}, true, DEFAULTS);
  assert.deepEqual([p.center, p.ink, p.saved], [[32, 40], [20, 20], 'container']);
  // An unscoped box carrying a container placement is not a hand box either.
  assert.equal(P.placementOf(pair([{...BOX, container: target}]), {}, true, DEFAULTS).saved, 'container');
});

test('order: pair box, saved container, published pair override, container default, centre', () => {
  assert.equal(P.placementOf(pair([{...BOX, scope: 'pair'}]), {}, true, DEFAULTS).label, 'Saved · this pair');
  assert.equal(P.placementOf(pair([{...BOX, scope: 'pair'}]), {}, false, DEFAULTS).label, 'Default · container anchor');
  assert.equal(P.placementOf(pair(null, {symbol: 'symbol/star'}), {}, true, DEFAULTS).label, 'Default · pair override');
  assert.deepEqual(P.placementOf(pair(null, {container: 'container/other'}), {}, true, DEFAULTS).center, [32, 32]);
  // Another symbol picked in the editor drops the pair's own box.
  assert.equal(P.placementOf(pair([BOX]), {symbol: 'symbol/star'}, true, DEFAULTS).label, 'Default · pair override');
});

test('a pair centre carried over without a box (0 x 0 placeholder) places the symbol from it', () => {
  const p = P.placementOf(pair([{x: 0, y: 0, w: 0, h: 0, scope: 'pair', center: [33, 30], size: null}]), {}, true, DEFAULTS);
  assert.deepEqual([p.box, p.center, p.ink, p.pinned], [undefined, [33, 30], null, true]);
  assert.equal(P.savedBox(pair([{x: 0, y: 0, w: 0, h: 0}]).parts[1]), null);
  assert.deepEqual(P.savedBox(pair([{x: 4, y: 30, w: 20, h: 0}]).parts[1]), {x: 4, y: 30, w: 20, h: 0}, 'a flat rule is a box');
});

test('a saved container placement applies only on the container it was saved for', () => {
  const target = {center: [32, 40], size: null};
  const item = pair([{...BOX, scope: 'container', container: target}]);
  assert.equal(P.placementOf(item, {container: 'container/other'}, true, DEFAULTS).saved, undefined);
  // The editor's save builds the pair on the container it picked (container-pairs.html `followed`).
  const followed = {...item, parts: item.parts.map(p => p.role === 'container' ? {...p, icon: 'container/other'} : p)};
  assert.equal(P.placementOf(followed, {container: 'container/other'}, false, DEFAULTS).saved, 'container');
});

test('builds mark the layout with the placement they came from', () => {
  const boxes = [{paths: [0], ...BOX}];
  assert.equal(P.builtLayout(boxes, {box: BOX, pinned: true})[0].scope, 'pair');
  assert.equal(P.builtLayout(boxes, {center: [1, 1], saved: 'container'})[0].scope, 'container');
  const kept = {center: [32, 40], size: null};
  assert.deepEqual(P.builtLayout(boxes, {center: [32, 32]}, kept)[0], {paths: [0], ...BOX, scope: 'default', container: kept});
});

test('a container-wide save keeps each pair\'s own placement and moves the rest', () => {
  const target = {center: [32, 40], size: [24, 24]};
  assert.equal(P.containerLayout(pair([BOX]), target)[0].scope, 'pair');
  assert.deepEqual(P.containerLayout(pair([{...BOX, scope: 'default'}]), target, {x: 1, y: 2, w: 3, h: 4})[0],
                   {x: 1, y: 2, w: 3, h: 4, scope: 'container', container: target});
  // Removing it: the pair goes back to the defaults, not to a hand box.
  const removed = P.containerLayout(pair([{...BOX, scope: 'container', container: target}]), null)[0];
  assert.deepEqual(removed, {...BOX, scope: 'default'});
  assert.equal(P.placementOf({...pair(null), parts: [{role: 'container', icon: 'container/box'}, {role: 'symbol', icon: 'symbol/plus', layout: [removed]}]},
                             {}, true, DEFAULTS).label, 'Default · container anchor');
  assert.equal(P.containerLayout(pair(null), target), null, 'nothing to store without a box');
});
