#!/usr/bin/env python3
"""Try a profile number against the whole corpus before committing to it.

The profile constants -- canvas, interior guide inset, MIC, keyshape scale --
live in two locked contracts, and every icon in the set was authored against
them. Changing one by hand means editing JSON, regenerating the resolved
keyshape table, regenerating the skills, rebuilding dist and re-running the
validator, and only then finding out that six icons no longer fit. This script
does that loop in one command, without touching a locked file:

    python3 icon_set/scripts/profile_lab.py show
    python3 icon_set/scripts/profile_lab.py try SOLO48.interior_guide_inset=8
    python3 icon_set/scripts/profile_lab.py try CONTAINER64.mic=6 --render
    python3 icon_set/scripts/profile_lab.py try SQUARE.width=26 SQUARE.height=26

`try` measures every registered icon twice -- once under the shipped contracts,
once under the proposal -- and prints what moved: which icons stop validating,
which gain or lose edge padding, which now have detail outside the interior
guide, and how the tightest clearance in each icon compares to the proposed
MIC. Nothing is written unless you pass `--write`.

The proposal is applied through ICON_CONTRACT_OVERLAY in a subprocess, so the
locked contracts, the build and the tests never see it.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

CONTRACTS = REPO_ROOT / "icon_set" / "model" / "contracts"
PROFILE_CONTRACT = "icon-profile.v1"
KEYSHAPE_CONTRACT = "keyshapes.v1"

PROFILE_FIELDS = ("canvas_size", "interior_guide_inset", "mic",
                  "equal_stroke_centerline_min", "keyshape_scale_numerator",
                  "keyshape_scale_denominator")
STYLE_FIELDS = ("grid", "stroke_width")


# -- measurement (runs in the child, under whatever contracts are in force) --

def measure() -> dict:
    from icon_set.model import contracts
    from icon_set.model.icons.registry import icons_in
    from icon_set.model.profiles import Profile
    from icon_set.validation import envelope
    from icon_set.validation.path_commands import commands_for_path
    from icon_set.validation.stroke_distance import analyze_paths
    from icon_set.validation.validator import IconValidator
    from icon_set.renderers.svg import build_paths

    validator = IconValidator()
    rows: dict[str, dict] = {}
    for family in contracts.families():
        profile = Profile.for_family(family)
        spec = profile.spec
        guide = spec.interior_guide_bounds
        for icon in icons_in(family):
            row: dict = {"family": family, "profile": profile.name,
                         "keyshape": getattr(icon.keyshape, "name", "?")}
            try:
                resolved = list(icon.draw().primitives)
                painted = envelope.visible_bounds(resolved)
                canvas = spec.canvas_size
                row["painted"] = [round(value, 4) for value in painted]
                row["edge_padding"] = round(min(painted[0], painted[1],
                                                canvas - painted[2],
                                                canvas - painted[3]), 4)
                row["guide_overflow"] = round(max(guide[0] - painted[0],
                                                  guide[1] - painted[1],
                                                  painted[2] - guide[2],
                                                  painted[3] - guide[3]), 4)
                # The silhouette is *supposed* to reach its keyshape envelope,
                # which for most keyshapes is already outside the guide. The
                # number a padding rule turns on is the interior detail: the
                # parts that do not touch the envelope and therefore had no
                # reason to cross the guide.
                inner = _interior_overflow(icon, build_paths(icon.draw()), guide)
                row["interior_overflow"] = inner[0]
                row["interior_parts"] = inner[1]
                paths = build_paths(icon.draw())
                if len(paths) > 1:
                    payload = [{"elementId": path["id"],
                                "commands": commands_for_path(path["primitives"],
                                                              path["closed"])}
                               for path in paths]
                    result = analyze_paths(payload, minimum_distance=float(canvas * 4),
                                           stroke_width=float(spec_stroke()))
                    distances = [pair.get("centerlineDistance")
                                 for pair in result.get("pairs", [])
                                 if isinstance(pair.get("centerlineDistance"), (int, float))]
                    row["min_clearance"] = round(min(distances), 4) if distances else None
                else:
                    row["min_clearance"] = None
            except Exception as error:  # a proposal can make geometry unresolvable
                row["error"] = f"{type(error).__name__}: {error}"

            try:
                report = validator.validate(icon)
                row["valid"] = report.ok
                row["findings"] = list(report.errors)
            except Exception as error:
                row["valid"] = False
                row["findings"] = [f"validator raised {type(error).__name__}: {error}"]
            rows[icon.icon_id] = row

    return {"profiles": _profile_snapshot(), "icons": rows}


def _interior_overflow(icon, paths, guide) -> tuple[float, int]:
    """Max distance interior parts push past the guide, and how many do.

    Measured per **contour**, not per segment. A silhouette is one closed path
    that sits on its keyshape envelope, and a segment of it that happens to
    curve inward -- a bus roofline, a robe shoulder -- is still silhouette, not
    interior detail. Judging segment by segment reports those as violations and
    roughly triples the count.
    """
    from icon_set.validation import envelope

    try:
        target = icon.keyshape_bounds()
    except ValueError:
        target = None
    worst, count = 0.0, 0
    for path in paths:
        try:
            bounds = envelope.visible_bounds(path["primitives"])
        except (ValueError, ZeroDivisionError):
            continue
        if target is not None and any(
            abs(bounds[index] - target[index]) <= 0.001 for index in range(4)
        ):
            continue  # part of the outer silhouette, sitting on its envelope
        over = max(guide[0] - bounds[0], guide[1] - bounds[1],
                   bounds[2] - guide[2], bounds[3] - guide[3])
        if over > 0.001:
            count += 1
            worst = max(worst, over)
    return round(worst, 4), count


def spec_stroke() -> int:
    from icon_set.model.profiles import STROKE_WIDTH
    return STROKE_WIDTH


def _profile_snapshot() -> dict:
    from icon_set.model import contracts
    from icon_set.model.keyshapes import Keyshape
    from icon_set.model.profiles import Profile, STROKE_WIDTH

    out: dict = {"style": {"stroke_width": STROKE_WIDTH,
                           "grid": contracts.icon_profile()["style"]["grid"]}}
    for profile in Profile:
        spec = profile.spec
        square = Keyshape.SQUARE.bounds_for(profile)
        out[profile.name] = {
            "family": spec.family,
            "canvas_size": spec.canvas_size,
            "interior_guide_inset": spec.interior_guide_inset,
            "interior_guide_bounds": list(spec.interior_guide_bounds),
            "mic": spec.mic,
            "equal_stroke_centerline_min": spec.equal_stroke_centerline_min,
            "keyshape_scale": f"{spec.keyshape_scale_numerator}/{spec.keyshape_scale_denominator}",
            "square_bounds": list(square),
            "square_edge_padding": square[0],
        }
    return out


def render_all(out: Path) -> None:
    from icon_set.model import contracts
    from icon_set.model.icons.registry import icons_in
    from icon_set.renderers.png import render_png

    out.mkdir(parents=True, exist_ok=True)
    for family in contracts.families():
        for icon in icons_in(family):
            try:
                (out / f"{icon.icon_id}.png").write_bytes(render_png(icon, scale=6))
            except Exception:
                continue


# -- proposal parsing --------------------------------------------------------

def parse_assignments(items: list[str]) -> tuple[dict, list[str]]:
    """Turn `SOLO48.mic=5` style arguments into an overlay document."""
    from icon_set.model import contracts

    profile_doc = contracts.load(PROFILE_CONTRACT)
    keyshape_doc = contracts.load(KEYSHAPE_CONTRACT)
    profiles = {name for name in profile_doc["profiles"]}
    bases = {row["name"]: row for row in keyshape_doc["base"]}

    profile_patch: dict = {}
    style_patch: dict = {}
    base_patch: dict[str, dict] = {}
    labels: list[str] = []

    for item in items:
        if "=" not in item or "." not in item.split("=", 1)[0]:
            raise SystemExit(f"error: expected TARGET.field=value, got {item!r}")
        target, raw = item.split("=", 1)
        scope, field = target.rsplit(".", 1)
        try:
            value = int(raw)
        except ValueError:
            raise SystemExit(f"error: {item!r} — values are integers")

        if scope in profiles:
            if field not in PROFILE_FIELDS:
                raise SystemExit(f"error: {scope} has no field {field!r}; "
                                 f"choose from {', '.join(PROFILE_FIELDS)}")
            was = profile_doc["profiles"][scope][field]
            profile_patch.setdefault("profiles", {}).setdefault(scope, {})[field] = value
            labels.append(f"{scope}.{field}: {was} → {value}")
        elif scope == "style":
            if field not in STYLE_FIELDS:
                raise SystemExit(f"error: style has no editable field {field!r}; "
                                 f"choose from {', '.join(STYLE_FIELDS)}")
            was = profile_doc["style"][field]
            style_patch[field] = value
            labels.append(f"style.{field}: {was} → {value}")
        elif scope in bases:
            if field not in ("width", "height"):
                raise SystemExit(f"error: keyshape {scope} has no field {field!r}")
            was = bases[scope][field]
            base_patch.setdefault(scope, {})[field] = value
            labels.append(f"{scope}.{field}: {was} → {value} (base size, scales to every profile)")
        else:
            raise SystemExit(f"error: unknown target {scope!r}; use a profile "
                             f"({', '.join(sorted(profiles))}), `style`, or a keyshape name")

    overlay: dict = {}
    if style_patch:
        profile_patch.setdefault("style", {}).update(style_patch)
    if profile_patch:
        overlay[PROFILE_CONTRACT] = profile_patch

    # The resolved table is a mirror of base size x profile scale, and
    # `keyshapes.py` asserts the two agree at import. Any proposal that moves
    # either side has to carry a rebuilt table or nothing will import.
    from icon_set.model.contracts import _merge

    proposed_profile = _merge(profile_doc, profile_patch) if profile_patch else profile_doc
    base = [dict(row) for row in keyshape_doc["base"]]
    for row in base:
        row.update(base_patch.get(row["name"], {}))
    if base_patch or _scale_or_canvas_moved(profile_patch):
        overlay[KEYSHAPE_CONTRACT] = {
            "base": base,
            "resolved": resolve_keyshape_table(proposed_profile, base),
        }
    return overlay, labels


def _scale_or_canvas_moved(profile_patch: dict) -> bool:
    watched = {"canvas_size", "keyshape_scale_numerator", "keyshape_scale_denominator"}
    if any(field in profile_patch.get("style", {}) for field in ("stroke_width",)):
        return True
    return any(watched & set(fields)
               for fields in profile_patch.get("profiles", {}).values())


def resolve_keyshape_table(profile_doc: dict, base_rows: list[dict]) -> dict:
    """The resolved table, derived the way `Keyshape.bounds_for` derives it.

    Pure arithmetic on the two contract documents, so it can be computed for a
    proposal before any module has imported it. Reproduces the shipped table
    exactly when handed the shipped documents.
    """
    stroke = profile_doc["style"]["stroke_width"]
    radius = stroke / 2.0
    table: dict = {}
    for name, profile in profile_doc["profiles"].items():
        canvas = profile["canvas_size"]
        numerator = profile["keyshape_scale_numerator"]
        denominator = profile["keyshape_scale_denominator"]
        rows: dict = {}
        for base in base_rows:
            width, w_rest = divmod(base["width"] * numerator, denominator)
            height, h_rest = divmod(base["height"] * numerator, denominator)
            if w_rest or h_rest:
                raise SystemExit(f"error: {base['name']} does not scale to an "
                                 f"integer on {name} ({numerator}/{denominator})")
            left, x_rest = divmod(canvas - width, 2)
            top, y_rest = divmod(canvas - height, 2)
            if x_rest or y_rest:
                raise SystemExit(f"error: {base['name']} cannot centre on the "
                                 f"{canvas}x{canvas} integer grid of {name}")
            bounds = [left, top, left + width, top + height]
            row = {
                "width": width,
                "height": height,
                "visible_bounds": bounds,
                "centerline_bounds": [bounds[0] + int(radius), bounds[1] + int(radius),
                                      bounds[2] - int(radius), bounds[3] - int(radius)],
            }
            if base["orientation"] == "radial":
                row["visible_radius"] = _number(width / 2.0)
                row["centerline_radius"] = _number(width / 2.0 - radius)
                row["center"] = [canvas // 2, canvas // 2]
            rows[base["name"]] = row
        table[name] = rows
    return table


def _number(value: float):
    return int(value) if float(value).is_integer() else value


# -- the editable page -------------------------------------------------------

def page_data() -> dict:
    """Everything the HTML page needs to recompute the rules in the browser.

    Geometry is exported on the **centerline**, never as painted bounds: the
    painted envelope is the centerline grown by half the stroke, so a page
    holding centerlines can redraw and re-measure at any stroke width, which a
    page holding painted bounds cannot.
    """
    from icon_set.model import contracts
    from icon_set.model.icons.registry import icons_in
    from icon_set.model.keyshapes import Keyshape
    from icon_set.model.profiles import Profile, STROKE_WIDTH
    from icon_set.validation import envelope
    from icon_set.validation.path_commands import commands_for_path
    from icon_set.validation.stroke_distance import analyze_paths
    from icon_set.renderers.svg import build_paths

    profile_doc = contracts.icon_profile()
    profiles = {}
    for profile in Profile:
        spec = profile.spec
        profiles[profile.name] = {
            "family": spec.family,
            "canvas": spec.canvas_size,
            "inset": spec.interior_guide_inset,
            "mic": spec.mic,
            "min_gap": spec.equal_stroke_centerline_min,
            "numerator": spec.keyshape_scale_numerator,
            "denominator": spec.keyshape_scale_denominator,
        }

    keyshapes = {shape.name: {"width": shape.base_size.width,
                              "height": shape.base_size.height,
                              "orientation": shape.orientation}
                 for shape in Keyshape if shape is not Keyshape.FREE}

    icons = []
    for family in contracts.families():
        profile = Profile.for_family(family)
        centre = profile.spec.center
        for icon in icons_in(family):
            try:
                resolved = list(icon.draw().primitives)
                paths = build_paths(icon.draw())
            except Exception:
                continue
            parts = []
            for path in paths:
                try:
                    bounds = envelope.centerline_bounds(path["primitives"])
                except (ValueError, ZeroDivisionError):
                    continue
                parts.append({"id": path["id"], "d": path["d"],
                              "bounds": [round(value, 4) for value in bounds]})
            clearance = None
            if len(paths) > 1:
                payload = [{"elementId": path["id"],
                            "commands": commands_for_path(path["primitives"], path["closed"])}
                           for path in paths]
                result = analyze_paths(payload,
                                       minimum_distance=float(profile.spec.canvas_size * 4),
                                       stroke_width=float(STROKE_WIDTH))
                distances = [pair.get("centerlineDistance") for pair in result.get("pairs", [])
                             if isinstance(pair.get("centerlineDistance"), (int, float))]
                if distances:
                    clearance = round(min(distances), 4)
            keyshape = getattr(icon.keyshape, "name", "FREE")
            free_bounds = None
            if keyshape == "FREE":
                try:
                    free_bounds = list(icon.keyshape_bounds())
                except Exception:
                    free_bounds = None
            icons.append({
                "id": icon.icon_id,
                "family": family,
                "profile": profile.name,
                "keyshape": keyshape,
                "free_bounds": free_bounds,
                "bounds": [round(value, 4)
                           for value in envelope.centerline_bounds(resolved)],
                "radial": round(envelope.centerline_radial_extent(resolved, centre), 4),
                "clearance": clearance,
                "parts": parts,
            })

    return {"stroke": STROKE_WIDTH, "grid": profile_doc["style"]["grid"],
            "profiles": profiles, "keyshapes": keyshapes,
            "icons": sorted(icons, key=lambda row: (row["profile"], row["id"]))}


def write_page(out: Path) -> None:
    template = Path(__file__).resolve().parent / "profile_lab.html"
    if not template.is_file():
        raise SystemExit(f"error: missing page template {template}")
    payload = json.dumps(page_data(), separators=(",", ":"))
    html = template.read_text(encoding="utf-8")
    marker = "/*PROFILE_LAB_DATA*/null"
    if marker not in html:
        raise SystemExit(f"error: {template.name} has no {marker} placeholder")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html.replace(marker, payload), encoding="utf-8")
    print(f"wrote {out}")
    print(f"  {len(page_data()['icons'])} icons embedded from the registry")
    print(f"  open it, move the sliders, and copy the `try` line it builds")
    print(f"  edit the layout in {template.relative_to(REPO_ROOT)} and re-run this command")


def run_child(command: str, overlay: Path | None, extra: list[str] | None = None) -> dict:
    env = dict(os.environ)
    if overlay is not None:
        env["ICON_CONTRACT_OVERLAY"] = str(overlay)
    else:
        env.pop("ICON_CONTRACT_OVERLAY", None)
    argv = [sys.executable, str(Path(__file__).resolve()), command, *(extra or [])]
    done = subprocess.run(argv, capture_output=True, text=True, env=env, cwd=REPO_ROOT)
    if done.returncode != 0:
        sys.stderr.write(done.stderr)
        raise SystemExit(f"error: measurement under {'proposal' if overlay else 'baseline'} failed")
    return json.loads(done.stdout) if done.stdout.strip() else {}


# -- reporting ---------------------------------------------------------------

def _fmt(value) -> str:
    if value is None:
        return "—"
    if isinstance(value, float) and value == int(value):
        return str(int(value))
    return str(value)


def report(before: dict, after: dict, labels: list[str], mic_by_profile: dict) -> int:
    print("Proposal\n")
    for label in labels:
        print(f"  {label}")

    print("\nProfiles\n")
    header = f"  {'profile':<12} {'canvas':>6} {'guide':>16} {'mic':>4} {'min gap':>8} {'SQUARE pad':>11}"
    print(header)
    for name, row in after["profiles"].items():
        if name == "style":
            continue
        old = before["profiles"][name]
        mark = "*" if row != old else " "
        guide = "(" + ",".join(str(v) for v in row["interior_guide_bounds"]) + ")"
        print(f" {mark}{name:<12} {row['canvas_size']:>6} {guide:>16} {row['mic']:>4} "
              f"{row['equal_stroke_centerline_min']:>8} {row['square_edge_padding']:>11}")

    broke, fixed, changed = [], [], []
    for icon_id, row in after["icons"].items():
        old = before["icons"].get(icon_id, {})
        if old.get("valid") and not row.get("valid"):
            broke.append((icon_id, row))
        elif not old.get("valid") and row.get("valid"):
            fixed.append((icon_id, row))
        if (old.get("edge_padding") != row.get("edge_padding")
                or old.get("guide_overflow") != row.get("guide_overflow")):
            changed.append((icon_id, old, row))

    total = len(after["icons"])
    print(f"\nValidation — {total} icons: {sum(1 for r in after['icons'].values() if r.get('valid'))} pass, "
          f"{len(broke)} newly failing, {len(fixed)} newly passing\n")
    for icon_id, row in broke[:10]:
        print(f"  BREAKS  {icon_id} ({row['profile']})")
        for finding in row.get("findings", [])[:2]:
            print(f"          {finding}")
    if len(broke) > 10:
        rest = ", ".join(icon_id for icon_id, _ in broke[10:])
        print(f"  BREAKS  and {len(broke) - 10} more: {rest}")
    for icon_id, row in fixed[:10]:
        print(f"  FIXED   {icon_id} ({row['profile']})")
    if len(fixed) > 10:
        print(f"  FIXED   and {len(fixed) - 10} more")
    if not broke and not fixed:
        print("  no change in which icons validate")

    print("\nInterior guide — interior detail outside the proposed guide\n")
    rows = sorted(((icon_id, row) for icon_id, row in after["icons"].items()
                   if (row.get("interior_overflow") or 0) > 0),
                  key=lambda pair: -(pair[1]["interior_overflow"]))
    silhouette = sum(1 for row in after["icons"].values()
                     if (row.get("guide_overflow") or 0) > 0
                     and not (row.get("interior_overflow") or 0))
    if rows:
        width = max(len(icon_id) for icon_id, _ in rows) + 2
        print(f"  {'icon':<{width}}{'profile':<13}{'keyshape':<11}{'outside by':>10}{'was':>7}{'parts':>7}")
        for icon_id, row in rows:
            was = before["icons"].get(icon_id, {}).get("interior_overflow")
            flag = " " if was == row["interior_overflow"] else "*"
            print(f" {flag}{icon_id:<{width}}{row['profile']:<13}{row['keyshape']:<11}"
                  f"{_fmt(row['interior_overflow']):>10}{_fmt(was):>7}{row['interior_parts']:>7}")
        print("\n  * = changed by this proposal. These are the icons a tighter guide")
        print("    would ask you to redraw; the guide constrains interior detail only.")
    else:
        print("  none — every icon's interior detail is inside the proposed guide")
    print(f"\n  {silhouette} more icons reach past the guide with their keyshape "
          "envelope itself,\n  which is what a full-width or radial keyshape is for.")

    print("\nClearance headroom — tightest gap in each icon vs the proposed minimum\n")
    tight = []
    for icon_id, row in after["icons"].items():
        gap = row.get("min_clearance")
        if gap is None:
            continue
        required = mic_by_profile.get(row["profile"])
        if required is not None and gap < required:
            tight.append((gap - required, icon_id, row, gap, required))
    if tight:
        print(f"  {'icon':<26} {'profile':<12} {'tightest':>9} {'needs':>7} {'short by':>9}")
        for _, icon_id, row, gap, required in sorted(tight):
            print(f"  {icon_id:<26} {row['profile']:<12} {_fmt(gap):>9} "
                  f"{_fmt(required):>7} {_fmt(round(required - gap, 4)):>9}")
        print("\n  A gap below the minimum is only a failure when the pair is not a "
              "declared\n  contact and does not belong to one placed child; see the "
              "validation block above.")
    else:
        print("  every measured gap clears the proposed minimum")

    return 1 if broke else 0


def write_through(overlay: dict) -> None:
    """Persist a proposal into the locked contracts and regenerate what derives."""
    for name, patch in overlay.items():
        path = CONTRACTS / f"{name}.json"
        document = json.loads(path.read_text(encoding="utf-8"))
        from icon_set.model.contracts import _merge
        document = _merge(document, patch)
        path.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
        print(f"  wrote {path.relative_to(REPO_ROOT)}")

    from importlib import reload
    from icon_set.model import contracts as contracts_module
    contracts_module.load.cache_clear()
    reload(contracts_module)
    _rewrite_resolved_table()
    subprocess.run([sys.executable, "icon_set/scripts/generate_skills.py"], cwd=REPO_ROOT)
    print("\nStill yours to do:")
    print("  - icon_set/tests/test_profiles_keyshapes.py pins the old constants in")
    print("    `test_locked_constants` and `test_interior_guide_bounds`; update both.")
    print("  - add a `notes` entry to icon-profile.v1.json saying what changed and why.")
    print("  - python3 -m unittest discover -s icon_set/tests")
    print("  - python3 icon_set/scripts/build.py")


def _rewrite_resolved_table() -> None:
    """Keep the resolved keyshape table in step with the numbers just written."""
    profile_doc = json.loads((CONTRACTS / f"{PROFILE_CONTRACT}.json").read_text(encoding="utf-8"))
    path = CONTRACTS / f"{KEYSHAPE_CONTRACT}.json"
    document = json.loads(path.read_text(encoding="utf-8"))
    document["resolved"] = resolve_keyshape_table(profile_doc, document["base"])
    path.write_text(json.dumps(document, indent=1, ensure_ascii=False) + "\n",
                    encoding="utf-8")
    print(f"  rebuilt the resolved keyshape table in {path.relative_to(REPO_ROOT)}")


def compare_page(before_dir: Path, after_dir: Path, out: Path, labels: list[str]) -> None:
    names = sorted(path.stem for path in after_dir.glob("*.png"))
    cards = "".join(
        f'<figure><div><img src="before/{name}.png" alt=""><img src="after/{name}.png" alt=""></div>'
        f'<figcaption>{name}</figcaption></figure>' for name in names)
    out.write_text(f"""<!doctype html><meta charset="utf-8">
<title>Profile proposal</title>
<style>
body{{margin:0;background:#faf9f7;color:#141413;font:14px/1.5 system-ui,sans-serif}}
header{{padding:22px 26px;border-bottom:1px solid #e5e3dd}}
h1{{margin:0 0 6px;font-size:18px}} code{{background:#f0efea;padding:1px 5px;border-radius:4px}}
main{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px;padding:20px}}
figure{{margin:0;background:#fff;border:1px solid #e5e3dd;border-radius:10px;padding:12px}}
figure div{{display:flex;gap:10px;justify-content:center;align-items:center}}
img{{max-width:46%;image-rendering:pixelated}}
figcaption{{margin-top:8px;text-align:center;color:#6b6963;font-size:12px}}
@media (prefers-color-scheme:dark){{body{{background:#1a1a18;color:#f2f1ec}}
figure{{background:#232320;border-color:#33322e}} img{{filter:invert(1)}}}}
</style>
<header><h1>Profile proposal — before (left) / after (right)</h1>
<p>{'; '.join(labels) or 'no change'}</p></header>
<main>{cards}</main>
""", encoding="utf-8")
    print(f"\n  comparison page: {out.relative_to(REPO_ROOT)}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    shown = sub.add_parser("show", help="print the profile numbers in force")
    shown.add_argument("--json", action="store_true", help="machine-readable instead of a table")
    trial = sub.add_parser("try", help="measure a proposal against every icon")
    trial.add_argument("assignments", nargs="+", metavar="TARGET.field=value")
    trial.add_argument("--render", action="store_true",
                       help="render every icon before and after into work/profile-lab/")
    trial.add_argument("--write", action="store_true",
                       help="persist the proposal into the contracts and regenerate skills")
    trial.add_argument("--out", type=Path, default=REPO_ROOT / "work" / "profile-lab")
    page = sub.add_parser("page", help="write the editable HTML lab with the live corpus in it")
    page.add_argument("--out", type=Path, default=REPO_ROOT / "work" / "profile-lab" / "lab.html")
    sub.add_parser("_measure", help=argparse.SUPPRESS)
    render = sub.add_parser("_render", help=argparse.SUPPRESS)
    render.add_argument("out", type=Path)
    args = parser.parse_args(argv)

    if args.command == "_measure":
        json.dump(measure(), sys.stdout)
        return 0
    if args.command == "_render":
        render_all(args.out)
        return 0
    if args.command == "page":
        write_page(args.out)
        return 0
    if args.command == "show":
        snapshot = _profile_snapshot()
        if args.json:
            print(json.dumps(snapshot, indent=2))
            return 0
        print(f"stroke {snapshot['style']['stroke_width']}, grid "
              f"{snapshot['style']['grid']}, integer coordinates\n")
        print(f"  {'profile':<13}{'family':<11}{'canvas':>7}{'guide':>18}{'mic':>5}"
              f"{'min gap':>9}{'scale':>7}{'SQUARE pad':>12}")
        for name, row in snapshot.items():
            if name == "style":
                continue
            guide = "(" + ",".join(str(value) for value in row["interior_guide_bounds"]) + ")"
            print(f"  {name:<13}{row['family']:<11}{row['canvas_size']:>7}{guide:>18}"
                  f"{row['mic']:>5}{row['equal_stroke_centerline_min']:>9}"
                  f"{row['keyshape_scale']:>7}{row['square_edge_padding']:>12}")
        print("\n  guide      interior detail stays inside this box; the silhouette need not")
        print("  mic        ink-to-ink clearance between distinct parts")
        print("  min gap    the same rule measured between centerlines (mic + stroke)")
        print("  SQUARE pad canvas edge to the SQUARE envelope, i.e. the outer padding a")
        print("             full-bleed rectilinear icon is drawn to")
        print("\n  Try a change:  python3 icon_set/scripts/profile_lab.py try "
              "SOLO48.interior_guide_inset=8")
        return 0

    overlay, labels = parse_assignments(args.assignments)
    if not overlay:
        raise SystemExit("error: nothing to change")

    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
        json.dump(overlay, handle)
        overlay_path = Path(handle.name)

    try:
        before = run_child("_measure", None)
        after = run_child("_measure", overlay_path)
        mic = {name: row["equal_stroke_centerline_min"]
               for name, row in after["profiles"].items() if name != "style"}
        code = report(before, after, labels, mic)
        if args.render:
            run_child("_render", None, [str(args.out / "before")])
            run_child("_render", overlay_path, [str(args.out / "after")])
            compare_page(args.out / "before", args.out / "after",
                         args.out / "compare.html", labels)
        if args.write:
            print("\nWriting through to the contracts\n")
            write_through(overlay)
        else:
            print("\nNothing written. Re-run with --write to apply this proposal.")
        return code
    finally:
        overlay_path.unlink(missing_ok=True)


if __name__ == "__main__":
    raise SystemExit(main())
