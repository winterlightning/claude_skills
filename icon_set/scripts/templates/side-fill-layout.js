/* The fill side pair layout editor's renderer, in the browser: a port of side_fill/pair_layout_review.py (the
 * keyshape checks of a layout proposal) and main_gallery_server.preview_side_layout, on side-fill-combine.js.
 *
 *   SideFillLayout.elements(sourceText) → {markup, names, sources}       the parts the editor draws and moves
 *   SideFillLayout.preview({keyshapes, position, main, sub, options, proposal}) → {candidate, svg, stress_svg}
 *
 * `keyshapes` is data/side-keyshapes.json ({main|sub: {NAME: [x0, y0, x1, y1]}}); `main` / `sub` are the parts as a pick
 * names them ({svg, source, outline}); `proposal` is what the editor sends ({position, main: {units, shape, size,
 * guide_size, …}, sub: {…}}). No DOM: the page and Node run the same code.
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory(require('./side-fill-combine.js'), require('./combine-side.js'));
  else root.SideFillLayout = factory(root.SideFillCombine, root.CombineSide);
})(typeof self !== 'undefined' ? self : this, function (Fill, CombineSide) {
  'use strict';

  const I = Fill.internals;
  const ANCHORS = {br: [1, 1], bl: [0, 1], tr: [1, 0], tl: [0, 0], ri: [1, .5], le: [0, .5], bo: [.5, 1], to: [.5, 0]};
  const PRESETS = {main: {base: 48, min: 32, max: 64}, sub: {base: 32, min: 12, max: 44}};
  const PAINTED_PADDING = 4, GAP = 4, STRESS_GAP = 8;
  const fail = message => { throw new Fill.FillError(message); };
  // Python's round(): half to even, so preset boxes land where the Python review puts them.
  const pyRound = v => { const f = Math.floor(v), d = v - f; return d > .5 ? f + 1 : d < .5 ? f : (f % 2 === 0 ? f : f + 1); };

  function elements(sourceText) {
    const {markup, names, sources} = CombineSide.elementParts(sourceText);
    return {markup, names, sources};
  }
  const sourceBounds = sourceText => {
    const boxes = elements(sourceText).sources.filter(Boolean);
    return [Math.min(...boxes.map(b => b[0])), Math.min(...boxes.map(b => b[1])), Math.max(...boxes.map(b => b[2])), Math.max(...boxes.map(b => b[3]))];
  };

  // source_keyshape_name: the drawing's own keyshape (SQUARE first), else 'custom'.
  function shapeName(keyshapes, role, bounds) {
    const names = Object.keys(keyshapes[role] || {}).sort((a, b) => (a !== 'SQUARE') - (b !== 'SQUARE'));
    return names.find(name => keyshapes[role][name].every((v, i) => Math.abs(v - bounds[i]) < .05)) || 'custom';
  }

  // keyshape_preset_box: the centerline box of a role at a size, its keyshape anchored opposite the other part.
  function presetBox(keyshapes, role, position, bounds, size, shape) {
    const {base, min, max} = PRESETS[role];
    if (!Number.isInteger(size) || size < min || size > max || (size - min) % 4) fail(`${role} preset size must be one of ${min}…${max} in steps of 4`);
    let w, h;
    if (shape === 'own') {
      const k = size / base;
      w = pyRound((bounds[2] - bounds[0]) * k); h = pyRound((bounds[3] - bounds[1]) * k);
    } else {
      const b = (keyshapes[role] || {})[shape];
      if (!b) fail(`unknown ${role} keyshape: ${shape}`);
      w = b[2] - b[0] + size - base; h = b[3] - b[1] + size - base;
    }
    const inner = 64 - 2 * PAINTED_PADDING;
    if (w < 4 || h < 4 || w + 4 > inner || h + 4 > inner) fail(`${role} keyshape preset is too large for the 64px canvas`);
    const [px, py] = ANCHORS[position] || fail(`unknown pair position ${position}`);
    const [ax, ay] = role === 'main' ? [1 - px, 1 - py] : [px, py];
    const x = pyRound(PAINTED_PADDING + (inner - w - 4) * ax) + 2, y = pyRound(PAINTED_PADDING + (inner - h - 4) * ay) + 2;
    return [x, y, x + w, y + h];
  }

  // keyshape_validation: where the boxes sit against the role's guide at the chosen size.
  function validation(keyshapes, role, position, bounds, boxes, change) {
    const source = shapeName(keyshapes, role, bounds);
    const current = [Math.min(...boxes.map(b => b.x)), Math.min(...boxes.map(b => b.y)),
                     Math.max(...boxes.map(b => b.x + b.w)), Math.max(...boxes.map(b => b.y + b.h))];
    const presetMode = 'size' in change || 'shape' in change;
    const mode = presetMode ? change.mode || 'preset' : 'baseline';
    const custom = mode === 'custom';
    const guideShape = custom ? 'own' : presetMode ? change.shape || 'own' : source !== 'custom' ? source : 'own';
    const iconSize = change.size ?? PRESETS[role].base;
    const size = change.guide_size ?? iconSize;
    const target = presetBox(keyshapes, role, position, bounds, size, guideShape);
    const overflow = Math.max(0, target[0] - current[0], target[1] - current[1], current[2] - target[2], current[3] - target[3]);
    const ow = bounds[2] - bounds[0], oh = bounds[3] - bounds[1], aw = current[2] - current[0], ah = current[3] - current[1];
    const aspect = ow && oh ? Math.abs(aw / ow - ah / oh) : 0;
    const preset = custom ? source : guideShape;
    return {source_shape: source, centerline_box: current,
            stroke_envelope_inside_canvas: current[0] >= 2 && current[1] >= 2 && current[2] <= 62 && current[3] <= 62,
            preset, size: iconSize, guide_size: size, mode, keyshape_overflow_px: Math.round(overflow * 1000) / 1000,
            aspect_error: Math.round(aspect * 1000) / 1000, target_centerline_box: target,
            fits_keyshape: overflow <= .05 && (mode === 'preset' || 'units' in change || aspect <= .05),
            guide_painted_box: [target[0] - 2, target[1] - 2, target[2] + 2, target[3] + 2],
            guide_kind: preset === 'CIRCLE' ? 'circle' : 'rect'};
  }

  // keyshape_ink_outside: the painted part's ink beyond its guide (grown a quarter pixel).
  function inkOutside(geometry, check) {
    const [x0, y0, x1, y1] = check.guide_painted_box;
    let guide;
    if (check.guide_kind === 'circle') {
      const cx = (x0 + x1) / 2, cy = (y0 + y1) / 2, r = (x1 - x0) / 2, ring = [];
      for (let i = 0; i < 384; i++) ring.push([cx + r * Math.cos(2 * Math.PI * i / 384), cy + r * Math.sin(2 * Math.PI * i / 384)]);
      guide = I.normalize([ring.map(([x, y]) => ({X: Math.round(x * 1e5), Y: Math.round(y * 1e5)}))]);
    } else guide = I.normalize([[[x0, y0], [x1, y0], [x1, y1], [x0, y1]].map(([x, y]) => ({X: Math.round(x * 1e5), Y: Math.round(y * 1e5)}))]);
    return I.area(I.difference(geometry, I.buffer(guide, .25)));
  }

  const inside = geometry => { const b = I.bounds(geometry); return !!b && b.every(v => v >= -0.01 && v <= 64.01); };

  // Every element of the drawing in exactly one unit, each unit on whole grid units.
  function checkUnits(role, units, sourceText) {
    const drawable = elements(sourceText).sources.map((b, i) => b ? i : null).filter(i => i !== null);
    if (!Array.isArray(units) || !units.length) fail(`${role} element layout must be a nonempty list`);
    const listed = units.flatMap(u => u.paths || []).sort((a, b) => a - b);
    if (listed.length !== drawable.length || listed.some((v, i) => v !== drawable[i])) fail(`${role} element layout must place each original path exactly once`);
    for (const u of units) for (const k of ['x', 'y', 'w', 'h']) if (!Number.isInteger(u[k])) fail(`${role} element ${k} must be an integer grid unit`);
  }

  // preview_side_layout: the proposal combined, checked, and stress-cut at 8px.
  function preview({keyshapes, position, main, sub, options = null, proposal}) {
    const where = proposal.position || position;
    const layouts = {}, checks = {};
    for (const [role, part] of [['main', main], ['sub', sub]]) {
      const change = proposal[role] || {};
      checkUnits(role, change.units, part.source);
      layouts[role] = change.units.map(({paths, x, y, w, h}) => ({paths: [...paths], x, y, w, h}));
      checks[role] = validation(keyshapes, role, where, sourceBounds(part.source), layouts[role], change);
      if (layouts[role].some(b => b.x < 2 || b.y < 2 || b.x + b.w > 62 || b.y + b.h > 62)) fail(`${role} 4px stroke envelope is outside 64x64`);
    }
    const result = Fill.combine({main: {...main, layout: layouts.main}, sub: {...sub, layout: layouts.sub}, options});
    const placedMain = result.main.placed, placedSub = result.sub.geometry;
    for (const [role, geometry] of [['main', placedMain], ['sub', placedSub]]) {
      checks[role].ink_outside_guide_px2 = Math.round(inkOutside(geometry, checks[role]) * 1000) / 1000;
      if (checks[role].ink_outside_guide_px2 > .5) checks[role].fits_keyshape = false;
      if (!inside(geometry)) fail('main or sub ink is outside 64x64');
    }
    if (!inside(result.geometry)) fail('combined ink is outside 64x64');
    let stressSvg = null, losses = [];
    if (!main.outline) {
      const stressCut = options?.overlap === 'join' ? placedMain : I.cutMain(placedMain, placedSub, STRESS_GAP).cut;
      stressSvg = Fill.toSvg(I.union([stressCut, placedSub]));
      // White counters of the filled main whose black border the 8px cut takes away.
      losses = I.polygons(placedMain).flatMap(p => p.holes).map((hole, n) => {
        const border = I.intersection(placedMain, I.buffer(I.normalize([hole]), 4));
        return {region: `white-${n + 1}`, lost_black_border_px2: Math.round(I.area(I.difference(border, stressCut)) * 100) / 100};
      });
    }
    const gap = I.distance(result.main.geometry, placedSub);
    return {svg: result.svg, stress_svg: stressSvg,
            candidate: {layout_boxes: layouts, keyshape_validation: checks, position: where,
                        render_gap_px: gap === null ? GAP : Math.round(gap * 1000) / 1000, white_border_loss_at_8px: losses,
                        main_how: result.main.how, sub_how: result.sub.how}};
  }

  return {elements, preview, presetBox, validation, shapeName, sourceBounds};
});
