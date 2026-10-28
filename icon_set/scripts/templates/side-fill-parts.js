/* Fill main icons and Fill sub icons (side-fill-mains.html, side-fill-subs.html; body[data-role] picks which).

   One keyset page of the parts the fill side pairs use (SideFillData.partsPage): each card is the part's own icon
   (its outline) and its fill variant icons with their Icon review status, the pairs that use it, and why a part
   has no fill. Each drawing is an image of the icon's current revision, so a redraw shows at once. */
(function () {
  'use strict';
  const $ = id => document.getElementById(id);
  const role = document.body.dataset.role === 'sub' ? 'sub' : 'main';
  const {partsPage, artBox, iconUrl} = window.SideFillData;
  const PER_PAGE = 48;
  const params = new URLSearchParams(location.search);
  const state = {status: params.get('status') || 'all', cursors: [null], at: 0, q: params.get('q') || ''};
  const KINDS = role === 'main'
    ? [['all', 'All'], ['ready', 'Filled'], ['outline', 'Outline only'], ['redrawn', 'Source changed'], ['no-fill', 'No fill'], ['no-source', 'No source'], ['not-drawn', 'Not drawn']]
    : [['all', 'All'], ['ready', 'Filled'], ['outline', 'Outline only'], ['text', 'Text subs'], ['redrawn', 'Source changed'], ['no-fill', 'No fill'], ['no-source', 'No source']];
  const NAMES = Object.fromEntries(KINDS);
  const BADGE = {ready: 'done', outline: 'review', redrawn: 'fail', 'no-fill': 'fail', 'no-source': 'fail', 'not-drawn': 'missing', text: 'text'};
  const REVIEW = {approve: 'approved', disapprove: 'disapproved', ready: 'ready'};
  let token = 0, counts = {};

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
        variants.append(figure(v.variant, iconUrl(v.key, v.svg_sha256), v.review));
      }
    }
    el.append(variants);
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
