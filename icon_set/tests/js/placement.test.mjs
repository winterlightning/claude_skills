// container-placement.js: which placement a container pair's symbol takes, and the layouts the page stores.
//   node --test icon_set/tests/js/*.test.mjs
import test from 'node:test';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';

const require = createRequire(import.meta.url);
const P = require('../../scripts/templates/container-placement.js');
const Combine = require('../../scripts/templates/combine.js');

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

const targetPair = (id, options = {}) => ({...pair([{...BOX, scope: 'pair', container: {center: [30, 30], size: null}}], options), reference_id: id});

function transferSetup(items, overrides = {}) {
  const calls = [], reports = [];
  return {calls, reports, options: {
    sourceId: 'source', containerKey: 'container/box', box: BOX, targetIds: items.map(item => item.reference_id),
    saveSource: async () => { calls.push('source'); return {ok: true}; },
    loadPairs: async () => { calls.push('refresh'); return items; },
    loadArtwork: async () => {},
    makeRequest: (item, {box, pinned}) => ({reference_id: item.reference_id, parts: {symbol: {
      icon: P.part(item, 'symbol').icon,
      layout: P.builtLayout([{paths: [0], ...box}], {pinned}, P.layoutOf(P.part(item, 'symbol')).container)
    }}}),
    build: async requests => { calls.push(requests); return requests.map(() => ({ok: true})); },
    onResult: result => reports.push(result), ...overrides
  }};
}

test('related pairs match exact drawing identity and exclude the source', () => {
  const items = [targetPair('source'), targetPair('same'), targetPair('variant', {container: 'container/box-v2'}), targetPair('missing', {container: null})];
  assert.deepEqual(P.relatedPairs(items, 'container/box', 'source').map(item => item.reference_id), ['same']);
  assert.deepEqual(P.relatedPairs(items, null, 'source'), []);
});

test('selected targets get pair boxes and keep their symbols and container defaults', async () => {
  const items = [targetPair('a'), targetPair('b', {symbol: 'symbol/star'}), targetPair('unselected')];
  const before = structuredClone(items), f = transferSetup(items, {targetIds: ['a', 'b', 'a', 'source']});
  await P.applySelected(f.options);
  assert.deepEqual(f.calls.slice(0, 2), ['source', 'refresh']);
  const requests = f.calls[2];
  assert.deepEqual(requests.map(r => r.reference_id), ['a', 'b']);
  assert.equal(requests[1].parts.symbol.icon, 'symbol/star');
  for (const request of requests) {
    const layout = request.parts.symbol.layout;
    assert.equal(layout[0].scope, 'pair');
    assert.deepEqual(P.savedBox({layout}), BOX);
    assert.deepEqual(layout[0].container, {center: [30, 30], size: null});
    assert.deepEqual(P.placementOf(pair(layout, {symbol: request.parts.symbol.icon}), {}, true).box, BOX);
  }
  assert.deepEqual(items, before, 'original target data, including unselected pairs, is untouched');
});

test('different symbol proportions are baked into the exact target box', () => {
  const svg = (size, body) => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${size} ${size}" fill="none" stroke="black" stroke-width="4">${body}</svg>`;
  const main = svg(64, '<rect x="4" y="4" width="56" height="56" rx="4"/>');
  for (const symbol of [svg(32, '<rect x="6" y="12" width="20" height="8"/>'), svg(32, '<path d="M 16 4 L 28 26 L 4 26 Z"/>')]) {
    const result = Combine.container(main, symbol, {box: BOX});
    assert.deepEqual(P.savedBox({layout: result.layout.symbol}), BOX);
    assert.match(result.svg, /stroke-width="4"/);
  }
});

test('source save failure prevents all target reads and writes', async () => {
  const f = transferSetup([targetPair('a')], {saveSource: async () => ({ok: false, error: 'Source rejected'})});
  await assert.rejects(P.applySelected(f.options), /Source rejected/);
  assert.deepEqual(f.calls, []);
});

test('changed containers, missing drawings and invalid fits are isolated per target', async () => {
  const f = transferSetup([targetPair('changed', {container: 'container/other'}), targetPair('missing', {symbol: null}), targetPair('invalid'), targetPair('ok')]);
  const make = f.options.makeRequest;
  f.options.makeRequest = (item, placement) => { if (item.reference_id === 'invalid') throw Error('Flat element cannot take this box'); return make(item, placement); };
  const result = await P.applySelected(f.options);
  assert.deepEqual(result.results.map(r => [r.reference_id, r.ok]), [['changed', false], ['missing', false], ['invalid', false], ['ok', true]]);
  assert.equal(f.calls[2].length, 1);
});

test('batches retain earlier successes on a network failure and mark remaining targets unattempted', async () => {
  const f = transferSetup(Array.from({length: 110}, (_, i) => targetPair(String(i))));
  let batches = 0;
  f.options.build = async requests => {
    assert.ok(requests.length <= 50);
    if (++batches === 2) throw Error('Network error');
    return requests.map((_, i) => i === 1 ? {ok: false, error: 'Conflict'} : {ok: true, build_failed: i === 0, errors: i === 0 ? ['Review needed'] : []});
  };
  const result = await P.applySelected(f.options);
  assert.equal(batches, 2);
  assert.equal(result.results.length, 110);
  assert.equal(result.results.filter(r => r.ok).length, 49);
  assert.equal(result.results[0].build_failed, true);
  assert.match(result.results[50].error, /not confirmed/);
  assert.match(result.results[100].error, /Not attempted/);
  assert.equal(f.reports.length, 110);
});

test('a refresh failure after saving the source reports every selected target', async () => {
  const f = transferSetup([targetPair('a'), targetPair('b')], {loadPairs: async () => { throw Error('Unavailable'); }});
  const result = await P.applySelected(f.options);
  assert.equal(result.source.ok, true);
  assert.equal(result.results.length, 2);
  assert.ok(result.results.every(r => !r.ok && /refresh/.test(r.error)));
  assert.deepEqual(f.calls, ['source']);
});
