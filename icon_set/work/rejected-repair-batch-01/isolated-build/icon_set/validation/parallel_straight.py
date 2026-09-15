"""Blocking parallel straight clearance across the whole resolved drawing.

Midpoint rays measure nearest neighbors on both sides. Positive-overlap pairs
also remain blocking, including staggered pairs missed by midpoint probes.
An intentional join does not exempt other facing edges of the connected shape.
"""
from .parallel_midpoints import analyze
from .report import Finding

RULES = {"version": 2, "profiles": "all", "blocking": True,
         "required_centerline_distance": 8, "required_ink_clearance": 4,
         "parallelism": "exact", "scope": "whole drawing",
         "measurement": "midpoint normals, nearest each side, with overlap fallback",
         "merge": "touching collinear pieces in same path",
         "relationship_exemption": False, "collinear_overlaps": "separate diagnostic"}


def check_parallel_straight(icon, drawing):
    required = RULES["required_centerline_distance"]
    try:
        result = analyze(drawing, required)
    except (ValueError, TypeError, ZeroDivisionError) as error:
        return [Finding("mic", f"parallel straight geometry could not be checked: {error}",
                        detail={"rule": "parallel_straight", "geometry_error": True})]
    pairs = {}
    for hit in result["hits"]:
        if hit["below_minimum"]:
            key = tuple(sorted((hit["source"], hit["target"])))
            pairs.setdefault(key, dict(hit, method="midpoint-normal"))
    for overlap in result["unmeasured_overlaps"]:
        if overlap["below_minimum"]:
            pairs.setdefault(tuple(overlap["pair"]), dict(overlap, method="overlap-fallback"))
    findings = []
    for (first, second), measurement in sorted(pairs.items()):
        a, b = result["runs"][first], result["runs"][second]
        distance = measurement["centerline_distance"]
        detail = dict(measurement, rule="parallel_straight",
                      elements=a["members"] + b["members"],
                      source_members=a["members"], target_members=b["members"],
                      required_centerline_distance=required, required_ink_clearance=4)
        findings.append(Finding(
            "mic", f"parallel straight edges {', '.join(a['members'])} and {', '.join(b['members'])} "
            f"are {distance:g} apart on centerlines (ink gap {measurement['ink_gap']:g}); "
            f"requires at least {required} centerline / 4 ink ({measurement['method']})",
            a["path"], detail))
    return findings
