"""Step 2 — Enhanced fill pipeline with adjacency-based clustering.

Algorithms:
  - smart_fill: Hole-level rules (content detection, adjacency-based propagation)
  - reverse_all: Drop border, fill every hole, children become cutouts

Changes from step_2_fill_refactor.py:
  - Rule 3 replaced: consecutive area ratio → adjacency-based propagation
    1. Fill largest hole
    2. Skip its neighbors that are significantly smaller (ratio >= 2.0)
    3. Remaining non-adjacent holes → fill (repeat from largest remaining)
  - Native stroke widths and canvas-relative adjacency distances
  - --edge-close joins lower endpoints within each open shape (opt-in)

Usage:
    python step_2_fill_refactor_enhance.py assets_todo_svg_1024_60/ --algo smart_fill
    python step_2_fill_refactor_enhance.py assets_todo_svg_1024_60/some_icon.svg --algo reverse_all

    from step_2_fill_refactor_enhance import process
    result, df_regions = process(polygon, algo='smart_fill', buffer_dist=70)
"""

import argparse
import os

import numpy as np
import pandas as pd
from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import unary_union

from fill_utils import (
    load,
    load_one,
    adjacency_distance,
    build_region_dataframe,
    assemble_polygon,
    geometry_to_svg,
    close_open_edges,
    to_polys,
)

PIPELINE_VERSION = 'native-svg-v2'


# ---------------------------------------------------------------------------
# Fill algorithms — each takes a region DataFrame and sets the 'fill' column
# ---------------------------------------------------------------------------

# Threshold for ring detection: if a cutout child has exactly 1 hole and
# that hole takes up >= this fraction of the child's gross area, it's treated
# as a ring center → cutout (white).  Otherwise holes are detail features → keep.
RING_HOLE_PCT = 0.15

# Adjacency area ratio threshold: if a filled hole is >= this times larger
# than a neighbor, the neighbor is skipped (kept as a gap).


def _small_compact_detail(geometry, max_size):
    """Circle/square-like small detail, not an elongated mark or a hollow ring."""
    if not max_size or geometry is None or geometry.is_empty:
        return False
    x0, y0, x1, y1 = geometry.bounds
    width, height = x1-x0, y1-y0
    if min(width, height) <= 1e-8 or max(width, height) > max_size + 1e-6:
        return False
    if min(width, height) / max(width, height) < 0.75:
        return False
    return geometry.area / (width * height) >= 0.65


def _assign_nonfip_holes(df, child, grandchild_holes_mask, small_detail_size=None):
    """Assign fill for grandchild holes when the parent does NOT flip.

    Ring-center holes (single large hole in a ring shape) → 'cutout' (white).
    Detail/counter-space holes (e.g. letter B bumps) → 'keep' (show underlying fill).
    """
    gc_df = df[grandchild_holes_mask]
    if gc_df.empty:
        return

    # Ring detection: 1 hole that takes up a significant portion of the child
    if len(gc_df) == 1:
        hole = gc_df.iloc[0]
        hole_area = hole.area
        gross_area = child.area + hole_area  # child.area is net (exterior - holes)
        tiny_center = _small_compact_detail(Polygon(hole.geometry.exterior), small_detail_size)
        if tiny_center or gross_area > 0 and hole_area / gross_area >= RING_HOLE_PCT:
            df.loc[gc_df.index, 'fill'] = 'cutout'
            if tiny_center:
                df.loc[gc_df.index, 'small_detail_rule'] = 'tiny_ring_center_white'
            return

    # Multiple holes or small single hole → keep (natural shape detail)
    df.loc[gc_df.index, 'fill'] = 'keep'


def _adjacency_fill(df, unset_holes):
    """Adjacency-based propagation fill for a group of unset L2 holes.

    Algorithm:
      1. Fill the largest unset hole.
      2. All its direct neighbors → keep (adjacent to a filled hole).
      3. Repeat from step 1 with remaining unset holes until none left.
    """
    remaining = set(unset_holes.index)

    while remaining:
        # Pick the largest remaining hole
        areas = {idx: df.loc[idx, 'area'] for idx in remaining}
        largest_idx = max(areas, key=areas.get)

        # Fill it
        df.loc[largest_idx, 'fill'] = 'fill'
        remaining.discard(largest_idx)

        # Skip ALL direct neighbors (they sit next to a filled hole → keep)
        neighbors = df.loc[largest_idx, 'adjacent_to']
        for n_idx in neighbors:
            if n_idx not in remaining:
                continue
            df.loc[n_idx, 'fill'] = 'keep'
            remaining.discard(n_idx)


def smart_fill(df, buffer_dist=70, small_detail_size=None):
    """Smart fill: hole-level rules with content detection and adjacency-based
    propagation.

    Rules (applied sequentially on level 2 holes):
      1. Holes with children → fill, children become cutouts
         - Flip check: if child is big vs parent (>= 25%) AND big vs canvas
           (>= 10%), its inner holes are filled back (black) to create a
           black/white reversal.  Otherwise detail holes → keep, ring → cutout.
      2. Empty holes adjacent to content holes → keep
      3. Adjacency-based propagation on remaining unset empty holes:
         - Fill the largest hole
         - Skip all its neighbors (keep)
         - Repeat with remaining unset holes
      4. Deep holes (level 4+) → fill (usually stroke artifacts)
      5. Anything still unset → keep
    """
    if df.empty:
        return df

    holes = df[df.ring == 'hole']
    if holes.empty:
        return df

    # --- Level 2 holes (primary holes in the main shape) ---
    l2 = holes[holes.level == 2]

    # Rule 1: Holes with children → fill, children become cutouts
    content_holes = l2[l2.has_children]
    if not content_holes.empty:
        df.loc[content_holes.index, 'fill'] = 'fill'
        content_ids = set(content_holes.region_id)
        children_mask = (df.parent_id.isin(content_ids)) & (df.level == 3) & (df.ring == 'exterior')
        df.loc[children_mask, 'fill'] = 'cutout'

        # Flip check: big child vs parent AND big vs canvas → inner holes
        # get filled (remain black), creating a black/white reversal effect.
        # Small vs canvas → ring-center cutout or detail keep.
        l1_ext = df[(df.level == 1) & (df.ring == 'exterior')]
        canvas_area = l1_ext.area.sum() if not l1_ext.empty else 1.0
        PARENT_PCT_THRESH = 0.25   # 25% of parent hole
        CANVAS_PCT_THRESH = 0.10   # 10% of entire canvas

        for idx in df[children_mask].index:
            child = df.loc[idx]
            parent_hole_area = df.loc[df.region_id == child.parent_id].area.values[0]
            pct_parent = child.area / parent_hole_area if parent_hole_area else 0
            pct_canvas = child.area / canvas_area if canvas_area else 0

            grandchild_holes = (df.parent_id == child.region_id) & (df.ring == 'hole')
            if pct_parent >= PARENT_PCT_THRESH and pct_canvas >= CANVAS_PCT_THRESH:
                # Flip: cutout the exterior, but fill inner holes (black)
                df.loc[grandchild_holes, 'fill'] = 'fill'
            else:
                # No flip — decide per hole: ring-center → cutout, detail → keep
                _assign_nonfip_holes(df, child, grandchild_holes, small_detail_size)

    # Rule 2: Empty holes adjacent to any content hole → keep
    content_ids = set(content_holes.region_id) if not content_holes.empty else set()
    if content_ids:
        for idx, row in l2.iterrows():
            if row.has_children:
                continue
            if row.adjacent_to & content_ids:
                df.loc[idx, 'fill'] = 'keep'

    # Rule 3: Adjacency-based propagation on remaining unset empty holes
    # Process per level-1 exterior so disconnected components are independent
    unset_l2 = l2[(df.loc[l2.index, 'fill'].isna()) & ~l2.has_children]
    if not unset_l2.empty:
        for parent_id, group in unset_l2.groupby('parent_id'):
            if len(group) == 1:
                # Single hole in this component → fill it
                df.loc[group.index[0], 'fill'] = 'fill'
            else:
                _adjacency_fill(df, group)

    # --- Level 4+ holes and their children (recursive nesting) ---
    # Fill deep holes, mark their child exteriors as cutout, and apply the
    # same flip check used at level 2/3 to decide whether grandchild holes
    # should be filled (flip) or cutout (small shape keeps center white).
    l1_ext = df[(df.level == 1) & (df.ring == 'exterior')]
    canvas_area = l1_ext.area.sum() if not l1_ext.empty else 1.0
    PARENT_PCT_THRESH = 0.25
    CANVAS_PCT_THRESH = 0.10

    # Iteratively process deeper levels until no new fills are assigned
    changed = True
    while changed:
        changed = False

        # Fill unset deep holes (level 4+) whose parent exterior is cutout
        deep_unset = df[
            (df.ring == 'hole') & (df.level >= 4) & df.fill.isna()
        ]
        for idx, hole_row in deep_unset.iterrows():
            parent = df[df.region_id == hole_row.parent_id]
            if parent.empty:
                continue
            parent_fill = parent.iloc[0].fill
            # Only fill if parent exterior is a cutout (part of the nesting)
            if parent_fill == 'cutout':
                df.loc[idx, 'fill'] = 'fill'
                changed = True

        # Mark unset exteriors inside filled holes as cutout, with flip check
        filled_hole_ids = set(df[(df.ring == 'hole') & (df.fill == 'fill')].region_id)
        if filled_hole_ids:
            deep_ext_mask = (
                df.parent_id.isin(filled_hole_ids)
                & (df.ring == 'exterior')
                & df.fill.isna()
            )
            for idx in df[deep_ext_mask].index:
                child = df.loc[idx]
                df.loc[idx, 'fill'] = 'cutout'
                changed = True

                # Flip check: same logic as level 2/3
                parent_hole_area = df.loc[
                    df.region_id == child.parent_id
                ].area.values[0]
                pct_parent = child.area / parent_hole_area if parent_hole_area else 0
                pct_canvas = child.area / canvas_area if canvas_area else 0

                grandchild_holes = (
                    (df.parent_id == child.region_id) & (df.ring == 'hole')
                )
                if pct_parent >= PARENT_PCT_THRESH and pct_canvas >= CANVAS_PCT_THRESH:
                    df.loc[grandchild_holes, 'fill'] = 'fill'
                else:
                    _assign_nonfip_holes(df, child, grandchild_holes, small_detail_size)

    # Default: anything still unset → keep
    df.loc[df.fill.isna(), 'fill'] = 'keep'

    # Exteriors at level 1 are always kept
    df.loc[(df.level == 1) & (df.ring == 'exterior'), 'fill'] = 'keep'

    return df


def reverse_all(df, buffer_dist=70):
    """Reverse all: drop the border, each hole becomes a filled region,
    children become cutouts.

    Drops level-1 exteriors entirely. The result is only the hole regions
    turned solid.
    """
    if df.empty:
        return df

    # Drop level 1 exteriors (the border)
    df.loc[(df.level == 1) & (df.ring == 'exterior'), 'fill'] = 'drop'

    # All holes → fill (they become solid regions)
    df.loc[df.ring == 'hole', 'fill'] = 'fill'

    # Children inside filled holes → cutout
    filled_hole_ids = set(df[df.fill == 'fill'].region_id)
    children_mask = (df.parent_id.isin(filled_hole_ids)) & (df.ring == 'exterior')
    df.loc[children_mask, 'fill'] = 'cutout'

    # Default: keep
    df.loc[df.fill.isna(), 'fill'] = 'keep'

    return df


ALGOS = {
    'smart_fill': smart_fill,
    'reverse_all': reverse_all,
}


# ---------------------------------------------------------------------------
# Process single polygon
# ---------------------------------------------------------------------------

def process(polygon, algo='smart_fill', buffer_dist=70, small_detail_size=None):
    """Run the fill pipeline on a single polygon.

    Args:
        polygon: Shapely Polygon or MultiPolygon
        algo: 'smart_fill', 'reverse_all', or 'fill_all'
        buffer_dist: buffer distance for adjacency detection

    Returns:
        (result_polygon, regions_df)
    """
    df = build_region_dataframe(polygon, buffer_dist)
    if df.empty:
        return polygon, df

    algo_fn = ALGOS.get(algo)
    if algo_fn is None:
        raise ValueError(f"Unknown algo '{algo}'. Choose from: {list(ALGOS.keys())}")

    df = algo_fn(df, buffer_dist, small_detail_size=small_detail_size) if algo == 'smart_fill' else algo_fn(df, buffer_dist)
    result = assemble_polygon(df)

    return result if result is not None else polygon, df


def process_loaded_svg(row, algo='smart_fill', buffer_dist=None, small_detail_size=None):
    """Apply fill decisions and invert small detached solid details inside filled surfaces."""
    distance = adjacency_distance(row['viewbox'], buffer_dist)
    vb = [float(x) for x in row['viewbox'].strip('()').replace(',', ' ').split()]
    small_detail_size = max(vb[2:]) / 12 if small_detail_size is None else small_detail_size
    row['small_detail_size'] = small_detail_size
    polygon = row.get('stroke_polygon', row['polygon'])
    result, regions = process(polygon, algo=algo, buffer_dist=distance, small_detail_size=small_detail_size)
    solid = row.get('filled_polygon')
    parts = [p for p in (result, solid) if p is not None and not p.is_empty]
    combined = unary_union(parts) if parts else None
    cuts, evidence = [], []
    if algo == 'smart_fill' and not regions.empty:
        if 'small_detail_rule' in regions:
            for _, r in regions[regions.small_detail_rule == 'tiny_ring_center_white'].iterrows():
                evidence.append({'rule': 'tiny_ring_center_white', 'region_id': int(r.region_id),
                                 'bounds': list(r.geometry.bounds), 'area': float(r.area)})
        owners = [Polygon(r.geometry.exterior) for _, r in regions[(regions.ring == 'hole') & (regions.fill == 'fill')].iterrows()]
        detail_cutouts = [Polygon(r.geometry.exterior) for _, r in regions[(regions.ring == 'exterior') & (regions.fill == 'cutout')].iterrows()]
        clearance = max(vb[2:]) / 960  # 0.05 units at 48px; reject touches to the enclosing stroke.
        for shape in row.get('filled_shapes', []):
            for dot in to_polys(shape['geometry']):
                if dot.interiors or not _small_compact_detail(dot, small_detail_size):
                    continue
                expanded = dot.buffer(clearance)
                if not any(owner.covers(expanded) for owner in owners):
                    continue
                in_cutout = any(detail.covers(expanded) for detail in detail_cutouts)
                if not in_cutout:
                    if result is None or not result.covers(expanded):
                        continue
                    if polygon is not None and polygon.distance(dot) <= clearance:
                        continue
                cuts.append(dot)
                evidence.append({'rule': 'native_solid_dot_in_cutout_white' if in_cutout else 'native_solid_dot_white', 'source_id': shape.get('source_id'),
                                 'bounds': list(dot.bounds), 'area': float(dot.area)})
    if cuts and combined is not None:
        combined = combined.difference(unary_union(cuts))
    row['small_detail_cutouts'] = evidence
    return combined, regions, distance


def process_svg(path, algo='smart_fill', stroke_width=None, buffer_dist=None, edge_close=False, small_detail_size=None):
    """Native SVG entry point shared by the CLI, review server, and batch runner."""
    row = load_one(path, stroke_width=stroke_width, edge_close=edge_close)
    result, regions, distance = process_loaded_svg(row, algo, buffer_dist, small_detail_size)
    return row, result, regions, distance


# ---------------------------------------------------------------------------
# Print region DataFrame summary
# ---------------------------------------------------------------------------

def print_regions(df, filename=''):
    """Print a compact summary of the region DataFrame."""
    if df.empty:
        print(f"  {filename}: no regions")
        return

    n_ext = len(df[df.ring == 'exterior'])
    n_holes = len(df[df.ring == 'hole'])
    n_content = len(df[(df.ring == 'hole') & df.has_children])
    max_level = df.level.max()

    print(f"\n{'='*60}")
    print(f"  {filename}")
    print(f"  Regions: {len(df)} ({n_ext} exterior, {n_holes} holes, "
          f"{n_content} with content)  max_level={max_level}")
    print(f"{'='*60}")

    display_cols = ['region_id', 'level', 'ring', 'area', 'parent_id',
                    'has_children', 'pct_of_parent', 'fill']
    available = [c for c in display_cols if c in df.columns]
    summary = df[available].copy()
    summary['area'] = summary['area'].round(1)
    if 'pct_of_parent' in summary.columns:
        summary['pct_of_parent'] = summary['pct_of_parent'].round(1)
    print(summary.to_string(index=False))

    holes_with_adj = df[(df.ring == 'hole') & (df.adjacent_to.apply(len) > 0)]
    if not holes_with_adj.empty:
        print(f"\n  Adjacency (buffer):")
        for _, row in holes_with_adj.iterrows():
            neighbors = ', '.join(f"R{n}" for n in sorted(row.adjacent_to))
            print(f"    R{row.region_id} ↔ {neighbors}")


# ---------------------------------------------------------------------------
# Save DataFrame to CSV
# ---------------------------------------------------------------------------

def save_regions_csv(df, csv_path):
    """Save the region DataFrame to CSV (without geometry column)."""
    save_df = df.copy()
    save_df['adjacent_to'] = save_df['adjacent_to'].apply(lambda s: ','.join(str(x) for x in sorted(s)) if s else '')
    save_df = save_df.drop(columns=['geometry'], errors='ignore')
    save_df.to_csv(csv_path, index=False)


# ---------------------------------------------------------------------------
# Visualization
# ---------------------------------------------------------------------------

FILL_COLORS = {
    'fill': '#4CAF50',     # green — hole will be filled
    'keep': '#F5A623',     # orange/yellow — hole kept as-is
    'cutout': '#E91E63',   # pink — child cut out from filled hole
}

def visualize_regions(polygon, regions_df, result, filename='', viewbox_str=None,
                      buffer_dist=70, save_path=None, show=True):
    """Matplotlib visualization: original polygon, region DataFrame, and result.

    3 panels:
      1. Original — polygon with holes colored by region level
      2. Fill decisions — holes colored by fill decision (fill/keep/cutout)
      3. Result — final assembled polygon
    """
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon as MplPatch

    fig, axes = plt.subplots(1, 3, figsize=(24, 8))

    # Parse viewbox for axis limits
    if viewbox_str:
        vb = tuple(float(x) for x in viewbox_str.strip('()').replace(',', ' ').split())
    else:
        vb = (0, 0, 1024, 1024)
    vb_x, vb_y, vb_w, vb_h = vb[:4] if len(vb) >= 4 else (0, 0, 1024, 1024)
    pad_x, pad_y = vb_w * 0.05, vb_h * 0.05

    def _setup_ax(ax, title):
        ax.set_xlim(vb_x - pad_x, vb_x + vb_w + pad_x)
        ax.set_ylim(vb_y + vb_h + pad_y, vb_y - pad_y)
        ax.set_aspect('equal')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(title, fontsize=11)

    def _draw_poly(ax, poly, facecolor, edgecolor='#333', alpha=0.6, lw=1):
        coords = np.array(poly.exterior.coords)
        ax.add_patch(MplPatch(coords, closed=True, facecolor=facecolor,
                              alpha=alpha, edgecolor=edgecolor, linewidth=lw))
        for interior in poly.interiors:
            ic = np.array(interior.coords)
            ax.add_patch(MplPatch(ic, closed=True, facecolor='white',
                                  alpha=1.0, edgecolor=edgecolor, linewidth=lw * 0.5))

    def _draw_geom(ax, geom, facecolor, **kwargs):
        polys = list(geom.geoms) if isinstance(geom, MultiPolygon) else [geom]
        for p in polys:
            if hasattr(p, 'exterior'):
                _draw_poly(ax, p, facecolor, **kwargs)

    # --- Panel 1: Original polygon with level coloring ---
    ax = axes[0]
    _setup_ax(ax, 'Original (by level)')
    level_colors = {1: '#4A90D9', 2: '#F5A623', 3: '#9B59B6', 4: '#E74C3C'}
    if not regions_df.empty:
        for _, row in regions_df.iterrows():
            color = level_colors.get(row.level, '#888')
            geom = row.geometry
            if row.ring == 'exterior':
                coords = np.array(geom.exterior.coords)
                ax.add_patch(MplPatch(coords, closed=True, facecolor=color,
                                      alpha=0.35, edgecolor=color, linewidth=0.8))
            else:
                coords = np.array(geom.exterior.coords)
                ax.add_patch(MplPatch(coords, closed=True, facecolor=color,
                                      alpha=0.5, edgecolor='#D4760A', linewidth=1.2))
            # Label
            c = geom.centroid
            label = f"R{row.region_id}\nL{row.level}\n{row.area:.0f}"
            ax.annotate(label, xy=(c.x, c.y), fontsize=6, ha='center', va='center',
                        fontweight='bold', color='#333',
                        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.7))

    # --- Panel 2: Fill decisions ---
    ax = axes[1]
    _setup_ax(ax, 'Fill Decisions')
    if not regions_df.empty:
        # Draw exteriors first (background)
        for _, row in regions_df[regions_df.ring == 'exterior'].iterrows():
            coords = np.array(row.geometry.exterior.coords)
            fc = '#4A90D9' if row.fill == 'keep' else FILL_COLORS.get(row.fill, '#888')
            ax.add_patch(MplPatch(coords, closed=True, facecolor=fc,
                                  alpha=0.25, edgecolor='#4A90D9', linewidth=0.5))

        # Draw holes with fill decision colors
        for _, row in regions_df[regions_df.ring == 'hole'].iterrows():
            color = FILL_COLORS.get(row.fill, '#888')
            coords = np.array(row.geometry.exterior.coords)
            ax.add_patch(MplPatch(coords, closed=True, facecolor=color,
                                  alpha=0.6, edgecolor='#333', linewidth=1.2))
            # Label
            c = row.geometry.centroid
            label = f"R{row.region_id}\n{row.fill}\n{row.area:.0f}"
            ax.annotate(label, xy=(c.x, c.y), fontsize=6, ha='center', va='center',
                        fontweight='bold', color='#fff',
                        bbox=dict(boxstyle='round,pad=0.2', facecolor=color, alpha=0.8))

        # Draw buffer outlines for adjacency
        if buffer_dist > 0:
            for _, row in regions_df[regions_df.ring == 'hole'].iterrows():
                if row.adjacent_to:
                    buffered = row.geometry.buffer(buffer_dist)
                    buf_polys = to_polys(buffered)
                    for bp in buf_polys:
                        bc = np.array(bp.exterior.coords)
                        ax.plot(bc[:, 0], bc[:, 1], color='#2ECC71',
                                linestyle='--', linewidth=0.8, alpha=0.5)

    # --- Panel 3: Result ---
    ax = axes[2]
    _setup_ax(ax, 'Result')
    if result is not None:
        _draw_geom(ax, result, facecolor='#333', edgecolor='#000', alpha=0.85)

    # Legend
    from matplotlib.patches import Patch
    legend_items = [
        Patch(facecolor=FILL_COLORS['fill'], alpha=0.6, label='fill (hole filled in)'),
        Patch(facecolor=FILL_COLORS['keep'], alpha=0.6, label='keep (hole preserved)'),
        Patch(facecolor=FILL_COLORS['cutout'], alpha=0.6, label='cutout (child subtracted)'),
    ]
    axes[1].legend(handles=legend_items, fontsize=7, loc='lower right')

    fig.suptitle(filename, fontsize=13, fontweight='bold')
    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches='tight')

    if show:
        plt.show()
    else:
        plt.close(fig)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Step 2 (enhanced) — Fill pipeline with adjacency-based smart_fill")
    parser.add_argument("path", nargs="?", default="48",
                        help="SVG file or directory of raw SVGs (default: 48)")
    parser.add_argument("--algo", choices=list(ALGOS.keys()), default='smart_fill',
                        help="Fill algorithm (default: smart_fill)")
    parser.add_argument("--stroke-width", type=float, default=None,
                        help="Override stroke widths in SVG units; default preserves source widths")
    parser.add_argument("--buffer", type=float, default=None,
                        help="Adjacency distance in SVG units; default scales to each viewBox")
    parser.add_argument("--edge-close", action=argparse.BooleanOptionalAction,
                        default=False,
                        help="Close lower endpoints within each open shape (default: off)")
    parser.add_argument("--no-save", action="store_true",
                        help="Skip saving output SVGs")
    parser.add_argument("--visualize", action="store_true",
                        help="Show matplotlib visualization (original, fill decisions, result)")
    parser.add_argument("--save-viz", action="store_true",
                        help="Save visualization as PNG (no display)")
    parser.add_argument("--print-df", action="store_true",
                        help="Print the full region DataFrame for each file")
    parser.add_argument("--filter-ids", default=None,
                        help="JSON file with list of {id:...} to filter SVGs")
    parser.add_argument("-o", "--output", default="output_fill",
                        help="Output dir for processed SVGs (default: output_fill)")
    parser.add_argument("--recursive", action=argparse.BooleanOptionalAction, default=True,
                        help="Search nested input folders (default: on)")
    args = parser.parse_args()
    if args.stroke_width is not None and (not np.isfinite(args.stroke_width) or args.stroke_width <= 0):
        parser.error("--stroke-width must be finite and positive")
    if args.buffer is not None and (not np.isfinite(args.buffer) or args.buffer < 0):
        parser.error("--buffer must be finite and non-negative")

    # Map JSON algo_type names to internal algo names
    ALGO_TYPE_MAP = {
        'smart_fill_v2': 'smart_fill',
        'reverse_all_v2': 'reverse_all',
    }
    # Reverse map: internal algo → JSON algo_type, for filtering
    ALGO_TO_JSON = {v: k for k, v in ALGO_TYPE_MAP.items()}
    algo_filter = ALGO_TO_JSON.get(args.algo) if args.filter_ids else None

    data_df = load(args.path, stroke_width=args.stroke_width,
                   filter_ids_file=args.filter_ids, algo_filter=algo_filter,
                   edge_close=args.edge_close, recursive=args.recursive)
    if data_df.empty:
        return

    edge_close = args.edge_close

    print(f"Loaded {len(data_df)} files, algo={args.algo}, "
          f"stroke_width={args.stroke_width}, edge_close={edge_close}")

    for _, row in data_df.iterrows():
        poly_input = row['polygon']
        if poly_input is None:
            print(f"  {row['filename']}: no polygon, skipping")
            continue

        if row.get('closed_edges'):
            print(f"  Closed bottom openings: {[c['shape'] for c in row['closures']]}")
        distance = adjacency_distance(row['viewbox'], args.buffer)
        regions_df = build_region_dataframe(row['stroke_polygon'], distance)
        print_regions(regions_df, row['filename'])

        if args.print_df and not regions_df.empty:
            print(f"\n  Full DataFrame:")
            print(regions_df.to_string())

        # Per-file algo from JSON, falling back to CLI --algo
        file_algo = args.algo
        if 'algo_type' in row and pd.notna(row.get('algo_type')):
            file_algo = ALGO_TYPE_MAP.get(row['algo_type'], row['algo_type'])
        algo_fn = ALGOS[file_algo]
        regions_df = algo_fn(regions_df, distance)

        if not regions_df.empty:
            holes = regions_df[regions_df.ring == 'hole']
            for _, h in holes.iterrows():
                action = h.fill or 'keep'
                children_info = " (has children → cutouts)" if h.has_children else ""
                print(f"    R{h.region_id} L{h.level} hole: area={h.area:.0f} → {action}{children_info}")

        result = assemble_polygon(regions_df)
        if result is None:
            result = row["stroke_polygon"]
        solid = row.get("filled_polygon")
        parts = [p for p in (result, solid) if p is not None and not p.is_empty]
        result = unary_union(parts) if parts else None
        relative_dir = os.path.dirname(os.path.relpath(row["file"], args.path)) if os.path.isdir(args.path) else ""

        if not args.no_save:
            stem = os.path.splitext(row['filename'])[0]
            out_dir = os.path.join(args.output, relative_dir, stem)
            os.makedirs(out_dir, exist_ok=True)

            # Save processed SVG
            out_svg = os.path.join(out_dir, f"{stem}_processed.svg")
            svg_str = geometry_to_svg(result, row['viewbox'], row.get('width'), row.get('height'))
            with open(out_svg, 'w') as f:
                f.write(svg_str)
            print(f"  → Saved: {out_svg}")

            # Save region DataFrame as CSV
            out_csv = os.path.join(out_dir, f"{stem}_regions.csv")
            save_regions_csv(regions_df, out_csv)
            print(f"  → Saved: {out_csv}")

        # Visualization
        if args.visualize or args.save_viz:
            stem = os.path.splitext(row['filename'])[0]
            png_path = None
            if args.save_viz:
                out_dir = os.path.join(args.output, relative_dir, stem)
                os.makedirs(out_dir, exist_ok=True)
                png_path = os.path.join(out_dir, f"{stem}_regions.png")
            visualize_regions(
                poly_input, regions_df, result,
                filename=row['filename'],
                viewbox_str=row['viewbox'],
                buffer_dist=distance,
                save_path=png_path,
                show=args.visualize,
            )
            if png_path:
                print(f"  → Saved: {png_path}")


if __name__ == "__main__":
    main()
