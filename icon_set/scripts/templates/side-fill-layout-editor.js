(() => {
  // The side-pair layout editor, ported from the pictographic side-pairs page (web/side-pairs/src/lib/editor.svelte.js
  // and components/LayoutEditorDialog.svelte): move and resize the main, the sub, or any chosen set of their elements,
  // snapped to the grid. Boxes are centerline units (the painted box is ±2, stroke 4). Width and height are
  // independent; Shift keeps the proportions. A unit is what moves as one piece: a connected element by default, or a
  // single path once split. Edits do not combine by themselves: Apply layout renders this layout (backend.preview,
  // side-fill-layout.js in the browser), and Save layout hands it to the page (backend.save: the pick it was opened
  // from takes these boxes). The source keyshape stays locked; every layout is sent as explicit element boxes.
  // open(row, candidate, host, backend): backend = {keyshapes(), elements(), preview(proposal), save(proposal, result)}.
  const NS = 'http://www.w3.org/2000/svg';
  const STROKE = 4, EDGE = 1e-9, CANVAS = 64, PAD = 4;
  const ROLES = ['main', 'sub'];
  const range = (from, to) => Array.from({length: (to - from) / 4 + 1}, (_v, i) => from + 4 * i);
  // pair_layout_review.keyshape_preset_box: main 32–64 (48 automatic), sub 12–44 (32 automatic).
  const PRESETS = {main: {base: 48, sizes: range(32, 64), label: 'Main'}, sub: {base: 32, sizes: range(12, 44), label: 'Sub'}};
  const ANCHORS = {br: [1, 1], bl: [0, 1], tr: [1, 0], tl: [0, 0], ri: [1, .5], le: [0, .5], bo: [.5, 1], to: [.5, 0]};
  const fmt = n => String(Math.round(n * 100) / 100);
  // Python's round (half to even), so preset boxes land where the server's validation puts them.
  const pyRound = v => { const r = Math.round(v);return Math.abs(v % 1) === .5 && r % 2 ? r - 1 : r; };
  const scales = u => {
    const sw = u.src[2] - u.src[0], sh = u.src[3] - u.src[1];
    const sx = sw > EDGE ? u.w / sw : null, sy = sh > EDGE ? u.h / sh : null;
    return [sx ?? sy ?? 1, sy ?? sx ?? 1];
  };
  const boxOf = u => [u.x, u.y, u.x + u.w, u.y + u.h];
  const union = boxes => boxes.reduce((a, b) => [Math.min(a[0], b[0]), Math.min(a[1], b[1]), Math.max(a[2], b[2]), Math.max(a[3], b[3])]);
  const unionOf = list => union(list.map(boxOf));
  const keyOf = (role, i) => role + ':' + i;
  const same = (a, b) => a && b && a.every((v, i) => Math.abs(v - b[i]) < 1e-6);
  const plain = units => units.map(({paths, x, y, w, h}) => ({paths: [...paths], x, y, w, h}));
  const srcOf = (r, paths) => union(paths.map(p => r.sources[p]).filter(Boolean));
  const withSrc = (r, units) => units.map(u => ({...plain([u])[0], src: srcOf(r, u.paths)}));
  const svgUrl = svg => svg ? `data:image/svg+xml;charset=utf-8,${encodeURIComponent(svg)}` : '';
  const node = (name, attrs = {}) => {
    const element = document.createElementNS(NS, name);
    for (const [key, value] of Object.entries(attrs)) if (value != null) element.setAttribute(key, String(value));
    return element;
  };
  const html = (tag, attrs = {}, ...children) => {
    const element = document.createElement(tag);
    for (const [key, value] of Object.entries(attrs)) {
      if (value == null || value === false) continue;
      if (key.startsWith('on')) element.addEventListener(key.slice(2), value);
      else if (key === 'class') element.className = value;
      else element.setAttribute(key, value === true ? '' : String(value));
    }
    element.append(...children.filter(child => child != null));
    return element;
  };

  const $ = id => document.getElementById(id);
  const dialog = $('layout-editor'), canvas = $('layout-canvas'), presetBar = $('layout-presets'), list = $('layout-element-list');
  const readout = $('layout-readout'), status = $('layout-status'), staleNote = $('layout-stale');
  const preview = $('layout-preview'), stress = $('layout-stress');
  const applyButton = $('layout-apply'), saveButton = $('layout-save'), forceBox = $('layout-force');
  const candidateFields = ['layout-base', 'layout-sub-variant', 'layout-position', 'layout-name', 'layout-reason'];
  let ctx = null, keyshapes = {}, centerline = true;
  try { centerline = localStorage.getItem('side-layout-centerline') !== 'off'; } catch { /* no storage */ }

  const setStatus = (text, bad = false) => { status.textContent = text;status.classList.toggle('risk', bad); };

  // ---- keyshapes and presets ----
  const roleSource = role => { const r = ctx.roles[role];return srcOf(r, r.sources.map((_b, i) => i)); };
  // pair_layout_review.source_keyshape_name: the drawing's own keyshape (SQUARE first), else 'own'.
  function lockedShape(role) {
    const src = roleSource(role), table = keyshapes[role] || {};
    const names = Object.keys(table).sort((a, b) => (a !== 'SQUARE') - (b !== 'SQUARE'));
    return names.find(name => table[name].every((v, i) => Math.abs(v - src[i]) < .05)) || 'own';
  }
  // Centerline box of a role at a preset size: its keyshape grows or shrinks by (size − base) on both axes and sits in
  // its corner, the main opposite the sub ('own': the drawing scaled evenly). Mirrors keyshape_preset_box.
  function presetBox(role, size, shape = ctx.locked[role]) {
    const {base} = PRESETS[role];
    let w, h;
    if (shape === 'own') { const s = roleSource(role), k = size / base;w = pyRound((s[2] - s[0]) * k);h = pyRound((s[3] - s[1]) * k); }
    else { const b = keyshapes[role]?.[shape];if (!b) return null;w = b[2] - b[0] + size - base;h = b[3] - b[1] + size - base; }
    const inner = CANVAS - 2 * PAD;
    if (w < 4 || h < 4 || w + 4 > inner || h + 4 > inner) return null;
    const [px, py] = ANCHORS[ctx.position] || [1, 1], [ax, ay] = role === 'main' ? [1 - px, 1 - py] : [px, py];
    const x = pyRound(PAD + (inner - w - 4) * ax) + 2, y = pyRound(PAD + (inner - h - 4) * ay) + 2;
    return [x, y, x + w, y + h];
  }
  // Distinct keyshapes of a role (names sharing bounds are one; the circle stays apart): square, circle, tall, wide.
  function shapes(role) {
    const unique = new Map();
    for (const [name, b] of Object.entries(keyshapes[role] || {})) {
      const k = (name === 'CIRCLE' ? 'c:' : '') + b.join(',');
      if (!unique.has(k)) unique.set(k, []);
      unique.get(k).push(name);
    }
    const locked = ctx.locked[role];
    const out = [...unique.values()].map(names => {
      const b = keyshapes[role][names[0]], w = b[2] - b[0], h = b[3] - b[1], circle = names.includes('CIRCLE');
      const kind = circle ? 'Circle' : w === h ? 'Square' : h > w ? 'Tall' : 'Wide';
      const suffix = kind === 'Tall' || kind === 'Wide' ? ' ' + names.map(n => n.split('_').pop()).join('/') : '';
      return {id: names.includes(locked) ? locked : names[0], names, label: kind + suffix, circle,
              rank: [kind === 'Square' ? 0 : kind === 'Circle' ? 1 : kind === 'Tall' ? 2 : 3, -Math.min(w, h)]};
    }).sort((a, b) => a.rank[0] - b.rank[0] || a.rank[1] - b.rank[1]);
    return locked === 'own' ? [{id: 'own', names: [], label: 'Own shape', circle: false}, ...out] : out;
  }
  // The preset size a role sits on right now, if any.
  function currentPreset(role) {
    const box = unionOf(ctx.roles[role].units);
    return PRESETS[role].sizes.find(size => same(box, presetBox(role, size))) ?? null;
  }
  // The keyshape limit the server checks a role against: its preset, else the smallest preset holding it.
  function guideSize(role) {
    const now = currentPreset(role);if (now != null) return now;
    const box = unionOf(ctx.roles[role].units), sizes = PRESETS[role].sizes.filter(size => presetBox(role, size));
    return sizes.find(size => { const b = presetBox(role, size);return b[0] <= box[0] + .05 && b[1] <= box[1] + .05 && b[2] >= box[2] - .05 && b[3] >= box[3] - .05; })
      ?? sizes[sizes.length - 1] ?? PRESETS[role].base;
  }
  // Map every unit of a role from its current box onto the preset box (edges rounded to the grid).
  function applyPreset(role, size) {
    const r = ctx.roles[role], target = presetBox(role, size);if (!target) return;
    const from = unionOf(r.units), fw = from[2] - from[0], fh = from[3] - from[1];
    const mapX = v => Math.round(fw > EDGE ? target[0] + (v - from[0]) * (target[2] - target[0]) / fw : target[0]);
    const mapY = v => Math.round(fh > EDGE ? target[1] + (v - from[1]) * (target[3] - target[1]) / fh : target[1]);
    for (const u of r.units) {
      const x0 = mapX(u.x), y0 = mapY(u.y), x1 = mapX(u.x + u.w), y1 = mapY(u.y + u.h);
      u.x = x0;u.y = y0;u.w = u.w > 0 ? Math.max(1, x1 - x0) : 0;u.h = u.h > 0 ? Math.max(1, y1 - y0) : 0;
    }
    ctx.sel = new Set(r.units.map((_u, i) => keyOf(role, i)));
    refresh();
  }
  // Free: the whole role selected, to drag its handles.
  function free(role) { ctx.level = 'whole';ctx.sel = new Set(ctx.roles[role].units.map((_u, i) => keyOf(role, i)));render(); }

  // ---- selection ----
  const selected = () => [...ctx.sel].map(k => { const [role, i] = k.split(':');return ctx.roles[role]?.units[Number(i)]; }).filter(Boolean);
  const selectedRoles = () => new Set([...ctx.sel].map(k => k.split(':')[0]));
  const outside = b => b[0] - 2 < -1e-6 || b[1] - 2 < -1e-6 || b[2] + 2 > CANVAS + 1e-6 || b[3] + 2 > CANVAS + 1e-6;
  const anyOutside = () => Object.values(ctx.roles).some(r => r.units.some(u => outside(boxOf(u))));
  // Split units (keys) into one unit per path, each keeping exactly where it is drawn now.
  // The selection follows; returns {role: {path: key}} for every path of every unit.
  function splitUnits(targets) {
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
  const split = () => { splitUnits(new Set(ctx.sel));ctx.level = 'path';refresh(); };
  // Ticking a child path of a connected element splits the element and selects that path.
  const pickPath = (role, i, p) => { const key = splitUnits(new Set([keyOf(role, i)]))[role][p];ctx.sel.add(key);ctx.level = 'path';refresh(); };

  // Scale the chosen units about a pinned point: fx / fy per axis (null leaves that axis alone).
  // Unit edges are rounded, so units that touched before still touch after.
  function scale(units, before, fx, fy, pinX, pinY) {
    units.forEach((u, i) => {
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
  function press(hit, additive) {
    let target = hit;
    // Artwork under the selection frame (the arrow inside a selected monitor) can still be picked.
    if (hit.move && hit.under) {
      const u = hit.under, k = keyOf(u.role, u.unit), unit = ctx.roles[u.role].units[u.unit];
      if (ctx.level === 'path') { if (additive || unit.paths.length > 1 || !ctx.sel.has(k)) target = u; }
      else if ((additive || !ctx.sel.has(k)) && (ctx.level === 'element' || !selectedRoles().has(u.role) || additive)) target = u;
    }
    if (!target.handle && !target.move) {
      if (target.role == null) { if (!additive) ctx.sel.clear();render();return null; }
      const role = target.role;let keys;
      if (ctx.level === 'path') {
        // A path of a connected element: split just that element, then pick the path.
        const unit = ctx.roles[role].units[target.unit], p = target.path ?? unit.paths[0];
        keys = [unit.paths.length > 1 ? splitUnits(new Set([keyOf(role, target.unit)]))[role][p] : keyOf(role, target.unit)];
      } else keys = ctx.level === 'element' ? [keyOf(role, target.unit)] : ctx.roles[role].units.map((_u, i) => keyOf(role, i));
      if (additive) { const on = keys.every(k => ctx.sel.has(k));for (const k of keys) on ? ctx.sel.delete(k) : ctx.sel.add(k);render();return null; }
      if (!keys.every(k => ctx.sel.has(k)) || keys.length !== ctx.sel.size) ctx.sel = new Set(keys);
    }
    if (!ctx.sel.size) return null;
    const units = selected(), before = units.map(u => ({...u}));
    render();
    return {units, before, box: unionOf(units), corner: target.handle || null, moved: false};
  }
  // A drag step to canvas point (px, py) from `start`; `shift` keeps proportions while resizing.
  function drag(d, start, [px, py], shift) {
    d.moved = true;
    if (!d.corner) {
      const dx = Math.round(px - start[0]), dy = Math.round(py - start[1]);
      d.units.forEach((u, i) => { u.x = d.before[i].x + dx;u.y = d.before[i].y + dy; });
    } else {
      const box = d.box, corner = d.corner, w = box[2] - box[0], h = box[3] - box[1];
      const pinX = corner.includes('w') ? box[2] : box[0], pinY = corner.includes('n') ? box[3] : box[1];
      // The dragged edge lands on a grid line (the painted edge is the centerline edge ±2).
      const edgeX = corner.includes('w') ? Math.round(px + 2) : Math.round(px - 2), edgeY = corner.includes('n') ? Math.round(py + 2) : Math.round(py - 2);
      let fx = /[ew]/.test(corner) && w > EDGE ? Math.max(1, Math.abs(edgeX - pinX)) / w : null;
      let fy = /[ns]/.test(corner) && h > EDGE ? Math.max(1, Math.abs(edgeY - pinY)) / h : null;
      if (shift) { const f = Math.max(fx ?? 0, fy ?? 0) || 1;fx = w > EDGE ? f : null;fy = h > EDGE ? f : null; }
      scale(d.units, d.before, fx, fy, pinX, pinY);
    }
    render({dragging: true});
  }
  function key(e) {
    if (!ctx?.loaded || !ctx.sel.size) return false;
    const units = selected(), steps = {ArrowLeft: [-1, 0], ArrowRight: [1, 0], ArrowUp: [0, -1], ArrowDown: [0, 1]};
    const box = unionOf(units), w = box[2] - box[0], h = box[3] - box[1];
    const resize = (dw, dh) => {
      const before = units.map(u => ({...u}));
      scale(units, before, dw && w > EDGE && w + dw >= 1 ? (w + dw) / w : null, dh && h > EDGE && h + dh >= 1 ? (h + dh) / h : null, box[0], box[1]);refresh();
    };
    if (steps[e.key] && e.altKey) resize(steps[e.key][0], steps[e.key][1]);
    else if (steps[e.key]) { const n = e.shiftKey ? 8 : 1;for (const u of units) { u.x += steps[e.key][0] * n;u.y += steps[e.key][1] * n; }refresh(); }
    else if (['+', '='].includes(e.key)) resize(1, 1);
    else if (['-', '_'].includes(e.key)) resize(-1, -1);
    else if (e.key === 'Escape') { ctx.sel.clear();render(); }
    else return false;
    return true;
  }

  // ---- composing and saving ----
  const part = role => { const size = guideSize(role);return {mode: 'preset', shape: ctx.locked[role], size, guide_size: size, dx: 0, dy: 0, units: plain(ctx.roles[role].units)}; };
  const proposal = (parts = {main: part('main'), sub: part('sub')}) => ({
    id: $('layout-name').value.trim(), base_variant: $('layout-base').value, sub_variant: $('layout-sub-variant').value,
    position: ctx.position, ...parts, reason: $('layout-reason').value.trim(),
  });
  // Edits do not combine by themselves: the result shown is marked out of date until Apply layout.
  function refresh() { ctx.token++;ctx.stale = true;render(); }
  function drawGuides(checks = {}) {
    for (const overlay of dialog.querySelectorAll('.layout-guides')) {
      overlay.replaceChildren();
      for (const role of ROLES) {
        const check = checks[role], b = check?.guide_painted_box;if (!b) continue;
        const valid = check.fits_keyshape && check.stroke_envelope_inside_canvas;
        const attrs = {class: 'guide ' + (valid ? role : 'bad'), fill: 'none'};
        overlay.append(check.guide_kind === 'circle'
          ? node('circle', {...attrs, cx: (b[0] + b[2]) / 2, cy: (b[1] + b[3]) / 2, r: (b[2] - b[0]) / 2})
          : node('rect', {...attrs, x: b[0], y: b[1], width: b[2] - b[0], height: b[3] - b[1], rx: 1}));
      }
    }
  }
  function clearResult() {
    preview.removeAttribute('src');stress.removeAttribute('src');drawGuides();
    dialog.querySelectorAll('[data-layout-size]').forEach(image => image.removeAttribute('src'));
  }
  function showResult(result) {
    preview.src = svgUrl(result.svg);
    stress.src = svgUrl(result.stress_svg || result.svg);
    $('layout-stress-label').textContent = result.stress_svg ? 'Actual 8px cut · inspect white details' : 'Outline main · 4px result';
    dialog.querySelectorAll('[data-layout-size]').forEach(image => { image.src = svgUrl(result.svg.replace(/currentColor/g, '#000000')); });
    const c = result.candidate, checks = c.keyshape_validation || {};
    drawGuides(checks);
    const damaged = (c.white_border_loss_at_8px || []).filter(item => item.lost_black_border_px2 > .05);
    const invalid = ROLES.filter(role => !checks[role]?.fits_keyshape || !checks[role]?.stroke_envelope_inside_canvas);
    const issues = invalid.map(role => {
      const check = checks[role], problems = [];
      if (check?.keyshape_overflow_px > .05) problems.push(`${check.keyshape_overflow_px}px beyond its ${check.guide_size}px keyshape`);
      if (check?.ink_outside_guide_px2 > .5) problems.push(`${check.ink_outside_guide_px2} px² of ink outside its guide`);
      if (check?.stroke_envelope_inside_canvas === false) problems.push('outside the 64px canvas');
      return `${PRESETS[role].label}: ${problems.join(', ') || 'does not fit its keyshape'}`;
    });
    ctx.valid = !invalid.length;
    // Only keyshape problems (still inside the canvas): a manual edit may be forced past them.
    ctx.forceable = !ctx.valid && ROLES.every(role => checks[role]?.stroke_envelope_inside_canvas);
    setStatus(`Main ${checks.main?.preset || 'own'} · guide ${checks.main?.guide_size ?? '—'}px. Sub ${checks.sub?.preset || 'own'} · guide ${checks.sub?.guide_size ?? '—'}px. `
      + (issues.length ? `${issues.join('; ')}. ${ctx.forceable ? 'Save is disabled until both fit (make the part smaller or move it into its keyshape), or tick Force to save this manual edit anyway. ' : 'Save is disabled until both are inside the 64px canvas. '}`
                       : 'Both painted icons fit their anchored keyshapes and the 64px canvas. ')
      + `4px gap ${c.render_gap_px.toFixed(2)}px · 8px border loss ${damaged.length ? damaged.map(x => `${x.region}: ${x.lost_black_border_px2}`).join(', ') : '0'} px².`,
      damaged.length > 0 || invalid.length > 0);
  }
  // Render `body` (a proposal) with the gallery's renderer. `adopt` takes the rendered boxes as the editor's units.
  async function compose(body, adopt = false) {
    const opening = ctx, token = ++ctx.token;
    ctx.combining = true;render();
    try {
      // A frame first, so the "combining" state paints before the work.
      await new Promise(resolve => setTimeout(resolve, 0));
      const result = await ctx.backend.preview(body);
      if (ctx !== opening) return false;
      if (adopt) for (const role of ROLES) ctx.roles[role].units = withSrc(ctx.roles[role], result.candidate.layout_boxes[role]);
      if (token !== ctx.token && !adopt) return false;
      ctx.result = result;ctx.composed = body;ctx.stale = false;
      showResult(result);
      return true;
    } catch (error) {
      if (ctx === opening && token === ctx.token) { ctx.result = null;ctx.valid = false;clearResult();setStatus(error.message, true); }
      throw error;
    } finally { if (ctx === opening) { ctx.combining = false;render(); } }
  }
  async function applyLayout() {
    if (anyOutside()) { setStatus('Move the artwork back inside the canvas first.', true);return; }
    try {
      if (await compose(proposal())) readout.textContent = ctx.valid ? 'Combined with this layout. Click Save layout to keep it as a review candidate.'
        : ctx.forceable ? 'Combined with this layout. It goes past its keyshape: tick Force to save it as a manual edit.'
        : 'Combined with this layout, but it cannot be saved: see the problem below.';
    }
    catch { /* shown in the status line */ }
  }
  const canSave = () => ctx.valid || (ctx.forceable && forceBox.checked);
  async function save() {
    if (!ctx?.result || ctx.stale || !canSave()) return;
    ctx.busy = true;render();
    try {
      const row = ctx.row;
      const result = await ctx.backend.save({...ctx.composed, keyshape_override: !ctx.valid}, ctx.result);
      // The pair now uses this layout; update its card in place (the gallery file rebuilds in the background).
      ctx.busy = false;
      dialog.close();
      window.SideFillPair?.layoutSaved(row, result);
    } catch (error) { setStatus(error.message, true);ctx.busy = false;render(); }
  }
  // Back to the production placement (automatic), or to what the editor opened with.
  function restore(units, position) {
    ctx.position = position;$('layout-position').value = position;
    for (const role of ROLES) ctx.roles[role].units = withSrc(ctx.roles[role], units[role]);
    ctx.sel.clear();refresh();
  }
  // Another pair side re-anchors each part: it keeps its size and edits, moved with its keyshape to its own corner.
  function changePosition(position) {
    const sizes = Object.fromEntries(ROLES.map(role => [role, guideSize(role)]));
    const before = Object.fromEntries(ROLES.map(role => [role, presetBox(role, sizes[role])]));
    ctx.position = position;
    for (const role of ROLES) {
      const old = before[role], next = presetBox(role, sizes[role]);if (!old || !next) continue;
      for (const u of ctx.roles[role].units) { u.x += next[0] - old[0];u.y += next[1] - old[1]; }
    }
    refresh();
  }

  // ---- view ----
  function render({dragging = false} = {}) {
    if (!ctx) return;
    drawCanvas();
    if (!dragging) { drawPresets();drawList(); }
    staleNote.hidden = !(ctx.loaded && ctx.stale && !ctx.combining);
    staleNote.textContent = ctx.loaded && anyOutside() ? 'Move the artwork back inside the canvas, then Apply layout.'
      : 'Layout changed. Click Apply layout to see the combined result.';
    preview.closest('.side-layout-results').classList.toggle('is-stale', !!(ctx.stale && ctx.result));
    for (const button of dialog.querySelectorAll('[data-select-level]')) {
      button.setAttribute('aria-pressed', String(ctx.level === button.dataset.selectLevel));button.disabled = !ctx.loaded;
    }
    const bad = ctx.loaded && anyOutside();
    applyButton.disabled = !ctx.loaded || ctx.busy || ctx.combining || bad;
    applyButton.textContent = ctx.combining ? 'Combining…' : 'Apply layout';
    applyButton.classList.toggle('side-layout-stale-button', ctx.stale && !ctx.combining);
    saveButton.disabled = !ctx.loaded || ctx.busy || ctx.combining || ctx.stale || !ctx.result || !canSave() || bad;
    forceBox.disabled = !ctx.loaded || ctx.busy || ctx.combining || ctx.stale || !ctx.result || !ctx.forceable;
    forceBox.closest('label').classList.toggle('is-forcing', !!(ctx.forceable && forceBox.checked && !ctx.stale));
    $('layout-reset').disabled = $('layout-discard').disabled = !ctx.loaded || ctx.busy;
    $('layout-split').disabled = !ctx.loaded || !selected().some(u => u.paths.length > 1);
    $('layout-clear-selection').disabled = !ctx.loaded || !ctx.sel.size;
    if (!ctx.loaded) return;
    const units = selected();
    if (!units.length) readout.textContent = bad ? 'Part of the artwork is outside the canvas.' : 'Select the main, the sub or some elements to adjust them.';
    else {
      const b = unionOf(units), what = units.length === 1 ? '1 element' : `${units.length} elements`;
      readout.textContent = `${what}: painted ${fmt(b[2] - b[0] + 4)}×${fmt(b[3] - b[1] + 4)} at (${fmt(b[0] - 2)}, ${fmt(b[1] - 2)})` + (bad ? ' · outside the canvas' : '');
    }
    readout.classList.toggle('bad', bad);
  }
  function unitArt(r, u, px, trace) {
    const [sx, sy] = scales(u);
    const group = node('g', {transform: `matrix(${sx} 0 0 ${sy} ${u.x - u.src[0] * sx} ${u.y - u.src[1] * sy})`});
    const parsed = new DOMParser().parseFromString(`<svg xmlns="${NS}">${u.paths.map(p => r.markup[p]).join('')}</svg>`, 'image/svg+xml').documentElement;
    [...parsed.children].forEach((child, n) => {
      const e = document.importNode(child, true);
      e.setAttribute('data-path', u.paths[n]);e.setAttribute('vector-effect', 'non-scaling-stroke');
      if (trace) { e.setAttribute('stroke', '#ef4444');e.setAttribute('stroke-width', 1.3);e.setAttribute('fill', 'none'); }
      else e.setAttribute('stroke-width', STROKE * px);
      group.append(e);
    });
    return group;
  }
  function drawCanvas() {
    canvas.replaceChildren();
    canvas.toggleAttribute('data-centerline', centerline);
    if (!ctx.loaded) return;
    const px = canvas.getBoundingClientRect().width / (CANVAS + 2) || 6;
    const grid = node('g', {'pointer-events': 'none'});
    for (let i = 0; i <= CANVAS; i++) {
      const attrs = {stroke: i % 8 === 0 ? '#9eb3bd' : '#dae4e9', 'stroke-width': i % 8 === 0 ? .13 : .055};
      grid.append(node('line', {x1: i, y1: 0, x2: i, y2: CANVAS, ...attrs}), node('line', {x1: 0, y1: i, x2: CANVAS, y2: i, ...attrs}));
    }
    canvas.append(grid);
    // Dashed outline of each role's keyshape at the size the server checks it against (red when it does not fit).
    for (const role of ROLES) {
      const b = presetBox(role, guideSize(role));if (!b) continue;
      const u = unionOf(ctx.roles[role].units), fits = b[0] <= u[0] + .05 && b[1] <= u[1] + .05 && b[2] >= u[2] - .05 && b[3] >= u[3] - .05;
      const p = [b[0] - 2, b[1] - 2, b[2] + 2, b[3] + 2], attrs = {class: 'guide ' + (fits ? role : 'bad'), fill: 'none'};
      canvas.append(ctx.locked[role] === 'CIRCLE'
        ? node('circle', {...attrs, cx: (p[0] + p[2]) / 2, cy: (p[1] + p[3]) / 2, r: (p[2] - p[0]) / 2})
        : node('rect', {...attrs, x: p[0], y: p[1], width: p[2] - p[0], height: p[3] - p[1], rx: 1}));
    }
    for (const role of ROLES) {
      const r = ctx.roles[role], layer = node('g', {fill: 'none', stroke: 'currentColor', 'stroke-linecap': 'round', 'stroke-linejoin': 'round'});
      r.units.forEach((u, i) => {
        const art = unitArt(r, u, px, false);
        art.setAttribute('class', 'layout-art' + (ctx.sel.has(keyOf(role, i)) ? ' picked' : ''));art.dataset.role = role;art.dataset.unit = i;
        layer.append(art);
      });
      canvas.append(layer);
    }
    if (centerline) {
      const trace = node('g', {class: 'trace', fill: 'none', stroke: '#ef4444'});
      for (const role of ROLES) for (const u of ctx.roles[role].units) trace.append(unitArt(ctx.roles[role], u, px, true));
      canvas.append(trace);
    }
    const units = selected();if (!units.length) return;
    const box = unionOf(units), p = [box[0] - 2, box[1] - 2, box[2] + 2, box[3] + 2], mx = (p[0] + p[2]) / 2, my = (p[1] + p[3]) / 2;
    for (const u of units) {
      const b = boxOf(u);
      if (units.length > 1 || outside(b)) canvas.append(node('rect', {class: 'unit' + (outside(b) ? ' out' : ''), x: b[0] - 2, y: b[1] - 2, width: b[2] - b[0] + 4, height: b[3] - b[1] + 4}));
    }
    const frame = {x: p[0], y: p[1], width: p[2] - p[0], height: p[3] - p[1]};
    canvas.append(node('rect', {class: 'move', ...frame, 'data-move': ''}), node('rect', {class: 'sel' + (outside(box) ? ' out' : ''), ...frame}));
    // Live size on the frame: painted ink (stroke included) and the centerline bounding box.
    const label = node('text', {class: 'size-label', x: p[0], y: p[1] > 4 ? p[1] - 1.2 : p[3] + 3.2});
    label.textContent = `ink ${fmt(p[2] - p[0])}×${fmt(p[3] - p[1])} · box ${fmt(box[2] - box[0])}×${fmt(box[3] - box[1])} · at ${fmt(p[0])},${fmt(p[1])}`;
    canvas.append(label);
    for (const [name, x, y] of [['nw', p[0], p[1]], ['n', mx, p[1]], ['ne', p[2], p[1]], ['e', p[2], my], ['se', p[2], p[3]], ['s', mx, p[3]], ['sw', p[0], p[3]], ['w', p[0], my]]) {
      canvas.append(node('rect', {class: 'handle ' + name, 'data-handle': name, x: x - .8, y: y - .8, width: 1.6, height: 1.6}));
    }
  }
  // ---- keyshape suggestion ----
  const holds = (b, u) => b && b[0] <= u[0] + .05 && b[1] <= u[1] + .05 && b[2] >= u[2] - .05 && b[3] >= u[3] - .05;
  // The smallest preset of each role whose keyshape, anchored for `position`, holds the part where it is now.
  function fitAt(position) {
    const saved = ctx.position;ctx.position = position;
    const sizes = Object.fromEntries(ROLES.map(role => [role,
      PRESETS[role].sizes.find(size => holds(presetBox(role, size), unionOf(ctx.roles[role].units))) ?? null]));
    ctx.position = saved;
    return ROLES.every(role => sizes[role] != null) ? {position, sizes} : null;
  }
  // Snap: the pair position, and a preset size for each part its keyshape there does not hold, whose
  // anchored keyshapes lie closest to where the parts were moved (summed edge distance). A part that
  // already fits at that position costs nothing and is left alone.
  function nearestSnap() {
    let best = null;
    const saved = ctx.position;
    for (const position of Object.keys(ANCHORS)) {
      ctx.position = position;
      let total = 0;const sizes = {};
      for (const role of ROLES) {
        const u = unionOf(ctx.roles[role].units);
        if (PRESETS[role].sizes.some(size => holds(presetBox(role, size), u))) continue;
        const options = PRESETS[role].sizes.map(size => [size, presetBox(role, size)]).filter(([, b]) => b)
          .map(([size, b]) => [size, b.reduce((d, v, k) => d + Math.abs(v - u[k]), 0)]);
        const [size, d] = options.reduce((a, b) => (!a || b[1] < a[1] ? b : a), null) || [];
        if (size == null) { total = Infinity;break; }
        sizes[role] = size;total += d;
      }
      if (!best || total < best.total) best = {position, sizes, total};
    }
    ctx.position = saved;
    return best;
  }
  function suggestionRow() {
    const here = fitAt(ctx.position), name = id => $('layout-position').querySelector(`option[value="${id}"]`)?.textContent || id;
    const row = html('div', {class: 'side-layout-suggest'});
    if (here) {
      row.append(html('span', {}, `Keyshapes fit here: Main ${here.sizes.main} · Sub ${here.sizes.sub} at ${name(ctx.position)}`));
      return row;
    }
    const elsewhere = Object.keys(ANCHORS).filter(id => id !== ctx.position).map(fitAt).filter(Boolean)
      .sort((a, b) => a.sizes.main + a.sizes.sub - b.sizes.main - b.sizes.sub)[0];
    if (elsewhere) {
      row.append(html('span', {}, `Moved parts fit the ${name(elsewhere.position)} keyshapes: Main ${elsewhere.sizes.main} · Sub ${elsewhere.sizes.sub}`),
        html('button', {type: 'button', class: 'primary', onclick: () => {
          // Re-anchor the guides only; the artwork stays where it was moved.
          ctx.position = elsewhere.position;$('layout-position').value = elsewhere.position;refresh();canvas.focus();
        }}, `Use ${name(elsewhere.position)}`));
      return row;
    }
    const snap = nearestSnap(), off = snap ? Object.keys(snap.sizes) : [];
    if (!snap || snap.total === Infinity) { row.append(html('span', {}, 'No keyshape fits; move the parts back inside the canvas.'));return row; }
    const plan = off.map(role => `${PRESETS[role].label} ${snap.sizes[role]}`).join(' · ');
    row.append(html('span', {}, `No keyshape holds the moved parts. Nearest: ${plan} at ${name(snap.position)}`),
      html('button', {type: 'button', class: 'primary', onclick: () => {
        // Re-anchor the guides there, then fit each part that was outside onto its keyshape.
        ctx.position = snap.position;$('layout-position').value = snap.position;
        for (const role of off) applyPreset(role, snap.sizes[role]);
        canvas.focus();
      }}, 'Snap to it'));
    return row;
  }
  function drawPresets() {
    presetBar.replaceChildren();
    if (!ctx.loaded) return;
    presetBar.append(suggestionRow());
    for (const role of ROLES) {
      const {base, sizes, label} = PRESETS[role], now = currentPreset(role), at = now ?? guideSize(role), current = unionOf(ctx.roles[role].units);
      presetBar.append(html('div', {class: 'side-layout-sizes ' + role}, html('span', {}, `${label} size`),
        ...sizes.filter(size => presetBox(role, size)).map(size => html('button', {type: 'button', 'aria-pressed': String(now === size),
          title: size === base ? 'Automatic size' : null, onclick: () => { applyPreset(role, size);canvas.focus(); }}, String(size))),
        html('button', {type: 'button', 'aria-pressed': String(now == null), title: `Resize the ${role} freely: drag its handles`,
          onclick: () => { free(role);canvas.focus(); }}, 'Free'),
        html('small', {}, `painted ${current[2] - current[0] + 4}×${current[3] - current[1] + 4}`)));
      const tiles = shapes(role).map(s => {
        const b = presetBox(role, at, s.id);if (!b) return null;
        const w = b[2] - b[0] + 4, h = b[3] - b[1] + 4, k = 18 / Math.max(w, h), sw = w * k, sh = h * k, locked = s.id === ctx.locked[role];
        const icon = node('svg', {viewBox: '0 0 22 22', width: 22, height: 22, 'aria-hidden': 'true'});
        icon.append(s.circle ? node('circle', {cx: 11, cy: 11, r: sw / 2, fill: 'none', stroke: 'currentColor', 'stroke-width': 1.6})
          : node('rect', {x: 11 - sw / 2, y: 11 - sh / 2, width: sw, height: sh, rx: 2, fill: 'none', stroke: 'currentColor', 'stroke-width': 1.6}));
        return html('button', {type: 'button', class: 'side-layout-shape', 'aria-pressed': String(locked && now != null), disabled: !locked,
          title: locked ? `${s.label}${s.names.length ? ' (' + s.names.join(', ') + ')' : ''}: painted ${w}×${h} at size ${at}`
                        : 'The keyshape is locked to the source drawing.',
          onclick: () => { applyPreset(role, at);canvas.focus(); }}, icon, html('span', {}, s.label), html('small', {}, `${w}×${h}${locked ? ' · own' : ''}`));
      });
      presetBar.append(html('div', {class: 'side-layout-shapes ' + role}, html('span', {}, `${label} keyshape at ${at}`), ...tiles));
    }
  }
  const NAMELESS = ['path', 'circle', 'ellipse', 'rect', 'line', 'polyline', 'polygon'];
  function drawList() {
    const scroll = list.scrollTop;
    list.replaceChildren();
    if (!ctx.loaded) return;
    for (const role of ROLES) {
      const r = ctx.roles[role], section = html('section', {}, html('h3', {}, role === 'main' ? 'Main elements' : 'Sub elements'));
      r.units.forEach((u, i) => {
        const named = u.paths.some(p => r.names[p] && !NAMELESS.includes(r.names[p]));
        section.append(html('label', {}, html('input', {type: 'checkbox', checked: ctx.sel.has(keyOf(role, i)),
          onchange: e => { if (e.currentTarget.checked) ctx.sel.add(keyOf(role, i)); else ctx.sel.delete(keyOf(role, i));render(); }}),
          html('span', {}, named ? u.paths.map(p => r.names[p]).join(' + ') : `Element ${i + 1}`, html('small', {}, ` · ${fmt(u.w + 4)}×${fmt(u.h + 4)}`))));
        // Child paths of a connected element: ticking one splits the element and selects that path.
        if (u.paths.length > 1) for (const p of u.paths) {
          section.append(html('label', {class: 'child'}, html('input', {type: 'checkbox', onchange: () => pickPath(role, i, p)}),
            html('span', {}, named && !NAMELESS.includes(r.names[p]) ? r.names[p] : `path ${p + 1}`)));
        }
      });
      section.append(html('div', {class: 'row-actions'}, html('button', {type: 'button',
        onclick: () => { r.units.forEach((_u, i) => ctx.sel.add(keyOf(role, i)));render(); }}, 'Select all')));
      list.append(section);
    }
    list.scrollTop = scroll;
  }

  // ---- pointer ----
  const point = e => { const p = new DOMPoint(e.clientX, e.clientY).matrixTransform(canvas.getScreenCTM().inverse());return [p.x, p.y]; };
  const artOf = el => {
    const art = el?.closest?.('.layout-art');
    return art ? {role: art.dataset.role, unit: Number(art.dataset.unit), path: el.closest('[data-path]') ? Number(el.closest('[data-path]').dataset.path) : null} : null;
  };
  canvas.addEventListener('pointerdown', e => {
    if (!ctx?.loaded) return;
    const additive = e.shiftKey || e.metaKey || e.ctrlKey, target = e.target;
    const hit = {handle: target.dataset?.handle || null, move: target.hasAttribute?.('data-move'), ...(artOf(target) || {role: null})};
    if (hit.move) {
      const under = document.elementsFromPoint(e.clientX, e.clientY).map(artOf).find(Boolean);
      if (under) hit.under = under;
    }
    const d = press(hit, additive);
    if (!d) return;
    canvas.focus();canvas.setPointerCapture?.(e.pointerId);e.preventDefault();
    const start = point(e);
    const move = ev => drag(d, start, point(ev), ev.shiftKey);
    const up = () => {
      canvas.removeEventListener('pointermove', move);canvas.removeEventListener('pointerup', up);canvas.removeEventListener('pointercancel', up);
      if (d.moved) refresh(); else render();
    };
    canvas.addEventListener('pointermove', move);canvas.addEventListener('pointerup', up);canvas.addEventListener('pointercancel', up);
  });
  canvas.addEventListener('keydown', e => { if (key(e)) { e.preventDefault();e.stopPropagation(); } });
  new ResizeObserver(() => { if (ctx?.loaded && dialog.open) drawCanvas(); }).observe(canvas);

  // ---- controls ----
  dialog.querySelectorAll('[data-select-level]').forEach(button => button.addEventListener('click', () => { ctx.level = button.dataset.selectLevel;render();canvas.focus(); }));
  $('layout-split').addEventListener('click', split);
  $('layout-clear-selection').addEventListener('click', () => { ctx.sel.clear();render(); });
  const centerlineBox = $('layout-centerline');
  centerlineBox.checked = centerline;
  centerlineBox.addEventListener('change', () => {
    centerline = centerlineBox.checked;
    try { localStorage.setItem('side-layout-centerline', centerline ? 'on' : 'off'); } catch { /* no storage */ }
    if (ctx) render();
  });
  applyButton.addEventListener('click', applyLayout);
  saveButton.addEventListener('click', save);
  forceBox.addEventListener('change', () => { if (ctx) render(); });
  $('layout-reset').addEventListener('click', () => restore(ctx.auto, ctx.sourcePosition));
  $('layout-discard').addEventListener('click', () => restore(ctx.opened, ctx.openedPosition));
  for (const id of candidateFields) $(id).addEventListener('input', () => {
    if (!ctx?.loaded) return;
    if (id === 'layout-position') changePosition($(id).value); else refresh();
  });
  $('layout-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('close', () => {
    if (dialog.open) return;  // the event is queued: the editor was reopened for another combination since
    if (ctx) ctx.token++;ctx = null;
    // An inline editor goes back to the page body, so a re-rendered card list cannot drop it.
    dialog.classList.remove('inline');document.body.append(dialog);
    for (const tile of document.querySelectorAll('.variant-tile.editing')) tile.classList.remove('editing');
  });
  // The gallery rebuilds its cards: park the inline editor first, then put it back under its pair.
  function park() { if (dialog.open && dialog.classList.contains('inline')) document.body.append(dialog); }
  function reattach() {
    if (!dialog.open || !dialog.classList.contains('inline') || dialog.parentElement !== document.body) return;
    const slot = ctx && document.querySelector(`#list [data-layout-slot="${CSS.escape(ctx.row.id)}"]`);
    if (slot) slot.append(dialog); else dialog.close();
  }

  // `host` (a pair's layout slot) shows the editor inline under that pair's combinations.
  async function open(row, candidate = null, host = null, backend) {
    const positionSelect = $('layout-position'), sourcePosition = row.id.slice(-2);
    const known = position => [...positionSelect.options].some(option => option.value === position);
    const opening = ctx = {row, roles: {}, sel: new Set(), level: 'whole', token: 0, loaded: false, stale: true, result: null, valid: false, forceable: false,
                           busy: false, combining: false, locked: {}, auto: {}, opened: {}, composed: null,
                           backend, sourcePosition: known(sourcePosition) ? sourcePosition : 'ri'};
    ctx.position = candidate?.position && known(candidate.position) ? candidate.position : ctx.sourcePosition;
    ctx.openedPosition = ctx.position;
    // The proposal this edit takes the place of when saved (the tile it was opened from).
    ctx.replaces = candidate?.replaces ?? candidate?.variant ?? candidate?.base_variant ?? null;
    $('layout-title').textContent = `Adjust layout · 64×64 · ${row.concept}${candidate?.label ? ` · ${candidate.label}` : ''}`;
    const base = $('layout-base');
    base.replaceChildren(...(row.variants || []).map(name => new Option(name, name)));
    if (!base.options.length) base.add(new Option('current', 'current'));
    if (candidate?.base_variant) base.value = candidate.base_variant;
    // Offer only what the server can combine: a sub without a real fill is used as its outline.
    const subSelect = $('layout-sub-variant'), subFilled = row.sub?.has_fill !== false;
    subSelect.querySelector('option[value="fill"]').disabled = !subFilled;
    subSelect.value = subFilled ? (candidate?.sub_variant || 'fill') : 'outline';
    forceBox.checked = !!candidate?.keyshape_override;
    positionSelect.value = ctx.position;
    $('layout-name').value = candidate?.kind === 'layout' ? candidate.variant.replace(/^layout-/, '')
      : candidate?.base_variant ? `${candidate.base_variant}-${candidate.sub_variant || 'fill'}-sub`.replace(/[^a-z0-9-]+/g, '-') : 'manual-adjusted';
    $('layout-reason').value = candidate?.layout_reason || 'Pair-local main/sub placement reviewed at 4px and 8px.';
    clearResult();readout.textContent = 'Loading elements…';setStatus('');
    if (host) {
      if (dialog.open && !dialog.classList.contains('inline')) dialog.close();
      ctx = opening;
      dialog.classList.add('inline');host.append(dialog);
      if (!dialog.open) dialog.show();
      dialog.scrollIntoView({block: 'nearest', behavior: 'smooth'});
    } else {
      if (dialog.open && dialog.classList.contains('inline')) dialog.close();
      ctx = opening;
      if (!dialog.open) dialog.showModal();
    }
    render();
    let elements;
    try { [elements, keyshapes] = await Promise.all([backend.elements(), backend.keyshapes()]); }
    catch (error) { if (ctx === opening) { readout.textContent = '';setStatus(error.message, true); }return; }
    if (ctx !== opening) return;
    for (const role of ROLES) {
      const r = elements[role];
      ctx.roles[role] = {markup: r.markup, names: r.names, sources: r.sources, units: []};
      ctx.roles[role].units = withSrc(ctx.roles[role], r.units);
      ctx.auto[role] = plain(r.units);
      ctx.locked[role] = lockedShape(role);
    }
    ctx.loaded = true;ctx.opened = ctx.auto;
    // The first composition: the pick's own boxes (candidate.units), else the pair's placement.
    if (candidate?.units) for (const role of ROLES) if (candidate.units[role]?.length) ctx.roles[role].units = withSrc(ctx.roles[role], candidate.units[role]);
    const saved = proposal();
    try { await compose(saved, true); }
    catch (error) {
      if (ctx !== opening || !candidate) return;
      try { await compose(proposal(), true);setStatus(`The saved candidate no longer renders (${error.message}); showing the production placement.`, true); }
      catch { return; }
    }
    if (ctx !== opening) return;
    ctx.opened = Object.fromEntries(ROLES.map(role => [role, plain(ctx.roles[role].units)]));
    render();canvas.focus();
  }
  window.SideLayoutEditor = {open, park, reattach};
})();
