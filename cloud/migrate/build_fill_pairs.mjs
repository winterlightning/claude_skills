#!/usr/bin/env node
// Build the combined icon of every fill side pair pick that has none or is stale, with the pages' own engine
// (icon_set/scripts/templates/side-fill-combine.js), and save each with POST /api/side-fill/build — as a person
// building it on the pair page would, so it lands in Icon review as Ready.
//
//   node cloud/migrate/build_fill_pairs.mjs --base-url http://localhost:8821 --cookie pictographic_session=…   # dry run
//   node cloud/migrate/build_fill_pairs.mjs --base-url https://… --token "$PICTOGRAPHIC_PUSH_TOKEN" --send
//
// Reads are bounded: the picked pairs in keyset pages of 120 (GET /api/side-fill/pairs), and the drawings of their
// icons and sources 100 keys at a time (GET /api/combinations/drawings). A pick is built when it has no combined
// icon or a part's drawing changed since it was built (built_sha); --all builds every pick again.
import {createRequire} from 'node:module';
import {parseArgs} from 'node:util';

const require = createRequire(import.meta.url);
const Fill = require('../../icon_set/scripts/templates/side-fill-combine.js');
const {values: args} = parseArgs({options: {
  'base-url': {type: 'string'}, token: {type: 'string'}, cookie: {type: 'string'}, send: {type: 'boolean'},
  all: {type: 'boolean'}, limit: {type: 'string'}, ids: {type: 'string'}}});
const base = (args['base-url'] || '').replace(/\/$/, '');
if (!base) { console.error('error: --base-url is required'); process.exit(2); }
const headers = {'User-Agent': 'pictographic-migrate/1.0', 'Content-Type': 'application/json',
                 ...(args.token ? {Authorization: 'Bearer ' + args.token} : {}), ...(args.cookie ? {Cookie: args.cookie, Origin: base} : {})};

async function call(method, path, body) {
  const response = await fetch(base + path, {method, headers, body: body === undefined ? undefined : JSON.stringify(body)});
  const data = await response.json().catch(() => ({}));
  if (!response.ok) throw new Error(`${method} ${path} → ${response.status} ${data.error || ''}`);
  return data;
}

const wanted = args.ids ? new Set(args.ids.split(',')) : null;
const pairs = [];
for (let after = null; ;) {
  const page = await call('GET', '/api/side-fill/pairs?' + new URLSearchParams({state: 'picked', limit: '120', ...(after ? {after} : {})}));
  pairs.push(...page.pairs.filter(p => !wanted || wanted.has(p.id)));
  if (!page.next) break;
  after = page.next;
}
const stale = pick => !pick.combined || ['main', 'sub'].some(r => pick[r] && pick[r].built_sha !== pick[r].svg_sha256);
let jobs = pairs.flatMap(pair => pair.picks.filter(p => p.main && p.sub && (args.all || stale(p))).map(pick => ({pair, pick})));
const total = jobs.length;
if (args.limit) jobs = jobs.slice(0, Number(args.limit));
console.log(`${pairs.length} picked pairs; ${total} picks to build${args.limit ? ` (building ${jobs.length})` : ''}`);
if (!args.send) process.exit(0);

// The drawings of every icon and source the picks use.
const keys = [...new Set(jobs.flatMap(({pair, pick}) => [pick.main.icon, pick.sub.icon, pair.main, pair.sub]))];
const drawings = {};
for (let i = 0; i < keys.length; i += 100) {
  Object.assign(drawings, await call('GET', '/api/combinations/drawings?keys=' + encodeURIComponent(keys.slice(i, i + 100).join(','))));
}
let built = 0, failed = 0, partsNotApproved = 0;
const problems = [];
for (const [n, {pair, pick}] of jobs.entries()) {
  const part = (role, source) => {
    const icon = drawings[pick[role].icon], src = drawings[source];
    if (!icon?.svg || !src?.svg) throw new Error(`${role}: drawing missing`);
    return {svg: icon.svg, source: src.svg, layout: pick[role].layout, outline: pick[role].icon === source, sha: icon.svg_sha256};
  };
  try {
    const main = part('main', pair.main), sub = part('sub', pair.sub);
    const {svg} = Fill.combine({main, sub, options: pick.options});
    const answer = await call('POST', '/api/side-fill/build', {reference_id: pair.id, rank: pick.rank, svg,
      main: {icon: pick.main.icon, svg_sha256: main.sha}, sub: {icon: pick.sub.icon, svg_sha256: sub.sha}});
    built++;
    if (answer.build_failed) partsNotApproved++;
  } catch (error) {
    failed++;
    problems.push(`${pair.id} #${pick.rank}: ${error.message}`);
  }
  if ((n + 1) % 200 === 0 || n + 1 === jobs.length) console.log(`built ${n + 1}/${jobs.length} (${failed} failed)`);
}
console.log(`${built} built (${partsNotApproved} with a part not approved in Icon review yet), ${failed} failed`);
for (const line of problems.slice(0, 15)) console.log('  ' + line);
process.exit(failed ? 1 : 0);
