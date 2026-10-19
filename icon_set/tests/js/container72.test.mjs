import test from 'node:test';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {readFileSync} from 'node:fs';
const require = createRequire(import.meta.url);
const C = require('../../scripts/templates/combine.js');
const S = require('../../scripts/templates/combine-side.js');
const P = require('../../scripts/templates/container-placement.js');
const fixtures = JSON.parse(readFileSync(new URL('./container72-fixtures.json', import.meta.url)));
const points = svg => S.engineSegments(svg).flat().map(p => p.map(n => +n.toFixed(2)));
for (const f of fixtures) test('native72 preserves recorded geometry: ' + f.name, () => {
  const result = C.container(f.main, f.symbol, f.placement);
  assert.deepEqual(points(result.svg), points(f.expected));
  const saved = C.container(f.main, f.symbol, {...f.placement, box: result.layout.symbol[0]});
  assert.equal(saved.svg, result.svg, 'save/reload retains fractional geometry');
});
const item = {reference_id: 'pair', parts: [{role: 'container', icon: 'container-72/a', current_sha: 'c'}, {role: 'symbol', icon: 'symbol-36/a', current_sha: 's'}]};
const proposal = {container:'container-72/a', symbol:'symbol-36/a', container_sha256:'c', symbol_sha256:'s', center:[36,30.5], offset:[0,-1], size:28, status:'accepted'};
const defaults = {canvas:72, containers:{'container-72/a':{sha256:'c',room:{center:[36,31],clear_square_side:32,symbol_guide_size:32,status:'provisional'}}},pairs:{pair:{...proposal,proposal}}};
test('accepted pair geometry wins over room; saved edits win over both', () => {
  assert.deepEqual(P.placementOf(item,{},true,defaults).center,[36,29.5]);
  const edited = structuredClone(item); edited.parts[1].layout=[{x:21.5,y:19,w:27,h:24,scope:'pair'}];
  assert.deepEqual(P.placementOf(edited,{},true,defaults).box,{x:21.5,y:19,w:27,h:24});
  assert.deepEqual(P.placementOf(item,{},false,defaults).center,[36,31]);
});
test('unaccepted or stale proposals are never silently applied', () => {
  const d=structuredClone(defaults);d.pairs.pair.proposal.status='propose';
  const p=P.placementOf(item,{},true,d);assert.deepEqual(p.center,[36,31]);assert.ok(p.proposal);
  const changed=structuredClone(item);changed.parts[1].current_sha='new';
  const stale=P.placementOf(changed,{},true,defaults);assert.deepEqual(stale.center,[36,31]);assert.match(stale.note,/older artwork/);
  changed.parts[0].current_sha='new-container';assert.equal(P.placementOf(changed,{},true,defaults).needsReview,true);
});
