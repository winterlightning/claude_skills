'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
const path = require('node:path');
const source = () => JSON.parse(fs.readFileSync(path.join(__dirname, '../../core/icon_profiles.json'), 'utf8'));
async function managerUI(save, load) {
  class Element {
    constructor(tag) { this.tagName = tag.toUpperCase(); this.children = []; this.attrs = {}; this.style = {}; this.value = ''; this.handlers = {}; this.classList = { toggle() {} }; }
    appendChild(child) { this.children.push(child); return child; }
    replaceChildren(...children) { this.children = children; }
    setAttribute(key, value) { this.attrs[key] = String(value); }
    addEventListener(name, callback) { this.handlers[name] = callback; }
    scrollIntoView() {}
  }
  const nodes = new Map(), document = { createElement: tag => new Element(tag), createElementNS: (_, tag) => new Element(tag), getElementById(id) { if (!nodes.has(id)) nodes.set(id, new Element('div')); return nodes.get(id); } };
  const envelope = { configuration: source(), revision: 'before', resolvedProfiles: {} };
  const context = vm.createContext({ document, window: { location: { search: '?token=session-test' }, confirm: () => true, addEventListener() {} }, URLSearchParams, console, setTimeout,
    ProfileAPI: { create: () => ({ load: load || (async () => envelope), save: save || (async configuration => ({ ...envelope, configuration, revision: 'after' })) }) } });
  for (const name of ['profile-config.js', 'profile-manager.js']) vm.runInContext(fs.readFileSync(path.join(__dirname, name), 'utf8'), context, { filename: name });
  await new Promise(resolve => setImmediate(resolve));
  const run = code => vm.runInContext(code, context), read = code => JSON.parse(run(`JSON.stringify(${code})`));
  return { run, read, nodes };
}
test('manager loads saved config and previews resolved profile with no implicit save', async () => {
  let writes = 0; const ui = await managerUI(async () => { writes++; });
  assert.equal(ui.run('dirty()'), false); assert.equal(ui.nodes.get('profile-list').children.length, 3);
  assert.equal(ui.nodes.get('profile-native').attrs.width, '48');
  assert.equal(ui.nodes.get('save-profiles').disabled, true); assert.equal(writes, 0);
  assert.equal(ui.nodes.has('open-editor'), false);
});
test('add and delete affect the draft only and keep an accurate unsaved state', async () => {
  const ui = await managerUI(); ui.run("pm('new-profile-id').value = 'toolbar'"); ui.nodes.get('add-profile').handlers.click();
  assert.ok(ui.read('manager.configuration.profiles.toolbar'));
  assert.equal(ui.run('dirty()'), true); assert.equal(ui.nodes.get('save-profiles').disabled, false);
  ui.nodes.get('delete-profile').handlers.click(); assert.equal(ui.run('dirty()'), false);
});
test('invalid raw JSON stays editable and does not replace the validated draft', async () => {
  const ui = await managerUI(), before = ui.read('manager.configuration');
  ui.nodes.get('profile-json').value = '{"schemaVersion":2}'; ui.nodes.get('profile-json').handlers.input(); ui.nodes.get('apply-json').handlers.click();
  assert.deepEqual(ui.read('manager.configuration'), before); assert.equal(ui.run('manager.rawDirty'), true);
  assert.match(ui.nodes.get('json-error').textContent, /validationDefaults|profiles/); assert.equal(ui.nodes.get('save-profiles').disabled, true);
});
test('validation failures pause previews and prevent saves', async () => {
  let writes = 0; const ui = await managerUI(async () => { writes++; });
  ui.run('manager.configuration.profiles.normal.strokeWidth = 0; changed();');
  assert.equal(ui.nodes.get('save-profiles').disabled, true); assert.equal(ui.nodes.get('validation-errors').hidden, false);
  assert.match(ui.nodes.get('preview-state').textContent, /paused/);
  await ui.run('saveProfiles()'); assert.equal(writes, 0);
});
test('conflicting saves preserve the entire unsaved draft', async () => {
  const ui = await managerUI(async () => { const error = new Error('Configuration changed.'); error.status = 409; throw error; });
  ui.run("manager.configuration.profiles.normal.label = 'Unsaved'; changed();"); await ui.run('saveProfiles()');
  assert.equal(ui.read('manager.configuration.profiles.normal.label'), 'Unsaved'); assert.equal(ui.run('dirty()'), true);
  assert.match(ui.nodes.get('server-status').textContent, /draft is preserved/);
});
test('saving while new raw text is typed never overwrites the newer draft text', async () => {
  let finish; const ui = await managerUI(configuration => new Promise(resolve => { finish = () => resolve({ configuration, revision: 'after', resolvedProfiles: {} }); }));
  ui.run("manager.configuration.profiles.normal.label = 'Saving'; changed();"); const saving = ui.run('saveProfiles()');
  ui.nodes.get('profile-json').value = '{"newer":"unfinished'; ui.nodes.get('profile-json').handlers.input(); finish(); await saving;
  assert.equal(ui.nodes.get('profile-json').value, '{"newer":"unfinished'); assert.equal(ui.run('manager.rawDirty'), true);
  assert.equal(ui.run('manager.revision'), 'after');
});
test('reload preserves edits typed while its response is pending', async () => {
  let count = 0, finish;
  const envelope = { configuration: source(), revision: 'loaded', resolvedProfiles: {} };
  const ui = await managerUI(undefined, async () => { if (++count === 1) return envelope; return new Promise(resolve => { finish = () => resolve(envelope); }); });
  const reloading = ui.run('loadProfiles()');
  ui.run("manager.configuration.profiles.normal.label = 'Newer draft'; changed();");
  finish(); await reloading;
  assert.equal(ui.read('manager.configuration.profiles.normal.label'), 'Newer draft');
  assert.equal(ui.run('dirty()'), true);
  assert.match(ui.nodes.get('server-status').textContent, /newer draft edits/);
});
