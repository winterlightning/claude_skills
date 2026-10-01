// The answers Icon review gave before it listed from D1: gallery.html's own list functions (filteredIcons,
// versionGroups, categoryCounts, render's tab counts) run over icon-query.json, with the review statuses, picks,
// feedback and work claims the page loaded from the API worked out from the fixture's tables.
//   node cloud/worker/core/tests/fixtures/make_icon_query_expected.mjs   → icon-query-expected.json
import {readFileSync, writeFileSync} from 'node:fs';
import vm from 'node:vm';

const here = new URL('.', import.meta.url);
const root = new URL('../../../../../', here);
const page = readFileSync(new URL('icon_set/scripts/templates/gallery.html', root), 'utf8');
const fixture = JSON.parse(readFileSync(new URL('icon-query.json', here), 'utf8'));

// A top-level declaration of the page script, by brace matching (strings, template literals and regexes skipped).
function declaration(start) {
  let depth = 0, i = page.indexOf('{', start);
  for (; i < page.length; i++) {
    const c = page[i];
    if (c === '"' || c === "'" || c === '`') {
      for (i++; i < page.length && page[i] !== c; i++) if (page[i] === '\\') i++;
    } else if (c === '/' && page[i + 1] === '/' ) {
      while (page[i] !== '\n') i++;
    } else if (c === '/' && /[(,=:!&|?{};]\s*$/.test(page.slice(Math.max(0, i - 3), i))) {
      for (i++; i < page.length && page[i] !== '/'; i++) { if (page[i] === '\\') i++; else if (page[i] === '[') while (page[++i] !== ']'); }
    } else if (c === '{') depth++;
    else if (c === '}' && --depth === 0) return page.slice(start, i + 1);
  }
  throw Error('unterminated declaration at ' + start);
}
const fn = name => {
  const at = page.indexOf('function ' + name + '(');
  if (at < 0) throw Error('missing ' + name);
  return declaration(at);
};
const line = text => {
  const at = page.indexOf(text);
  if (at < 0) throw Error('missing ' + text);
  return page.slice(at, page.indexOf(';', at) + 1);
};
const source = [
  line('const COMBINED_FAMILIES='), line('const blockedCombination='), line('const VIRTUAL_FAMILIES='), line('const facetFields='),
  ...['iconState', 'inSection', 'versionMode', 'versionGroupKey', 'versionGroups', 'iconVersion', 'sectionIcons', 'matchesFamily',
      'matchesSearchExceptCategory', 'matchesSearch', 'matchesApprover', 'matchesFeedbackAuthor', 'modelAvailable', 'artworkKind',
      'strokeCount', 'segmentCount', 'symmetryAxes', 'matchesFacets', 'sortIcons', 'filteredIcons', 'matchesPendingFeedback',
      'categoryCounts'].map(fn)].join('\n');

// ---- what the page loaded: review statuses (current_decisions), picks (overrides), work claims, feedback
const records = fixture.records.map(r => ({...r}));
const byKey = new Map(records.map(r => [r.key, r]));
const graphs = new Set(fixture.graphs);
for (const {key, document} of fixture.artwork) {
  const record = byKey.get(key), now = fixture.current_sha[key];
  const applies = document.source_svg_sha256 && (!graphs.has(now) || document.source_svg_sha256 === now);
  if (applies) Object.assign(record, {artwork_source: document.source_mode || 'use_org', svg_sha256: now});
}
const sorted = [...fixture.reviews].sort((a, b) => a.updated_at.localeCompare(b.updated_at));
const decisions = new Map(records.map(r => [r.key, {status: 'ready', actor: null}]));
for (const row of sorted) if (byKey.get(row.icon)?.svg_sha256 === row.svg_sha256)
  decisions.set(row.icon, {status: row.status === 're-generated' ? 'ready' : row.status, actor: row.updated_by});
for (const row of sorted) if (byKey.has(row.icon) && row.status === 'rejected') decisions.set(row.icon, {status: 'rejected', actor: row.updated_by});
for (const split of fixture.splits) if (split.active && byKey.get(split.icon)?.svg_sha256 === split.svg_sha256)
  decisions.set(split.icon, {status: 'rejected', actor: split.created_by});
const by = statuses => Object.fromEntries([...decisions].filter(([, d]) => statuses.includes(d.status) && d.actor).map(([k, d]) => [k, d.actor]));
const workClaims = {};
for (const row of fixture.reviews) {
  if (!row.worker || byKey.get(row.icon)?.svg_sha256 !== row.svg_sha256) continue;
  const state = row.status === 'ready' ? 'done' : row.status === 'pending' ? 'cannot-fix' : null;  // claims in the fixture have expired
  if (state) workClaims[row.icon] = {state, svg_sha256: row.svg_sha256};
}
const feedbackBy = {};
for (const row of fixture.feedback) if (row.author && byKey.has(row.icon)) (feedbackBy[row.icon] ||= []).includes(row.author) || feedbackBy[row.icon].push(row.author);
const latest = new Map();
for (const row of fixture.feedback) {
  const icon = byKey.get(row.icon);
  if (!icon || row.svg_sha256 !== icon.svg_sha256) continue;
  if (!latest.has(row.icon) || row.id > latest.get(row.icon).id) latest.set(row.icon, row);
}
const statuses = Object.fromEntries([...decisions].map(([k, d]) => [k, d.status]));

const controls = {};
const $ = id => (controls[id] ||= {value: ''});
const context = vm.createContext({
  $, icons: records.filter(r => !r.build_failed), failedIcons: records.filter(r => r.build_failed), reviews: statuses,
  approvedBy: by(['approve']), disapprovedBy: by(['pending', 'disapprove', 'claimed']), rejectedBy: by(['rejected']),
  feedbackBy, workClaims, reviewFacets: fixture.facets, reviewsLoaded: true, pendingFeedbackLoaded: true,
  pendingFeedbackKeys: new Set(fixture.feedback.map(r => r.icon)),
  pendingReasons: Object.fromEntries([...latest].map(([k, row]) => [k, row.reason === 'bad-draw' ? 'bad-stroke' : row.reason || 'other'])),
  section: 'icons', reviewFilter: '',
});
vm.runInContext(source.replace(/^const /gm, 'var '), context);

const IDS = {family: 'family', q: 'search', category: 'category', symmetry: 'symmetryFilter', strokes: 'strokeFilter',
             reason: 'reasonFilter', keyshape: 'keyshapeFilter', revision: 'versionFilter', reference: 'referenceFilter',
             artwork: 'artworkFilter', author: 'authorFilter', reviewer: 'approvedBy', icon_feedback_by: 'iconFeedbackBy',
             pending_feedback: 'pendingFeedback', sort: 'iconSort', view: 'iconView'};
const results = fixture.cases.map(params => {
  for (const [name, id] of Object.entries(IDS)) $(id).value = params[name] ?? (name === 'sort' ? 'name' : name === 'view' ? 'generated' : '');
  context.reviewFilter = params.reason ? 'pending' : params.status || '';
  return vm.runInContext(`(() => {
    const rows = filteredIcons(), grouped = versionMode(), units = grouped ? versionGroups(rows) : rows;
    const limit = ${params.limit || 48}, pages = Math.max(1, Math.ceil(units.length / limit));
    const page = Math.max(1, Math.min(${Math.floor((params.offset || 0) / (params.limit || 48)) + 1}, pages));
    const visible = units.slice((page - 1) * limit, page * limit);
    const matching = sectionIcons().filter(matchesSearch), states = {};
    for (const icon of matching) states[iconState(icon)] = (states[iconState(icon)] || 0) + 1;
    return {keys: (grouped ? visible.flat() : visible).map(i => i.key), total: units.length, versions: rows.length,
            offset: (page - 1) * limit, states, categories: Object.fromEntries([...categoryCounts()].sort())};
  })()`, context);
});
writeFileSync(new URL('icon-query-expected.json', here), JSON.stringify({statuses, results}, null, 1) + '\n');
console.log(results.length + ' cases; ' + results.reduce((n, r) => n + r.keys.length, 0) + ' listed icons');
