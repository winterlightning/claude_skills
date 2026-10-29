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
import {createRequire} from 'node:module';
import {parseArgs} from 'node:util';
import {readFileSync, writeFileSync} from 'node:fs';

const require = createRequire(import.meta.url);
const Layout = require('../../icon_set/scripts/templates/side-fill-layout.js');
const Fill = require('../../icon_set/scripts/templates/side-fill-combine.js');
const I = Fill.internals;
const OUT = new URL('../../icon_set/data/side-fill/data/keyshape-fit-layouts.json', import.meta.url);
const KEYSHAPES_FILE = new URL('../../icon_set/data/side-fill/data/side-keyshapes.json', import.meta.url);
const {values: args} = parseArgs({options: {'base-url': {type: 'string'}, ids: {type: 'string'}}});
const base = (args['base-url'] || '').replace(/\/$/, '');
if (!base) { console.error('error: --base-url is required'); process.exit(2); }
const headers = {'User-Agent': 'pictographic-migrate/1.0'};
const get = async path => {
  const response = await fetch(base + path, {headers});
  if (!response.ok) throw new Error(`GET ${path} → ${response.status}`);
  return response.json();
};

// Painted keyshapes and the centerline boxes they mean (2px in: half the 4px stroke).
const KEYSHAPES = {SQUARE: [4, 4, 60, 60], HRECT: [2, 10, 62, 54], VRECT: [10, 2, 54, 62]};
const box = layout => [Math.min(...layout.map(b => b.x)), Math.min(...layout.map(b => b.y)),
                       Math.max(...layout.map(b => b.x + b.w)), Math.max(...layout.map(b => b.y + b.h))];
const union = (a, b) => [Math.min(a[0], b[0]), Math.min(a[1], b[1]), Math.max(a[2], b[2]), Math.max(a[3], b[3])];
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
  if (vertical || horizontal) {
    // The stack's short side: 40 (centerline 12..52) for a 44 rect, its long side 56 (4..60).
    const target = vertical ? 'VRECT' : 'HRECT';
    const across = Math.max(vertical ? mw : mh, vertical ? sw : sh);
    const k = 40 / across;
    const first = position === 'to' || position === 'le' ? 'sub' : 'main';
    const dims = {main: [mw * k, mh * k], sub: [sw * k, sh * k]};
    const along = r => vertical ? dims[r][1] : dims[r][0];
    const overlapBefore = vertical ? Math.max(0, Math.min(box(main)[3], box(sub)[3]) - Math.max(box(main)[1], box(sub)[1]))
                                   : Math.max(0, Math.min(box(main)[2], box(sub)[2]) - Math.max(box(main)[0], box(sub)[0]));
    if (along('main') + along('sub') - 56 <= overlapBefore * k + 0.5) {
      const second = first === 'sub' ? 'main' : 'sub';
      const at = {[first]: 4, [second]: 60 - along(second)};
      const layout = {};
      for (const role of ['main', 'sub']) {
        const centred = 12 + (40 - (vertical ? dims[role][0] : dims[role][1])) / 2;
        layout[role] = vertical ? place(role === 'main' ? main : sub, k, centred, at[role]) : place(role === 'main' ? main : sub, k, at[role], centred);
      }
      out.push({target, ...layout});
    }
  }
  if (vertical || horizontal) {
    // stack64's sizing: one part spans the short side, the other fills the rest of the long side after a gap. The
    // parts are sized apart, so the balance moves: kept only while the sub:main size ratio stays 0.8–1.3 of the pick's.
    const target = vertical ? 'VRECT' : 'HRECT';
    const first = position === 'to' || position === 'le' ? 'sub' : 'main';
    const second = first === 'sub' ? 'main' : 'sub';
    const own = {main: [mw, mh], sub: [sw, sh]}, layouts = {main, sub};
    const tried = [];
    for (const gap of [10, 12, 8, 6, 4, 2, 0, -4, -8]) {
      for (const wide of ['main', 'sub']) {
        const other = wide === 'main' ? 'sub' : 'main';
        const kw = 40 / (vertical ? own[wide][0] : own[wide][1]);
        const rest = 56 - gap - (vertical ? own[wide][1] : own[wide][0]) * kw;
        const ko = rest / (vertical ? own[other][1] : own[other][0]);
        if (!(rest >= 12) || (vertical ? own[other][0] : own[other][1]) * ko > 40.5) continue;
        const k = {[wide]: kw, [other]: ko};
        const q = k.sub / k.main;
        if (q < 0.8 || q > 1.3) continue;
        tried.push({gap, k, q});
      }
    }
    tried.sort((a, b) => Math.abs(Math.log(a.q)) - Math.abs(Math.log(b.q)));
    for (const {gap, k} of tried) {
      const along = r => (vertical ? own[r][1] : own[r][0]) * k[r];
      const at = {[first]: 4, [second]: 4 + along(first) + gap};
      const layout = {};
      for (const role of ['main', 'sub']) {
        const centred = 12 + (40 - (vertical ? own[role][0] : own[role][1]) * k[role]) / 2;
        layout[role] = vertical ? place(layouts[role], k[role], centred, at[role]) : place(layouts[role], k[role], at[role], centred);
      }
      out.push({target, ...layout});
    }
  }
  // Corners (and a stack that could not be scaled): sizes kept, each part pushed to its side of the nearest keyshape.
  const anchors = {br: [[0, 0], [1, 1]], tr: [[0, 1], [1, 0]], bl: [[1, 0], [0, 1]], tl: [[1, 1], [0, 0]],
                   ri: [[0, .5], [1, .5]], le: [[1, .5], [0, .5]], to: [[.5, 1], [.5, 0]], bo: [[.5, 0], [.5, 1]]}[position];
  for (const target of ['SQUARE', 'HRECT', 'VRECT']) {
    const [x0, y0, x1, y1] = KEYSHAPES[target].map((v, i) => i < 2 ? v + 2 : v - 2);
    const layout = {};
    for (const [role, [ax, ay]] of [['main', anchors[0]], ['sub', anchors[1]]]) {
      const [w, h] = role === 'main' ? [mw, mh] : [sw, sh];
      layout[role] = place(role === 'main' ? main : sub, 1, x0 + (x1 - x0 - w) * ax, y0 + (y1 - y0 - h) * ay);
    }
    out.push({target, ...layout});
  }
  return out;
}

const keyshapes = JSON.parse(readFileSync(KEYSHAPES_FILE));
const wanted = args.ids ? new Set(args.ids.split(',')) : null;
const result = {}, unfit = [];
let checked = 0, off = 0;
for (let after = null; ;) {
  const page = await get('/api/side-fill/pairs?' + new URLSearchParams({state: 'picked', limit: '120', ...(after ? {after} : {})}));
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
      const mainUnits = units(pick.main.layout, pair.main), subUnits = units(pick.sub.layout, pair.sub);
      // What the sub cuts from the main, and how far apart the parts are.
      const reading = (mainLayout, subLayout) => {
        const r = Fill.combine({main: {...part('main', pair.main), layout: mainLayout}, sub: {...part('sub', pair.sub), layout: subLayout}, options: pick.options});
        const placed = I.area(r.main.placed);
        return {cut: placed ? 1 - r.main.area / placed : 0, gap: I.distance(r.main.placed, r.sub.geometry) ?? 0};
      };
      const before = reading(mainUnits, subUnits);
      // Where the sub sits against the main on each axis: -1, 0 (within 4px of level) or 1.
      const side = (m, s) => { const a = box(m), b = box(s);
        return [0, 1].map(i => { const d = (b[i] + b[i + 2]) / 2 - (a[i] + a[i + 2]) / 2;return Math.abs(d) < 4 ? 0 : Math.sign(d); }); };
      const sideBefore = side(mainUnits, subUnits);
      let kept = null, why = 'no candidate';
      for (const c of candidates(pair.id.slice(-2), mainUnits, subUnits)) {
        const m = measure(c.main, c.sub);
        if (!m.ok) { why = `candidate measures ${m.painted.join(',')}`; if (process.env.DEBUG) console.log(c.target, why); continue; }
        try {
          Layout.preview({keyshapes, position: pair.id.slice(-2), options: pick.options, main: part('main', pair.main), sub: part('sub', pair.sub),
                          proposal: {main: {units: c.main}, sub: {units: c.sub}}});
          const after = reading(c.main, c.sub);
          if (after.cut > before.cut + 0.04) throw new Error(`cuts ${Math.round(after.cut * 100)}% of the main away (now ${Math.round(before.cut * 100)}%)`);
          const sideAfter = side(c.main, c.sub);
          if (sideAfter.some((v, i) => v !== sideBefore[i])) throw new Error(`the sub moves to another side of the main (${sideBefore} → ${sideAfter})`);
          if (after.gap > before.gap + 4) throw new Error(`parts drift apart (${after.gap.toFixed(1)}px, now ${before.gap.toFixed(1)}px)`);
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
writeFileSync(OUT, JSON.stringify({schema: 'side-fill-keyshape-fit/v1', pairs: result, unfit}, null, 1) + '\n');
const fitted = Object.values(result).reduce((n, ranks) => n + Object.keys(ranks).length, 0);
console.log(`${checked} picks checked; ${off} off keyshape; ${fitted} laid out again; ${unfit.length} left for a hand layout`);
for (const u of unfit.slice(0, 15)) console.log(`  ${u.id} #${u.rank} ${u.concept}: ${u.why}`);
