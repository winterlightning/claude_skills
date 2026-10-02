// Change main / sub, and a side pair made from a combination primitive (the old side-pair-maker.js without its DOM).
// A reference classified as a combination is not a side pair until it is made one: pick its main (a solo icon) and
// its sub (a sub icon) from pictures, prefilled from the classification's briefs; when no icon fits yet, keep the
// name of the one to draw. From D1: the pair (GET /api/combinations), its icons and names to draw
// (POST /api/combinations/parts), a new pair (POST /api/combinations/pair), candidates (GET /api/combinations/candidates);
// a new side is saved with a build composed in this browser (side-pairs-data.js).
import {SvelteMap} from 'svelte/reactivity';

export const POSITIONS = {br: 'Bottom-right', bl: 'Bottom-left', tr: 'Top-right', tl: 'Top-left', ri: 'Right', le: 'Left', bo: 'Bottom', to: 'Top'};
export const ROLES = {main: {label: 'Main icon', family: 'solo', hint: 'A 48×48 solo icon', example: 'eye'},
                      sub: {label: 'Sub icon', family: 'sub', hint: 'A 32×32 sub icon', example: 'light bulb'}};
export const STATUS = {needs_both: ['Needs main + sub drawn', 'todo'], needs_main: ['Needs main drawn', 'todo'], needs_sub: ['Needs sub drawn', 'todo'],
                       waiting: ['On the side page', 'drawn'], generated: ['Combined', 'generated']};
export const TRACK = 'primitives.html?view=side&side=made';

// Open forms by primitive uuid; they survive the page's re-renders, and the page does not refresh while one is open.
export const forms = new SvelteMap();
// The last save's confirmation per card, shown until the next change.
export const notices = new SvelteMap();
// Saved pairs by primitive uuid (GET /api/combinations?q=), read once per card.
export const pairs = new SvelteMap();
const pairRequests = new Map();

const size = () => window.SideData?.size() || 64;
async function readJSON(response, fallback) {
  let data = {};
  try { data = await response.json(); } catch { /* no body */ }
  if (!response.ok) throw Error(data.error || fallback);
  return data;
}
const post = async (url, body, fallback) => readJSON(await fetch(url, {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(body)}), fallback);
const iconURL = (key, sha) => '/api/icon-artwork/svg?' + new URLSearchParams({icon: key, ...(sha ? {v: sha.slice(0, 12)} : {})});
export const iconName = i => i?.icon?.replace(/-/g, ' ') || '';
// What a saved pair uses for a part: its icon's name, or the name of the icon still to draw.
export const partName = (r, role) => r[role + 's']?.length ? iconName(r[role + 's'][0]) : 'to draw: ' + (r[role + '_name'] || '?');
export const combinedURL = (uuid, version) => 'combination-previews/' + encodeURIComponent(uuid) + '.svg' + (version ? '?v=' + encodeURIComponent(version) : '');

// The side pair of a reference as the old list gave it: {row: {id, position, mains, subs}, status}.
export function pairEntry(item) {
  const part = role => item.parts.find(p => p.role === role) || {}, m = part('main'), s = part('sub');
  const icon = p => p.icon ? [{icon: p.icon.split('/')[1], family: p.icon.split('/')[0], model_key: p.icon, preview_url: iconURL(p.icon, p.current_sha)}] : [];
  const status = !m.icon && !s.icon ? 'needs_both' : !m.icon ? 'needs_main' : !s.icon ? 'needs_sub' : item.state === 'built' ? 'generated' : 'waiting';
  const formKey = f => f && !f.native_text ? (f.model_key || f.family + '/' + f.icon) : null;
  return {row: {id: item.reference_id, position: s.position, mains: icon(m), subs: icon(s), generated: item.icon ? {at: item.icon.svg_sha256} : null,
                main_name: m.icon ? null : m.draw_name || null, sub_name: s.icon ? null : s.draw_name || null, forms: {main: formKey(m.form), sub: formKey(s.form)}},
          status, main: m.icon ? {preview_url: icon(m)[0].preview_url} : null, sub: s.icon ? {preview_url: icon(s)[0].preview_url} : null};
}
export function loadPair(uuid) {
  if (pairRequests.has(uuid)) return pairRequests.get(uuid);
  const request = fetch('/api/combinations?' + new URLSearchParams({kind: 'side', size: String(size()), q: uuid, limit: '5', forms: '1'}), {cache: 'no-store'})
    .then(r => r.ok ? r.json() : {items: []}).catch(() => ({items: []}))
    .then(data => { const item = data.items.find(i => i.reference_id === uuid);if (item) pairs.set(uuid, pairEntry(item)); else pairs.delete(uuid); });
  pairRequests.set(uuid, request);return request;
}

// Icons that can be the main or sub of a side pair of the page's size, approved first (GET /api/combinations/candidates).
// A phrase with no match (a brief name, "Idea lightbulb") is looked up word by word, longest first.
export async function findCandidates(role, query) {
  const ask = async q => (await readJSON(await fetch('/api/combinations/candidates?' + new URLSearchParams({role, size: String(size()), q}), {cache: 'no-store'}), 'Search failed.'))
    .map(c => ({key: c.key, icon_id: c.key.split('/')[1], name: c.name, approved: c.review === 'approve', preview_url: iconURL(c.key, c.svg_sha256 || '')}));
  const found = await ask(query.trim());
  if (found.length || !query.trim()) return found;
  const seen = new Map();
  for (const word of query.toLowerCase().split(/[^a-z0-9]+/).filter(w => w.length > 2).sort((a, b) => b.length - a.length)) {
    for (const c of await ask(word)) if (!seen.has(c.key)) seen.set(c.key, c);
  }
  return [...seen.values()].slice(0, 40);
}

// Save the pair in D1: make it (a primitive's first save), pick its icons or names to draw, and save a changed side
// with a build composed in this browser (the side is stored with the pair's build). → {pair, status} or {removed}.
export async function savePair(row, body) {
  const id = row.uuid;
  if (body.remove) {
    const saved = pairs.get(id);
    if (row.published && saved) {
      for (const role of ['main', 'sub']) if (saved.row.forms[role]) await post('/api/combinations/parts', {reference_id: id, role, icon: saved.row.forms[role], size: size()}, 'Could not restore the published icons.');
    } else await post('/api/combinations/pair', {reference_id: id, remove: true}, 'Could not remove the side pair.');
    return {removed: true};
  }
  if (!pairs.has(id)) await post('/api/combinations/pair', {reference_id: id, position: body.position || 'br'}, 'Could not make the side pair.');
  for (const role of ['main', 'sub']) {
    if (body[role]) await post('/api/combinations/parts', {reference_id: id, role, icon: body[role], size: size()}, 'Could not save the ' + role + '.');
    // No icon fits yet: the part keeps the name of the one to draw (shown on the side page until one is picked).
    else if (body[role + '_name'] !== undefined) await post('/api/combinations/parts', {reference_id: id, role, draw_name: body[role + '_name'] || null, size: size()}, 'Could not save the ' + role + ' to draw.');
  }
  let got = await window.SideData?.refresh(id);
  const sub = got?.item.parts.find(p => p.role === 'sub');
  if (got && body.position && sub?.position !== body.position && got.item.parts.every(p => p.icon || p.form?.native_text)) {
    const composed = await window.SideData.compose(id, {position: body.position});
    const [built] = await window.SideData.build([composed.request]);
    if (!built?.ok) throw Error(built?.error || 'Could not save the side.');
    got = await window.SideData.refresh(id);
  }
  const entry = got ? pairEntry(got.item) : null;
  if (entry) pairs.set(id, entry);
  return entry ? {pair: entry.row, status: entry.status} : {pair: {id, position: body.position, mains: [], subs: []}, status: 'needs_both'};
}
export function pairBody(form) {
  const part = role => form.draw[role] !== null ? {[role + '_name']: form.draw[role].trim()} : form[role] && form[role] !== form.saved?.[role] ? {[role]: form[role]} : {};
  return {...part('main'), ...part('sub'), position: form.position};
}

// A form for a pair: its saved icons (or names to draw), then searches from the primitive's briefs or the pair's icons.
export async function openForm(row) {
  await loadPair(row.uuid);
  const saved = pairs.get(row.uuid), r = saved?.row;notices.delete(row.uuid);
  const form = $state({uuid: row.uuid, loaded: false, busy: false, message: '', main: '', sub: '', position: r?.position || row.position || '',
                       queries: {main: '', sub: ''}, candidates: {main: [], sub: []}, chosen: {main: null, sub: null}, draw: {main: null, sub: null},
                       brief: {main: '', sub: ''}, saved: {}, sub_position: null});
  // A saved pair opens as it was saved: its icons.
  for (const role of ['main', 'sub']) {
    const i = r?.[role + 's']?.[0];
    if (i) { form[role] = form.saved[role] = i.model_key;form.chosen[role] = {key: i.model_key, icon_id: i.icon, name: iconName(i), preview_url: saved?.[role]?.preview_url || i.preview_url}; }
    else if (r?.[role + '_name']) form.draw[role] = r[role + '_name'];
  }
  forms.set(row.uuid, form);
  try {
    // The searches start from the primitive's classification briefs, or a published pair's icon names.
    const statuses = await fetch('/api/primitives/status', {cache: 'no-store'}).then(x => x.ok ? x.json() : {}).catch(() => ({}));
    const status = statuses[row.uuid] || {};
    const brief = b => typeof b === 'string' ? (() => { try { return JSON.parse(b); } catch { return {name: b}; } })() : b;
    for (const role of ['main', 'sub']) {
      const name = brief(status[role + '_brief'])?.name || row.current?.[role]?.name || (r?.[role + 's']?.[0] ? iconName(r[role + 's'][0]) : '');
      form.queries[role] = form.brief[role] = name || '';form.candidates[role] = await findCandidates(role, form.queries[role]);
      // A published pair opens with what it uses now; a new pair with the best match of the brief name.
      const now = !r && row.current?.[role];
      if (now) { form[role] = now.key;form.chosen[role] = now; }
      else if (!r && form.candidates[role][0]) { form[role] = form.candidates[role][0].key;form.chosen[role] = form.candidates[role][0]; }
    }
    const codes = {'bottom-right': 'br', 'bottom-left': 'bl', 'top-right': 'tr', 'top-left': 'tl', right: 'ri', left: 'le', bottom: 'bo', top: 'to'};
    form.position ||= codes[status.sub_position] || '';form.sub_position = status.sub_position;
  } catch (error) { form.message = error.message; }
  form.loaded = true;
}
export async function send(row, form, body, working) {
  form.busy = true;form.message = working;
  try { return await savePair(row, body); }
  catch (error) { form.message = error.message;return null; }
  finally { form.busy = false; }
}
