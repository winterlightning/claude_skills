'use strict';

const PC = ProfileConfig;
const pm = id => document.getElementById(id);
const sessionToken = new URLSearchParams(window.location.search).get('token') || '';
const profileAPI = ProfileAPI.create(sessionToken);
const manager = { configuration: null, saved: '', revision: '', selected: null, rawDirty: false, busy: false, errors: [], resolved: {} };
const palette = ['#267254', '#2563b0', '#b15f1a', '#9461ad', '#d14854', '#248692'];
const stamp = configuration => JSON.stringify(configuration);
const dirty = () => manager.rawDirty || (manager.configuration && stamp(manager.configuration) !== manager.saved);
function notice(message, error = false) { pm('server-status').textContent = message; pm('server-status').classList.toggle('error', error); }
function run(action) { try { action(); } catch (error) { notice(error.message, true); } }
function element(tag, text, className) { const node = document.createElement(tag); if (text !== undefined) node.textContent = text; if (className) node.className = className; return node; }
function button(text, action, className) { const node = element('button', text, className); node.addEventListener('click', () => run(action)); return node; }
function selectedRaw() { return manager.configuration?.profiles[manager.selected]; }
function selectedResolved() { return manager.resolved[manager.selected]; }
function updateStatus() {
  pm('save-state').textContent = manager.busy ? 'Working with local configuration…' : manager.rawDirty ? 'Unsaved JSON text — apply it to the draft first' : dirty() ? 'Unsaved configuration changes' : manager.configuration ? 'Saved configuration · no unsaved changes' : 'No configuration loaded';
  pm('save-state').classList.toggle('unsaved', !!dirty());
  pm('save-profiles').disabled = manager.busy || !manager.configuration || manager.rawDirty || manager.errors.length > 0 || !dirty();
  pm('reload-profiles').disabled = manager.busy;
  for (const id of ['add-profile', 'duplicate-profile', 'delete-profile', 'show-json', 'import-profiles', 'export-profiles']) pm(id).disabled = manager.busy || !manager.configuration;
}
function evaluateDraft() {
  const checked = PC.inspect(manager.configuration); manager.errors = checked.errors; manager.resolved = checked.resolvedProfiles;
  const box = pm('validation-errors'); box.replaceChildren(); box.hidden = !manager.errors.length;
  if (manager.errors.length) {
    box.appendChild(element('strong', 'Resolve these configuration errors before saving:'));
    const list = element('ul'); for (const error of manager.errors) list.appendChild(element('li', error)); box.appendChild(list);
  }
  updateStatus(); renderPreview(); renderList();
}
function changed() {
  evaluateDraft();
  if (!manager.rawDirty) pm('profile-json').value = JSON.stringify(manager.configuration, null, 2);
}
function field(container, title, value, apply, options = {}) {
  const label = element('label', title), input = document.createElement(options.choices ? 'select' : 'input');
  if (options.choices) {
    for (const [key, text] of options.choices) { const option = element('option', text); option.value = key; input.appendChild(option); }
  } else { input.type = options.number ? 'number' : 'text'; if (options.number) input.step = 'any'; input.spellcheck = false; }
  input.value = value ?? ''; if (options.placeholder !== undefined) input.placeholder = String(options.placeholder);
  input.disabled = !!options.disabled;
  input.addEventListener(options.choices ? 'change' : 'input', () => run(() => {
    const value = options.number ? (input.value.trim() === '' ? undefined : Number(input.value)) : input.value;
    apply(value); changed(); if (options.rebuild) renderForms();
  }));
  label.appendChild(input); container.appendChild(label); return input;
}
function assignOptional(object, key, value) { if (value === undefined || value === '') delete object[key]; else object[key] = value; }
function section(title, hint) { const card = element('section', undefined, 'config-card'); card.appendChild(element('h2', title)); if (hint) card.appendChild(element('p', hint, 'hint')); pm('profile-form').appendChild(card); return card; }
function grid(card) { const node = element('div', undefined, 'field-grid'); card.appendChild(node); return node; }
function defaultChoices() { return Object.entries(manager.configuration.profiles).map(([name, profile]) => [name, `${profile.label || name} (${name})`]); }

function renderList() {
  if (!manager.configuration) return;
  pm('profile-list').replaceChildren();
  for (const [name, raw] of Object.entries(manager.configuration.profiles)) {
    const profile = manager.resolved[name];
    const row = button('', () => { manager.selected = name; renderForms(); renderList(); renderPreview(); }, 'profile-row');
    row.classList.toggle('selected', name === manager.selected); row.setAttribute('aria-pressed', String(name === manager.selected));
    row.appendChild(element('strong', raw.label || name));
    row.appendChild(element('small', `${name}${manager.configuration.defaultIconType === name ? ' · default' : ''} · ${profile?.canvas ?? '?'}px / ${profile?.strokeWidth ?? '?'}u`));
    pm('profile-list').appendChild(row);
  }
  const select = pm('default-profile'); select.replaceChildren();
  for (const [name, label] of defaultChoices()) { const option = element('option', label); option.value = name; select.appendChild(option); }
  select.value = manager.configuration.defaultIconType;
}
function renderForms() {
  pm('profile-form').replaceChildren(); pm('validation-defaults').replaceChildren();
  if (!manager.configuration) return;
  const raw = selectedRaw(), resolved = selectedResolved(); if (!raw) return;
  const basics = grid(section(`Profile: ${manager.selected}`, 'Blank numeric values inherit from the parent. Label remains local to this profile.'));
  field(basics, 'Display label', raw.label, value => { raw.label = value; });
  field(basics, 'Inherit from', raw.extends || '', value => assignOptional(raw, 'extends', value), { choices: [['', 'No parent'], ...defaultChoices().filter(([name]) => name !== manager.selected)], rebuild: true });
  field(basics, 'Native canvas (px)', raw.canvas, value => assignOptional(raw, 'canvas', value), { number: true, placeholder: resolved?.canvas ?? 'Required' });
  field(basics, 'Stroke width (u = px)', raw.strokeWidth, value => assignOptional(raw, 'strokeWidth', value), { number: true, placeholder: resolved?.strokeWidth ?? 'Required' });
  const overrides = grid(section('Validation overrides', 'Blank values use the inherited/default value. Minimum solid fill depth can be 0 to disable the pinch check.'));
  for (const [key, label] of Object.entries(PC.VALIDATION_LABELS)) {
    field(overrides, label, raw.validation?.[key], value => { raw.validation ||= {}; assignOptional(raw.validation, key, value); if (!Object.keys(raw.validation).length) delete raw.validation; }, { number: true, placeholder: resolved?.validation?.[key] });
    field(pm('validation-defaults'), label, manager.configuration.validationDefaults[key], value => { manager.configuration.validationDefaults[key] = value === undefined ? null : value; }, { number: true });
  }
  renderKeyshapeForm(raw, resolved); renderSlotForm(raw, resolved);
}
function renderKeyshapeForm(raw, resolved) {
  const card = section('Centered keyshapes', 'Keyshapes describe painted boundaries. Names are independent of dimensions, so changing size does not silently rename icon references.');
  if (!Object.hasOwn(raw, 'keyshapes')) {
    card.appendChild(element('p', 'This profile inherits its keyshape list.', 'hint'));
    card.appendChild(button('Customize inherited keyshapes', () => { raw.keyshapes = PC.clone(resolved?.keyshapes || []); changed(); renderForms(); })); return;
  }
  const list = element('div', undefined, 'token-list'); card.appendChild(list);
  for (const [index, token] of raw.keyshapes.entries()) {
    const row = element('div', undefined, 'token-row'), fields = element('div', undefined, 'token-fields'); row.appendChild(fields);
    field(fields, 'Name', token.name, value => { token.name = value; });
    field(fields, 'Shape', token.shape, value => {
      token.shape = value;
      if (value === 'circle') { token.height = token.width; token.diameter = token.width; token.orientation = 'circle'; }
      else { delete token.diameter; token.orientation = token.width === token.height ? 'square' : token.width > token.height ? 'landscape' : 'portrait'; }
    }, { choices: [['rect', 'Rectangle'], ['circle', 'Circle']], rebuild: true });
    function dimension(name, value) {
      token[name] = value === undefined ? null : value;
      if (token.shape === 'circle') token.width = token.height = token.diameter = token[name];
      else token.orientation = token.width === token.height ? 'square' : token.width > token.height ? 'landscape' : 'portrait';
    }
    field(fields, token.shape === 'circle' ? 'Diameter' : 'Width', token.width, value => dimension('width', value), { number: true });
    if (token.shape === 'rect') field(fields, 'Height', token.height, value => dimension('height', value), { number: true });
    const controls = element('div', undefined, 'button-row');
    controls.appendChild(button('Remove', () => { raw.keyshapes.splice(index, 1); changed(); renderForms(); })); row.appendChild(controls); list.appendChild(row);
  }
  const controls = element('div', undefined, 'button-row');
  controls.appendChild(button('Add keyshape', () => {
    const size = Math.max(resolved?.strokeWidth || 4, (resolved?.canvas || 48) - (resolved?.strokeWidth || 4) * 2); let index = 1;
    while (raw.keyshapes.some(token => token.name === `keyshape-${index}`)) index++;
    raw.keyshapes.push({ name: `keyshape-${index}`, shape: 'rect', orientation: 'square', width: size, height: size }); changed(); renderForms();
  }));
  if (raw.extends) controls.appendChild(button('Use inherited keyshapes', () => { delete raw.keyshapes; changed(); renderForms(); }));
  card.appendChild(controls);
}
function renderSlotForm(raw, resolved) {
  const card = section('Container slot', 'Any profile can host an accepted profile. Slots must be centered and exactly match the accepted canvas.');
  const mode = !Object.hasOwn(raw, 'containerSlot') ? 'inherit' : raw.containerSlot === null ? 'none' : 'custom';
  field(card, 'Slot mode', mode, value => {
    if (value === 'inherit') delete raw.containerSlot;
    else if (value === 'none') raw.containerSlot = null;
    else {
      const accepted = Object.entries(manager.resolved).find(([name, profile]) => name !== manager.selected && profile.canvas <= (resolved?.canvas || 48));
      const name = accepted?.[0] || manager.selected, size = accepted?.[1].canvas || resolved?.canvas || 48, offset = ((resolved?.canvas || 48) - size) / 2;
      raw.containerSlot = { x: offset, y: offset, w: size, h: size, acceptedProfile: name, minimumClearSquare: size };
    }
  }, { choices: [['inherit', 'Inherit (or no slot)'], ['none', 'No slot — override parent'], ['custom', 'Custom slot']], rebuild: true });
  if (mode !== 'custom') { card.appendChild(element('p', resolved?.containerSlot ? `Effective slot accepts ${resolved.containerSlot.acceptedProfile}.` : 'No effective slot.', 'hint')); return; }
  const fields = grid(card), slot = raw.containerSlot;
  field(fields, 'Accepted profile', slot.acceptedProfile, value => {
    slot.acceptedProfile = value; const size = manager.resolved[value]?.canvas;
    if (size) { slot.w = slot.h = slot.minimumClearSquare = size; slot.x = slot.y = ((resolved?.canvas || 48) - size) / 2; }
  }, { choices: defaultChoices(), rebuild: true });
  for (const [key, label] of [['x', 'X'], ['y', 'Y'], ['w', 'Width'], ['h', 'Height'], ['minimumClearSquare', 'Minimum clear square']]) field(fields, label, slot[key], value => { slot[key] = value === undefined ? null : value; }, { number: true });
  card.appendChild(button('Center and match accepted canvas', () => {
    const size = manager.resolved[slot.acceptedProfile]?.canvas; if (!size) throw new Error('Choose a valid accepted profile first.');
    slot.w = slot.h = slot.minimumClearSquare = size; slot.x = slot.y = ((selectedResolved()?.canvas || 48) - size) / 2; changed(); renderForms();
  }));
}

function svgNode(tag, attrs) { const node = document.createElementNS('http://www.w3.org/2000/svg', tag); for (const [name, value] of Object.entries(attrs)) node.setAttribute(name, value); return node; }
function renderPreview() {
  const profile = selectedResolved();
  pm('preview-title').textContent = profile?.label || 'Resolved profile preview';
  if (manager.errors.length || !profile) { pm('preview-state').textContent = 'Preview paused while configuration is invalid. Last valid preview is shown.'; return; }
  pm('preview-state').textContent = 'Centered keyshapes are guides, not icon geometry.';
  pm('preview-summary').textContent = `${profile.canvas} × ${profile.canvas}px native · ${profile.strokeWidth}u stroke · ${profile.validation.gridStep}u grid`;
  const canvas = pm('profile-canvas'); canvas.replaceChildren(); canvas.setAttribute('viewBox', `0 0 ${profile.canvas} ${profile.canvas}`);
  for (const value of PC.gridCoordinates(profile.canvas, profile.validation.gridStep)) {
    const major = Math.abs(value / profile.validation.majorGridStep - Math.round(value / profile.validation.majorGridStep)) < 1e-8;
    for (const attrs of [{ x1: value, y1: 0, x2: value, y2: profile.canvas }, { x1: 0, y1: value, x2: profile.canvas, y2: value }]) canvas.appendChild(svgNode('line', { ...attrs, stroke: major ? '#d1dbcf' : '#edf0eb', 'stroke-width': profile.canvas / 600 }));
  }
  pm('keyshape-legend').replaceChildren();
  profile.keyshapes.forEach((token, index) => {
    const color = palette[index % palette.length], attrs = token.shape === 'circle' ? { cx: profile.canvas / 2, cy: profile.canvas / 2, r: token.diameter / 2 } : { x: (profile.canvas - token.width) / 2, y: (profile.canvas - token.height) / 2, width: token.width, height: token.height };
    canvas.appendChild(svgNode(token.shape, { ...attrs, fill: 'none', stroke: color, 'stroke-width': profile.canvas / 180 }));
    const row = element('div', undefined, 'legend-row'), swatch = element('span', undefined, 'legend-swatch'); swatch.style.borderColor = color; row.appendChild(swatch); row.appendChild(element('span', `${token.name} · ${token.width} × ${token.height}`)); pm('keyshape-legend').appendChild(row);
  });
  if (profile.containerSlot) { const slot = profile.containerSlot; canvas.appendChild(svgNode('rect', { x: slot.x, y: slot.y, width: slot.w, height: slot.h, fill: '#9461ad0d', stroke: '#9461ad', 'stroke-width': profile.canvas / 180, 'stroke-dasharray': `${profile.canvas / 30} ${profile.canvas / 60}` })); }
  const sample = pm('profile-native'); sample.replaceChildren();
  for (const key of ['width', 'height']) sample.setAttribute(key, profile.canvas);
  sample.setAttribute('viewBox', `0 0 ${profile.canvas} ${profile.canvas}`);
  sample.appendChild(svgNode('path', { d: `M ${profile.canvas * .25} ${profile.canvas * .65} L ${profile.canvas * .45} ${profile.canvas * .35} L ${profile.canvas * .75} ${profile.canvas * .65}`, fill: 'none', stroke: 'currentColor', 'stroke-width': profile.strokeWidth, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }));
  pm('resolved-json').textContent = JSON.stringify(profile, null, 2);
}

function adopt(envelope) {
  const checked = PC.inspect(envelope.configuration); if (checked.errors.length) throw new Error(`Server configuration cannot be previewed: ${checked.errors.join('; ')}`);
  manager.configuration = PC.clone(envelope.configuration); manager.saved = stamp(manager.configuration); manager.revision = envelope.revision; manager.rawDirty = false;
  if (!Object.hasOwn(manager.configuration.profiles, manager.selected)) manager.selected = manager.configuration.defaultIconType;
  changed(); renderForms();
}
async function loadProfiles() {
  if (dirty() && !window.confirm('Discard unsaved configuration changes and reload the saved version?')) return;
  const before = stamp(manager.configuration), beforeRaw = pm('profile-json').value, beforeRawDirty = manager.rawDirty;
  manager.busy = true; updateStatus();
  try {
    const envelope = await profileAPI.load();
    if (stamp(manager.configuration) !== before || pm('profile-json').value !== beforeRaw || manager.rawDirty !== beforeRawDirty) throw new Error('Reload did not replace newer draft edits. Your changes are preserved; reload again when ready.');
    adopt(envelope); notice('Loaded canonical configuration.');
  }
  catch (error) { notice(`${error.message}${!sessionToken ? ' Open the manager using the local server URL with its session token.' : ''}`, true); }
  finally { manager.busy = false; updateStatus(); }
}
async function saveProfiles() {
  if (!manager.configuration || manager.rawDirty || manager.errors.length || manager.busy) return;
  const outgoing = PC.clone(manager.configuration), before = stamp(outgoing); manager.busy = true; updateStatus();
  try {
    const envelope = await profileAPI.save(outgoing, manager.revision);
    if (stamp(manager.configuration) === before && !manager.rawDirty) adopt(envelope);
    else { manager.saved = stamp(envelope.configuration); manager.revision = envelope.revision; changed(); }
    notice('Saved canonical profiles and regenerated mirrors. Existing icon geometry was not changed.');
  } catch (error) { notice(error.status === 409 ? `${error.message} Your draft is preserved. Export it before reloading the latest configuration.` : error.message, true); }
  finally { manager.busy = false; updateStatus(); }
}
function requestedName() { const name = pm('new-profile-id').value.trim(); if (!PC.safeName(name) || Object.hasOwn(manager.configuration.profiles, name)) throw new Error('Enter an unused kebab-case profile id.'); return name; }
function adoptDraft(configuration) {
  const checked = PC.inspect(configuration); if (checked.errors.length) throw new Error(checked.errors.join('\n'));
  manager.configuration = PC.clone(configuration); manager.rawDirty = false;
  if (!Object.hasOwn(configuration.profiles, manager.selected)) manager.selected = configuration.defaultIconType;
  changed(); renderForms();
}
pm('add-profile').addEventListener('click', () => run(() => {
  const name = requestedName(), base = selectedResolved();
  manager.configuration.profiles[name] = { label: name.replaceAll('-', ' '), canvas: base?.canvas || 48, strokeWidth: base?.strokeWidth || 4, keyshapes: PC.clone(base?.keyshapes || [{ name: 'square-40', shape: 'rect', orientation: 'square', width: 40, height: 40 }]) };
  manager.selected = name; pm('new-profile-id').value = ''; changed(); renderForms();
}));
pm('duplicate-profile').addEventListener('click', () => run(() => { const name = requestedName(); manager.configuration = PC.duplicate(manager.configuration, manager.selected, name); manager.selected = name; pm('new-profile-id').value = ''; changed(); renderForms(); }));
pm('delete-profile').addEventListener('click', () => run(() => { const next = PC.remove(manager.configuration, manager.selected); if (!window.confirm(`Delete profile ${manager.selected} from this draft? This takes effect only when you save.`)) return; manager.configuration = next; manager.selected = next.defaultIconType; changed(); renderForms(); }));
pm('default-profile').addEventListener('change', () => { manager.configuration.defaultIconType = pm('default-profile').value; changed(); });
pm('save-profiles').addEventListener('click', saveProfiles); pm('reload-profiles').addEventListener('click', loadProfiles);
pm('show-json').addEventListener('click', () => { pm('raw-panel').hidden = !pm('raw-panel').hidden; if (!pm('raw-panel').hidden) pm('raw-panel').scrollIntoView({ behavior: 'smooth', block: 'start' }); });
pm('profile-json').addEventListener('input', () => { manager.rawDirty = true; updateStatus(); });
pm('apply-json').addEventListener('click', () => { try { adoptDraft(JSON.parse(pm('profile-json').value)); pm('json-error').textContent = ''; notice('JSON applied to the unsaved draft.'); } catch (error) { pm('json-error').textContent = error.message; } });
pm('reset-json').addEventListener('click', () => { pm('profile-json').value = JSON.stringify(manager.configuration, null, 2); manager.rawDirty = false; pm('json-error').textContent = ''; updateStatus(); });
pm('import-profiles').addEventListener('click', () => pm('profile-file').click());
pm('profile-file').addEventListener('change', async event => {
  const file = event.target.files[0]; if (!file) return;
  try { if (file.size > 1000000) throw new Error('Choose a profile configuration smaller than 1 MB.'); const imported = JSON.parse(await file.text()); if (dirty() && !window.confirm('Replace unsaved changes with the imported draft?')) return; adoptDraft(imported); notice('Imported configuration draft. Save to apply it to the system.'); }
  catch (error) { notice(error.message, true); } finally { event.target.value = ''; }
});
pm('export-profiles').addEventListener('click', () => {
  const body = manager.rawDirty ? pm('profile-json').value : JSON.stringify(manager.configuration, null, 2), url = URL.createObjectURL(new Blob([`${body}\n`], { type: 'application/json' }));
  const anchor = document.createElement('a'); anchor.href = url; anchor.download = 'icon-profiles.json'; anchor.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
});
window.addEventListener('beforeunload', event => { if (dirty()) { event.preventDefault(); event.returnValue = ''; } });
updateStatus();
loadProfiles();
