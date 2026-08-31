'use strict';

/* Icon builder editor: 48x48 canvas, 1-unit snapping, drag/resize/rotate/flip,
 * fill & stroke styling, standalone SVG export. Depends on SHAPES (shapes.js). */

const SVGNS = 'http://www.w3.org/2000/svg';
const CANVAS_SIZE = 48;
const MIN_SIZE = 1;
const ROT_SNAP = 15;
const DEFAULT_FILL = '#1f2937';
const DEFAULT_STROKE = '#1f2937';

/* Persisted user settings. Stroke is in 48u design units; 4u is Regular. */
const SETTINGS_KEY = 'unlimited-shapes.settings.v3';
const settings = { strokeWidth: 4, keyshape: 'square-40', showSkeleton: false };
try {
  Object.assign(settings, JSON.parse(localStorage.getItem(SETTINGS_KEY)) || {});
} catch (e) { /* storage unavailable or corrupt — fall back to defaults */ }
function saveSettings() {
  try { localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings)); } catch (e) { /* ignore */ }
}
const storedStrokeWidth = Number(settings.strokeWidth);
settings.strokeWidth = Number.isFinite(storedStrokeWidth)
  ? Math.min(6, Math.max(0, storedStrokeWidth))
  : 4;
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
  node.setAttribute('fill', def.closed && inst.fillOn ? inst.fill : 'none');
  if (inst.strokeWidth > 0) {
    node.setAttribute('stroke', inst.stroke);
    node.setAttribute('stroke-width', fmt(inst.strokeWidth));
    node.setAttribute('stroke-linecap', 'round');
    node.setAttribute('stroke-linejoin', 'round');
  }
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
  const line = (x1, y1, x2, y2, color, width) => {
    const l = document.createElementNS(SVGNS, 'line');
    l.setAttribute('x1', x1); l.setAttribute('y1', y1);
    l.setAttribute('x2', x2); l.setAttribute('y2', y2);
    l.setAttribute('stroke', color);
    l.setAttribute('stroke-width', width);
    gridLayer.appendChild(l);
  };
  for (let v = 0; v <= CANVAS_SIZE; v += 1) {
    const major = v % 4 === 0;
    const center = v === CANVAS_SIZE / 2;
    const color = center ? '#aeb8c7' : major ? '#d1d7df' : '#edf0f4';
    const width = center ? 0.12 : major ? 0.08 : 0.035;
    line(v, 0, v, CANVAS_SIZE, color, width);
    line(0, v, CANVAS_SIZE, v, color, width);
  }
}

const KEYSHAPES = {
  'circle-44': { kind: 'circle', cx: 24, cy: 24, r: 22 },
  'square-40': { kind: 'rect', x: 4, y: 4, w: 40, h: 40 },
  'portrait-36x44': { kind: 'rect', x: 6, y: 2, w: 36, h: 44 },
  'landscape-44x36': { kind: 'rect', x: 2, y: 6, w: 44, h: 36 },
};

function renderKeyshape() {
  keyshapeLayer.replaceChildren();
  const token = KEYSHAPES[settings.keyshape] || KEYSHAPES['square-40'];
  const guide = document.createElementNS(SVGNS, token.kind);
  if (token.kind === 'circle') {
    guide.setAttribute('cx', token.cx); guide.setAttribute('cy', token.cy); guide.setAttribute('r', token.r);
  } else {
    guide.setAttribute('x', token.x); guide.setAttribute('y', token.y);
    guide.setAttribute('width', token.w); guide.setAttribute('height', token.h);
  }
  guide.setAttribute('fill', 'none');
  guide.setAttribute('stroke', '#16a34a');
  guide.setAttribute('stroke-width', '0.18');
  guide.setAttribute('stroke-dasharray', '0.8 0.8');
  keyshapeLayer.appendChild(guide);
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
  fill: document.getElementById('p-fill'),
  fillOn: document.getElementById('p-fill-on'),
  fillRow: document.getElementById('row-fill'),
  stroke: document.getElementById('p-stroke'),
  sw: document.getElementById('p-sw'),
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
  props.fillRow.hidden = !def.closed;
  props.fillOn.checked = !!inst.fillOn;
  setInput(props.fill, inst.fill);
  setInput(props.stroke, inst.stroke);
  setInput(props.sw, inst.strokeWidth);
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
bindNumberInput(props.sw, (i, v) => {
  i.strokeWidth = clamp(v, 0, 6);
  settings.strokeWidth = i.strokeWidth;
  saveSettings();
});

props.fill.addEventListener('input', () => {
  const inst = selected();
  if (inst) { pushHistory('fill'); inst.fill = props.fill.value; inst.fillOn = true; render(); }
});
props.fillOn.addEventListener('change', () => {
  const inst = selected();
  if (inst) { pushHistory(); inst.fillOn = props.fillOn.checked; render(); }
});
props.stroke.addEventListener('input', () => {
  const inst = selected();
  if (inst) { pushHistory('stroke'); inst.stroke = props.stroke.value; render(); }
});

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
buttons.export.addEventListener('click', exportSVG);

function exportSVG() {
  if (state.instances.length === 0) return;
  const body = state.instances
    .map(inst => `  ${buildInstanceNode(inst).outerHTML}`)
    .join('\n');
  const doc = `<svg xmlns="${SVGNS}" viewBox="0 0 ${CANVAS_SIZE} ${CANVAS_SIZE}" data-keyshape="${settings.keyshape}">\n${body}\n</svg>\n`;
  const blob = new Blob([doc], { type: 'image/svg+xml' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'icon.svg';
  a.click();
  URL.revokeObjectURL(url);
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
  for (const def of SHAPES) {
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
  const inst = {
    id: state.nextId++,
    shapeId,
    w: def.defaultW,
    h: def.defaultH,
    x: clamp(snap(cx - def.defaultW / 2), -def.defaultW / 2, CANVAS_SIZE - def.defaultW / 2),
    y: clamp(snap(cy - def.defaultH / 2), -def.defaultH / 2, CANVAS_SIZE - def.defaultH / 2),
    rotation: 0,
    flipX: false,
    flipY: false,
    fillOn: false,
    fill: DEFAULT_FILL,
    stroke: DEFAULT_STROKE,
    strokeWidth: clamp(settings.strokeWidth, 0, 6),
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
      addInstance(def.id, CANVAS_SIZE / 2, CANVAS_SIZE / 2);
      return;
    }
    const p = toCanvas(e);
    if (p.x >= 0 && p.x <= CANVAS_SIZE && p.y >= 0 && p.y <= CANVAS_SIZE) {
      addInstance(def.id, p.x, p.y);
    }
  };
  window.addEventListener('pointermove', onMove);
  window.addEventListener('pointerup', onUp);
}

/* ---------------- Keyboard ---------------- */

document.addEventListener('keydown', evt => {
  const tag = document.activeElement && document.activeElement.tagName;
  if (tag === 'INPUT' || tag === 'TEXTAREA') return;
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

const keyshapeSelect = document.getElementById('keyshape-select');
const skeletonToggle = document.getElementById('skeleton-toggle');
settings.keyshape = KEYSHAPES[settings.keyshape] ? settings.keyshape : 'square-40';
keyshapeSelect.value = settings.keyshape;
keyshapeSelect.addEventListener('change', () => {
  settings.keyshape = keyshapeSelect.value;
  saveSettings();
  renderKeyshape();
});
skeletonToggle.checked = !!settings.showSkeleton;
skeletonToggle.addEventListener('change', () => {
  settings.showSkeleton = skeletonToggle.checked;
  saveSettings();
  render();
});

renderGrid();
renderKeyshape();
buildPalette();
render();
