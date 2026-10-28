"""Write a file://-friendly catalog for the local Normal side-pair gallery."""

from __future__ import annotations

from .paths import DATA, FILL_ENGINE, WORK  # noqa: F401
import json
from collections import Counter
from functools import lru_cache
import os
import hashlib
from functools import lru_cache
from pathlib import Path
from urllib.parse import quote

from .ai_variant_review import REVIEW_PROTOCOL
from .adaptive_overlap import fill_path, source_path
from .combine_fill_side import load_fill
from .combine_fill_side_layouts import repo_layout_svg
from .pair_layout_review import (keyshape_validation, source_centerline_bounds,
                                 source_keyshape_name)



HERE = WORK
WORKSPACE = DATA
LAYOUTS = DATA / "data/production-layouts.json"
REPORT = WORK / "normal-fill-proposals/report.json"
GRAPH_REPORT = WORK / "normal-fill-proposals/graph-report.json"
OUTPUT = WORK / "gallery-data.js"
RECOMBINED_REPORT = WORK / "recombined-all/report.json"
VARIANT_REPORT = (RECOMBINED_REPORT if RECOMBINED_REPORT.is_file()
                  else WORK / "adaptive-8px-all/report.json")
VARIANT_OUTPUT = VARIANT_REPORT.parent
SIDE_DECISIONS = DATA / "data/ai-variant-decisions.json"
LAYOUT_SPECS = DATA / "data/ai-layout-proposals.json"
LAYOUT_OUTPUT = WORK / "ai-layout-proposals"


def url(path: Path) -> str | None:
    if not path.is_file():
        return None
    relative = Path(os.path.relpath(path, HERE))
    # Recombines rewrite SVGs under the same names; the version makes browsers fetch the new file.
    return ("/".join(quote(part, safe="-._~") for part in relative.parts)
            + f"?v={path.stat().st_mtime_ns:x}")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@lru_cache(maxsize=2048)
def source_meta(role: str, filename: str, modified_ns: int) -> dict:
    path = Path(filename)
    bounds = source_centerline_bounds(repo_layout_svg(), path, role)
    return {"sha256": sha256(path), "bounds": bounds,
            "shape": source_keyshape_name(role, bounds)}


def part_keyshape(part: dict, role: str) -> tuple[dict, dict | None]:
    canvas = 48 if role == 'main' else 32
    empty = {"canvas": canvas}
    if not part.get('icon'):
        return empty, None
    path = source_path(part, role)
    if not path.is_file():
        return empty, None
    try:
        meta = source_meta(role, str(path), path.stat().st_mtime_ns)
    except (ValueError, IndexError, TypeError):
        return empty, None
    expected = part.get('current_sha') or part.get('built_sha')
    if expected and meta['sha256'] != expected:
        return empty, None
    bounds = meta['bounds']
    return {"canvas": canvas, "source_shape": meta['shape'],
            "preset": meta['shape'] if meta['shape'] != 'custom' else 'own',
            "size": canvas, "guide_kind": 'circle' if meta['shape'] == 'CIRCLE' else 'rect',
            "guide_painted_box": [bounds[0]-2, bounds[1]-2, bounds[2]+2, bounds[3]+2],
            "fits_keyshape": True, "stroke_envelope_inside_canvas": True}, meta


def component(part: dict, role: str, guide: dict | None = None) -> dict:
    key = part.get("icon")
    if not key or "/" not in key:
        return {"key": key, "name": part.get("draw_name") or "No linked drawing", "source": None, "fill": None}
    name = key.split("/", 1)[1]
    revision = part.get("current_sha") or part.get("built_sha")
    if role == "main":
        source = DATA / "normal" / f"{name}.svg"
    else:
        source = DATA / "archive/side-sub-32" / f"{name}.svg"
        if not source.is_file():
            source = DATA / "archive/sub-32-revisions" / name / f"{revision}.svg"
    fill = fill_path(part, role)
    result = {"key": key, "name": name, "source": url(source), "fill": url(fill),
              "revision": revision, "guide": guide or {"canvas": 48 if role == 'main' else 32},
              "has_fill": genuine_fill(source, fill)}
    if role == "main":
        # Standalone fill variants from build_main_variant_previews.py (current fill excluded).
        entry = main_variant_index().get(name, {})
        result["variants"] = [{"variant": v["variant"], "status": v["status"], "url": url(HERE / v["svg"])}
                              for v in entry.get("variants", []) if (HERE / v["svg"]).is_file()]
    return result


FILL_CACHE = WORK / "genuine-fill-cache.json"
_fill_cache: dict | None = None


def genuine_fill(source: Path, fill: Path) -> bool:
    """Whether a fill paints more than its source outline (the server's fill-combination rule,
    ai_variant_review.candidate_has_genuine_fill), cached by the two files' hashes."""
    global _fill_cache
    if not source.is_file() or not fill.is_file():
        return False
    if _fill_cache is None:
        _fill_cache = json.loads(FILL_CACHE.read_text()) if FILL_CACHE.exists() else {}
    key = f"{sha256(source)}:{sha256(fill)}"
    if key not in _fill_cache:
        _fill_cache[key] = load_fill(source)[0].symmetric_difference(load_fill(fill)[0]).area > 1
    return _fill_cache[key]


def fill_combination(candidate: dict, main_filled: bool, sub_filled: bool) -> bool:
    """A candidate that paints at least one genuinely filled icon (else the server refuses it)."""
    main_variant = candidate.get("base_variant", candidate["variant"])
    sub_variant = candidate.get("sub_variant", "fill")
    if main_variant not in ("current", "outline"):
        return True
    return (main_variant == "current" and main_filled) or (sub_variant == "fill" and sub_filled)


@lru_cache(maxsize=1)
def main_variant_index() -> dict:
    path = WORK / "main-variants/index.json"
    return json.loads(path.read_text()) if path.exists() else {}


def layout_entry(candidate: dict, keyshape_checks: dict, stress_file: Path | None) -> dict:
    """A pair-local layout candidate as a gallery tile (also sent back by the layout save)."""
    file = LAYOUT_OUTPUT / candidate["svg"]
    return {
        "variant": candidate["variant"], "kind": "layout",
        "base_variant": candidate["base_variant"],
        "sub_variant": candidate.get("sub_variant", "fill"),
        "position": candidate.get("position"),
        "main_adjustment": candidate["main"],
        "sub_adjustment": candidate["sub"],
        "layout_reason": candidate["reason"],
        "keyshape_validation": keyshape_checks,
        "keyshape_override": candidate.get("keyshape_override", False),
        "stress": url(stress_file) if stress_file else None,
        "stress_sha256": candidate.get("stress_sha256"),
        "white_border_loss_at_8px": candidate.get("white_border_loss_at_8px", []),
        "white_region_overlaps": candidate["white_regions_inside_8px"],
        "combined": url(file), "safe": None,
        "status": candidate["status"],
        "main_style": "normal", "sub_style": "normal",
        "sha256": candidate["candidate_sha256"],
        "validation_overlap": sum(x["overlap_px2"] for x in candidate["white_regions_inside_8px"]),
        "render_gap": candidate["render_gap_px"],
        "graph_status": candidate["graph_status"],
        "graph_issues": candidate["graph_issues"],
    }


def build() -> dict:
    main_variant_index.cache_clear()
    layouts = json.loads(LAYOUTS.read_text())["items"]
    report = json.loads(REPORT.read_text())
    graph_report = json.loads(GRAPH_REPORT.read_text()) if GRAPH_REPORT.exists() else {}
    variant_report = json.loads(VARIANT_REPORT.read_text()) if VARIANT_REPORT.exists() else {"rows": []}
    variant_by_id = {row["id"]: row for row in variant_report["rows"]}
    variant_errors = {row["id"]: row["error"] for row in variant_report.get("errors", [])}
    layout_report = json.loads((LAYOUT_OUTPUT / "report.json").read_text()).get("pairs", {}) if (LAYOUT_OUTPUT / "report.json").exists() else {}
    layout_specs = json.loads(LAYOUT_SPECS.read_text()).get("pairs", {}) if LAYOUT_SPECS.exists() else {}
    layout_digest = sha256(LAYOUTS)
    decisions = json.loads(SIDE_DECISIONS.read_text()).get("decisions", {}) if SIDE_DECISIONS.exists() else {}
    by_id = {row["id"]: row for row in report["rows"]}
    rows = []
    for item in layouts:
        reference_id = item["reference_id"]
        result = by_id[reference_id]
        graph = graph_report.get(reference_id, {})
        main_nodes = {node["id"]: node for node in graph.get("main", {}).get("nodes", [])}
        parts = {part["role"]: part for part in item["parts"]}
        main_source_guide, main_meta = part_keyshape(parts.get('main', {}), 'main')
        sub_source_guide, sub_meta = part_keyshape(parts.get('sub', {}), 'sub')
        pair_guides = {"canvas": 64}
        for role, meta in (('main', main_meta), ('sub', sub_meta)):
            part = parts.get(role, {})
            if meta and part.get('layout') and parts.get('sub', {}).get('position'):
                try:
                    pair_guides[role] = keyshape_validation(
                        role, parts['sub']['position'], meta['bounds'], part['layout'], {})
                except (ValueError, KeyError, ZeroDivisionError):
                    pass
        pair = WORK / "normal-fill-proposals/svg" / f"{reference_id}.svg"
        variant_row = variant_by_id.get(reference_id, {})
        variants = []
        for candidate in variant_row.get("candidates", []):
            if candidate.get("main_style", "normal") != "normal" or candidate.get("sub_style", "normal") != "normal":
                continue
            if candidate.get("duplicate_of"):   # same picture as the stroke-keeping current fill
                continue
            combined = url(VARIANT_OUTPUT / candidate["svg"])
            if combined:
                variants.append({
                    "variant": candidate["variant"],
                    "kind": "normal",
                    "combined": combined,
                    "safe": candidate["safe"],
                    "status": candidate["semantic_status"],
                    "main_style": candidate.get("main_style", "normal"),
                    "sub_style": candidate.get("sub_style", "normal"),
                    "sha256": candidate.get("candidate_sha256") or sha256(VARIANT_OUTPUT / candidate["svg"]),
                    "validation_overlap": candidate["added_fill_inside_validation_px2"],
                    "render_gap": candidate.get("render_gap_px"),
                    "graph_status": candidate["graph_status"],
                    "graph_issues": candidate["graph_issues"],
                })
        layout_row = layout_report.get(reference_id, {})
        expected_specs = hashlib.sha256(json.dumps(layout_specs.get(reference_id, []),
                            sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        layout_sources_current = bool(layout_row) and all(
            path.is_file() and layout_row.get(field) == sha256(path)
            for field, path in (
                ("main_source_sha256", source_path(parts["main"], "main")),
                ("sub_source_sha256", source_path(parts["sub"], "sub")),
                ("main_fill_sha256", fill_path(parts["main"], "main")),
                ("sub_fill_sha256", fill_path(parts["sub"], "sub")),
            ))
        if (layout_row.get("layout_sha256") == layout_digest
                and layout_row.get("pair_specs_sha256") == expected_specs
                and layout_sources_current):
            for candidate in layout_row.get("candidates", []):
                file = LAYOUT_OUTPUT / candidate["svg"]
                if not file.is_file() or sha256(file) != candidate["candidate_sha256"]:
                    continue
                keyshape_checks = candidate.get('keyshape_validation', {})
                if keyshape_checks and any((not check.get('fits_keyshape') and
                                            not candidate.get('keyshape_override')) or
                                           not check.get('stroke_envelope_inside_canvas')
                                           for check in keyshape_checks.values()):
                    continue
                stress_file = LAYOUT_OUTPUT / candidate['stress_svg'] if candidate.get('stress_svg') else None
                if stress_file and (not stress_file.is_file() or sha256(stress_file) != candidate.get('stress_sha256')):
                    continue
                variants.append(layout_entry(candidate, keyshape_checks, stress_file))
        main_filled = component(parts.get("main", {}), "main").get("has_fill", False)
        sub_filled = component(parts.get("sub", {}), "sub").get("has_fill", False)
        # Candidates the server would refuse (no genuinely filled icon) are not offered.
        not_fill = [candidate["variant"] for candidate in variants
                    if not fill_combination(candidate, main_filled, sub_filled)]
        variants = [candidate for candidate in variants if candidate["variant"] not in not_fill]
        decision = decisions.get(reference_id)
        evidence = decision.get('evidence', []) if decision else []
        if isinstance(evidence, str):
            evidence = [evidence]
        review_sheet = next((url(path) for value in evidence if isinstance(value, str)
                             for path in [Path(value) if Path(value).is_absolute()
                                          else WORKSPACE / value]
                             if path.resolve().is_relative_to(HERE) and path.is_file()
                             and path.suffix.lower() == '.png'), None)
        reviewed_at_48 = bool(decision and decision.get('review_protocol') == REVIEW_PROTOCOL)
        selected = next((candidate for candidate in variants
                         if reviewed_at_48 and decision.get("status") == "accepted"
                         and candidate["variant"] == decision.get("variant")
                         and candidate["sha256"] == decision.get("candidate_sha256")), None)
        acceptable = decision.get("acceptable_candidate_sha256", {}) if reviewed_at_48 else {}
        rejected = decision.get("rejected_candidate_sha256", {}) if decision else {}
        for candidate in variants:
            stress_valid = (candidate.get('kind') != 'layout' or candidate.get('base_variant') == 'outline'
                            or (candidate.get('stress') and candidate.get('stress_sha256')
                                == decision.get('stress_candidate_sha256', {}).get(candidate['variant']))) if decision else candidate.get('kind') != 'layout'
            candidate["ai_acceptable"] = bool(stress_valid and (
                candidate is selected or acceptable.get(candidate["variant"]) == candidate["sha256"]))
            candidate["ai_rejected"] = bool(rejected.get(candidate["variant"]) == candidate["sha256"])
        if selected and not selected['ai_acceptable']:
            selected = None
        proposals = [candidate["variant"] for candidate in variants if candidate["ai_acceptable"]]
        if selected is None and proposals:
            selected = next(candidate for candidate in variants if candidate["variant"] == proposals[0])
        variant_unavailable = None
        if not variants:
            variant_unavailable = variant_errors.get(reference_id) or {
                "sub_not_a_drawing": "The sub part has no linked drawing to combine.",
                "main_source_hash_mismatch": "The saved main drawing revision differs from the current source.",
            }.get(result["status"], "No variants were generated for this proposal." if result["status"] == "proposal"
                  else f"The pair build is held: {result['status'].replace('_', ' ')}.")
        rows.append({
            "id": reference_id,
            "concept": item["concept"],
            "state": item["state"],
            "status": result["status"],
            "main": component(parts.get("main", {}), "main", main_source_guide),
            "sub": component(parts.get("sub", {}), "sub", sub_source_guide),
            "pair_guides": pair_guides,
            "combined": url(pair) if result["status"] == "proposal" else None,
            "variant_combinations": variants,
            "selected_variant": selected["variant"] if selected else None,
            "proposed_variants": proposals,
            "review_reason": decision.get("reason") if selected or
                             decision and decision.get('status') == 'pending_human' else None,
            "review_sheet": review_sheet,
            "selection_status": ("selected" if selected else "stale" if decision and decision.get("status") == "accepted"
                                 else decision.get("status", "pending") if decision else "pending"),
            "variant_unavailable": variant_unavailable,
            "style_unavailable": variant_row.get("style_unavailable", {}),
            "main_layout": result.get("main_layout"),
            "sub_layout": result.get("sub_layout"),
            "gap": result.get("gap"),
            "flags": result.get("flags", []),
            "graph_status": result.get("graph_status"),
            "graph_issues": result.get("graph_issues", []),
            "graph_regions": [
                {**match, "area": main_nodes.get(match["source"], {}).get("area")}
                for match in graph.get("matches", [])
            ],
            "graph_edges": graph.get("main", {}).get("edges", []),
        })
    assert len(rows) == sum(report["counts"].values())
    assert sum(row["combined"] is not None for row in rows) == report["counts"].get("proposal", 0)
    # Pairs with no combined artwork (text subs, changed or missing sources) are left out of the
    # gallery; their saved layouts are untouched and only counted here.
    unavailable = Counter(row["status"] if row["combined"] is None else "no_fill_combination"
                          for row in rows if not row["variant_combinations"])
    rows = [row for row in rows if row["variant_combinations"]]
    if _fill_cache is not None:
        FILL_CACHE.write_text(json.dumps(_fill_cache) + "\n")
    payload = {"counts": report["counts"], "hidden_unavailable": dict(unavailable), "graph_reviews": sum(row["graph_status"] == "review" for row in rows),
               "variant_pairs": sum(bool(row["variant_combinations"]) for row in rows),
               "variant_combinations": sum(len(row["variant_combinations"]) for row in rows),
               "selected_pairs": sum(row["selection_status"] == "selected" for row in rows), "rows": rows}
    OUTPUT.write_text("window.SIDE_COMBINATIONS = " + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";\n")
    return {"rows": len(rows), "proposals": report["counts"].get("proposal", 0),
            "graph_reviews": payload["graph_reviews"], "variant_pairs": payload["variant_pairs"],
            "variant_combinations": payload["variant_combinations"], "output": str(OUTPUT)}


if __name__ == "__main__":
    print(json.dumps(build(), indent=2))
