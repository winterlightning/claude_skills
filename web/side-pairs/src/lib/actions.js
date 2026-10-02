// Svelte actions for the plain-JS helpers the page reuses (side-repair-flags.js, side-combination-popup.js).

// The combined popup on a combined icon: main / sub bounds and centerline (SideCombinationPopup.attach).
export function combinedPopup(image, {concept, result}) {
  if (result) window.SideCombinationPopup?.attach(image, concept, result);
  return {update: next => { if (next.result) window.SideCombinationPopup?.attach(image, next.concept, next.result); }};
}
// Put a helper's node just before an (empty, hidden) anchor, so its parent is the anchor's parent: side-repair-flags.js
// puts its notes after the review chip's parent, the actions row.
export function mountBefore(anchor, make) {
  let node = null;
  const place = make => { node?.remove();node = make?.() || null;if (node) anchor.before(node); };
  place(make);
  return {update: place, destroy: () => node?.remove()};
}
