// The layout editor's state and actions (the old side-layout-editor.js, carried over line for line without its DOM):
// move and resize the main, the sub, or any chosen set of their elements, snapped to the grid. Boxes are
// centerline units (the painted box is ±2, stroke 4). Width and height are independent; Shift keeps the proportions.
// A unit is what moves as one piece: a connected element by default, or a single path once split.
// Every composition happens in this browser (side-pairs-data.js / combine-side.js); saving stores the build.

export const STROKE = 4, EDGE = 1e-9, PADDING = 2;
// Size presets every 4 units: a role's keyshape grows or shrinks by the same amount on both axes.
// 64 pairs: main SOLO48 keyshapes, 32–64, 48 automatic; sub SUB32 keyshapes, 20–44, 32 automatic.
// 72 pairs: main on 54 (38–70, 54 automatic), sub on 36 (24–48, 36 automatic), tracer's 54 / 36 keyshapes.
export const PRESET_SETS = {
  64: {main: {base: 48, sizes: Array.from({length: 9}, (_v, i) => 32 + 4 * i), label: 'Main'},
       sub: {base: 32, sizes: Array.from({length: 7}, (_v, i) => 20 + 4 * i), label: 'Sub'}},
  72: {main: {base: 54, sizes: Array.from({length: 9}, (_v, i) => 38 + 4 * i), label: 'Main'},
       sub: {base: 36, sizes: Array.from({length: 7}, (_v, i) => 24 + 4 * i), label: 'Sub'}}};
// The keyshapes the 72 parts are drawn on: tracer's gridicon/rules.py KEYSHAPES_BY_GRID[54] and [36], outer boxes
// (x, y, w, h) on the part's grid, named by size so they read like the 64 ones (Tall / Wide L, M, S).
const KEYSHAPES72 = {
  main: {CIRCLE: [2, 2, 50, 50], SQUARE: [4, 4, 46, 46], portrait_L: [6, 2, 42, 50], landscape_L: [2, 6, 50, 42], tall_M: [8, 2, 38, 50],
         wide_M: [2, 8, 50, 38], slim_S: [11, 2, 32, 50], flat_S: [2, 11, 50, 32]},
  sub: {CIRCLE: [0, 0, 36, 36], SQUARE: [0, 0, 36, 36], portrait_L: [2, 0, 32, 36], landscape_L: [0, 2, 36, 32], tall_M: [4, 0, 28, 36],
        wide_M: [0, 4, 36, 28], slim_S: [6, 0, 24, 36], flat_S: [0, 6, 36, 24]}};
export const ANCHORS = {br: [1, 1], bl: [0, 1], tr: [1, 0], tl: [0, 0], ri: [1, .5], le: [0, .5], bo: [.5, 1], to: [.5, 0]};
export const SIDES = {br: 'Bottom-right', bl: 'Bottom-left', tr: 'Top-right', tl: 'Top-left', ri: 'Right', le: 'Left', bo: 'Bottom', to: 'Top'};
export const fmt = n => String(Math.round(n * 100) / 100);

// A unit maps its source box onto (x, y, w, h). A flat axis (a straight rule) has no scale of its own.
export const scales = u => {
  const sw = u.src[2] - u.src[0], sh = u.src[3] - u.src[1];
  const sx = sw > EDGE ? u.w / sw : null, sy = sh > EDGE ? u.h / sh : null;
  return [sx ?? sy ?? 1, sy ?? sx ?? 1];
};
export const boxOf = u => [u.x, u.y, u.x + u.w, u.y + u.h];
export const unionOf = list => list.map(boxOf).reduce((a, b) => [Math.min(a[0], b[0]), Math.min(a[1], b[1]), Math.max(a[2], b[2]), Math.max(a[3], b[3])]);
export const keyOf = (role, i) => role + ':' + i;

// The contract's SOLO48 / SUB32 keyshapes (laboratory.json), as the presets read them: name → centerline bounds.
let keyshapesLoaded = null;
function contractKeyshapes() {
  return keyshapesLoaded ??= fetch('laboratory.json', {cache: 'no-cache'}).then(r => r.ok ? r.json() : null).catch(() => null).then(d => {
    const of = profile => Object.fromEntries(Object.entries(d?.keyshapes?.resolved?.[profile] || {}).map(([n, k]) => [n, k.centerline_bounds]).filter(([, b]) => Array.isArray(b)));
    return {main: of('SOLO48'), sub: of('SUB32')};
  });
}
// At 72: KEYSHAPES72 as centerline bounds (half the 4-unit stroke inside each outer box).
const keyshapes72 = () => Object.fromEntries(Object.entries(KEYSHAPES72).map(([role, table]) =>
  [role, Object.fromEntries(Object.entries(table).map(([name, [x, y, w, h]]) => [name, [x + 2, y + 2, x + w - 2, y + h - 2]]))]));

export class LayoutEditor {
  version = $state(0);
  open = $state(false);
  // Counts openings: the dialog opens on each, even when it was closed without telling (no close event).
  shown = $state(0);
  readout = $state({text: '', bad: false});
  error = $state('');
  centerline = $state(true);
  // the pairs using this main (Apply panel), given by the page
  pairsWithMain = () => [];
  applied = () => {};
  ctx = null;
  presets = PRESET_SETS[64];

  constructor() { try { this.centerline = localStorage.getItem('side-layout-centerline') !== 'off'; } catch { /* no storage */ } }
  touchView() { this.version++; }
  setCenterline(on) { this.centerline = on;try { localStorage.setItem('side-layout-centerline', on ? 'on' : 'off'); } catch { /* no storage */ } this.touchView(); }

  // The pair combined in this browser, with no layout (automatic) or `body.layout`; with `elements`, each part's
  // elements and groups as the editor moves them (SideData.elements).
  async combine(body) {
    const data = window.SideData, composed = await data.compose(body.id, {layout: body.layout ?? null});
    const out = {...composed.result, svg: composed.svg};
    if (body.elements) {
      try { out.elements = Object.fromEntries(['main', 'sub'].map(role => [role, data.elements(composed, role, body.layout?.[role])])); }
      catch (e) { out.elements = null;out.elements_error = e.message; }
      out.keyshapes = data.size() === 72 ? keyshapes72() : await contractKeyshapes();
    }
    return out;
  }
  // `saved` is the pair's saved hand layout, if any.
  async show(pair, main, sub, onSaved, saved = null) {
    this.open = true;this.shown++;
    await this.load(pair, main, sub, onSaved, saved);
  }
  close() { this.open = false;this.touchView(); }
  async load(pair, main, sub, onSaved, saved) {
    this.presets = PRESET_SETS[window.SideData.size()] || PRESET_SETS[64];
    this.ctx = {pair, main, sub, onSaved, saved, canvas: window.SideData.sizes().canvas, roles: {}, dirty: new Set(), sel: new Set(),
                level: this.ctx?.level || 'whole', busy: false, token: 0, result: null, stale: false, combining: false, targets: null,
                applyResults: null, applyOpen: this.ctx?.applyOpen, preset: {}, shapes: null, keyshapes: {}, loaded: false};
    const ctx = this.ctx;
    this.error = '';this.readout = {text: 'Loading elements…', bad: false};this.touchView();
    let data;
    try { data = await this.combine({id: pair.id, elements: true, ...(saved ? {layout: saved} : {})}); }
    catch (e) {
      if (!saved) { this.readout = {text: '', bad: false};this.error = e.message;this.touchView();return; }
      try { data = await this.combine({id: pair.id, elements: true});this.error = 'The saved layout no longer fits these drawings: ' + e.message; }
      catch (e2) { this.readout = {text: '', bad: false};this.error = e2.message;this.touchView();return; }
    }
    if (this.ctx !== ctx) return;
    ctx.result = data;
    if (!data.elements) { this.readout = {text: '', bad: false};this.error = data.elements_error || 'This pair cannot be adjusted.';this.touchView();return; }
    ctx.canvas = data.canvas || 64;ctx.keyshapes = data.keyshapes || {};
    for (const [role, c] of Object.entries(data.elements)) {
      ctx.roles[role] = {markup: c.markup, names: c.names, sources: c.sources,
                         units: c.groups.map(g => { const b = g.box;return {paths: g.paths, src: g.source, x: b[0], y: b[1], w: b[2] - b[0], h: b[3] - b[1]}; })};
      if (saved?.[role]) ctx.dirty.add(role);
    }
    ctx.loaded = true;
    const pairs = this.pairsWithMain(main.icon, pair.id);
    ctx.targets = new Set(pairs.filter(p => p.position === pair.position).map(p => p.id));
    this.status();
  }

  selected() { const ctx = this.ctx;return [...ctx.sel].map(k => { const [role, i] = k.split(':');return ctx.roles[role]?.units[Number(i)]; }).filter(Boolean); }
  selectedRoles() { return new Set([...this.ctx.sel].map(k => k.split(':')[0])); }
  outside(b) { const c = this.ctx.canvas;return b[0] - 2 < -1e-6 || b[1] - 2 < -1e-6 || b[2] + 2 > c + 1e-6 || b[3] + 2 > c + 1e-6; }
  anyOutside() { return Object.values(this.ctx.roles).some(r => r.units.some(u => this.outside(boxOf(u)))); }

  // The first edit of a role snaps every one of its units onto the grid (edges, so touching units stay touching).
  touch(roles) {
    for (const role of roles) {
      if (this.ctx.dirty.has(role)) continue;this.ctx.dirty.add(role);
      for (const u of this.ctx.roles[role].units) {
        const x1 = Math.round(u.x + u.w), y1 = Math.round(u.y + u.h);u.x = Math.round(u.x);u.y = Math.round(u.y);u.w = x1 - u.x;u.h = y1 - u.y;
      }
    }
  }
  layout() {
    const out = {};
    for (const role of this.ctx.dirty) out[role] = this.ctx.roles[role].units.map(u => ({paths: u.paths, x: u.x, y: u.y, w: u.w, h: u.h}));
    return Object.keys(out).length ? out : null;
  }
  // Split units (keys) into one unit per path, each keeping exactly where it is drawn now.
  // The selection follows; returns {role: {path: key}} for every path of every unit.
  splitUnits(targets) {
    const ctx = this.ctx;
    this.touch(new Set([...targets].map(k => k.split(':')[0])));
    const remap = new Map(), byPath = {};
    for (const [role, r] of Object.entries(ctx.roles)) {
      const units = [];byPath[role] = {};
      r.units.forEach((u, i) => {
        const old = keyOf(role, i);
        if (!targets.has(old) || u.paths.length < 2) {
          const key = keyOf(role, units.length);remap.set(old, [key]);for (const p of u.paths) byPath[role][p] = key;units.push(u);return;
        }
        const [sx, sy] = scales(u), keys = [];
        for (const p of u.paths) {
          const s = r.sources[p], x0 = Math.round(u.x + (s[0] - u.src[0]) * sx), y0 = Math.round(u.y + (s[1] - u.src[1]) * sy);
          const x1 = Math.round(u.x + (s[2] - u.src[0]) * sx), y1 = Math.round(u.y + (s[3] - u.src[1]) * sy);
          const key = keyOf(role, units.length);keys.push(key);byPath[role][p] = key;
          units.push({paths: [p], src: s, x: x0, y: y0, w: s[2] - s[0] > EDGE ? x1 - x0 : 0, h: s[3] - s[1] > EDGE ? y1 - y0 : 0});
        }
        remap.set(old, keys);
      });
      r.units = units;
    }
    ctx.sel = new Set([...ctx.sel].flatMap(k => remap.get(k) || []));
    return byPath;
  }
  split() { this.splitUnits(new Set(this.ctx.sel));this.ctx.level = 'path';this.refresh(); }
  setLevel(level) { this.ctx.level = level;this.status(); }
  clearSelection() { this.ctx.sel.clear();this.status(); }
  toggleUnit(role, i, on) { const k = keyOf(role, i);if (on) this.ctx.sel.add(k); else this.ctx.sel.delete(k);this.status(); }
  selectRole(role) { this.ctx.roles[role].units.forEach((_u, i) => this.ctx.sel.add(keyOf(role, i)));this.status(); }
  // Ticking a child path of a connected element splits the element and selects that path.
  pickPath(role, i, p) { const key = this.splitUnits(new Set([keyOf(role, i)]))[role][p];this.ctx.sel.add(key);this.ctx.level = 'path';this.refresh(); }

  // A role's drawing's centerline box in its own coordinates, and its own canvas.
  roleSource(role) {
    const r = this.ctx.roles[role];if (!r) return null;
    const boxes = r.sources.filter(Boolean);
    return boxes.length ? boxes.reduce((a, b) => [Math.min(a[0], b[0]), Math.min(a[1], b[1]), Math.max(a[2], b[2]), Math.max(a[3], b[3])]) : null;
  }
  roleCanvas(role) { return (role === 'main' ? this.ctx.main.canvas : this.ctx.sub.canvas) || this.presets[role].base; }
  // A role's distinct keyshapes from the contract (names that share bounds are one keyshape;
  // the circle stays apart from the square). Order: square, circle, tall…, wide…
  shapes(role) {
    const ctx = this.ctx;ctx.shapes ??= {};if (ctx.shapes[role]) return ctx.shapes[role];
    const unique = new Map();
    for (const [name, b] of Object.entries(ctx.keyshapes?.[role] || {})) {
      const k = (name === 'CIRCLE' ? 'c:' : '') + b.join(',');if (!unique.has(k)) unique.set(k, {names: [], bounds: b});unique.get(k).names.push(name);
    }
    const list = [...unique.values()].map(s => ({...s, w: s.bounds[2] - s.bounds[0], h: s.bounds[3] - s.bounds[1], circle: s.names.includes('CIRCLE')}));
    const tall = list.filter(s => s.h > s.w).sort((a, b) => b.w - a.w), wide = list.filter(s => s.w > s.h).sort((a, b) => b.h - a.h);
    // Two sizes: "Tall" / "Tall small"; more: the contract's size suffix ("Tall XL" … "Tall S").
    const named = (kind, group) => group.map((s, i) => [`${kind.toLowerCase()}-${i}`, group.length <= 2 ? (i ? `${kind} small` : kind) : `${kind} ${s.names[0].split('_').pop()}`, s]);
    const order = [['square', 'Square', list.find(s => s.w === s.h && !s.circle)], ['circle', 'Circle', list.find(s => s.circle)]];
    for (let i = 0; i < Math.max(tall.length, wide.length); i++) order.push(...named('Tall', tall).slice(i, i + 1), ...named('Wide', wide).slice(i, i + 1));
    return ctx.shapes[role] = order.filter(([, , s]) => s).map(([id, label, s]) => ({id, label, ...s}));
  }
  ownShape(role) {
    const src = this.roleSource(role);if (!src || Math.abs(this.roleCanvas(role) - this.presets[role].base) > 1e-6) return null;
    return this.shapes(role).find(s => s.bounds.every((v, i) => Math.abs(v - src[i]) < .05))?.id || null;
  }
  // Centerline box of a role at a preset: its keyshape grows or shrinks by (size − base) on both axes and sits in its
  // corner (the main opposite the sub), as the automatic placement puts it at the base size. 'own' (a drawing on no
  // keyshape) scales evenly instead.
  presetBox(role, size, shapeId) {
    const ctx = this.ctx, [px, py] = ANCHORS[ctx.pair.position] || [1, 1], [ax, ay] = role === 'main' ? [1 - px, 1 - py] : [px, py];
    const c = ctx.canvas, shape = this.shapes(role).find(s => s.id === shapeId), base = this.presets[role].base;
    let w, h;
    if (shape) { w = shape.w + size - base;h = shape.h + size - base; }
    else { const src = this.roleSource(role);if (!src) return null;const k = size / this.roleCanvas(role);w = Math.round((src[2] - src[0]) * k);h = Math.round((src[3] - src[1]) * k); }
    if (w < 4 || h < 4 || w + 4 > c - 2 * PADDING || h + 4 > c - 2 * PADDING) return null;
    const x = Math.round(PADDING + (c - 2 * PADDING - w - 4) * ax) + 2, y = Math.round(PADDING + (c - 2 * PADDING - h - 4) * ay) + 2;
    return [x, y, x + w, y + h];
  }
  // Native text keeps its own size rules; keyshape presets are for drawn icons.
  hasPresets(role) { return !!this.ctx.roles[role] && !(role === 'sub' && this.ctx.pair.native_text); }
  // The preset (size + keyshape) a role is on right now, if any.
  currentPreset(role) {
    const r = this.ctx.roles[role];if (!r) return null;const box = unionOf(r.units), chosen = this.ctx.preset?.[role];
    const same = (a, b) => a && b && a.every((v, i) => Math.abs(v - b[i]) < 1e-6);
    // Boxes can coincide (circle at 44 = square at 48): what was chosen last wins, then the own keyshape.
    if (chosen?.size && chosen.shape && same(box, this.presetBox(role, chosen.size, chosen.shape))) return {...chosen};
    const own = this.ownShape(role), ids = [own || 'own', ...this.shapes(role).map(s => s.id)];
    for (const id of ids) for (const size of this.presets[role].sizes) if (same(box, this.presetBox(role, size, id))) return {size, shape: id};
    return null;
  }
  // The size and keyshape a role's preset rows show (the chosen ones, else the current, else the base on its own shape).
  presetState(role) {
    const now = this.currentPreset(role), state = this.ctx.preset[role] ??= {};
    if (now) Object.assign(state, now);
    state.size ??= this.presets[role].base;state.shape ??= this.ownShape(role) || 'own';
    return {state, now};
  }
  // Map every unit of a role from its current box onto the preset box (edges rounded to the grid).
  applyPreset(role, size, shapeId) {
    const r = this.ctx.roles[role], target = this.presetBox(role, size, shapeId);if (!r || !target) return;
    this.touch([role]);this.ctx.preset[role] = {size, shape: shapeId};
    const from = unionOf(r.units), fw = from[2] - from[0], fh = from[3] - from[1];
    const mapX = v => Math.round(fw > EDGE ? target[0] + (v - from[0]) * (target[2] - target[0]) / fw : target[0]);
    const mapY = v => Math.round(fh > EDGE ? target[1] + (v - from[1]) * (target[3] - target[1]) / fh : target[1]);
    for (const u of r.units) { const x0 = mapX(u.x), y0 = mapY(u.y), x1 = mapX(u.x + u.w), y1 = mapY(u.y + u.h);u.x = x0;u.y = y0;u.w = u.w > 0 ? Math.max(1, x1 - x0) : 0;u.h = u.h > 0 ? Math.max(1, y1 - y0) : 0; }
    this.ctx.sel = new Set(r.units.map((_u, i) => keyOf(role, i)));this.refresh();
  }
  // Free: the whole role selected, to drag its handles.
  free(role) { this.ctx.level = 'whole';this.ctx.sel = new Set(this.ctx.roles[role].units.map((_u, i) => keyOf(role, i)));this.status(); }

  // Scale the chosen units about a pinned point: fx / fy per axis (null leaves that axis alone).
  // Unit edges are rounded, so units that touched before still touch after.
  scale(list, before, fx, fy, pinX, pinY) {
    list.forEach((u, i) => {
      const b = before[i], sw = b.src[2] - b.src[0], sh = b.src[3] - b.src[1];
      if (fx != null) {
        const x0 = Math.round(pinX + (b.x - pinX) * fx), x1 = Math.round(pinX + (b.x + b.w - pinX) * fx);
        u.x = sw > EDGE ? Math.min(x0, x1 - 1) : Math.round(pinX + (b.x - pinX) * fx);u.w = sw > EDGE ? Math.max(1, x1 - u.x) : 0;
      }
      if (fy != null) {
        const y0 = Math.round(pinY + (b.y - pinY) * fy), y1 = Math.round(pinY + (b.y + b.h - pinY) * fy);
        u.y = sh > EDGE ? Math.min(y0, y1 - 1) : Math.round(pinY + (b.y - pinY) * fy);u.h = sh > EDGE ? Math.max(1, y1 - u.y) : 0;
      }
    });
  }
  // Pointer: pick, move the selection, or resize it from a corner or an edge with the opposite side pinned.
  // `hit`: {role, unit, path, handle, move, under: {role, unit, path} (artwork under the selection frame)}.
  press(hit, additive) {
    const ctx = this.ctx;
    let target = hit;
    // Artwork under the selection frame (the arrow inside a selected monitor) can still be picked.
    if (hit.move && hit.under) {
      const u = hit.under, k = keyOf(u.role, u.unit), unit = ctx.roles[u.role].units[u.unit];
      if (ctx.level === 'path') { if (additive || unit.paths.length > 1 || !ctx.sel.has(k)) target = u; }
      else if ((additive || !ctx.sel.has(k)) && (ctx.level === 'element' || !this.selectedRoles().has(u.role) || additive)) target = u;
    }
    if (!target.handle && !target.move) {
      if (target.role == null) { if (!additive) ctx.sel.clear();this.status();return null; }
      const role = target.role;let keys;
      if (ctx.level === 'path') {
        // A path of a connected element: split just that element, then pick the path.
        const unit = ctx.roles[role].units[target.unit], p = target.path ?? unit.paths[0];
        keys = [unit.paths.length > 1 ? this.splitUnits(new Set([keyOf(role, target.unit)]))[role][p] : keyOf(role, target.unit)];
      } else keys = ctx.level === 'element' ? [keyOf(role, target.unit)] : ctx.roles[role].units.map((_u, i) => keyOf(role, i));
      if (additive) { const on = keys.every(k => ctx.sel.has(k));for (const k of keys) on ? ctx.sel.delete(k) : ctx.sel.add(k);this.status();return null; }
      if (!keys.every(k => ctx.sel.has(k)) || keys.length !== ctx.sel.size) ctx.sel = new Set(keys);
    }
    if (!ctx.sel.size) return null;
    this.touch(this.selectedRoles());
    const list = this.selected(), before = list.map(u => ({...u})), box = unionOf(list);
    this.status();
    return {list, before, box, corner: target.handle || null, moved: false};
  }
  // A drag step to canvas point (px, py) from `start`; `shift` keeps proportions while resizing.
  drag(d, start, [px, py], shift) {
    d.moved = true;
    if (!d.corner) {
      const dx = Math.round(px - start[0]), dy = Math.round(py - start[1]);
      d.list.forEach((u, i) => { u.x = d.before[i].x + dx;u.y = d.before[i].y + dy; });
    } else {
      const box = d.box, corner = d.corner, w = box[2] - box[0], h = box[3] - box[1];
      const pinX = corner.includes('w') ? box[2] : box[0], pinY = corner.includes('n') ? box[3] : box[1];
      // The dragged edge lands on a grid line (the painted edge is the centerline edge ±2).
      const edgeX = corner.includes('w') ? Math.round(px + 2) : Math.round(px - 2), edgeY = corner.includes('n') ? Math.round(py + 2) : Math.round(py - 2);
      let fx = /[ew]/.test(corner) && w > EDGE ? Math.max(1, Math.abs(edgeX - pinX)) / w : null, fy = /[ns]/.test(corner) && h > EDGE ? Math.max(1, Math.abs(edgeY - pinY)) / h : null;
      if (shift) { const f = Math.max(fx ?? 0, fy ?? 0) || 1;fx = w > EDGE ? f : null;fy = h > EDGE ? f : null; }
      this.scale(d.list, d.before, fx, fy, pinX, pinY);
    }
    this.touchView();
  }
  release(d) { if (d?.moved) this.refresh(); }
  key(e) {
    const ctx = this.ctx;if (!ctx?.sel.size) return false;
    const list = this.selected(), steps = {ArrowLeft: [-1, 0], ArrowRight: [1, 0], ArrowUp: [0, -1], ArrowDown: [0, 1]}, box = unionOf(list), w = box[2] - box[0], h = box[3] - box[1];
    const resize = (dw, dh) => {
      this.touch(this.selectedRoles());const before = list.map(u => ({...u}));
      this.scale(list, before, dw && w > EDGE && w + dw >= 1 ? (w + dw) / w : null, dh && h > EDGE && h + dh >= 1 ? (h + dh) / h : null, box[0], box[1]);this.refresh();
    };
    if (steps[e.key] && e.altKey) resize(steps[e.key][0], steps[e.key][1]);
    else if (steps[e.key]) { this.touch(this.selectedRoles());const n = e.shiftKey ? 8 : 1;for (const u of list) { u.x += steps[e.key][0] * n;u.y += steps[e.key][1] * n; }this.refresh(); }
    else if (['+', '='].includes(e.key)) resize(1, 1);
    else if (['-', '_'].includes(e.key)) resize(-1, -1);
    else if (e.key === 'Escape') { ctx.sel.clear();this.status(); }
    else return false;
    return true;
  }

  // Edits do not combine by themselves: the result shown is marked out of date until Apply layout combines this layout.
  refresh() { this.ctx.token++;this.ctx.stale = true;this.status(); }
  async applyLayout() {
    const ctx = this.ctx;
    if (this.anyOutside()) { this.error = 'Move the artwork back inside the canvas first.';this.touchView();return; }
    const token = ++ctx.token, body = {id: ctx.pair.id}, l = this.layout();if (l) body.layout = l;
    ctx.combining = true;this.error = '';this.status();
    let done = false;
    try { const data = await this.combine(body);if (token === ctx.token) { ctx.stale = false;ctx.result = data;done = true; } }
    catch (e) { if (token === ctx.token) this.error = e.message; }
    finally { ctx.combining = false;this.status();if (done) this.readout = {text: 'Combined with this layout. Click Save layout to keep it.', bad: false}; }
  }
  // Composed in this browser with the layout (null: automatic) and stored as the pair's combined icon.
  async post(body) {
    const ctx = this.ctx;ctx.busy = true;this.error = '';this.status();
    try {
      const composed = await window.SideData.compose(body.pair_id, {layout: body.layout});
      const [built] = await window.SideData.build([composed.request]);
      if (!built?.ok) throw Error(built?.error || 'Could not save the layout.');
      const data = {layout: {layout: body.layout}, result: {...composed.result, svg: composed.svg}};
      ctx.onSaved?.(data);return data;
    } finally { ctx.busy = false;this.status(); }
  }
  async save() {
    const l = this.layout();if (!l) return;
    try { const data = await this.post({pair_id: this.ctx.pair.id, layout: l});this.ctx.saved = data.layout.layout;this.ctx.stale = false;this.ctx.result = data.result;this.readout = {text: 'Layout saved.', bad: false}; }
    catch (e) { this.error = e.message; }
    this.touchView();
  }
  async reset() {
    try { await this.post({pair_id: this.ctx.pair.id, layout: null});await this.load(this.ctx.pair, this.ctx.main, this.ctx.sub, this.ctx.onSaved, null); }
    catch (e) { this.error = e.message;this.touchView(); }
  }
  discard() { const c = this.ctx;return this.load(c.pair, c.main, c.sub, c.onSaved, c.saved); }

  // This pair with layout `l` and each target with `l` moved onto it (CombineSide.transfer: same side copies, another
  // side re-anchors each part, a different sub fits its own groups to the edited sub's box), composed in this browser
  // and stored together → {source: {layout: {layout}, result}, results: [{pair_id, ok, error?}]}.
  async applyHere(l, targets) {
    const data = window.SideData, ctx = this.ctx;
    const source = await data.compose(ctx.pair.id, {layout: l}), requests = [source.request], outcome = [];
    const sourceSub = data.part(data.item(ctx.pair.id), 'sub');
    for (const target of targets) {
      try {
        const sub = data.part(data.item(target.pair_id), 'sub');
        const auto = await data.compose(target.pair_id, {layout: null});
        const moved = window.CombineSide.transfer(l, ctx.pair.position, sourceSub.icon, sub.position, sub.icon, auto.result.canvas,
                                                  sub.icon !== sourceSub.icon ? data.elements(auto, 'sub', null).groups : null);
        const composed = await data.compose(target.pair_id, {layout: moved});
        requests.push(composed.request);outcome.push({pair_id: target.pair_id, index: requests.length - 1});
      } catch (e) { outcome.push({pair_id: target.pair_id, ok: false, error: e.message}); }
    }
    const built = await data.build(requests);
    if (!built[0]?.ok) throw Error(built[0]?.error || 'Could not save the layout.');
    const results = outcome.map(o => o.index === undefined ? o : built[o.index]?.ok ? {pair_id: o.pair_id, ok: true} : {pair_id: o.pair_id, ok: false, error: built[o.index]?.error || 'Not saved.'});
    return {source: {layout: {layout: l}, result: {...source.result, svg: source.svg}}, results};
  }
  async applyToTargets() {
    const ctx = this.ctx, l = this.layout(), pairs = this.pairsWithMain(ctx.main.icon, ctx.pair.id);if (!l) return;
    const targets = pairs.filter(p => ctx.targets.has(p.id)).map(p => ({pair_id: p.id, sub: p.sub}));
    ctx.busy = true;this.error = '';this.status();this.readout = {text: `Applying to ${targets.length} pairs…`, bad: false};
    let message = '';
    try {
      const data = await this.applyHere(l, targets);
      ctx.onSaved?.(data.source);ctx.saved = data.source.layout.layout;ctx.stale = false;ctx.result = data.source.result;
      ctx.applyResults = Object.fromEntries(data.results.map(x => [x.pair_id, x]));await this.applied(data.results);
      const ok = data.results.filter(x => x.ok).length;
      message = `Saved. Applied to ${ok} of ${data.results.length} pairs${ok < data.results.length ? ' — see the list for the ones that could not take it' : ''}.`;
    } catch (e) { this.error = e.message; }
    finally { ctx.busy = false;this.status();if (message) this.readout = {text: message, bad: false}; }
  }

  // The readout line: the selection's painted size and place, or what to do; red when outside the canvas.
  status() {
    const ctx = this.ctx;
    if (ctx?.loaded) {
      const bad = this.anyOutside(), list = this.selected();
      if (!list.length) this.readout = {text: bad ? 'Part of the artwork is outside the canvas.' : 'Select the main, the sub or some elements to adjust them.', bad};
      else {
        const b = unionOf(list), what = list.length === 1 ? '1 element' : `${list.length} elements`;
        this.readout = {text: `${what}: painted ${fmt(b[2] - b[0] + 4)}×${fmt(b[3] - b[1] + 4)} at (${fmt(b[0] - 2)}, ${fmt(b[1] - 2)})` + (bad ? ' · outside the canvas' : ''), bad};
      }
    }
    this.touchView();
  }
}
