'use strict';

/**
 * Browser-side mirror of the authoritative Python shape registry.
 *
 * Geometry is PARAMETRIC: `geometry(w, h)` returns the actual SVG primitive
 * (tag + attributes) drawn at real size in a local 0..w x 0..h box. Shapes are
 * never scaled with a transform — resizing recomputes the geometry — so
 * stroke width stays constant no matter the size. Only rigid ops (translate,
 * rotate, flip) are applied as transforms, which never distort strokes.
 *
 *   id        stable identifier (also the asset filename)
 *   name      label shown in the palette
 *   closed    true  → closed outline that can optionally be filled
 *             false → open path (line/curve), never filled
 *   natural   the size the palette thumbnail and asset file are drawn at
 *   defaultW/defaultH  size (in canvas units) when dropped on the canvas
 *   geometry(w, h)     the SVG primitive for a w x h instance
 *
 * `core/shape_registry.py` owns canonical geometry used for emission,
 * validation, and standalone asset generation. Registry tests guard this
 * browser mirror's IDs and representative formulas against drift.
 */
const N = v => +v.toFixed(3);
const TAN_15 = Math.tan(Math.PI / 12);
const TAN_60 = Math.tan(Math.PI / 3);

const dashedRectanglePath = (w, h) => {
  const perimeter = 2 * (w + h);
  const boundaries = [w, w + h, 2 * w + h, perimeter];
  const pointAt = distance => {
    const s = Math.min(Math.max(distance, 0), perimeter);
    if (s <= w) return [s, 0];
    if (s <= w + h) return [w, s - w];
    if (s <= 2 * w + h) return [2 * w + h - s, h];
    return [0, perimeter - s];
  };
  const parts = [];
  for (let start = 0; start < perimeter; start += 8) {
    const end = Math.min(start + 4, perimeter);
    let [x, y] = pointAt(start);
    parts.push(`M ${N(x)} ${N(y)}`);
    boundaries.filter(boundary => start < boundary && boundary < end).forEach(boundary => {
      [x, y] = pointAt(boundary);
      parts.push(`L ${N(x)} ${N(y)}`);
    });
    [x, y] = pointAt(end);
    parts.push(`L ${N(x)} ${N(y)}`);
  }
  return parts.join(' ');
};

const SHAPES = [
  // ---- Closed shapes -------------------------------------------------
  {
    id: 'circle', name: 'Circle', closed: true,
    natural: { w: 20, h: 20 }, defaultW: 8, defaultH: 8,
    geometry: (w, h) => ({ tag: 'ellipse', attrs: { cx: N(w / 2), cy: N(h / 2), rx: N(w / 2), ry: N(h / 2) } }),
  },
  {
    id: 'ellipse', name: 'Ellipse', closed: true,
    natural: { w: 20, h: 12 }, defaultW: 10, defaultH: 6,
    geometry: (w, h) => ({ tag: 'ellipse', attrs: { cx: N(w / 2), cy: N(h / 2), rx: N(w / 2), ry: N(h / 2) } }),
  },
  {
    id: 'square', name: 'Square', closed: true,
    natural: { w: 20, h: 20 }, defaultW: 8, defaultH: 8,
    geometry: (w, h) => ({ tag: 'rect', attrs: { x: 0, y: 0, width: N(w), height: N(h) } }),
  },
  {
    id: 'rectangle', name: 'Rectangle', closed: true,
    natural: { w: 20, h: 12 }, defaultW: 10, defaultH: 6,
    geometry: (w, h) => ({ tag: 'rect', attrs: { x: 0, y: 0, width: N(w), height: N(h) } }),
  },
  {
    id: 'dashed-rectangle', name: 'Dashed rectangle', closed: false,
    natural: { w: 20, h: 28 }, defaultW: 12, defaultH: 20,
    // A paint-free broken rectangular perimeter with a fixed 4u dash / 4u gap
    // rhythm. Dashes continue around corners as geometry, so resizing never
    // changes the canonical stroke or relies on a presentation attribute.
    geometry: (w, h) => ({ tag: 'path', attrs: { d: dashedRectanglePath(w, h) } }),
  },
  {
    id: 'water-drop', name: 'Water drop', closed: true,
    natural: { w: 12, h: 18 }, defaultW: 8, defaultH: 12,
    geometry: (w, h) => ({
      tag: 'path', attrs: {
        d: `M ${N(w / 2)} 0 Q ${N(w)} ${N(h * 0.45)} ${N(w)} ${N(h * 0.7)} ` +
           `Q ${N(w)} ${N(h)} ${N(w / 2)} ${N(h)} Q 0 ${N(h)} 0 ${N(h * 0.7)} ` +
           `Q 0 ${N(h * 0.45)} ${N(w / 2)} 0 Z`,
      },
    }),
  },
  {
    id: 'tapered-spire', name: 'Tapered spire', closed: true,
    natural: { w: 24, h: 32 }, defaultW: 16, defaultH: 24,
    // Symmetric pointed shell with two organic quadratic sides and a flat
    // base. It stays edge-to-edge at any size without introducing shoulders.
    geometry: (w, h) => ({
      tag: 'path',
      attrs: {
        d: `M ${N(w / 2)} 0 Q 0 ${N(h * 0.7)} 0 ${N(h)} ` +
           `L ${N(w)} ${N(h)} Q ${N(w)} ${N(h * 0.7)} ${N(w / 2)} 0 Z`,
      },
    }),
  },
  {
    id: 'rounded-square', name: 'Rounded square', closed: true,
    natural: { w: 20, h: 20 }, defaultW: 8, defaultH: 8,
    geometry: (w, h) => ({ tag: 'rect', attrs: { x: 0, y: 0, width: N(w), height: N(h), rx: N(Math.min(w, h) * 0.2) } }),
  },
  {
    id: 'rounded-rectangle', name: 'Rounded rectangle', closed: true,
    natural: { w: 24, h: 32 }, defaultW: 16, defaultH: 20,
    // New-grid rectangle with the ordinary 4u corner token. The radius clamps
    // only when a very small box cannot physically contain the full token.
    geometry: (w, h) => ({ tag: 'rect', attrs: { x: 0, y: 0, width: N(w), height: N(h), rx: N(Math.min(4, w / 2, h / 2)) } }),
  },
  {
    id: 'pill', name: 'Pill', closed: true,
    natural: { w: 20, h: 8 }, defaultW: 10, defaultH: 4,
    geometry: (w, h) => ({ tag: 'rect', attrs: { x: 0, y: 0, width: N(w), height: N(h), rx: N(Math.min(w, h) / 2) } }),
  },
  {
    id: 'triangle', name: 'Triangle', closed: true,
    natural: { w: 20, h: 20 }, defaultW: 8, defaultH: 8,
    geometry: (w, h) => ({ tag: 'path', attrs: { d: `M ${N(w / 2)} 0 L ${N(w)} ${N(h)} L 0 ${N(h)} Z` } }),
  },
  {
    id: 'right-triangle', name: 'Right triangle', closed: true,
    natural: { w: 20, h: 20 }, defaultW: 8, defaultH: 8,
    geometry: (w, h) => ({ tag: 'path', attrs: { d: `M 0 0 L ${N(w)} ${N(h)} L 0 ${N(h)} Z` } }),
  },
  {
    id: 'diamond', name: 'Diamond', closed: true,
    natural: { w: 20, h: 20 }, defaultW: 8, defaultH: 8,
    geometry: (w, h) => ({
      tag: 'path',
      attrs: { d: `M ${N(w / 2)} 0 L ${N(w)} ${N(h / 2)} L ${N(w / 2)} ${N(h)} L 0 ${N(h / 2)} Z` },
    }),
  },
  {
    id: 'gable', name: 'Gable', closed: true,
    natural: { w: 14, h: 20 }, defaultW: 8, defaultH: 12,
    // Closed pentagon: a rectangular body under a peaked head. The head rise
    // is w/2, so both roof edges sit at exactly 45 degrees at every size, and
    // the body runs from the springing line down to the bottom edge. When
    // h <= w/2 the body vanishes and the outline degenerates to the triangle
    // spanning the box, which keeps the atom valid across its whole size
    // range. This is the pointed-head counterpart of the round-headed `arch`.
    geometry: (w, h) => {
      const r = Math.min(w / 2, h);
      const d = h - r > 0
        ? `M 0 ${N(h)} L 0 ${N(r)} L ${N(w / 2)} 0 L ${N(w)} ${N(r)} L ${N(w)} ${N(h)} Z`
        : `M 0 ${N(r)} L ${N(w / 2)} 0 L ${N(w)} ${N(r)} Z`;
      return { tag: 'path', attrs: { d } };
    },
  },
  {
    id: 'twin-gable', name: 'Twin gable', closed: true,
    natural: { w: 40, h: 32 }, defaultW: 16, defaultH: 12,
    // One reusable closed shell for two equal adjoining peaked forms. The
    // shared valley is part of the outer contour; a separate line can add a
    // central wall without doubling either roof or side geometry.
    geometry: (w, h) => {
      const r = Math.min(w / 4, h);
      return {
        tag: 'path',
        attrs: {
          d: `M 0 ${N(h)} L 0 ${N(r)} L ${N(w / 4)} 0 L ${N(w / 2)} ${N(r)} ` +
             `L ${N(3 * w / 4)} 0 L ${N(w)} ${N(r)} L ${N(w)} ${N(h)} Z`,
        },
      };
    },
  },
  {
    id: 'sloped-box', name: 'Sloped box', closed: true,
    natural: { w: 24, h: 18 }, defaultW: 16, defaultH: 14,
    // One-sided modern building shell. The roof is always exactly 15 degrees;
    // useful instances keep h >= w*tan(15deg) so the left wall remains.
    geometry: (w, h) => {
      const rise = Math.min(w * TAN_15, h);
      return { tag: 'path', attrs: { d: `M 0 ${N(rise)} L ${N(w)} 0 L ${N(w)} ${N(h)} L 0 ${N(h)} Z` } };
    },
  },
  {
    id: 'trapezoid', name: 'Trapezoid', closed: true,
    natural: { w: 24, h: 12 }, defaultW: 16, defaultH: 8,
    // Closed symmetric quadrilateral: a full-width base under a narrower flat
    // top, both sides fixed at exactly 60 degrees from horizontal at every
    // size — the same on-grid guarantee `gable` gives its 45 degree roof and
    // `sloped-box` its 15 degree one. The inset is `h / tan(60deg)`, clamped to
    // `w * 0.4` so the top edge can never collapse to a point and the whole
    // size range stays valid; a squat box gives a shallow flare, a tall one
    // reaches the clamp and holds a 20 percent top edge. This is the
    // flat-topped, two-sided counterpart of the one-sided `sloped-box` and the
    // peaked `gable`. Default orientation is the wide base; `flipY` gives the
    // hopper and `rotation` lays it on its side.
    geometry: (w, h) => {
      const inset = Math.min(h / TAN_60, w * 0.4);
      return {
        tag: 'path',
        attrs: { d: `M ${N(inset)} 0 L ${N(w - inset)} 0 L ${N(w)} ${N(h)} L 0 ${N(h)} Z` },
      };
    },
  },
  {
    id: 'flared-horn', name: 'Flared horn', closed: true,
    natural: { w: 24, h: 16 }, defaultW: 24, defaultH: 16,
    // Closed flared tube with a narrow rear opening and a full-height bell.
    // Its quadratic sides keep the silhouette natural across useful aspect
    // ratios. Reuse it for horns, speaker bells, funnels, and nozzles.
    geometry: (w, h) => ({
      tag: 'path',
      attrs: {
        d: `M 0 ${N(h * 6 / 16)} ` +
           `Q ${N(w * 0.5)} ${N(h * 0.25)} ${N(w)} 0 ` +
           `L ${N(w)} ${N(h)} ` +
           `Q ${N(w * 0.5)} ${N(h * 0.75)} 0 ${N(h * 0.625)} Z`,
      },
    }),
  },
  {
    id: 'cut-corner-box', name: 'Cut-corner box', closed: true,
    natural: { w: 20, h: 20 }, defaultW: 12, defaultH: 12,
    // Closed pentagon: a rectangle whose top-left corner is replaced by one
    // straight run. The cut is `min(w, h) / 2` on both axes, so it sits at
    // exactly 45 degrees at every size — the same guarantee `gable` gives its
    // roof and `sloped-box` gives its 15 degree top — and it always fits
    // inside the box, so the whole size range stays valid. The roof and the
    // left wall keep whatever the cut leaves them, which is what separates
    // this from `sloped-box`: there the entire top edge slopes, here it stays
    // flat over the rest of the span. Default orientation cuts the top-left;
    // `flipX`, `flipY` and rotation reach the other three corners.
    geometry: (w, h) => {
      const c = Math.min(w, h) / 2;
      return {
        tag: 'path',
        attrs: { d: `M 0 ${N(c)} L ${N(c)} 0 L ${N(w)} 0 L ${N(w)} ${N(h)} L 0 ${N(h)} Z` },
      };
    },
  },
  {
    id: 'hexagon', name: 'Hexagon', closed: true,
    natural: { w: 24, h: 16 }, defaultW: 16, defaultH: 12,
    // Closed flat-top hexagon: a rectangle whose two ends are mitred to a
    // point. The mitre inset is `min(h, w) / 2`, so all four slanted edges sit
    // at exactly 45 degrees whenever `w >= h` — the same on-grid guarantee
    // `gable` gives its roof and `cut-corner-box` its corner — and the whole
    // outline stays edge-to-edge in the box. The polygon-family companion to
    // `triangle`, `square` and `diamond`: chips, badges, honeycomb cells, nuts,
    // and angular geometric bodies. At `w === h` the flats vanish and the
    // outline is the diamond spanning the box, which keeps the size range
    // valid; useful instances therefore keep `w >= h`, and `rotation: 90`
    // gives the pointy-top form with vertical sides.
    geometry: (w, h) => {
      const inset = Math.min(h / 2, w / 2);
      return {
        tag: 'path',
        attrs: {
          d: `M ${N(inset)} 0 L ${N(w - inset)} 0 L ${N(w)} ${N(h / 2)} ` +
             `L ${N(w - inset)} ${N(h)} L ${N(inset)} ${N(h)} L 0 ${N(h / 2)} Z`,
        },
      };
    },
  },
  {
    id: 'star', name: 'Star', closed: true,
    natural: { w: 20, h: 20 }, defaultW: 16, defaultH: 16,
    // Closed five-point star: the classic rating/favourite outline. Outer
    // vertices sit every 72 degrees from the apex and the inner radius is
    // cos(72)/cos(36), so each pair of edges is collinear with one pentagram
    // line. The unit star is mapped onto the box, so the apex touches the top
    // edge, the two upper arms the sides, and the two lower arms the bottom
    // edge at every size. Its edges run at 18 and 54 degrees, which is off the
    // 15 degree direction grid; an icon using it carries a documented grid
    // exception.
    geometry: (w, h) => {
      const inner = Math.cos(Math.PI * 0.4) / Math.cos(Math.PI / 5);
      const vertices = [];
      for (let step = 0; step < 10; step += 1) {
        const radius = step % 2 === 0 ? 1 : inner;
        const angle = -Math.PI / 2 + (step * Math.PI) / 5;
        vertices.push([radius * Math.cos(angle), radius * Math.sin(angle)]);
      }
      const xs = vertices.map(v => v[0]); const ys = vertices.map(v => v[1]);
      const left = Math.min(...xs); const right = Math.max(...xs);
      const top = Math.min(...ys); const bottom = Math.max(...ys);
      const points = vertices.map(([x, y]) => [
        ((x - left) * w) / (right - left),
        ((y - top) * h) / (bottom - top),
      ]);
      const runs = points.slice(1).map(([x, y]) => `L ${N(x)} ${N(y)}`).join(' ');
      return { tag: 'path', attrs: { d: `M ${N(points[0][0])} ${N(points[0][1])} ${runs} Z` } };
    },
  },
  {
    id: 'dome', name: 'Dome', closed: true,
    natural: { w: 20, h: 10 }, defaultW: 10, defaultH: 5,
    geometry: (w, h) => ({ tag: 'path', attrs: { d: `M 0 ${N(h)} A ${N(w / 2)} ${N(h)} 0 0 1 ${N(w)} ${N(h)} Z` } }),
  },
  {
    id: 'cloud', name: 'Cloud', closed: true,
    natural: { w: 24, h: 14 }, defaultW: 16, defaultH: 10,
    // Symmetric multi-lobed cloud with a straight lower chord. Quadratic
    // segments keep the atom new-grid compatible while width and height stay
    // genuinely parametric for ordinary cloud aspect ratios.
    geometry: (w, h) => ({
      tag: 'path',
      attrs: {
        d: `M 0 ${N(h * 0.65)} ` +
           `Q 0 ${N(h * 0.35)} ${N(w * 0.2)} ${N(h * 0.35)} ` +
           `Q ${N(w * 0.25)} 0 ${N(w * 0.5)} 0 ` +
           `Q ${N(w * 0.75)} 0 ${N(w * 0.8)} ${N(h * 0.35)} ` +
           `Q ${N(w)} ${N(h * 0.35)} ${N(w)} ${N(h * 0.65)} ` +
           `Q ${N(w)} ${N(h)} ${N(w * 0.82)} ${N(h)} ` +
           `L ${N(w * 0.18)} ${N(h)} ` +
           `Q 0 ${N(h)} 0 ${N(h * 0.65)} Z`,
      },
    }),
  },
  {
    id: 'scalloped-oval', name: 'Scalloped oval', closed: true,
    natural: { w: 20, h: 20 }, defaultW: 16, defaultH: 16,
    // Closed radially lobed oval: eight equal bulges around one continuous
    // contour. One quadratic per lobe, running valley to valley with its
    // control point on the crest ray; the control radius is solved from the
    // valley radius so each crest lands exactly on the box ellipse, which puts
    // the four cardinal extremes on the box edges at any aspect ratio. Valleys
    // sit on the 0.82 ellipse. No segment doubles back, so the contour never
    // closes a spurious pocket at a valley. The radially symmetric counterpart of `cloud`, which lobes only
    // its upper half over a straight lower chord: brain hemispheres, blossoms,
    // soft cogs, organic blobs. A non-square box gives the wide or tall
    // variant and `rotation` offsets the lobe rhythm.
    geometry: (w, h) => {
      const cx = w / 2, cy = h / 2, lobes = 8, valley = 0.82;
      const half = Math.PI / lobes;
      const crest = 2 - valley * Math.cos(half);
      const place = (radius, angle) => [
        N(cx + cx * radius * Math.cos(angle)),
        N(cy + cy * radius * Math.sin(angle)),
      ];
      const [sx, sy] = place(valley, half);
      const parts = [`M ${sx} ${sy}`];
      for (let lobe = 0; lobe < lobes; lobe += 1) {
        const [hx, hy] = place(crest, 2 * half * (lobe + 1));
        const [ex, ey] = place(valley, 2 * half * (lobe + 1) + half);
        parts.push(`Q ${hx} ${hy} ${ex} ${ey}`);
      }
      return { tag: 'path', attrs: { d: `${parts.join(' ')} Z` } };
    },
  },
  {
    id: 'lens', name: 'Lens', closed: true,
    natural: { w: 20, h: 12 }, defaultW: 12, defaultH: 7,
    // Closed pointed oval: two equal circular arcs meeting at cusps on the ends
    // of the horizontal axis. The tips sit at (0, h/2) and (w, h/2); the upper
    // arc touches y = 0 at mid-span and the lower arc touches y = h, so the
    // contour fills the box edge to edge. One radius serves both arcs,
    // R = (w^2 + h^2) / 4h, which is what makes the atom parametric in w and h
    // alone: h/w sets the tip angle. At h = w the radius is w/2, the arcs are
    // semicircles and the outline degenerates exactly to a circle; past h = w
    // the arcs run more than half a turn, so the large-arc flag turns on and
    // the form becomes a fat vertical oval with cusps on its sides. The whole
    // size range therefore stays valid. Doubly symmetric, so flipX and flipY
    // are no-ops; rotation places it on any allowed direction.
    geometry: (w, h) => {
      const R = (w * w + h * h) / (4 * h);
      const large = h > w ? 1 : 0;
      return {
        tag: 'path',
        attrs: {
          d: `M 0 ${N(h / 2)} A ${N(R)} ${N(R)} 0 ${large} 1 ${N(w)} ${N(h / 2)} ` +
             `A ${N(R)} ${N(R)} 0 ${large} 1 0 ${N(h / 2)} Z`,
        },
      };
    },
  },
  {
    id: 'lobed-drop', name: 'Lobed drop', closed: true,
    natural: { w: 20, h: 24 }, defaultW: 12, defaultH: 16,
    // Closed asymmetric drop with a folded lobe and inward notch. The contour
    // remains edge-to-edge and useful as a flame, leaf, petal, or flowing drop
    // over a broad range of portrait aspect ratios. Quadratics only.
    geometry: (w, h) => ({
      tag: 'path',
      attrs: {
        d: `M ${N(w * 21 / 32)} 0 ` +
           `Q ${N(w * 24 / 32)} 0 ${N(w * 27 / 32)} ${N(h * 6 / 40)} ` +
           `Q ${N(w)} ${N(h * 19 / 40)} ${N(w)} ${N(h * 28 / 40)} ` +
           `Q ${N(w)} ${N(h)} ${N(w * 0.5)} ${N(h)} ` +
           `Q 0 ${N(h)} 0 ${N(h * 28 / 40)} ` +
           `Q 0 ${N(h * 18 / 40)} ${N(w * 9 / 32)} ${N(h * 10 / 40)} ` +
           `Q ${N(w * 11 / 32)} ${N(h * 10 / 40)} ${N(w * 9 / 32)} ${N(h * 17 / 40)} ` +
           `Q ${N(w * 9 / 32)} ${N(h * 21 / 40)} ${N(w * 13 / 32)} ${N(h * 21 / 40)} ` +
           `Q ${N(w * 15 / 32)} ${N(h * 21 / 40)} ${N(w * 15 / 32)} ${N(h * 17 / 40)} ` +
           `Q ${N(w * 15 / 32)} ${N(h * 10 / 40)} ${N(w * 19 / 32)} ${N(h * 5 / 40)} ` +
           `Q ${N(w * 20 / 32)} ${N(h * 2 / 40)} ${N(w * 21 / 32)} 0 Z`,
      },
    }),
  },
  {
    id: 'stepped-cog', name: 'Stepped cog', closed: true,
    natural: { w: 20, h: 20 }, defaultW: 12, defaultH: 12,
    // Sparse orthogonal cog contour. Four broad cardinal teeth and four open
    // corner cutaways keep the silhouette mechanical without a busy rim.
    geometry: (w, h) => {
      const points = [
        [14,0],[22,0],[22,6],[30,6],[30,14],
        [36,14],[36,22],[30,22],[30,30],[22,30],
        [22,36],[14,36],[14,30],[6,30],[6,22],
        [0,22],[0,14],[6,14],[6,6],[14,6],
      ].map(([x, y]) => [N(w * x / 36), N(h * y / 36)]);
      return { tag: 'path', attrs: { d: `M ${points.map(p => p.join(' ')).join(' L ')} Z` } };
    },
  },
  {
    id: 'twin-lobed-drop', name: 'Twin-lobed drop', closed: true,
    natural: { w: 20, h: 20 }, defaultW: 12, defaultH: 12,
    // Symmetric double-lobed drop with a central cleft. One continuous
    // quadratic contour avoids doubled joints when used as a heart or crest.
    geometry: (w, h) => ({
      tag: 'path',
      attrs: {
        d: `M ${N(w / 2)} ${N(h)} ` +
           `Q 0 ${N(h * 26 / 36)} 0 ${N(h * 12 / 36)} ` +
           `Q 0 ${N(h * 2 / 36)} ${N(w * 9 / 36)} 0 ` +
           `Q ${N(w * 15 / 36)} 0 ${N(w / 2)} ${N(h * 8 / 36)} ` +
           `Q ${N(w * 21 / 36)} 0 ${N(w * 27 / 36)} 0 ` +
           `Q ${N(w)} ${N(h * 2 / 36)} ${N(w)} ${N(h * 12 / 36)} ` +
           `Q ${N(w)} ${N(h * 26 / 36)} ${N(w / 2)} ${N(h)} Z`,
      },
    }),
  },
  {
    id: 'lightning-bolt', name: 'Lightning bolt', closed: true,
    natural: { w: 20, h: 24 }, defaultW: 20, defaultH: 24,
    // Upright six-vertex bolt. In the canonical 20x24 frame its two long
    // diagonals use exact 14u and 12u square runs, so every edge sits on-grid.
    geometry: (w, h) => {
      const top = Math.min(w * 0.7, h);
      const inner = w * 0.4;
      const bottom = Math.max(0, h - (w - inner));
      return {
        tag: 'path',
        attrs: {
          d: `M ${N(w * 0.7)} 0 L 0 ${N(top)} L ${N(inner)} ${N(top)} ` +
             `L ${N(inner)} ${N(h)} L ${N(w)} ${N(bottom)} ` +
             `L ${N(w * 0.7)} ${N(bottom)} Z`,
        },
      };
    },
  },
  {
    id: 'puzzle-piece', name: 'Puzzle piece', closed: true,
    natural: { w: 20, h: 20 }, defaultW: 20, defaultH: 20,
    // Two outward tabs and two inward sockets form one reusable jigsaw
    // silhouette. Quadratics keep every lobe cubic-free and inside the box.
    geometry: (w, h) => ({
      tag: 'path',
      attrs: {
        d: `M 0 ${N(h * 0.2)} L ${N(w * 0.35)} ${N(h * 0.2)} ` +
           `Q ${N(w * 0.35)} 0 ${N(w * 0.5)} 0 Q ${N(w * 0.65)} 0 ${N(w * 0.65)} ${N(h * 0.2)} ` +
           `L ${N(w * 0.8)} ${N(h * 0.2)} L ${N(w * 0.8)} ${N(h * 0.35)} ` +
           `Q ${N(w)} ${N(h * 0.35)} ${N(w)} ${N(h * 0.5)} Q ${N(w)} ${N(h * 0.65)} ${N(w * 0.8)} ${N(h * 0.65)} ` +
           `L ${N(w * 0.8)} ${N(h)} L ${N(w * 0.65)} ${N(h)} ` +
           `Q ${N(w * 0.65)} ${N(h * 0.8)} ${N(w * 0.5)} ${N(h * 0.8)} Q ${N(w * 0.35)} ${N(h * 0.8)} ${N(w * 0.35)} ${N(h)} ` +
           `L 0 ${N(h)} L 0 ${N(h * 0.65)} ` +
           `Q ${N(w * 0.2)} ${N(h * 0.65)} ${N(w * 0.2)} ${N(h * 0.5)} Q ${N(w * 0.2)} ${N(h * 0.35)} 0 ${N(h * 0.35)} Z`,
      },
    }),
  },
  {
    id: 'phone-handset-outline', name: 'Phone handset outline', closed: true,
    natural: { w: 36, h: 36 }, defaultW: 36, defaultH: 36,
    // Closed diagonal receiver with flared earpieces. The canonical square
    // frame keeps every exposed straight run horizontal, vertical, or at 45
    // degrees; quadratic shoulders form the curved connecting body.
    geometry: (w, h) => {
      const X = value => N(w * value / 36);
      const Y = value => N(h * value / 36);
      return {
        tag: 'path',
        attrs: {
          d: `M ${X(6)} 0 L ${X(12)} 0 Q ${X(14)} 0 ${X(15)} ${Y(2)} ` +
             `L ${X(20)} ${Y(7)} Q ${X(21)} ${Y(8)} ${X(20)} ${Y(9)} ` +
             `L ${X(17)} ${Y(12)} Q ${X(15)} ${Y(14)} ${X(17)} ${Y(15)} ` +
             `L ${X(21)} ${Y(19)} Q ${X(23)} ${Y(21)} ${X(24)} ${Y(19)} ` +
             `L ${X(27)} ${Y(16)} Q ${X(29)} ${Y(14)} ${X(30)} ${Y(16)} ` +
             `L ${X(35)} ${Y(21)} Q ${X(36)} ${Y(23)} ${X(36)} ${Y(24)} ` +
             `L ${X(36)} ${Y(30)} Q ${X(36)} ${Y(33)} ${X(33)} ${Y(36)} ` +
             `Q ${X(29)} ${Y(36)} ${X(25)} ${Y(34)} ` +
             `Q ${X(12)} ${Y(30)} ${X(2)} ${Y(20)} Q 0 ${Y(17)} 0 ${Y(14)} ` +
             `L 0 ${Y(9)} Q 0 ${Y(7)} ${X(2)} ${Y(6)} ` +
             `L ${X(5)} ${Y(3)} Q ${X(6)} ${Y(2)} ${X(6)} 0 Z`,
        },
      };
    },
  },
  {
    id: 'quarter-circle', name: 'Quarter circle', closed: true,
    natural: { w: 20, h: 20 }, defaultW: 8, defaultH: 8,
    geometry: (w, h) => ({ tag: 'path', attrs: { d: `M 0 ${N(h)} L 0 0 A ${N(w)} ${N(h)} 0 0 1 ${N(w)} ${N(h)} Z` } }),
  },
  {
    id: 'ring', name: 'Ring', closed: true,
    natural: { w: 20, h: 20 }, defaultW: 8, defaultH: 8,
    geometry: (w, h) => {
      const cx = w / 2, cy = h / 2;
      const rx = w / 2, ry = h / 2;
      const irx = rx * 0.6, iry = ry * 0.6;
      return {
        tag: 'path',
        attrs: {
          d: `M ${N(cx)} 0 A ${N(rx)} ${N(ry)} 0 1 0 ${N(cx)} ${N(h)} A ${N(rx)} ${N(ry)} 0 1 0 ${N(cx)} 0 Z ` +
             `M ${N(cx)} ${N(cy - iry)} A ${N(irx)} ${N(iry)} 0 1 0 ${N(cx)} ${N(cy + iry)} ` +
             `A ${N(irx)} ${N(iry)} 0 1 0 ${N(cx)} ${N(cy - iry)} Z`,
          'fill-rule': 'evenodd',
        },
      };
    },
  },

  // ---- Open paths (lines & curves) -----------------------------------
  {
    id: 'dot', name: 'Dot', closed: false,
    natural: { w: 4, h: 4 }, defaultW: 4, defaultH: 4,
    // A true point-line dot. The renderer's round line cap supplies the
    // visible disc, so its diameter always matches the selected stroke width.
    geometry: (w, h) => ({
      tag: 'path', attrs: { d: `M ${N(w / 2)} ${N(h / 2)} L ${N(w / 2)} ${N(h / 2)}` },
    }),
  },
  {
    id: 'line', name: 'Line', closed: false,
    natural: { w: 20, h: 2 }, defaultW: 8, defaultH: 1,
    geometry: (w, h) => ({ tag: 'path', attrs: { d: `M 0 ${N(h / 2)} L ${N(w)} ${N(h / 2)}` } }),
  },
  {
    id: 'diagonal-line', name: 'Diagonal line', closed: false,
    natural: { w: 20, h: 20 }, defaultW: 8, defaultH: 8,
    geometry: (w, h) => ({ tag: 'path', attrs: { d: `M 0 ${N(h)} L ${N(w)} 0` } }),
  },
  {
    id: 'curve', name: 'Curve', closed: false,
    natural: { w: 20, h: 12 }, defaultW: 10, defaultH: 6,
    // Quadratic arch: endpoints at the bottom corners, peak touching the top.
    geometry: (w, h) => ({ tag: 'path', attrs: { d: `M 0 ${N(h)} Q ${N(w / 2)} ${N(-h)} ${N(w)} ${N(h)}` } }),
  },
  {
    id: 's-curve', name: 'S-curve', closed: false,
    natural: { w: 20, h: 20 }, defaultW: 8, defaultH: 8,
    geometry: (w, h) => ({
      tag: 'path',
      attrs: { d: `M 0 ${N(h)} C ${N(w / 2)} ${N(h)} ${N(w / 2)} 0 ${N(w)} 0` },
    }),
  },
  {
    id: 's-bend', name: 'S-bend', closed: false,
    natural: { w: 20, h: 20 }, defaultW: 12, defaultH: 12,
    // Two opposite-sweep quarter ellipses meet tangentially at box center.
    // The default contour runs top-left to bottom-right; rigid flips and
    // rotations provide the other S-bend orientations.
    geometry: (w, h) => ({
      tag: 'path',
      attrs: {
        d: `M 0 0 A ${N(w / 2)} ${N(h / 2)} 0 0 1 ${N(w / 2)} ${N(h / 2)} ` +
           `A ${N(w / 2)} ${N(h / 2)} 0 0 0 ${N(w)} ${N(h)}`,
      },
    }),
  },
  {
    id: 'arc', name: 'Arc', closed: false,
    natural: { w: 20, h: 10 }, defaultW: 10, defaultH: 5,
    geometry: (w, h) => ({ tag: 'path', attrs: { d: `M 0 ${N(h)} A ${N(w / 2)} ${N(h)} 0 0 1 ${N(w)} ${N(h)}` } }),
  },
  {
    id: 'quarter-arc', name: 'Quarter arc', closed: false,
    natural: { w: 20, h: 20 }, defaultW: 8, defaultH: 8,
    // Open contour: one quarter of an ellipse spanning the box. It leaves the
    // top-left corner tangent to the top edge and arrives at the bottom-right
    // corner tangent to the right edge, curving around a centre at the
    // bottom-left. This is the open counterpart of `quarter-circle`; `flipX`,
    // `flipY`, and rotation reach the other three corner orientations.
    geometry: (w, h) => ({ tag: 'path', attrs: { d: `M 0 0 A ${N(w)} ${N(h)} 0 0 1 ${N(w)} ${N(h)}` } }),
  },
  {
    id: 'bulb-outline', name: 'Bulb outline', closed: false,
    natural: { w: 24, h: 32 }, defaultW: 12, defaultH: 16,
    // Open symmetric globe contour. It reaches the top and side extrema,
    // then tapers to two neck endpoints one third and two thirds across the
    // bottom edge so a separate socket can attach without hidden geometry.
    geometry: (w, h) => ({
      tag: 'path', attrs: {
        d: `M ${N(w / 3)} ${N(h)} ` +
           `Q ${N(w / 3)} ${N(3 * h / 4)} ${N(w / 6)} ${N(5 * h / 8)} ` +
           `Q 0 ${N(h / 2)} 0 ${N(3 * h / 8)} ` +
           `Q 0 0 ${N(w / 2)} 0 ` +
           `Q ${N(w)} 0 ${N(w)} ${N(3 * h / 8)} ` +
           `Q ${N(w)} ${N(h / 2)} ${N(5 * w / 6)} ${N(5 * h / 8)} ` +
           `Q ${N(2 * w / 3)} ${N(3 * h / 4)} ${N(2 * w / 3)} ${N(h)}`,
      },
    }),
  },
  {
    id: 'open-rectangle', name: 'Open rectangle', closed: false,
    natural: { w: 20, h: 20 }, defaultW: 8, defaultH: 10,
    // Open contour: three sides of a rectangle, the fourth absent. The default
    // orientation opens downward, matching `arch` and `gable`, so the contour
    // runs up the left side, across the flat head, and down the right side.
    // This is the flat-headed counterpart of the round-headed `arch` and the
    // open counterpart of `rectangle`; `flipY` turns it over and `rotation`
    // gives a side-opening channel.
    geometry: (w, h) => ({ tag: 'path', attrs: { d: `M 0 ${N(h)} L 0 0 L ${N(w)} 0 L ${N(w)} ${N(h)}` } }),
  },
  {
    id: 'arch', name: 'Arch', closed: false,
    natural: { w: 20, h: 20 }, defaultW: 10, defaultH: 12,
    // Open contour: an elliptical head on two straight jambs, opening downward.
    // The head is rx = w/2, ry = min(w/2, h) — semicircular whenever the box is
    // at least half as tall as it is wide — and the jambs run from the springing
    // line to the bottom edge. When h <= w/2 the jambs vanish and only the head
    // remains, which keeps the atom valid across its whole size range.
    geometry: (w, h) => {
      const ry = Math.min(w / 2, h);
      const head = `A ${N(w / 2)} ${N(ry)} 0 0 1 ${N(w)} ${N(ry)}`;
      const d = h - ry > 0
        ? `M 0 ${N(h)} L 0 ${N(ry)} ${head} L ${N(w)} ${N(h)}`
        : `M 0 ${N(ry)} ${head}`;
      return { tag: 'path', attrs: { d } };
    },
  },
  {
    id: 'hook', name: 'Hook', closed: false,
    natural: { w: 8, h: 16 }, defaultW: 8, defaultH: 14,
    // Open J-hook: a long stem enters a semicircular bowl and returns through
    // one short tip. Portrait instances with h >= w preserve the full contour;
    // flips place the attachment stem on either side.
    geometry: (w, h) => {
      const r = w / 2;
      const bowlY = Math.max(r, h - r);
      const tipY = Math.max(0, bowlY - r);
      return {
        tag: 'path',
        attrs: { d: `M 0 0 L 0 ${N(bowlY)} A ${N(r)} ${N(r)} 0 0 0 ${N(w)} ${N(bowlY)} L ${N(w)} ${N(tipY)}` },
      };
    },
  },
  {
    id: 'faucet', name: 'Faucet', closed: false,
    natural: { w: 24, h: 20 }, defaultW: 20, defaultH: 16,
    geometry: (w, h) => ({
      tag: 'path', attrs: {
        d: `M 0 ${N(h * 0.5)} L ${N(w * 0.75)} ${N(h * 0.5)} ` +
           `A ${N(w * 0.25)} ${N(h * 0.25)} 0 0 1 ${N(w)} ${N(h * 0.75)} L ${N(w)} ${N(h)} ` +
           `M ${N(w * 0.35)} ${N(h * 0.5)} L ${N(w * 0.35)} 0 ` +
           `M ${N(w * 0.2)} 0 L ${N(w * 0.5)} 0`,
      },
    }),
  },
  {
    id: 'open-end-wrench', name: 'Open-end wrench', closed: false,
    natural: { w: 24, h: 8 }, defaultW: 20, defaultH: 8,
    geometry: (w, h) => {
      const r = h / 2;
      const neck = w - r;
      return {
        tag: 'path', attrs: {
          d: `M ${N(r)} 0 A ${N(r)} ${N(r)} 0 1 1 ${N(r)} ${N(h)} A ${N(r)} ${N(r)} 0 1 1 ${N(r)} 0 ` +
             `M ${N(h)} ${N(r)} L ${N(neck)} ${N(r)} M ${N(neck)} ${N(r)} L ${N(w)} 0 ` +
             `M ${N(neck)} ${N(r)} L ${N(w)} ${N(h)}`,
        },
      };
    },
  },
  {
    id: 'open-gable', name: 'Open gable', closed: false,
    natural: { w: 20, h: 20 }, defaultW: 12, defaultH: 14,
    // Open contour: a peaked head on two straight walls, opening downward. The
    // head rise is min(w/2, h) — so both roof edges sit at exactly 45 degrees
    // whenever the box is at least half as tall as it is wide — and the walls
    // run from the springing line to the bottom edge. This
    // is `gable` with its base absent — the pointed-head counterpart of the
    // round-headed `arch` and the flat-headed `open-rectangle`, and the open
    // counterpart of `gable`. Use it wherever the bottom edge is drawn
    // separately or interrupted, such as a shell whose ground line is broken by
    // a doorway. When h <= w/2 the walls vanish and only the peak remains,
    // which keeps the atom valid across its whole size range. `flipY` turns it
    // over and `rotation` gives a side-opening channel.
    geometry: (w, h) => {
      const r = Math.min(w / 2, h);
      const head = `L ${N(w / 2)} 0 L ${N(w)} ${N(r)}`;
      const d = h - r > 0
        ? `M 0 ${N(h)} L 0 ${N(r)} ${head} L ${N(w)} ${N(h)}`
        : `M 0 ${N(r)} ${head}`;
      return { tag: 'path', attrs: { d } };
    },
  },
  {
    id: 'head-profile', name: 'Head profile', closed: false,
    natural: { w: 24, h: 32 }, defaultW: 18, defaultH: 24,
    // Open human head seen in profile, facing right, drawn as one continuous
    // contour: up the back of the neck, up the back of the skull, over the crown,
    // down the forehead, out to the nose, in at the lip, out at the chin, then
    // down the front of the neck. The contour touches all four box edges — the
    // back of the skull on the left, the crown on top, the nose tip on the
    // right, both neck ends on the bottom — and the bottom stays open between
    // them so a shoulder, collar, or frame can be drawn separately. Built from
    // quadratics only, so the atom never emits a straight segment and can
    // never leave the 15 degree angle grid at any size. `flipX` faces it left.
    geometry: (w, h) => ({
      tag: 'path',
      attrs: {
        d: `M ${N(w * 0.10)} ${N(h)} ` +
           `Q ${N(w * 0.10)} ${N(h * 0.80)} ${N(w * 0.04)} ${N(h * 0.66)} ` +
           `Q 0 ${N(h * 0.52)} 0 ${N(h * 0.40)} ` +
           `Q 0 0 ${N(w * 0.44)} 0 ` +
           `Q ${N(w * 0.80)} 0 ${N(w * 0.82)} ${N(h * 0.28)} ` +
           `Q ${N(w * 0.84)} ${N(h * 0.38)} ${N(w)} ${N(h * 0.50)} ` +
           `Q ${N(w * 0.90)} ${N(h * 0.56)} ${N(w * 0.84)} ${N(h * 0.60)} ` +
           `Q ${N(w * 0.78)} ${N(h * 0.66)} ${N(w * 0.70)} ${N(h * 0.76)} ` +
           `Q ${N(w * 0.68)} ${N(h * 0.88)} ${N(w * 0.68)} ${N(h)}`,
      },
    }),
  },
  {
    id: 'worker-profile', name: 'Worker profile', closed: false,
    natural: { w: 20, h: 40 }, defaultW: 18, defaultH: 40,
    // Reusable side-view worker: separate circular head plus one open walking
    // contour for torso, arm, and legs. Quadratics keep the pose cubic-free and
    // adaptable across tall portrait proportions.
    geometry: (w, h) => {
      const r = Math.min(w * 0.20, h * 0.09);
      const cx = w * 0.45;
      return { tag: 'path', attrs: { d:
        `M ${N(cx)} 0 A ${N(r)} ${N(r)} 0 1 1 ${N(cx)} ${N(2 * r)} ` +
        `A ${N(r)} ${N(r)} 0 1 1 ${N(cx)} 0 Z ` +
        `M ${N(cx)} ${N(2 * r)} ` +
        `Q ${N(w * 0.20)} ${N(h * 0.32)} ${N(w * 0.38)} ${N(h * 0.52)} ` +
        `Q ${N(w * 0.52)} ${N(h * 0.68)} 0 ${N(h)} ` +
        `M ${N(w * 0.38)} ${N(h * 0.52)} Q ${N(w * 0.62)} ${N(h * 0.58)} ${N(w)} ${N(h * 0.70)} ` +
        `M ${N(w * 0.38)} ${N(h * 0.52)} Q ${N(w * 0.58)} ${N(h * 0.72)} ${N(w * 0.68)} ${N(h)}` } };
    },
  },
  {
    id: 'worker-profile-solid', name: 'Worker profile solid', closed: false,
    natural: { w: 12, h: 24 }, defaultW: 12, defaultH: 24,
    // Compact sibling of worker-profile. Its body uses the identical
    // proportional quadratic contours, while one zero-length point at the
    // outlined head's centre lets round-cap paint make a solid 4u head with
    // no enclosed hole.
    geometry: (w, h) => {
      const r = Math.min(w * 0.18, h * 0.08);
      const cx = w * 0.45;
      const cy = r;
      return { tag: 'path', attrs: { d:
        `M ${N(cx)} ${N(cy)} L ${N(cx)} ${N(cy)} ` +
        `M ${N(cx)} ${N(2 * r)} ` +
        `Q ${N(w * 0.20)} ${N(h * 0.32)} ${N(w * 0.38)} ${N(h * 0.52)} ` +
        `Q ${N(w * 0.52)} ${N(h * 0.68)} 0 ${N(h)} ` +
        `M ${N(w * 0.38)} ${N(h * 0.52)} Q ${N(w * 0.62)} ${N(h * 0.58)} ${N(w)} ${N(h * 0.70)} ` +
        `M ${N(w * 0.38)} ${N(h * 0.52)} Q ${N(w * 0.58)} ${N(h * 0.72)} ${N(w * 0.68)} ${N(h)}` } };
    },
  },
  {
    id: 'pig-outline', name: 'Pig outline', closed: true,
    natural: { w: 40, h: 22 }, defaultW: 40, defaultH: 22,
    // Closed side-view pig body with a raised ear, blunt snout, belly, and two
    // feet. The contour carries no bank slot or damage cue, so those remain
    // composable semantic details.
    geometry: (w, h) => ({ tag: 'path', attrs: { d:
      `M 0 ${N(h * 0.50)} ` +
      `Q ${N(w * 0.08)} ${N(h * 0.12)} ${N(w * 0.38)} ${N(h * 0.12)} ` +
      `Q ${N(w * 0.44)} 0 ${N(w * 0.54)} 0 ` +
      `Q ${N(w * 0.62)} ${N(h * 0.12)} ${N(w * 0.70)} ${N(h * 0.14)} ` +
      `Q ${N(w * 0.90)} ${N(h * 0.14)} ${N(w)} ${N(h * 0.40)} ` +
      `Q ${N(w)} ${N(h * 0.65)} ${N(w * 0.84)} ${N(h * 0.70)} ` +
      `Q ${N(w * 0.82)} ${N(h * 0.90)} ${N(w * 0.72)} ${N(h)} ` +
      `Q ${N(w * 0.60)} ${N(h)} ${N(w * 0.58)} ${N(h * 0.76)} ` +
      `Q ${N(w * 0.40)} ${N(h * 0.80)} ${N(w * 0.30)} ${N(h * 0.76)} ` +
      `Q ${N(w * 0.28)} ${N(h)} ${N(w * 0.16)} ${N(h)} ` +
      `Q ${N(w * 0.04)} ${N(h * 0.86)} 0 ${N(h * 0.50)} Z` } }),
  },
  {
    id: 'broken-pig-outline', name: 'Broken pig outline', closed: true,
    natural: { w: 40, h: 22 }, defaultW: 40, defaultH: 22,
    // Two independently closed pig halves separated by matching zigzag crack
    // edges. The canonical 40x22 frame scales proportionally into the box;
    // at its natural aspect ratio every crack run is exactly 45 degrees.
    geometry: (w, h) => {
      const X = value => N(w * value / 40);
      const Y = value => N(h * value / 22);
      return { tag: 'path', attrs: { d:
        `M ${X(17)} ${Y(4)} ` +
        `Q ${X(16)} ${Y(0)} ${X(12)} ${Y(0)} ` +
        `Q ${X(8)} ${Y(2)} ${X(4)} ${Y(4)} ` +
        `Q ${X(0)} ${Y(6)} ${X(0)} ${Y(11)} ` +
        `Q ${X(0)} ${Y(16)} ${X(4)} ${Y(17)} ` +
        `Q ${X(4)} ${Y(21)} ${X(8)} ${Y(22)} ` +
        `Q ${X(12)} ${Y(22)} ${X(12)} ${Y(18)} ` +
        `Q ${X(15)} ${Y(20)} ${X(17)} ${Y(20)} ` +
        `L ${X(13)} ${Y(16)} L ${X(17)} ${Y(12)} L ${X(13)} ${Y(8)} L ${X(17)} ${Y(4)} Z ` +
        `M ${X(27)} ${Y(4)} ` +
        `Q ${X(30)} ${Y(2)} ${X(34)} ${Y(4)} ` +
        `Q ${X(40)} ${Y(4)} ${X(40)} ${Y(10)} ` +
        `Q ${X(40)} ${Y(14)} ${X(35)} ${Y(15)} ` +
        `Q ${X(34)} ${Y(20)} ${X(30)} ${Y(22)} ` +
        `Q ${X(26)} ${Y(22)} ${X(26)} ${Y(18)} ` +
        `Q ${X(26)} ${Y(20)} ${X(27)} ${Y(20)} ` +
        `L ${X(23)} ${Y(16)} L ${X(27)} ${Y(12)} L ${X(23)} ${Y(8)} L ${X(27)} ${Y(4)} Z` },
      };
    },
  },
  {
    id: 'holding-hand', name: 'Holding hand', closed: false,
    natural: { w: 24, h: 24 }, defaultW: 24, defaultH: 24,
    // Side-view gripping hand with two broad finger lobes and an open wrist.
    // Quadratics and elliptical arcs keep the contour reusable and cubic-free.
    geometry: (w, h) => ({
      tag: 'path',
      attrs: {
        d: `M 0 ${N(h * 14 / 24)} ` +
           `Q ${N(w * 4 / 24)} 0 ${N(w * 14 / 24)} 0 ` +
           `L ${N(w * 20 / 24)} 0 ` +
           `A ${N(w * 4 / 24)} ${N(h * 4 / 24)} 0 0 1 ${N(w * 20 / 24)} ${N(h * 8 / 24)} ` +
           `L ${N(w * 16 / 24)} ${N(h * 8 / 24)} ` +
           `A ${N(w * 4 / 24)} ${N(h * 4 / 24)} 0 0 0 ${N(w * 16 / 24)} ${N(h * 16 / 24)} ` +
           `L ${N(w * 20 / 24)} ${N(h * 16 / 24)} ` +
           `A ${N(w * 4 / 24)} ${N(h * 4 / 24)} 0 0 1 ${N(w * 20 / 24)} ${N(h)} ` +
           `L ${N(w * 14 / 24)} ${N(h)} ` +
           `Q ${N(w * 10 / 24)} ${N(h)} ${N(w * 8 / 24)} ${N(h * 20 / 24)} ` +
           `L 0 ${N(h * 20 / 24)}`,
      },
    }),
  },
  {
    id: 'bottle-outline', name: 'Bottle outline', closed: true,
    natural: { w: 14, h: 20 }, defaultW: 14, defaultH: 20,
    // Broad 8u neck, exact 45-degree shoulders, and ordinary 4u circular
    // lower corners at the canonical 14x20 size.
    geometry: (w, h) => {
      const neck = Math.min(8, w - 4);
      const shoulder = (w - neck) / 2;
      const neckHeight = Math.min(4, Math.max(0, h - 12));
      const shoulderBottom = neckHeight + shoulder;
      const radius = Math.min(4, w / 2, Math.max(0, (h - shoulderBottom) / 2));
      return { tag: 'path', attrs: { d:
        `M ${N(shoulder)} 0 L ${N(w - shoulder)} 0 ` +
        `L ${N(w - shoulder)} ${N(neckHeight)} ` +
        `L ${N(w)} ${N(shoulderBottom)} L ${N(w)} ${N(h - radius)} ` +
        `A ${N(radius)} ${N(radius)} 0 0 1 ${N(w - radius)} ${N(h)} ` +
        `L ${N(radius)} ${N(h)} ` +
        `A ${N(radius)} ${N(radius)} 0 0 1 0 ${N(h - radius)} ` +
        `L 0 ${N(shoulderBottom)} L ${N(shoulder)} ${N(neckHeight)} Z` } };
    },
  },
  {
    id: 'transfer-hand', name: 'Transfer hand', closed: false,
    natural: { w: 20, h: 12 }, defaultW: 20, defaultH: 12,
    // Compact open wrist, thumb rise, and broad fingertip for small transfer
    // gestures. Canonical exposed diagonals sit on the 45-degree grid.
    geometry: (w, h) => ({ tag: 'path', attrs: { d:
      `M 0 0 L ${N(w * 0.2)} 0 ` +
      `Q ${N(w * 0.3)} 0 ${N(w * 0.4)} ${N(h * 0.25)} ` +
      `L ${N(w * 0.55)} ${N(h * 0.5)} L ${N(w * 0.9)} ${N(h * 0.5)} ` +
      `Q ${N(w)} ${N(h * 0.5)} ${N(w)} ${N(h * 2 / 3)} ` +
      `Q ${N(w)} ${N(h * 5 / 6)} ${N(w * 0.9)} ${N(h * 5 / 6)} ` +
      `L ${N(w * 0.6)} ${N(h * 5 / 6)} ` +
      `Q ${N(w * 0.45)} ${N(h)} ${N(w * 0.3)} ${N(h)} L 0 ${N(h * 0.5)}` } }),
  },
  {
    id: 'radial-ticks', name: 'Radial ticks', closed: false,
    natural: { w: 20, h: 20 }, defaultW: 12, defaultH: 12,
    // Twelve evenly spaced radial ticks running from the 0.8 inner ellipse out
    // to the box edges, emitted as twelve open subpaths. Every tick sits on a
    // 30-degree ray, so the whole ring stays on the 15-degree grid at any size,
    // and the inner endpoints land exactly on the 0.8 ellipse so a separate
    // `circle` rim drawn in that box meets them without doubled paint. Reusable
    // wherever a rim carries repeated radial marks — cog and gear teeth, dial
    // and gauge ticks, compass rose, sun rays, spinner segments. Rotation
    // offsets the whole ring; a non-square box gives the elliptical variant.
    // Endpoints keep four decimals rather than the usual three: a tick is only
    // 0.2 of the box radius long, so at small sizes three-decimal rounding can
    // swing a 30-degree ray past the 0.01-degree straight-angle tolerance.
    geometry: (w, h) => {
      const R = v => +v.toFixed(4);
      const cx = w / 2, cy = h / 2, inner = 0.8;
      const d = Array.from({ length: 12 }, (_, step) => {
        const angle = step * Math.PI / 6;
        const cos = Math.cos(angle), sin = Math.sin(angle);
        return `M ${R(cx + inner * cx * cos)} ${R(cy + inner * cy * sin)} ` +
               `L ${R(cx + cx * cos)} ${R(cy + cy * sin)}`;
      }).join(' ');
      return { tag: 'path', attrs: { d } };
    },
  },
  {
    id: 'open-twin-gable', name: 'Open twin gable', closed: false,
    natural: { w: 40, h: 32 }, defaultW: 16, defaultH: 12,
    // `twin-gable` with its base removed — the two-peak counterpart of
    // `open-gable`, and the open counterpart of `twin-gable`. The rise is
    // min(w/4, h), so all four flanks sit at exactly 45 degrees and the whole
    // contour stays on the 15-degree grid at any size; when the box is taller
    // than that rise the two end stems drop to the bottom edge so the box is
    // still filled edge to edge. Use it wherever a repeated peaked edge is a
    // contour rather than a silhouette: a cracked shell or broken edge, a comb
    // or crest, a frill, a sawtooth or signal trace. `flipY` turns the peaks
    // into notches and `rotation` gives a vertical serration.
    geometry: (w, h) => {
      const rise = Math.min(w / 4, h);
      const peaks = `L ${N(w / 4)} 0 L ${N(w / 2)} ${N(rise)} L ${N(3 * w / 4)} 0 L ${N(w)} ${N(rise)}`;
      const d = h - rise > 0
        ? `M 0 ${N(h)} L 0 ${N(rise)} ${peaks} L ${N(w)} ${N(h)}`
        : `M 0 ${N(rise)} ${peaks}`;
      return { tag: 'path', attrs: { d } };
    },
  },
  {
    id: 'spiral', name: 'Spiral', closed: false,
    natural: { w: 22, h: 20 }, defaultW: 16, defaultH: 14,
    // One open contour that winds inward: five 90-degree arcs, each radius
    // 0.86 of the one before, with every centre placed on the shared normal at
    // the junction so the contour is tangent-continuous rather than a chain of
    // separate arcs. Every junction lands on a multiple of 90 degrees, so each
    // arc's extremes are its own endpoints and the contour fills its box
    // exactly. A non-square box gives the elliptical variant; rotation and the
    // flips choose where the mouth opens. The turn count and ratio are set so
    // adjacent turns stay far enough apart to read at ship size. Use it for
    // shells, snails, ferns, volutes, whirls, and spinners.
    geometry: (w, h) => {
      const ratio = 0.86, quarters = 5;
      const radii = Array.from({ length: quarters }, (_, step) => ratio ** step);
      const points = [[radii[0], 0]];
      let centre = [0, 0];
      radii.forEach((radius, step) => {
        const start = step * Math.PI / 2;
        if (step) centre = [points[step][0] - radius * Math.cos(start), points[step][1] - radius * Math.sin(start)];
        const end = start + Math.PI / 2;
        points.push([centre[0] + radius * Math.cos(end), centre[1] + radius * Math.sin(end)]);
      });
      const xs = points.map(point => point[0]), ys = points.map(point => point[1]);
      const left = Math.min(...xs), top = Math.min(...ys);
      const sx = w / (Math.max(...xs) - left), sy = h / (Math.max(...ys) - top);
      const place = point => `${N((point[0] - left) * sx)} ${N((point[1] - top) * sy)}`;
      const d = [`M ${place(points[0])}`, ...radii.map((radius, step) =>
        `A ${N(radius * sx)} ${N(radius * sy)} 0 0 1 ${place(points[step + 1])}`)].join(' ');
      return { tag: 'path', attrs: { d } };
    },
  },
  {
    id: 'gapped-rounded-rectangle', name: 'Gapped rounded rectangle', closed: false,
    natural: { w: 24, h: 32 }, defaultW: 16, defaultH: 20,
    // The closed `rounded-rectangle` broken in the middle of its head: one open
    // contour running clockwise from the gap's right lip, around all four
    // ordinary 4u corners, and back to the gap's left lip. The gap is exactly
    // half the box width, so the two head runs stay equal and the opening stays
    // centred at every size, and the corner radius clamps to the head run and
    // half-height so those runs can never invert. Use it wherever a frame is
    // interrupted by a part that seats in the break rather than crossing it —
    // a clipboard clip, a tab or handle, a labelled panel, a gated enclosure —
    // instead of drawing the frame and then hiding the crossing. `flipY` moves
    // the gap to the foot and `rotation` puts it on either side.
    geometry: (w, h) => {
      const gap = w * 0.5;
      const left = (w - gap) / 2, right = (w + gap) / 2;
      const r = Math.min(4, left, h / 2);
      return { tag: 'path', attrs: { d:
        `M ${N(right)} 0 L ${N(w - r)} 0 ` +
        `A ${N(r)} ${N(r)} 0 0 1 ${N(w)} ${N(r)} L ${N(w)} ${N(h - r)} ` +
        `A ${N(r)} ${N(r)} 0 0 1 ${N(w - r)} ${N(h)} L ${N(r)} ${N(h)} ` +
        `A ${N(r)} ${N(r)} 0 0 1 0 ${N(h - r)} L 0 ${N(r)} ` +
        `A ${N(r)} ${N(r)} 0 0 1 ${N(r)} 0 L ${N(left)} 0` } };
    },
  },
  {
    id: 'corner-gapped-rounded-rectangle', name: 'Corner-gapped rounded rectangle', closed: false,
    natural: { w: 28, h: 20 }, defaultW: 28, defaultH: 20,
    // Rounded frame with its lower-left corner deliberately removed so a
    // foreground object can cross the frame without doubled hidden geometry.
    geometry: (w, h) => {
      const radius = Math.min(4, w / 2, h / 2);
      const bottomLip = w * 0.75;
      return {
        tag: 'path',
        attrs: {
          d: `M 0 ${N(radius)} ` +
             `A ${N(radius)} ${N(radius)} 0 0 1 ${N(radius)} 0 L ${N(w - radius)} 0 ` +
             `A ${N(radius)} ${N(radius)} 0 0 1 ${N(w)} ${N(radius)} L ${N(w)} ${N(h - radius)} ` +
             `A ${N(radius)} ${N(radius)} 0 0 1 ${N(w - radius)} ${N(h)} L ${N(bottomLip)} ${N(h)}`,
        },
      };
    },
  },
  {
    id: 'open-shell', name: 'Open shell', closed: false,
    natural: { w: 40, h: 32 }, defaultW: 32, defaultH: 24,
    geometry: (w, h) => ({
      tag: 'path', attrs: { d:
        `M 0 ${N(h / 2)} Q ${N(w * 0.3)} 0 ${N(w * 0.8)} 0 Q ${N(w)} 0 ${N(w)} ${N(h * 0.25)} ` +
        `M 0 ${N(h / 2)} Q ${N(w * 0.3)} ${N(h)} ${N(w * 0.75)} ${N(h)} Q ${N(w)} ${N(h)} ${N(w)} ${N(h * 0.75)}` },
    }),
  },
  {
    id: 'oyster-shell', name: 'Oyster shell', closed: false,
    natural: { w: 40, h: 32 }, defaultW: 40, defaultH: 32,
    geometry: (w, h) => ({
      tag: 'path', attrs: { d:
        `M ${N(w * 0.53)} ${N(h * 0.38)} ` +
        `Q ${N(w * 0.82)} ${N(h * 0.28)} ${N(w * 0.98)} ${N(h * 0.08)} ` +
        `Q ${N(w)} 0 ${N(w * 0.83)} 0 ` +
        `Q ${N(w * 0.43)} 0 ${N(w * 0.16)} ${N(h * 0.25)} ` +
        `Q 0 ${N(h * 0.42)} 0 ${N(h * 0.55)} ` +
        `Q ${N(w * 0.03)} ${N(h * 0.78)} ${N(w * 0.27)} ${N(h * 0.94)} ` +
        `Q ${N(w * 0.58)} ${N(h * 1.0648)} ${N(w * 0.85)} ${N(h * 0.93)} ` +
        `Q ${N(w)} ${N(h * 0.86)} ${N(w)} ${N(h * 0.73)} ` +
        `Q ${N(w)} ${N(h * 0.63)} ${N(w * 0.85)} ${N(h * 0.60)} ` +
        `Q ${N(w * 0.75)} ${N(h * 0.58)} ${N(w * 0.67)} ${N(h * 0.55)}` },
    }),
  },
  {
    id: 'side-gapped-rounded-rectangle', name: 'Side-gapped rounded rectangle', closed: false,
    natural: { w: 20, h: 32 }, defaultW: 18, defaultH: 32,
    geometry: (w, h) => {
      const radius = Math.min(4, w / 2, h / 2);
      const gapTop = h * 0.375;
      const gapBottom = h * 0.625;
      return { tag: 'path', attrs: { d:
        `M 0 ${N(gapBottom)} L 0 ${N(h - radius)} ` +
        `A ${N(radius)} ${N(radius)} 0 0 0 ${N(radius)} ${N(h)} L ${N(w - radius)} ${N(h)} ` +
        `A ${N(radius)} ${N(radius)} 0 0 0 ${N(w)} ${N(h - radius)} L ${N(w)} ${N(radius)} ` +
        `A ${N(radius)} ${N(radius)} 0 0 0 ${N(w - radius)} 0 L ${N(radius)} 0 ` +
        `A ${N(radius)} ${N(radius)} 0 0 0 0 ${N(radius)} L 0 ${N(gapTop)}` } };
    },
  },
  {
    id: 'shark-fin', name: 'Shark fin', closed: false,
    natural: { w: 20, h: 24 }, defaultW: 20, defaultH: 24,
    geometry: (w, h) => ({ tag: 'path', attrs: { d:
      `M 0 ${N(h)} Q ${N(w / 4)} ${N(h * 3 / 8)} ${N(w)} 0 ` +
      `Q ${N(w * 4 / 5)} ${N(h / 2)} ${N(w * 4 / 5)} ${N(h)}` },
    }),
  },
  {
    id: 'wave-line', name: 'Wave line', closed: false,
    natural: { w: 40, h: 8 }, defaultW: 32, defaultH: 8,
    geometry: (w, h) => {
      const mid = h / 2;
      return { tag: 'path', attrs: { d:
        `M 0 ${N(mid)} Q ${N(w / 8)} ${N(-h / 2)} ${N(w / 4)} ${N(mid)} ` +
        `Q ${N(3 * w / 8)} ${N(3 * h / 2)} ${N(w / 2)} ${N(mid)} ` +
        `Q ${N(5 * w / 8)} ${N(-h / 2)} ${N(3 * w / 4)} ${N(mid)} ` +
        `Q ${N(7 * w / 8)} ${N(3 * h / 2)} ${N(w)} ${N(mid)}` } };
    },
  },
  {
    id: 'gripping-hand', name: 'Gripping hand', closed: false,
    natural: { w: 24, h: 20 }, defaultW: 24, defaultH: 20,
    geometry: (w, h) => ({ tag: 'path', attrs: { d:
      `M ${N(w / 2)} 0 Q ${N(w / 3)} 0 ${N(w / 6)} ${N(h / 5)} L 0 ${N(2 * h / 5)} ` +
      `Q 0 ${N(3 * h / 5)} ${N(w / 12)} ${N(4 * h / 5)} Q ${N(5 * w / 24)} ${N(h)} ${N(w / 3)} ${N(h)} ` +
      `Q ${N(w / 2)} ${N(h)} ${N(7 * w / 12)} ${N(4 * h / 5)} L ${N(2 * w / 3)} ${N(7 * h / 10)} ` +
      `Q ${N(3 * w / 4)} ${N(3 * h / 5)} ${N(11 * w / 12)} ${N(3 * h / 5)} Q ${N(w)} ${N(3 * h / 5)} ${N(w)} ${N(3 * h / 4)} ` +
      `Q ${N(w)} ${N(9 * h / 10)} ${N(7 * w / 8)} ${N(9 * h / 10)} L ${N(2 * w / 3)} ${N(9 * h / 10)} ` +
      `M ${N(7 * w / 12)} ${N(3 * h / 10)} L ${N(5 * w / 6)} ${N(3 * h / 10)} ` +
      `Q ${N(w)} ${N(3 * h / 10)} ${N(w)} ${N(9 * h / 20)} Q ${N(w)} ${N(3 * h / 5)} ${N(5 * w / 6)} ${N(3 * h / 5)} ` +
      `L ${N(2 * w / 3)} ${N(3 * h / 5)}` },
    }),
  },
  {
    id: 'gapped-eye', name: 'Gapped eye', closed: false,
    natural: { w: 40, h: 28 }, defaultW: 40, defaultH: 28,
    // The lower quadratic is split around a broad lower-right cutout so a
    // search handle or foreground tool can pass without a doubled crossing.
    geometry: (w, h) => ({ tag: 'path', attrs: { d:
      `M 0 ${N(h / 2)} Q ${N(w / 2)} ${N(-h / 2)} ${N(w)} ${N(h / 2)} ` +
      `M 0 ${N(h / 2)} Q ${N(w * 0.275)} ${N(h)} ${N(w * 0.55)} ${N(h)} ` +
      `M ${N(w * 0.85)} ${N(3 * h / 4)} Q ${N(w * 0.925)} ${N(9 * h / 14)} ${N(w)} ${N(h / 2)}` },
    }),
  },
];
