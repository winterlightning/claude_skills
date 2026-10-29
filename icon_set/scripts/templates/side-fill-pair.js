/* One fill side pair (side-fill-pair.html?id=…): its picks, every candidate, its parts, and the layout editor.

   The pair (its picks, its parts' fill variants) is one D1 read (GET /api/side-fill/pair); the drawings of its parts
   are one more (GET /api/combinations/drawings). Everything shown is combined here, from the parts' current drawings,
   by side-fill-combine.js: a redrawn part shows at once. A pick is a pair of icons and their boxes
   (POST /api/side-fill/pick); its combined icon is the drawing made here, saved with POST /api/side-fill/build into
   Icon review as Ready. The first pick is the pair's output; the others are alternatives in order. The pair's
   normal Side combination 64 icon (its original) comes with the pair and is shown above the picks. */
(function () {
  'use strict';
  const $ = id => document.getElementById(id);
  const D = window.SideFillData, Fill = window.SideFillCombine, Layout = window.SideFillLayout;
  const {overlay, label, keyshape} = window.SideFillOverlay;
  const id = new URLSearchParams(location.search).get('id');
  let pair = null, drawings = {}, busy = false, renders = new Map(), token = 0;
  const MAX_PICKS = 9;

  const status = (text, bad = false) => { $('status').textContent = text;$('status').style.color = bad ? '#b91c1c' : ''; };
  const yieldFrame = () => new Promise(resolve => setTimeout(resolve, 0));
  function button(text, onClick, cls = '') {
    const b = document.createElement('button');
    b.type = 'button';b.textContent = text;b.className = cls;b.disabled = busy;
    b.addEventListener('click', onClick);
    return b;
  }

  // The parts as the engine takes them: a fill variant icon, or the solo / sub icon itself for the outline.
  function part(role, key, layout) {
    const source = drawings[pair[role]], icon = drawings[key];
    if (!source?.svg || !icon?.svg) throw new Error(`The ${role} drawing is not available.`);
    return {svg: icon.svg, source: source.svg, layout, outline: key === pair[role], sha: icon.svg_sha256};
  }
  // The pair's own placement. A drawing with transforms cannot be split into elements: its boxes are used as stored
  // (a box over all its elements places it whole, as the engine does).
  function baseLayout(role) {
    let sources = [];
    try { sources = Layout.elements(drawings[pair[role]].svg).sources; } catch (error) { /* placed whole */ }
    return D.units(pair.layout?.[role], sources);
  }
  // Main choices: its fill variants (current first) and the outline; sub choices: its fill and the outline.
  function choices(role) {
    const variants = [...(pair[`${role}_variants`] || [])].sort((a, b) => (a.variant !== 'current') - (b.variant !== 'current') || a.variant.localeCompare(b.variant));
    return [...variants.map(v => ({key: v.key, name: v.variant, review: v.review})), {key: pair[role], name: 'outline', review: drawings[pair[role]]?.review}];
  }
  const keyOfName = (role, name) => choices(role).find(c => c.name === name)?.key;

  // Combined here (cached by its inputs): {svg} or {error}.
  function render(main, sub, options) {
    const cacheKey = JSON.stringify([main.key, drawings[main.key]?.svg_sha256, main.layout, sub.key, drawings[sub.key]?.svg_sha256, sub.layout, options]);
    if (!renders.has(cacheKey)) {
      try { renders.set(cacheKey, {svg: Fill.combine({main: part('main', main.key, main.layout), sub: part('sub', sub.key, sub.layout), options}).svg}); }
      catch (error) { renders.set(cacheKey, {error: error.message}); }
    }
    return renders.get(cacheKey);
  }

  async function act(work, done) {
    busy = true;draw();
    try { await work();await load();status(done); }
    catch (error) { status(error.message, true); }
    finally { busy = false;draw(); }
  }
  // Save a pick (icons and boxes), then build its combined icon from what is shown. `mode`: 'append' adds it after
  // the last pick, 'insert' puts it in at `rank` (the picks from there on move down one), 'replace' changes the pick
  // at `rank`. Each names the pair version this page shows, so a pair changed elsewhere is refused, never overwritten.
  async function savePick(rank, main, sub, options, mode) {
    const saved = await D.pick({reference_id: pair.id, rank, append: mode === 'append', insert: mode === 'insert', version: pair.version,
                                main: main.key, sub: sub.key, layout: {main: main.layout, sub: sub.layout}, options});
    await buildPick(saved.rank, main, sub, options, saved.version);
  }
  async function buildPick(rank, main, sub, options, version = pair.version) {
    const result = render(main, sub, options);
    if (result.error) throw new Error(`Saved the pick, but it cannot be combined: ${result.error}`);
    const answer = await D.build({reference_id: pair.id, rank, version, svg: result.svg,
      main: {icon: main.key, svg_sha256: drawings[main.key].svg_sha256}, sub: {icon: sub.key, svg_sha256: drawings[sub.key].svg_sha256}});
    return answer;
  }
  const full = () => pair.picks.length >= MAX_PICKS;

  function tile({main, sub, options, pick}) {
    const card = document.createElement('article');
    card.className = 'sf-tile';
    if (pick) card.dataset.picked = '';
    const result = render(main, sub, options);
    const ks = keyshape(main.layout, sub.layout);
    card.append(D.artBox(null, {svg: result.svg, overlay: overlay(ks), empty: result.error ? 'Cannot combine' : 'No artwork'}));
    const name = document.createElement('h3');
    name.textContent = `${D.labelOf(pair, 'main', main.key)} + ${D.labelOf(pair, 'sub', sub.key)}`;name.title = `${main.key}\n${sub.key}`;
    const ksLine = document.createElement('p');
    ksLine.className = 'sf-ks ' + (ks?.ok === false ? 'bad' : 'ok');ksLine.textContent = result.error || label(ks);
    card.append(name, ksLine);
    const actions = document.createElement('div');actions.className = 'sf-actions';
    if (pick) {
      const order = document.createElement('p');order.className = 'order';
      const built = pick.combined;
      order.textContent = `Pick ${pick.rank} of ${pair.picks.length}${pick.rank === 1 ? ' · the output' : ''}`;
      const state = document.createElement('p');state.className = 'sf-flag';
      state.textContent = !built ? 'Not built: Build saves it to Icon review' : D.stale(pick) ? 'A part was redrawn: Build again'
        : `Built · Icon review: ${built.review}${built.build_failed ? ' · a part is not approved yet' : ''}`;
      card.append(order, state);
      if (!built || D.stale(pick)) actions.append(button('Build', () => act(() => buildPick(pick.rank, main, sub, options), `Pick ${pick.rank} built: it is in Icon review as Ready.`), 'primary'));
      if (pick.rank !== 1) actions.append(button('Make the output', () => act(() => D.move({reference_id: pair.id, rank: pick.rank, to: 1, version: pair.version}),
        'This pick is now the output; the others moved down one.')));
      actions.append(button('Adjust layout', () => editLayout({main, sub, options, rank: pick.rank})));
      actions.append(button('Remove', () => act(() => D.unpick({reference_id: pair.id, rank: pick.rank, version: pair.version}), `Pick ${pick.rank} removed.`), 'danger'));
    } else {
      // A pair keeps at most 9 picks: adding is off then (replace or remove a pick instead).
      const add = button(pair.picks.length ? 'Add as next pick' : 'Pick as output', () => act(() => savePick(null, main, sub, options, 'append'),
        pair.picks.length ? 'Added as the next pick.' : 'Picked as the output.'), 'primary');
      const first = button('Make the output', () => act(() => savePick(1, main, sub, options, 'insert'),
        'This combination is now the output; the other picks moved down one.'));
      for (const b of [add, first]) if (full()) { b.disabled = true;b.title = `A pair keeps at most ${MAX_PICKS} picks: remove one first.`; }
      actions.append(add);
      if (pair.picks.length) actions.append(first);
      actions.append(button('Adjust layout', () => editLayout({main, sub, options, rank: null})));
    }
    card.append(actions);
    return card;
  }

  // The layout editor on one combination; saving gives that pick (or a new one) these boxes.
  function editLayout({main, sub, options, rank}) {
    const mains = choices('main'), subs = choices('sub');
    const row = {id: pair.id, concept: pair.concept, variants: mains.map(c => c.name), sub: {has_fill: subs.length > 1}};
    const candidate = {base_variant: D.labelOf(pair, 'main', main.key), sub_variant: sub.key === pair.sub ? 'outline' : 'fill',
                       label: rank ? `pick ${rank}` : 'new pick', units: {main: main.layout, sub: sub.layout}};
    // The sub the editor's "fill" means is the one this combination uses (a sub can have several fills).
    const subKey = name => D.subFor(name, sub.key, pair.sub, subs.filter(c => c.name !== 'outline'));
    const backend = {
      keyshapes: D.keyshapes,
      elements: async () => Object.fromEntries(['main', 'sub'].map(role => {
        const parts = Layout.elements(drawings[pair[role]].svg);
        return [role, {...parts, units: baseLayout(role)}];
      })),
      preview: async proposal => {
        const mainKey = keyOfName('main', proposal.base_variant) || main.key, sKey = subKey(proposal.sub_variant) || sub.key;
        const keyshapes = await D.keyshapes();
        return Layout.preview({keyshapes, position: pair.id.slice(-2), options,
                               main: part('main', mainKey), sub: part('sub', sKey), proposal});
      },
      save: async (proposal, result) => {
        const mainKey = keyOfName('main', proposal.base_variant) || main.key, sKey = subKey(proposal.sub_variant) || sub.key;
        const boxes = result.candidate.layout_boxes;
        if (!rank && full()) throw new Error(`A pair keeps at most ${MAX_PICKS} picks: remove one before adding this layout.`);
        await act(() => savePick(rank, {key: mainKey, layout: boxes.main}, {key: sKey, layout: boxes.sub}, options, rank ? 'replace' : 'append'),
                  rank ? `Layout saved into pick ${rank} and built.` : 'Layout saved as a new pick and built.');
        return {variant: rank ? `pick ${rank}` : 'new pick'};
      },
    };
    window.SideLayoutEditor.open(row, candidate, null, backend);
  }

  async function draw() {
    if (!pair) return;
    const mine = ++token;
    const picks = [...pair.picks].sort((a, b) => a.rank - b.rank);
    const pickedTiles = [];
    for (const p of picks) {
      if (!p.main || !p.sub) continue;
      pickedTiles.push(tile({main: {key: p.main.icon, layout: p.main.layout}, sub: {key: p.sub.icon, layout: p.sub.layout}, options: p.options, pick: p}));
      await yieldFrame();
      if (mine !== token) return;
    }
    $('picks').replaceChildren(...(pickedTiles.length ? pickedTiles
      : [Object.assign(document.createElement('p'), {className: 'sc-empty', textContent: 'Nothing picked yet: pick a candidate below.'})]));
    $('picksNote').textContent = pickedTiles.length ? 'The first pick is the pair’s output; later picks are alternatives in order. Each is built into Icon review.' : '';
    // Every main choice with every sub choice, on the pair's own placement, less what is picked already.
    const taken = new Set(picks.map(p => `${p.main?.icon}|${p.sub?.icon}|${JSON.stringify(p.main?.layout)}|${JSON.stringify(p.sub?.layout)}`));
    const base = {main: baseLayout('main'), sub: baseLayout('sub')};
    const candidates = [];
    $('candidates').replaceChildren(Object.assign(document.createElement('p'), {className: 'sc-note', textContent: 'Combining…'}));
    for (const m of choices('main')) {
      for (const s of choices('sub')) {
        if (m.name === 'outline' && s.name === 'outline') continue;    // a fill side pair needs a filled main or sub
        if (taken.has(`${m.key}|${s.key}|${JSON.stringify(base.main)}|${JSON.stringify(base.sub)}`)) continue;
        candidates.push(tile({main: {key: m.key, layout: base.main}, sub: {key: s.key, layout: base.sub}, options: null}));
        await yieldFrame();
        if (mine !== token) return;
      }
    }
    $('candidates').replaceChildren(...(candidates.length ? candidates : [Object.assign(document.createElement('p'), {className: 'sc-empty',
      textContent: choices('main').length + choices('sub').length === 2 ? 'Neither the main nor the sub has a fill: this pair has no fill version.'
        : 'Every candidate is picked already.'})]));
    parts();
  }

  function original() {
    const o = pair.original, card = document.createElement('article');
    card.className = 'sf-tile';
    const caption = document.createElement('p');
    caption.textContent = o ? `${o.key} · ${o.review === 'approve' ? 'approved' : o.review}` : `No normal icon side_combination64/${pair.id}`;
    caption.title = caption.textContent;
    card.append(D.artBox(o ? D.iconUrl(o.key, o.svg_sha256) : null, {empty: 'No normal icon'}), caption);
    $('original').replaceChildren(card);
  }

  function parts() {
    const figures = [];
    for (const role of ['main', 'sub']) {
      for (const c of choices(role)) {
        const f = document.createElement('figure');
        f.dataset.status = c.review === 'approve' ? 'approved' : c.review || 'ready';
        const caption = document.createElement('figcaption');
        caption.textContent = `${role} ${c.name} · ${c.review === 'approve' ? 'approved' : c.review || 'ready'}`;
        f.append(D.artBox(D.iconUrl(c.key, drawings[c.key]?.svg_sha256)), caption);
        figures.push(f);
      }
    }
    $('parts').replaceChildren(...figures);
  }

  async function load() {
    pair = await D.pair(id);
    const keys = [pair.main, pair.sub, ...pair.main_variants.map(v => v.key), ...pair.sub_variants.map(v => v.key),
                  ...pair.picks.flatMap(p => [p.main?.icon, p.sub?.icon])];
    drawings = await D.drawings(keys);
  }

  async function start() {
    if (!id) { $('title').textContent = 'No pair chosen';status('Open a pair from Fill side pairs.', true);return; }
    try { await load(); }
    catch (error) { $('title').textContent = 'Pair not available';status(error.message, true);return; }
    document.title = `${pair.concept} · Fill side pair`;
    $('title').textContent = pair.concept;
    $('subtitle').textContent = `${pair.main} + ${pair.sub} · ${pair.id.slice(-2)} · ${pair.id} · ${pair.state}`;
    const go = to => { location.search = '?id=' + encodeURIComponent(to); };
    $('prev').disabled = !pair.neighbours?.previous;$('next').disabled = !pair.neighbours?.next;
    $('prev').onclick = () => go(pair.neighbours.previous);$('next').onclick = () => go(pair.neighbours.next);
    original();
    // A pair the import could not combine can still be picked once a part has a fill (Add fill on the parts pages).
    if (pair.state === 'uncombined' && !(pair.main && pair.sub && (pair.main_variants.length || pair.sub_variants.length))) {
      status(pair.note || 'The combine cannot draw this pair.', true);
      return;
    }
    draw().catch(error => status(`This pair cannot be shown: ${error.message}`, true));
  }
  start();
})();
