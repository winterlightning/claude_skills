/* Fill main icons and Fill sub icons (side-fill-mains.html, side-fill-subs.html; body[data-role] picks which).

   One keyset page of the parts the fill side pairs use (SideFillData.partsPage): each card is the part's own icon
   (its outline) and its fill variant icons with their Icon review status, the pairs that use it, and why a part
   has no fill. Each drawing is an image of the icon's current revision, so a redraw shows at once. Signed in, a
   variant's Replace takes an SVG as its new drawing and Add fill stores a new variant (POST /api/icons/styled, style
   fill, as the uploader does): Ready in Icon review again, and every pick using it shows Build again. */
(function () {
  'use strict';
  const $ = id => document.getElementById(id);
  const role = document.body.dataset.role === 'sub' ? 'sub' : 'main';
  const {partsPage, artBox, iconUrl} = window.SideFillData;
  const PER_PAGE = 48;
  const params = new URLSearchParams(location.search);
  const state = {status: params.get('status') || 'all', cursors: [null], at: 0, q: params.get('q') || ''};
  const KINDS = role === 'main'
    ? [['all', 'All'], ['ready', 'Filled'], ['outline', 'Outline only'], ['redrawn', 'Needs a new layout'], ['no-fill', 'No fill'], ['no-source', 'No source'], ['not-drawn', 'Not drawn']]
    : [['all', 'All'], ['ready', 'Filled'], ['outline', 'Outline only'], ['text', 'Text subs'], ['redrawn', 'Needs a new layout'], ['no-fill', 'No fill'], ['no-source', 'No source']];
  const NAMES = Object.fromEntries(KINDS);
  const BADGE = {ready: 'done', outline: 'review', redrawn: 'fail', 'no-fill': 'fail', 'no-source': 'fail', 'not-drawn': 'missing', text: 'text'};
  const REVIEW = {approve: 'approved', disapprove: 'disapproved', ready: 'ready'};
  let token = 0, counts = {};

  // An SVG file chosen by the reviewer, stored as the part's fill variant (replacing the drawing it has).
  function chooseSvg(onText) {
    const input = document.createElement('input');
    input.type = 'file';input.accept = '.svg,image/svg+xml';
    input.addEventListener('change', async () => { if (input.files[0]) onText(await input.files[0].text()); });
    input.click();
  }
  // `expected`: the drawing the card showed (Replace), or null to only create one (Add fill). A drawing changed by
  // someone else meanwhile is reported, never overwritten.
  async function storeFill(part, variant, svg, expected) {
    $('headline').textContent = `Saving ${variant} of ${part.key}…`;
    try {
      const response = await fetch('/api/icons/styled', {method: 'POST', credentials: 'same-origin', headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({items: [{source_key: part.key, style: 'fill', variant, svg, expected_sha256: expected}], replace: true})});
      const answer = await response.json().catch(() => ({}));
      if (!response.ok) throw Error(answer.error || response.statusText);
      const refused = answer.errors?.[0];
      if (refused?.conflict) throw Error(expected === null ? `a variant named ${variant} exists already: Replace it instead`
        : 'someone changed this variant since the page loaded: reload and try again');
      if (refused) throw Error(refused.error);
      const outcome = answer.results?.[0]?.outcome;
      await load();
      $('headline').textContent = outcome === 'unchanged' ? `${variant} of ${part.key} already has that drawing.`
        : `${variant} of ${part.key} saved: Ready in Icon review; its pairs show Build again.`;
    } catch (error) { $('headline').textContent = `Could not save ${variant} of ${part.key}: ${error.message}`; }
  }
  function action(text, title, onClick) {
    const b = document.createElement('button');
    b.type = 'button';b.className = 'sf-part-action login-only';b.textContent = text;b.title = title;
    b.addEventListener('click', onClick);
    return b;
  }

  function figure(caption, url, review) {
    const f = document.createElement('figure');
    f.dataset.status = review === 'approve' ? 'approved' : review === 'disapprove' ? 'rejected' : 'ready';
    const c = document.createElement('figcaption');
    c.textContent = `${caption} · ${REVIEW[review] || review || 'ready'}`;
    f.append(artBox(url, {empty: 'None'}), c);
    return f;
  }

  function card(part) {
    const el = document.createElement('article');
    el.className = 'sc-tile';el.dataset.status = part.status === 'ready' ? 'done' : part.status === 'text' ? 'text' : 'failing';
    const title = document.createElement('h3');title.textContent = part.key.split('/').pop();title.title = part.key;
    const badges = document.createElement('div');badges.className = 'sc-badges';
    const badge = document.createElement('span');badge.className = 'sc-badge ' + (BADGE[part.status] || '');badge.textContent = NAMES[part.status] || part.status;
    const uses = document.createElement('span');uses.className = 'sc-badge';uses.textContent = `${part.pair_count} pair${part.pair_count === 1 ? '' : 's'}`;
    badges.append(badge, uses);
    el.append(title, badges);
    const variants = document.createElement('div');variants.className = 'sf-variants';
    if (part.status === 'text') {
      const f = document.createElement('figure');
      const art = document.createElement('div');art.className = 'sf-art sf-text';art.textContent = part.text || '?';
      const c = document.createElement('figcaption');c.textContent = 'text sub (typeface)';
      f.append(art, c);variants.append(f);
    } else {
      if (part.source_sha256) variants.append(figure('outline', iconUrl(part.key, part.source_sha256), part.source_review));
      const order = v => v.variant === 'current' || v.variant === 'fill' ? '' : v.variant;
      for (const v of [...part.variants].sort((a, b) => order(a).localeCompare(order(b), undefined, {numeric: true}))) {
        const f = figure(v.variant, iconUrl(v.key, v.svg_sha256), v.review);
        f.append(action('Replace', `Choose an SVG as the new drawing of ${v.key}`, () => chooseSvg(svg => storeFill(part, v.variant, svg, v.svg_sha256))));
        variants.append(f);
      }
    }
    el.append(variants);
    if (part.status !== 'text' && part.source_sha256) {
      const base = role === 'main' ? 'current' : 'fill';
      el.append(action('Add fill…', `Store an SVG as a new fill variant of ${part.key}: ${base}, or a name such as region-5`, () => {
        const name = document.createElement('input');
        name.className = 'sf-variant-name';name.value = part.variants.some(v => v.variant === base) ? 'region-' : base;
        name.setAttribute('aria-label', 'Variant name');name.title = `${base}, or a short name: letters, digits, hyphens`;
        const go = action('Choose SVG', 'Choose the SVG for this variant', () => {
          const variant = name.value.trim().toLowerCase();
          if (!/^[a-z0-9-]{1,60}$/.test(variant)) { $('headline').textContent = 'A variant name is letters, digits and hyphens.';return; }
          chooseSvg(svg => storeFill(part, variant, svg, null));
        });
        const row = document.createElement('div');row.className = 'sf-add-row';row.append(name, go);
        el.querySelector('.sf-add-row')?.remove();el.append(row);name.focus();
      }));
    }
    if (part.note) { const n = document.createElement('p');n.className = 'sf-note';n.textContent = part.note;el.append(n); }
    return el;
  }

  function stats() {
    $('stats').replaceChildren(...KINDS.filter(([key]) => key === 'all' || counts[key]).map(([key, name]) => {
      const button = document.createElement('button');
      button.type = 'button';button.className = 'sc-stat';button.setAttribute('aria-pressed', String(state.status === key));
      button.innerHTML = '<span></span><strong></strong>';
      button.querySelector('span').textContent = name;button.querySelector('strong').textContent = (counts[key] || 0).toLocaleString();
      button.addEventListener('click', () => { state.status = key;restart(); });
      return button;
    }));
  }

  function pager(nav, next) {
    const button = (text, onClick, off) => {
      const b = document.createElement('button');
      b.type = 'button';b.textContent = text;b.disabled = off;
      b.addEventListener('click', () => { onClick();if (nav.id === 'pagerBottom') $('grid').scrollIntoView(); });
      return b;
    };
    const info = document.createElement('span');info.className = 'sc-note';
    const total = counts[state.status] || 0;
    info.textContent = state.q ? `Page ${state.at + 1} · names starting “${state.q}”`
      : `Page ${state.at + 1} of ${Math.max(1, Math.ceil(total / PER_PAGE))} · ${total.toLocaleString()} ${role}s`;
    nav.replaceChildren(button('« First', () => { state.at = 0;load(); }, state.at === 0),
                        button('‹ Prev', () => { state.at--;load(); }, state.at === 0), info,
                        button('Next ›', () => { state.cursors[state.at + 1] = next;state.at++;load(); }, !next));
  }

  async function load() {
    const mine = ++token;
    $('headline').textContent = 'Loading…';
    let page;
    try { page = await partsPage({role, status: state.status === 'all' ? null : state.status, after: state.cursors[state.at], limit: PER_PAGE, q: state.q}); }
    catch (error) { $('headline').textContent = `Could not load the ${role}s: ${error.message}`;return; }
    if (mine !== token) return;
    counts = page.counts;stats();
    $('grid').replaceChildren(...(page.parts.length ? page.parts.map(card) : [Object.assign(document.createElement('p'), {className: 'sc-empty', textContent: 'Nothing matches.'})]));
    for (const nav of [$('pagerTop'), $('pagerBottom')]) pager(nav, page.next);
    $('headline').textContent = `${page.parts.length} ${role}s on this page`;
    const url = new URL(location.href);
    for (const [k, v] of [['status', state.status === 'all' ? '' : state.status], ['q', state.q]]) v ? url.searchParams.set(k, v) : url.searchParams.delete(k);
    history.replaceState(null, '', url);
  }
  function restart() { state.cursors = [null];state.at = 0;load(); }

  let typing;
  $('search').value = state.q;
  $('search').placeholder = 'Name starts with…';
  $('search').addEventListener('input', () => { clearTimeout(typing);typing = setTimeout(() => { state.q = $('search').value.trim().toLowerCase();restart(); }, 250); });
  load();
})();
