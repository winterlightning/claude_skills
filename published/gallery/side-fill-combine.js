/* Fill side pairs combined in the browser: a port of icon_set/scripts/side_fill/pick_combine.py.
 *
 *   SideFillCombine.combine({main: {svg, source, layout, outline}, sub: {…}, options}) → {svg, area, bounds, how}
 *
 * A pick's main and sub are icons: a fill variant (stroke-fill/v1, or a flat fill) or, for the outline, the solo /
 * sub icon itself; `source` is that part's solo / sub drawing (its element numbers are what a layout's `paths` name),
 * `layout` the part's boxes on the 64 grid. The main is placed and cut clear of the placed sub exactly as the Python
 * build does it (combine_fill_side_layouts.place_part, combine_fill_side.cut_main / cut_outline_strokes); shapely's
 * buffers and booleans are Clipper's here (clipper.js), with GEOS's 8 segments per quarter circle, so a combined
 * drawing matches the Python one to a fraction of a square pixel (icon_set/tests/js/side-fill.test.mjs).
 * No DOM: the page and Node run the same code.
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory(require('./clipper.js'), require('./combine-side.js'));
  else root.SideFillCombine = factory(root.ClipperLib, root.CombineSide);
})(typeof self !== 'undefined' ? self : this, function (ClipperLib, CombineSide) {
  'use strict';

  const {parseXml} = CombineSide;
  const {segmentsOf, bbox, unionBoxes, bake, drawables, local} = CombineSide.internals;
  const CANVAS = 64, HALF_STROKE = 2.0, GAP = 4.0, EPS = 0.05;
  const MIN_PART_AREA = 4.0, MIN_HOLE_AREA = 2.0, MIN_PART_WIDTH = 2.0, STUB_SHARE = 0.5, DETAIL_AREA = 48.0;
  const SCRAP_AREA = 64.0, FRAGMENT_AREA = 24.0;
  const SAME_MAP = 0.75, OWNER_SHARE = 0.9, SAMPLE_STEP = 0.5, MAX_GROUP_SCALE = 2.0, MAX_GROUP_STRETCH = 1.5;
  const CLASSIFY_STEP = 0.5, SLIVER = 0.4, TUCK = 1.0, DEFAULT_WIDTH = 4.0;
  const CURVE_SAMPLES = 20, CIRCLE_SAMPLES = 64;
  const INHERITED = ['fill', 'stroke', 'stroke-width', 'stroke-linecap', 'stroke-linejoin', 'stroke-miterlimit',
                     'fill-rule', 'opacity', 'stroke-opacity', 'fill-opacity'];

  class FillError extends Error {}
  const fail = message => { throw new FillError(message); };

  // ======== geometry: shapely's operations on Clipper paths ========
  // A shape is a list of rings (Clipper paths of integer points, SCALE per pixel) in the form a nonzero union
  // leaves them: outer rings one way round, holes the other.

  const C = ClipperLib, SCALE = 1e5, NZ = C.PolyFillType.pftNonZero, EO = C.PolyFillType.pftEvenOdd;
  const QUARTER_SEGMENTS = 8;                                   // GEOS buffer quad_segs
  const GEOS_SAG = 1 - Math.cos(Math.PI / (4 * QUARTER_SEGMENTS));
  const FINE = 0.002 * SCALE;                                   // skia-stroked outlines: close to exact curves
  const EMPTY = [];

  const ring = points => points.map(([x, y]) => ({X: Math.round(x * SCALE), Y: Math.round(y * SCALE)}));
  const pointsOf = path => path.map(p => [p.X / SCALE, p.Y / SCALE]);

  function clip(type, subject, clipping = null, fill = NZ) {
    const c = new C.Clipper();
    if (subject.length) c.AddPaths(subject, C.PolyType.ptSubject, true);
    if (clipping && clipping.length) c.AddPaths(clipping, C.PolyType.ptClip, true);
    const out = [];
    c.Execute(type, out, fill, NZ);
    return out.filter(p => p.length > 2);
  }
  const normalize = (paths, fill = NZ) => clip(C.ClipType.ctUnion, paths, null, fill);
  const union = shapes => normalize([].concat(...shapes.filter(Boolean)));
  const difference = (a, b) => (!a.length ? EMPTY : !b.length ? a : clip(C.ClipType.ctDifference, a, b));
  const intersection = (a, b) => (!a.length || !b.length ? EMPTY : clip(C.ClipType.ctIntersection, a, b));
  const area = shape => shape.reduce((sum, p) => sum + C.Clipper.Area(p), 0) / (SCALE * SCALE);
  const isEmpty = shape => !shape.length || Math.abs(area(shape)) < 1e-12;

  function bounds(shape) {
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    for (const path of shape) for (const p of path) {
      if (p.X < x0) x0 = p.X; if (p.X > x1) x1 = p.X; if (p.Y < y0) y0 = p.Y; if (p.Y > y1) y1 = p.Y;
    }
    return x0 === Infinity ? null : [x0 / SCALE, y0 / SCALE, x1 / SCALE, y1 / SCALE];
  }

  const arcTolerance = delta => Math.max(1, Math.abs(delta) * SCALE * GEOS_SAG);

  // shape.buffer(delta, join_style='round'|'mitre'): a polygon offset.
  function buffer(shape, delta, {join = 'round', fine = false} = {}) {
    if (!shape.length) return EMPTY;
    if (Math.abs(delta) < 1e-9) return shape;
    const co = new C.ClipperOffset(2, fine ? FINE : arcTolerance(delta));
    co.AddPaths(shape, join === 'round' ? C.JoinType.jtRound : C.JoinType.jtMiter, C.EndType.etClosedPolygon);
    const out = [];
    co.Execute(out, delta * SCALE);
    return normalize(out);
  }

  function circle(x, y, r, segments = 4 * QUARTER_SEGMENTS) {
    const points = [];
    for (let i = 0; i < segments; i++) {
      const a = 2 * Math.PI * i / segments;
      points.push([x + r * Math.cos(a), y + r * Math.sin(a)]);
    }
    return [ring(points)];
  }

  // Strokes around centerlines: [{points, closed}] painted `width` wide with the cap and join (SVG names).
  function stroke(lines, width, {cap = 'round', join = 'round', miter = 4, fine = false} = {}) {
    const half = width / 2;
    if (half <= 0) return EMPTY;
    const jt = join === 'round' ? C.JoinType.jtRound : join === 'miter' ? C.JoinType.jtMiter : C.JoinType.jtSquare;
    const et = cap === 'round' ? C.EndType.etOpenRound : cap === 'square' ? C.EndType.etOpenSquare : C.EndType.etOpenButt;
    const co = new C.ClipperOffset(Math.max(2, miter), fine ? FINE : arcTolerance(half));
    const dots = [];
    for (const {points, closed} of lines) {
      if (!points.length) continue;
      const length = points.slice(1).reduce((s, p, i) => s + Math.hypot(p[0] - points[i][0], p[1] - points[i][1]), 0);
      if (length < 1e-6) {
        // A zero-length stroke: its round cap is a dot, a square cap a square, a butt cap nothing.
        const [x, y] = points[0];
        if (cap === 'round') dots.push(fine ? circle(x, y, half, 128) : circle(x, y, half));
        else if (cap === 'square') dots.push([ring([[x - half, y - half], [x + half, y - half], [x + half, y + half], [x - half, y + half]])]);
        continue;
      }
      co.AddPath(ring(points), jt, closed && points.length > 2 ? C.EndType.etClosedLine : et);
    }
    const out = [];
    co.Execute(out, half * SCALE);
    return union([out, ...dots]);
  }

  // The pieces of open centerlines outside an area (LineString.difference): each segment split where it crosses the
  // area's edges, the pieces whose middle is outside kept and joined where they meet. (Clipper's open-path clipping
  // loses whole lines that never reach the area.)
  function linesOutside(lines, shape) {
    if (!shape.length) return lines.map(l => l.points);
    const edges = [];
    for (const path of shape) {
      for (let i = 0; i < path.length; i++) {
        const a = path[i], b = path[(i + 1) % path.length];
        edges.push([a.X / SCALE, a.Y / SCALE, b.X / SCALE, b.Y / SCALE]);
      }
    }
    const [bx0, by0, bx1, by1] = bounds(shape);
    const out = [];
    for (const {points} of lines) {
      let run = null;
      const flush = () => { if (run && run.length > 1) out.push(run); run = null; };
      // GEOS nodes a line where it crosses itself, so a piece ends there too (and a short one is dropped as such).
      const {nodes, vertices} = selfNodes(points);
      for (let i = 0; i + 1 < points.length; i++) {
        if (i > 0 && vertices.has(i)) flush();
        const [x0, y0] = points[i], [x1, y1] = points[i + 1];
        const cuts = [0, 1, ...(nodes.get(i) || [])];
        const breaks = new Set(nodes.get(i) || []);
        if (!(Math.max(x0, x1) < bx0 || Math.min(x0, x1) > bx1 || Math.max(y0, y1) < by0 || Math.min(y0, y1) > by1)) {
          const dx = x1 - x0, dy = y1 - y0;
          for (const [ex0, ey0, ex1, ey1] of edges) {
            const fx = ex1 - ex0, fy = ey1 - ey0, den = dx * fy - dy * fx;
            if (Math.abs(den) < 1e-15) continue;
            const t = ((ex0 - x0) * fy - (ey0 - y0) * fx) / den, u = ((ex0 - x0) * dy - (ey0 - y0) * dx) / den;
            if (t > 0 && t < 1 && u >= 0 && u <= 1) cuts.push(t);
          }
        }
        cuts.sort((m, n) => m - n);
        for (let k = 0; k + 1 < cuts.length; k++) {
          const t0 = cuts[k], t1 = cuts[k + 1];
          if (t1 - t0 < 1e-12) continue;
          const tm = (t0 + t1) / 2, mid = [x0 + (x1 - x0) * tm, y0 + (y1 - y0) * tm];
          const a = [x0 + (x1 - x0) * t0, y0 + (y1 - y0) * t0], b = [x0 + (x1 - x0) * t1, y0 + (y1 - y0) * t1];
          if (contains(shape, mid)) { flush(); continue; }
          if (!run) run = [a];
          run.push(b);
          if (breaks.has(t1)) flush();
        }
      }
      flush();
    }
    return out;
  }

  // Where a polyline crosses or touches itself: {nodes: {segment index: [t, …]}, vertices: Set of vertex indexes}.
  function selfNodes(points) {
    const nodes = new Map(), vertices = new Set(), n = points.length - 1;
    const closed = n > 2 && close(points[0], points[n], 1e-9);
    const add = (i, t) => {
      if (t <= 1e-9) vertices.add(i);
      else if (t >= 1 - 1e-9) vertices.add(i + 1);
      else { if (!nodes.has(i)) nodes.set(i, []); nodes.get(i).push(t); }
    };
    for (let i = 0; i < n; i++) {
      const [ax, ay] = points[i], [bx, by] = points[i + 1], dx = bx - ax, dy = by - ay;
      for (let j = i + 2; j < n; j++) {
        if (closed && i === 0 && j === n - 1) continue;          // the ring's first and last segments meet at its start
        const [cx, cy] = points[j], [ex, ey] = points[j + 1], fx = ex - cx, fy = ey - cy;
        if (Math.max(ax, bx) < Math.min(cx, ex) || Math.max(cx, ex) < Math.min(ax, bx) || Math.max(ay, by) < Math.min(cy, ey) || Math.max(cy, ey) < Math.min(ay, by)) continue;
        const den = dx * fy - dy * fx;
        if (Math.abs(den) < 1e-15) continue;
        const t = ((cx - ax) * fy - (cy - ay) * fx) / den, u = ((cx - ax) * dy - (cy - ay) * dx) / den;
        if (t >= -1e-12 && t <= 1 + 1e-12 && u >= -1e-12 && u <= 1 + 1e-12) { add(i, t); add(j, u); }
      }
    }
    vertices.delete(0);vertices.delete(n);
    return {nodes, vertices};
  }
  const lineLength = points => points.slice(1).reduce((s, p, i) => s + Math.hypot(p[0] - points[i][0], p[1] - points[i][1]), 0);

  // shape's polygons: [{outer, holes}] (a polygon in a hole of another is its own).
  function polygons(shape) {
    if (!shape.length) return [];
    const c = new C.Clipper();
    c.AddPaths(shape, C.PolyType.ptSubject, true);
    const tree = new C.PolyTree();
    c.Execute(C.ClipType.ctUnion, tree, NZ, NZ);
    const out = [];
    const walk = node => {
      for (const outer of node.Childs()) {
        out.push({outer: outer.Contour(), holes: outer.Childs().map(h => h.Contour())});
        for (const hole of outer.Childs()) walk(hole);
      }
    };
    walk(tree);
    return out;
  }
  const polygonShape = p => [p.outer, ...p.holes];
  const exterior = p => [p.outer];

  function convexHull(shape) {
    const points = [];
    for (const path of shape) for (const p of path) points.push([p.X, p.Y]);
    if (points.length < 3) return EMPTY;
    points.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    const cross = (o, a, b) => (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
    const lower = [], upper = [];
    for (const p of points) {
      while (lower.length >= 2 && cross(lower[lower.length - 2], lower[lower.length - 1], p) <= 0) lower.pop();
      lower.push(p);
    }
    for (let i = points.length - 1; i >= 0; i--) {
      const p = points[i];
      while (upper.length >= 2 && cross(upper[upper.length - 2], upper[upper.length - 1], p) <= 0) upper.pop();
      upper.push(p);
    }
    const hull = lower.slice(0, -1).concat(upper.slice(0, -1));
    return normalize([hull.map(([X, Y]) => ({X, Y}))]);
  }

  // A point inside a polygon, away from its edges (shapely's representative_point: the widest gap on a scanline).
  function representativePoint(p) {
    const rings = [p.outer, ...p.holes];
    let y0 = Infinity, y1 = -Infinity;
    for (const pt of p.outer) { if (pt.Y < y0) y0 = pt.Y; if (pt.Y > y1) y1 = pt.Y; }
    let y = (y0 + y1) / 2;
    const ys = new Set(rings.flatMap(r => r.map(pt => pt.Y)));
    while (ys.has(y)) y += 0.37;
    const xs = [];
    for (const r of rings) {
      for (let i = 0; i < r.length; i++) {
        const a = r[i], b = r[(i + 1) % r.length];
        if ((a.Y > y) !== (b.Y > y)) xs.push(a.X + (y - a.Y) * (b.X - a.X) / (b.Y - a.Y));
      }
    }
    xs.sort((m, n) => m - n);
    let best = null, width = -1;
    for (let i = 0; i + 1 < xs.length; i += 2) if (xs[i + 1] - xs[i] > width) { width = xs[i + 1] - xs[i]; best = (xs[i] + xs[i + 1]) / 2; }
    return best === null ? [p.outer[0].X / SCALE, p.outer[0].Y / SCALE] : [best / SCALE, y / SCALE];
  }

  // Whether a point is inside a shape (holes excluded); on an edge counts as inside unless `strict` (shapely's
  // prepared contains, which rebuild_strokes classifies centerline pieces with).
  function contains(shape, [x, y], strict = false) {
    const pt = {X: Math.round(x * SCALE), Y: Math.round(y * SCALE)};
    let inside = 0;
    for (const path of shape) {
      const r = C.Clipper.PointInPolygon(pt, path);
      if (r === -1) return !strict;
      if (r === 1) inside += C.Clipper.Area(path) > 0 ? 1 : -1;
    }
    return inside > 0;
  }

  // An affine map: [sx, sy, dx, dy] (a layout group) or [a, b, c, d, e, f] (an SVG matrix).
  function mapShape(shape, m) {
    const [a, b, c, d, e, f] = m.length === 4 ? [m[0], 0, 0, m[1], m[2], m[3]] : m;
    const flip = a * d - b * c < 0;
    return normalize(shape.map(path => {
      const moved = path.map(p => ({X: Math.round(a * p.X + c * p.Y + e * SCALE), Y: Math.round(b * p.X + d * p.Y + f * SCALE)}));
      return flip ? moved.reverse() : moved;
    }));
  }
  function mapPoints(points, m) {
    const [a, b, c, d, e, f] = m.length === 4 ? [m[0], 0, 0, m[1], m[2], m[3]] : m;
    return points.map(([x, y]) => [a * x + c * y + e, b * x + d * y + f]);
  }

  function dropTinyHoles(p, minArea) {
    return {outer: p.outer, holes: p.holes.filter(h => Math.abs(C.Clipper.Area(h)) / (SCALE * SCALE) >= minArea)};
  }

  // ======== SVG reading: fill_utils.parse_all_shapes / path_to_linestrings ========

  const NUMBER = /[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?/g;
  const ARGS = {M: 2, L: 2, H: 1, V: 1, C: 6, S: 4, Q: 4, T: 2, A: 7, Z: 0};

  // The segments of path data: [{kind: 'L'|'C'|'Q'|'A', …}] in subpaths [{segments, closed}].
  function pathSegments(d) {
    const tokens = d.match(/[MmLlHhVvCcSsQqTtAaZz]|[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?/g) || [];
    const subpaths = [];
    let current = [0, 0], start = [0, 0], i = 0, command = null, sub = null, lastControl = null, lastKind = null;
    const begin = () => { sub = {segments: [], closed: false}; subpaths.push(sub); };
    while (i < tokens.length) {
      if (/^[a-z]$/i.test(tokens[i])) {
        command = tokens[i++];
        if (command === 'Z' || command === 'z') {
          if (sub) {
            if (Math.hypot(current[0] - start[0], current[1] - start[1]) > 1e-12) sub.segments.push({kind: 'L', p0: current, p1: start});
            sub.closed = true;
          }
          current = start; sub = null; lastKind = 'Z';
          continue;
        }
      } else if (command === null) break;
      const upper = command.toUpperCase(), relative = command !== upper, n = ARGS[upper];
      const v = tokens.slice(i, i + n).map(Number);
      if (v.length !== n || v.some(Number.isNaN)) break;
      i += n;
      const pt = (x, y) => relative ? [current[0] + x, current[1] + y] : [x, y];
      if (upper === 'M') {
        current = start = pt(v[0], v[1]); begin();
        command = relative ? 'l' : 'L'; lastKind = 'M';
        continue;
      }
      if (!sub) { begin(); start = current; }
      let end, segment;
      if (upper === 'L') { end = pt(v[0], v[1]); segment = {kind: 'L', p0: current, p1: end}; }
      else if (upper === 'H') { end = [relative ? current[0] + v[0] : v[0], current[1]]; segment = {kind: 'L', p0: current, p1: end}; }
      else if (upper === 'V') { end = [current[0], relative ? current[1] + v[0] : v[0]]; segment = {kind: 'L', p0: current, p1: end}; }
      else if (upper === 'C' || upper === 'S') {
        let c1, c2;
        if (upper === 'C') { c1 = pt(v[0], v[1]); c2 = pt(v[2], v[3]); end = pt(v[4], v[5]); }
        else {
          c1 = lastKind === 'C' && lastControl ? [2 * current[0] - lastControl[0], 2 * current[1] - lastControl[1]] : current;
          c2 = pt(v[0], v[1]); end = pt(v[2], v[3]);
        }
        segment = {kind: 'C', p0: current, c1, c2, p1: end}; lastControl = c2;
      } else if (upper === 'Q' || upper === 'T') {
        let c1;
        if (upper === 'Q') { c1 = pt(v[0], v[1]); end = pt(v[2], v[3]); }
        else { c1 = lastKind === 'Q' && lastControl ? [2 * current[0] - lastControl[0], 2 * current[1] - lastControl[1]] : current; end = pt(v[0], v[1]); }
        segment = {kind: 'Q', p0: current, c1, p1: end}; lastControl = c1;
      } else {
        end = pt(v[5], v[6]);
        segment = arcSegment(current, v[0], v[1], v[2], !!v[3], !!v[4], end);
      }
      if (segment) sub.segments.push(segment);
      lastKind = upper === 'S' ? 'C' : upper === 'T' ? 'Q' : upper;
      current = end;
    }
    return subpaths.filter(s => s.segments.length || true);
  }

  // An SVG arc as centre, radii, rotation and angles (as svgpathtools.Arc parameterises it), or a line.
  function arcSegment(p0, rx, ry, rotation, large, sweep, p1) {
    if (Math.hypot(p1[0] - p0[0], p1[1] - p0[1]) < 1e-12) return null;   // an arc to its own start draws nothing
    rx = Math.abs(rx); ry = Math.abs(ry);
    if (rx < 1e-12 || ry < 1e-12) return {kind: 'L', p0, p1};
    const phi = rotation * Math.PI / 180, cos = Math.cos(phi), sin = Math.sin(phi);
    const dx = (p0[0] - p1[0]) / 2, dy = (p0[1] - p1[1]) / 2;
    const x1 = cos * dx + sin * dy, y1 = -sin * dx + cos * dy;
    const lambda = (x1 * x1) / (rx * rx) + (y1 * y1) / (ry * ry);
    if (lambda > 1) { rx *= Math.sqrt(lambda); ry *= Math.sqrt(lambda); }
    const num = rx * rx * ry * ry - rx * rx * y1 * y1 - ry * ry * x1 * x1, den = rx * rx * y1 * y1 + ry * ry * x1 * x1;
    const coef = (large === sweep ? -1 : 1) * Math.sqrt(Math.max(0, num / den));
    const cxp = coef * rx * y1 / ry, cyp = -coef * ry * x1 / rx;
    const cx = cos * cxp - sin * cyp + (p0[0] + p1[0]) / 2, cy = sin * cxp + cos * cyp + (p0[1] + p1[1]) / 2;
    const angle = (ux, uy, vx, vy) => Math.atan2(ux * vy - uy * vx, ux * vx + uy * vy);
    const theta = angle(1, 0, (x1 - cxp) / rx, (y1 - cyp) / ry);
    let delta = angle((x1 - cxp) / rx, (y1 - cyp) / ry, (-x1 - cxp) / rx, (-y1 - cyp) / ry);
    if (!sweep && delta > 0) delta -= 2 * Math.PI;
    if (sweep && delta < 0) delta += 2 * Math.PI;
    return {kind: 'A', p0, p1, cx, cy, rx, ry, cos, sin, theta, delta};
  }

  function pointAt(s, t) {
    if (s.kind === 'L') return [s.p0[0] + (s.p1[0] - s.p0[0]) * t, s.p0[1] + (s.p1[1] - s.p0[1]) * t];
    if (s.kind === 'C') {
      const u = 1 - t;
      return [u * u * u * s.p0[0] + 3 * u * u * t * s.c1[0] + 3 * u * t * t * s.c2[0] + t * t * t * s.p1[0],
              u * u * u * s.p0[1] + 3 * u * u * t * s.c1[1] + 3 * u * t * t * s.c2[1] + t * t * t * s.p1[1]];
    }
    if (s.kind === 'Q') {
      const u = 1 - t;
      return [u * u * s.p0[0] + 2 * u * t * s.c1[0] + t * t * s.p1[0], u * u * s.p0[1] + 2 * u * t * s.c1[1] + t * t * s.p1[1]];
    }
    if (t === 0) return s.p0;
    if (t === 1) return s.p1;
    const a = s.theta + s.delta * t, x = s.rx * Math.cos(a), y = s.ry * Math.sin(a);
    return [s.cos * x - s.sin * y + s.cx, s.sin * x + s.cos * y + s.cy];
  }

  // Points along a segment: 'sampled' as fill_utils samples curves (CURVE_SAMPLES steps of t), 'fine' close to
  // the curve itself (for outlines skia strokes from the curves).
  function segmentPoints(s, mode) {
    if (s.kind === 'L') return [s.p0, s.p1];
    let n = CURVE_SAMPLES;
    if (mode === 'fine') {
      let length = 0, last = s.p0;
      for (let k = 1; k <= 16; k++) { const p = pointAt(s, k / 16); length += Math.hypot(p[0] - last[0], p[1] - last[1]); last = p; }
      n = Math.max(8, Math.min(400, Math.ceil(length / 0.15)));
    }
    const out = [];
    for (let k = 0; k <= n; k++) out.push(pointAt(s, k / n));
    return out;
  }

  const close = (a, b, tol = 1e-4) => Math.abs(a[0] - b[0]) < tol && Math.abs(a[1] - b[1]) < tol;

  // path_to_linestrings: chains of points, split where a segment does not start at the last point.
  function pathChains(d, mode = 'sampled') {
    const out = [];
    for (const sub of pathSegments(d)) {
      let chain = [];
      const flush = closed => {
        const dedup = [];
        for (const p of chain) if (!dedup.length || !close(dedup[dedup.length - 1], p)) dedup.push(p);
        if (dedup.length >= 2) out.push({points: dedup, closed});
        else if (dedup.length === 1 && chain.length) out.push({points: [dedup[0], dedup[0]], closed: false});
        chain = [];
      };
      if (!sub.segments.length) continue;
      for (const s of sub.segments) {
        const pts = segmentPoints(s, mode);
        if (chain.length && !close(chain[chain.length - 1], pts[0])) flush(false);
        if (chain.length && close(chain[chain.length - 1], pts[0])) chain.push(...pts.slice(1));
        else chain.push(...pts);
      }
      flush(sub.closed);
    }
    return out;
  }

  // _filled_path_geometry: the area chains enclose under a fill rule (every chain closed).
  function filledArea(chains, rule = 'nonzero') {
    const rings = chains.filter(c => new Set(c.points.map(p => p.join(','))).size >= 3).map(c => ring(c.points));
    return rings.length ? normalize(rings, rule === 'evenodd' ? EO : NZ) : EMPTY;
  }

  function circlePoints(cx, cy, rx, ry, n = CIRCLE_SAMPLES) {
    const out = [];
    for (let i = 0; i < n; i++) { const a = 2 * Math.PI * i / (n - 1); out.push([cx + rx * Math.cos(a), cy + ry * Math.sin(a)]); }
    return out;
  }
  function roundedRectPoints(x, y, w, h, rx, ry) {
    rx = Math.min(Math.max(rx, 0), w / 2); ry = Math.min(Math.max(ry, 0), h / 2);
    if (rx <= 0 || ry <= 0) return [[x, y], [x + w, y], [x + w, y + h], [x, y + h], [x, y]];
    const per = Math.max(4, Math.floor(CIRCLE_SAMPLES / 4)), coords = [];
    const corner = (cx, cy, from) => { for (let k = 0; k < per; k++) { const a = from + (Math.PI / 2) * k / (per - 1); coords.push([cx + rx * Math.cos(a), cy + ry * Math.sin(a)]); } };
    corner(x + w - rx, y + ry, -Math.PI / 2); corner(x + w - rx, y + h - ry, 0); corner(x + rx, y + h - ry, Math.PI / 2); corner(x + rx, y + ry, Math.PI);
    const dedup = [coords[0]];
    for (const c of coords.slice(1)) if (Math.abs(c[0] - dedup[dedup.length - 1][0]) > 1e-9 || Math.abs(c[1] - dedup[dedup.length - 1][1]) > 1e-9) dedup.push(c);
    if (!close(dedup[0], dedup[dedup.length - 1], 1e-12)) dedup.push(dedup[0]);
    return dedup;
  }

  const num = (v, fallback = 0) => { const n = parseFloat(String(v ?? '').replace(/px$/i, '')); return Number.isFinite(n) ? n : fallback; };

  // The chains of one leaf element ([{points, closed}]), as _extract_leaf_coords reads it.
  function leafChains(el, mode = 'sampled') {
    const a = el.attrib, tag = local(el.tag);
    if (tag === 'path') return a.d && a.d.trim() ? pathChains(a.d, mode) : [];
    if (tag === 'circle') { const r = num(a.r); return r > 0 ? [{points: circlePoints(num(a.cx), num(a.cy), r, r, mode === 'fine' ? 256 : CIRCLE_SAMPLES), closed: true}] : []; }
    if (tag === 'ellipse') { const rx = num(a.rx), ry = num(a.ry); return rx > 0 && ry > 0 ? [{points: circlePoints(num(a.cx), num(a.cy), rx, ry, mode === 'fine' ? 256 : CIRCLE_SAMPLES), closed: true}] : []; }
    if (tag === 'rect') {
      const w = num(a.width), h = num(a.height);
      if (!(w > 0 && h > 0)) return [];
      let rx = num(a.rx), ry = num(a.ry);
      if (rx > 0 && ry <= 0) ry = rx; else if (ry > 0 && rx <= 0) rx = ry;
      return [{points: roundedRectPoints(num(a.x), num(a.y), w, h, rx, ry), closed: true}];
    }
    if (tag === 'line') return [{points: [[num(a.x1), num(a.y1)], [num(a.x2), num(a.y2)]], closed: false}];
    if (tag === 'polyline' || tag === 'polygon') {
      const n = (a.points || '').match(NUMBER) || [], pts = [];
      for (let i = 0; i + 1 < n.length; i += 2) pts.push([+n[i], +n[i + 1]]);
      if (tag === 'polygon') { if (pts.length < 3) return []; if (!close(pts[0], pts[pts.length - 1], 1e-12)) pts.push(pts[0]); return [{points: pts, closed: true}]; }
      return pts.length >= 2 ? [{points: pts, closed: false}] : [];
    }
    return [];
  }

  const IDENTITY = [1, 0, 0, 1, 0, 0];
  const compose = (m1, m2) => [m1[0] * m2[0] + m1[2] * m2[1], m1[1] * m2[0] + m1[3] * m2[1], m1[0] * m2[2] + m1[2] * m2[3],
                               m1[1] * m2[2] + m1[3] * m2[3], m1[0] * m2[4] + m1[2] * m2[5] + m1[4], m1[1] * m2[4] + m1[3] * m2[5] + m1[5]];
  function parseTransform(text) {
    let m = IDENTITY;
    for (const [, name, body] of (text || '').matchAll(/(matrix|translate|scale|rotate|skewX|skewY)\s*\(([^)]*)\)/g)) {
      const n = (body.match(NUMBER) || []).map(Number);
      let t = null;
      if (name === 'matrix' && n.length === 6) t = n;
      else if (name === 'translate') t = [1, 0, 0, 1, n[0] || 0, n[1] || 0];
      else if (name === 'scale') t = [n[0] ?? 1, 0, 0, n.length > 1 ? n[1] : (n[0] ?? 1), 0, 0];
      else if (name === 'rotate') {
        const a = (n[0] || 0) * Math.PI / 180, c = Math.cos(a), s = Math.sin(a);
        t = n.length >= 3 ? [c, s, -s, c, n[1] - c * n[1] + s * n[2], n[2] - s * n[1] - c * n[2]] : [c, s, -s, c, 0, 0];
      } else if (name === 'skewX') t = [1, 0, Math.tan((n[0] || 0) * Math.PI / 180), 1, 0, 0];
      else if (name === 'skewY') t = [1, Math.tan((n[0] || 0) * Math.PI / 180), 0, 1, 0, 0];
      if (t) m = compose(m, t);
    }
    return m;
  }
  const isIdentity = m => m.every((v, i) => Math.abs(v - IDENTITY[i]) < 1e-12);

  const LEAVES = ['path', 'circle', 'ellipse', 'rect', 'line', 'polyline', 'polygon'];
  const isNone = v => ['none', 'transparent'].includes(String(v ?? '').trim().toLowerCase());

  // parse_all_shapes(…, include_fills=True): {strokes: [{chains, fine, closed, width, cap, join, miter, matrix,
  // clip}], fills: [shape]} with every attribute resolved through its ancestors.
  function readShapes(text) {
    const rootEl = parseXml(CombineSide.inlineClassStyles(text));
    const ids = {};
    const walkIds = el => { if (el.attrib.id) ids[el.attrib.id] = ids[el.attrib.id] || el; el.children.forEach(walkIds); };
    walkIds(rootEl);
    const strokes = [], fills = [];
    const clipOf = (reference, matrix) => {
      const m = /url\(\s*['"]?#([^\s'")]+)['"]?\s*\)/.exec(reference);
      const el = m && ids[m[1]];
      if (!el || local(el.tag) !== 'clipPath') fail('Unresolved SVG clip-path: ' + reference);
      const parts = [];
      const walk = (node, at) => {
        const here = compose(at, parseTransform(node.attrib.transform));
        if (['clipPath', 'g'].includes(local(node.tag))) node.children.forEach(child => walk(child, here));
        else parts.push(mapShape(filledArea(leafChains(node), node.attrib['clip-rule'] || 'nonzero'), here));
      };
      walk(el, matrix);
      return union(parts);
    };
    const walk = (el, matrix, inherited, clip) => {
      const tag = local(el.tag), a = el.attrib;
      if (a.display === 'none' || ['hidden', 'collapse'].includes(a.visibility)) return;
      if (['defs', 'symbol', 'title', 'desc', 'metadata', 'style'].includes(tag)) return;
      const here = compose(matrix, parseTransform(a.transform));
      const own = {...inherited};
      const styled = {...a};
      for (const declaration of (a.style || '').split(';')) {
        const i = declaration.indexOf(':');
        if (i > 0) styled[declaration.slice(0, i).trim().toLowerCase()] = declaration.slice(i + 1).trim();
      }
      for (const k of ['fill', 'stroke', 'stroke-width', 'stroke-linecap', 'stroke-linejoin', 'stroke-miterlimit', 'fill-rule', 'clip-rule']) if (k in styled) own[k] = styled[k];
      if (a['clip-path'] && a['clip-path'] !== 'none') {
        const local_ = clipOf(a['clip-path'], here);
        clip = clip ? intersection(clip, local_) : local_;
      }
      if (['svg', 'g', 'a'].includes(tag)) { el.children.forEach(child => walk(child, here, own, clip)); return; }
      if (!LEAVES.includes(tag)) return;
      const chains = leafChains(el);
      const fill = own.fill ?? 'black';
      if (!['none', 'transparent', 'white', '#fff', '#ffffff'].includes(String(fill).toLowerCase())) {
        let geometry = filledArea(chains, own['fill-rule'] || 'nonzero');
        if (geometry.length) {
          geometry = isIdentity(here) ? geometry : mapShape(geometry, here);
          fills.push(clip ? intersection(geometry, clip) : geometry);
        }
      }
      const strokeColor = own.stroke ?? 'none';
      if (String(strokeColor).toLowerCase() === 'none') return;
      const width = num(own['stroke-width'] ?? '1', NaN);
      if (!(width > 0)) return;
      const miter = num(own['stroke-miterlimit'] ?? '4', 4);
      const fine = leafChains(el, 'fine');
      chains.forEach((chain, k) => strokes.push({
        points: chain.points, closed: chain.closed, fine: fine[k] ? fine[k].points : chain.points,
        width, cap: own['stroke-linecap'] || 'butt', join: own['stroke-linejoin'] || 'miter', miter: miter >= 1 ? miter : 4,
        matrix: here, clip}));
    };
    walk(rootEl, IDENTITY, {}, null);
    return {strokes, fills, root: rootEl};
  }

  // close_returning: a stroked line that ends where it starts is closed, as a final Z would be.
  function closeReturning(strokes) {
    for (const s of strokes) {
      const p = s.points;
      if (!s.closed && p.length > 3 && Math.max(Math.abs(p[0][0] - p[p.length - 1][0]), Math.abs(p[0][1] - p[p.length - 1][1])) < 1e-6) s.closed = true;
    }
    return strokes;
  }

  // stroke_to_polygon: each stroke painted at its width (from the curves, as skia strokes them), then merged.
  function strokeToPolygon(strokes, {sampled = false} = {}) {
    const painted = [];
    for (const s of strokes) {
      const points = sampled ? s.points : s.fine;
      let ink = stroke([{points, closed: s.closed}], s.width, {cap: s.cap, join: s.join, miter: s.miter, fine: !sampled});
      if (!isIdentity(s.matrix)) ink = mapShape(ink, s.matrix);
      if (s.clip) ink = intersection(ink, s.clip);
      if (ink.length) painted.push(ink);
    }
    return union(painted);
  }

  // ======== the parts as the build reads them ========

  // combination_layout_svg.elements + segments_of: each drawable element's engine segments, in element order.
  function elementSegments(documentText) {
    const rootEl = parseXml(documentText);
    const attrs = Object.fromEntries(Object.entries(rootEl.attrib).filter(([k]) => INHERITED.includes(k)));
    let found;
    try { found = drawables(rootEl); } catch (error) { throw new FillError(error.message); }
    return found.map(([el, own]) => segmentsOf(el, {...attrs, ...own}));
  }

  // The SVG's kind: a stroke-fill/v1 icon (regions plus its source strokes), a flat fill, or stroked lines.
  const isStrokeFill = text => /^\s*(?:<\?xml[^>]*>\s*)?<svg\b[^>]*\b(?:data-format="stroke-fill\/v1"|id="stroke-fill-v1")/.test(text);
  const isReverseFill = text => /^\s*(?:<\?xml[^>]*>\s*)?<svg\b[^>]*\bid="reverse-fill"/.test(text);

  // stroke_fill_format._parts: the regions and every stroked element (its paint, width, centerline and area).
  function strokeFillParts(text) {
    const rootEl = parseXml(text);
    let regions = EMPTY;
    const entries = [];
    const walk = (node, inherited, group) => {
      for (const child of node.children) {
        const name = local(child.tag);
        if (['defs', 'clipPath', 'mask', 'title', 'desc', 'metadata', 'style'].includes(name)) continue;
        const own = {...inherited};
        for (const k of INHERITED) if (k in child.attrib) own[k] = child.attrib[k];
        if (name === 'g') { walk(child, own, child); continue; }
        if (!LEAVES.includes(name)) continue;
        if (child.attrib.id === 'fill-regions') { regions = ownFilledArea(child); continue; }
        const groupId = group ? group.attrib.id || '' : '';
        const index = child.attrib['data-element'] != null ? parseInt(child.attrib['data-element'], 10)
          : /^element-(\d+)$/.test(child.attrib.id || '') ? parseInt(child.attrib.id.slice(8), 10) : -1;
        const stroked = !isNone(child.attrib.stroke ?? own.stroke ?? 'none');
        const filled = !isNone(child.attrib.fill ?? own.fill ?? 'none');
        const width = num(child.attrib['stroke-width'] ?? own['stroke-width'] ?? DEFAULT_WIDTH, DEFAULT_WIDTH);
        const lines = [];
        if (stroked) {
          const strokeAttrs = Object.fromEntries(Object.entries(own).filter(([k]) => k.startsWith('stroke')));
          const seen = new Set();
          for (const seg of segmentsOf(child, strokeAttrs)) {
            const key = seg.map(p => `${p[0].toFixed(6)},${p[1].toFixed(6)}`).join(' ');
            if (seg.length && !seen.has(key)) { seen.add(key); lines.push(seg); }
          }
        }
        let centerline = lines.map(seg => ({points: seg.length > 1 && lineLength(seg) > 1e-9 ? seg : [seg[0], seg[0]], closed: false}));
        if (stroked && child.attrib['stroke-dasharray']) centerline = dashed(child, centerline);
        entries.push({index, paint: groupId.includes('white') ? 'white' : 'black', under: groupId === 'white-strokes-under',
                      width, centerline: chainSegments(centerline), stroked, area: filled ? ownFilledArea(child) : EMPTY});
      }
    };
    walk(rootEl, {}, null);
    return {regions, entries};
  }

  // stroke_fill_rework.filled_area: one element's own fill (black, no stroke), read by the fill parser.
  const ownFilledArea = el => filledArea(leafChains(el), el.attrib['fill-rule'] || 'nonzero');

  // Two-point engine segments joined into runs where one ends at the next one's start (round joins make the
  // union of the segments' strokes the same as the run's stroke).
  function chainSegments(lines) {
    const out = [];
    for (const line of lines) {
      const last = out[out.length - 1];
      if (last && lineLength(line.points) > 0 && lineLength(last.points) > 0 && close(last.points[last.points.length - 1], line.points[0], 1e-9)) {
        last.points.push(...line.points.slice(1));
      } else out.push({points: line.points.slice(), closed: false});
    }
    return out;
  }

  // stroke_fill_format._dashed: the dash pieces of one continuous centerline, in path-length units.
  function dashed(el, centerline) {
    let pattern = el.attrib['stroke-dasharray'].replace(/,/g, ' ').trim().split(/\s+/).map(Number);
    const runs = chainSegments(centerline).filter(r => lineLength(r.points) > 0);
    if (runs.length !== 1) return centerline;
    const line = runs[0].points, lineLen = lineLength(line);
    let length = lineLen;
    if (local(el.tag) === 'path' && el.attrib.d) {
      length = pathChains(el.attrib.d, 'fine').reduce((s, c) => s + lineLength(c.points), 0) || lineLen;
    }
    if (pattern.length % 2) pattern = pattern.concat(pattern);
    const total = pattern.reduce((s, v) => s + v, 0);
    if (total <= 0 || lineLen <= 0) return centerline;
    const ratio = lineLen / length;
    let into = ((num(el.attrib['stroke-dashoffset'] || '0') % total) + total) % total, index = 0;
    while (into >= pattern[index]) { into -= pattern[index]; index = (index + 1) % pattern.length; }
    const pieces = [];
    let position = 0;
    while (position < length) {
      const end = Math.min(position + pattern[index] - into, length);
      if (index % 2 === 0 && end > position) pieces.push({points: substring(line, position * ratio, end * ratio), closed: false});
      position = end; into = 0; index = (index + 1) % pattern.length;
    }
    return pieces;
  }

  // LineString.interpolate: the point a distance along a polyline (its start for a zero-length one).
  function interpolate(points, distance) {
    let walked = 0;
    for (let i = 0; i + 1 < points.length; i++) {
      const a = points[i], b = points[i + 1], len = Math.hypot(b[0] - a[0], b[1] - a[1]);
      if (walked + len >= distance && len > 0) {
        const t = Math.max(0, (distance - walked) / len);
        return [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t];
      }
      walked += len;
    }
    return points[distance <= 0 ? 0 : points.length - 1];
  }

  // shapely.ops.substring of a polyline between two distances along it.
  function substring(points, from, to) {
    const out = [];
    let walked = 0;
    for (let i = 0; i + 1 < points.length; i++) {
      const a = points[i], b = points[i + 1], len = Math.hypot(b[0] - a[0], b[1] - a[1]);
      const lerp = d => [a[0] + (b[0] - a[0]) * (d - walked) / (len || 1), a[1] + (b[1] - a[1]) * (d - walked) / (len || 1)];
      if (walked + len >= from && walked <= to) {
        if (!out.length) out.push(from >= walked ? lerp(from) : a);
        if (to <= walked + len) { out.push(lerp(to)); break; }
        out.push(b);
      }
      walked += len;
    }
    if (out.length === 1) out.push(out[0]);
    return out;
  }

  const ink = (entry, m) => {
    const lines = entry.centerline.map(l => ({points: mapPoints(l.points, m), closed: false}));
    const strokes = entry.stroked && lines.length ? stroke(lines, entry.width) : EMPTY;
    return union([strokes, entry.area.length ? mapShape(entry.area, m) : EMPTY]);
  };

  // stroke_fill_format.render: the regions placed, then each layer of strokes drawn at its own width.
  function renderStrokeFill(parts, mapOf, pieces) {
    const placed = [];
    for (const [piece, m] of pieces || [[parts.regions, [1, 1, 0, 0]]]) {
      if (!piece.length) continue;
      const grow = Math.max(0, Math.max(m[0], m[1]) * TUCK - (DEFAULT_WIDTH / 2 - .2));
      const moved = mapShape(piece, m);
      placed.push(grow > 0 ? buffer(moved, grow) : moved);
    }
    let painted = union(placed);
    for (const layer of ['under', 'black', 'over']) {
      for (const entry of parts.entries) {
        if (layer === 'under' && !(entry.paint === 'white' && entry.under)) continue;
        if (layer === 'black' && entry.paint !== 'black') continue;
        if (layer === 'over' && !(entry.paint === 'white' && !entry.under)) continue;
        const drawn = ink(entry, mapOf(entry.index));
        painted = layer === 'black' ? union([painted, drawn]) : difference(painted, drawn);
      }
    }
    return painted;
  }

  // load_fill: the icon's ink at its own size, and whether it is stroked lines.
  const cache = new Map();
  function loaded(text) {
    if (cache.has(text)) return cache.get(text);
    let result;
    if (isStrokeFill(text)) {
      const parts = strokeFillParts(text);
      result = {kind: 'stroke-fill', parts, geometry: renderStrokeFill(parts, () => [1, 1, 0, 0]), stroked: true};
    } else {
      const shapes = readShapes(text);
      closeReturning(shapes.strokes);
      const strokes = shapes.strokes.length ? strokeToPolygon(shapes.strokes) : EMPTY;
      result = {kind: shapes.fills.length ? 'flat' : 'lines', shapes, geometry: union([strokes, ...shapes.fills]),
                stroked: strokes.length > 0, reverse: isReverseFill(text)};
    }
    if (isEmpty(result.geometry)) fail('The icon has no ink.');
    if (cache.size > 400) cache.delete(cache.keys().next().value);
    cache.set(text, result);
    return result;
  }

  // ======== placement: combine_fill_side_layouts.place_part ========

  function groupMap([x0, y0, x1, y1], box) {
    let sx = x1 - x0 > 1e-9 ? box.w / (x1 - x0) : null, sy = y1 - y0 > 1e-9 ? box.h / (y1 - y0) : null;
    sx = sx ?? sy ?? 1.0; sy = sy ?? sx;
    return [sx, sy, box.x - x0 * sx, box.y - y0 * sy];
  }

  function layoutGroups(segments, layout) {
    const boxes = segments.map(s => s.length ? bbox(s) : null);
    let groups;
    if (layout.length && layout.every(g => 'paths' in g)) {
      groups = layout.map(g => g.paths.filter(i => i < boxes.length && boxes[i]));
      const listed = groups.flat().sort((a, b) => a - b), drawable = boxes.map((b, i) => b ? i : null).filter(i => i !== null);
      if (listed.length !== drawable.length || listed.some((v, i) => v !== drawable[i])) fail('layout elements do not match the drawing');
    } else if (layout.length === 1) groups = [boxes.map((b, i) => b ? i : null).filter(i => i !== null)];
    else fail('several boxes without element numbers');
    return groups.map((g, k) => {
      const source = unionBoxes(g.map(i => boxes[i]));
      return {elements: g, source, map: groupMap(source, layout[k])};
    });
  }

  function movesAsOne(groups) {
    const first = groups[0].map;
    return groups.slice(1).every(({source: [x0, y0, x1, y1], map: m}) => {
      const mine = [x0 * m[0] + m[2], y0 * m[1] + m[3], x1 * m[0] + m[2], y1 * m[1] + m[3]];
      const theirs = [x0 * first[0] + first[2], y0 * first[1] + first[3], x1 * first[0] + first[2], y1 * first[1] + first[3]];
      return Math.max(...mine.map((v, i) => Math.abs(v - theirs[i]))) <= SAME_MAP;
    });
  }

  function plausible(groups) {
    return groups.every(({source: [x0, y0, x1, y1], map: [sx, sy]}) => {
      const flat = x1 - x0 <= 1e-9 || y1 - y0 <= 1e-9;
      if (!(1 / MAX_GROUP_SCALE <= sx && sx <= MAX_GROUP_SCALE) || !(1 / MAX_GROUP_SCALE <= sy && sy <= MAX_GROUP_SCALE)) return false;
      return flat || Math.max(sx, sy) / Math.min(sx, sy) <= MAX_GROUP_STRETCH;
    });
  }

  const layoutBox = layout => {
    if (!layout.length) fail('The part has no layout boxes.');
    const x0 = Math.min(...layout.map(g => g.x)), y0 = Math.min(...layout.map(g => g.y));
    return {x: x0, y: y0, w: Math.max(...layout.map(g => g.x + g.w)) - x0, h: Math.max(...layout.map(g => g.y + g.h)) - y0};
  };

  // keep_stroke_weight: a scaled fill painted as a 4px stroke drawing keeps its half stroke.
  function keepStrokeWeight(geometry, m) {
    const s = (m[0] + m[1]) / 2, grown = HALF_STROKE * (s - 1);
    if (Math.abs(grown) < 1e-3) return geometry;
    return union(polygons(geometry).map(p => {
      const body = buffer(exterior(p), -grown);
      const holes = p.holes.map(h => {
        const hole = normalize([h]);
        const slit = isEmpty(buffer(hole, -HALF_STROKE * s * 1.1));
        return buffer(hole, slit ? -grown : grown);
      });
      return holes.length ? difference(body, union(holes)) : body;
    }));
  }

  // restroke: stroked lines (no filled shapes) moved, then painted at their own width.
  function restroke(fill, m) {
    if (fill.kind !== 'lines') return null;
    const moved = fill.shapes.strokes.map(s => ({...s, points: mapPoints(mapPoints(s.points, s.matrix), m),
      fine: mapPoints(mapPoints(s.fine, s.matrix), m), matrix: IDENTITY, clip: s.clip ? mapShape(s.clip, m) : null}));
    return strokeToPolygon(moved);
  }

  // rebuild_strokes: a flat fill moved by its layout, its strokes redrawn 4px wide on the moved centerlines.
  function rebuildStrokes(fill, segments, groups, pieces) {
    const black = [], white = [], blackHere = [], whiteHere = [];
    for (const {elements, map: m} of groups) {
      for (const i of elements) {
        for (const seg of segments[i]) {
          if (seg.length < 2) continue;
          const length = lineLength(seg), n = Math.max(1, Math.trunc(length / CLASSIFY_STEP));
          for (let k = 0; k < n; k++) {
            const part = substring(seg, length * k / n, length * (k + 1) / n);
            if (lineLength(part) <= 0) continue;
            const mid = interpolate(seg, length * (k + .5) / n);
            const inked = contains(fill, mid, true);
            (inked ? blackHere : whiteHere).push({points: part, closed: false});
            (inked ? black : white).push({points: mapPoints(part, m), closed: false});
          }
        }
      }
    }
    if (!black.length && !white.length) return null;
    // Consecutive pieces of one kind are one run: the same round-joined stroke from far fewer paths.
    [black, white, blackHere, whiteHere].forEach(list => list.splice(0, list.length, ...chainSegments(list)));
    const strokesHere = blackHere.length ? stroke(blackHere, 2 * HALF_STROKE) : EMPTY;
    const cutsHere = whiteHere.length ? stroke(whiteHere, 2 * (HALF_STROKE + .05)) : EMPTY;
    const regions = [];
    for (const [piece, m] of pieces) {
      const reach = HALF_STROKE + .3;
      const closed = buffer(buffer(piece, reach), -reach);
      const inside = union([closed, ...polygons(piece).map(exterior)]);
      const whole = union([piece, intersection(cutsHere, inside)]);
      let region = difference(whole, strokesHere);
      region = buffer(buffer(region, -SLIVER), SLIVER);
      if (isEmpty(region)) continue;
      const s = (m[0] + m[1]) / 2, grown = Math.max(0, HALF_STROKE * (s - 1));
      const outline = union(polygons(whole).map(exterior));
      let bound = buffer(mapShape(outline, m), -HALF_STROKE * (s - 1));
      const counters = union(polygons(whole).flatMap(p => p.holes.map(h => normalize([h]))));
      if (counters.length) bound = difference(bound, buffer(mapShape(counters, m), grown));
      regions.push(intersection(buffer(mapShape(region, m), grown + .05), bound));
    }
    const painted = union([...regions, black.length ? stroke(black, 2 * HALF_STROKE) : EMPTY]);
    return white.length ? difference(painted, stroke(white, 2 * HALF_STROKE)) : painted;
  }

  // split_fill: each fill part to the group whose strokes it was drawn from (Voronoi cells of centerline points).
  function splitFill(fill, segments, groups) {
    const lines = groups.map(({elements}) => elements.flatMap(i => segments[i].filter(s => s.length > 1)));
    const inkOf = lines.map(ls => stroke(ls.map(points => ({points, closed: false})), 2 * HALF_STROKE));
    const points = [], owner = [], seen = new Set();
    lines.forEach((ls, n) => {
      for (const line of ls) {
        const length = lineLength(line), steps = Math.max(1, Math.trunc(length / SAMPLE_STEP));
        for (let k = 0; k <= steps; k++) {
          const p = interpolate(line, length * k / steps);
          const key = `${p[0].toFixed(6)},${p[1].toFixed(6)}`;
          if (!seen.has(key)) { seen.add(key); points.push(p); owner.push(n); }
        }
      }
    });
    const box = bounds(fill);
    const extent = [box[0] - 64, box[1] - 64, box[2] + 64, box[3] + 64];
    const regions = groups.map((_, n) => voronoiRegion(points, owner, n, extent));
    const pieces = groups.map(() => []);
    let divided = false;
    for (const p of polygons(fill)) {
      const part = polygonShape(p);
      const overlap = inkOf.map(i => area(intersection(part, i)));
      const total = overlap.reduce((s, v) => s + v, 0);
      let best = 0;
      overlap.forEach((v, i) => { if (v > overlap[best]) best = i; });
      if (total <= 0 || overlap[best] >= OWNER_SHARE * total) { pieces[best].push(part); continue; }
      divided = true;
      // The group with most of the part's ink keeps it whole (a region divided between groups that move apart
      // would open white seams along the cut); each other group also draws its own share where it goes.
      pieces[best].push(part);
      regions.forEach((region, n) => { if (n === best) return; const piece = intersection(part, region); if (piece.length) pieces[n].push(piece); });
    }
    return {pieces: pieces.map((p, n) => [union(p), groups[n].map, p.length]).filter(x => x[2]).map(([p, m]) => [p, m]), divided};
  }

  // The points nearer one owner's points than any other owner's: the union of their Voronoi cells, each cut from the
  // extent by the bisectors with the other owners' points (a point's own owner's points do not divide the region).
  function voronoiRegion(points, owner, n, [x0, y0, x1, y1]) {
    const mine = points.filter((_, i) => owner[i] === n), others = points.filter((_, i) => owner[i] !== n);
    const cells = [];
    for (const p of mine) {
      let cell = [[x0, y0], [x1, y0], [x1, y1], [x0, y1]];
      let reach = Math.max(...cell.map(c => Math.hypot(c[0] - p[0], c[1] - p[1])));
      const near = others.map(q => [Math.hypot(q[0] - p[0], q[1] - p[1]), q]).sort((a, b) => a[0] - b[0]);
      for (const [d, q] of near) {
        if (d > 2 * reach) break;
        cell = halfPlane(cell, p, q);
        if (cell.length < 3) break;
        reach = Math.max(...cell.map(c => Math.hypot(c[0] - p[0], c[1] - p[1])));
      }
      if (cell.length >= 3) cells.push(ring(cell));
    }
    return normalize(cells);
  }
  // The part of a convex polygon nearer p than q.
  function halfPlane(cell, p, q) {
    const mx = (p[0] + q[0]) / 2, my = (p[1] + q[1]) / 2, nx = q[0] - p[0], ny = q[1] - p[1];
    const side = c => (c[0] - mx) * nx + (c[1] - my) * ny;
    const out = [];
    for (let i = 0; i < cell.length; i++) {
      const a = cell[i], b = cell[(i + 1) % cell.length], sa = side(a), sb = side(b);
      if (sa <= 0) out.push(a);
      if ((sa < 0 && sb > 0) || (sa > 0 && sb < 0)) { const t = sa / (sa - sb); out.push([a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t]); }
    }
    return out;
  }

  // whole_box: the whole fill in the box all the layout's groups cover (measured from the fill's own ink).
  function wholeBox(fill, layout, {scaleStrokeWeight = false, restroked = true} = {}) {
    const [x0, y0, x1, y1] = bounds(fill.geometry);
    const m = groupMap([x0 + HALF_STROKE, y0 + HALF_STROKE, x1 - HALF_STROKE, y1 - HALF_STROKE], layoutBox(layout));
    if (scaleStrokeWeight) return {geometry: mapShape(fill.geometry, m), how: 'whole_box', map: m};
    if (fill.kind === 'stroke-fill') return {geometry: renderStrokeFill(fill.parts, () => m, [[fill.parts.regions, m]]), how: 'whole_box', map: m};
    const lines = fill.reverse || !restroked ? null : restroke(fill, m);
    return {geometry: lines ?? keepStrokeWeight(mapShape(fill.geometry, m), m), how: 'whole_box', map: m};
  }

  function readGroups(source, layout) {
    const segments = elementSegments(source);
    let groups = layoutGroups(segments, layout), how = 'rigid';
    if (!plausible(groups)) {
      const everything = groups.flatMap(g => g.elements);
      const box = unionBoxes(everything.map(i => bbox(segments[i])));
      groups = [{elements: everything, source: box, map: groupMap(box, layoutBox(layout))}];
      how = 'layout_mismatch';
    }
    return {segments, groups, how};
  }

  // place_part: the part's icon moved by its layout, and how ('rigid' | 'split' | 'split_divided' | …).
  // `restroked`: stroked lines are painted again after they move (false: an outline sub is its strokes' outline
  // moved, as pair_layout_review placed it, with no fill file to restroke).
  function placePart(fill, source, layout, {restroked = true, scaleStrokeWeight = false} = {}) {
    let read;
    try { read = readGroups(source, layout); }
    catch (error) { if (error instanceof FillError) return wholeBox(fill, layout, {restroked, scaleStrokeWeight: scaleStrokeWeight && fill.kind !== 'stroke-fill'}); throw error; }
    const {segments, groups} = read;
    let how = read.how;
    if (fill.kind === 'stroke-fill') {
      const regions = fill.parts.regions, first = groups[0].map;
      if (groups.length === 1 || movesAsOne(groups)) return {geometry: renderStrokeFill(fill.parts, () => first, [[regions, first]]), how, map: first};
      const maps = new Map(groups.flatMap(g => g.elements.map(i => [i, g.map])));
      const {pieces, divided} = regions.length ? splitFill(regions, segments, groups) : {pieces: [], divided: false};
      return {geometry: renderStrokeFill(fill.parts, index => maps.get(index) || first, pieces), how: divided ? 'split_divided' : 'split', map: null};
    }
    if (groups.length === 1 || movesAsOne(groups)) {
      const m = groups[0].map;
      if (scaleStrokeWeight) return {geometry: mapShape(fill.geometry, m), how, map: m};
      let lines = fill.reverse || !restroked ? null : restroke(fill, m);
      if (lines === null && !fill.reverse && Math.abs(m[0] - 1) + Math.abs(m[1] - 1) > 1e-3) lines = rebuildStrokes(fill.geometry, segments, groups, [[fill.geometry, m]]);
      return {geometry: lines ?? keepStrokeWeight(mapShape(fill.geometry, m), m), how, map: m};
    }
    const {pieces, divided} = splitFill(fill.geometry, segments, groups);
    how = divided ? 'split_divided' : 'split';
    if (scaleStrokeWeight) return {geometry: union(pieces.map(([piece, m]) => mapShape(piece, m))), how, map: null};
    if (!fill.reverse) {
      const rebuilt = rebuildStrokes(fill.geometry, segments, groups, pieces);
      if (rebuilt !== null) return {geometry: rebuilt, how, map: null};
    }
    return {geometry: union(pieces.map(([piece, m]) => keepStrokeWeight(mapShape(piece, m), m))), how, map: null};
  }

  // outline_boxes: the boxes the outline is baked into, as placePart moves it (null: the layout cannot number it).
  function outlineBoxes(source, layout) {
    let segments, groups;
    try { segments = elementSegments(source); groups = layoutGroups(segments, layout); }
    catch (error) { if (error instanceof FillError) return null; throw error; }
    if (plausible(groups)) return layout.map((box, k) => ({...box, paths: groups[k].elements}));
    const b = layoutBox(layout);
    return [{paths: groups.flatMap(g => g.elements).sort((m, n) => m - n), ...b}];
  }

  // ======== the cut: combine_fill_side ========

  const clearance = (sub, gap = GAP) => buffer(convexHull(sub), gap);

  function roundCutEnds(cut, clear) {
    const r = HALF_STROKE - EPS;
    const opened = buffer(buffer(cut, -r), r);
    const band = difference(buffer(clear, 2 * HALF_STROKE), clear);
    return difference(cut, difference(band, opened));
  }

  function cleanMain(main) {
    const kept = [];
    for (const p of polygons(main)) {
      const part = polygonShape(p);
      if (area(part) < MIN_PART_AREA || isEmpty(buffer(part, -MIN_PART_WIDTH / 2))) continue;
      kept.push(polygonShape(dropTinyHoles(p, MIN_HOLE_AREA)));
    }
    const cleaned = union(kept);
    return {cleaned, big: polygons(cleaned).filter(p => area(polygonShape(p)) >= FRAGMENT_AREA).length};
  }

  function holesNear(main, clear) {
    const zone = buffer(clear, 2 * HALF_STROKE);
    const out = [], later = [];
    let closed = 0;
    for (const p of polygons(main)) {
      const keep = [];
      for (const h of p.holes) {
        const hole = normalize([h]);
        if (!intersects(hole, zone)) { keep.push(h); continue; }
        const holeArea = area(hole);
        const detail = holeArea < DETAIL_AREA || isEmpty(buffer(hole, -HALF_STROKE * 1.1));
        if (detail && area(difference(hole, zone)) < STUB_SHARE * holeArea) closed += 1;
        else if (intersects(hole, clear)) keep.push(h);
        else later.push(hole);
      }
      out.push([p.outer, ...keep]);
    }
    return {solid: out.length ? union(out) : main, later, closed};
  }

  function dropCutScraps(drawn, cut) {
    const pieces = polygons(cut).map(polygonShape), parts = polygons(drawn).map(polygonShape);
    const owner = new Map();
    pieces.forEach((piece, i) => {
      let best = 0, at = null;
      parts.forEach((part, k) => { const a = area(intersection(piece, part)); if (a > best) { best = a; at = k; } });
      if (best > EPS) owner.set(i, at);
    });
    const keep = [];
    let dropped = 0;
    parts.forEach((_, k) => {
      const mine = pieces.filter((_, i) => owner.get(i) === k);
      if (!mine.length) return;
      const areas = mine.map(area), largest = areas.indexOf(Math.max(...areas));
      mine.forEach((p, i) => { if (i === largest || areas[i] >= SCRAP_AREA) keep.push(p); else dropped += 1; });
    });
    return {cut: union(keep), dropped};
  }

  function cutMain(main, sub, gap = GAP) {
    const clear = clearance(sub, gap);
    const {solid, later, closed} = holesNear(main, clear);
    let cut = difference(solid, clear);
    const erased = area(solid) - area(cut);
    if (erased > EPS) cut = roundCutEnds(cut, clear);
    if (later.length) {
      cut = difference(cut, union(later));
      // Black islands inside a reopened white opening are restored, clear of the sub.
      const islands = polygons(main).filter(p => later.some(hole => contains(hole, representativePoint(p))));
      if (islands.length) cut = union([cut, ...islands.map(p => difference(polygonShape(p), clear))]);
    }
    const scraps = dropCutScraps(main, cut);
    const {cleaned, big} = cleanMain(scraps.cut);
    const drawn = cleanMain(main).big;
    return {cut: cleaned, details: {erased_area: +erased.toFixed(3), main_parts: big, closed_holes: closed,
                                    dropped_scraps: scraps.dropped, split_parts: Math.max(0, big - drawn)}};
  }

  // cut_outline_strokes: the outline's centerlines clipped around the sub's ink, painted again at their widths.
  function cutOutlineStrokes(placedSvg, sub, gap = GAP) {
    const shapes = readShapes(placedSvg);
    closeReturning(shapes.strokes);
    const clipped = [];
    for (const s of shapes.strokes) {
      const points = mapPoints(s.points, s.matrix);
      const clear = buffer(sub, gap + s.width / 2);
      const piece = extra => ({...s, matrix: IDENTITY, clip: null, ...extra});
      if (lineLength(points) <= EPS) {
        if (!contains(clear, points[0])) clipped.push(piece({points, fine: points}));
        continue;
      }
      const remaining = linesOutside([{points}], clear);
      const wasCut = remaining.reduce((t, l) => t + lineLength(l), 0) < lineLength(points) - EPS;
      for (const part of remaining) {
        if (lineLength(part) <= EPS || (wasCut && lineLength(part) < 1.5 * s.width)) continue;
        clipped.push(piece({points: part, fine: part, closed: false}));
      }
    }
    const strokes = clipped.length ? strokeToPolygon(clipped, {sampled: true}) : EMPTY;
    const painted = buffer(sub, gap);
    const cut = union([strokes, ...shapes.fills.map(f => difference(f, painted))]);
    return {cut, details: {main_parts: cleanMain(cut).big}};
  }

  // ======== the SVG written: fill_utils.geometry_to_svg ========

  const coord = v => { const s = v.toFixed(3).replace(/\.?0+$/, ''); return s === '-0' || s === '' ? '0' : s; };
  function toSvg(shape, size = CANVAS) {
    const d = polygons(shape).map(p => [p.outer, ...p.holes].map(r => {
      const pts = pointsOf(r);
      return 'M' + pts.map(([x, y]) => `${coord(x)},${coord(y)}`).join('L') + 'Z';
    }).join('')).join('');
    return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 ${size} ${size}">` +
           `<path d="${d}" fill="#000000" fill-rule="nonzero"/></svg>`;
  }

  // ======== a pick ========

  // pick_combine.omitted: main elements left out (unstroked in the source, dropped from a stroke-fill).
  function omitted(source, fill, omit) {
    const want = new Set(omit);
    const rootEl = parseXml(source);
    const drawn = [];
    const walk = el => { for (const child of el.children) { if (LEAVES.includes(local(child.tag))) drawn.push(child); walk(child); } };
    walk(rootEl);
    for (const i of want) if (drawn[i]) { drawn[i].attrib.stroke = 'none'; drawn[i].attrib.fill = 'none'; }
    const sourceOut = CombineSide.tostring(rootEl);
    if (fill === null) return [sourceOut, null];
    const fillRoot = parseXml(fill);
    const prune = el => {
      el.children = el.children.filter(child => {
        const index = child.attrib['data-element'] != null ? +child.attrib['data-element']
          : /^element-(\d+)$/.test(child.attrib.id || '') ? +child.attrib.id.slice(8) : -1;
        return !want.has(index);
      });
      el.children.forEach(prune);
    };
    prune(fillRoot);
    return [sourceOut, CombineSide.tostring(fillRoot)];
  }

  function placeRole(part, source, fillText, options) {
    const fill = loaded(fillText ?? source);
    return placePart(fill, source, part.layout || [], options);
  }

  // {main|sub: {svg, source, layout, outline}, options} → {svg, area, bounds, how, main, sub}
  function combine(pick) {
    const options = pick.options || {}, main = pick.main, sub = pick.sub;
    let mainSource = main.source, mainFill = main.outline ? null : main.svg;
    if (options.omit && options.omit.length) [mainSource, mainFill] = omitted(mainSource, mainFill, options.omit);
    const placedMain = placeRole(main, mainSource, mainFill);
    // A sub placed under 20px with its fill (options.sub_scaled) scales its stroke too, as pair_layout_review
    // places it: a 4px stroke would close its small white marks.
    const placedSub = placeRole(sub, sub.source, sub.outline ? null : sub.svg,
                                {restroked: !sub.outline, scaleStrokeWeight: !sub.outline && !!options.sub_scaled});
    const subInk = placedSub.geometry;
    let cut;
    if (options.overlap === 'join') cut = placedMain.geometry;
    else if (main.outline) {
      const boxes = outlineBoxes(mainSource, main.layout || []);
      if (boxes === null) cut = cutMain(placedMain.geometry, subInk).cut;
      else {
        let baked;
        try { baked = bake('main', mainSource, boxes, CANVAS).document; } catch (error) { baked = null; }
        cut = baked === null ? cutMain(placedMain.geometry, subInk).cut : cutOutlineStrokes(baked, subInk).cut;
      }
    } else cut = cutMain(placedMain.geometry, subInk).cut;
    const combined = union([cut, subInk]);
    return {svg: toSvg(combined), geometry: combined, area: area(combined), bounds: bounds(combined),
            main: {geometry: cut, area: area(cut), how: placedMain.how, placed: placedMain.geometry},
            sub: {geometry: subInk, area: area(subInk), how: placedSub.how}};
  }

  // How much two drawings differ, in px²: what either covers that the other does not, less the slivers thinner than
  // 0.3 px along their edges (two engines rounding the same curve differently; nothing a 64 icon shows).
  function differs(svgA, svgB) {
    const a = loaded(svgA).geometry, b = loaded(svgB).geometry;
    const xor = clip(C.ClipType.ctXor, a, b);
    return area(buffer(buffer(xor, -0.15, {fine: true}), 0.15, {fine: true}));
  }

  // shapely's intersects: they overlap, or their edges touch.
  function intersects(a, b) {
    const ba = bounds(a), bb = bounds(b);
    if (!ba || !bb || ba[2] < bb[0] || bb[2] < ba[0] || ba[3] < bb[1] || bb[3] < ba[1]) return false;
    if (area(intersection(a, b)) > 1e-12) return true;
    return distance(a, b) <= 2 / SCALE;
  }

  // The distance between two drawings (0 when they touch): the nearest of every vertex of one to every edge of the
  // other, edges far from the other's box skipped.
  function distance(a, b) {
    if (!a.length || !b.length) return null;
    if (area(intersection(a, b)) > 1e-9) return 0;
    const edges = shape => shape.flatMap(path => path.map((p, i) => [p, path[(i + 1) % path.length]]));
    const toEdge = (p, [s, e]) => {
      const dx = e.X - s.X, dy = e.Y - s.Y, length = dx * dx + dy * dy;
      const t = length ? Math.max(0, Math.min(1, ((p.X - s.X) * dx + (p.Y - s.Y) * dy) / length)) : 0;
      return Math.hypot(p.X - s.X - t * dx, p.Y - s.Y - t * dy);
    };
    let best = Infinity;
    for (const [from, to] of [[a, b], [b, a]]) {
      const targets = edges(to);
      for (const path of from) for (const p of path) for (const edge of targets) {
        const d = toEdge(p, edge);
        if (d < best) best = d;
      }
    }
    return best / SCALE;
  }

  return {combine, differs, toSvg, FillError,
          internals: {loaded, placePart, cutMain, distance, normalize, mapShape, cutOutlineStrokes, clearance, readShapes, strokeToPolygon, pathChains,
                      polygons, area, bounds, union, difference, intersection, buffer, stroke, convexHull, outlineBoxes}};
});
