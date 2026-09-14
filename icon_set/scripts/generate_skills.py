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
    choices = contracts.icon_profile()["profiles"][profile.name].get("keyshape_choices")
    for shape in Keyshape:
        if shape is Keyshape.FREE or (choices and shape.name not in choices):
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
    # Keep instructions stable while new icons are generated in the workspace.
    return ", ".join(f"`{i}`" for i in ids[:limit])


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
            "Curved parts need margin unless the distance engine certifies exact "
            "axis separation. Preserve the exact human head-to-body gap from "
            "`{shared}/human-reference.md`.",
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
            "A **solo** icon is one independently readable subject. It is never hosted "
            "and hosts nothing, but it does not own the edge of the 48 canvas: its "
            "keyshape envelope sits inset (2 units on a long axis or `CIRCLE`, 4 on "
            "`SQUARE`, 6 on a short axis). It "
            "is always `semantic_role = \"MAIN\"`, `semantic_kind = \"noun\"`."
        ),
        "specifics": [
            "SOLO48 has four keyshapes: `CIRCLE`, `SQUARE`, `HRECT_L` and `VRECT_L`, "
            "with the visible-ink bounds in the table above. Older modules may still "
            "name `HRECT_XL`/`_M`/`_S` or `VRECT_XL`/`_M`/`_S`; on SOLO48 those resolve "
            "to the same bounds as `HRECT_L`/`VRECT_L`, so never choose one for new "
            "work. If an upright "
            "subject cannot fit, try a recognizable diagonal construction on "
            "the integer grid. If it still cannot fit, retain the validation "
            "findings and request the gallery's exception flag for manual review; "
            "record the reason and attempted fit. The flag is not a validation "
            "waiver or permission to leave the 48x48 canvas.",
            "Budget before drawing: the centerline box is 36x36 on `SQUARE` and 40x32 on "
            "`HRECT_L`/`VRECT_L`, and every gap between distinct parts costs 8 on "
            "centerlines. An interior mark between two walls needs a band of 16 between "
            "the wall centerlines, 17 if either wall is curved, because the engine cannot "
            "certify a curved pair sitting exactly on the minimum. If the band is short, "
            "change the keyshape or drop the part; never squeeze.",
            "Existing solo modules authored before 2026-09-13 were drawn to full-canvas "
            "envelopes (ink 0-48) and MIC 2, and many no longer validate. Run "
            "`validate_icon()` on any icon before imitating its coordinates; take "
            "construction ideas from a failing one, not numbers.",
            "Traced references: render first, then re-author on this grid. Reconstruct "
            "the subject, never the source's coordinates. Put arc centres on integer "
            "points and pick radii whose apex *is* the endpoint, so the arc reaches the "
            "keyshape edge exactly and cannot overshoot it.",
            "Split a wall where a part attaches so the two share an endpoint; declare "
            "the contact with `relate(\"connect\", ...)`. An arc merely touching a line is "
            "not proved as a connection and comes back `review`.",
            "Parallel straight edges inside the same contour must also meet the "
            "profile's ink clearance and centerline minimum. This is an exact blocking "
            "MIC check for positive overlapping runs, excluding adjacent segments and "
            "shared endpoints. Curved and near-parallel internal edges remain sampled advisories.",
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
            "A gap at the minimum needs exact straight distance or certified "
            "axis separation of enclosing geometry. Where a straight run has to hold a minimum gap, "
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

For any human subject or human part in a scene, first read
`{SHARED}/human-reference.md` and inspect the relevant files in
`icon_set/references/human_ref/`. These own human proportions and construction;
detached heads require exactly 4 units of visible head-to-body clearance.

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
   matching module for this family for reuse; for review changes create an independent variant instead of overwriting it.
   See `{SHARED}/naming.md`.

Before reduction, apply `{SHARED}/reference-triage.md`. If the reference is a
container combination or side combination, route to `/icon-making` to reject
it as one primitive and queue two component briefs. A Pending component brief
already specifies which single component to isolate. For review revisions,
preserve the parent and edit a new file from `create_variant.py`.

2. **Reduce.** Keep the smallest recognizable silhouette, the features that carry
   identity, and nothing that disappears at {spec.canvas_size} pixels. With a
   reference in scope, render it and look at it; read the subject, never the
   coordinates. See `{SHARED}/intake.md`.

   **Plan symbols before coordinates.** Read `{SHARED}/symbol-construction.md`.
   Identify typed shapes, nesting, repeated definitions/series, intended symmetry,
   and shared attachment points. Record a compact plan in the module; implement
   it with shared Python parameters and the existing geometry API. During repairs,
   change the owning symbol or repeat definition so joins and equality survive.

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
   original ID), `SOURCE_PATH` (the supplied source path) and `AUTHOR` (the
   model that drew it). Use `None` only for missing values; never discard an ID
   because the input also has a name. `AUTHOR` is never `None` and never
   guessed: name the model **you** are running as, in lowercase and hyphenated
   -- `astra-chatgpt` labels everything authored before this field existed, so
   use it only if that is you. If you do not know which model you are, ask
   rather than guess. Patching an existing module makes `AUTHOR` yours. Follow
   the UUID example, the author table and the patch lookup in
   `{SHARED}/naming.md`.

   ```python
   from ...keyshapes import Keyshape
   from ._base import {base}

   SOURCE_ICON_ID = "<exact-reference-id>"  # None only if no ID was supplied
   SOURCE_PATH = "<source-path>"  # None only if no path was supplied
   AUTHOR = "<your-model>"  # the model authoring this file; never None


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
  records the exact `SOURCE_ICON_ID`, `SOURCE_PATH` and an `AUTHOR` naming your
  own model. Existing matches are patched in place, with source metadata
  preserved or added and `AUTHOR` updated to you.
- Tests green; `build.py --family {family}` exits 0; the icon is in
  `icon_set/{row['dist']}/manifest.json`.
- `validate_icon()` is `valid` with no warnings.
- Reviewed at native size in both themes for smooth joins, consistent radii,
  balanced negative space, and symmetry wherever the subject supports it.
- State which Lucide construction informed the drawing, or that no useful match
  was found; explain any deliberate asymmetry.
- For human figures, name the shared human reference and verify its proportions
  and exact 4-unit detached head-to-body ink gap in the emitted geometry.
"""


def render_codex(content: str, source_skill: str = "icon-brief") -> str:
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
        f"Generated from .claude/skills/{source_skill}/SKILL.md by "
        "icon_set/scripts/generate_skills.py; edit the source, not this copy.",
    )
    return content.replace(
        "Request: $ARGUMENTS",
        "Use the user's request as the brief, including any supplied icon ID, "
        "reference paths, and output directory.\n\n"
        "Resolve repository paths and run commands from the `claude_skills` directory "
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
    if agent in ("all", "codex"):
        making = (SKILLS_DIR / "icon-making" / "SKILL.md").read_text(encoding="utf-8")
        outputs[CODEX_SKILLS_DIR / "icon-making" / "SKILL.md"] = render_codex(making, "icon-making")
        # Portable skills are generated from the same Codex text, not edited separately.
        for target, content in list(outputs.items()):
            if target.parent.parent == CODEX_SKILLS_DIR:
                outputs[REPO_ROOT / "skills" / target.parent.name / "SKILL.md"] = content
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
