#!/usr/bin/env node
// Side combination layouts (64 build) for an agent: read a pair from production, try a layout, store it.
//
//   node icon_set/scripts/side_layout.mjs list [--offset 0] [--limit 20] [--hand | --auto] [--unreviewed] [--q TEXT]
//   (list, fetch and push take only pairs whose main and sub are approved in Icon review on their current drawing)
//   node icon_set/scripts/side_layout.mjs fetch <reference_id> [--out DIR]
//   node icon_set/scripts/side_layout.mjs preview <DIR> [--main x,y,w,h] [--sub x,y,w,h] [--position P] [--auto]
//   node icon_set/scripts/side_layout.mjs push <DIR> [--dry-run]
//
// The pair lives in D1 (reference_parts: icon, position, layout boxes on the 64 grid). The combined drawing is
// composed here by combine-side.js exactly as the side page composes it (SideData.compose → CombineSide.pairRequest),
// and `push` stores it the way the layout editor's Save layout does: one POST /api/combinations/build carrying each
// part's layout and the sub's position. Only the layout changes; the picked icons never do.
//
// DIR (default icon_set/work/side-layout-adjust/<reference_id>) holds:
//   item.json, drawings.json   the pair and its parts' drawings as fetched (push refuses if production changed since)
//   layout.json                {position, main: [groups], sub: [groups]}: the file to edit; each group is
//                              {paths: [element numbers], x, y, w, h} in whole 64-grid units
//   elements.json              each part's elements (index, name, source box) so groups can be split or regrouped
//   current.svg / current*.png the stored combination;  proposed.svg / proposed*.png / compare.png the last preview
//   overlap-current.png / overlap.png   side_overlap.mjs's picture of the stored / proposed meeting (erased red, sub
//                              blue, crumbs orange); fetch and preview print its numbers under `overlap`
//
// Env: PICTOGRAPHIC_API (default production), PICTOGRAPHIC_ADMIN_USER + PICTOGRAPHIC_ADMIN_PASSWORD (push only),
// or PICTOGRAPHIC_SESSION (an existing pictographic_session cookie value).
import {existsSync, mkdirSync, writeFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import path from 'node:path';
import {SIZE, Side, WORK_NAME, compose, drawingMap, readJSON} from './side_compose.mjs';
import {analyzeDir, summary} from './side_overlap.mjs';
import {checkDir} from './side_contact_check.mjs';
import {intoCanvasKeyshape, keyshapeCheck} from './side_keyshape_check.mjs';
const POSITIONS = ['tl', 'tr', 'bl', 'br', 'ri', 'le', 'bo', 'to'];
const BASE = (process.env.PICTOGRAPHIC_API || 'https://pictographic-review-next.pictographic.workers.dev').replace(/\/$/, '');
// Cloudflare's browser integrity check refuses unknown agents (error 1010); work_queue.py sends the same one.
const USER_AGENT = 'pictographic-work-queue/1.0';
// A request that never answers would hang a batch forever.
const TIMEOUT_MS = 60000;
const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const WORK = path.join(ROOT, 'icon_set/work', WORK_NAME);

function fail(message) { console.error('error: ' + message); process.exit(1); }

function options(argv) {
  const out = {_: []};
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (!a.startsWith('--')) { out._.push(a); continue; }
    const name = a.slice(2), next = argv[i + 1];
    if (next === undefined || next.startsWith('--')) out[name] = true;
    else { out[name] = next; i++; }
  }
  return out;
}

let cookie = process.env.PICTOGRAPHIC_SESSION ? `pictographic_session=${process.env.PICTOGRAPHIC_SESSION}` : null;
export async function api(route, body) {
  const headers = {'User-Agent': USER_AGENT, Accept: 'application/json'};
  if (cookie) headers.Cookie = cookie;
  const init = body === undefined ? {headers} : {method: 'POST', headers: {...headers, 'Content-Type': 'application/json'}, body: JSON.stringify(body)};
  init.signal = AbortSignal.timeout(TIMEOUT_MS);
  const response = await fetch(BASE + route, init);
  const text = await response.text();
  let data;
  try { data = JSON.parse(text); } catch { data = {error: text.slice(0, 200)}; }
  if (!response.ok) throw Error(`${route.split('?')[0]}: HTTP ${response.status} ${data.error || ''}`.trim());
  return {data, response};
}
export async function getText(route) {
  const response = await fetch(BASE + route, {headers: {'User-Agent': USER_AGENT}, signal: AbortSignal.timeout(TIMEOUT_MS)});
  if (!response.ok) throw Error(`${route.split('?')[0]}: HTTP ${response.status}`);
  return response.text();
}
export async function login() {
  if (cookie) return;
  const username = process.env.PICTOGRAPHIC_ADMIN_USER, password = process.env.PICTOGRAPHIC_ADMIN_PASSWORD;
  if (!username || !password) fail('push needs PICTOGRAPHIC_ADMIN_USER and PICTOGRAPHIC_ADMIN_PASSWORD (or PICTOGRAPHIC_SESSION).');
  const {response} = await api('/api/auth/login', {username, password});
  const set = response.headers.getSetCookie?.() || [response.headers.get('set-cookie') || ''];
  const found = set.map(c => c.split(';')[0]).find(c => c.startsWith('pictographic_session='));
  if (!found) fail('login answered without a session cookie.');
  cookie = found;
}

export const query = extra => '/api/combinations?' + new URLSearchParams({kind: 'side', size: String(SIZE), forms: '1', ...extra});
const part = (item, role) => item.parts.find(p => p.role === role) || {role};
// Only approved icons are combined, and only pairs built from them are reviewed: the parts whose current drawing is
// not approved in Icon review, as "sub sub/x (pending)". A native-text sub has no icon and no review of its own.
export const unapprovedParts = item => item.parts.filter(p => p.icon && p.review !== 'approve')
  .map(p => `${p.role} ${p.icon} (${p.review || 'not reviewed'})`);
const writeJSON = (file, data) => writeFileSync(file, JSON.stringify(data, null, 2) + '\n');

async function itemOf(id) {
  const {data} = await api(query({q: id, limit: '5', offset: '0'}));
  return data.items.find(i => i.reference_id === id) || null;
}
async function drawingsOf(item) {
  const keys = ['main', 'sub'].map(r => part(item, r).icon).filter(Boolean);
  if (!keys.length) return {};
  const {data} = await api('/api/combinations/drawings?keys=' + encodeURIComponent(keys.join(',')));
  return data;
}

// A role's groups as the layout editor shows them (SideData.elements): the hand layout's groups, else the automatic
// placement split into connected pieces.
function groupsOf(composed, role, hand) {
  const form = composed.current.row[role === 'main' ? 'mains' : 'subs'][0];
  const parts = Side.elementParts(form.engine_document ?? form.document);
  const placed = composed.result.placements[role === 'main' ? 0 : 1].painted_box;
  let groups = hand;
  if (!groups || !groups.length) {
    const auto = {paths: parts.sources.map((b, i) => b ? i : null).filter(i => i !== null), x: placed.x + 2, y: placed.y + 2, w: placed.w - 4, h: placed.h - 4};
    const {sx, sy} = Side.groupTransform(auto, parts.sources);
    groups = Side.splitGroups([auto], parts.sources, Side.connected(parts.segments, 4 / ((sx + sy) / 2)));
  }
  const elements = parts.names.map((name, i) => ({index: i, name, source: parts.sources[i] && parts.sources[i].map(v => +v.toFixed(2))}));
  return {groups: groups.map(g => ({paths: [...g.paths], x: g.x, y: g.y, w: g.w, h: g.h})), elements};
}

function png(svgFile, out, size) {
  try { execFileSync('rsvg-convert', ['-w', String(size), '-h', String(size), '-b', 'white', '-o', out, svgFile], {timeout: 30000}); return true; }
  catch { return false; }
}
function pictures(dir, name, svg) {
  const file = path.join(dir, name + '.svg');
  writeFileSync(file, svg);
  png(file, path.join(dir, name + '.png'), 64);
  png(file, path.join(dir, name + '@4x.png'), 256);
}

// Where each part's ink lands (group boxes are centerlines; the stroke adds 2 on each side) and how they relate.
function metrics(layout, canvas = SIZE) {
  const ink = role => {
    const b = Side.groupsBox(layout[role]);
    return {x: b.x - 2, y: b.y - 2, w: b.w + 4, h: b.h + 4};
  };
  const main = ink('main'), sub = ink('sub');
  const gapX = Math.max(sub.x - (main.x + main.w), main.x - (sub.x + sub.w));
  const gapY = Math.max(sub.y - (main.y + main.h), main.y - (sub.y + sub.h));
  const outside = [main, sub].some(b => b.x < 0 || b.y < 0 || b.x + b.w > canvas || b.y + b.h > canvas);
  return {position: layout.position, main_ink: main, sub_ink: sub,
          sub_to_main: +(Math.max(sub.w, sub.h) / Math.max(main.w, main.h)).toFixed(2),
          // > 0: clear space between the ink boxes; <= 0: they overlap by that much on the shallower axis (the sub
          // erases the main where they meet).
          box_gap: Math.max(gapX, gapY),
          outside_canvas: outside};
}


async function list(opts) {
  const limit = Number(opts.limit || 20);
  const hand = i => !!Side.handLayout(i);
  // --unreviewed skips pairs that already have a review.json (side_review_record.mjs) in their work folder.
  const reviewed = i => existsSync(path.join(WORK, i.reference_id, 'review.json'));
  const keep = i => i.parts.every(p => p.icon || p.form?.native_text) && !(opts.hand && !hand(i)) &&
                    !(opts.auto && hand(i)) && !(opts.unreviewed && reviewed(i)) && !unapprovedParts(i).length;
  // Filters page through the list until `limit` pairs pass; next is the offset just past the last pair looked at.
  let offset = Number(opts.offset || 0), next = offset, total = 0;
  const rows = [];
  while (rows.length < limit && offset !== null) {
    const {data} = await api(query({state: 'built', limit: '500', offset: String(offset), ...(opts.q ? {q: opts.q} : {})}));
    total = data.total;
    for (const [k, i] of data.items.entries()) {
      if (rows.length >= limit) break;
      next = offset + k + 1;
      if (keep(i)) rows.push(i);
    }
    offset = data.next_offset ?? null;
    if (!data.items.length) break;
  }
  if (rows.length < limit && offset === null) next = null;
  for (const i of rows) {
    console.log([i.reference_id, part(i, 'sub').position || '-', hand(i) ? 'hand' : 'auto', i.icon?.review || '-',
                 part(i, 'main').icon || '-', part(i, 'sub').icon || '(text)', i.concept].join('\t'));
  }
  console.error(`${rows.length} shown; ${total} built side pairs; next --offset ${next ?? '-'}`);
}

async function fetchPair(id, opts) {
  const item = await itemOf(id);
  if (!item) fail(`no side pair ${id}.`);
  if (item.state === 'unbuilt') fail(`${id} has never been built; build it on the side page first.`);
  if (!item.parts.every(p => p.icon || p.form?.native_text)) fail(`${id} has a part with no icon picked.`);
  const unapproved = unapprovedParts(item);
  if (unapproved.length) fail(`${id} is not reviewed: only pairs whose main and sub are approved are. Not approved: ${unapproved.join(', ')}.`);
  const dir = path.resolve(opts.out || path.join(WORK, id));
  const drawings = await drawingsOf(item);
  const stored = item.icon?.preview_url ? await getText(item.icon.preview_url) : null;
  console.log(JSON.stringify(savePair(dir, item, drawings, stored), null, 2));
}

// Write a fetched pair's work folder (see the header) and return what fetch prints. `stored` is the stored combined
// SVG, or null. Shared with side_audit_refresh.mjs, which downloads many pairs at once.
export function savePair(dir, item, drawings, stored) {
  const id = item.reference_id;
  mkdirSync(dir, {recursive: true});
  writeJSON(path.join(dir, 'item.json'), item);
  writeJSON(path.join(dir, 'drawings.json'), drawings);
  for (const role of ['main', 'sub']) {
    const key = part(item, role).icon;
    if (key && drawings[key]) {
      writeFileSync(path.join(dir, role + '.svg'), drawings[key].svg);
      // The part on its own, for the agent to look at before judging the pair.
      png(path.join(dir, role + '.svg'), path.join(dir, role + '@4x.png'), 256);
    }
  }

  const composed = Side.pairRequest(item, drawingMap(drawings), {size: SIZE});
  const hand = Side.handLayout(item) || {};
  const layout = {position: part(item, 'sub').position}, elements = {};
  for (const role of ['main', 'sub']) {
    const g = groupsOf(composed, role, hand[role]);
    layout[role] = g.groups;
    elements[role] = g.elements;
  }
  writeJSON(path.join(dir, 'layout.json'), layout);
  writeJSON(path.join(dir, 'base-layout.json'), {...layout, hand: {main: !!hand.main, sub: !!hand.sub}});
  writeJSON(path.join(dir, 'elements.json'), elements);

  if (stored !== null) pictures(dir, 'current', stored);
  const rebuilt = compose(dir, layout).svg;
  pictures(dir, 'rebuilt', rebuilt);
  return {dir, reference_id: id, concept: item.concept, state: item.state,
          main: part(item, 'main').icon, sub: part(item, 'sub').icon || '(native text)',
          hand_layout: {main: !!hand.main, sub: !!hand.sub},
          rebuilt_matches_stored: stored === null ? null : stored === rebuilt,
          // What a rebuild changes: 'none'; 'sub' (only the drawn sub: the engine now publishes the
          // original sub drawing where it used to publish its SUB32-snapped copy); or 'main' (the
          // main's cut differs: the stored icon was built some other way or from older drawings).
          rebuild_change: stored === null ? null : stored === rebuilt ? 'none'
            : groupOf(stored, 'main-icon-clipped') === groupOf(rebuilt, 'main-icon-clipped') ? 'sub' : 'main',
          metrics: metrics(layout), overlap: overlapOf(dir, 'overlap-current.png')};
}

// One top-level group of a combined SVG, by id (the main's clipped strokes, or the sub).
const groupOf = (svg, id) => (svg.match(new RegExp(`<g[^>]*id="${id}"[\\s\\S]*?</g>\\s*(?=<g|</svg>)`)) || [''])[0];

function parseBox(text, role) {
  const v = String(text).split(',').map(Number);
  if (v.length !== 4 || v.some(n => !Number.isInteger(n))) fail(`--${role} takes x,y,w,h as whole grid units.`);
  return {x: v[0], y: v[1], w: v[2], h: v[3]};
}

// side_overlap.mjs's measurement of the folder's layout.json.
const overlapOf = (dir, picture) => summary(analyzeDir(dir, {}, picture));

async function preview(dir, opts) {
  dir = path.resolve(dir);
  const file = path.join(dir, 'layout.json');
  let layout = readJSON(file);
  if (opts.position) {
    if (!POSITIONS.includes(opts.position)) fail(`--position is one of ${POSITIONS.join(', ')}.`);
    layout.position = opts.position;
  }
  if (opts.auto) {
    // Automatic placement at the (new) position, as editable groups.
    const item = readJSON(path.join(dir, 'item.json'));
    const composed = Side.pairRequest(item, drawingMap(readJSON(path.join(dir, 'drawings.json'))), {position: layout.position, layout: null, size: SIZE});
    for (const role of ['main', 'sub']) layout[role] = groupsOf(composed, role, null).groups;
    // The engine places parts at the canvas padding; the canvas keyshape rule (2026-10-12) needs main + sub inside one
    // canvas keyshape, so move them in by whole units (sizes unchanged), as the snap did for stored layouts.
    if (!item.parts.some(p => p.role === 'sub' && !p.icon)) layout = intoCanvasKeyshape(layout);
  }
  // Move and scale a whole part: every group of it mapped from the part's box onto the new one. The groups come from
  // the stored layout (base-layout.json) when they are the same groups, so repeated previews never stack rounding
  // (a 10x13 arrow group shrank to 10x1 over a search of whole-unit moves). Fine edits by hand go after the last move.
  const base = existsSync(path.join(dir, 'base-layout.json')) ? readJSON(path.join(dir, 'base-layout.json')) : null;
  const sameGroups = (a, b) => JSON.stringify((a || []).map(g => g.paths)) === JSON.stringify((b || []).map(g => g.paths));
  for (const role of ['main', 'sub']) {
    if (!opts[role]) continue;
    const from = base && !opts.auto && sameGroups(base[role], layout[role]) ? base[role] : layout[role];
    layout[role] = Side.mapGroups(from, Side.groupsBox(from), parseBox(opts[role], role));
  }
  let composed;
  try { composed = compose(dir, layout); }
  catch (e) { fail(`the engine refused this layout (layout.json unchanged): ${e.message}`); }
  writeJSON(file, layout);
  pictures(dir, 'proposed', composed.svg);
  writeJSON(path.join(dir, 'request.json'), composed.request);
  const current = path.join(dir, 'current@4x.png'), proposed = path.join(dir, 'proposed@4x.png');
  if (existsSync(current) && existsSync(proposed)) {
    try {
      execFileSync('magick', [current, proposed, '-bordercolor', '#ccc', '-border', '2', '+append', path.join(dir, 'compare.png')], {timeout: 30000});
    } catch { /* compare.png is a convenience */ }
  }
  console.log(JSON.stringify({proposed: path.join(dir, 'proposed@4x.png'), compare: path.join(dir, 'compare.png'),
                              warnings: composed.result.warnings || [], metrics: metrics(layout, composed.result.canvas || SIZE),
                              overlap: overlapOf(dir, 'overlap.png'),
                              layout}, null, 2));
}

async function push(dir, opts) {
  dir = path.resolve(dir);
  const saved = readJSON(path.join(dir, 'item.json'));
  const layout = readJSON(path.join(dir, 'layout.json'));
  const composed = compose(dir, layout);
  const request = composed.request;
  // Cut or clear, never a nick: refuse a proposal whose parts graze, shave or nick each other.
  const check = checkDir(dir);
  // A gap the user approved by eye (review.json gap_ok / user_directed for this very layout) is not a refusal.
  const rev = existsSync(path.join(dir, 'review.json')) ? readJSON(path.join(dir, 'review.json')) : {};
  const box = groups => { const x0 = Math.min(...groups.map(g => g.x)), y0 = Math.min(...groups.map(g => g.y));
    return [x0, y0, Math.max(...groups.map(g => g.x + g.w)) - x0, Math.max(...groups.map(g => g.y + g.h)) - y0]; };
  const approved = (rev.gap_ok || rev.user_directed) && rev.after && rev.after.position === layout.position
    && JSON.stringify(rev.after.main) === JSON.stringify(box(layout.main)) && JSON.stringify(rev.after.sub) === JSON.stringify(box(layout.sub));
  // --as-stored: re-store the pair's own stored layout unchanged (explicit boxes), e.g. to pin it after the shared
  // position moved; the checks judged proposals, not the stored layout, so they are skipped for it.
  const asStored = opts['as-stored'] && JSON.stringify(layout) === JSON.stringify(readJSON(path.join(dir, 'base-layout.json')));
  if (opts['as-stored'] && !asStored) fail('--as-stored needs layout.json equal to base-layout.json.');
  if (check.verdict === 'fail' && !approved && !asStored) fail(`the proposal fails the contact check (side_contact_check.mjs):\n  ${check.problems.join('\n  ')}`);
  // The keyshape system: each part only on its own keyshape at a preset size in its corner (side_keyshape_check.mjs).
  const ks = keyshapeCheck(dir, layout);
  if (!ks.ok && !asStored) fail(`the layout is off the keyshape system (side_keyshape_check.mjs):\n  ${Object.values(ks.roles).filter(r => !r.ok).map(r => `${r.problem}; nearest allowed: ${r.nearest.join(' | ')}`).join('\n  ')}`);
  if (opts['dry-run']) { console.log(JSON.stringify({dry_run: true, request: {...request, svg: request.svg.length + ' chars'}}, null, 2)); return; }

  // Refuse when someone changed the pair since fetch: a picked icon, a redrawing, a layout or the position.
  const now = await itemOf(saved.reference_id);
  if (!now) fail('the pair is gone.');
  const facts = it => it.parts.map(p => [p.role, p.icon, p.current_sha, JSON.stringify(p.layout), p.position]);
  if (JSON.stringify(facts(now)) !== JSON.stringify(facts(saved))) fail('the pair changed on production since fetch; fetch it again.');
  const unapproved = unapprovedParts(now);
  if (unapproved.length) fail(`not pushed: only approved icons are combined. Not approved: ${unapproved.join(', ')}.`);

  await login();
  const {data} = await api('/api/combinations/build', {size: SIZE, builds: [request]});
  const result = data.results[0];
  if (!result?.ok) fail(result?.error || 'the build was refused.');
  // The agent's review of this pair (side_review_record.mjs) now shows the fix as stored.
  const reviewFile = path.join(dir, 'review.json');
  if (existsSync(reviewFile)) {
    const review = readJSON(reviewFile);
    Object.assign(review, {result: 'pushed', svg_sha256: result.svg_sha256, pushed_at: new Date().toISOString()});
    writeFileSync(reviewFile, JSON.stringify(review, null, 2) + '\n');
  }
  console.log(JSON.stringify(result, null, 2));
}

// Run as a command.
if (process.argv[1] && path.resolve(process.argv[1]) === new URL(import.meta.url).pathname) {
  const [command, ...rest] = process.argv.slice(2);
  const opts = options(rest);
  try {
    if (command === 'list') await list(opts);
    else if (command === 'fetch' && opts._[0]) await fetchPair(opts._[0], opts);
    else if (command === 'preview' && opts._[0]) await preview(opts._[0], opts);
    else if (command === 'push' && opts._[0]) await push(opts._[0], opts);
    // session <FILE>: log in once and keep the session cookie value in FILE (mode 600) for a batch of pushes.
    else if (command === 'session' && opts._[0]) { await login(); writeFileSync(opts._[0], cookie.split('=').slice(1).join('='), {mode: 0o600}); console.log('session saved'); }
    else fail('usage: side_layout.mjs list | fetch <reference_id> | preview <dir> | push <dir> (see the header).');
  } catch (e) {
    fail(e.message);
  }
}
