#!/usr/bin/env node
// How a side combination's main and sub meet, for the layout decision (/side-layout-adjust).
//
//   node icon_set/scripts/side_overlap.mjs <DIR> [--json] [--min-piece 6] [--detach 4.5] [--heavy-cut 30] [--shave-reach 4] [--lost-part 40] [--container 80]
//
// DIR is a side_layout.mjs work folder; the pair is composed from its layout.json (the proposal, or the stored
// layout right after fetch). Three drawings are rasterized at 8 px a grid unit with the 4-unit round stroke:
//   main    the main where it was placed, before the sub erased it
//   kept    the main as combined (the `main-icon-clipped` group of the combined SVG, exactly as stored)
//   sub     the sub where it was placed
// and measured:
//   erased_pct   share of the main's ink the sub erased (how deep the sub cuts in)
//   overlap_pct  share of the sub's ink that lies on the uncut main (how far the sub sits on the main)
//   gap          clear space between the kept main and the sub, in units (4 = the engine's clean knockout)
//   main_to_sub  kept main ink over sub ink: below about 1 the sub takes over the icon
//   reach        clear space between the uncut main and the sub (<= 0: they overlap; large: the sub floats apart)
//   inside_pct   share of the sub's ink inside the uncut main's ink box (the main around the sub, not beside it)
//   opened       closed outlines of the main the sub cut open (normal for a knockout; context only)
//   fragments    connected pieces of the main before and after; `new` pieces were cut off by the sub, `stubs` are
//                cut pieces shorter than --min-piece units (crumbs left at the edge of the knockout)
// and flagged: detached (reach > --detach: the two do not meet, nothing is knocked out), fragmented (any new piece),
// lost_feature (a run of one element between turns, such as a cart's handle, at least --feature-min units long and
// erased --lost-feature percent or more), stub (any crumb), heavy_cut (erased_pct > --heavy-cut), lost_part (a drawn element of the main, such as a jar's lip
// or a bike's saddle, erased --lost-part percent or more, even when it touches the rest), shaved (the sub's ink does not touch the main, reach > 0,
// yet it sits inside the engine's 4-unit cut margin, reach < --shave-reach, or the cut erased at least --shave-min percent:
// a nick on the main however small), container (inside_pct >= --container: the main surrounds the sub, a symbol inside
// a head or a remote inside a house, which is a container combination, not a side one). `penalty` adds them up to compare proposals: lower is
// better, 0 means nothing flagged. Writes DIR/overlap.png: kept main black, erased main red, sub blue, stubs orange.
import {execFileSync} from 'node:child_process';
import {rmSync, writeFileSync} from 'node:fs';
import path from 'node:path';
import {Side, compose, layoutFor, readJSON} from './side_compose.mjs';

const RES = 8;               // raster pixels a grid unit
const HALF = 2;              // half the 4-unit stroke
const GRID = 24;             // the engine's placement boxes are on a 24 grid (combine-side.js GRID)

// ---- geometry ----

function pointSegment(px, py, [[ax, ay], [bx, by]]) {
  const dx = bx - ax, dy = by - ay, len = dx * dx + dy * dy;
  const t = len ? Math.max(0, Math.min(1, ((px - ax) * dx + (py - ay) * dy) / len)) : 0;
  return Math.hypot(px - (ax + t * dx), py - (ay + t * dy));
}
function segmentDistance(s, t) {
  const [[ax, ay], [bx, by]] = s, [[cx, cy], [dx, dy]] = t;
  const cross = (ox, oy, px, py, qx, qy) => (px - ox) * (qy - oy) - (py - oy) * (qx - ox);
  const d1 = cross(cx, cy, dx, dy, ax, ay), d2 = cross(cx, cy, dx, dy, bx, by);
  const d3 = cross(ax, ay, bx, by, cx, cy), d4 = cross(ax, ay, bx, by, dx, dy);
  if (((d1 > 0 && d2 < 0) || (d1 < 0 && d2 > 0)) && ((d3 > 0 && d4 < 0) || (d3 < 0 && d4 > 0))) return 0;
  return Math.min(pointSegment(ax, ay, t), pointSegment(bx, by, t), pointSegment(cx, cy, s), pointSegment(dx, dy, s));
}
// Clear space between two stroked drawings (centerline distance less both half strokes).
function clearance(a, b) {
  let best = Infinity;
  for (const s of a) for (const t of b) best = Math.min(best, segmentDistance(s, t));
  return best === Infinity ? null : +(best - 2 * HALF).toFixed(2);
}

// A part's centerline segments where the engine placed it: fold's fitInto(engineSegments(document), box), the
// document baked from the hand layout (each group's elements moved and scaled by groupTransform) when it has one.
function placedSegments(form, placement, groups, canvas) {
  const document = form.engine_document ?? form.document;
  let segments, owner = null, names = null;
  if (groups) {
    const parts = Side.elementParts(document);
    segments = [];
    owner = [];
    names = parts.names;
    for (const g of groups) {
      const {sx, sy, tx, ty} = Side.groupTransform(g, parts.sources, parts.round, canvas);  // round parts as the engine draws them
      for (const i of g.paths) for (const [a, b] of (parts.inkSegments || parts.segments)[i] || []) {
        segments.push([[a[0] * sx + tx, a[1] * sy + ty], [b[0] * sx + tx, b[1] * sy + ty]]);
        owner.push(i);
      }
    }
  } else segments = Side.engineSegments(document);
  const k = canvas / GRID, box = placement.box, target = [box.x * k, box.y * k, box.w * k, box.h * k];
  const placed = Side.internals.fitInto(segments, target);
  // fitInto keeps the order: owner[j] is the element (path index) segment j came from, names[i] its id.
  placed.owner = owner;
  placed.names = names;
  if (!groups) {
    // Automatic placement fits the whole drawing at once. Fit each element's segments together with it: the box of
    // the union is the drawing's box, so they share its transform. Kept only when the drawing lands where it did alone.
    try {
      const parts = Side.elementParts(document), extra = [], extraOwner = [];
      (parts.inkSegments || parts.segments).forEach((list, i) => { for (const seg of list || []) { extra.push(seg); extraOwner.push(i); } });
      const both = Side.internals.fitInto([...segments, ...extra], target);
      const same = placed.every((seg, j) => seg.every((p, q) => Math.abs(p[0] - both[j][q][0]) < 1e-6 && Math.abs(p[1] - both[j][q][1]) < 1e-6));
      if (same && extra.length) {
        placed.elements = both.slice(segments.length);
        placed.elementOwner = extraOwner;
        placed.names = parts.names;
      }
    } catch { /* no per-element view; parts stay unmeasured */ }
  }
  return placed;
}

// The kept main as stored: the straight segments of the combined SVG's `main-icon-clipped` path.
function keptSegments(svg) {
  const group = svg.match(/<g id="main-icon-clipped"[^>]*>([\s\S]*?)<\/g>/);
  const d = group ? [...group[1].matchAll(/\sd="([^"]*)"/g)].map(m => m[1]).join(' ') : '';
  const segs = [...d.matchAll(/M\s*(-?[\d.]+)[ ,](-?[\d.]+)\s*L\s*(-?[\d.]+)[ ,](-?[\d.]+)/g)]
    .map(m => [[+m[1], +m[2]], [+m[3], +m[4]]]);
  // Filled dots the engine keeps (keepDots, the 72 build) are <circle> elements, not path lines: list them, so
  // analyze() counts the uncut main's ink under each kept dot as kept and a kept dot does not read as erased.
  segs.dots = [];
  for (const m of group ? group[1].matchAll(/<circle\b[^>]*>/g) : []) {
    const at = k => +(m[0].match(new RegExp(`\\s${k}="(-?[\\d.]+)"`)) || [])[1];
    const cx = at('cx'), cy = at('cy'), r = at('r');
    if (/fill="(?!none)/.test(m[0]) && [cx, cy, r].every(Number.isFinite)) segs.dots.push({cx, cy, r});
  }
  return segs;
}

// ---- raster ----

function raster(segments, n) {
  const mask = new Uint8Array(n * n);
  for (const seg of segments) {
    const [[ax, ay], [bx, by]] = seg;
    const x0 = Math.max(0, Math.floor((Math.min(ax, bx) - HALF) * RES)), x1 = Math.min(n - 1, Math.ceil((Math.max(ax, bx) + HALF) * RES));
    const y0 = Math.max(0, Math.floor((Math.min(ay, by) - HALF) * RES)), y1 = Math.min(n - 1, Math.ceil((Math.max(ay, by) + HALF) * RES));
    for (let y = y0; y <= y1; y++) for (let x = x0; x <= x1; x++) {
      const i = y * n + x;
      if (!mask[i] && pointSegment((x + 0.5) / RES, (y + 0.5) / RES, seg) <= HALF) mask[i] = 1;
    }
  }
  return mask;
}
const count = mask => mask.reduce((a, v) => a + v, 0);

// 8-connected pieces of a mask → {labels, pieces: [{label, px, box: [x0, y0, x1, y1] in px}]}.
function pieces(mask, n) {
  const labels = new Int32Array(n * n), out = [];
  const stack = [];
  for (let start = 0; start < mask.length; start++) {
    if (!mask[start] || labels[start]) continue;
    const label = out.length + 1, piece = {label, px: 0, box: [n, n, -1, -1]};
    labels[start] = label;
    stack.push(start);
    while (stack.length) {
      const i = stack.pop(), x = i % n, y = (i - x) / n;
      piece.px++;
      piece.box = [Math.min(piece.box[0], x), Math.min(piece.box[1], y), Math.max(piece.box[2], x), Math.max(piece.box[3], y)];
      for (let dy = -1; dy <= 1; dy++) for (let dx = -1; dx <= 1; dx++) {
        const xx = x + dx, yy = y + dy;
        if (xx < 0 || yy < 0 || xx >= n || yy >= n) continue;
        const j = yy * n + xx;
        if (mask[j] && !labels[j]) { labels[j] = label; stack.push(j); }
      }
    }
    out.push(piece);
  }
  return {labels, pieces: out};
}

// Enclosed holes of a mask (4-connected background pieces that do not reach the border): closed outlines.
function holes(mask, n) {
  const seen = new Uint8Array(n * n), stack = [];
  let found = 0;
  for (let start = 0; start < mask.length; start++) {
    if (mask[start] || seen[start]) continue;
    let border = false;
    seen[start] = 1;
    stack.push(start);
    while (stack.length) {
      const i = stack.pop(), x = i % n, y = (i - x) / n;
      if (x === 0 || y === 0 || x === n - 1 || y === n - 1) border = true;
      for (const j of [x > 0 ? i - 1 : -1, x < n - 1 ? i + 1 : -1, y > 0 ? i - n : -1, y < n - 1 ? i + n : -1]) {
        if (j >= 0 && !mask[j] && !seen[j]) { seen[j] = 1; stack.push(j); }
      }
    }
    if (!border) found++;
  }
  return found;
}

// ---- the measurement ----

const DEFAULTS = {minPiece: 6, detach: 4.5, heavyCut: 30, shaveMin: 1, shaveReach: 4, lostPart: 40, container: 80,
                  featureTurn: 60, featureMin: 10, lostFeature: 85, tailMin: 8};

// The features of one drawn element: its centerline split where the stroke turns (a cart's rail, riser and handle are
// one path but three features). Consecutive segments stay in one feature while their heading stays within
// --feature-turn degrees of the feature's first heading; a jump between subpaths also starts a new feature.
export function features(segs, turn = DEFAULTS.featureTurn) {
  const out = [];
  let cur = null, ref = null, last = null;
  for (const seg of segs) {
    const [[ax, ay], [bx, by]] = seg, len = Math.hypot(bx - ax, by - ay);
    const joined = last && Math.hypot(ax - last[0], ay - last[1]) < 0.3;
    const h = len > 0.05 ? Math.atan2(by - ay, bx - ax) : null;
    let diff = 0;
    if (h !== null && ref !== null) { diff = Math.abs(h - ref) * 180 / Math.PI; if (diff > 180) diff = 360 - diff; }
    if (!cur || !joined || diff > turn) { cur = {segs: [], length: 0}; out.push(cur); ref = h; }
    if (ref === null) ref = h;
    cur.segs.push(seg);
    cur.length += len;
    last = [bx, by];
  }
  return out;
}

// `composed` from side_layout.compose (pairRequest), `layout` the layout passed to it ({main?, sub?} groups or null).
export function analyze(composed, layout, limits = {}) {
  const {minPiece, detach, heavyCut, shaveMin, shaveReach, lostPart, container, featureTurn, featureMin, lostFeature, tailMin} = {...DEFAULTS, ...limits};
  const canvas = composed.result.canvas || 64, n = canvas * RES, unit = RES * RES;
  const row = composed.current.row, [mainAt, subAt] = composed.result.placements;
  const mainSegs = placedSegments(row.mains[0], mainAt, layout?.main, canvas);
  const subSegs = placedSegments(row.subs[0], subAt, layout?.sub, canvas);
  const keptSegs = keptSegments(composed.svg);

  const main = raster(mainSegs, n), sub = raster(subSegs, n), kept = raster(keptSegs, n);
  for (const {cx, cy, r} of keptSegs.dots || []) {
    const R = (r + HALF) * RES, x0 = Math.max(0, Math.floor(cx * RES - R)), x1 = Math.min(n - 1, Math.ceil(cx * RES + R));
    const y0 = Math.max(0, Math.floor(cy * RES - R)), y1 = Math.min(n - 1, Math.ceil(cy * RES + R));
    for (let y = y0; y <= y1; y++) for (let x = x0; x <= x1; x++) {
      if ((x + 0.5 - cx * RES) ** 2 + (y + 0.5 - cy * RES) ** 2 <= R * R && main[y * n + x]) kept[y * n + x] = 1;
    }
  }
  let mainPx = 0, keptOnMain = 0, subPx = 0, subOnMain = 0;
  for (let i = 0; i < main.length; i++) {
    if (main[i]) { mainPx++; if (kept[i]) keptOnMain++; }
    if (sub[i]) { subPx++; if (main[i]) subOnMain++; }
  }
  // Under half a percent is the 2-decimal rounding of the stored path, not a cut.
  const raw = mainPx ? 100 * (mainPx - keptOnMain) / mainPx : 0, erasedPct = raw < 0.5 ? 0 : raw;
  const keptPx = count(kept);

  // The uncut main's ink box: a sub whose ink lies mostly inside it is surrounded by the main, not beside it.
  let bx0 = n, by0 = n, bx1 = -1, by1 = -1, subInside = 0;
  for (let i = 0; i < main.length; i++) if (main[i]) {
    const x = i % n, y = (i - x) / n;
    bx0 = Math.min(bx0, x); bx1 = Math.max(bx1, x); by0 = Math.min(by0, y); by1 = Math.max(by1, y);
  }
  for (let i = 0; i < sub.length; i++) if (sub[i]) {
    const x = i % n, y = (i - x) / n;
    if (x >= bx0 && x <= bx1 && y >= by0 && y <= by1) subInside++;
  }
  const insidePct = subPx ? 100 * subInside / subPx : 0;

  // Pieces of the main before and after; a kept piece belongs to the uncut piece it mostly lies on.
  const before = pieces(main, n), after = pieces(kept, n);
  const home = new Map();
  for (let i = 0; i < kept.length; i++) {
    if (!kept[i] || !before.labels[i]) continue;
    const votes = home.get(after.labels[i]) || new Map();
    votes.set(before.labels[i], (votes.get(before.labels[i]) || 0) + 1);
    home.set(after.labels[i], votes);
  }
  const fromOf = label => [...(home.get(label) || new Map())].sort((a, b) => b[1] - a[1])[0]?.[0] ?? null;
  // Stroke length of a piece: area = 4·length + the two round caps (4π).
  const length = px => Math.max(0, (px / unit - Math.PI * HALF * HALF) / (2 * HALF));
  const keptPieces = after.pieces.map(p => {
    const from = fromOf(p.label), source = before.pieces[from - 1];
    const cut = !source || p.px < source.px * 0.98;
    return {area: +(p.px / unit).toFixed(1), length: +length(p.px).toFixed(1), cut, from,
            box: p.box.map((v, k) => +(k < 2 ? v / RES : (v + 1) / RES).toFixed(1))};
  });
  const perSource = new Map();
  for (const p of keptPieces) perSource.set(p.from, (perSource.get(p.from) || 0) + 1);
  const removed = before.pieces.filter(p => !perSource.has(p.label)).length;
  const stubs = keptPieces.filter(p => p.cut && p.length < minPiece);
  const newPieces = keptPieces.length - (before.pieces.length - removed);

  // Each drawn element of the main (lip, saddle, page, hands) on its own: how much of it the cut left. Touching
  // elements rasterize into one connected piece, so `removed` misses a lip erased off a jar's neck; this does not.
  const parts = [];
  const elementSegs = mainSegs.owner ? mainSegs : mainSegs.elements, elementOwner = mainSegs.owner ?? mainSegs.elementOwner;
  if (elementSegs && elementOwner) {
    const byElement = new Map();
    elementSegs.forEach((seg, j) => {
      const i = elementOwner[j];
      if (!byElement.has(i)) byElement.set(i, []);
      byElement.get(i).push(seg);
    });
    for (const [i, segs] of [...byElement].sort((a, b) => a[0] - b[0])) {
      const mask = raster(segs, n);
      let px = 0, left = 0;
      for (let k = 0; k < mask.length; k++) if (mask[k]) { px++; if (kept[k]) left++; }
      if (!px) continue;
      parts.push({index: i, name: mainSegs.names?.[i] ?? String(i), erased_pct: +(100 * (px - left) / px).toFixed(1)});
    }
  }
  const lostParts = parts.filter(p => p.erased_pct >= lostPart);

  // Each element's features on their own (the cart's riser and handle, a pot's spout): a feature at least
  // --feature-min units long erased --lost-feature percent or more is a lost feature, even when its element keeps most
  // of its ink. Elements already lost (lost_part) are not counted again.
  const lostFeatures = [];
  if (elementSegs && elementOwner) {
    const byElement = new Map();
    elementSegs.forEach((seg, j) => { const i = elementOwner[j]; if (!byElement.has(i)) byElement.set(i, []); byElement.get(i).push(seg); });
    const lostNames = new Set(lostParts.map(p => p.index));
    const inked = (x, y) => { const px = Math.floor(x * RES), py = Math.floor(y * RES); return px >= 0 && py >= 0 && px < n && py < n && kept[py * n + px]; };
    // Erased run from one open end of a stroke: its length and the widest turn inside it.
    const tail = run => {
      let length = 0, ref = null, widest = 0;
      for (const [[ax, ay], [bx, by]] of run) {
        const len = Math.hypot(bx - ax, by - ay), steps = Math.max(1, Math.ceil(len * 2));
        let gone = 0;
        for (let t = 0; t <= steps; t++) { if (inked(ax + (bx - ax) * t / steps, ay + (by - ay) * t / steps)) break; gone = t / steps; }
        if (len > 0.05) {
          const h = Math.atan2(by - ay, bx - ax);
          if (ref === null) ref = h;
          let d = Math.abs(h - ref) * 180 / Math.PI; if (d > 180) d = 360 - d;
          if (gone > 0.5) widest = Math.max(widest, d);
        }
        length += len * gone;
        if (gone < 1) break;
      }
      return {length, turn: widest};
    };
    for (const [i, all] of byElement) {
      if (lostNames.has(i)) continue;
      const seen = new Set(), segs = all.filter(sg => { const k = sg.flat().map(v => v.toFixed(2)).join(); return !seen.has(k) && seen.add(k); });
      // Subpaths: runs of joined segments. An open one (ends apart) whose end the cut chopped off through a turn has
      // lost its end feature (the cart's riser and handle), even when no single feature reaches --lost-feature.
      const subpaths = [];
      for (const sg of segs) {
        const last = subpaths.at(-1)?.at(-1);
        if (last && Math.hypot(sg[0][0] - last[1][0], sg[0][1] - last[1][1]) < 0.3) subpaths.at(-1).push(sg); else subpaths.push([sg]);
      }
      subpaths.forEach((sp, k) => {
        const a = sp[0][0], b = sp.at(-1)[1], total = sp.reduce((t, [[ax, ay], [bx, by]]) => t + Math.hypot(bx - ax, by - ay), 0);
        if (Math.hypot(a[0] - b[0], a[1] - b[1]) < 0.5 || total < 2 * tailMin) return;
        for (const [end, run] of [['start', sp], ['end', sp.slice().reverse().map(([p, q]) => [q, p])]]) {
          const t = tail(run);
          if (t.length >= tailMin && t.turn >= featureTurn)
            lostFeatures.push({element: mainSegs.names?.[i] ?? String(i), feature: `${end} of stroke ${k}`, length: +t.length.toFixed(1),
                               erased_pct: +(100 * t.length / total).toFixed(1), turn: Math.round(t.turn)});
        }
      });
      features(segs, featureTurn).forEach((f, k) => {
        if (f.length < featureMin) return;
        const mask = raster(f.segs, n);
        let px = 0, left = 0;
        for (let q = 0; q < mask.length; q++) if (mask[q]) { px++; if (kept[q]) left++; }
        const pct = px ? 100 * (px - left) / px : 0;
        if (pct >= lostFeature) lostFeatures.push({element: mainSegs.names?.[i] ?? String(i), feature: k, length: +f.length.toFixed(1), erased_pct: +pct.toFixed(1)});
      });
    }
  }

  const gap = clearance(keptSegs, subSegs), reach = clearance(mainSegs, subSegs);
  const flags = [];
  if (reach !== null && reach > detach) flags.push('detached');
  if (newPieces >= 1) flags.push('fragmented');
  if (stubs.length) flags.push('stub');
  if (erasedPct > heavyCut) flags.push('heavy_cut');
  if (removed) flags.push('erased_whole_piece');
  // A drawn part of the main mostly erased (the jar's lip, the bike's saddle): the main loses a part its meaning
  // needs, even when the whole cut stays under heavy_cut and the part was joined to the rest.
  if (lostParts.length) flags.push('lost_part');
  // A feature of the main mostly erased (the cart's handle, a kettle's spout) while its element keeps most of its ink.
  if (lostFeatures.length) flags.push('lost_feature');
  // The sub's ink never reaches the main, yet the cut margin (about 4 units past the sub) shaved the main's edge:
  // the main looks broken for no visible reason (CCPA over a map's peaks, a camera under a cloud). Move the main
  // clear (reach about 4, nothing erased) or into the sub (a real overlap). Any reach inside the 4-unit margin nicks
  // the main, even when the nick rounds to 0 % erased (a speck off a bell's shoulder still looks broken).
  if (reach !== null && reach > 0 && (reach < shaveReach || erasedPct >= shaveMin)) flags.push('shaved');
  // The main surrounds the sub (the hierarchy inside the head, the remote in the house's doorway): that is a container
  // combination. A side pair keeps the sub at its corner or side, beside the main or cutting into its edge.
  if (insidePct >= container) flags.push('container');
  const penalty = (flags.includes('detached') ? 10 + 2 * (reach - detach) : 0) + 8 * Math.max(0, newPieces) + 10 * stubs.length
    + 12 * Math.max(removed, lostParts.length) + 12 * lostFeatures.length + Math.max(0, erasedPct - heavyCut) + (flags.includes('shaved') ? 6 + erasedPct : 0)
    + (flags.includes('container') ? 20 : 0);

  return {
    // How much of the main is left to read beside the sub: kept main ink over sub ink (the main should stay the
    // larger shape; near or below 1 the sub takes over the icon).
    main_to_sub: subPx ? +(keptPx / subPx).toFixed(2) : null,
    erased_pct: +erasedPct.toFixed(1), overlap_pct: +(subPx ? 100 * subOnMain / subPx : 0).toFixed(1),
    gap, reach, inside_pct: +insidePct.toFixed(1),
    // Closed outlines of the main the sub opened (a frame cut open): normal for a knockout, reported for context.
    opened: Math.max(0, holes(main, n) - holes(kept, n)),
    fragments: {before: before.pieces.length, after: after.pieces.length, new: newPieces, removed, stubs: stubs.length,
                pieces: keptPieces.filter(p => p.cut)},
    // The main's drawn elements the sub cut into (erased_pct > 0); `lost` names those at or over --lost-part percent.
    parts: {cut: parts.filter(p => p.erased_pct > 0), lost: lostParts.map(p => p.name)},
    // Features (turn-split runs of one element) at least --feature-min long that the cut erased --lost-feature % or more.
    lost_features: lostFeatures,
    flags, penalty: +penalty.toFixed(1),
    masks: {n, main, sub, kept, stubs: stubs.map(s => s), labels: after.labels, keptPieces},
  };
}

// overlap.png: kept main black, erased main red, sub blue (over everything), stub pieces orange.
export function overlay(analysis, file) {
  const {n, main, sub, kept, labels, keptPieces} = analysis.masks;
  const stubLabels = new Set(keptPieces.map((p, i) => (p.cut && analysis.fragments.pieces.includes(p) && p.length < (analysis.minPiece ?? DEFAULTS.minPiece)) ? i + 1 : 0).filter(Boolean));
  const rgb = Buffer.alloc(n * n * 3, 255);
  for (let i = 0; i < n * n; i++) {
    let c = null;
    if (main[i] && !kept[i]) c = [230, 60, 50];
    if (kept[i]) c = stubLabels.has(labels[i]) ? [245, 150, 20] : [20, 20, 20];
    if (sub[i]) c = kept[i] || main[i] ? [40, 90, 230] : [70, 130, 240];
    if (c) rgb.set(c, i * 3);
  }
  const ppm = Buffer.concat([Buffer.from(`P6\n${n} ${n}\n255\n`), rgb]);
  // Through a file, not stdin: magick now and then waited on a piped image forever and hung a whole batch.
  const raw = file + '.ppm';
  try {
    writeFileSync(raw, ppm);
    execFileSync('magick', [raw, file], {timeout: 30000});
    return file;
  } catch { return null; } finally { rmSync(raw, {force: true}); }
}

// The work folder's current proposal (layout.json), measured.
export function analyzeDir(dir, limits = {}, picture = 'overlap.png') {
  const layout = readJSON(path.join(dir, 'layout.json'));
  const composed = compose(dir, layout);
  const analysis = analyze(composed, layoutFor(dir, layout), limits);
  analysis.minPiece = limits.minPiece ?? DEFAULTS.minPiece;
  analysis.overlay = overlay(analysis, path.join(dir, picture));
  return analysis;
}
export const summary = a => ({main_to_sub: a.main_to_sub, erased_pct: a.erased_pct, overlap_pct: a.overlap_pct, gap: a.gap, reach: a.reach, inside_pct: a.inside_pct, opened: a.opened,
                              fragments: a.fragments, parts: a.parts, lost_features: a.lost_features, flags: a.flags, penalty: a.penalty, overlay: a.overlay});

if (process.argv[1] && path.resolve(process.argv[1]) === new URL(import.meta.url).pathname) {
  const args = process.argv.slice(2), dir = args.find(a => !a.startsWith('--'));
  const value = name => { const i = args.indexOf('--' + name); return i >= 0 ? Number(args[i + 1]) : undefined; };
  if (!dir) { console.error('usage: side_overlap.mjs <DIR> [--min-piece 6] [--detach 4.5] [--heavy-cut 30] [--shave-reach 4] [--lost-part 40] [--container 80]'); process.exit(1); }
  try {
    const limits = Object.fromEntries([['minPiece', value('min-piece')], ['detach', value('detach')], ['heavyCut', value('heavy-cut')], ['shaveMin', value('shave-min')], ['shaveReach', value('shave-reach')], ['lostPart', value('lost-part')], ['container', value('container')]]
      .filter(([, v]) => v !== undefined && Number.isFinite(v)));
    console.log(JSON.stringify(summary(analyzeDir(path.resolve(dir), limits)), null, 2));
  } catch (e) { console.error('error: ' + e.message); process.exit(1); }
}
