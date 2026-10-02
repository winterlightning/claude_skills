// What a side pair's row shows and how it is filtered: the old Side pairs grid's rules (side-pairs-grid.js),
// carried over line for line. `s` is the page's data (store.svelte.js): pairs, previews, components and their
// status per source, reviews, primitive statuses and the catalog rows / references.

export const POSITIONS = {br: 'Bottom-right', bl: 'Bottom-left', tr: 'Top-right', tl: 'Top-left', ri: 'Right', le: 'Left', bo: 'Bottom', to: 'Top'};
// One plain status per pair. Waiting: main and sub are drawn but not in the combine data yet.
export const STATES = {ready: 'Ready', fix: 'Fix sub', fixmain: 'Fix main', waiting: 'Waiting', main: 'Needs main', sub: 'Needs sub', textsub: 'Needs text sub'};
export const STATE_HINTS = {
  ready: 'Main and sub are drawn and can be combined.', fix: 'The sub fails a check. Fix it before combining.',
  fixmain: 'A 48×48 main is drawn but fails validation or was marked needs fix, so it is not in Icon review. Fix it on the Main icons page (Needs fix).',
  waiting: 'Main and sub are drawn but not combined yet.', main: 'No 48×48 solo main icon yet.', sub: 'No 32×32 sub icon yet.',
  textsub: 'The sub is text or a number and is not drawn yet. It is generated separately.'};
export const FILTERS = {'': 'All', ...STATES, uncombined: 'Not combined', text: 'Text sub', multi: '2+ subs', made: 'From review',
  changed: 'Main / sub changed', built: 'Built', stale: 'Stale (built from older drawings)', unbuilt: 'Not built'};
export const GROUPS = {'': 'No grouping', main: 'Group by main', sub: 'Group by sub'};
export const PAGE_SIZES = [24, 48, 96];
export const REVIEW_LABELS = {approve: 'Approved', ready: 'To review', 're-generated': 'To review', pending: 'Needs fix', disapprove: 'Needs fix',
  claimed: 'Being fixed', rejected: 'Rejected'};

export const subKey = item => item.model_key || item.family + '/' + item.icon;
export const dataURL = svg => 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
export const round = n => Math.round(n * 10) / 10;

// Same rule as side-components.js: a passing drawing marked needs fix (review pending) or rejected does not count;
// a failing drawing counts once a reviewer approved it as an exception.
export const usable = (s, d) => (d.status === 'pass' || s.reviews[d.key] === 'approve') && !['pending', 'rejected'].includes(s.reviews[d.key]);
// Why a drawing shown on a tile does not count: failed checks or its review state.
export function drawingProblems(s, d) {
  if (!d || usable(s, d)) return [];
  if (d.status !== 'pass') return d.errors?.length ? d.errors : ['Fails validation'];
  return [s.reviews[d.key] === 'rejected' ? 'Rejected in Icon review' : 'Disapproved — needs fix'];
}
// Ink box including the 4px stroke; subs report their normalized 32px ink directly.
export function ink(item, sub) {
  if (sub && item.ink32) return [item.ink32.ink_width, item.ink32.ink_height];
  const b = item.bounds;
  // A made pair's items are measured by the combine engine only; its sub is a sub-family icon, checked at 32 by its build.
  if (!b) return [0, 0];
  return [b[2] - b[0] + 4, b[3] - b[1] + 4];
}
export function subProblems(s, item, flagged = () => false) {
  const problems = [], [w, h] = ink(item, true);
  if (item.model_validation && item.model_validation !== 'pass') problems.push('Model validation: ' + item.model_validation);
  if (['needs_redraw', 'needs_review'].includes(item.sub32_status)) problems.push(item.sub32_reason || 'Needs a SUB32 redraw');
  if (!item.native_text && (w > 32.01 || h > 32.01)) problems.push(`Ink ${round(w)}×${round(h)} exceeds 32×32`);
  if (flagged(item)) problems.push('Disapproved — needs fix');
  return problems;
}
export const currentSub = pair => pair.subs[0];
// The main a row shows and combines (the server picks the same one when none is named).
export const mainOf = pair => pair.mains.find(m => m.family === 'solo' || m.family === 'combination_main') || pair.mains[0];
// A sub is text when its source was marked text / number or its current drawing is sized as text.
export function subIsText(s, row, pair) {
  const refs = s.catalog.references;
  if ([row.sub_id, refs[row.sub_id]?.canonical_id].some(id => id && s.statuses[id]?.reason === 'text_number')) return true;
  return !!pair?.subs.length && currentSub(pair).sizing_kind === 'text';
}
// A main counts only as a passing main drawing; a sub only as a sub drawing.
export function key(s, row, flagged) {
  const pair = s.pairs.get(row.id), main = s.componentStatus.main.get(row.main_id), sub = s.componentStatus.sub.get(row.sub_id);
  const textSub = sub === 'missing' && subIsText(s, row, pair);
  // A drawn main that fails is a fix, not a missing main; the tile still shows that drawing.
  if (main === 'failing') return 'fixmain';
  if (main !== 'done') return sub === 'missing' ? (textSub ? 'both-text' : 'both') : 'main';
  if (sub === 'missing') return textSub ? 'textsub' : 'sub';
  if (sub === 'failing') return 'fix';
  if (pair?.mains.length && pair.subs.length) return subProblems(s, currentSub(pair), flagged).length ? 'fix' : 'ready';
  return 'waiting';
}
export function category(s, row, flagged, buildState) {
  const pair = s.pairs.get(row.id), k = key(s, row, flagged);
  const both = k.startsWith('both');
  // Not combined: main and sub are both drawn, but no combined icon is stored for the pair.
  const uncombined = !['main', 'fixmain', 'sub', 'textsub'].includes(k) && !both && !s.previews[row.id];
  const subNeeded = k === 'fixmain' && s.componentStatus.sub.get(row.sub_id) === 'missing' ? (subIsText(s, row, pair) ? 'textsub' : 'sub') : null;
  // The pair's build in D1: built, stale (a part redrawn since) or not built.
  return {[buildState || 'unbuilt']: true, made: !!pair?.custom && !pair.published, changed: !!pair?.published, [both ? 'main' : k]: true,
          ...(both ? {[k === 'both' ? 'sub' : 'textsub']: true} : {}), ...(subNeeded ? {[subNeeded]: true} : {}), uncombined,
          multi: (pair?.subs.length || 0) > 1, text: subIsText(s, row, pair)};
}

// Resolve the exact displayed variant; use the live failed drawing when no passing one exists.
export function editableDrawing(s, row, role, item) {
  const source = row[role + '_id'], list = s.components?.[role === 'main' ? 'mains' : 'subs'] || [];
  const component = list.find(c => c.id === source || c.source_ids.includes(source));
  const drawings = component?.drawings || [], k = item?.model_key || item?.key;
  return (k ? drawings.find(d => d.key === k) : null) || (item?.icon ? drawings.find(d => d.icon_id === item.icon) : drawings[0]);
}
/* Each pair is one row: Original → Main → Sub → Combined, with one main and one sub. */
export function parts(s, row, flagged) {
  const refs = s.catalog.references, pair = s.pairs.get(row.id);
  const k = key(s, row, flagged), hasMain = !['main', 'fixmain', 'both', 'both-text'].includes(k);
  const hasSub = !['sub', 'textsub', 'both', 'both-text'].includes(k) && !(k === 'fixmain' && s.componentStatus.sub.get(row.sub_id) === 'missing');
  if (pair?.mains.length && pair.subs.length && hasMain && hasSub) return {pair, key: k, main: mainOf(pair), sub: currentSub(pair), ready: true};
  const main = (refs[row.main_id]?.generated || []).find(g => /^(solo|combination_main|main-54)\//.test(g.key));
  const sub = (row.sub_generated ?? refs[row.sub_id]?.generated ?? []).find(g => /^(sub|text|sub-36)\//.test(g.key));
  return {pair, key: k, main: hasMain && main && {icon: main.icon_id, preview_url: main.preview_url, pending: true},
          sub: hasSub && sub && {icon: sub.icon_id, preview_url: sub.preview_url, pending: true}, ready: false};
}
// The badge a row's head shows: its label, tone and hint.
export function state(s, row, p) {
  const k = p.key.startsWith('both') ? 'main' : p.key, subMissing = k === 'fixmain' && s.componentStatus.sub.get(row.sub_id) === 'missing';
  const label = p.key === 'both' ? 'Needs main + sub' : p.key === 'both-text' ? 'Needs main + text sub' : subMissing ? 'Fix main + needs sub' : STATES[k];
  return [label, {ready: 'ready', fix: 'fix', fixmain: 'fix', waiting: 'waiting', textsub: 'info'}[k] || 'needed', STATE_HINTS[k]];
}
// What a part's tile shows: the pair's item, or the catalog drawing when the item is not the drawing it shows now.
export function display(s, row, role, item) {
  const drawing = editableDrawing(s, row, role, item);
  if (item && drawing && item.sha256 === drawing.svg_sha256 && !drawing.preview_url?.includes('/api/icon-artwork/')) return item;
  return drawing ? {...item, icon: drawing.icon_id, key: drawing.key, model_key: drawing.key, family: drawing.family,
                    preview_url: drawing.preview_url, document: null, pending: item?.pending ?? true} : item;
}
// The rows a search, filter and grouping keep.
export function matches(s, row, query) {
  const q = query.trim().toLowerCase();
  if (!q) return true;
  const refs = s.catalog.references, pair = s.pairs.get(row.id);
  return [row.concept, row.id, row.main_id, row.sub_id, refs[row.main_id]?.concept, refs[row.sub_id]?.concept,
          ...(pair ? [...pair.mains, ...pair.subs].map(m => m.icon) : [])].join(' ').toLowerCase().includes(q);
}
/* Grouping collects pairs that reuse the same main or the same sub icon. */
export function groups(s, rows, by, flagged) {
  const refs = s.catalog.references, out = new Map();
  for (const row of rows) {
    const item = parts(s, row, flagged)[by], sourceId = by === 'main' ? row.main_id : row.sub_id;
    const k = item ? by + '/' + item.icon : 'needed/' + sourceId;
    if (!out.has(k)) out.set(k, {key: k, item, title: item ? item.icon : (refs[sourceId]?.concept || sourceId), rows: []});
    out.get(k).rows.push(row);
  }
  return [...out.values()].sort((a, b) => b.rows.length - a.rows.length || a.title.localeCompare(b.title));
}
