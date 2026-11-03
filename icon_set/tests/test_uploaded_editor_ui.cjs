// Async geometry loading must not erase the saved Manual Upload edit base.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const root = path.resolve(__dirname, '../..');
const source = fs.readFileSync(path.join(root, 'icon_set/scripts/templates/gallery.html'), 'utf8');
const published = fs.readFileSync(path.join(root, 'published/gallery/index.html'), 'utf8');
const functionLine = text => text.split('\n').find(line => line.startsWith('async function openStrokeEditor('));
assert.equal(functionLine(source), functionLine(published));
const pending = [];
let current, upload;
const context = vm.createContext({
  fetch: () => new Promise(resolve => pending.push(resolve)),
  window: {StrokeEditor: {
    open: icon => { current = icon.key; upload = null; },
    setUpload: (key, sha) => { assert.equal(key, current); upload = sha; },
  }},
});
vm.runInContext('let strokeEditorRequest=0;\n' + functionLine(source), context);
const answer = sha => ({ok: true, json: async () => ({record: {primitives: [{}]}, choice: {uploaded: {svg_sha256: sha}}})});
(async () => {
  const load = context.openStrokeEditor({key: 'solo-64/one', uploaded_icon: true});
  context.window.StrokeEditor.setUpload('solo-64/one', 'manual-one'); // artwork choices arrived first
  pending.shift()(answer('manual-one'));
  await load;
  assert.equal(upload, 'manual-one', 'late geometry must restore the existing upload base');
  const stale = context.openStrokeEditor({key: 'solo-64/stale', uploaded_icon: true});
  const latest = context.openStrokeEditor({key: 'icon-72/latest', uploaded_icon: true});
  pending.pop()(answer('manual-latest'));
  await latest;
  pending.shift()(answer('manual-stale'));
  await stale;
  assert.equal(current, 'icon-72/latest');
  assert.equal(upload, 'manual-latest', 'a stale inspector response must not replace the current base');
  console.log('Uploaded geometry/base ordering and stale inspector response checks passed.');
})().catch(error => { console.error(error); process.exitCode = 1; });
