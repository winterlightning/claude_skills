'use strict';

// DOM-independent editor behavior regression tests. Real-browser pointer,
// rendering, and visual checks complement these tests.
// Run: node --test frontend/js/*.test.js
const test = require('node:test');
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
const path = require('node:path');

function editor() {
  class Element {
    constructor(tag) {
      this.tagName = tag.toUpperCase(); this.children = []; this.attrs = {}; this.dataset = {}; this.style = {}; this.value = '';
      this.classList = { toggle() {} }; this.handlers = {};
    }
    setAttribute(name, value) { this.attrs[name] = String(value); }
    appendChild(child) { this.children.push(child); child.parentNode = this; return child; }
    replaceChildren(...children) { this.children = []; children.forEach(child => this.appendChild(child)); }
    addEventListener(name, callback) { this.handlers[name] = callback; }
    focus() {}
    getBBox() { return { x: 0, y: 0, width: 20, height: 20 }; }
  }
  const elements = new Map();
  const document = {
    getElementById(id) { if (!elements.has(id)) elements.set(id, new Element('div')); return elements.get(id); },
    createElement: tag => new Element(tag), createElementNS: (_, tag) => new Element(tag), addEventListener() {},
  };
  const context = vm.createContext({ document, localStorage: { getItem() { return null; }, setItem() {} }, window: { document }, console, setTimeout });
  for (const filename of ['icon-profiles.js', 'geometry.js', 'app.js']) vm.runInContext(fs.readFileSync(path.join(__dirname, filename), 'utf8'), context, { filename });
  const run = code => vm.runInContext(code, context);
  const read = code => JSON.parse(run(`JSON.stringify(${code})`));
  return { run, read, elements };
}
const document = {
  schemaVersion: 2, name: 'test-icon', iconType: 'normal', canvas: 48, strokeWidth: 4,
  keyfitCheck: { targetToken: 'square-40' },
  sourceAnalysis: { incomplete: false, references: [{ name: 'lucide-reference' }], relationships: [], spacingChecks: [] },
  elements: [{ id: 'outer', role: 'outline', tag: 'path', attrs: { d: 'M6 24 Q10 6 24 6 C36 6 42 18 42 24' } }],
};

test('editor boots with seven starters and shared profiles without a registry', () => {
  const app = editor();
  assert.equal(app.elements.get('palette-geometry').children.length, 7);
  assert.equal(app.elements.get('canvas').attrs.viewBox, '0 0 48 48');
  assert.equal(app.run('typeof SHAPES'), 'undefined');
});
test('import and export preserve exact geometry, references and extra metadata', () => {
  const app = editor();
  const source = { ...document, projectNotes: { preserved: true }, keyfitCheck: { targetToken: 'square-40', mode: 'optical', rationale: 'Narrow symbol.' } };
  app.run(`importDocument(${JSON.stringify(source)})`);
  assert.deepEqual(app.read('editableDocument()'), source);
});
test('invalid imports leave the current document and undo history untouched', () => {
  const app = editor(); app.run(`importDocument(${JSON.stringify(document)})`);
  const before = app.read('editableDocument()'), historyLength = app.run('history.length');
  const unsafe = { ...document, elements: [{ id: 'bad', tag: 'circle', attrs: { r: 2, style: 'fill:red' } }] };
  assert.throws(() => app.run(`importDocument(${JSON.stringify(unsafe)})`), /not a geometry attribute/);
  assert.deepEqual(app.read('editableDocument()'), before);
  assert.equal(app.run('history.length'), historyLength);
});
test('legacy placements are rejected with an actionable migration explanation', () => {
  const app = editor();
  assert.throws(() => app.run(`validateDocument(${JSON.stringify({ ...document, schemaVersion: 1, instances: [] })})`), /migrated/);
  assert.throws(() => app.run(`validateDocument(${JSON.stringify({ ...document, instances: [] })})`), /migrated/);
});
test('profile canvas, stroke and keyshape mismatches are rejected', () => {
  const app = editor();
  for (const change of [{ canvas: 24 }, { strokeWidth: 2 }, { iconType: 'sub' }, { keyfitCheck: { targetToken: 'missing' } }, { iconType: '__proto__' }]) {
    assert.throws(() => app.run(`validateDocument(${JSON.stringify({ ...document, ...change })})`));
  }
});
test('geometry edits invalidate QA, preserve references, and undo restores both', () => {
  const app = editor(); app.run(`importDocument(${JSON.stringify(document)}); state.selectedId = 'outer'; moveSelected(0.5, 1.25);`);
  const changed = app.read('editableDocument()');
  assert.equal(changed.sourceAnalysis.incomplete, true);
  assert.deepEqual(changed.sourceAnalysis.references, document.sourceAnalysis.references);
  assert.match(changed.elements[0].attrs.d, /^M 6.5 25.25/);
  assert.ok(!Object.hasOwn(changed.elements[0].attrs, 'transform'));
  app.run('undo()'); assert.deepEqual(app.read('editableDocument()'), document);
});
test('duplicate has an independent attrs object and unique id', () => {
  const app = editor(); app.run(`importDocument(${JSON.stringify(document)}); state.selectedId = 'outer'; duplicateSelected();`);
  const items = app.read('state.elements'); assert.equal(items.length, 2); assert.notEqual(items[0].id, items[1].id);
  app.run("state.elements[1].attrs.d = 'M0 0 L1 1'");
  assert.equal(app.read('state.elements')[0].attrs.d, document.elements[0].attrs.d);
});
test('container preview keeps the full slot and accepted sub guide', () => {
  const app = editor();
  const source = { ...document, iconType: 'container', canvas: 64, keyfitCheck: { targetToken: 'square-56' }, containerSlot: { x: 16, y: 16, w: 32, h: 32, acceptedKeyshape: 'circle-32' } };
  app.run(`importDocument(${JSON.stringify(source)})`);
  assert.equal(app.elements.get('canvas').attrs.viewBox, '0 0 64 64');
  assert.equal(app.elements.get('ship-preview').attrs.width, '32');
  assert.equal(app.elements.get('keyshape-guide').children.length, 3);
  const slot = app.elements.get('keyshape-guide').children.find(child => child.dataset.containerSlotGuide === 'true');
  assert.deepEqual([slot.attrs.x, slot.attrs.y, slot.attrs.width, slot.attrs.height], ['16', '16', '32', '32']);
  assert.deepEqual(app.read('editableDocument()'), source);
});
test('native SVG preview has central paint and no imported transform/style', () => {
  const app = editor(); app.run(`importDocument(${JSON.stringify(document)})`);
  const preview = app.run('documentElementSVG(editableDocument())');
  assert.equal(preview.attrs['stroke-width'], '4'); assert.equal(preview.attrs['stroke-linejoin'], 'round'); assert.equal(preview.attrs.fill, 'none');
  assert.equal(preview.children[0].attrs.d, document.elements[0].attrs.d);
  assert.ok(!Object.hasOwn(preview.children[0].attrs, 'transform'));
});
