/* Where a container pair's symbol goes (container-pairs.html), kept apart from the page so the Node tests
 * (icon_set/tests/js/placement.test.mjs) run the same rules.
 *
 * A pair's symbol layout (reference_parts.layout, one box) carries the placement it was built with:
 *   scope: 'pair'       the box was saved for this pair only ("This pair only"); with `center` and no box yet
 *                       (a placement carried over from the old container_centers table), {center, size} is.
 *   scope: 'container'  the box follows `container: {center, size}`, the container's placement ("This container ·
 *                       all symbols"), which is kept on every pair of that container.
 *   scope: 'default'    the box is where the published defaults (container-centers.json) put it.
 *   no scope            a box saved before placements had scopes: placed by hand on this pair, so it stays its own.
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.ContainerPlacement = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  const SOURCES = {preference: 'placement preference', area: 'reviewed content area', anchor: 'container anchor'};
  const part = (item, role) => item.parts.find(p => p.role === role) || {role};
  const layoutOf = p => Array.isArray(p.layout) ? p.layout[0] || null : null;
  const idOf = key => (key || '').split('/').pop();
  const sizeOf = v => Array.isArray(v) && v.length === 2 ? v.map(Number) : null;
  const sameBox = (a, b) => !!a && !!b && ['x', 'y', 'w', 'h'].every(k => a[k] === b[k]);
  // The box a build stored ({x, y, w, h}, whole units); a 0 × 0 placeholder (a placement with no box yet) is none.
  const savedBox = p => {
    const b = Array.isArray(p.layout) && p.layout.length === 1 ? p.layout[0] : null;
    return b && ['x', 'y', 'w', 'h'].every(k => Number.isFinite(b[k])) && (b.w || b.h) ? {x: b.x, y: b.y, w: b.w, h: b.h} : null;
  };
  const scopeOf = p => layoutOf(p)?.scope;
  const pairBox = p => scopeOf(p) === 'pair' || (!scopeOf(p) && !layoutOf(p)?.container) ? savedBox(p) : null;
  const pairCenter = p => { const l = layoutOf(p); return l?.scope === 'pair' && Array.isArray(l.center) ? {center: l.center, ink: sizeOf(l.size)} : null; };
  const containerTarget = p => { const c = layoutOf(p)?.container; return c && Array.isArray(c.center) ? {center: c.center, ink: sizeOf(c.size)} : null; };

  // The symbol's placement for a pair: its own box or centre ({box | center, pinned}) unless `own` is false or another
  // symbol is picked, else {center, ink} from (in order) the container's saved placement, the published pair override,
  // the container's published default, the canvas centre. `label` says which, `scope` where a save would go.
  function placementOf(item, icons = {}, own = true, defaults = {}) {
    if (defaults.canvas === 72) return placement72(item, icons, own, defaults);
    const containerKey = icons.container ?? part(item, 'container').icon;
    // This reviewed center-only container is an overlay: its slash must be erased around the symbol.
    // Keep the 64px container identity/layout; side-pair routing would change its roles and placement.
    // Older saved layouts and container-centers.json did not record the composition mode.
    const savedOverlay = containerKey === part(item, 'container').icon ? layoutOf(part(item, 'symbol'))?.overlay : undefined;
    const overlay = savedOverlay ?? (containerKey === 'container/universal-prohibited-symbol');
    const placement = placement64(item, icons, own, defaults);
    return overlay || savedOverlay !== undefined ? {...placement, overlay: !!overlay} : placement;
  }

  function placement64(item, icons, own, defaults) {
    const s = part(item, 'symbol'), containerKey = icons.container ?? part(item, 'container').icon, symbolKey = icons.symbol ?? s.icon;
    if (own && symbolKey === s.icon) {
      const box = pairBox(s), center = box ? null : pairCenter(s);
      if (box) return {box, pinned: true, label: 'Saved · this pair', scope: 'pair', by: s.updated_by};
      if (center) return {...center, pinned: true, label: 'Saved · this pair', scope: 'pair', by: s.updated_by};
    }
    const c = idOf(containerKey), y = idOf(symbolKey);
    const whole = containerKey === part(item, 'container').icon ? containerTarget(s) : null;
    if (whole) return {...whole, saved: 'container', label: 'Saved · this container', scope: 'container', by: s.updated_by};
    const optical = defaults.pairs?.[c]?.[y];
    if (optical) return {center: optical, ink: null, label: 'Default · pair override', scope: 'pair'};
    const d = defaults.containers?.[c];
    if (d) return {center: d.center, ink: null, label: 'Default · ' + (SOURCES[d.source] || d.source), scope: 'container'};
    return {center: [32, 32], ink: null, label: 'Default · canvas center', scope: 'container'};
  }

  // Native 72 review data is keyed by exact artwork identity; never scale a 64px room.
  function placement72(item, icons, own, defaults) {
    const c = part(item, 'container'), s = part(item, 'symbol');
    const ck = icons.container ?? c.icon, sk = icons.symbol ?? s.icon;
    const record = defaults.pairs?.[item.reference_id];
    const matches = p => p && p.container === ck && p.symbol === sk
      && p.container_sha256 === (icons.containerSha ?? c.current_sha)
      && p.symbol_sha256 === (icons.symbolSha ?? s.current_sha);
    const active = record && record.container === ck && record.symbol === sk ? record : null;
    const extra = {canvas: 72, overlay: !!(layoutOf(s)?.overlay ?? active?.overlay), nativeText: !!(layoutOf(s)?.native_text ?? active?.native_text)};
    if (own && ck === c.icon && sk === s.icon) {
      const box = pairBox(s), center = box ? null : pairCenter(s);
      if (box || center) return {...extra, ...(box ? {box} : center), pinned: true, label: 'Saved · this pair', scope: 'pair', by: s.updated_by};
    }
    const whole = ck === c.icon ? containerTarget(s) : null;
    if (whole) return {...extra, ...whole, saved: 'container', label: 'Saved · this container', scope: 'container'};
    const recorded = p => ({...extra, center: p.center.map((v, i) => v + (p.offset?.[i] || 0)), size: p.size, nativeText: !!(p.native_text ?? active?.native_text), overlay: !!p.overlay, scope: 'pair'});
    if (own && matches(active) && active.baseline_sha256 && item.icon?.svg_sha256 === active.baseline_sha256)
      return {...recorded(active), label: 'Recorded · current uploaded layout'};
    if (own && matches(active?.proposal) && active.proposal.status === 'accepted')
      return {...recorded(active.proposal), label: 'Reviewed · accepted pair layout'};
    const d = defaults.containers?.[ck], room = d?.room;
    const stale = d && d.sha256 !== (icons.containerSha ?? c.current_sha);
    const proposal = active?.proposal;
    const note = [stale ? 'Container artwork changed; room needs review.' : '', proposal && !matches(proposal) ? 'Recorded pair layout belongs to older artwork; review it again.' : proposal?.status === 'propose' ? 'A pair proposal is available; it has not been accepted.' : '', room?.note || ''].filter(Boolean).join(' ');
    return {...extra, center: room?.center || [36, 36], size: room?.symbol_guide_size || 36, room,
      needsReview: !room || stale, note, proposal: matches(proposal) ? proposal : null,
      label: room ? 'Recorded room · ' + room.status + (stale ? ' · outdated' : '') : 'No recorded room · place manually', scope: 'container'};
  }

  // The symbol layout a build stores: the engine's boxes marked with the placement they came from, and the
  // container's placement (`kept`) carried along.
  function builtLayout(boxes, placement, kept) {
    const scope = placement.pinned ? 'pair' : placement.saved === 'container' ? 'container' : 'default';
    const composition = placement.canvas === 72 ? {overlay: !!placement.overlay, native_text: !!placement.nativeText}
      : placement.overlay !== undefined ? {overlay: !!placement.overlay} : {};
    return boxes.map(b => ({...b, scope, ...composition, ...(kept ? {container: kept} : {})}));
  }

  // A pair's symbol layout once its container's placement is `target` ({center, size}, or null to remove it): its
  // own placement is kept; otherwise it follows the target, or the defaults. `box`: the box to store, else the old one.
  function containerLayout(item, target, box = null) {
    const s = part(item, 'symbol'), old = layoutOf(s), own = !!(pairBox(s) || pairCenter(s));
    const {container: _, scope: __, ...rest} = old || {};
    if (!box && !old) return null;
    return [{...rest, ...(box || {}), scope: own ? 'pair' : target ? 'container' : 'default',
             ...(target ? {container: {center: target.center, size: target.size}} : {})}];
  }

  // Exact drawing identity, not the container's reference or variant family.
  function relatedPairs(items, containerKey, sourceId) {
    return items.filter(item => containerKey && item.reference_id !== sourceId && part(item, 'container').icon === containerKey);
  }

  // Save the source first. Each target keeps its own artwork and gets only the whole-symbol box.
  // Build responses are reported per batch so a later network failure cannot hide earlier successes.
  async function applySelected({sourceId, containerKey, box, targetIds, saveSource, loadPairs, loadArtwork,
                                makeRequest, build, onResult = () => {}}) {
    const source = await saveSource();
    if (!source?.ok) throw Error(source?.error || 'Could not save the current combination.');
    const results = [];
    const report = result => { results.push(result); onResult(result); };
    const ids = [...new Set(targetIds)].filter(id => id !== sourceId);
    let pairs;
    try { pairs = new Map((await loadPairs()).map(item => [item.reference_id, item])); }
    catch (error) {
      ids.forEach(id => report({reference_id: id, ok: false, error: 'Could not refresh combinations: ' + error.message}));
      return {source, results};
    }
    for (let offset = 0; offset < ids.length; offset += 50) {
      const batch = ids.slice(offset, offset + 50), eligible = [], requests = [];
      for (const id of batch) {
        const item = pairs.get(id);
        if (!item || part(item, 'container').icon !== containerKey) {
          report({reference_id: id, ok: false, error: 'This combination no longer uses this container.'});
        } else if (!part(item, 'symbol').icon) {
          report({reference_id: id, ok: false, error: 'This combination needs a symbol drawing.'});
        } else eligible.push(item);
      }
      try { await loadArtwork(eligible.flatMap(item => item.parts.map(p => p.icon))); }
      catch (error) {
        eligible.forEach(item => report({reference_id: item.reference_id, ok: false, error: 'Could not refresh drawings: ' + error.message}));
        continue;
      }
      for (const item of eligible) {
        try { requests.push(makeRequest(item, {box: {...box}, pinned: true})); }
        catch (error) { report({reference_id: item.reference_id, ok: false, error: error.message}); }
      }
      if (!requests.length) continue;
      try {
        const saved = await build(requests);
        requests.forEach((request, i) => report({...saved[i], reference_id: request.reference_id,
          ...(!saved[i] ? {ok: false, error: 'No save result received; refresh before retrying.'} : {})}));
      } catch (error) {
        requests.forEach(request => report({reference_id: request.reference_id, ok: false,
          error: 'Save not confirmed; refresh before retrying. ' + error.message}));
        ids.slice(offset + 50).forEach(id => report({reference_id: id, ok: false, error: 'Not attempted after a save request failed.'}));
        break;
      }
    }
    return {source, results};
  }

  return {SOURCES, part, layoutOf, idOf, sizeOf, sameBox, savedBox, pairBox, pairCenter, containerTarget, placementOf,
          builtLayout, containerLayout, relatedPairs, applySelected};
});
