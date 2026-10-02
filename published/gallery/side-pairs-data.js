/* Side pairs from D1, for the Progression › Side page (side-pairs-grid.js, side-layout-editor.js, side-pair-maker.js).

   The page reads what it used to read from the published files (experiment-combination.json, its results,
   combinations.json, side-combination64.json) and the side routes, in the same shapes, from the combination tables:
   GET /api/combinations (pairs, picked icons, layouts, builds, forms), /api/side-components (each main / sub source
   with its drawings and status), /api/reviews. Combined icons are composed here by combine-side.js; the Worker only
   stores what the browser built (POST /api/combinations/build). */
(function () {
  'use strict';
  const PAGE = 500;
  // The pair size: 64 (a 48 main and a 32 sub) or 72 (a main-54 and a sub-36). The page switches it and loads again.
  const SIZES = {64: {canvas: 64, main: 48, sub: 32, mainFamily: 'solo', subFamily: 'sub', combined: 'side_combination64'},
                 72: {canvas: 72, main: 54, sub: 36, mainFamily: 'main-54', subFamily: 'sub-36', combined: 'combination-72'}};
  let SIZE = 64;
  function setSize(size) { SIZE = SIZES[size] ? Number(size) : 64; items.clear(); drawings.clear(); return SIZE; }
  const items = new Map();       // reference id → /api/combinations item (with forms)
  const drawings = new Map();    // icon key → {svg, svg_sha256, review}
  let components = null;

  async function api(path, body) {
    const response = await fetch(path, body === undefined ? {cache: 'no-store'}
      : {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(body)});
    const data = await response.json().catch(() => ({}));
    if (!response.ok) throw Error(data.error || response.statusText);
    return data;
  }
  async function loadDrawings(keys) {
    const wanted = [...new Set(keys.filter(k => k && !drawings.has(k)))];
    for (let i = 0; i < wanted.length; i += 100) {
      const got = await api('/api/combinations/drawings?keys=' + encodeURIComponent(wanted.slice(i, i + 100).join(',')));
      for (const [key, d] of Object.entries(got)) drawings.set(key, d);
    }
  }
  const query = extra => '/api/combinations?' + new URLSearchParams({kind: 'side', size: String(SIZE), forms: '1', ...extra});
  const part = (item, role) => item.parts.find(p => p.role === role) || {role};
  const formKey = f => f && !f.native_text ? (f.model_key || `${f.family}/${f.icon}`) : null;
  const iconURL = (key, sha) => '/api/icon-artwork/svg?' + new URLSearchParams({icon: key, ...(sha ? {v: sha.slice(0, 12)} : {})});

  // A part as the old pair rows listed it (experiment-combination.json's items): the stored form when it describes the
  // picked icon (or a native text sub), else the picked icon by key and picture.
  function partItem(p) {
    let item;
    if (p.form && (p.icon ? formKey(p.form) === p.icon : p.form.native_text)) {
      item = {...p.form, model_key: p.form.model_key || formKey(p.form), sha256: p.form.sha256};
    } else if (p.icon) {
      const [family, name] = p.icon.split('/');
      item = {icon: name, family, model_key: p.icon, sha256: p.current_sha, preview_url: iconURL(p.icon, p.current_sha)};
    } else return null;
    // What the old items also carried, from the drawing's catalog entry: its Python model and validation.
    const drawing = drawingByKey().get(item.model_key);
    if (drawing) Object.assign(item, {python_source: drawing.python_source, model_validation: drawing.status, errors: drawing.errors});
    return item;
  }
  let drawingIndex = null;
  const drawingByKey = () => drawingIndex ??= new Map([...(components?.mains || []), ...(components?.subs || [])]
    .flatMap(c => c.drawings.map(d => [d.key, d])));
  // A pair row (the old sidePairs entry): its main and sub items, side and flags.
  function pairOf(item) {
    const m = part(item, 'main'), s = part(item, 'sub'), main = partItem(m), sub = partItem(s);
    // A pair with no stored forms was made here (From review); one whose picked icon is not its form's changed it.
    // At 72 no part has a form (the 72 drawings are picked, never published), so neither applies there.
    const changed = SIZE === 64 && [m, s].some(p => p.form && p.icon && formKey(p.form) !== p.icon);
    const made = SIZE === 64 && !m.form && !s.form;
    return {id: item.reference_id, concept: item.concept, position: s.position, main_id: m.part_reference_id, sub_id: s.part_reference_id,
            // The name of an icon still to draw for a part with none picked (draw_name, migration 0016).
            main_name: main ? null : m.draw_name || null, sub_name: sub ? null : s.draw_name || null,
            mains: main ? [main] : [], subs: sub ? [sub] : [], native_text: !!sub?.native_text, custom: made || changed, published: changed,
            canvas_width: sub?.native_text ? Math.max(64, SIZE) : SIZE, canvas_height: sub?.native_text ? Math.max(64, SIZE) : SIZE};
  }
  // The old catalog row (combinations.json) and the references its main, sub and pair point at.
  function catalogOf(list) {
    const references = {}, rows = [];
    const component = role => new Map((components?.[role === 'main' ? 'mains' : 'subs'] || []).flatMap(c => [c.id, ...c.source_ids].map(id => [id, c])));
    const mains = component('main'), subs = component('sub');
    const generatedOf = (p, source) => {
      const list = (source?.drawings || []).map(d => ({key: d.key, icon_id: d.icon_id, preview_url: d.preview_url}));
      if (p.icon && !list.some(g => g.key === p.icon)) list.unshift({key: p.icon, icon_id: p.icon.split('/')[1], preview_url: iconURL(p.icon, p.current_sha)});
      return list;
    };
    for (const item of list) {
      const m = part(item, 'main'), s = part(item, 'sub');
      rows.push({id: item.reference_id, concept: item.concept, main_id: m.part_reference_id, sub_id: s.part_reference_id, position: s.position,
                 kind: 'side', remappings: [], generated: item.icon ? [{icon_id: item.reference_id, preview_url: item.icon.preview_url}] : []});
      references[item.reference_id] = {id: item.reference_id, concept: item.concept,
                                       reference_url: 'combination-originals/' + encodeURIComponent(item.reference_id) + '.svg', generated: []};
      for (const [p, sources] of [[m, mains], [s, subs]]) {
        if (!p.part_reference_id) continue;
        const source = sources.get(p.part_reference_id), seen = references[p.part_reference_id];
        const generated = generatedOf(p, source);
        references[p.part_reference_id] = {id: p.part_reference_id, concept: source?.concept || seen?.concept || p.part_reference_id,
                                           generated: seen ? [...seen.generated, ...generated.filter(g => !seen.generated.some(x => x.key === g.key))] : generated};
      }
    }
    return {rows, references};
  }

  // Everything the page loads at once: every side pair (500 a request), the components, reviews and primitive statuses.
  async function load() {
    items.clear();
    const [first, sideComponents, reviews, statuses] = await Promise.all([
      api(query({limit: PAGE, offset: 0})), api('/api/side-components'),
      api('/api/reviews').catch(() => ({})), api('/api/primitives/status').catch(() => ({}))]);
    // At 72 each part's drawing is its picked main-54 / sub-36 icon: the components are built from those picks, with
    // the concepts of the 64 sources (the same part references).
    components = SIZE === 72 ? null : sideComponents;
    drawingIndex = null;
    const concepts = new Map([...sideComponents.mains, ...sideComponents.subs].flatMap(c => [c.id, ...c.source_ids].map(id => [id, c.concept])));
    const pages = [first];
    const rest = [];
    for (let offset = PAGE; offset < first.total; offset += PAGE) rest.push(api(query({limit: PAGE, offset})));
    pages.push(...await Promise.all(rest));
    for (const page of pages) for (const item of page.items) items.set(item.reference_id, item);
    if (SIZE === 72) components = componentsAt72(concepts, reviews);
    return snapshot({reviews, statuses});
  }
  function snapshot(extra = {}) {
    const list = [...items.values()];
    const pairs = new Map(list.map(item => [item.reference_id, pairOf(item)]));
    // A built pair's stored icon is its preview; the rest are composed here when shown.
    const previews = {};
    for (const item of list) if (item.icon) previews[item.reference_id] = {url: item.icon.preview_url, built: true, state: item.state};
    // The combined icons the summary counts (was side-combination64.json): every built pair.
    const run = {count: list.filter(i => i.icon).length, icons: list.filter(i => i.icon).map(i => ({key: i.icon.key}))};
    return {catalog: catalogOf(list), pairs, previews, components, run, ...extra};
  }
  // One pair read again after a change (a build, a new pick): its row, pair and preview.
  async function refresh(id) {
    const data = await api(query({q: id, limit: 5, offset: 0}));
    const item = data.items.find(i => i.reference_id === id);
    if (!item) { items.delete(id); return null; }
    items.set(id, item);
    for (const p of item.parts) if (p.icon) drawings.delete(p.icon);
    return {item, pair: pairOf(item), row: catalogOf([item]).rows[0], references: catalogOf([item]).references,
            preview: item.icon ? {url: item.icon.preview_url, built: true, state: item.state} : null};
  }

  // The 72 parts as side-components.json lists the 64 ones: each main / sub reference with the drawing picked for it
  // (status 'pass': a 72 part has no build check; its review decides whether it counts, as for 64).
  function componentsAt72(concepts, reviews) {
    const byRole = {main: new Map(), sub: new Map()};
    for (const it of items.values()) for (const p of it.parts) {
      const id = p.part_reference_id, list = byRole[p.role];
      if (!id || !list) continue;
      const entry = list.get(id) || {id, concept: concepts.get(id) || id, source_ids: [id], reference_url: 'combination-originals/' + encodeURIComponent(id) + '.svg',
                                      pairs: [], drawings: []};
      entry.pairs.push({id: it.reference_id, concept: it.concept});
      if (p.icon && !entry.drawings.some(d => d.key === p.icon)) {
        const [family, name] = p.icon.split('/');
        entry.drawings.push({key: p.icon, icon_id: name, family, status: 'pass', review: reviews[p.icon] || p.review, preview_url: iconURL(p.icon, p.current_sha),
                             svg_sha256: p.current_sha, errors: [], profile: family.toUpperCase()});
      }
      list.set(id, entry);
    }
    const mains = [...byRole.main.values()], subs = [...byRole.sub.values()];
    return {generated_at: null, mains, subs, counts: {mains: mains.length, subs: subs.length}};
  }

  const item = id => items.get(id);
  // The pair's hand layout (groups listing their elements), or null on automatic placement.
  const handLayout = id => items.has(id) ? CombineSide.handLayout(items.get(id)) : null;
  // Which parts were redrawn since the pair was built.
  const staleRoles = id => (items.get(id)?.parts || []).filter(p => p.stale).map(p => p.role);

  // Compose a pair in the browser from its parts' current drawings → {svg, result, current, request}.
  // `options`: {icons, position, layout} as CombineSide.pairRequest takes them (layout null: automatic).
  async function compose(id, options = {}) {
    const it = items.get(id);
    if (!it) throw Error('Unknown side pair.');
    const icons = options.icons || {main: part(it, 'main').icon, sub: part(it, 'sub').icon};
    await loadDrawings(Object.values(icons));
    return CombineSide.pairRequest(it, drawings, {...options, size: SIZE});
  }
  // Store browser builds, 50 a request → [{reference_id, ok, key, svg_sha256, build_failed, errors} | {ok: false, error}].
  async function build(requests, progress) {
    const results = [];
    for (let i = 0; i < requests.length; i += 50) {
      results.push(...(await api('/api/combinations/build', {size: SIZE, builds: requests.slice(i, i + 50)})).results);
      progress?.(results.length, requests.length);
    }
    return results;
  }
  // Compose and store pairs (Build all, Recombine): those that cannot be drawn are reported, not sent.
  async function buildPairs(ids, progress) {
    const requests = [], skipped = [];
    for (const id of ids) {
      try { requests.push((await compose(id)).request); } catch (error) { skipped.push({reference_id: id, error: error.message}); }
    }
    const results = requests.length ? await build(requests, progress) : [];
    return {results, skipped};
  }

  // A part's elements for the layout editor (side_layout component): markup, names, source boxes and its connected
  // groups as canvas boxes where the composed result placed the part (or its hand layout's groups).
  function elements(composed, role, layout) {
    const form = composed.current.row[role === 'main' ? 'mains' : 'subs'][0];
    const document = form.engine_document ?? form.document;
    const parts = CombineSide.elementParts(document);
    const placed = composed.result.placements[role === 'main' ? 0 : 1].painted_box;
    const auto = {paths: parts.sources.map((b, i) => b ? i : null).filter(i => i !== null), x: placed.x + 2, y: placed.y + 2, w: placed.w - 4, h: placed.h - 4};
    let groups;
    if (layout && layout.length) groups = layout;
    else {
      const {sx, sy} = CombineSide.groupTransform(auto, parts.sources);
      groups = CombineSide.splitGroups([auto], parts.sources, CombineSide.connected(parts.segments, 4 / ((sx + sy) / 2)));
    }
    return {markup: parts.markup, names: parts.names, sources: parts.sources,
            groups: groups.map(g => {
              const source = parts.sources.filter((_b, i) => g.paths.includes(i)).reduce((a, b) => b ? [Math.min(a[0], b[0]), Math.min(a[1], b[1]), Math.max(a[2], b[2]), Math.max(a[3], b[3])] : a, [Infinity, Infinity, -Infinity, -Infinity]);
              return {paths: g.paths, source, box: [g.x, g.y, g.x + g.w, g.y + g.h]};
            })};
  }

  // Other side pairs drawn with this main icon (the layout editor's Apply panel).
  function pairsWithMain(mainKey, exceptId) {
    return [...items.values()].filter(it => it.reference_id !== exceptId && part(it, 'main').icon === mainKey && part(it, 'sub').icon);
  }

  window.SideData = {SIZES, size: () => SIZE, sizes: () => SIZES[SIZE], setSize, load, snapshot, refresh, item, part, handLayout, staleRoles, compose, build, buildPairs, elements,
                     pairsWithMain, loadDrawings, drawings, iconURL, api};
})();
