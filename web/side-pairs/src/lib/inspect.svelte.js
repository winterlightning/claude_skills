// The part inspector (the old grid's sideInspect): a main or sub large on its own grid with its stroke centerline.
const NS = 'http://www.w3.org/2000/svg';
export const inspect = $state({open: false, shown: 0, label: '', item: null, size: 48, concept: '', view: 'both', svg: null, facts: [], error: ''});

const svgEl = (name, attrs) => { const e = document.createElementNS(NS, name);for (const [k, v] of Object.entries(attrs)) e.setAttribute(k, v);return e; };
async function documentOf(item) {
  if (item.document) return item.document;
  const r = await fetch(item.preview_url, {cache: 'no-store'});if (!r.ok) throw Error('Artwork unavailable');return r.text();
}
// Artwork in soft gray, the same paths as a thin centerline on top, over a one-unit grid.
export function inspectSVG(text) {
  const source = new DOMParser().parseFromString(text, 'image/svg+xml').documentElement;if (source.nodeName !== 'svg') throw Error('Artwork is not an SVG');
  const box = (source.getAttribute('viewBox') || `0 0 ${source.getAttribute('width') || 48} ${source.getAttribute('height') || 48}`).split(/[\s,]+/).map(Number), [x, y, w, h] = box;
  const svg = svgEl('svg', {viewBox: box.join(' '), class: 'side-component-canvas', role: 'img'});
  const grid = svgEl('g', {'aria-hidden': 'true'});
  for (let i = 0; i <= w; i++) grid.append(svgEl('line', {x1: x + i, y1: y, x2: x + i, y2: y + h, stroke: i % 8 === 0 ? '#9eb3bd' : '#dae4e9', 'stroke-width': i % 8 === 0 ? .1 : .045}));
  for (let i = 0; i <= h; i++) grid.append(svgEl('line', {x1: x, y1: y + i, x2: x + w, y2: y + i, stroke: i % 8 === 0 ? '#9eb3bd' : '#dae4e9', 'stroke-width': i % 8 === 0 ? .1 : .045}));
  const art = svgEl('g', {class: 'side-component-art'}), line = svgEl('g', {class: 'side-component-centerline', 'aria-hidden': 'true'});
  for (const a of ['fill', 'stroke', 'stroke-width', 'stroke-linecap', 'stroke-linejoin']) if (source.hasAttribute(a)) art.setAttribute(a, source.getAttribute(a));
  if (!art.hasAttribute('stroke')) art.setAttribute('stroke', 'currentColor');
  for (const child of [...source.children]) { if (['title', 'desc', 'metadata'].includes(child.localName)) continue;art.append(document.importNode(child, true)); }
  const trace = art.cloneNode(true);
  for (const e of [trace, ...trace.querySelectorAll('*')]) {
    e.removeAttribute('id');if (e !== trace && e.getAttribute('fill') && e.getAttribute('fill') !== 'none' && !e.hasAttribute('stroke')) continue;
    e.setAttribute('stroke', '#ef4444');e.setAttribute('stroke-width', '.3');e.setAttribute('fill', 'none');
  }
  line.append(...trace.childNodes);svg.append(grid, art, line);
  return {svg, width: w, height: h};
}
// Open the inspector on a part: its facts come with the artwork (`facts` worked out by the caller's rules).
// A newer opening wins (`inspect.item` is a state proxy, so the request is told apart by a counter).
let opened = 0;
export async function openInspect(label, item, size, concept, factsOf) {
  const request = ++opened;
  // `shown` counts openings: the dialog opens on each, even when it was closed without telling (no close event).
  Object.assign(inspect, {open: true, shown: inspect.shown + 1, label, item, size, concept, svg: null, facts: [], error: ''});
  try {
    const text = await documentOf(item), {svg, width, height} = inspectSVG(text);
    svg.setAttribute('aria-label', `${item.icon} on a ${width} by ${height} grid`);
    if (request === opened) { inspect.svg = svg;inspect.facts = factsOf(width, height); }
  } catch (error) { if (request === opened) inspect.error = error.message; }
}
