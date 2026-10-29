#!/usr/bin/env node
// Give an output to the fill side pairs that use a part brought up to the site's drawing (`side-fill sources`,
// data/site-drawings.json) and have no pick yet, as a person would on the pair page: the main's current fill (else
// its outline) with the sub's fill (else its outline) on the pair's own placement, combined by the pages' engine,
// checked by the layout preview, then picked (POST /api/side-fill/pick) and built (POST /api/side-fill/build).
// A part redrawn after its pair was laid out has elements the layout does not number: it gets one box over the
// area its old boxes covered, at its own proportions, anchored to its side of the pair.
//
//   node cloud/migrate/pick_new_pairs.mjs --base-url http://localhost:8821 --cookie pictographic_session=…   # dry run
//   node cloud/migrate/pick_new_pairs.mjs --base-url … --cookie … --send
import {createRequire} from 'node:module';
import {parseArgs} from 'node:util';
import {readFileSync} from 'node:fs';

const require = createRequire(import.meta.url);
const Fill = require('../../icon_set/scripts/templates/side-fill-combine.js');
const Layout = require('../../icon_set/scripts/templates/side-fill-layout.js');
const SITE = JSON.parse(readFileSync(new URL('../../icon_set/data/side-fill/data/site-drawings.json', import.meta.url)));
// The contract's SOLO48 / SUB32 keyshapes as centerline bounds, as the pages read them (side-fill-data.js keyshapes).
const LAB = JSON.parse(readFileSync(new URL('../../published/gallery/laboratory.json', import.meta.url)));
const KEYSHAPE_TABLE = Object.fromEntries([['main', 'SOLO48'], ['sub', 'SUB32']].map(([role, profile]) => [role, Object.fromEntries(
  Object.entries(LAB.keyshapes.resolved[profile]).map(([n, k]) => [n, k.centerline_bounds]).filter(([, b]) => Array.isArray(b)))]));
const KEYSHAPES = KEYSHAPE_TABLE;
const {values: args} = parseArgs({options: {'base-url': {type: 'string'}, cookie: {type: 'string'}, send: {type: 'boolean'}}});
const base = (args['base-url'] || '').replace(/\/$/, '');
if (!base || (args.send && !args.cookie)) { console.error('error: --base-url is required, and --send needs --cookie (a signed-in session)'); process.exit(2); }
const headers = {'User-Agent': 'pictographic-migrate/1.0', 'Content-Type': 'application/json', ...(args.cookie ? {Cookie: args.cookie, Origin: base} : {})};
async function call(method, path, body) {
  const response = await fetch(base + path, {method, headers, body: body === undefined ? undefined : JSON.stringify(body)});
  const data = await response.json().catch(() => ({}));
  if (!response.ok) throw new Error(`${method} ${path} → ${response.status} ${data.error || ''}`);
  return data;
}

const box = layout => [Math.min(...layout.map(b => b.x)), Math.min(...layout.map(b => b.y)),
                       Math.max(...layout.map(b => b.x + b.w)), Math.max(...layout.map(b => b.y + b.h))];
const ANCHOR = {br: [1, 1], tr: [1, 0], bl: [0, 1], tl: [0, 0], ri: [1, .5], le: [0, .5], to: [.5, 0], bo: [.5, 1]};
// The part's boxes for its current drawing: the pair's own when they number its elements, else one box.
function units(role, layout, source, position) {
  const drawable = Layout.elements(source).sources.map((b, i) => b ? i : null).filter(i => i !== null);
  const listed = (layout || []).flatMap(u => u.paths || []).sort((a, b) => a - b);
  if (layout?.length === 1 && !layout[0].paths) return [{...layout[0], paths: drawable}];
  if (listed.length === drawable.length && listed.every((v, i) => v === drawable[i])) return layout;
  // Redrawn since laid out: the area the old boxes covered, the drawing at its own proportions inside it.
  const [x0, y0, x1, y1] = box(layout), bounds = Layout.sourceBounds(source);
  const k = Math.min((x1 - x0) / (bounds[2] - bounds[0]), (y1 - y0) / (bounds[3] - bounds[1]));
  const w = Math.round((bounds[2] - bounds[0]) * k), h = Math.round((bounds[3] - bounds[1]) * k);
  const [ax, ay] = role === 'main' ? ANCHOR[position].map(v => 1 - v) : ANCHOR[position];
  return [{paths: drawable, x: Math.round(x0 + (x1 - x0 - w) * ax), y: Math.round(y0 + (y1 - y0 - h) * ay), w, h}];
}

const sites = new Set(Object.keys(SITE));
const pairs = [];
for (const state of ['unpicked', 'uncombined']) {
  for (let after = null; ;) {
    const page = await call('GET', '/api/side-fill/pairs?' + new URLSearchParams({state, limit: '120', ...(after ? {after} : {})}));
    pairs.push(...page.pairs.filter(p => !p.picks.length && (sites.has(p.main) || sites.has(p.sub))));
    if (!page.next) break;
    after = page.next;
  }
}
let made = 0;
const skipped = [];
for (const listed of pairs) {
  const pair = await call('GET', '/api/side-fill/pair?id=' + encodeURIComponent(listed.id));
  if (!pair.main || !pair.sub || !pair.layout?.main || !pair.layout?.sub) { skipped.push(`${pair.id} ${pair.concept}: ${pair.note || 'a part is missing'}`); continue; }
  const variant = (role, name) => pair[`${role}_variants`].find(v => v.variant === name)?.key;
  const main = variant('main', 'current') || pair.main, sub = variant('sub', 'fill') || pair.sub;
  if (main === pair.main && sub === pair.sub) { skipped.push(`${pair.id} ${pair.concept}: no fill on either part`); continue; }
  const drawings = await call('GET', '/api/combinations/drawings?keys=' + encodeURIComponent([main, sub, pair.main, pair.sub].join(',')));
  const rejected = [main, sub, pair.main, pair.sub].filter(k => drawings[k]?.review === 'rejected');
  if (rejected.length) { skipped.push(`${pair.id} ${pair.concept}: ${rejected.join(', ')} is rejected in Icon review`); continue; }
  const position = pair.id.slice(-2);
  const part = (key, source) => ({svg: drawings[key].svg, source: drawings[source].svg, outline: key === source});
  let svg, layout;
  try {
    layout = {main: units('main', pair.layout.main, drawings[pair.main].svg, position), sub: units('sub', pair.layout.sub, drawings[pair.sub].svg, position)};
    Layout.preview({keyshapes: KEYSHAPES, position, main: part(main, pair.main), sub: part(sub, pair.sub), proposal: {main: {units: layout.main}, sub: {units: layout.sub}}});
    svg = Fill.combine({main: {...part(main, pair.main), layout: layout.main}, sub: {...part(sub, pair.sub), layout: layout.sub}}).svg;
  } catch (error) { skipped.push(`${pair.id} ${pair.concept}: ${error.message}`); continue; }
  made++;
  if (!args.send) continue;
  await call('POST', '/api/side-fill/pick', {reference_id: pair.id, rank: 1, main, sub, layout});
  await call('POST', '/api/side-fill/build', {reference_id: pair.id, rank: 1, svg,
    main: {icon: main, svg_sha256: drawings[main].svg_sha256}, sub: {icon: sub, svg_sha256: drawings[sub].svg_sha256}});
}
console.log(`${pairs.length} pairs without a pick use a part brought up to the site; ${made} ${args.send ? 'picked and built' : 'can be picked'}; ${skipped.length} skipped`);
for (const line of skipped.slice(0, 20)) console.log('  ' + line);
