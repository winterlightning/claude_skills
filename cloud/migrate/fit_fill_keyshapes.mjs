#!/usr/bin/env node
// Lay out again every fill side pair pick whose combined box misses the 64px keyshapes (a 56 square, 60×44, 44×60,
// ±1px; measured as the pages measure it: the parts' boxes plus the 4px stroke, side-fill-overlay.js), keeping its
// balance: the pick's two parts are scaled together (the sub:main size ratio stays) and moved apart, never stretched.
//   a stack (top / bottom, left / right): scaled so the wider part spans the keyshape's short side, the parts pushed
//   to the ends of its long side (they may overlap no more than they did);
//   a corner pair: the parts moved out to their corners of the square, sizes kept.
// Each layout is checked with the pages' own preview (side-fill-layout.js: canvas, stroke envelope, combine) and
// must read like the pick it replaces: the sub cuts no more than 4% more of the main away, and the parts sit no
// more than 4px further apart (a sub that touched the main still does), and the sub stays on the same side of the
// main on each axis (left / level / right, above / level / below): the composition does not change. Writes icon_set/data/side-fill/data/keyshape-fit-layouts.json ({pair: {rank: {main, sub, keyshape}}}),
// which `side-fill d1-import` applies to the picks; pairs it cannot fit are listed for a hand layout.
//
//   node cloud/migrate/fit_fill_keyshapes.mjs --base-url http://localhost:8821        # reads the picks (keyset pages)
//   … --size 72      the 72 pairs, against the keyshapes the site's Side combination 72 icons use (a 64 square 4..68,
//                    68×54 and 54×68, and the _M 68×50 / 50×68), into icon_set/data/side-fill-72/keyshape-fit-layouts.json
//                    (applied by `side-fill d1-import72`). A pick laid out larger than its keyshape is first scaled down
//                    whole, both parts together, as it reads.
import {createRequire} from 'node:module';
import {parseArgs} from 'node:util';
import {readFileSync, writeFileSync} from 'node:fs';

const require = createRequire(import.meta.url);
const Layout = require('../../icon_set/scripts/templates/side-fill-layout.js');
const Fill = require('../../icon_set/scripts/templates/side-fill-combine.js');
const I = Fill.internals;
const OUTS = {64: new URL('../../icon_set/data/side-fill/data/keyshape-fit-layouts.json', import.meta.url),
              72: new URL('../../icon_set/data/side-fill-72/keyshape-fit-layouts.json', import.meta.url)};
// The contract's SOLO48 / SUB32 keyshapes as centerline bounds, as the pages read them (side-fill-data.js keyshapes).
const LAB = JSON.parse(readFileSync(new URL('../../published/gallery/laboratory.json', import.meta.url)));
const {values: args} = parseArgs({options: {'base-url': {type: 'string'}, ids: {type: 'string'}, size: {type: 'string', default: '64'},
  // How far a refit may move from the pick (defaults: the strict pass). A wider pass is for a person to review.
  'max-cut': {type: 'string', default: '0.04'}, 'max-gap': {type: 'string', default: '4'}, balance: {type: 'string', default: '0.8-1.3'},
  // --search: for the picks no stack or corner fits, every main and sub size (×0.7–1.25) with each part anchored in its
  // corner of each keyshape, the least changed first; a drawing the page cannot split (transforms, element numbers
  // that no longer match it) moves whole. For a person to review, like a wider pass.
  search: {type: 'boolean'},
  // --any-side: no same-side check (the sub may sit level instead of beside the main): only with a person's review.
  'any-side': {type: 'boolean'},
  out: {type: 'string'}}});
const MAX_CUT = Number(args['max-cut']), MAX_GAP = Number(args['max-gap']);
const SIZE = Number(args.size);
if (SIZE !== 64 && SIZE !== 72) { console.error('error: --size is 64 or 72'); process.exit(2); }
const OUT = OUTS[SIZE];
// The parts' own keyshapes for the preview's checks: the contract's SOLO48 / SUB32, and at 72 the same ×72/64 (54 / 36).
const KEYSHAPE_TABLE = Object.fromEntries([['main', 'SOLO48'], ['sub', 'SUB32']].map(([role, profile]) => [role, Object.fromEntries(
  Object.entries(LAB.keyshapes.resolved[profile]).map(([n, k]) => [n, k.centerline_bounds]).filter(([, b]) => Array.isArray(b))
    .map(([n, b]) => [n, b.map(v => v * SIZE / 64)]))]));
const [BALANCE_LO, BALANCE_HI] = args.balance.split('-').map(Number);
const base = (args['base-url'] || '').replace(/\/$/, '');
if (!base) { console.error('error: --base-url is required'); process.exit(2); }
const headers = {'User-Agent': 'pictographic-migrate/1.0'};
// A connection the server closed while this was busy combining is reset: such a request is tried again.
const get = async (path, tries = 3) => {
  let response;
  try { response = await fetch(base + path, {headers}); }
  catch (error) { if (tries > 1) return get(path, tries - 1); throw error; }
  if (!response.ok) throw new Error(`GET ${path} → ${response.status}`);
  return response.json();
};

// Painted keyshapes and the centerline boxes they mean (2px in: half the 4px stroke). At 72 they are the ones the
// site's Side combination 72 icons carry (keyshape, keyshape_bounds); side-fill-overlay.js draws the same.
const KEYSHAPES = SIZE === 72
  ? {SQUARE: [4, 4, 68, 68], HRECT: [2, 9, 70, 63], VRECT: [9, 2, 63, 70], HRECT_M: [2, 11, 70, 61], VRECT_M: [11, 2, 61, 70]}
  : {SQUARE: [4, 4, 60, 60], HRECT: [2, 10, 62, 54], VRECT: [10, 2, 54, 62]};
const inner = name => KEYSHAPES[name].map((v, i) => i < 2 ? v + 2 : v - 2);     // its centerline box
const box = layout => [Math.min(...layout.map(b => b.x)), Math.min(...layout.map(b => b.y)),
                       Math.max(...layout.map(b => b.x + b.w)), Math.max(...layout.map(b => b.y + b.h))];
const union = (a, b) => [Math.min(a[0], b[0]), Math.min(a[1], b[1]), Math.max(a[2], b[2]), Math.max(a[3], b[3])];
const unionBox = layout => { const [x0, y0, x1, y1] = box(layout);return {x: x0, y: y0, w: x1 - x0, h: y1 - y0}; };
function measure(main, sub) {
  const u = union(box(main), box(sub)), painted = [u[0] - 2, u[1] - 2, u[2] + 2, u[3] + 2];
  let best = null;
  for (const [name, k] of Object.entries(KEYSHAPES)) {
    const off = Math.max(...k.map((v, i) => Math.abs(v - painted[i])));
    if (!best || off < best.off) best = {name, off};
  }
  return {...best, ok: best.off <= 1, painted};
}
// A part's boxes scaled by k about its own box's corner, then moved so that box starts at (x, y): whole grid units.
function place(layout, k, x, y) {
  const [x0, y0] = box(layout);
  return layout.map(b => ({...b, x: Math.round(x + (b.x - x0) * k), y: Math.round(y + (b.y - y0) * k),
                           // A straight line's box is 0 across: it stays 0 (the stroke gives it its width).
                           w: b.w ? Math.max(1, Math.round(b.w * k)) : 0, h: b.h ? Math.max(1, Math.round(b.h * k)) : 0}));
}
const size = layout => { const b = box(layout);return [b[2] - b[0], b[3] - b[1]]; };

// Candidate layouts for one pick, most like the pick first.
function candidates(position, main, sub) {
  const out = [];
  const [mw, mh] = size(main), [sw, sh] = size(sub);
  const vertical = position === 'to' || position === 'bo', horizontal = position === 'le' || position === 'ri';
  // At 72: the whole pick scaled together (never stretched) to fill the keyshape nearest its own proportions, its
  // composition kept: most 72 picks were laid out 4px larger than the 64 square (the 72 set's 2px canvas inset).
  // Up to ×1.15 up for a pick a little short of filling it; centred across the side it does not span.
  if (SIZE === 72) {
    const u = union(box(main), box(sub)), uw = u[2] - u[0], uh = u[3] - u[1];
    const ranked = Object.keys(KEYSHAPES).map(name => { const [x0, y0, x1, y1] = inner(name);
      const k = Math.min((x1 - x0) / uw, (y1 - y0) / uh);
      return {name, k, box: [x0, y0, x1, y1], fit: Math.abs(Math.log(((x1 - x0) / (y1 - y0)) / (uw / uh)))}; })
      .filter(c => c.k <= 1.15).sort((a, b) => a.fit - b.fit);
    for (const {name, k, box: [x0, y0, x1, y1]} of ranked) {
      const ox = x0 + (x1 - x0 - uw * k) / 2, oy = y0 + (y1 - y0 - uh * k) / 2;
      const at = layout => { const b = box(layout);return [ox + (b[0] - u[0]) * k, oy + (b[1] - u[1]) * k]; };
      out.push({target: name, main: place(main, k, ...at(main)), sub: place(sub, k, ...at(sub))});
    }
  }
  if (vertical || horizontal) {
    // The stack's short side: the keyshape rect's centerline across (40 for a 44 rect at 64), its long side along
    // (56 at 64), both read from the keyshape (KEYSHAPES).
    const target = vertical ? 'VRECT' : 'HRECT';
    const [tx0, ty0, tx1, ty1] = inner(target);
    const SHORT = vertical ? tx1 - tx0 : ty1 - ty0, LONG = vertical ? ty1 - ty0 : tx1 - tx0;
    const START = vertical ? ty0 : tx0, ACROSS = vertical ? tx0 : ty0;
    const across = Math.max(vertical ? mw : mh, vertical ? sw : sh);
    const k = SHORT / across;
    const first = position === 'to' || position === 'le' ? 'sub' : 'main';
    const dims = {main: [mw * k, mh * k], sub: [sw * k, sh * k]};
    const along = r => vertical ? dims[r][1] : dims[r][0];
    const overlapBefore = vertical ? Math.max(0, Math.min(box(main)[3], box(sub)[3]) - Math.max(box(main)[1], box(sub)[1]))
                                   : Math.max(0, Math.min(box(main)[2], box(sub)[2]) - Math.max(box(main)[0], box(sub)[0]));
    if (along('main') + along('sub') - LONG <= overlapBefore * k + 0.5) {
      const second = first === 'sub' ? 'main' : 'sub';
      const at = {[first]: START, [second]: START + LONG - along(second)};
      const layout = {};
      for (const role of ['main', 'sub']) {
        const centred = ACROSS + (SHORT - (vertical ? dims[role][0] : dims[role][1])) / 2;
        layout[role] = vertical ? place(role === 'main' ? main : sub, k, centred, at[role]) : place(role === 'main' ? main : sub, k, at[role], centred);
      }
      out.push({target, ...layout});
    }
  }
  if (vertical || horizontal) {
    // stack64's sizing: one part spans the short side, the other fills the rest of the long side after a gap. The
    // parts are sized apart, so the balance moves: kept only while the sub:main size ratio stays 0.8–1.3 of the pick's.
    const target = vertical ? 'VRECT' : 'HRECT';
    const [tx0, ty0, tx1, ty1] = inner(target);
    const SHORT = vertical ? tx1 - tx0 : ty1 - ty0, LONG = vertical ? ty1 - ty0 : tx1 - tx0;
    const START = vertical ? ty0 : tx0, ACROSS = vertical ? tx0 : ty0;
    const first = position === 'to' || position === 'le' ? 'sub' : 'main';
    const second = first === 'sub' ? 'main' : 'sub';
    const own = {main: [mw, mh], sub: [sw, sh]}, layouts = {main, sub};
    const tried = [];
    for (const gap of [10, 12, 8, 6, 4, 2, 0, -4, -8]) {
      for (const wide of ['main', 'sub']) {
        const other = wide === 'main' ? 'sub' : 'main';
        const kw = SHORT / (vertical ? own[wide][0] : own[wide][1]);
        const rest = LONG - gap - (vertical ? own[wide][1] : own[wide][0]) * kw;
        const ko = rest / (vertical ? own[other][1] : own[other][0]);
        if (!(rest >= 12) || (vertical ? own[other][0] : own[other][1]) * ko > SHORT + .5) continue;
        const k = {[wide]: kw, [other]: ko};
        const q = k.sub / k.main;
        if (q < BALANCE_LO || q > BALANCE_HI) continue;
        tried.push({gap, k, q});
      }
    }
    tried.sort((a, b) => Math.abs(Math.log(a.q)) - Math.abs(Math.log(b.q)));
    for (const {gap, k} of tried) {
      const along = r => (vertical ? own[r][1] : own[r][0]) * k[r];
      const at = {[first]: START, [second]: START + along(first) + gap};
      const layout = {};
      for (const role of ['main', 'sub']) {
        const centred = ACROSS + (SHORT - (vertical ? own[role][0] : own[role][1]) * k[role]) / 2;
        layout[role] = vertical ? place(layouts[role], k[role], centred, at[role]) : place(layouts[role], k[role], at[role], centred);
      }
      out.push({target, ...layout});
    }
  }
  // Corners (and a stack that could not be scaled): sizes kept, each part pushed to its side of the nearest keyshape.
  const anchors = {br: [[0, 0], [1, 1]], tr: [[0, 1], [1, 0]], bl: [[1, 0], [0, 1]], tl: [[1, 1], [0, 0]],
                   ri: [[0, .5], [1, .5]], le: [[1, .5], [0, .5]], to: [[.5, 1], [.5, 0]], bo: [[.5, 0], [.5, 1]]}[position];
  for (const target of anchors ? Object.keys(KEYSHAPES) : []) {
    const [x0, y0, x1, y1] = inner(target);
    const layout = {};
    for (const [role, [ax, ay]] of [['main', anchors[0]], ['sub', anchors[1]]]) {
      const [w, h] = role === 'main' ? [mw, mh] : [sw, sh];
      layout[role] = place(role === 'main' ? main : sub, 1, x0 + (x1 - x0 - w) * ax, y0 + (y1 - y0 - h) * ay);
    }
    out.push({target, ...layout});
  }
  return out;
}

// --search candidates: each part anchored in its corner of a keyshape at a size of its own, least changed first.
const CORNERS = {br: [[0, 0], [1, 1]], tr: [[0, 1], [1, 0]], bl: [[1, 0], [0, 1]], tl: [[1, 1], [0, 0]],
                 ri: [[0, .5], [1, .5]], le: [[1, .5], [0, .5]], to: [[.5, 1], [.5, 0]], bo: [[.5, 0], [.5, 1]]};
function searchCandidates(position, main, sub) {
  const anchors = CORNERS[position] || [[0, 0], [1, 1]];
  const [mw, mh] = size(main), [sw, sh] = size(sub), out = [];
  for (const target of Object.keys(KEYSHAPES)) {
    const [x0, y0, x1, y1] = inner(target), W = x1 - x0, H = y1 - y0;
    for (let km = 0.7; km <= 1.25; km += 0.02) for (let ks = 0.7; ks <= 1.3; ks += 0.025) {
      if (mw * km > W + .5 || mh * km > H + .5 || sw * ks > W + .5 || sh * ks > H + .5) continue;
      const m = place(main, km, x0 + (W - mw * km) * anchors[0][0], y0 + (H - mh * km) * anchors[0][1]);
      const s = place(sub, ks, x0 + (W - sw * ks) * anchors[1][0], y0 + (H - sh * ks) * anchors[1][1]);
      if (!measure(m, s).ok) continue;
      out.push({target, main: m, sub: s, score: Math.abs(Math.log(km)) + Math.abs(Math.log(ks)) + 2 * Math.abs(Math.log(ks / km))});
    }
  }
  return out.sort((a, b) => a.score - b.score).slice(0, 80);
}

const keyshapes = KEYSHAPE_TABLE;
const wanted = args.ids ? new Set(args.ids.split(',')) : null;
const result = {}, unfit = [];
let checked = 0, off = 0;
for (let after = null; ;) {
  const page = await get('/api/side-fill/pairs?' + new URLSearchParams({state: 'picked', limit: '120', size: String(SIZE), ...(after ? {after} : {})}));
  const jobs = [];
  for (const pair of page.pairs) {
    if (wanted && !wanted.has(pair.id)) continue;
    for (const pick of pair.picks) {
      if (!pick.main?.layout || !pick.sub?.layout) continue;
      checked++;
      if (measure(pick.main.layout, pick.sub.layout).ok) continue;
      off++;
      jobs.push({pair, pick});
    }
  }
  if (jobs.length) {
    const keys = [...new Set(jobs.flatMap(({pair, pick}) => [pick.main.icon, pick.sub.icon, pair.main, pair.sub]))];
    const drawings = {};
    for (let i = 0; i < keys.length; i += 100) Object.assign(drawings, await get('/api/combinations/drawings?keys=' + encodeURIComponent(keys.slice(i, i + 100).join(','))));
    for (const {pair, pick} of jobs) {
      const part = (role, source) => ({svg: drawings[pick[role].icon].svg, source: drawings[source].svg, outline: pick[role].icon === source});
      // A single box without element numbers takes them all (side-fill-data.js units), as the pages place it.
      const units = (layout, source) => layout.length === 1 && !layout[0].paths
        ? [{...layout[0], paths: Layout.elements(drawings[source].svg).sources.map((b, i) => b ? i : null).filter(i => i !== null)}] : layout;
      let mainUnits, subUnits, whole = false;
      try { mainUnits = units(pick.main.layout, pair.main); subUnits = units(pick.sub.layout, pair.sub); }
      catch (error) {
        // A drawing with transforms cannot be split into elements: its pick is laid out by hand on its pair page, or
        // with --search moved whole (its boxes as they are; the page places such a drawing whole in them).
        if (!args.search) {
          unfit.push({id: pair.id, rank: pick.rank, concept: pair.concept, measured: measure(pick.main.layout, pick.sub.layout).painted, why: error.message});
          continue;
        }
        mainUnits = pick.main.layout; subUnits = pick.sub.layout; whole = true;
      }
      // Element numbers that no longer match the drawing (it was redrawn): with --search one box over all of it.
      const allOf = (layout, source) => [{...unionBox(layout), paths: Layout.elements(drawings[source].svg).sources.map((b, i) => b ? i : null).filter(i => i !== null)}];
      if (args.search && !whole) {
        for (const [role, source] of [['main', pair.main], ['sub', pair.sub]]) {
          const listed = (role === 'main' ? mainUnits : subUnits).flatMap(u => u.paths || []).sort((a, b) => a - b);
          let drawable;
          try { drawable = Layout.elements(drawings[source].svg).sources.map((b, i) => b ? i : null).filter(i => i !== null); }
          catch { whole = true; break; }
          if (listed.length !== drawable.length || listed.some((v, i) => v !== drawable[i])) {
            if (role === 'main') mainUnits = allOf(mainUnits, source); else subUnits = allOf(subUnits, source);
          }
        }
      }
      // What the sub cuts from the main, and how far apart the parts are.
      const reading = (mainLayout, subLayout) => {
        const r = Fill.combine({main: {...part('main', pair.main), layout: mainLayout}, sub: {...part('sub', pair.sub), layout: subLayout}, options: pick.options, size: SIZE});
        const placed = I.area(r.main.placed);
        return {cut: placed ? 1 - r.main.area / placed : 0, gap: I.distance(r.main.placed, r.sub.geometry) ?? 0};
      };
      const before = reading(mainUnits, subUnits);
      // Where the sub sits against the main on each axis: -1, 0 (within 4px of level) or 1.
      const side = (m, s) => { const a = box(m), b = box(s);
        return [0, 1].map(i => { const d = (b[i] + b[i + 2]) / 2 - (a[i] + a[i + 2]) / 2;return Math.abs(d) < 4 ? 0 : Math.sign(d); }); };
      const sideBefore = side(mainUnits, subUnits);
      let kept = null, why = 'no candidate';
      const tries = args.search ? [...candidates(pair.id.slice(-2), mainUnits, subUnits), ...searchCandidates(pair.id.slice(-2), mainUnits, subUnits)]
        : candidates(pair.id.slice(-2), mainUnits, subUnits);
      for (const c of tries) {
        const m = measure(c.main, c.sub);
        if (!m.ok) { why = `candidate measures ${m.painted.join(',')}`; if (process.env.DEBUG) console.log(c.target, why); continue; }
        try {
          if (whole) {
            // Not splittable: combined as the page will combine it, held to the canvas.
            const r = Fill.combine({main: {...part('main', pair.main), layout: c.main}, sub: {...part('sub', pair.sub), layout: c.sub}, options: pick.options, size: SIZE});
            const b = I.bounds(r.geometry);
            if (!b || b.some(v => v < -.01 || v > SIZE + .01)) throw new Error('ink outside the canvas');
          } else {
            Layout.preview({keyshapes, position: pair.id.slice(-2), options: pick.options, size: SIZE, main: part('main', pair.main), sub: part('sub', pair.sub),
                            proposal: {main: {units: c.main}, sub: {units: c.sub}}});
          }
          const after = reading(c.main, c.sub);
          if (after.cut > before.cut + MAX_CUT) throw new Error(`cuts ${Math.round(after.cut * 100)}% of the main away (now ${Math.round(before.cut * 100)}%)`);
          const sideAfter = side(c.main, c.sub);
          if (!args['any-side'] && sideAfter.some((v, i) => v !== sideBefore[i])) throw new Error(`the sub moves to another side of the main (${sideBefore} → ${sideAfter})`);
          if (after.gap > before.gap + MAX_GAP) throw new Error(`parts drift apart (${after.gap.toFixed(1)}px, now ${before.gap.toFixed(1)}px)`);
          kept = {main: c.main, sub: c.sub, keyshape: m.name};
          break;
        } catch (error) { why = error.message; if (process.env.DEBUG) console.log(c.target, why); }
      }
      if (kept) (result[pair.id] ||= {})[pick.rank] = kept;
      else unfit.push({id: pair.id, rank: pick.rank, concept: pair.concept, measured: measure(pick.main.layout, pick.sub.layout).painted, why});
    }
  }
  if (!page.next) break;
  after = page.next;
}
// Picks fitted before keep their layouts (they are on the keyshape now, so this run does not see them again).
const target = args.out ? new URL(args.out, `file://${process.cwd()}/`) : OUT;
let earlier = {};
try { earlier = JSON.parse(readFileSync(OUT)).pairs || {}; } catch { /* first run */ }
const merged = {...earlier};
for (const [id, ranks] of Object.entries(result)) merged[id] = {...(merged[id] || {}), ...ranks};
writeFileSync(target, JSON.stringify({schema: 'side-fill-keyshape-fit/v1', pairs: args.out ? result : merged, unfit}, null, 1) + '\n');
const fitted = Object.values(result).reduce((n, ranks) => n + Object.keys(ranks).length, 0);
console.log(`${checked} picks checked; ${off} off keyshape; ${fitted} laid out again; ${unfit.length} left for a hand layout`);
for (const u of unfit.slice(0, 15)) console.log(`  ${u.id} #${u.rank} ${u.concept}: ${u.why}`);
