// side-fill-combine.js against the Python fill combine (side_fill/pick_combine.py).
//   node --test icon_set/tests/js/side-fill.test.mjs
// fixtures/side-fill/*.json.gz: real picks of every kind (stroke-fill, flat and outline mains and subs, layout picks,
// omitted elements, joined overlaps) combined by pick_combine.combine (`python3 -m icon_set side-fill goldens`).
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

test('fill side pairs match the Python combine', () => {
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
test('the layout editor previews a pick as it is combined', () => {
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
