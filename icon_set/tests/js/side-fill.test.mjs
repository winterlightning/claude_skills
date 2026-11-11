// side-fill-combine.js against the Python fill combine (side_fill/pick_combine.py).
//   node --test icon_set/tests/js/side-fill.test.mjs
// fixtures/side-fill/*.json.gz: real picks of every kind (stroke-fill, flat and outline mains and subs, layout picks,
// omitted elements, joined overlaps) combined by pick_combine.combine. They are made from the snapshot, which is data
// in R2, not in git: `python3 cloud/migrate/side_fill_data.py pull`, then `python3 -m icon_set side-fill goldens`.
// Without them these tests are skipped and say so.
// Shapely and Clipper round arcs differently, so the drawings are compared by area: the part of either drawing the
// other does not cover, less slivers thinner than 0.3 px along the edges, must stay under a square pixel.
import test from 'node:test';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {existsSync, readdirSync, readFileSync} from 'node:fs';
import {gunzipSync} from 'node:zlib';

const require = createRequire(import.meta.url);
const Fill = require('../../scripts/templates/side-fill-combine.js');
const folder = process.env.SIDE_FILL_GOLDENS || new URL('./fixtures/side-fill/', import.meta.url).pathname;
const cases = existsSync(folder) ? readdirSync(folder).filter(f => f.endsWith('.json.gz')).sort()
  .map(f => JSON.parse(gunzipSync(readFileSync(folder + f)))) : [];
const TOLERANCE = 1.0;   // px²
const skip = cases.length ? false : `no side fill goldens in ${folder}: pull the snapshot and run \`python3 -m icon_set side-fill goldens\``;

test('fill side pairs match the Python combine', {skip}, () => {
  assert.ok(cases.length >= 100, `side fill goldens missing (${folder})`);
  const failures = [], slow = [];
  let worst = 0;
  for (const c of cases) {
    const label = `${c.id} #${c.rank} ${c.variant} [${c.kind.join(' / ')}]`;
    const started = performance.now();
    let result;
    try { result = Fill.combine(c.pick); } catch (error) { failures.push(`${label}: ${error.stack.split('\n').slice(0, 3).join(' ')}`); continue; }
    const ms = performance.now() - started;
    if (ms > 1500) slow.push(`${label}: ${ms.toFixed(0)} ms`);
    const differs = Fill.differs(result.svg, c.expected.svg);
    worst = Math.max(worst, differs);
    if (differs > TOLERANCE) {
      failures.push(`${label}: ${differs.toFixed(2)} px² differ (area js ${result.area.toFixed(2)} py ${c.expected.area}; ` +
                    `main js ${result.main.area.toFixed(2)} py ${c.expected.main_area}; sub js ${result.sub.area.toFixed(2)} py ${c.expected.sub_area})`);
    }
  }
  assert.equal(failures.length, 0, `${failures.length} of ${cases.length} differ (worst ${worst.toFixed(2)} px²):\n` + failures.slice(0, 15).join('\n'));
  assert.equal(slow.length, 0, `slow combines:\n${slow.slice(0, 10).join('\n')}`);
});

// The layout editor's preview (side-fill-layout.js): a pick's own boxes sent back as the editor sends them give the
// same drawing as the pick, keyshape checks for both parts, and the 8px stress cut for a filled main.
test('the layout editor previews a pick as it is combined', {skip}, () => {
  const Layout = require('../../scripts/templates/side-fill-layout.js');
  const keyshapes = JSON.parse(readFileSync(new URL('../../data/side-fill/data/side-keyshapes.json', import.meta.url)));
  const picks = cases.filter(c => c.pick.main.layout?.every(b => b.paths) && c.pick.sub.layout?.every(b => b.paths)).slice(0, 25);
  assert.ok(picks.length >= 10, 'goldens with element boxes missing');
  for (const c of picks) {
    const position = c.id.slice(-2);
    // The editor locks a part to its drawing's keyshape, or to its own proportions ('own') when it has none.
    const locked = role => { const name = Layout.shapeName(keyshapes, role, Layout.sourceBounds(c.pick[role].source)); return name === 'custom' ? 'own' : name; };
    const change = role => ({mode: 'preset', shape: locked(role),
                             size: role === 'main' ? 48 : 32, units: c.pick[role].layout.map(b => ({...b, x: Math.round(b.x), y: Math.round(b.y), w: Math.round(b.w), h: Math.round(b.h)}))});
    const proposal = {position, main: change('main'), sub: change('sub')};
    const integral = ['main', 'sub'].every(role => c.pick[role].layout.every(b => ['x', 'y', 'w', 'h'].every(k => Number.isInteger(b[k]))));
    let result;
    try { result = Layout.preview({keyshapes, position, main: c.pick.main, sub: c.pick.sub, options: c.pick.options, proposal}); }
    catch (error) { if (error.message.includes('outside 64x64')) continue; throw error; }
    for (const role of ['main', 'sub']) {
      const check = result.candidate.keyshape_validation[role];
      assert.ok(check.guide_painted_box.length === 4 && typeof check.fits_keyshape === 'boolean', `${c.id}: ${role} check`);
    }
    if (integral) assert.ok(Fill.differs(result.svg, Fill.combine(c.pick).svg) < 0.01, `${c.id}: preview differs from the pick`);
    assert.equal(result.stress_svg === null, !!c.pick.main.outline, `${c.id}: stress cut only for a filled main`);
  }
});

// The 72 pairs (fixtures/side-fill-72, `python3 -m icon_set side-fill goldens72` from the 72 snapshot): fill-remake's
// own renders of real 72 picks (main-54 + sub-36 on 72, stroke-fill regions tucked 0.5 px), combined here at size 72.
const folder72 = process.env.SIDE_FILL_GOLDENS_72 || new URL('./fixtures/side-fill-72/', import.meta.url).pathname;
const cases72 = existsSync(folder72) ? readdirSync(folder72).filter(f => f.endsWith('.json.gz')).sort()
  .map(f => JSON.parse(gunzipSync(readFileSync(folder72 + f)))) : [];
const skip72 = cases72.length ? false : `no 72 side fill goldens in ${folder72}: import the 72 snapshot and run \`python3 -m icon_set side-fill goldens72\``;

// A part drawn with SVG transforms cannot be split into elements here (CombineSide.elementParts refuses it), so the
// page places it whole in its boxes where Python bakes the transforms and moves each box's elements: those picks are
// listed, not held to the tolerance (12 of the 1,369 72 parts; the 64 set has the same few).
const transformed = c => ['main', 'sub'].some(role => /\btransform=/.test(c.pick[role].source));

test('72 fill side pairs match the Python combine at 72', {skip: skip72}, () => {
  assert.ok(cases72.length >= 100, `72 side fill goldens missing (${folder72})`);
  const failures = [], slow = [], known = [];
  let worst = 0;
  for (const c of cases72) {
    const label = `${c.id} #${c.rank} ${c.variant} [${c.kind.join(' / ')}]`;
    const started = performance.now();
    let result;
    try { result = Fill.combine(c.pick); } catch (error) { failures.push(`${label}: ${error.stack.split('\n').slice(0, 3).join(' ')}`); continue; }
    if (performance.now() - started > 1500) slow.push(`${label}: ${(performance.now() - started).toFixed(0)} ms`);
    assert.ok(result.svg.includes('viewBox="0 0 72 72"'), `${label}: not drawn on the 72 canvas`);
    const differs = Fill.differs(result.svg, c.expected.svg);
    if (transformed(c)) { if (differs > TOLERANCE) known.push(`${label}: ${differs.toFixed(2)} px²`); continue; }
    worst = Math.max(worst, differs);
    if (differs > TOLERANCE) failures.push(`${label}: ${differs.toFixed(2)} px² differ (area js ${result.area.toFixed(2)} py ${c.expected.area})`);
  }
  if (known.length) console.log(`# ${known.length} picks of a transformed drawing placed whole:\n# ` + known.join('\n# '));
  assert.ok(known.length <= 5, `more transformed drawings than expected: ${known.length}`);
  assert.equal(failures.length, 0, `${failures.length} of ${cases72.length} differ (worst ${worst.toFixed(2)} px²):\n` + failures.slice(0, 15).join('\n'));
  assert.equal(slow.length, 0, `slow combines:\n${slow.slice(0, 10).join('\n')}`);
});

test('the layout editor previews a 72 pick on the 72 canvas', {skip: skip72}, () => {
  const Layout = require('../../scripts/templates/side-fill-layout.js');
  const base = JSON.parse(readFileSync(new URL('../../data/side-fill/data/side-keyshapes.json', import.meta.url)));
  // The 72 keyshapes are the 48 / 32 ones scaled 72/64 (side-fill-data.js keyshapes()).
  const keyshapes = Object.fromEntries(Object.entries(base).map(([role, t]) => [role, Object.fromEntries(Object.entries(t).map(([n, b]) => [n, b.map(v => v * 72 / 64)]))]));
  const integral = c => ['main', 'sub'].every(role => c.pick[role].layout?.every(b => b.paths && ['x', 'y', 'w', 'h'].every(k => Number.isInteger(b[k]))));
  const picks = cases72.filter(c => integral(c) && !transformed(c)).slice(0, 25);
  assert.ok(picks.length >= 10, 'integral 72 goldens missing');
  for (const c of picks) {
    const position = c.id.slice(-2);
    const change = role => ({units: c.pick[role].layout.map(b => ({...b}))});
    const result = Layout.preview({keyshapes, position, main: c.pick.main, sub: c.pick.sub, options: null, size: 72,
                                   proposal: {position, main: change('main'), sub: change('sub')}});
    assert.ok(Fill.differs(result.svg, Fill.combine(c.pick).svg) < 0.01, `${c.id}: preview differs from the pick`);
    assert.equal(result.stress_svg === null, !!c.pick.main.outline, `${c.id}: stress cut only for a filled main`);
    if (result.stress_svg) assert.ok(result.stress_svg.includes('viewBox="0 0 72 72"'), `${c.id}: stress cut not on 72`);
    for (const role of ['main', 'sub']) assert.equal(typeof result.candidate.keyshape_validation[role].fits_keyshape, 'boolean');
  }
});
