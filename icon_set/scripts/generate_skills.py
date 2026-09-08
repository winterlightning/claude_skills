#!/usr/bin/env python3
"""Generate Claude Code and ChatGPT/Codex icon skills.

Each skill is pinned to a single family, and therefore to a single profile,
folder, base class and dist folder. Every number in it -- canvas, clearance,
the keyshape table -- is rendered from the contracts, so the skills cannot
drift from the rules they teach. The shared technique (arcs, contours, the
repair ladder, FREE) stays in ``icon_set/skills/icon-design/`` and each skill
links to it rather than restating it.

    python3 icon_set/scripts/generate_skills.py            # write both agents' skills
    python3 icon_set/scripts/generate_skills.py --agent codex  # only .agents/skills
    python3 icon_set/scripts/generate_skills.py --check    # exit 1 if any file is stale

Claude output lands in ``<repo>/.claude/skills/``; Codex output lands in
``<repo>/.agents/skills/`` with ``$icon-<family>`` invocation. The hand-authored
Claude icon-brief is also adapted for Codex; edit its Claude source to update it.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.model import contracts  # noqa: E402
from icon_set.model.icons.registry import icons_in  # noqa: E402
from icon_set.model.keyshapes import Keyshape  # noqa: E402
from icon_set.model.profiles import Profile  # noqa: E402

SKILLS_DIR = REPO_ROOT / ".claude" / "skills"
CODEX_SKILLS_DIR = REPO_ROOT / ".agents" / "skills"
SHARED = "icon_set/skills/icon-design"


def _keyshape_table(profile: Profile) -> str:
    rows = ["| Keyshape | Visible ink | Centerline box (author to this) |", "|---|---|---|"]
    for shape in Keyshape:
        if shape is Keyshape.FREE:
            continue
        if shape.is_radial:
            radius = int(shape.visible_radius_for(profile))
            cx, cy = profile.spec.center
            rows.append(f"| `CIRCLE` | radius {radius} about ({cx},{cy}) | radius {radius - 2} |")
            continue
        left, top, right, bottom = shape.bounds_for(profile)
        rows.append(
            f"| `{shape.name}` | ({left},{top})-({right},{bottom}) "
            f"| ({left + 2},{top + 2})-({right - 2},{bottom - 2}) |"
        )
    return "\n".join(rows)


def _examples(family: str, limit: int = 6) -> str:
    ids = [icon.icon_id for icon in icons_in(family)]
    shown = ", ".join(f"`{i}`" for i in ids[:limit])
    more = f" and {len(ids) - limit} more" if len(ids) > limit else ""
    return f"{shown}{more}"


def _content_region() -> tuple[int, int, int, int]:
    """Where a hosted SUB32 child lands, derived from the frozen template.

    Advisory since the protected slot was withdrawn on 2026-09-07: it marks a
    place, it does not reserve one.
    """
    template = contracts.composition_templates()["classes"]["CONTAINER_COMBINE"]
    content = template["children"][1]
    left, top = content["position"]
    size = Profile[content["profile"]].spec.canvas_size
    return (left, top, left + size, top + size)


# Family-specific guidance. Everything numeric comes from the contract; these
# are the judgement calls that differ per family.
FAMILY_TEXT = {
    "sub": {
        "trigger": (
            "Use when asked for a small glyph, mark, operator, arrow, chevron, state, "
            "modifier, or a simple shape meant to sit inside a container or beside another "
            "icon -- anything that must read at 32 pixels."
        ),
        "default_role": "SUB",
        "default_kind": "modifier",
        "default_category": "primitives/<operator|mark|shape|arrow|chevron|control>",
        "job": (
            "A **sub** icon is read small and hosted by others. Its whole canvas is the "
            "container's content region, so anything valid here can be placed in one. "
            "Verbs, states and modifiers declare `semantic_role = \"SUB\"`; a simple noun "
            "shape (`heart`, `circle`, `star`) declares `MAIN` with `semantic_kind = "
            "\"noun\"` and is still a sub icon -- the role describes the subject, the "
            "family decides the canvas."
        ),
        "specifics": [
            "Eight stroke widths across the canvas. Keep the smallest recognizable "
            "silhouette and one identifying feature; a third level of detail does not "
            "survive at 32 pixels.",
            "The stroke-defined glyphs (`minus`, `bar`, `dot`, `exclamation`, `ellipsis`, "
            "`dots-vertical`) use `FREE` with an approved record. A new 4-unit-axis glyph "
            "needs its own record in `icon_set/model/contracts/exceptions.v1.json` with "
            "`status: \"proposed\"`; see `{shared}/keyshape-fitting.md`.",
            "Straight parts may sit exactly on the 7-unit centerline minimum. Curved parts "
            "need a unit of margin or the engine returns `review`.",
            "After it validates, prove it composes: "
            "`python3 icon_set/scripts/compose.py --host container-circle --sub <icon_id>`.",
        ],
        "not_this": (
            "If the brief is a standalone subject with its own silhouette (a device, an "
            "object, a badge), stop and use `/icon-solo`. If it is an enclosure meant to "
            "hold something, use `/icon-container`."
        ),
    },
    "solo": {
        "trigger": (
            "Use when asked for a standalone subject -- a device, object, badge, tool, "
            "figure, or a traced reference drawing -- that is read on its own at 48 pixels "
            "and neither hosts nor is hosted."
        ),
        "default_role": "MAIN",
        "default_kind": "noun",
        "default_category": "objects/<device|media|award|...>",
        "job": (
            "A **solo** icon is one independently readable subject. The whole 48 canvas "
            "belongs to it: there is nothing it must fit inside. It "
            "is always `semantic_role = \"MAIN\"`, `semantic_kind = \"noun\"`."
        ),
        "specifics": [
            "Twelve stroke widths across the canvas: one more feature than a sub icon, no "
            "more. Between a curved outline and an interior part you need the 8-unit "
            "minimum *plus* a unit of margin, because the engine cannot certify a curved "
            "pair sitting exactly on the minimum. `film-frame` moved from `SQUARE` to "
            "`VRECT_XL` for exactly this reason: a 15-deep band cannot hold a 4-unit mark "
            "with 8 on both sides.",
            "Traced references: render first, then re-author on this grid. Reconstruct "
            "the subject, never the source's coordinates. Pick arc radii whose apex *is* "
            "the endpoint so the arc cannot overshoot the keyshape (`smartwatch`: r 15 "
            "from (10,11) to (22,5)).",
            "Split a wall where a part attaches so the two share an endpoint; declare "
            "the contact with `relate(\"connect\", ...)`. An arc merely touching a line is "
            "not proved as a connection and comes back `review`.",
            "Same concept also wanted at 32 or 64? That is a separately authored icon in "
            "another family with a suffix (`bell-sub`, `bell-container`). Never scale.",
        ],
        "not_this": (
            "If the brief is a small glyph, operator or modifier meant to be hosted, stop "
            "and use `/icon-sub`. If it is an enclosure meant to hold a sub icon, use "
            "`/icon-container`."
        ),
    },
    "container": {
        "trigger": (
            "Use when asked for an enclosure, frame, window, screen, badge outline, "
            "bubble, board, card, or any framed device drawn at 64."
        ),
        "default_role": "MAIN",
        "default_kind": "noun",
        "default_category": "containers",
        "job": (
            "A **container** stands alone as a noun and is the outer half of a "
            "`CONTAINER_COMBINE`. Nothing inside its canvas is reserved: draw the "
            "subject with the interior furniture it actually has -- a title bar, a "
            "lid, a dial face, a keypad. `{slot}` is the **content region**, where a "
            "hosted child would land; the base adds `content-top-left` and "
            "`content-bottom-right` anchors marking it. Painting through it is allowed "
            "and often necessary; it just means this container will not clear that "
            "child, which `compose.py` measures per pair. The protected slot that used "
            "to forbid ink there was withdrawn on 2026-09-07 -- it made windows, tab "
            "bars and lids undrawable -- and `contracts/composition-templates.v1.json` "
            "keeps the record under `withdrawn_slot`."
        ),
        "specifics": [
            "Design the subject, then measure what it holds -- not the other way "
            "round. Ink anywhere in `{slot}` is legal; it costs hosting for children "
            "whose own ink reaches that far, and `mic` reports exactly which.",
            "A gap that sits exactly on the minimum is only certifiable when both "
            "sides are straight. Where a straight run has to hold a minimum gap, "
            "emit it as its own path rather than inside a contour that also carries "
            "corner arcs -- but only where the parts genuinely still share endpoints, "
            "because splitting a corner into two paths that do not touch invents "
            "crowding that is not there. See `browser-window`.",
            "Attached details (a clip, a tab, a handle) share endpoints with the outline "
            "and are declared with `relate(\"connect\", ...)`. See `clipboard`.",
            "After it validates, measure what it hosts: run "
            "`python3 icon_set/scripts/compose.py --host <icon_id> --sub plus`, then "
            "`--sub heart` and `--sub check`. Record the answer in the docstring. "
            "Hosting nothing is a legitimate outcome for a container with a full "
            "interior; it is never a reason to empty the drawing out.",
        ],
        "not_this": (
            "If the subject reads at 48 and is never framed around anything, use "
            "`/icon-solo`. If it is the thing that goes *inside*, use `/icon-sub`."
        ),
    },
}


def render(family: str) -> str:
    row = contracts.families()[family]
    profile = Profile.for_family(family)
    spec = profile.spec
    text = FAMILY_TEXT[family]
    folder = row["package"].rsplit("/", 1)[-1]
    dist = row["dist"].rsplit("/", 1)[-1]
    base = row["base_class"]
    region = _content_region()
    region_text = f"({region[0]},{region[1]})-({region[2]},{region[3]})"
    fmt = {"shared": SHARED, "slot": region_text}
    others = [f for f in contracts.families() if f != family]
    other_lines = "\n".join(
        f"- `/icon-{other}` — {other} family, "
        f"`{contracts.families()[other]['profile']}`, "
        f"{Profile.for_family(other).spec.canvas_size}×{Profile.for_family(other).spec.canvas_size}"
        for other in others
    )
    specifics = "\n".join(f"- {item.format(**fmt)}" for item in text["specifics"])
    module_example = f"icon_set/model/icons/{folder}/<icon_id_with_underscores>.py"
    guide_l, guide_t, guide_r, guide_b = spec.interior_guide_bounds
    cx, cy = spec.center

    return f"""---
name: icon-{family}
description: Author a {family}-family icon for the Pictographic icon set on the {row['profile']} profile ({spec.canvas_size}x{spec.canvas_size}). {text['trigger']} Generated from the contracts by icon_set/scripts/generate_skills.py; do not edit by hand.
argument-hint: <icon-id> — <one-sentence brief> [references: <paths>]
---

# /icon-{family} — one {family} icon on `{row['profile']}`

Request: $ARGUMENTS

This skill authors **exactly one family**. Everything below is fixed by the
family and read from `icon_set/model/contracts/icon-profile.v1.json`:

| | |
|---|---|
| Family | `{family}` |
| Profile | `{row['profile']}` |
| Canvas | {spec.canvas_size}×{spec.canvas_size}, centre ({cx},{cy}), integer grid 1, stroke 4, round caps and joins |
| Module goes in | `icon_set/model/icons/{folder}/` — one file per icon |
| Subclass | `{base}` from `._base` |
| Ships to | `icon_set/{row['dist']}/` with its own `manifest.json` |
| Ink clearance (MIC) | {spec.mic} between distinct parts = **{spec.equal_stroke_centerline_min} between centerlines** |
| Interior guide | ({guide_l},{guide_t})-({guide_r},{guide_b}) — constrains inner detail only |
| Existing icons to imitate | {_examples(family)} |

{text['job'].format(**fmt)}

**Wrong family? Stop.** {text['not_this']} A {family} icon cannot be authored on
another canvas: the base has no profile to override, the registry refuses a
`{base}` in another folder, and the validator rejects the profile. Do not widen
this skill's scope to "just draw it bigger"; name the right skill and hand over.

{other_lines}

## Visual priorities

Prioritize **Lucide-style geometric construction and smooth curves**.
Prefer mirrored geometry and visual balance only where they preserve the icon's
meaning, recognizability, and natural shape. These are optional design choices,
not requirements: skip mirroring or forced balance when they would distort the
subject. A palm tree, for example, may retain uneven fronds and a leaning trunk;
mirror only the parts where it helps the drawing read clearly.

Before authoring, inspect a relevant local Lucide original and its atomic-debug
geometry when a useful match exists. Use its construction principles with this
family's own grid, stroke and keyshape; preserve the requested subject.

Build symmetric subjects from a shared axis and mirrored coordinates, with
matching radii and spacing. Preserve intentional asymmetry in directional,
perspective, or naturally asymmetric subjects. Make curve-to-curve and
curve-to-line joins tangent-continuous where the silhouette should be smooth;
round stroke caps alone do not repair a kink. Prefer fewer coherent curves over
many short segments. Preserve deliberate corners and recognizable features.

Apply `icon_set/skills/icon-design/authoring.md` for the construction and visual
review checklist. A numeric pass alone is not enough: inspect curve flow,
paired proportions, and negative space at native size in both themes. Repair
tight areas by rebalancing geometry, without weakening validation rules.

## Procedure

1. **Name it.** One sentence for what the subject is, then a kebab-case
   `icon_id` (`^[a-z][a-z0-9]*(-[a-z0-9]+)*$`). Synonyms go in `aliases`,
   search terms in `keywords`. Keep a supplied `sym-<id>` at the front.
   Preserve any reference UUID or explicit source ID separately from the name.
   Search existing Python files by that ID before creating a new file; patch the
   matching module for this family when it already exists.
   See `{SHARED}/naming.md`.

2. **Reduce.** Keep the smallest recognizable silhouette, the features that carry
   identity, and nothing that disappears at {spec.canvas_size} pixels. With a
   reference in scope, render it and look at it; read the subject, never the
   coordinates. See `{SHARED}/intake.md`.

3. **Choose the keyshape, write down its four extremes, design backwards to
   them.** The rectangle fit is exact (tolerance 0); `CIRCLE` is radial. These are
   the `{row['profile']}` numbers:

{_keyshape_table(profile)}

   Ask the model instead of doing arithmetic:
   `Keyshape.HRECT_L.bounds_for(Profile.{profile.name})`.

4. **Author the module** at `{module_example}`:

   For a supplied reference ID, the new filename must instead be
   `<descriptive_name>_<source_id_with_underscores>.py`. Every generated module
   or one-off Python generation script must include `SOURCE_ICON_ID` (the exact
   original ID) and `SOURCE_PATH` (the supplied source path). Use `None` only
   for missing values; never discard an ID because the input also has a name.
   Follow the UUID example and patch lookup in `{SHARED}/naming.md`.

   ```python
   from ...keyshapes import Keyshape
   from ._base import {base}

   SOURCE_ICON_ID = "<exact-reference-id>"  # None only if no ID was supplied
   SOURCE_PATH = "<source-path>"  # None only if no path was supplied


   class <ClassName>({base}):
       icon_id = "<icon-id>"
       keyshape = Keyshape.<TOKEN>
       semantic_role = "{text['default_role']}"
       semantic_kind = "{text['default_kind']}"
       category = "{text['default_category']}"
       aliases = ()
       keywords = ()

       def build(self) -> None:
           # add_line / add_arc / add_dot / add_polyline / add_contour / relate
           ...
   ```

   Contour members paint as round joins; loose primitives as round caps. Where two
   parts genuinely touch, share an endpoint and declare it:
   `self.relate("connect", "a", "b")` — that pair only. Technique, arcs and
   tangent-continuous joins: `{SHARED}/geometry.md`, `{SHARED}/authoring.md`.

   Nothing to register. The folder is the registry.

5. **Validate and repair the model, never the SVG.**

   ```python
   from icon_set.model.icons.registry import create
   report = create("<icon-id>").validate_icon()
   print(report.describe())      # status must be "valid" with zero warnings
   ```

   Eight checks run in order; every failure names the element and coordinates.
   A `review` warning is **not** a pass. Repair ladder for crowding: enlarge the
   opening, rebalance, remove the part — never squeeze. Re-check the keyshape after
   every repair. See `{SHARED}/validation.md`.

6. **Family-specific checks.**

{specifics}

7. **Build and look.**

   ```bash
   python3 -m unittest discover -s icon_set/tests -t .
   python3 icon_set/scripts/build.py --family {family}
   python3 icon_set/scripts/contact_sheet.py --family {family} --theme dark --png /tmp/{family}.png
   ```

   Open the PNG and judge it at {spec.canvas_size} pixels. Numeric success is not
   visual approval; if two candidates are close, render both and keep the stronger.

8. **Report.** Say what the subject is, which keyshape and why, what you dropped
   and why, which references you used and what you took from each, and the
   validation status. If something could not be made to pass, name the check and
   the element and stop — a reported blocker beats a weakened rule.

## Never

- Change a profile constant, keyshape dimension, tolerance or `numeric_epsilon`.
- Put this icon in another family's folder or subclass another base for a
  different canvas.
- Scale a drawing from another family. Every family is authored fresh.
- Declare `connect` on parts that do not touch, add a `FREE` record to dodge a
  repair, or describe a `review` as a pass.
- Hand-write or patch the emitted SVG.

## Definition of done

- Python filename includes the supplied source ID for a new file; the script
  records the exact `SOURCE_ICON_ID` and `SOURCE_PATH`. Existing matches are
  patched in place, with source metadata preserved or added.
- Tests green; `build.py --family {family}` exits 0; the icon is in
  `icon_set/{row['dist']}/manifest.json`.
- `validate_icon()` is `valid` with no warnings.
- Reviewed at native size in both themes for smooth joins, consistent radii,
  balanced negative space, and symmetry wherever the subject supports it.
- State which Lucide construction informed the drawing, or that no useful match
  was found; explain any deliberate asymmetry.
"""


def render_codex(content: str) -> str:
    """Adapt host syntax while retaining the shared authoring instructions."""
    content = "\n".join(
        line for line in content.split("\n")
        if not line.startswith("argument-hint:")
    )
    # `skills/icon-design` is a real path, not a skill invocation.
    content = content.replace("skills/icon-design", "\0")
    content = content.replace("/icon-", "$icon-")
    content = content.replace("\0", "skills/icon-design")
    content = content.replace(
        "Hand-authored; edit this file directly.",
        "Generated from .claude/skills/icon-brief/SKILL.md by "
        "icon_set/scripts/generate_skills.py; edit the source, not this copy.",
    )
    return content.replace(
        "Request: $ARGUMENTS",
        "Use the user's request as the brief, including any supplied icon ID, "
        "reference paths, and output directory.\n\n"
        "Resolve repository paths and run commands from the `icon_lib` directory "
        "containing `icon_set/` (three levels above this skill folder). "
        "In Codex, invoke these skills with `$icon-brief`, `$icon-sub`, "
        "`$icon-solo`, or `$icon-container`; in ChatGPT, select the skill with `@`. "
        "Treat slash-style handoffs in generated briefs as references to the "
        "corresponding skill.",
    )


def write_all(check_only: bool = False, agent: str = "all") -> int:
    stale = []
    outputs = {}
    for family in contracts.families():
        content = render(family)
        if agent in ("all", "claude"):
            outputs[SKILLS_DIR / f"icon-{family}" / "SKILL.md"] = content
        if agent in ("all", "codex"):
            outputs[CODEX_SKILLS_DIR / f"icon-{family}" / "SKILL.md"] = render_codex(content)
    if agent in ("all", "codex"):
        brief = (SKILLS_DIR / "icon-brief" / "SKILL.md").read_text(encoding="utf-8")
        outputs[CODEX_SKILLS_DIR / "icon-brief" / "SKILL.md"] = render_codex(brief)
    for target, content in outputs.items():
        current = target.read_text(encoding="utf-8") if target.is_file() else None
        if current == content:
            continue
        stale.append(target)
        if not check_only:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            print(f"wrote {target.relative_to(REPO_ROOT)}")
    if check_only and stale:
        for target in stale:
            print(f"stale: {target.relative_to(REPO_ROOT)}")
        return 1
    if not stale:
        print("skills up to date")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="report stale files instead of writing")
    parser.add_argument("--agent", choices=("all", "claude", "codex"), default="all",
                        help="which agent's skills to generate (default: all)")
    args = parser.parse_args(argv)
    return write_all(check_only=args.check, agent=args.agent)


if __name__ == "__main__":
    raise SystemExit(main())
