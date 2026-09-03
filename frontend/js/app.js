'use strict';

/* Reference-led editor. State is canonical schemaVersion:2 geometry, not a
 * placement catalog. SVG previews use only validated DOM elements. */
const G = IconGeometry;
const $ = id => document.getElementById(id);
const clone = G.clone;
const SVGNS = G.NS;
const SETTINGS_KEY = 'reference-led-icons.settings.v1';
const settings = { iconName: 'icon', iconType: ICON_PROFILES.defaultIconType, keyshape: 'square-40', containerAcceptedKeyshape: 'square-32', showSkeleton: false };
try { Object.assign(settings, JSON.parse(localStorage.getItem(SETTINGS_KEY)) || {}); } catch (_) { /* unavailable storage */ }
if (!Object.hasOwn(ICON_PROFILES.profiles, settings.iconType)) settings.iconType = ICON_PROFILES.defaultIconType;
if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(settings.iconName)) settings.iconName = 'icon';
function saveSettings() { try { localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings)); } catch (_) { /* optional storage */ } }
function profileFor(iconType) {
  const raw = ICON_PROFILES.profiles[iconType];
  if (!raw) throw new Error(`Unknown icon profile: ${iconType}.`);
  return { ...(raw.extends ? profileFor(raw.extends) : {}), ...raw, iconType };
}
const currentProfile = () => profileFor(settings.iconType);
const canvasSize = () => currentProfile().designCanvas;
const keyshapeNamed = (profile, name) => profile.keyshapes.find(token => token.name === name);
const svg = $('canvas');
const state = { elements: [], selectedId: null, metadata: {} };
const selected = () => state.elements.find(element => element.id === state.selectedId) || null;
const history = [];
let clipboard = null, drag = null, renderedSelection = null;
const blankAnalysis = () => ({ incomplete: true, references: [], mappings: [], relationships: [], spacingChecks: [] });

function status(message, isError = false) { $('editor-status').textContent = message; $('editor-status').classList.toggle('error', isError); }
function attempt(action) { try { return action(); } catch (error) { status(error.message, true); return undefined; } }
function snapshot() { return clone({ elements: state.elements, selectedId: state.selectedId, metadata: state.metadata, settings }); }
function pushHistory(tag) {
  const now = Date.now(), previous = history[history.length - 1];
  if (tag && previous?.tag === tag && now - previous.time < 800) { previous.time = now; return; }
  history.push({ tag, time: now, state: snapshot() });
  if (history.length > 100) history.shift();
}
function undo() {
  const previous = history.pop();
  if (!previous) return;
  Object.assign(state, { elements: previous.state.elements, selectedId: previous.state.selectedId, metadata: previous.state.metadata });
  Object.assign(settings, previous.state.settings);
  renderedSelection = null; syncProfileControls(); status('Undid the last edit.');
}
function newId(tag) {
  let index = 1;
  while (state.elements.some(element => element.id === `${tag}-${index}`)) index++;
  return `${tag}-${index}`;
}
function updateSelected(element) { state.elements[state.elements.findIndex(item => item.id === state.selectedId)] = element; state.selectedId = element.id; }
function geometryChanged(message) {
  // Keep references/observations, but invalidate QA when the geometry changes.
  state.metadata.sourceAnalysis = { ...blankAnalysis(), ...(state.metadata.sourceAnalysis || {}), incomplete: true };
  renderedSelection = null; render(); if (message) status(message);
}

function styledNode(element, skeleton = false) {
  const node = G.node(element);
  node.setAttribute('fill', 'none'); node.setAttribute('stroke', skeleton ? '#ef4444' : 'currentColor');
  node.setAttribute('stroke-width', skeleton ? '0.05' : currentProfile().designStroke);
  node.setAttribute('stroke-linecap', 'round'); node.setAttribute('stroke-linejoin', 'round');
  return node;
}
function renderElements() {
  $('shapes').replaceChildren(); $('skeletons').replaceChildren(); $('ship-preview').replaceChildren();
  for (const element of state.elements) {
    const node = styledNode(element); node.dataset.elementId = element.id; node.style.cursor = 'move'; $('shapes').appendChild(node);
    $('ship-preview').appendChild(styledNode(element));
    if (settings.showSkeleton) { const skeleton = styledNode(element, true); skeleton.setAttribute('pointer-events', 'none'); $('skeletons').appendChild(skeleton); }
  }
  const profile = currentProfile();
  $('ship-preview').setAttribute('viewBox', `0 0 ${profile.designCanvas} ${profile.designCanvas}`);
  $('ship-preview').setAttribute('width', profile.shipCanvas); $('ship-preview').setAttribute('height', profile.shipCanvas);
  $('ship-size').textContent = `${profile.shipCanvas} × ${profile.shipCanvas}px`;
}
function renderOverlay() {
  $('overlay').replaceChildren();
  const element = selected();
  if (!element) return;
  const node = [...$('shapes').children].find(child => child.dataset.elementId === element.id);
  if (!node) return;
  const bounds = node.getBBox(), box = document.createElementNS(SVGNS, 'rect');
  box.setAttribute('x', bounds.x - 0.5); box.setAttribute('y', bounds.y - 0.5);
  box.setAttribute('width', Math.max(1, bounds.width + 1)); box.setAttribute('height', Math.max(1, bounds.height + 1));
  box.setAttribute('fill', 'none'); box.setAttribute('stroke', '#3b82f6'); box.setAttribute('stroke-width', '0.12');
  box.setAttribute('stroke-dasharray', '0.5 0.5'); box.setAttribute('pointer-events', 'none'); $('overlay').appendChild(box);
}
function renderElementList() {
  $('element-list').replaceChildren(); $('element-count').textContent = state.elements.length;
  for (const element of state.elements) {
    const button = document.createElement('button'); button.className = 'element-row';
    button.classList.toggle('selected', element.id === state.selectedId); button.textContent = `${element.id} · ${element.role || element.tag}`;
    button.title = 'Select element; list order is SVG paint order'; button.setAttribute('aria-pressed', String(element.id === state.selectedId));
    button.addEventListener('click', () => { state.selectedId = element.id; renderedSelection = null; render(); svg.focus(); }); $('element-list').appendChild(button);
  }
}
function renderProps() {
  const element = selected(); $('props-empty').hidden = !!element; $('props-body').hidden = !element;
  if (!element) { renderedSelection = null; return; }
  $('props-title').textContent = `<${element.tag}> · exact design-space geometry`;
  const fingerprint = JSON.stringify(element);
  if (fingerprint !== renderedSelection) {
    $('p-id').value = element.id; $('p-role').value = element.role || ''; $('p-attrs').value = JSON.stringify(element.attrs, null, 2); renderedSelection = fingerprint;
  }
}
function renderToolbar() {
  for (const id of ['copy', 'forward', 'backward', 'duplicate', 'delete']) $(`btn-${id}`).disabled = !selected();
  $('btn-undo').disabled = history.length === 0; $('btn-paste').disabled = !clipboard;
  for (const id of ['clear', 'preview', 'export']) $(`btn-${id}`).disabled = state.elements.length === 0;
}
function render() { renderElements(); renderOverlay(); renderElementList(); renderProps(); renderToolbar(); }
function renderGrid() {
  $('grid').replaceChildren(); const size = canvasSize(); svg.setAttribute('viewBox', `0 0 ${size} ${size}`);
  for (let value = 0; value <= size; value++) {
    const center = value === size / 2, major = value % 4 === 0;
    for (const attrs of [{ x1: value, y1: 0, x2: value, y2: size }, { x1: 0, y1: value, x2: size, y2: value }]) {
      const line = document.createElementNS(SVGNS, 'line');
      for (const [key, coordinate] of Object.entries(attrs)) line.setAttribute(key, coordinate);
      line.setAttribute('stroke', center ? '#aeb8c7' : major ? '#d1d7df' : '#edf0f4'); line.setAttribute('stroke-width', center ? '0.12' : major ? '0.08' : '0.035'); $('grid').appendChild(line);
    }
  }
}
function appendKeyshapeGuide(profile, token, dx = 0, dy = 0, protectedRegion = false) {
  const attrs = token.shape === 'circle' ? { cx: profile.center.x + dx, cy: profile.center.y + dy, r: token.diameter / 2 }
    : { x: profile.center.x - token.width / 2 + dx, y: profile.center.y - token.height / 2 + dy, width: token.width, height: token.height };
  const guide = G.node({ id: 'keyshape-guide', tag: token.shape === 'circle' ? 'circle' : 'rect', attrs });
  guide.setAttribute('fill', 'none'); guide.setAttribute('stroke', protectedRegion ? '#dc2626' : '#16a34a'); guide.setAttribute('stroke-width', '0.18');
  guide.setAttribute('stroke-dasharray', protectedRegion ? '0.35 0.55' : '0.8 0.8'); guide.setAttribute('pointer-events', 'none'); $('keyshape-guide').appendChild(guide);
}
function renderKeyshape() {
  $('keyshape-guide').replaceChildren(); const profile = currentProfile();
  appendKeyshapeGuide(profile, keyshapeNamed(profile, settings.keyshape) || profile.keyshapes[0]);
  if (settings.iconType === 'container') {
    const slot = profile.containerSlot, guide = G.node({ id: 'slot-guide', tag: 'rect', attrs: { x: slot.x, y: slot.y, width: slot.w, height: slot.h } });
    guide.setAttribute('fill', 'none'); guide.setAttribute('stroke', '#7c3aed'); guide.setAttribute('stroke-width', '0.14'); guide.setAttribute('stroke-dasharray', '1 1');
    guide.setAttribute('pointer-events', 'none'); guide.dataset.containerSlotGuide = 'true'; $('keyshape-guide').appendChild(guide);
    const acceptedProfile = profileFor(slot.acceptedProfile);
    appendKeyshapeGuide(acceptedProfile, keyshapeNamed(acceptedProfile, settings.containerAcceptedKeyshape) || acceptedProfile.keyshapes[0], slot.x, slot.y, true);
  }
}

function applyGeometry() {
  const element = selected(); if (!element) return;
  const id = $('p-id').value.trim(), role = $('p-role').value.trim();
  if (state.elements.some(item => item !== element && item.id === id)) throw new Error(`Duplicate element id: ${id}.`);
  const updated = G.validateElement({ id, ...(role ? { role } : {}), tag: element.tag, attrs: JSON.parse($('p-attrs').value) });
  pushHistory(); updateSelected(updated); geometryChanged('Geometry updated. Recheck connections, spacing, and analysis before shipping.');
}
function moveSelected(dx, dy, tag) {
  if (!selected()) return;
  const updated = G.translate(selected(), dx, dy); pushHistory(tag); updateSelected(updated); geometryChanged();
}
function copySelected() { if (selected()) { clipboard = clone(selected()); renderToolbar(); status('Element copied.'); } }
function pasteClipboard() {
  if (!clipboard) return;
  const copied = G.translate(clipboard, 1, 1); copied.id = newId(copied.tag);
  pushHistory(); clipboard = clone(copied); state.elements.push(copied); state.selectedId = copied.id; geometryChanged('Pasted element.');
}
function duplicateSelected() { if (selected()) { clipboard = clone(selected()); pasteClipboard(); } }
function deleteSelected() {
  if (!selected()) return;
  pushHistory(); state.elements = state.elements.filter(element => element.id !== state.selectedId); state.selectedId = null; geometryChanged('Deleted element. Undo is available.');
}
function moveInStack(direction) {
  const index = state.elements.indexOf(selected()), next = index + direction;
  if (index < 0 || next < 0 || next >= state.elements.length) return;
  pushHistory(); [state.elements[index], state.elements[next]] = [state.elements[next], state.elements[index]]; geometryChanged();
}
function validatedIconName() {
  const name = $('icon-name').value.trim();
  if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(name)) throw new Error('Use a kebab-case icon name such as coffee-mug.');
  return name;
}
function editableDocument() {
  const profile = currentProfile();
  const result = {
    ...clone(state.metadata), schemaVersion: 2, name: validatedIconName(), iconType: settings.iconType, canvas: profile.designCanvas, strokeWidth: profile.designStroke,
    keyfitCheck: { ...(state.metadata.keyfitCheck || {}), targetToken: settings.keyshape },
    sourceAnalysis: clone(state.metadata.sourceAnalysis || blankAnalysis()), elements: G.validateElements(state.elements),
  };
  if (settings.iconType === 'container') { const slot = profile.containerSlot; result.containerSlot = { x: slot.x, y: slot.y, w: slot.w, h: slot.h, acceptedKeyshape: settings.containerAcceptedKeyshape }; }
  else delete result.containerSlot;
  return result;
}
function validateDocument(raw) {
  if (!raw || typeof raw !== 'object' || Array.isArray(raw)) throw new Error('The document must be a JSON object.');
  if (raw.schemaVersion !== 2 || Object.hasOwn(raw, 'instances')) throw new Error('This editor uses schemaVersion: 2 and elements. Legacy instances are supported by the backend, but must be migrated before editing here.');
  if (typeof raw.name !== 'string' || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(raw.name)) throw new Error('The document name must be kebab-case.');
  if (typeof raw.iconType !== 'string' || !Object.hasOwn(ICON_PROFILES.profiles, raw.iconType)) throw new Error('Choose a supported iconType: normal, sub, or container.');
  const profile = profileFor(raw.iconType);
  if (raw.canvas !== profile.designCanvas || raw.strokeWidth !== profile.designStroke) throw new Error(`${raw.iconType} requires canvas ${profile.designCanvas} and strokeWidth ${profile.designStroke}.`);
  if (!raw.keyfitCheck || !keyshapeNamed(profile, raw.keyfitCheck.targetToken)) throw new Error('keyfitCheck.targetToken must name a keyshape in this profile.');
  if (raw.sourceAnalysis !== undefined && (!raw.sourceAnalysis || typeof raw.sourceAnalysis !== 'object' || Array.isArray(raw.sourceAnalysis))) throw new Error('sourceAnalysis must be an object.');
  if (raw.iconType === 'container') {
    const slot = profile.containerSlot;
    if (!raw.containerSlot || ['x', 'y', 'w', 'h'].some(key => raw.containerSlot[key] !== slot[key])) throw new Error('containerSlot must match the protected slot in the selected profile.');
    if (!keyshapeNamed(profileFor(slot.acceptedProfile), raw.containerSlot.acceptedKeyshape)) throw new Error('containerSlot.acceptedKeyshape must name a sub keyshape.');
  } else if (Object.hasOwn(raw, 'containerSlot')) throw new Error('containerSlot is only supported for container icons.');
  return { ...clone(raw), elements: G.validateElements(raw.elements) };
}
function importDocument(raw) {
  const document = validateDocument(raw); // Validate everything before mutation.
  pushHistory(); const { elements, ...metadata } = document;
  state.metadata = metadata; state.elements = elements; state.selectedId = null;
  settings.iconName = document.name; settings.iconType = document.iconType; settings.keyshape = document.keyfitCheck.targetToken;
  if (document.containerSlot) settings.containerAcceptedKeyshape = document.containerSlot.acceptedKeyshape;
  clipboard = null; renderedSelection = null; syncProfileControls(); status(`Imported ${document.name}: ${elements.length} editable elements. Run pipeline QA before shipping.`);
}
function download(filename, body, type) {
  const url = URL.createObjectURL(new Blob([body], { type })), anchor = document.createElement('a'); anchor.href = url; anchor.download = filename; anchor.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
}
function exportJSON() {
  const document = editableDocument(); download(`${document.name}.json`, `${JSON.stringify(document, null, 2)}\n`, 'application/json');
  status(document.sourceAnalysis?.incomplete ? 'Exported JSON. Complete source analysis and run QA before shipping.' : 'Exported editable JSON. Run pipeline QA before shipping.');
}
function documentElementSVG(document) {
  const root = window.document.createElementNS(SVGNS, 'svg'); root.setAttribute('viewBox', `0 0 ${document.canvas} ${document.canvas}`);
  root.setAttribute('fill', 'none'); root.setAttribute('stroke', 'currentColor'); root.setAttribute('stroke-width', document.strokeWidth); root.setAttribute('stroke-linecap', 'round'); root.setAttribute('stroke-linejoin', 'round');
  root.setAttribute('data-icon-type', document.iconType); root.setAttribute('data-keyshape', document.keyfitCheck.targetToken);
  for (const element of document.elements) root.appendChild(G.node(element));
  return root;
}
function exportPreviewSVG() {
  const document = editableDocument(); download(`${document.name}-preview.svg`, `${new XMLSerializer().serializeToString(documentElementSVG(document))}\n`, 'image/svg+xml'); status('Exported design-size preview. This is not a QA-approved ship artifact.');
}
function toCanvas(event) {
  const transform = svg.getScreenCTM(); if (!transform) throw new Error('Canvas is not visible.');
  return new DOMPoint(event.clientX, event.clientY).matrixTransform(transform.inverse());
}
svg.addEventListener('pointerdown', event => attempt(() => {
  if (event.button !== 0) return;
  const node = event.target.closest('[data-element-id]');
  if (!node || node.parentNode !== $('shapes')) { state.selectedId = null; render(); return; }
  state.selectedId = node.dataset.elementId; const point = toCanvas(event); drag = { original: clone(selected()), x: point.x, y: point.y, pushed: false };
  render(); svg.focus(); svg.setPointerCapture(event.pointerId); event.preventDefault();
}));
svg.addEventListener('pointermove', event => attempt(() => {
  if (!drag) return;
  const point = toCanvas(event), dx = event.altKey ? point.x - drag.x : Math.round(point.x - drag.x), dy = event.altKey ? point.y - drag.y : Math.round(point.y - drag.y);
  if (!drag.pushed && dx === 0 && dy === 0) return;
  const updated = G.translate(drag.original, dx, dy);
  if (!drag.pushed) { pushHistory(); drag.pushed = true; }
  updateSelected(updated); geometryChanged();
}));
function endDrag(event) { if (svg.hasPointerCapture(event.pointerId)) svg.releasePointerCapture(event.pointerId); drag = null; }
svg.addEventListener('pointerup', endDrag); svg.addEventListener('pointercancel', endDrag);

function buildThumb(starter) {
  const thumbnail = document.createElementNS(SVGNS, 'svg'); thumbnail.setAttribute('viewBox', '-14 -14 28 28'); thumbnail.setAttribute('width', '34'); thumbnail.setAttribute('height', '34');
  const node = G.node({ id: 'starter', tag: starter.tag, attrs: starter.attrs }); node.setAttribute('fill', 'none'); node.setAttribute('stroke', 'currentColor'); node.setAttribute('stroke-width', '2'); node.setAttribute('stroke-linecap', 'round'); node.setAttribute('stroke-linejoin', 'round'); thumbnail.appendChild(node); return thumbnail;
}
function addElement(starter, x, y) {
  const element = G.translate({ id: newId(starter.tag), tag: starter.tag, attrs: starter.attrs }, x, y);
  pushHistory(); state.elements.push(element); state.selectedId = element.id; geometryChanged(`Added ${starter.tag}. Edit its geometry to suit the subject and references.`); svg.focus();
}
function buildPalette() {
  for (const starter of G.STARTERS) {
    const button = document.createElement('button'); button.className = 'palette-item'; button.title = `Add editable ${starter.tag}`; button.appendChild(buildThumb(starter));
    const label = document.createElement('span'); label.textContent = starter.name; button.appendChild(label);
    button.addEventListener('click', event => { if (event.detail === 0) attempt(() => addElement(starter, canvasSize() / 2, canvasSize() / 2)); });
    button.addEventListener('pointerdown', event => {
      if (event.button !== 0) return;
      event.preventDefault(); const startX = event.clientX, startY = event.clientY;
      const ghost = document.createElement('div'); ghost.id = 'drag-ghost'; ghost.appendChild(buildThumb(starter)); document.body.appendChild(ghost);
      const move = e => { ghost.style.left = `${e.clientX}px`; ghost.style.top = `${e.clientY}px`; };
      const cleanup = () => { window.removeEventListener('pointermove', move); window.removeEventListener('pointerup', end); window.removeEventListener('pointercancel', cleanup); ghost.remove(); };
      const end = e => {
        cleanup(); attempt(() => {
          if (Math.hypot(e.clientX - startX, e.clientY - startY) < 4) { addElement(starter, canvasSize() / 2, canvasSize() / 2); return; }
          const point = toCanvas(e); if (point.x >= 0 && point.x <= canvasSize() && point.y >= 0 && point.y <= canvasSize()) addElement(starter, Math.round(point.x), Math.round(point.y));
        });
      };
      move(event); window.addEventListener('pointermove', move); window.addEventListener('pointerup', end); window.addEventListener('pointercancel', cleanup);
    });
    $('palette-geometry').appendChild(button);
  }
}
function replaceKeyshapeOptions(select, profile) { select.replaceChildren(...profile.keyshapes.map(token => { const option = document.createElement('option'); option.value = token.name; option.textContent = token.name; return option; })); }
function syncProfileControls() {
  const profile = currentProfile(); $('icon-name').value = settings.iconName; $('icon-type-select').value = settings.iconType;
  replaceKeyshapeOptions($('keyshape-select'), profile);
  if (!keyshapeNamed(profile, settings.keyshape)) settings.keyshape = profile.keyshapes.find(token => token.orientation === 'square')?.name || profile.keyshapes[0].name;
  $('keyshape-select').value = settings.keyshape; $('container-keyshape-control').hidden = settings.iconType !== 'container';
  if (settings.iconType === 'container') {
    const acceptedProfile = profileFor(profile.containerSlot.acceptedProfile); replaceKeyshapeOptions($('container-keyshape-select'), acceptedProfile);
    if (!keyshapeNamed(acceptedProfile, settings.containerAcceptedKeyshape)) settings.containerAcceptedKeyshape = acceptedProfile.keyshapes.find(token => token.orientation === 'square')?.name || acceptedProfile.keyshapes[0].name;
    $('container-keyshape-select').value = settings.containerAcceptedKeyshape;
  }
  $('skeleton-toggle').checked = !!settings.showSkeleton; saveSettings(); renderGrid(); renderKeyshape(); render();
}
for (const [id, action] of Object.entries({ undo, copy: copySelected, paste: pasteClipboard, duplicate: duplicateSelected, delete: deleteSelected,
  backward: () => moveInStack(-1), forward: () => moveInStack(1), 'apply-geometry': applyGeometry,
  translate: () => moveSelected(G.numeric($('p-dx').value, 'ΔX'), G.numeric($('p-dy').value, 'ΔY')), export: exportJSON, preview: exportPreviewSVG,
  clear: () => { if (!state.elements.length) return; pushHistory(); state.elements = []; state.selectedId = null; geometryChanged('Cleared geometry. Undo is available.'); },
  source: () => { $('document-source').value = JSON.stringify(editableDocument(), null, 2); $('source-error').textContent = ''; $('source-dialog').showModal(); },
  'close-source': () => $('source-dialog').close(), import: () => $('import-file').click(),
})) $(`btn-${id}`).addEventListener('click', () => attempt(action));
$('btn-apply-source').addEventListener('click', () => { try { importDocument(JSON.parse($('document-source').value)); $('source-dialog').close(); } catch (error) { $('source-error').textContent = error.message; } });
$('import-file').addEventListener('change', async event => {
  const file = event.target.files[0]; if (!file) return;
  try {
    if (file.size > 1000000) throw new Error('Choose a JSON document smaller than 1 MB.');
    const document = validateDocument(JSON.parse(await file.text()));
    if (state.elements.length && !window.confirm('Replace the current document? Undo will restore it.')) return;
    importDocument(document);
  } catch (error) { status(error.message, true); } finally { event.target.value = ''; }
});
$('icon-name').addEventListener('input', () => { settings.iconName = $('icon-name').value.trim(); saveSettings(); });
$('icon-type-select').addEventListener('change', () => {
  const next = $('icon-type-select').value; if (next === settings.iconType) return;
  if (state.elements.length && !window.confirm('Changing icon type starts a new empty composition. Undo will restore this document. Continue?')) { $('icon-type-select').value = settings.iconType; return; }
  pushHistory(); settings.iconType = next; state.elements = []; state.metadata = {}; state.selectedId = null; clipboard = null; syncProfileControls(); status('Started a new composition using the selected profile.');
});
$('keyshape-select').addEventListener('change', () => { pushHistory(); settings.keyshape = $('keyshape-select').value; saveSettings(); renderKeyshape(); geometryChanged(); });
$('container-keyshape-select').addEventListener('change', () => { pushHistory(); settings.containerAcceptedKeyshape = $('container-keyshape-select').value; saveSettings(); renderKeyshape(); geometryChanged(); });
$('skeleton-toggle').addEventListener('change', () => { settings.showSkeleton = $('skeleton-toggle').checked; saveSettings(); render(); });
document.addEventListener('keydown', event => {
  if ($('source-dialog').open || ['INPUT', 'TEXTAREA', 'SELECT', 'BUTTON'].includes(document.activeElement?.tagName) || document.activeElement?.isContentEditable) return;
  if (event.metaKey || event.ctrlKey) {
    const action = { z: undo, c: copySelected, v: pasteClipboard, d: duplicateSelected }[event.key.toLowerCase()];
    if (action) { event.preventDefault(); attempt(action); } return;
  }
  const step = event.altKey ? 0.1 : 1, delta = { ArrowLeft: [-step, 0], ArrowRight: [step, 0], ArrowUp: [0, -step], ArrowDown: [0, step] }[event.key];
  if (delta && selected()) { event.preventDefault(); attempt(() => moveSelected(...delta, 'nudge')); }
  else if (['Delete', 'Backspace'].includes(event.key) && selected()) { event.preventDefault(); deleteSelected(); }
  else if (event.key === 'Escape') { state.selectedId = null; render(); }
  else if (event.key === '[') moveInStack(-1); else if (event.key === ']') moveInStack(1);
});
buildPalette();
syncProfileControls();
