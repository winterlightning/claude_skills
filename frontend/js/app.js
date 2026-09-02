'use strict';

/* Profile-aware atomic icon editor with canonical-schema JSON scaffold export.
 * Depends on ICON_PROFILES (icon-profiles.js) and SHAPES (shapes.js). */

const SVGNS = 'http://www.w3.org/2000/svg';
const MIN_SIZE = 1;
const ROT_SNAP = 15;
const LEGACY_PALETTE_SHAPES = new Set(['rounded-square', 's-curve']);

function resolveProfile(iconType) {
  const raw = ICON_PROFILES.profiles[iconType];
  if (!raw) throw new Error(`Unknown icon profile: ${iconType}`);
  const base = raw.extends ? resolveProfile(raw.extends) : {};
  return { ...base, ...raw, iconType };
}

const profileFor = iconType => resolveProfile(iconType);
const currentProfile = () => profileFor(settings.iconType);
const canvasSize = () => currentProfile().designCanvas;

/* Persisted user settings. Geometry and Regular stroke come from the profile. */
const SETTINGS_KEY = 'unlimited-shapes.settings.v3';
const settings = {
  iconName: 'icon',
  iconType: ICON_PROFILES.defaultIconType,
  keyshape: 'square-40',
  containerAcceptedKeyshape: 'square-24',
  showSkeleton: false,
};
try {
  Object.assign(settings, JSON.parse(localStorage.getItem(SETTINGS_KEY)) || {});
} catch (e) { /* storage unavailable or corrupt — fall back to defaults */ }
function saveSettings() {
  try { localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings)); } catch (e) { /* ignore */ }
}
if (!ICON_PROFILES.profiles[settings.iconType]) settings.iconType = ICON_PROFILES.defaultIconType;
saveSettings();

const svg = document.getElementById('canvas');
const gridLayer = document.getElementById('grid');
const keyshapeLayer = document.getElementById('keyshape-guide');
const shapeLayer = document.getElementById('shapes');
const skeletonLayer = document.getElementById('skeletons');
const overlayLayer = document.getElementById('overlay');

const state = {
  instances: [],
  selectedId: null,
  nextId: 1,
};

const shapeById = id => SHAPES.find(s => s.id === id);
const selected = () => state.instances.find(i => i.id === state.selectedId) || null;

/* ---------------- History (undo) & clipboard ---------------- */

const history = [];
const HISTORY_MAX = 100;
let clipboard = null;

// Snapshot the document before a mutation. Consecutive pushes with the same
// tag within 800ms are coalesced so continuous gestures (typing in an input,
// dragging a color picker, repeated nudges) undo as a single step.
function pushHistory(tag) {
  const now = Date.now();
  const last = history[history.length - 1];
  if (tag && last && last.tag === tag && now - last.t < 800) {
    last.t = now;
    return;
  }
  history.push({
    tag, t: now,
    instances: JSON.parse(JSON.stringify(state.instances)),
    selectedId: state.selectedId,
  });
  if (history.length > HISTORY_MAX) history.shift();
}

function undo() {
  const snapshot = history.pop();
  if (!snapshot) return;
  state.instances = snapshot.instances;
  state.selectedId = snapshot.selectedId;
  render();
}

function copySelected() {
  const inst = selected();
  if (!inst) return;
  clipboard = { ...inst };
  renderToolbar();
}

function pasteClipboard() {
  if (!clipboard) return;
  pushHistory();
  // Each paste lands one unit further so repeated pastes cascade.
  clipboard = { ...clipboard, x: clipboard.x + 1, y: clipboard.y + 1 };
  const copy = { ...clipboard, id: state.nextId++ };
  state.instances.push(copy);
  state.selectedId = copy.id;
  render();
}
const snapStep = () => 1;
const snap = (v, step = snapStep()) => Math.round(v / step) * step;
const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v));
const fmt = v => String(+(+v).toFixed(3));

/* ---------------- Rendering ---------------- */

function makeShapeEl(def, w, h) {
  const geo = def.geometry(w, h);
  const el = document.createElementNS(SVGNS, geo.tag);
  for (const [k, v] of Object.entries(geo.attrs)) el.setAttribute(k, v);
  return el;
}

// Only rigid operations (translate, rotate, flip) — never scale, so stroke
// width is unaffected. Size lives in the geometry itself.
function instanceTransform(inst) {
  const cx = inst.x + inst.w / 2;
  const cy = inst.y + inst.h / 2;
  const fx = inst.flipX ? -1 : 1;
  const fy = inst.flipY ? -1 : 1;
  return `translate(${fmt(cx)} ${fmt(cy)}) rotate(${fmt(inst.rotation)}) ` +
         `scale(${fx} ${fy}) translate(${fmt(-inst.w / 2)} ${fmt(-inst.h / 2)})`;
}

function buildInstanceNode(inst) {
  const def = shapeById(inst.shapeId);
  const node = makeShapeEl(def, inst.w, inst.h);
  node.setAttribute('fill', 'none');
  node.setAttribute('stroke', 'currentColor');
  node.setAttribute('stroke-width', fmt(currentProfile().designStroke));
  node.setAttribute('stroke-linecap', 'round');
  node.setAttribute('stroke-linejoin', 'round');
  const g = document.createElementNS(SVGNS, 'g');
  g.setAttribute('transform', instanceTransform(inst));
  g.appendChild(node);
  return g;
}

function renderShapes() {
  shapeLayer.replaceChildren();
  for (const inst of state.instances) {
    const g = buildInstanceNode(inst);
    g.dataset.id = inst.id;
    g.style.cursor = 'move';
    shapeLayer.appendChild(g);
  }
}

function renderSkeletons() {
  skeletonLayer.replaceChildren();
  if (!settings.showSkeleton) return;

  for (const inst of state.instances) {
    const def = shapeById(inst.shapeId);
    const node = makeShapeEl(def, inst.w, inst.h);
    node.setAttribute('fill', 'none');
    node.setAttribute('stroke', '#ef4444');
    node.setAttribute('stroke-width', '0.01');
    node.setAttribute('stroke-linecap', 'round');
    node.setAttribute('stroke-linejoin', 'round');
    node.setAttribute('vector-effect', 'non-scaling-stroke');

    const g = document.createElementNS(SVGNS, 'g');
    g.setAttribute('transform', instanceTransform(inst));
    g.setAttribute('pointer-events', 'none');
    g.appendChild(node);
    skeletonLayer.appendChild(g);
  }
}

const HANDLE_CURSORS = {
  '-1,-1': 'nwse-resize', '1,1': 'nwse-resize',
  '1,-1': 'nesw-resize', '-1,1': 'nesw-resize',
  '0,-1': 'ns-resize', '0,1': 'ns-resize',
  '-1,0': 'ew-resize', '1,0': 'ew-resize',
};

function renderOverlay() {
  overlayLayer.replaceChildren();
  const inst = selected();
  if (!inst) return;

  const g = document.createElementNS(SVGNS, 'g');
  const cx = inst.x + inst.w / 2;
  const cy = inst.y + inst.h / 2;
  g.setAttribute('transform', `translate(${fmt(cx)} ${fmt(cy)}) rotate(${fmt(inst.rotation)})`);

  const box = document.createElementNS(SVGNS, 'rect');
  box.setAttribute('x', fmt(-inst.w / 2));
  box.setAttribute('y', fmt(-inst.h / 2));
  box.setAttribute('width', fmt(inst.w));
  box.setAttribute('height', fmt(inst.h));
  box.setAttribute('fill', 'none');
  box.setAttribute('stroke', '#3b82f6');
  box.setAttribute('stroke-width', '0.06');
  g.appendChild(box);

  // Rotate handle: a small circle above the top edge, connected by a stem.
  const stem = document.createElementNS(SVGNS, 'line');
  stem.setAttribute('x1', '0');
  stem.setAttribute('y1', fmt(-inst.h / 2));
  stem.setAttribute('x2', '0');
  stem.setAttribute('y2', fmt(-inst.h / 2 - 1));
  stem.setAttribute('stroke', '#3b82f6');
  stem.setAttribute('stroke-width', '0.06');
  g.appendChild(stem);

  const rot = document.createElementNS(SVGNS, 'circle');
  rot.setAttribute('cx', '0');
  rot.setAttribute('cy', fmt(-inst.h / 2 - 1.3));
  rot.setAttribute('r', '0.32');
  rot.setAttribute('fill', '#fff');
  rot.setAttribute('stroke', '#3b82f6');
  rot.setAttribute('stroke-width', '0.06');
  rot.dataset.rotate = '1';
  rot.style.cursor = 'grab';
  g.appendChild(rot);

  for (const hx of [-1, 0, 1]) {
    for (const hy of [-1, 0, 1]) {
      if (hx === 0 && hy === 0) continue;
      const h = document.createElementNS(SVGNS, 'rect');
      const size = 0.5;
      h.setAttribute('x', fmt(hx * inst.w / 2 - size / 2));
      h.setAttribute('y', fmt(hy * inst.h / 2 - size / 2));
      h.setAttribute('width', fmt(size));
      h.setAttribute('height', fmt(size));
      h.setAttribute('fill', '#fff');
      h.setAttribute('stroke', '#3b82f6');
      h.setAttribute('stroke-width', '0.06');
      h.dataset.handle = `${hx},${hy}`;
      h.style.cursor = HANDLE_CURSORS[`${hx},${hy}`];
      g.appendChild(h);
    }
  }
  overlayLayer.appendChild(g);

  if (settings.showSkeleton) {
    const r = inst.rotation * Math.PI / 180;
    const lx = -inst.w / 2;
    const ly = -inst.h / 2;
    const ox = cx + lx * Math.cos(r) - ly * Math.sin(r);
    const oy = cy + lx * Math.sin(r) + ly * Math.cos(r);
    const coordinates = document.createElementNS(SVGNS, 'g');
    coordinates.setAttribute('pointer-events', 'none');

    const origin = document.createElementNS(SVGNS, 'circle');
    origin.setAttribute('cx', fmt(ox));
    origin.setAttribute('cy', fmt(oy));
    origin.setAttribute('r', '0.18');
    origin.setAttribute('fill', '#ef4444');
    coordinates.appendChild(origin);

    const label = document.createElementNS(SVGNS, 'text');
    label.setAttribute('x', fmt(ox + 0.45));
    label.setAttribute('y', fmt(oy - 0.45));
    label.setAttribute('font-size', '1.05');
    label.setAttribute('font-family', 'ui-monospace, SFMono-Regular, Menlo, monospace');
    label.setAttribute('fill', '#dc2626');
    label.setAttribute('stroke', '#fff');
    label.setAttribute('stroke-width', '0.28');
    label.setAttribute('paint-order', 'stroke');
    label.textContent = `x:${fmt(inst.x)} y:${fmt(inst.y)}`;
    coordinates.appendChild(label);
    overlayLayer.appendChild(coordinates);
  }
}

function renderGrid() {
  gridLayer.replaceChildren();
  const size = canvasSize();
  svg.setAttribute('viewBox', `0 0 ${size} ${size}`);
  const line = (x1, y1, x2, y2, color, width) => {
    const l = document.createElementNS(SVGNS, 'line');
    l.setAttribute('x1', x1); l.setAttribute('y1', y1);
    l.setAttribute('x2', x2); l.setAttribute('y2', y2);
    l.setAttribute('stroke', color);
    l.setAttribute('stroke-width', width);
    gridLayer.appendChild(l);
  };
  for (let v = 0; v <= size; v += 1) {
    const major = v % 4 === 0;
    const center = v === size / 2;
    const color = center ? '#aeb8c7' : major ? '#d1d7df' : '#edf0f4';
    const width = center ? 0.12 : major ? 0.08 : 0.035;
    line(v, 0, v, size, color, width);
    line(0, v, size, v, color, width);
  }
}

function keyshapeNamed(profile, name) {
  return profile.keyshapes.find(keyshape => keyshape.name === name) || null;
}

function appendKeyshapeGuide(profile, token, offsetX = 0, offsetY = 0, protectedRegion = false) {
  const guide = document.createElementNS(SVGNS, token.shape === 'circle' ? 'circle' : 'rect');
  if (token.shape === 'circle') {
    guide.setAttribute('cx', profile.center.x + offsetX);
    guide.setAttribute('cy', profile.center.y + offsetY);
    guide.setAttribute('r', token.diameter / 2);
  } else {
    guide.setAttribute('x', profile.center.x - token.width / 2 + offsetX);
    guide.setAttribute('y', profile.center.y - token.height / 2 + offsetY);
    guide.setAttribute('width', token.width);
    guide.setAttribute('height', token.height);
  }
  guide.setAttribute('fill', 'none');
  guide.setAttribute('stroke', protectedRegion ? '#dc2626' : '#16a34a');
  guide.setAttribute('stroke-width', '0.18');
  guide.setAttribute('stroke-dasharray', protectedRegion ? '0.35 0.55' : '0.8 0.8');
  guide.setAttribute('pointer-events', 'none');
  keyshapeLayer.appendChild(guide);
}

function appendContainerSlotGuide(slot) {
  const guide = document.createElementNS(SVGNS, 'rect');
  guide.setAttribute('x', slot.x);
  guide.setAttribute('y', slot.y);
  guide.setAttribute('width', slot.w);
  guide.setAttribute('height', slot.h);
  guide.setAttribute('fill', 'none');
  guide.setAttribute('stroke', '#7c3aed');
  guide.setAttribute('stroke-width', '0.14');
  guide.setAttribute('stroke-dasharray', '1 1');
  guide.setAttribute('pointer-events', 'none');
  guide.dataset.containerSlotGuide = 'true';
  keyshapeLayer.appendChild(guide);
}

function renderKeyshape() {
  keyshapeLayer.replaceChildren();
  const profile = currentProfile();
  const token = keyshapeNamed(profile, settings.keyshape) || profile.keyshapes[0];
  appendKeyshapeGuide(profile, token);

  if (settings.iconType === 'container') {
    const acceptedProfile = profileFor(profile.containerSlot.acceptedProfile);
    const accepted = keyshapeNamed(acceptedProfile, settings.containerAcceptedKeyshape) || acceptedProfile.keyshapes[0];
    appendContainerSlotGuide(profile.containerSlot);
    appendKeyshapeGuide(
      acceptedProfile,
      accepted,
      profile.containerSlot.x,
      profile.containerSlot.y,
      true,
    );
  }
}

function render() {
  renderShapes();
  renderSkeletons();
  renderOverlay();
  renderProps();
  renderToolbar();
}

/* ---------------- Properties panel ---------------- */

const props = {
  empty: document.getElementById('props-empty'),
  body: document.getElementById('props-body'),
  title: document.getElementById('props-title'),
  x: document.getElementById('p-x'),
  y: document.getElementById('p-y'),
  cx: document.getElementById('p-cx'),
  cy: document.getElementById('p-cy'),
  w: document.getElementById('p-w'),
  h: document.getElementById('p-h'),
  rot: document.getElementById('p-rot'),
};

function setInput(input, value) {
  if (document.activeElement !== input) input.value = value;
}

function renderProps() {
  const inst = selected();
  props.empty.hidden = !!inst;
  props.body.hidden = !inst;
  if (!inst) return;
  const def = shapeById(inst.shapeId);
  props.title.textContent = def.name;
  setInput(props.x, inst.x);
  setInput(props.y, inst.y);
  setInput(props.cx, inst.x + inst.w / 2);
  setInput(props.cy, inst.y + inst.h / 2);
  setInput(props.w, inst.w);
  setInput(props.h, inst.h);
  setInput(props.rot, inst.rotation);
}

function bindNumberInput(input, apply) {
  input.addEventListener('input', () => {
    const inst = selected();
    const v = parseFloat(input.value);
    if (!inst || Number.isNaN(v)) return;
    pushHistory(`input:${input.id}`);
    apply(inst, v);
    render();
  });
}

bindNumberInput(props.x, (i, v) => { i.x = v; });
bindNumberInput(props.y, (i, v) => { i.y = v; });
bindNumberInput(props.cx, (i, v) => { i.x = v - i.w / 2; });
bindNumberInput(props.cy, (i, v) => { i.y = v - i.h / 2; });
bindNumberInput(props.w, (i, v) => { i.w = Math.max(MIN_SIZE, v); });
bindNumberInput(props.h, (i, v) => { i.h = Math.max(MIN_SIZE, v); });
bindNumberInput(props.rot, (i, v) => { i.rotation = ((v % 360) + 360) % 360; });

document.getElementById('btn-flip-h').addEventListener('click', () => {
  const inst = selected();
  if (inst) { pushHistory(); inst.flipX = !inst.flipX; render(); }
});
document.getElementById('btn-flip-v').addEventListener('click', () => {
  const inst = selected();
  if (inst) { pushHistory(); inst.flipY = !inst.flipY; render(); }
});

/* ---------------- Toolbar ---------------- */

const buttons = {
  undo: document.getElementById('btn-undo'),
  copy: document.getElementById('btn-copy'),
  paste: document.getElementById('btn-paste'),
  forward: document.getElementById('btn-forward'),
  backward: document.getElementById('btn-backward'),
  duplicate: document.getElementById('btn-duplicate'),
  del: document.getElementById('btn-delete'),
  clear: document.getElementById('btn-clear'),
  preview: document.getElementById('btn-preview'),
  export: document.getElementById('btn-export'),
};

function renderToolbar() {
  const hasSel = !!selected();
  buttons.undo.disabled = history.length === 0;
  buttons.copy.disabled = !hasSel;
  buttons.paste.disabled = !clipboard;
  buttons.forward.disabled = !hasSel;
  buttons.backward.disabled = !hasSel;
  buttons.duplicate.disabled = !hasSel;
  buttons.del.disabled = !hasSel;
  buttons.clear.disabled = state.instances.length === 0;
  buttons.preview.disabled = state.instances.length === 0;
  buttons.export.disabled = state.instances.length === 0;
}

function deleteSelected() {
  const inst = selected();
  if (!inst) return;
  pushHistory();
  state.instances = state.instances.filter(i => i !== inst);
  state.selectedId = null;
  render();
}

function duplicateSelected() {
  const inst = selected();
  if (!inst) return;
  pushHistory();
  const copy = { ...inst, id: state.nextId++, x: inst.x + 1, y: inst.y + 1 };
  state.instances.push(copy);
  state.selectedId = copy.id;
  render();
}

function moveInStack(dir) {
  const inst = selected();
  if (!inst) return;
  const i = state.instances.indexOf(inst);
  const j = i + dir;
  if (j < 0 || j >= state.instances.length) return;
  pushHistory('stack');
  [state.instances[i], state.instances[j]] = [state.instances[j], state.instances[i]];
  render();
}

buttons.undo.addEventListener('click', undo);
buttons.copy.addEventListener('click', copySelected);
buttons.paste.addEventListener('click', pasteClipboard);
buttons.forward.addEventListener('click', () => moveInStack(1));
buttons.backward.addEventListener('click', () => moveInStack(-1));
buttons.duplicate.addEventListener('click', duplicateSelected);
buttons.del.addEventListener('click', deleteSelected);
buttons.clear.addEventListener('click', () => {
  if (state.instances.length === 0) return;
  pushHistory();
  state.instances = [];
  state.selectedId = null;
  render();
});
buttons.preview.addEventListener('click', exportPreviewSVG);
buttons.export.addEventListener('click', exportJSON);

function validatedIconName() {
  const input = document.getElementById('icon-name');
  const name = input.value.trim();
  const valid = /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(name);
  input.setCustomValidity(valid ? '' : 'Use a kebab-case name such as coffee-mug.');
  if (!valid) input.reportValidity();
  return valid ? name : null;
}

function download(filename, body, type) {
  const blob = new Blob([body], { type });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement('a');
  anchor.href = url;
  anchor.download = filename;
  anchor.click();
  URL.revokeObjectURL(url);
}

function editableDocument(name) {
  const profile = currentProfile();
  const document = {
    name,
    iconType: settings.iconType,
    canvas: profile.designCanvas,
    strokeWidth: profile.designStroke,
    keyfitCheck: { targetToken: settings.keyshape },
    cornerStyle: 'round',
    sourceAnalysis: {
      incomplete: true,
      mappings: [],
      relationships: [],
      spacingChecks: [],
    },
    instances: state.instances.map((instance, z) => ({
      shapeId: instance.shapeId,
      x: instance.x,
      y: instance.y,
      w: instance.w,
      h: instance.h,
      rotation: instance.rotation,
      flipX: instance.flipX,
      flipY: instance.flipY,
      z,
    })),
  };
  if (settings.iconType === 'container') {
    document.containerSlot = {
      x: profile.containerSlot.x,
      y: profile.containerSlot.y,
      w: profile.containerSlot.w,
      h: profile.containerSlot.h,
      acceptedKeyshape: settings.containerAcceptedKeyshape,
    };
  }
  return document;
}

function exportJSON() {
  if (state.instances.length === 0) return;
  const name = validatedIconName();
  if (!name) return;
  download(`${name}.json`, `${JSON.stringify(editableDocument(name), null, 2)}\n`, 'application/json');
}

function exportPreviewSVG() {
  if (state.instances.length === 0) return;
  const name = validatedIconName();
  if (!name) return;
  const profile = currentProfile();
  const body = state.instances
    .map(inst => `  ${buildInstanceNode(inst).outerHTML}`)
    .join('\n');
  const doc = `<svg xmlns="${SVGNS}" viewBox="0 0 ${profile.designCanvas} ${profile.designCanvas}" fill="none" stroke="currentColor" stroke-width="${profile.designStroke}" stroke-linecap="round" stroke-linejoin="round" data-icon-type="${settings.iconType}" data-keyshape="${settings.keyshape}">\n${body}\n</svg>\n`;
  download(`${name}-preview.svg`, doc, 'image/svg+xml');
}

/* ---------------- Canvas interactions ---------------- */

function toCanvas(evt) {
  const p = new DOMPoint(evt.clientX, evt.clientY)
    .matrixTransform(svg.getScreenCTM().inverse());
  return { x: p.x, y: p.y };
}

let drag = null;

svg.addEventListener('pointerdown', evt => {
  const rotateEl = evt.target.closest('[data-rotate]');
  const handleEl = evt.target.closest('[data-handle]');
  const shapeEl = evt.target.closest('#shapes > g[data-id]');
  const p = toCanvas(evt);

  if (rotateEl && selected()) {
    drag = { mode: 'rotate', inst: selected() };
  } else if (handleEl && selected()) {
    const [hx, hy] = handleEl.dataset.handle.split(',').map(Number);
    const inst = selected();
    drag = {
      mode: 'resize', inst, hx, hy,
      start: { cx: inst.x + inst.w / 2, cy: inst.y + inst.h / 2, w: inst.w, h: inst.h },
    };
  } else if (shapeEl) {
    const inst = state.instances.find(i => i.id === +shapeEl.dataset.id);
    state.selectedId = inst.id;
    drag = { mode: 'move', inst, startX: inst.x, startY: inst.y, px: p.x, py: p.y };
    render();
  } else {
    state.selectedId = null;
    render();
    return;
  }
  evt.preventDefault();
  svg.setPointerCapture(evt.pointerId);
});

svg.addEventListener('pointermove', evt => {
  if (!drag) return;
  const p = toCanvas(evt);
  const inst = drag.inst;
  // Snapshot lazily on the first actual change, so a plain click-to-select
  // doesn't create an empty undo step.
  if (!drag.pushed) {
    pushHistory();
    drag.pushed = true;
  }

  if (drag.mode === 'move') {
    inst.x = snap(drag.startX + (p.x - drag.px));
    inst.y = snap(drag.startY + (p.y - drag.py));
  } else if (drag.mode === 'rotate') {
    const cx = inst.x + inst.w / 2;
    const cy = inst.y + inst.h / 2;
    const angle = Math.atan2(p.y - cy, p.x - cx) * 180 / Math.PI + 90;
    inst.rotation = ((snap(angle, ROT_SNAP) % 360) + 360) % 360;
  } else if (drag.mode === 'resize') {
    resizeTo(inst, drag, p, evt.shiftKey);
  }
  render();
});

function endDrag(evt) {
  if (drag && svg.hasPointerCapture(evt.pointerId)) svg.releasePointerCapture(evt.pointerId);
  drag = null;
}
svg.addEventListener('pointerup', endDrag);
svg.addEventListener('pointercancel', endDrag);

// Resize in the shape's rotated frame, anchored at the opposite edge/corner.
function resizeTo(inst, { hx, hy, start }, p, keepAspect) {
  const r = inst.rotation * Math.PI / 180;
  const cos = Math.cos(r), sin = Math.sin(r);
  // World position of the anchor (the point opposite the dragged handle).
  const alx = -hx * start.w / 2, aly = -hy * start.h / 2;
  const ax = start.cx + alx * cos - aly * sin;
  const ay = start.cy + alx * sin + aly * cos;
  // Pointer offset from the anchor, expressed in the shape's local frame.
  const dx = p.x - ax, dy = p.y - ay;
  const lx = dx * cos + dy * sin;
  const ly = -dx * sin + dy * cos;

  let w = hx !== 0 ? Math.max(MIN_SIZE, snap(hx * lx)) : start.w;
  let h = hy !== 0 ? Math.max(MIN_SIZE, snap(hy * ly)) : start.h;
  if (keepAspect && hx !== 0 && hy !== 0) {
    const k = Math.max(w / start.w, h / start.h);
    w = Math.max(MIN_SIZE, snap(start.w * k));
    h = Math.max(MIN_SIZE, snap(start.h * k));
  }

  const nlx = hx !== 0 ? hx * w / 2 : 0;
  const nly = hy !== 0 ? hy * h / 2 : 0;
  const ncx = ax + nlx * cos - nly * sin;
  const ncy = ay + nlx * sin + nly * cos;
  inst.w = w;
  inst.h = h;
  inst.x = ncx - w / 2;
  inst.y = ncy - h / 2;
}

/* ---------------- Palette ---------------- */

function buildThumb(def, px) {
  const { w: nw, h: nh } = def.natural;
  const thumb = document.createElementNS(SVGNS, 'svg');
  thumb.setAttribute('viewBox', `-1.25 -1.25 ${nw + 2.5} ${nh + 2.5}`);
  const scale = px / Math.max(nw, nh);
  thumb.setAttribute('width', Math.round(nw * scale));
  thumb.setAttribute('height', Math.max(10, Math.round(nh * scale)));
  const node = makeShapeEl(def, nw, nh);
  node.setAttribute('fill', 'none');
  node.setAttribute('stroke', 'currentColor');
  node.setAttribute('stroke-width', '1.5');
  node.setAttribute('stroke-linecap', 'round');
  node.setAttribute('stroke-linejoin', 'round');
  thumb.appendChild(node);
  return thumb;
}

function buildPalette() {
  const containers = {
    closed: document.getElementById('palette-closed'),
    open: document.getElementById('palette-open'),
  };
  for (const def of SHAPES.filter(shape => !LEGACY_PALETTE_SHAPES.has(shape.id))) {
    const item = document.createElement('div');
    item.className = 'palette-item';
    item.title = def.name;
    item.appendChild(buildThumb(def, 34));
    const label = document.createElement('span');
    label.textContent = def.name;
    item.appendChild(label);
    item.addEventListener('pointerdown', evt => startPaletteDrag(evt, def));
    containers[def.closed ? 'closed' : 'open'].appendChild(item);
  }
}

function addInstance(shapeId, cx, cy) {
  pushHistory();
  const def = shapeById(shapeId);
  const size = canvasSize();
  const profile = currentProfile();
  const maximumCenterlineExtent = Math.max(
    ...profile.keyshapes.flatMap(token => [token.width, token.height]),
  ) - profile.designStroke;
  let fit = 1;
  while (Math.max(def.defaultW, def.defaultH) * fit > maximumCenterlineExtent) {
    fit /= 2;
  }
  // A uniform power-of-two fit preserves atom proportions and angle-critical
  // relationships. Independent width/height rounding can turn a 45° contour
  // into an off-grid one.
  const width = Math.max(MIN_SIZE, def.defaultW * fit);
  const height = Math.max(MIN_SIZE, def.defaultH * fit);
  const inst = {
    id: state.nextId++,
    shapeId,
    w: width,
    h: height,
    x: clamp(snap(cx - width / 2), 0, size - width),
    y: clamp(snap(cy - height / 2), 0, size - height),
    rotation: 0,
    flipX: false,
    flipY: false,
  };
  state.instances.push(inst);
  state.selectedId = inst.id;
  render();
}

function startPaletteDrag(evt, def) {
  evt.preventDefault();
  const ghost = document.createElement('div');
  ghost.id = 'drag-ghost';
  ghost.appendChild(buildThumb(def, 40));
  document.body.appendChild(ghost);

  const startX = evt.clientX, startY = evt.clientY;
  let moved = false;
  const place = e => {
    ghost.style.left = `${e.clientX}px`;
    ghost.style.top = `${e.clientY}px`;
  };
  place(evt);

  const onMove = e => {
    if (Math.hypot(e.clientX - startX, e.clientY - startY) > 4) moved = true;
    place(e);
  };
  const onUp = e => {
    window.removeEventListener('pointermove', onMove);
    window.removeEventListener('pointerup', onUp);
    ghost.remove();
    if (!moved) {
      // Plain click: drop the shape at the center of the canvas.
      addInstance(def.id, canvasSize() / 2, canvasSize() / 2);
      return;
    }
    const p = toCanvas(e);
    const size = canvasSize();
    if (p.x >= 0 && p.x <= size && p.y >= 0 && p.y <= size) {
      addInstance(def.id, p.x, p.y);
    }
  };
  window.addEventListener('pointermove', onMove);
  window.addEventListener('pointerup', onUp);
}

/* ---------------- Keyboard ---------------- */

document.addEventListener('keydown', evt => {
  const tag = document.activeElement && document.activeElement.tagName;
  if (['INPUT', 'TEXTAREA', 'SELECT', 'BUTTON'].includes(tag) || document.activeElement?.isContentEditable) return;
  const inst = selected();

  if (evt.metaKey || evt.ctrlKey) {
    const key = evt.key.toLowerCase();
    if (key === 'd' && inst) { evt.preventDefault(); duplicateSelected(); }
    else if (key === 'c' && inst) { evt.preventDefault(); copySelected(); }
    else if (key === 'v' && clipboard) { evt.preventDefault(); pasteClipboard(); }
    else if (key === 'z') { evt.preventDefault(); undo(); }
    return;
  }
  if (!inst) return;

  const s = snapStep();
  const nudge = { ArrowLeft: [-s, 0], ArrowRight: [s, 0], ArrowUp: [0, -s], ArrowDown: [0, s] }[evt.key];
  if (nudge) {
    evt.preventDefault();
    pushHistory('nudge');
    inst.x = snap(inst.x + nudge[0]);
    inst.y = snap(inst.y + nudge[1]);
    render();
  } else if (evt.key === 'Delete' || evt.key === 'Backspace') {
    evt.preventDefault();
    deleteSelected();
  } else if (evt.key === 'Escape') {
    state.selectedId = null;
    render();
  } else if (evt.key === ']') {
    moveInStack(1);
  } else if (evt.key === '[') {
    moveInStack(-1);
  }
});

/* ---------------- Init ---------------- */

const iconNameInput = document.getElementById('icon-name');
const iconTypeSelect = document.getElementById('icon-type-select');
const keyshapeSelect = document.getElementById('keyshape-select');
const containerKeyshapeControl = document.getElementById('container-keyshape-control');
const containerKeyshapeSelect = document.getElementById('container-keyshape-select');
const skeletonToggle = document.getElementById('skeleton-toggle');

function replaceKeyshapeOptions(select, profile) {
  select.replaceChildren(...profile.keyshapes.map(token => {
    const option = document.createElement('option');
    option.value = token.name;
    option.textContent = token.name;
    return option;
  }));
}

function syncProfileControls() {
  const profile = currentProfile();
  replaceKeyshapeOptions(keyshapeSelect, profile);
  if (!keyshapeNamed(profile, settings.keyshape)) {
    settings.keyshape = profile.keyshapes.find(token => token.orientation === 'square')?.name || profile.keyshapes[0].name;
  }
  keyshapeSelect.value = settings.keyshape;

  const isContainer = settings.iconType === 'container';
  containerKeyshapeControl.hidden = !isContainer;
  if (isContainer) {
    const acceptedProfile = profileFor(profile.containerSlot.acceptedProfile);
    replaceKeyshapeOptions(containerKeyshapeSelect, acceptedProfile);
    if (!keyshapeNamed(acceptedProfile, settings.containerAcceptedKeyshape)) {
      settings.containerAcceptedKeyshape = acceptedProfile.keyshapes.find(token => token.orientation === 'square')?.name || acceptedProfile.keyshapes[0].name;
    }
    containerKeyshapeSelect.value = settings.containerAcceptedKeyshape;
  }
  saveSettings();
  renderGrid();
  renderKeyshape();
  render();
}

settings.iconName = /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(settings.iconName) ? settings.iconName : 'icon';
iconNameInput.value = settings.iconName;
iconNameInput.addEventListener('input', () => {
  iconNameInput.setCustomValidity('');
  settings.iconName = iconNameInput.value.trim();
  saveSettings();
});

iconTypeSelect.value = settings.iconType;
iconTypeSelect.addEventListener('change', () => {
  const nextIconType = iconTypeSelect.value;
  if (nextIconType === settings.iconType) return;
  const hasProfileState = state.instances.length > 0 || history.length > 0 || clipboard !== null;
  if (hasProfileState) {
    const reset = window.confirm(
      'Changing icon type clears the current composition, undo history, and clipboard so geometry from one profile cannot leak into another. Continue?',
    );
    if (!reset) {
      iconTypeSelect.value = settings.iconType;
      return;
    }
    state.instances = [];
    state.selectedId = null;
    state.nextId = 1;
    history.length = 0;
    clipboard = null;
  }
  settings.iconType = nextIconType;
  syncProfileControls();
});
keyshapeSelect.addEventListener('change', () => {
  settings.keyshape = keyshapeSelect.value;
  saveSettings();
  renderKeyshape();
});
containerKeyshapeSelect.addEventListener('change', () => {
  settings.containerAcceptedKeyshape = containerKeyshapeSelect.value;
  saveSettings();
  renderKeyshape();
});
skeletonToggle.checked = !!settings.showSkeleton;
skeletonToggle.addEventListener('change', () => {
  settings.showSkeleton = skeletonToggle.checked;
  saveSettings();
  render();
});

buildPalette();
syncProfileControls();
