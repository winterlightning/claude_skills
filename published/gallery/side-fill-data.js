/* Fill side pairs data, for the Fill side pairs, pair, Fill main icons and Fill sub icons pages.

   Every record is D1's, through the Worker (the dev server forwards /api/ to it): lists are keyset pages
   (?after=<cursor>&limit=), so a page reads about as many rows as it shows and its totals come with it. A drawing is
   an icon's current revision: an image from /api/icon-artwork/svg (one icon row and one revision row), or the SVG
   text from /api/combinations/drawings (100 keys a request) when the page combines parts itself. */
(function () {
  'use strict';
  async function api(path, body) {
    const response = await fetch('/api/side-fill/' + path, body === undefined ? {cache: 'no-store', credentials: 'same-origin'}
      : {method: 'POST', credentials: 'same-origin', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(body)});
    const data = await response.json().catch(() => ({}));
    if (!response.ok) throw Error(data.error || response.statusText);
    return data;
  }
  const query = params => new URLSearchParams(Object.entries(params).filter(([, v]) => v !== undefined && v !== null && v !== '')).toString();
  // {pairs: [{id, concept, state, note, main, sub, layout, picks: [{rank, main, sub, options, combined}], main_variants,
  //   sub_variants}], next, counts}
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
  let keyshapeTable = null;
  const keyshapes = () => keyshapeTable ||= fetch('side-fill-keyshapes.json', {cache: 'no-cache'}).then(r => r.ok ? r.json() : {}).catch(() => ({}));

  // What a pick's part is: its variant label, or 'outline' when it is the solo / sub icon itself.
  function labelOf(pairRow, role, key) {
    if (!key) return '—';
    if (key === pairRow[role]) return 'outline';
    return (pairRow[`${role}_variants`] || []).find(v => v.key === key)?.variant || key.split('/').pop();
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

  window.SideFillData = {api, pairsPage, pair, partsPage, pick, unpick, build, move, drawings, iconUrl, svgUrl, keyshapes, labelOf, stale, units, artBox};
})();
