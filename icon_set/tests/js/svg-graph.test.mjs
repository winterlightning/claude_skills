// svg-graph.js against svg_graph.py: graph-goldens.json (make_graph_goldens.py) holds the Python graph of every
// combined drawing in container-goldens.json plus shapes for each converter. The graphs must be identical.
//   node --test icon_set/tests/js
import test from 'node:test';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {readFileSync} from 'node:fs';

const require = createRequire(import.meta.url);
const SvgGraph = require('../../scripts/templates/svg-graph.js');
const cases = JSON.parse(readFileSync(new URL('./graph-goldens.json', import.meta.url)));

test('graphs match svg_graph.py', () => {
  assert.ok(cases.length >= 100);
  for (const c of cases) {
    const g = c.graph;
    const actual = SvgGraph.fromSvg(c.svg, {canvas: g.canvas_size, family: g.family, icon_id: g.icon_id, name: g.name, profile: g.profile});
    assert.deepEqual(actual, g, c.name);
  }
});
