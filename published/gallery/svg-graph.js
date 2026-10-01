/* Editable stroke geometry (the Browser Edit graph) read back from a flat SVG drawing: a port of
 * icon_set/scripts/svg_graph.graph_from_svg, so a combined icon built in the browser gets the graph the Python
 * engine stored for it.
 *
 *   SvgGraph.fromSvg(svg, {canvas, family, icon_id, name, profile}) → graph
 *
 * `line`, `arc` and `bezier` primitives, one contour per continuous subpath; each top-level group with an id (for a
 * container pair: `container` and `symbol`) prefixes its element ids, so the symbol's strokes can be selected on
 * their own. Paths are parsed with NormalizeInk32's svgpathtools port and the XML with Combine.parse; checked
 * against svg_graph.py by icon_set/tests/js/svg-graph.test.mjs.
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory(require('./combine.js'), require('./normalize-ink32.js'));
  else root.SvgGraph = factory(root.Combine, root.NormalizeInk32);
})(typeof self !== 'undefined' ? self : this, function (Combine, NormalizeInk32) {
  'use strict';

  const {parsePath, asCubicCurves} = NormalizeInk32.internals;
  const SHAPES = new Set(['path', 'line', 'polyline', 'polygon', 'rect', 'circle', 'ellipse']);
  const SKIP = new Set(['title', 'desc', 'metadata', 'defs', 'style']);
  const local = tag => tag.slice(tag.lastIndexOf(':') + 1);

  // Python's round(v, 4), then an int when whole. Only odd multiples of 1/32 are exact ties at four decimals;
  // those round half to even, everything else rounds as toFixed does.
  function num(v) {
    const scaled = v * 1e4;
    let r;
    if (Number.isInteger(v * 32) && Math.abs(scaled % 1) === 0.5) {
      const f = Math.floor(scaled);
      r = (f % 2 === 0 ? f : f + 1) / 1e4;
    } else r = Number(v.toFixed(4));
    return r === 0 ? 0 : r;
  }
  const pt = z => [num(z[0]), num(z[1])];

  // Path data for a basic shape (attributes as drawn; transforms must already be flattened).
  function shapeD(el) {
    const tag = local(el.tag), f = name => parseFloat(el.attrs[name] || 0) || 0;
    if (tag === 'path') return el.attrs.d || '';
    if (tag === 'line') return `M${f('x1')} ${f('y1')}L${f('x2')} ${f('y2')}`;
    if (tag === 'polyline' || tag === 'polygon') {
      const values = (el.attrs.points || '').replace(/,/g, ' ').split(/\s+/).filter(Boolean).map(Number);
      const pairs = [];
      for (let i = 0; i + 1 < values.length; i += 2) pairs.push(`${values[i]} ${values[i + 1]}`);
      return pairs.length ? 'M' + pairs.join('L') + (tag === 'polygon' ? 'Z' : '') : '';
    }
    if (tag === 'circle' || tag === 'ellipse') {
      const cx = f('cx'), cy = f('cy');
      const [rx, ry] = tag === 'circle' ? [f('r'), f('r')] : [f('rx'), f('ry')];
      return `M${cx - rx} ${cy}A${rx} ${ry} 0 0 1 ${cx + rx} ${cy}A${rx} ${ry} 0 0 1 ${cx - rx} ${cy}Z`;
    }
    if (tag === 'rect') {
      const x = f('x'), y = f('y'), w = f('width'), h = f('height');
      const rx = Math.min(f('rx') || f('ry'), w / 2), ry = Math.min(f('ry') || rx, h / 2);
      if (!rx) return `M${x} ${y}H${x + w}V${y + h}H${x}Z`;
      return `M${x + rx} ${y}H${x + w - rx}A${rx} ${ry} 0 0 1 ${x + w} ${y + ry}V${y + h - ry}A${rx} ${ry} 0 0 1 ${x + w - rx} ${y + h}`
        + `H${x + rx}A${rx} ${ry} 0 0 1 ${x} ${y + h - ry}V${y + ry}A${rx} ${ry} 0 0 1 ${x + rx} ${y}Z`;
    }
    return '';
  }

  // A quadratic as its exact cubic.
  function cubic(seg) {
    const c1 = [seg.start[0] + 2 / 3 * (seg.control[0] - seg.start[0]), seg.start[1] + 2 / 3 * (seg.control[1] - seg.start[1])];
    const c2 = [seg.end[0] + 2 / 3 * (seg.control[0] - seg.end[0]), seg.end[1] + 2 / 3 * (seg.control[1] - seg.end[1])];
    return {type: 'C', start: seg.start, control1: c1, control2: c2, end: seg.end};
  }

  const same = (a, b) => a[0] === b[0] && a[1] === b[1];

  // svgpathtools Path.continuous_subpaths: a new subpath wherever a segment does not start where the last ended.
  function continuousSubpaths(segs) {
    const out = [];
    let from = 0;
    for (let i = 0; i < segs.length - 1; i++) {
      if (!same(segs[i].end, segs[i + 1].start)) { out.push(segs.slice(from, i + 1)); from = i + 1; }
    }
    out.push(segs.slice(from));
    return out;
  }

  // Primitives of one continuous subpath; consecutive cubics join into one bezier primitive.
  function primitivesOf(subpath, prefix, counter) {
    const out = [];
    for (let seg of subpath) {
      if (seg.type === 'Q') seg = cubic(seg);
      if (seg.type === 'A' && Math.abs(seg.rotation) > 1e-9) {
        // The editor's arcs are axis-aligned; a rotated arc is kept as its cubic approximation.
        for (const c of asCubicCurves(seg, 1)) out.push(['bezier', c]);
        continue;
      }
      out.push([seg.type === 'C' ? 'bezier' : seg.type === 'A' ? 'arc' : 'line', seg]);
    }
    const result = [];
    for (const [kind, seg] of out) {
      const last = result[result.length - 1];
      if (kind === 'bezier' && last && last.kind === 'bezier') {
        last.segments.push([pt(seg.control1), pt(seg.control2), pt(seg.end)]);
        last.end = pt(seg.end);
        continue;
      }
      counter[0] += 1;
      const p = {kind, element_id: `${prefix}-${counter[0]}`, start: pt(seg.start), end: pt(seg.end)};
      if (kind === 'bezier') p.segments = [[pt(seg.control1), pt(seg.control2), pt(seg.end)]];
      else if (kind === 'arc') Object.assign(p, {radius_x: num(seg.radius[0]), radius_y: num(seg.radius[1]), large_arc: !!seg.large_arc, sweep: !!seg.sweep});
      result.push(p);
    }
    return result;
  }

  function fromSvg(svg, {canvas, family, icon_id = '', name = '', profile = ''}) {
    const root = Combine.parse(svg);
    const primitives = [], contours = [];
    const walk = (children, role, counters) => {
      for (const child of children) {
        if (!child.tag) continue;
        const tag = local(child.tag);
        if (SKIP.has(tag)) continue;
        if (tag === 'g') { walk(child.children, role, counters); continue; }
        if (!SHAPES.has(tag) || child.attrs.stroke === 'none') continue;
        const d = shapeD(child);
        if (!d.trim()) continue;
        const segs = parsePath(d);
        if (!segs.length) continue;
        for (const sub of continuousSubpaths(segs)) {
          if (!sub.length) continue;
          const members = primitivesOf(sub, role, counters.p);
          if (!members.length) continue;
          counters.c[0] += 1;
          primitives.push(...members);
          contours.push({contour_id: `${role}-${counters.c[0]}`, members: members.map(m => m.element_id),
                         closed: same(sub[0].start, sub[sub.length - 1].end)});
        }
      }
    };
    const elements = root.children.filter(c => c.tag);
    const named = c => local(c.tag) === 'g' && c.attrs.id;
    for (const g of elements.filter(named)) walk(g.children, g.attrs.id, {p: [0], c: [0]});
    const loose = elements.filter(c => !named(c));
    if (loose.length) walk(loose, 'stroke', {p: [0], c: [0]});
    return {icon_id, name, family, profile, canvas_size: canvas,
            keyshape: 'FREE', keyshape_bounds: [0, 0, canvas, canvas],
            free_keyshape: {bounds: [0, 0, canvas, canvas], approval_id: null,
                            rationale: 'Engine-combined drawing: the parts were placed by the combination engine.'},
            style: {stroke_width: 4, line_cap: 'round', line_join: 'round', grid: 1},
            primitives, contours, anchors: {}, relationships: []};
  }

  return {fromSvg};
});
