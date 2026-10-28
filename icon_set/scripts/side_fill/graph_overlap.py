"""Compare the black/white region graph of a main fill with a side composition.

This is a conservative geometry check. A lost enclosed white region or black
component is evidence for review, not proof that a particular semantic detail
was intentionally or unintentionally changed. It evaluates the rendered 4px
cut; it does not test whether an essential white mark in a filled main enters
the separate 8px validation zone. That decision belongs to visual review.
"""

from __future__ import annotations

from shapely.geometry import Polygon

from .combine_fill_side import polygons


MIN_REGION_AREA = 2.0
WHITE_PRESERVED = 0.85
BLACK_PRESERVED = 0.55
SPLIT_MIN_AREA = 4.0


def _bounds(geometry):
    return [round(value, 3) for value in geometry.bounds]


def _parts(geometry):
    return sorted(polygons(geometry), key=lambda part: (-part.area, part.bounds))


def region_graph(geometry):
    """Return geometry-bearing black/white nodes and containment edges."""
    black = _parts(geometry)
    holes = []
    for index, part in enumerate(black):
        for ring in part.interiors:
            hole = Polygon(ring)
            if hole.area >= MIN_REGION_AREA:
                holes.append((index, hole))
    holes.sort(key=lambda item: (-item[1].area, item[1].bounds))
    nodes = []
    edges = []
    for index, part in enumerate(black):
        nodes.append({"id": f"black_{index}", "kind": "black", "geometry": part})
    for index, (owner, hole) in enumerate(holes):
        hole_id = f"white_{index}"
        nodes.append({"id": hole_id, "kind": "white", "geometry": hole})
        edges.append({"from": f"black_{owner}", "to": hole_id, "kind": "contains"})
        for black_index, part in enumerate(black):
            if black_index != owner and hole.contains(part.representative_point()):
                edges.append({"from": hole_id, "to": f"black_{black_index}", "kind": "contains"})
    return nodes, edges


def _public_graph(nodes, edges):
    return {
        "nodes": [
            {"id": node["id"], "kind": node["kind"], "area": round(node["geometry"].area, 3),
             "bounds": _bounds(node["geometry"])}
            for node in nodes
        ],
        "edges": edges,
    }


def analyze(main, sub, cut, combined, clearance):
    """Track every meaningful main region through the cut and final union.

    Black main nodes are matched against the cut main, so a sub painted in the
    same location cannot falsely count as preserved main material. White nodes
    are matched against holes of the final combination, so a sub covering a
    white detail is detected even if the cut main still contains its hole.
    """
    main_nodes, main_edges = region_graph(main)
    final_nodes, final_edges = region_graph(combined)
    cut_black = _parts(cut)
    final_white = [node for node in final_nodes if node["kind"] == "white"]
    used_white = set()
    matches = []
    issues = []
    for node in main_nodes:
        source = node["geometry"]
        area = source.area
        if area < MIN_REGION_AREA:
            continue
        if node["kind"] == "black":
            kept_area = source.intersection(cut).area
            fraction = min(1.0, kept_area / area)
            fragments = [
                part for part in cut_black
                if source.intersection(part).area >= max(SPLIT_MIN_AREA, area * 0.05)
            ]
            matches.append({
                "source": node["id"], "kind": "black", "kept_fraction": round(fraction, 4),
                "clearance_overlap_area": round(source.intersection(clearance).area, 3),
                "fragment_count": len(fragments),
            })
            if fraction < BLACK_PRESERVED:
                issues.append({"type": "black_component_lost", "source": node["id"], "kept_fraction": round(fraction, 4)})
            elif len(fragments) > 1:
                issues.append({"type": "black_component_split", "source": node["id"], "fragments": len(fragments)})
        else:
            candidates = [
                (other["geometry"].intersection(source).area / area, other)
                for other in final_white if other["id"] not in used_white
            ]
            best_fraction, best = max(candidates, key=lambda item: item[0], default=(0.0, None))
            if best is not None and best_fraction > 0:
                used_white.add(best["id"])
            matches.append({
                "source": node["id"], "kind": "white", "kept_fraction": round(best_fraction, 4),
                "matched_final": best["id"] if best is not None and best_fraction > 0 else None,
                "clearance_overlap_area": round(source.intersection(clearance).area, 3),
            })
            if best_fraction < WHITE_PRESERVED:
                issues.append({"type": "white_region_lost", "source": node["id"], "kept_fraction": round(best_fraction, 4)})
    return {
        "status": "review" if issues else "pass",
        "issues": issues,
        "main": _public_graph(main_nodes, main_edges),
        "combined": _public_graph(final_nodes, final_edges),
        "matches": matches,
        "sub_area": round(sub.area, 3),
        "main_area": round(main.area, 3),
        "cut_main_area": round(cut.area, 3),
    }
