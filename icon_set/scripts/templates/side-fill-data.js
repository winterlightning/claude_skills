/* Fill side pairs data, for the Fill side pairs, pair, Fill main icons and Fill sub icons pages.

   Every record is D1's, through the Worker (the dev server forwards /api/ to it): lists are keyset pages
   (?after=<cursor>&limit=), so a page reads about as many rows as it shows and its totals come with it. A drawing is
   an icon's current revision: an image from /api/icon-artwork/svg (one icon row and one revision row), or the SVG
   text from /api/combinations/drawings (100 keys a request) when the page combines parts itself. */
(function () {
  'use strict';
  // The fill side pairs come in two sizes (?size=72 on every page): 64, a 48 main and a 32 sub of the solo / sub
  // families combined on 64 into side_combination64 outputs; and 72, a 54 main and a 36 sub (main-54 / sub-36)
  // combined on 72 into combination-72 outputs, whose stroke-fill regions are tucked 0.5 px (stroke-width 1).
  const SIZES = {
    64: {size: 64, canvas: 64, main: 48, sub: 32, tuck: 1.0, scale: 1, combined: 'side_combination64', normal: 'Side combination 64'},
    72: {size: 72, canvas: 72, main: 54, sub: 36, tuck: 0.5, scale: 72 / 64, combined: 'combination-72', normal: 'Side combination 72'},
  };
  const size = typeof location !== 'undefined' && new URLSearchParams(location.search).get('size') === '72' ? SIZES[72] : SIZES[64];
  // A link to another fill side pairs page, at this page's size.
  function link(href) {
    if (size.size === 64) return href;
    const url = new URL(href, typeof location !== 'undefined' ? location.href : 'http://localhost/');
    url.searchParams.set('size', '72');
    return url.pathname.split('/').pop() + url.search + url.hash;
  }
  // Every in-page link to a fill side pairs page keeps the size.
  if (typeof document !== 'undefined' && size.size === 72) {
    const keep = () => {
      for (const a of document.querySelectorAll('a[href^="side-fill"]')) a.setAttribute('href', link(a.getAttribute('href')));
      document.body?.setAttribute('data-size', '72');
    };
    document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', keep) : keep();
  }

  async function api(path, body) {
    if (size.size === 72) {
      if (body === undefined) path += (path.includes('?') ? '&' : '?') + 'size=72';
      else body = {...body, size: 72};
    }
    const response = await fetch('/api/side-fill/' + path, body === undefined ? {cache: 'no-store', credentials: 'same-origin'}
      : {method: 'POST', credentials: 'same-origin', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(body)});
    const data = await response.json().catch(() => ({}));
    if (!response.ok) throw Error(data.error || response.statusText);
    return data;
  }
  const query = params => new URLSearchParams(Object.entries(params).filter(([, v]) => v !== undefined && v !== null && v !== '')).toString();
  // {pairs: [{id, concept, state, note, main, sub, layout, picks: [{rank, main, sub, options, combined}], main_variants,
  //   sub_variants, original (with original: 1: the normal side_combination64/<id> icon {key, svg_sha256, review})}], next, counts}
  const pairsPage = params => api('pairs?' + query(params));
  const pair = id => api('pair?id=' + encodeURIComponent(id));      // as in pairs, with neighbours {previous, next}
  const partsPage = params => api('parts?' + query(params));        // {parts: [{key, role, status, note, text, pair_count, variants}], next, counts}
  const pick = body => api('pick', body);
  const unpick = body => api('unpick', body);
  const build = body => api('build', body);
  const move = body => api('move', body);

  // {key: {svg_sha256, svg, review}} of icon keys.
  async function drawings(keys) {
    const out = {}, unique = [...new Set(keys.filter(Boolean))];
    for (let i = 0; i < unique.length; i += 100) {
      const response = await fetch('/api/combinations/drawings?keys=' + encodeURIComponent(unique.slice(i, i + 100).join(',')),
                                   {cache: 'no-store', credentials: 'same-origin'});
      if (!response.ok) throw Error((await response.json().catch(() => ({}))).error || response.statusText);
      Object.assign(out, await response.json());
    }
    return out;
  }
  const iconUrl = (key, sha) => key ? `/api/icon-artwork/svg?icon=${encodeURIComponent(key)}${sha ? '&v=' + sha.slice(0, 12) : ''}` : null;
  const svgUrl = svg => svg ? `data:image/svg+xml;charset=utf-8,${encodeURIComponent(svg)}` : null;
  // The contract's SOLO48 / SUB32 keyshapes as centerline bounds ({main: {name: bounds}, sub: …}), from laboratory.json
  // as the Side pairs editor reads them. No contract defines 54 / 36 keyshapes: at 72 they are these scaled 72/64,
  // as the 54 main and 36 sub are the 48 and 32 ones scaled.
  let keyshapeTable = null;
  const keyshapes = () => keyshapeTable ||= fetch('laboratory.json', {cache: 'no-cache'}).then(r => r.ok ? r.json() : null).catch(() => null)
    .then(d => Object.fromEntries([['main', 'SOLO48'], ['sub', 'SUB32']].map(([role, profile]) => [role, Object.fromEntries(
      Object.entries(d?.keyshapes?.resolved?.[profile] || {}).map(([n, k]) => [n, k.centerline_bounds]).filter(([, b]) => Array.isArray(b))
        .map(([n, b]) => [n, b.map(v => v * size.scale)]))])));

  // What a pick's part is: its variant label, or 'outline' when it is the solo / sub icon itself.
  function labelOf(pairRow, role, key) {
    if (!key) return '—';
    if (key === pairRow[role]) return 'outline';
    return (pairRow[`${role}_variants`] || []).find(v => v.key === key)?.variant || key.split('/').pop();
  }
  // The sub icon the layout editor's sub variant names: the outline is the sub itself; "fill" is the fill this
  // combination uses when it uses one (a sub can have several), else its first fill.
  function subFor(name, selected, outline, fills) {
    if (name === 'outline') return outline;
    return fills.some(f => f.key === selected) ? selected : fills[0]?.key;
  }
  // A pick is stale when a part was redrawn since its combined icon was built (or it was never built).
  const stale = p => !p.combined || ['main', 'sub'].some(r => p[r] && p[r].built_sha !== p[r].svg_sha256);
  // The pair's own placement as units of whole elements (a single box without element numbers takes them all).
  function units(layout, sources) {
    const boxes = (layout || []).map(b => ({...b, x: Math.round(b.x), y: Math.round(b.y), w: Math.round(b.w), h: Math.round(b.h)}));
    if (boxes.length === 1 && !boxes[0].paths) boxes[0].paths = sources.map((s, i) => s ? i : null).filter(i => i !== null);
    return boxes;
  }

  // An artwork tile: an image (cached by its URL), with an optional overlay on top.
  function artBox(url, {href, overlay, empty = 'No artwork', svg} = {}) {
    const box = document.createElement(href ? 'a' : 'div');
    box.className = 'sf-art';
    if (href) box.href = href;
    const src = url || svgUrl(svg);
    if (src) {
      const img = new Image();
      img.alt = '';img.decoding = 'async';img.loading = 'lazy';img.src = src;
      box.append(img);
    } else {
      const ph = document.createElement('span');ph.className = 'ph';ph.textContent = empty;box.append(ph);
    }
    if (overlay) box.append(overlay);
    return box;
  }

  const exported = {api, pairsPage, pair, partsPage, pick, unpick, build, move, drawings, iconUrl, svgUrl, keyshapes, labelOf, stale, units, artBox, subFor,
                    size, SIZES, link};
  if (typeof window !== 'undefined') window.SideFillData = exported;
  if (typeof module === 'object' && module.exports) module.exports = exported;
})();
