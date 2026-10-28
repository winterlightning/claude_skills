/* Fill side pairs: the grid of every pair's picked outputs (side-fill.html).

   One keyset page of pairs at a time (SideFillData.pairsPage): a picked pair shows each pick's combined icon in rank
   order, an unpicked pair a link to choose its output, and a pair the combine cannot draw why. Totals come with the
   page, so the filter buttons never count rows. The keyshape overlay is measured from each pick's boxes. */
(function () {
  'use strict';
  const $ = id => document.getElementById(id);
  const {pairsPage, artBox, iconUrl, labelOf, stale} = window.SideFillData;
  const {overlay, label, keyshape} = window.SideFillOverlay;
  const GROUPS = [['all', 'All pairs'], ['picked', 'Picked'], ['unpicked', 'Not picked'], ['uncombined', 'Not combined']];
  const params = new URLSearchParams(location.search);
  const state = {group: params.get('group') || 'all', cursors: [null], at: 0, q: params.get('q') || ''};
  let token = 0, counts = {}, lastPage = null;

  function stats() {
    $('stats').replaceChildren(...GROUPS.map(([key, name]) => {
      const button = document.createElement('button');
      button.type = 'button';button.className = 'sc-stat';button.setAttribute('aria-pressed', String(state.group === key));
      button.innerHTML = '<span></span><strong></strong>';
      button.querySelector('span').textContent = name;button.querySelector('strong').textContent = (counts[key] || 0).toLocaleString();
      button.addEventListener('click', () => { state.group = key;restart(); });
      return button;
    }));
  }

  function tile(pair, pick) {
    const card = document.createElement('article');
    card.className = 'sf-tile';card.dataset.group = pair.state;
    const href = 'side-fill-pair.html?id=' + encodeURIComponent(pair.id);
    const guides = $('guides').getAttribute('aria-pressed') === 'true';
    const ks = pick ? keyshape(pick.main?.layout, pick.sub?.layout) : null;
    const built = pick?.combined;
    card.append(artBox(built ? iconUrl(built.key, built.svg_sha256) : null, {href, overlay: pick && guides ? overlay(ks) : null,
      empty: pair.state === 'uncombined' ? 'Not combined' : pair.state === 'unpicked' ? 'Choose an output' : 'Not built yet'}));
    const title = document.createElement('h3');
    title.textContent = pair.concept || pair.id;title.title = `${pair.concept}\n${pair.main || '—'} + ${pair.sub || '—'}\n${pair.id}`;
    card.append(title);
    const which = document.createElement('p');
    if (!pick) {
      which.className = 'sf-note';which.textContent = pair.note || (pair.state === 'unpicked' ? 'No output picked yet.' : 'Not combined.');
      which.title = which.textContent;card.append(which);
      return card;
    }
    const names = `${pick.main?.label || labelOf(pair, 'main', pick.main?.icon)} + ${pick.sub?.label || labelOf(pair, 'sub', pick.sub?.icon)}`;
    which.className = pair.picks.length > 1 ? 'multi' : '';
    which.textContent = pair.picks.length > 1 ? `${names} · ${pick.rank} of ${pair.picks.length}` : names;which.title = names;
    const ksLine = document.createElement('p');
    ksLine.className = 'sf-ks ' + (ks?.ok === false ? 'bad' : 'ok');ksLine.textContent = label(ks);
    card.append(which, ksLine);
    const flags = [];
    if (stale(pick)) flags.push(built ? 'part redrawn: rebuild' : 'not built');
    if (built?.review && built.review !== 'ready') flags.push(built.review === 'approve' ? 'approved' : built.review);
    if (flags.length) { const f = document.createElement('p');f.className = 'sf-flag';f.textContent = flags.join(' · ');card.append(f); }
    return card;
  }

  function pager(nav, next) {
    const button = (text, onClick, off) => {
      const b = document.createElement('button');
      b.type = 'button';b.textContent = text;b.disabled = off;
      b.addEventListener('click', () => { onClick();if (nav.id === 'pagerBottom') $('grid').scrollIntoView(); });
      return b;
    };
    const info = document.createElement('span');
    info.className = 'sc-note';
    const size = Number($('perPage').value), total = counts[state.group] || 0;
    info.textContent = state.q ? `Page ${state.at + 1} · concepts starting “${state.q}”`
      : `Page ${state.at + 1} of ${Math.max(1, Math.ceil(total / size))} · ${total.toLocaleString()} pairs`;
    nav.replaceChildren(button('« First', () => { state.at = 0;load(); }, state.at === 0),
                        button('‹ Prev', () => { state.at--;load(); }, state.at === 0), info,
                        button('Next ›', () => { state.cursors[state.at + 1] = next;state.at++;load(); }, !next));
  }

  function render() {
    const page = lastPage;
    if (!page) return;
    const offOnly = $('keyshape').value === 'bad';
    const tiles = [];
    for (const pair of page.pairs) {
      const shown = pair.picks.length ? pair.picks : [null];
      for (const pick of shown) {
        if (offOnly && (!pick || keyshape(pick.main?.layout, pick.sub?.layout).ok !== false)) continue;
        tiles.push(tile(pair, pick));
      }
    }
    $('grid').replaceChildren(...(tiles.length ? tiles : [Object.assign(document.createElement('p'), {className: 'sc-empty', textContent: 'No pair matches.'})]));
    $('headline').textContent = `${page.pairs.length} pairs on this page · ${tiles.length} tiles${offOnly ? ' off keyshape' : ''}`;
  }

  async function load() {
    const mine = ++token;
    $('headline').textContent = 'Loading…';
    let page;
    try {
      page = await pairsPage({state: state.group === 'all' ? null : state.group, after: state.cursors[state.at], limit: $('perPage').value, q: state.q});
    } catch (error) { $('headline').textContent = `Could not load the fill side pairs: ${error.message}`;return; }
    if (mine !== token) return;
    lastPage = page;counts = page.counts;stats();render();
    for (const nav of [$('pagerTop'), $('pagerBottom')]) pager(nav, page.next);
    const url = new URL(location.href);
    for (const [k, v] of [['group', state.group === 'all' ? '' : state.group], ['q', state.q]]) v ? url.searchParams.set(k, v) : url.searchParams.delete(k);
    history.replaceState(null, '', url);
  }
  function restart() { state.cursors = [null];state.at = 0;load(); }

  let typing;
  $('search').value = state.q;
  $('search').addEventListener('input', () => { clearTimeout(typing);typing = setTimeout(() => { state.q = $('search').value.trim();restart(); }, 250); });
  $('perPage').addEventListener('change', restart);
  $('keyshape').addEventListener('change', render);
  $('guides').addEventListener('click', event => {
    const on = event.currentTarget.getAttribute('aria-pressed') !== 'true';
    event.currentTarget.setAttribute('aria-pressed', String(on));render();
  });
  $('tileSize').addEventListener('change', () => document.documentElement.style.setProperty('--sf-tile', $('tileSize').value));
  load();
})();
