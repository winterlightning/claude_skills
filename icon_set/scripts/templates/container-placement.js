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
    return b && ['x', 'y', 'w', 'h'].every(k => Number.isInteger(b[k])) && (b.w || b.h) ? {x: b.x, y: b.y, w: b.w, h: b.h} : null;
  };
  const scopeOf = p => layoutOf(p)?.scope;
  const pairBox = p => scopeOf(p) === 'pair' || (!scopeOf(p) && !layoutOf(p)?.container) ? savedBox(p) : null;
  const pairCenter = p => { const l = layoutOf(p); return l?.scope === 'pair' && Array.isArray(l.center) ? {center: l.center, ink: sizeOf(l.size)} : null; };
  const containerTarget = p => { const c = layoutOf(p)?.container; return c && Array.isArray(c.center) ? {center: c.center, ink: sizeOf(c.size)} : null; };

  // The symbol's placement for a pair: its own box or centre ({box | center, pinned}) unless `own` is false or another
  // symbol is picked, else {center, ink} from (in order) the container's saved placement, the published pair override,
  // the container's published default, the canvas centre. `label` says which, `scope` where a save would go.
  function placementOf(item, icons = {}, own = true, defaults = {}) {
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

  // The symbol layout a build stores: the engine's boxes marked with the placement they came from, and the
  // container's placement (`kept`) carried along.
  function builtLayout(boxes, placement, kept) {
    const scope = placement.pinned ? 'pair' : placement.saved === 'container' ? 'container' : 'default';
    return boxes.map(b => ({...b, scope, ...(kept ? {container: kept} : {})}));
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

  return {SOURCES, part, layoutOf, idOf, sizeOf, sameBox, savedBox, pairBox, pairCenter, containerTarget, placementOf,
          builtLayout, containerLayout};
});
