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
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.scripts.workspace import DEFAULT_DIST
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
            "Use the profile-wide 4px stroke for every ordinary path. Do not set "
            "`STROKE_WIDTH = 2` or add `PATH_STROKE_WIDTHS` merely to rescue "
            "crowded detail, enlarge an opening, or force a 32px fit. Existing named "
            "compact exceptions remain scoped to their already approved records; do "
            "not create a new compact exception without explicit user approval.",
            "Intentional enclosed negative space is acceptable when it defines the "
            "concept. The triangular openings in Bluetooth and the inner opening of a "
            "crescent moon are reference examples: preserve their count, direction, "
            "and readable separation instead of filling, collapsing, or removing them "
            "just to avoid a hole finding. Verify each opening at native size in light "
            "and dark themes. If validation still flags an expected opening, report "
            "that finding honestly; visual acceptance of the hole does not waive an "
            "unrelated MIC, keyshape, or spacing failure.",
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
            "object, a badge), stop and use `/icon-solo`. For a wrapper component isolated "
            "from a hosted-icon combination, use `/icon-container`."
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
            "`SQUARE`, 6 on an `_L` short axis, 8 on an `_M` short axis). It "
            "is always `semantic_role = \"MAIN\"`, `semantic_kind = \"noun\"`."
        ),
        "specifics": [
            "SOLO48 has six keyshapes: `CIRCLE`, `SQUARE`, `HRECT_L`, `HRECT_M`, `VRECT_L` and `VRECT_M`, "
            "with the visible-ink bounds in the table above. Older modules may still "
            "name `HRECT_XL`/`_S` or `VRECT_XL`/`_S`; on SOLO48 those resolve "
            "to the same bounds as `HRECT_L`/`VRECT_L`, so never choose one for new "
            "work. The `_M` rectangles reduce only the short visible-ink side by 4: "
            "44x32 horizontal or 32x44 vertical. If an upright "
            "subject cannot fit, try a recognizable diagonal construction on "
            "the integer grid. If it still cannot fit, retain the validation "
            "findings and request the gallery's exception flag for manual review; "
            "record the reason and attempted fit. The flag is not a validation "
            "waiver or permission to leave the 48x48 canvas.",
            "Budget before drawing: centerline boxes are 36x36 on `SQUARE`, 40x32 on "
            "`HRECT_L`, 32x40 on `VRECT_L`, 40x28 on `HRECT_M`, and 28x40 on "
            "`VRECT_M`. Every gap between distinct parts costs 8 on "
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
            "and use `/icon-sub`. For a wrapper component isolated from a hosted-icon combination, use "
            "`/icon-container`."
        ),
    },
    "container": {
        "trigger": (
            "Use for a CONTAINER64 wrapper component isolated from an actual hosted-icon "
            "combination, or an explicitly requested container component. Empty standalone "
            "boards, screens, frames and speech bubbles with no separate icon inside use solo."
        ),
        "default_role": "MAIN",
        "default_kind": "noun",
        "default_category": "container",
        "job": (
            "A **container** is an explicitly requested wrapper component or the outer half of a "
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
            "If the reference is an empty standalone enclosure with no separate icon inside, use "
            "`/icon-solo`. If it is the thing that goes *inside*, use `/icon-sub`."
        ),
    },
    "avatar": {
        "trigger": "Use for a standalone user avatar, profile bust, or head-and-body portrait drawn at 48. A head and its own body form one natural subject.",
        "default_role": "MAIN",
        "default_kind": "noun",
        "default_category": "avatars",
        "job": "This is the specialized avatar skill for the **solo family**, not a separate family. An **avatar** combines a head and its own body into one standalone human subject. Author directly on 48x48; it hosts nothing and has no container content slot. Use `icon_set/references/human_ref/user.svg` for the circular head, rounded shoulders, and open bottom. The current avatar rule supersedes its detached layout: head ink touches body ink, with no visible gap.",
        "specifics": [
            "Avatar is a specialized authoring skill within the solo family, using SOLO48 and its six exact inset keyshapes: `CIRCLE` (44×44), `SQUARE` (40×40), `HRECT_L` (44×36), `HRECT_M` (44×32), `VRECT_L` (36×44), and `VRECT_M` (32×44). Fit the whole avatar, including head, hair/headwear and body, to that envelope. Use family `solo`, profile `SOLO48`, base `Solo48`, folder `model/icons/solo/`, and exports `published/solo48/`. Do not introduce an avatar family, profile, base class, registry folder, or export folder. Legacy `_XL` and `_S` rectangle size tokens resolve to their orientation's `_L` bounds and must not be chosen for new work.",
            "Center the head/face circle on the canvas vertical axis: head_cx = 24 on SOLO48. Measure the face itself, excluding hair, buns and hats; asymmetric accessories must not shift the face off-axis. Fit accessories within the keyshape by rebalancing them. For tall headwear, shorten the body and simplify clothing while preserving a circular face, curved shoulders and head/body contact.",
            "Read `HEAD_BODY_INK_GAP` and `HEAD_BODY_CENTERLINE_GAP` from this family's `._base`. These derive from `authoring.avatar.head_body_ink_gap` in the profile contract. Head ink must touch body ink: {avatar_gap} visible gap, or {avatar_centerline_gap} centerline separation for tangent stroke contact with stroke 4. Declare a scoped `connect` only for the actually touching head/body paths; keep the normal MIC for other separate parts. Derive `body_top = head_cy + head_radius + HEAD_BODY_CENTERLINE_GAP`; measure the nearest painted edges for angled poses.",
            "Body silhouettes must follow `human_ref/user.svg`: broad curved shoulders with smooth tangent joins and short rounded sides. Use arcs or coherent Bezier curves, not straight diagonal shoulders, trapezoids, or boxy sleeve outlines. Differentiate avatars with clothing, collars, seams, and natural arm poses while preserving that curved construction.",
            "For a set of avatars, plan one recognizable body cue per subject before drawing: an apron, wrap collar, coat fastening, scarf, or natural arm pose. Compare neighboring avatars at native size, especially those sharing similar heads. Do not reuse an identical generic torso for every named subject or invent arbitrary costume details just to make it different; retain the simple bust for a generic user.",
            "Budget the round head, touching shoulder junction, and torso together inside the inset keyshape. Keep hair/headwear within the same whole-avatar envelope. Leave enough torso height for broad readable clothing openings; simplify details instead of crowding collars, widening the gap, or replacing curved shoulders with angular clothing outlines.",
            "Head and body are natural parts of one avatar: do not split them into Pending component briefs. A separate badge, enclosure, or state modifier still follows the shared combination triage.",
            "Use the 48-unit keyshape table above and re-author the reference on the integer grid. The supplied user.svg uses the same 48x48 canvas; use its construction while fitting the chosen keyshape. Keep round caps, tangent shoulder curves, and coherent head/body proportions.",
            "Verify painted head/body contact in emitted geometry and record the measured zero gap. Face and jaw outlines must use circular arcs with equal radius_x and radius_y, or a full circle; do not stretch or flatten the face into an oval. Hair and headwear may retain subject-specific outlines. Never add false connect relationships or disable holes/pinches to obtain a pass.",
        ],
        "not_this": "For an isolated head or a full-body action scene intended at 48, use `/icon-solo`. For a wrapper component isolated from a hosted-icon combination, use `/icon-container`; for a hosted glyph, use `/icon-sub`.",
    },
}


# The new save family intentionally shares every solo drawing instruction.
FAMILY_TEXT["combination_main"] = {
    **FAMILY_TEXT["solo"],
    "trigger": "Use when asked to draw the main subject of an icon combination and save it in the icon combination main family, with the same drawing rules as solo.",
    "job": FAMILY_TEXT["solo"]["job"].replace(
        "A **solo** icon is one independently readable subject. It is never hosted and hosts nothing,",
        "An **icon combination main** is one independently readable main subject, saved separately for use in a combination. Draw only the main subject; it hosts nothing,"
    ),
    "specifics": [item.replace("SOLO48", "COMBINATION_MAIN48") for item in FAMILY_TEXT["solo"]["specifics"]],
}


# SYMBOL32 is now a separate registered family; it must not break generation
# of the existing authoring skills when the contracts enumerate all families.
FAMILY_TEXT["symbol"] = {
    **FAMILY_TEXT["sub"],
    "trigger": "Use when asked for an independently editable SYMBOL32 content symbol placed inside a container.",
    "job": "A **symbol** is content placed inside a container. Keep its Python source independent from its linked side sub-icon; use the SYMBOL32 profile and its contract values below.",
    "specifics": FAMILY_TEXT["sub"]["specifics"][:-1],
    "not_this": "For a side modifier, use /icon-sub. For a standalone subject, use /icon-solo. For a wrapper component isolated from a hosted-icon combination, use /icon-container.",
}


def skill_name(family: str) -> str:
    return "icon-" + family.replace("_", "-")


def render(family: str) -> str:
    bound_family = "solo" if family == "avatar" else family
    row = contracts.families()[bound_family]
    profile = Profile.for_family(bound_family)
    spec = profile.spec
    text = FAMILY_TEXT[family]
    folder = row["package"].rsplit("/", 1)[-1]
    dist = row["dist"].rsplit("/", 1)[-1]
    base = row["base_class"]
    region = _content_region()
    region_text = f"({region[0]},{region[1]})-({region[2]},{region[3]})"
    avatar_gap = contracts.icon_profile()["authoring"]["avatar"]["head_body_ink_gap"]
    human_gap = avatar_gap if family == "avatar" else 4
    fmt = {"shared": SHARED, "slot": region_text,
           "avatar_gap": avatar_gap, "avatar_centerline_gap": avatar_gap + 4}
    others = [f for f in contracts.families() if f != bound_family]
    other_lines = "\n".join(
        f"- `/{skill_name(other)}` — {other} family, "
        f"`{contracts.families()[other]['profile']}`, "
        f"{Profile.for_family(other).spec.canvas_size}×{Profile.for_family(other).spec.canvas_size}"
        for other in others
    )
    specifics = "\n".join(f"- {item.format(**fmt)}" for item in text["specifics"])
    module_example = f"icon_set/model/icons/{folder}/<icon_id_with_underscores>.py"
    guide_l, guide_t, guide_r, guide_b = spec.interior_guide_bounds
    cx, cy = spec.center

    revision_rule = (
        "matching module in place, including review corrections. Preserve its icon_id, filename, and source metadata; create a variant only when the user explicitly requests alternatives."
        if family == "avatar" else
        "matching module for this family for reuse; for review changes create an independent variant instead of overwriting it."
    )
    revision_handoff = (
        "already specifies which single component to isolate. For avatar corrections,\n"
        "update the original module and rebuild its SVG, PNG, manifest and review previews.\n"
        "Do not leave a v2 beside an outdated original unless alternatives were requested."
        if family == "avatar" else
        "already specifies which single component to isolate. For review revisions,\n"
        "preserve the parent and edit a new file from `create_variant.py`."
    )
    release_check = ""
    if family == "avatar":
        release_check = """
   **Check the exported stroke too.** `validate_icon()` covers vector rules;
   it does not establish that holes/pinches pass. Run the release checker:

   ```python
   from icon_set.validation.library_qa import inspect_icon
   qa = inspect_icon(create("<icon-id>"))
   print(qa["status"], qa["errors"], qa["warnings"])
   print(qa["negative_space"])
   ```

   Require `status == "pass"`, no errors/warnings, and passing negative-space
   checks, including authored-stroke holes. Thinning a stroke can open a tiny
   trapped pocket and hide it inside a larger region; inspect the actual
   4-unit SVG stroke, especially fringe/crown junctions, lapels and collars.
   Enlarge or rebalance a failing opening. Do not ink it over, weaken the
   threshold, or assume a minimum-spacing pass proves the hole is safe.
"""
    test_command = (
        "python3 -m unittest icon_set.tests.test_avatar icon_set.tests.test_profiles_keyshapes"
        if family == "avatar" else "python3 -m unittest discover -s icon_set/tests -t ."
    )
    preview_options = " --category avatars" if family == "avatar" else ""
    build_options = " --icon icon_set/model/icons/solo/<module_filename>.py --no-report" if family == "avatar" else ""
    light_preview = (
        "   python3 icon_set/scripts/contact_sheet.py --family solo --category avatars --theme light --png /tmp/avatar-light.png\n"
        if family == "avatar" else ""
    )
    build_note = (
        "   Replace `<module_filename>` with the original avatar module; repeat `--icon`\n"
        "   for a batch. This rebuilds those solo icons; `--no-report` skips only\n"
        "   the library-wide report, not release validation. If shared validation code\n"
        "   changes, run its relevant regression tests too. Report unrelated test failures\n"
        "   separately; do not claim the entire suite passed.\n\n"
        if family == "avatar" else ""
    )
    avatar_done = (
        '- Release QA passes, including holes measured at the actual 4-unit stroke; report its result separately from vector validation.\n'
        '- Named avatars have recognizable body cues while retaining curved reference shoulders; compare the set at native size.\n'
        if family == "avatar" else ""
    )

    reference_fidelity = """
## Reference fidelity comes first

**Library-wide user policy:** Read `icon_set/skills/icon-design/sub-reference-policy.md`.
Every authored sub output must use the plain SUB32 profile: a 32×32 canvas,
`viewBox="0 0 32 32"`, and 4px strokes throughout. These are hard limits,
including for reference recreations. Preserve the source's defining parts and
relationships by redrawing at this size. If they cannot fit, mark the source
SKIP with review evidence; do not publish a larger or thinner-stroked sub icon.

**Exact resize mode:** If the user explicitly requests the original unchanged,
only resized, preserve it as a reference artifact, separate from the authored
sub library. Label it an exact resized original, not a validated SUB32 model.
Check every source/output pair for unchanged SVG content apart from display
dimensions and identical renders at 32px and an enlarged size. Show the complete
result as the primary gallery image; retain extracted or simplified earlier
versions only as superseded comparisons. Never retain a “keep” verdict merely
because an altered drawing remains recognizable under an exact-match request.

When recreating a supplied original, the deliverable is the **complete original
composition** unless the user explicitly asks to extract a named component.
Preserve every visible part: outline circles, frames, badges, secondary symbols,
text, repeated marks, holes, and their relative positions, directions and counts.
An enclosing circle can carry meaning; never assume it is decoration.

This rule takes precedence over reduction, family routing, shared reference
triage, and component-only Pending briefs below. A generated brief saying
"exclude Circle Frame" is not user authorization to remove it. Reopen the
original and correct that brief before drawing. Internal decomposition may help
construction, but the delivered result must recombine every part. Do not count
several extracted components as several completed original icons.

Before drawing, inventory all source parts. After drawing, compare the whole
original and result side by side at native and enlarged sizes, checking every
part, layout, count, opening and directional cue. Use reference-supported
geometry; do not replace an entire composition with a generic canonical mark.
Typeface reuse must preserve the original text and its position in the complete
composition; a text-only export does not replace a text-and-symbol original.

If the complete design cannot meet SUB32 spacing and stroke rules, retain all
parts in the reference and mark that original SKIP with a specific reason and
saved review evidence. Keep the requested 32px canvas and 4px stroke; do not
remove parts, enlarge the canvas or thin strokes to force completion. Continue
with the next drawable original. Never count a skipped source as generated.
For every authored result, run
`python3 icon_set/scripts/fix_icon_sub.py check --icon <icon-id>` and require a
strict-32 pass before reporting it done. This checks the emitted SVG root,
every stroke width, keyshape, and the full no-warning QA gate. A regular
`validate_icon()` pass on an expanded canvas is insufficient.
Record skips by source UUID in the batch audit and primitive status, and flag
any earlier incomplete generated variants for review without deleting them.
Do not weaken a validator or label an incomplete output SUB32-compliant.
A reference copy or lossless re-export can be useful comparison evidence, but
must be labelled as such, never claimed as a newly redrawn icon.

For review corrections, preserve the earlier variant and provide a new complete
variant linked to its exact source UUID. Completion requires both profile checks
for the chosen output and a source-part coverage check; a numeric pass alone
cannot approve an incomplete recreation.

""" if family == "sub" else ""

    parallel_note = (
        "For SUB32 parallel straight strokes, the same 2px visible ink gap means "
        "at least 6px between their centerlines. The 4px stroke width is included "
        "in that distance.\n\n"
        if family == "sub" else ""
    )

    return f"""---
name: {skill_name(family)}
description: Author a {bound_family}-family {"avatar" if family == "avatar" else "icon"} for the Pictographic icon set on the {row['profile']} profile ({spec.canvas_size}x{spec.canvas_size}). {text['trigger']} Generated from the contracts by icon_set/scripts/generate_skills.py; do not edit by hand.
argument-hint: <icon-id> — <one-sentence brief> [references: <paths>]
---

# /{skill_name(family)} — one {family} icon on `{row['profile']}`

Request: $ARGUMENTS
{reference_fidelity}
**Text and numbers:** follow `{SHARED}/typeface.md` and reuse the existing
glyphs in `icon_set/typeface/glyphs.json`. Do not invent new letter/number
geometry, including text components in combined icons or Pending briefs.
This routing rule takes precedence over the primitive-authoring workflow below.

This skill authors **exactly one family**. Everything below is fixed by the
family and read from `icon_set/model/contracts/icon-profile.v1.json`:

| | |
|---|---|
| Family | `{bound_family}` |
| Profile | `{row['profile']}` |
| Canvas | {spec.canvas_size}×{spec.canvas_size}, centre ({cx},{cy}), integer grid 1, stroke 4, round caps and joins |
| Module goes in | `icon_set/model/icons/{folder}/` — one file per icon |
| Subclass | `{base}` from `._base` |
| Ships to | `{DEFAULT_DIST.relative_to(REPO_ROOT).as_posix()}/{dist}/` with its own `manifest.json` |
| Ink clearance (MIC) | {spec.mic} between distinct parts = **{spec.equal_stroke_centerline_min} between centerlines** |
| Interior guide | ({guide_l},{guide_t})-({guide_r},{guide_b}) — constrains inner detail only |
| Existing icons to imitate | {("`user-avatar`, `woman-store-clerk-3-avatar`, `boxer-avatar`" if family == "avatar" else _examples("solo" if family == "combination_main" else family))} |

{parallel_note}{text['job'].format(**fmt)}

**Wrong family? Stop.** {text['not_this']} {"An" if family == "avatar" else "A"} {family} icon cannot be authored on
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
{('avatar heads touch the body with zero visible gap and use circular face arcs.' if family == 'avatar' else 'detached heads require exactly 4 units of visible head-to-body clearance.')}{(chr(10) + 'For each stick figure, call `self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")` after creating those parts. The head flag names its outline primitive or contour; the torso flag names the upper torso primitive, with `start` or `end` identifying its actual neck junction. Use a unique figure ID for each person. The required gap is exactly 8 units between stroke centerlines / 4 units between ink edges. See the shared human reference for the full example and measurement rules. These flags support future validation; they do not certify spacing or declare contact.' if family in ('solo', 'combination_main') else '')}

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
   {revision_rule}
   See `{SHARED}/naming.md`.

Before reduction, apply `{SHARED}/reference-triage.md`. If the reference is a
container combination or side combination, route to `/icon-making` to reject
it as one primitive and queue two component briefs. A Pending component brief
{revision_handoff}

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
{release_check}
6. **Family-specific checks.**

{specifics}

7. **Build and look.**

   ```bash
   {test_command}
   python3 icon_set/scripts/build.py --family {bound_family}{build_options}
{light_preview}   python3 icon_set/scripts/contact_sheet.py --family {bound_family}{preview_options} --theme dark --png /tmp/{family}.png
   ```

{build_note}   Open the PNG and judge it at {spec.canvas_size} pixels. Numeric success is not
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
- Tests green; `build.py --family {bound_family}` exits 0; the icon is in
  `{DEFAULT_DIST.relative_to(REPO_ROOT).as_posix()}/{dist}/manifest.json`.
- `validate_icon()` is `valid` with no warnings.
{avatar_done}- Reviewed at native size in both themes for smooth joins, consistent radii,
  balanced negative space, and symmetry wherever the subject supports it.
- State which Lucide construction informed the drawing, or that no useful match
  was found; explain any deliberate asymmetry.
- For human figures, name the shared human reference and verify its proportions
  and {('zero-gap head/body contact and circular face arcs' if family == 'avatar' else 'exact 4-unit detached head-to-body ink gap')} in the emitted geometry.
"""


def render_primitive_fix() -> str:
    """/primitive-fix-thuan: the production claim and upload around /primitive-make-ray."""
    return (
        "---\n"
        "name: primitive-fix-thuan\n"
        "argument-hint: <count> [--offset N] [--disapprove-status bad-stroke|meaning|manual-fix-request|other] [--worker name]\n"
        "description: Claim a number of disapproved Pictographic solo icons from the shared production fix "
        "queue, redraw each one by running /primitive-make-ray on its original reference with the reviewer's "
        "feedback, upload the before and after drawings to production and report done or cannot-fix. "
        "Arguments: count, optional --offset, --disapprove-status and --worker. Generated from the contracts "
        "by icon_set/scripts/generate_skills.py; do not edit by hand.\n"
        "---\n\n"
        "# /primitive-fix-thuan — claim, redraw with /primitive-make-ray, upload\n\n"
        "Arguments: $ARGUMENTS\n\n"
        "This skill does **only the production part** of a fix: claim the icons, hand each one to\n"
        "/primitive-make-ray, then upload the result and report it. All drawing, validation and\n"
        "export rules are /primitive-make-ray's; do not author or repair geometry any other way.\n\n"
        "Run from the repository containing `icon_set/`. The first number in the arguments is the\n"
        "**count** of icons to claim (required; ask when it is missing). `--offset N` skips that many\n"
        "claimable icons, `--disapprove-status` keeps one disapproval reason (`bad-stroke`, `meaning`,\n"
        "`manual-fix-request`, `other`). The **worker name** identifies your machine on every call and is\n"
        "**required**: take it from `--worker`, else from `$PICTOGRAPHIC_WORKER`; if neither is set, ask\n"
        "the user for it (for example `thuan-mac`) before claiming anything. Never invent one from the\n"
        "hostname, and never reuse a name you saw in the queue; the scripts refuse to run without it.\n\n"
        "## 1. Claim\n\n"
        "```bash\n"
        "python3 icon_set/scripts/primitive_fix.py start --worker <name> --limit <count> [--offset N] [--disapprove-status R]\n"
        "```\n\n"
        "It claims the icons on production (so no other machine fixes them), creates one fix directory\n"
        "per icon at `icon_set/work/primitive-fix-thuan/<icon-key>/<run-id>/` with `brief.txt`,\n"
        "`claim.json`, a `before/` copy of the registered module and the displayed SVG, and\n"
        "`reference/<concept>_<source-uuid>.svg` (the original reference), uploads the before drawing to\n"
        "production, and prints one block per icon: the icon key, the **reference** path, the `before/`\n"
        "folder, the disapproval reason and the reviewer's **feedback**. Exit code 3 means nothing was\n"
        "claimable: report that and stop.\n\n"
        "## 2. Redraw with /primitive-make-ray\n\n"
        "For each block, run /primitive-make-ray on its **reference** path and follow that skill\n"
        "completely. Two additions for a fix:\n\n"
        "- The reviewer's feedback is the specification for the revision, and `before/<icon-id>.svg` is\n"
        "  the drawing they rejected; look at both before drawing. Keep the `icon_id` of the block.\n"
        "- This is a revision: author a **fresh** run even when an earlier\n"
        "  `icon_set/work/primitive-make-ray/<source-uuid>/*/result.json` exists; that skip rule does not\n"
        "  apply here.\n\n"
        "Note the new `RESULT_DIR` it creates. A block whose reference line says `none` cannot go through\n"
        "/primitive-make-ray: finish it as cannot-fix.\n\n"
        "## 3. Upload and report\n\n"
        "When the /primitive-make-ray run is valid with zero warnings:\n\n"
        "```bash\n"
        "python3 icon_set/scripts/primitive_fix.py finish --worker <name> --icon <icon-key> --run <make-ray RESULT_DIR> --outcome done --note \"<what changed>\"\n"
        "```\n\n"
        "`finish` loads the module from that run, validates it again, writes `after/` (module, SVG,\n"
        "light/dark previews), `validation.txt` and `result.json` in the fix directory, uploads the after\n"
        "drawing, module and validation to production, and reports **done**: the revision returns to\n"
        "Ready for the reviewer. It refuses `done` (exit 2, nothing uploaded or reported) while the model\n"
        "is invalid or has warnings; go back to /primitive-make-ray. When no meaning-preserving drawing\n"
        "can pass, report instead (add `--run` when a run exists so its attempt is uploaded):\n\n"
        "```bash\n"
        "python3 icon_set/scripts/primitive_fix.py finish --worker <name> --icon <icon-key> [--run <make-ray RESULT_DIR>] --outcome cannot-fix --note \"<the blocking check and element>\"\n"
        "```\n\n"
        "The icon stays **Disapproved** with your worker name and note; reviewers find it with the Cannot\n"
        "fix filter.\n\n"
        "## 4. Report\n\n"
        "For every claimed icon say the key, what the feedback asked for, the /primitive-make-ray\n"
        "`RESULT_DIR` and its SVG, the validation status, and the outcome reported (done or cannot-fix).\n\n"
        "## Never\n\n"
        "- Fix an icon you did not claim, or claim more than the requested count.\n"
        "- Edit registered modules, build, publish or push; the fix lives in the /primitive-make-ray\n"
        "  run and is promoted separately.\n"
        "- Report `done` without `finish`, or change the production status through `/api/reviews`.\n"
        "- Leave a claimed icon without a `finish` call (done or cannot-fix).\n"
    )


def render_codex(content: str, source_skill: str = "icon-brief") -> str:
    """Adapt host syntax while retaining the shared authoring instructions."""
    content = "\n".join(
        line for line in content.split("\n")
        if not line.startswith("argument-hint:")
    )
    # `skills/icon-design` is a real path, not a skill invocation.
    content = content.replace("skills/icon-design", "\0")
    content = re.sub(r"(?<![\w./-])/icon-", "$icon-", content)
    content = content.replace("\0", "skills/icon-design")
    content = content.replace(
        "Queue offset argument: $ARGUMENTS",
        "Read the queue offset from the user's skill invocation or request.",
    )
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
        "`$icon-solo`, `$icon-combination-main`, `$icon-avatar`, or `$icon-container`; in ChatGPT, select the skill with `@`. "
        "Treat slash-style handoffs in generated briefs as references to the "
        "corresponding skill.",
    )


def _swap(content: str, old: str, new: str, *, regex: bool = False) -> str:
    """Replace exactly once, failing loudly when the source skill text has drifted."""
    if regex:
        result, count = re.subn(old, lambda _: new, content, count=1, flags=re.DOTALL | re.MULTILINE)
    else:
        count = content.count(old)
        result = content.replace(old, new, 1)
    if count != 1:
        raise ValueError(f"side-sub-make-thuan: expected one match for {old[:60]!r}, found {count}")
    return result


def render_side_sub() -> str:
    """The icon-sub workflow on the next missing side sub, saved to a standalone folder."""
    root = "icon_set/work/side-sub-make-thuan/"
    content = render("sub")
    content = "\n".join(line for line in content.split("\n") if not line.startswith("argument-hint:"))
    content = _swap(content, "name: icon-sub\n", "name: side-sub-make-thuan\n")
    content = _swap(content, "# /icon-sub —", "# /side-sub-make-thuan —")
    content = _swap(
        content, r"^description: [^\n]*",
        "description: Retrieve the next missing side-combination sub (gallery side-subs page) "
        "without parameters and author it as a Pictographic SUB32 icon exactly like its "
        "reference, with no classification or routing. Save results and retrieval metadata "
        "in a standalone folder without gallery updates. Generated from the contracts by "
        "icon_set/scripts/generate_skills.py; do not edit by hand.", regex=True)
    content = _swap(
        content, "Request: $ARGUMENTS",
        "Invoke this skill without parameters. Run from the repository containing `icon_set/`.\n\n"
        "Retrieve the next missing side-combination sub (the Missing bucket of "
        "`gallery/side-subs.html`: no drawing yet, not marked text/number) by running this "
        "command without parameters:\n\n"
        "```bash\npython3 icon_set/scripts/next_side_sub.py\n```\n\n"
        "Use its output as the brief, including the source ID and reference path, then "
        "follow the full authoring workflow below.\n\n"
        f"**Folder-only output:** create a fresh result directory at `{root}"
        "<source-uuid>/<unique-run-id>/`. Call it `RESULT_DIR` below. Store all source, "
        "exports, reference renders, previews, retrieval metadata and findings there, "
        "including unsuccessful attempts. Never overwrite an earlier run. Do not write to "
        "`published/`, the registered icon folders, metadata catalogs, contracts, galleries, "
        "queues or runtime state. Do not run build, compose, finish-icon, publish, release or "
        "gallery update commands. This output rule overrides output and registration advice "
        "in shared guides. The next-side-sub helper skips a source UUID once a run contains "
        "an authored Python module and a readable result.json with that source_uuid. "
        "Validation failures, warnings, and failed exports still count as attempts; do not "
        "retry them automatically. Write result.json last, including failures. Only attempts "
        "without a saved result remain eligible for automatic retry. If retrieval fails or no "
        "missing side sub remains, report that result and stop.")
    content = _swap(
        content, r"## Reference fidelity comes first.*?(?=This skill authors)",
        "**Draw the reference as it is:** author the retrieved sub `reference` as one SUB32 "
        "icon that follows the reference. Do not classify, triage, route, skip or split it "
        "into component briefs. Preserve every visible part of the reference: frames, "
        "badges, secondary marks, holes, and their positions, directions and counts. The "
        "`combination context` SVGs only show how this sub sits beside its main; never draw "
        "that main. Inventory the reference parts before drawing, and afterwards compare "
        "reference and result side by side at native and enlarged sizes.\n\n"
        "Keep the strict 32×32 canvas and the 4px stroke: side combinations need a sub that "
        "passes SUB32 as is. Do not enlarge the canvas, thin strokes, or produce an exact "
        "resized original. If the complete reference cannot pass, keep every part, save the "
        "validation findings and attempted fit in RESULT_DIR, and record the failure in "
        "result.json; do not drop parts to force a pass.\n\n"
        "Letters or digits inside the reference: reuse the matching glyphs in "
        "`icon_set/typeface/glyphs.json` when they fit the reference; hand-author them only "
        "when needed to preserve the reference's shape. These scope and text rules override "
        "routing, skip and typeface restrictions in the shared guides. All SUB32 geometry "
        "and validation requirements still apply.\n\n", regex=True)
    content = _swap(
        content, r"A \*\*sub\*\* icon is read small.*?(?=## Visual priorities)",
        "Every input stays in `RESULT_DIR/` and subclasses `Sub32`. Modifiers, states and "
        "verbs declare `semantic_role = \"SUB\"`; a simple noun shape (`heart`, `star`) "
        "declares `MAIN` with `semantic_kind = \"noun\"`. Keep the complete reference on "
        "the 32×32 canvas; do not reroute it to another family or enlarge the canvas.\n\n",
        regex=True)
    content = _swap(
        content,
        "   Search existing Python files by that ID before creating a new file; patch the\n"
        "   matching module for this family for reuse; for review changes create an independent variant instead of overwriting it.",
        "   Inspect existing Python files by that ID for context, but author a new\n"
        "   standalone module inside this run's RESULT_DIR; do not patch registered originals.")
    content = _swap(
        content, r"Before reduction, apply .*?(?=2\. \*\*Reduce\.)",
        "Inspect the complete reference before reduction, then glance at the (at most two) "
        "combination-context SVGs to confirm which part is the sub. Draw only the reference; "
        "do not reject, reroute or split it. For revisions, preserve the parent and author "
        "the revised module in a fresh result directory.\n\n", regex=True)
    content = _swap(content, "`icon_set/model/icons/sub/` — one file per icon", "`RESULT_DIR/` — one file per icon")
    content = _swap(content, "`icon_set/model/icons/sub/<icon_id_with_underscores>.py`",
                    "`RESULT_DIR/<icon_id_with_underscores>.py`")
    content = _swap(
        content,
        f"| Ships to | `{DEFAULT_DIST.relative_to(REPO_ROOT).as_posix()}/sub32/` with its own `manifest.json` |",
        "| Exports to | `RESULT_DIR/` only; no gallery or manifest updates |")
    content = _swap(content, "`Sub32` from `._base`", "`Sub32` from `icon_set.model.icons.sub._base`")
    content = _swap(content, "from ...keyshapes import Keyshape\n   from ._base import Sub32",
                    "from icon_set.model.keyshapes import Keyshape\n   from icon_set.model.icons.sub._base import Sub32")
    content = _swap(
        content, "   Nothing to register. The folder is the registry.",
        "   Keep the module outside the registry. Load it by file path with\n"
        "   `importlib.util.spec_from_file_location` from the repository root\n"
        "   and instantiate its authored class directly.")
    content = _swap(
        content,
        '   from icon_set.model.icons.registry import create\n   report = create("<icon-id>").validate_icon()',
        "   icon = module.<ClassName>()  # module loaded from RESULT_DIR\n   report = icon.validate_icon()")
    content = _swap(
        content,
        "A new 4-unit-axis glyph needs its own record in `icon_set/model/contracts/exceptions.v1.json` with `status: \"proposed\"`; see `icon_set/skills/icon-design/keyshape-fitting.md`.",
        "A new 4-unit-axis glyph needs a proposed record; write the proposal into result.json instead of editing `icon_set/model/contracts/exceptions.v1.json`, and report it. See `icon_set/skills/icon-design/keyshape-fitting.md`.")
    content = _swap(content, "opening, rebalance, remove the part — never squeeze.",
                    "opening, rebalance — never squeeze or remove a reference part.")
    content = _swap(
        content, r"- After it validates, prove it composes: .*?\n",
        "- The module is not registered, so skip `compose.py`; the result is judged on its own at 32 pixels.\n",
        regex=True)
    content = _swap(
        content, r"7\. \*\*Build and look\.\*\*.*?(?=8\. \*\*Report\.)",
        "7. **Export locally and look.**\n\n"
        "   Save `icon.to_svg()` as `RESULT_DIR/<icon-id>.svg` and\n"
        "   save the retrieval metadata beside it as `RESULT_DIR/<icon-id>.metadata.json`.\n"
        "   Preserve the helper's concept, source UUID, reference path, category,\n"
        "   `aliases`, `uses` and `combination_context` (a list of the context lines) as\n"
        "   `concept`, `source_uuid`, `reference_path`, `category`, `aliases`, `uses` and\n"
        "   `combination_context`. Keep the exact strings; do not substitute inferred values.\n"
        "   Include the complete original stdout as `retrieval_stdout` to retain\n"
        "   any additional fields, and stderr warnings as `retrieval_stderr`.\n"
        "   Write this JSON as soon as retrieval succeeds, even if drawing fails.\n"
        "   Save\n"
        "   `report.describe()` as `RESULT_DIR/validation.txt`. Render that SVG\n"
        "   directly with CairoSVG into light and dark PNGs at native 32px and\n"
        "   enlarged size, all inside RESULT_DIR. Inspect both themes. Save a\n"
        "   `result.json` containing source UUID/path, icon ID, author, validation\n"
        "   status, visual-review findings, reference-part coverage, omissions and\n"
        "   artifact filenames. Retain invalid candidates with their failure findings;\n"
        "   do not claim they passed. If validation or rendering raises, retain the\n"
        "   source and save the error in this same folder. No library build is needed.\n\n",
        regex=True)
    content = _swap(
        content,
        "Existing matches are patched in place, with source metadata\n  preserved or added and `AUTHOR` updated to you.",
        "Source metadata is preserved in the standalone result module;\n  earlier runs and registered originals remain unchanged.")
    content = _swap(
        content,
        "- Tests green; `build.py --family sub` exits 0; the icon is in\n"
        f"  `{DEFAULT_DIST.relative_to(REPO_ROOT).as_posix()}/sub32/manifest.json`.",
        "- Source, SVG, matching retrieval metadata JSON, previews, validation findings\n"
        "  and result.json are saved\n"
        "  together in RESULT_DIR; link this directory and its SVG in the final response.\n"
        "- No gallery, published output, registry, contract, queue or runtime-state updates.\n"
        "- Every visible part of the reference is present on the 32×32 canvas with the 4px stroke.")
    return content


def write_all(check_only: bool = False, agent: str = "all", skill: str | None = None) -> int:
    stale = []
    outputs = {}
    for family in [*contracts.families(), "avatar"]:
        if skill is not None and skill != skill_name(family):
            continue
        content = render(family)
        if agent in ("all", "claude"):
            outputs[SKILLS_DIR / skill_name(family) / "SKILL.md"] = content
        if agent in ("all", "codex"):
            outputs[CODEX_SKILLS_DIR / skill_name(family) / "SKILL.md"] = render_codex(content)
    # Reuse solo construction, with Ray's queue intake and all-input scope.
    if skill in (None, "primitive-make-ray", "side-main-make-thuan"):
        content = render("solo").replace(
            "name: icon-solo\n", "name: primitive-make-ray\n", 1
        ).replace("# /icon-solo —", "# /primitive-make-ray —", 1)
        content = "\n".join(
            line for line in content.split("\n")
            if not line.startswith("argument-hint:")
        ).replace(
            "Request: $ARGUMENTS",
            "Invoke this skill without parameters. Run from the repository containing `icon_set/`.\n\n"
            "Retrieve the next TODO icon by running this command without parameters:\n\n"
            "```bash\npython3 icon_set/scripts/next_icon.py\n```\n\n"
            "Use its output as the brief, including the source ID and reference path, "
            "then follow the full authoring workflow below. If retrieval fails or no "
            "TODO icon remains, report that result and stop.",
        )
        content = re.sub(
            r"^description: .*",
            "description: Retrieve the next TODO reference without parameters and author "
            "its complete composition as a Pictographic SOLO48 icon, including text, "
            "digits, logos, symbols, avatars, wrappers and combinations. Save results "
            "and retrieval metadata in a standalone folder without gallery updates. Generated from "
            "the contracts by icon_set/scripts/generate_skills.py; do not edit by hand.",
            content, count=1, flags=re.MULTILINE,
        )
        content = re.sub(
            r"\*\*Text and numbers:\*\*.*?(?=This skill authors)",
            "**Generate every input:** author the complete retrieved reference as one "
            "SOLO48 icon. Do not skip, split into component briefs, or hand off because "
            "it contains text, digits, a logo, a symbol, an avatar, an enclosure or a "
            "combination. Preserve its defining features and arrangement.\n\n"
            "Letters and digits may be hand-authored to preserve the reference's "
            "distinctive shape, including outlined or three-dimensional forms. "
            "Existing typeface glyphs are optional construction references, not a "
            "required substitute. These scope and text rules override routing and "
            "typeface restrictions in the shared guides. All SOLO48 geometry and "
            "validation requirements still apply.\n\n",
            content, count=1, flags=re.DOTALL,
        )
        content = re.sub(
            r"A \*\*solo\*\* icon.*?(?=## Visual priorities)",
            "Every input stays in `icon_set/model/icons/solo/`, subclasses `Solo48`, "
            "and uses `semantic_role = \"MAIN\"`, `semantic_kind = \"noun\"`. "
            "Keep the complete composition on the 48×48 canvas; do not reroute it "
            "to another family or enlarge the canvas.\n\n",
            content, count=1, flags=re.DOTALL,
        )
        content = re.sub(
            r"Before reduction, apply .*?(?=2\. \*\*Reduce\.)",
            "Inspect the complete reference before reduction. Treat its text, "
            "enclosure, main subject and modifiers as parts of the requested "
            "composition; do not reject or split combinations. For review revisions, "
            "preserve the parent and edit a new file from `create_variant.py`.\n\n",
            content, count=1, flags=re.DOTALL,
        )
        content = content.replace(
            "then follow the full authoring workflow below.",
            "then follow the full authoring workflow below.\n\n"
            "**Folder-only output:** create a fresh result directory at "
            "`icon_set/work/primitive-make-ray/<source-uuid>/<unique-run-id>/`. "
            "Call it `RESULT_DIR` below. Store all source, exports, reference renders, "
            "previews, retrieval metadata and findings there, including unsuccessful attempts. Never "
            "overwrite an earlier run. Do not write to `published/`, the registered "
            "icon folders, metadata catalogs, galleries, queues or runtime state. "
            "Do not run build, finish-icon, publish, release or gallery update commands. "
            "This output rule overrides output and registration advice in shared guides. "
            "The next-icon helper skips a source UUID once a run contains an authored "
            "Python module and a readable result.json with that source_uuid. "
            "Validation failures, warnings, and failed exports still count as attempts; "
            "do not retry them automatically. Write result.json last, including failures. "
            "Only attempts without a saved result remain eligible for automatic retry.",
        )
        content = content.replace("icon_set/model/icons/solo/", "RESULT_DIR/")
        content = content.replace(
            f"| Ships to | `{DEFAULT_DIST.relative_to(REPO_ROOT).as_posix()}/solo48/` with its own `manifest.json` |",
            "| Exports to | `RESULT_DIR/` only; no gallery or manifest updates |",
        ).replace("`Solo48` from `._base`", "`Solo48` from `icon_set.model.icons.solo._base`")
        content = content.replace(
            "   Search existing Python files by that ID before creating a new file; patch the\n"
            "   matching module for this family for reuse; for review changes create an independent variant instead of overwriting it.",
            "   Inspect existing Python files by that ID for context, but author a new\n"
            "   standalone module inside this run's RESULT_DIR; do not patch registered originals.",
        ).replace(
            "For review revisions, preserve the parent and edit a new file from `create_variant.py`.",
            "For revisions, preserve the parent and author the revised module in a fresh result directory.",
        ).replace(
            "from ...keyshapes import Keyshape\n   from ._base import Solo48",
            "from icon_set.model.keyshapes import Keyshape\n   from icon_set.model.icons.solo._base import Solo48",
        ).replace(
            "   Nothing to register. The folder is the registry.",
            "   Keep the module outside the registry. Load it by file path with\n"
            "   `importlib.util.spec_from_file_location` from the repository root\n"
            "   and instantiate its authored class directly.",
        ).replace(
            '   from icon_set.model.icons.registry import create\n   report = create("<icon-id>").validate_icon()',
            "   icon = module.<ClassName>()  # module loaded from RESULT_DIR\n   report = icon.validate_icon()",
        ).replace(
            "retain the validation findings and request the gallery's exception flag for manual review; record the reason and attempted fit. The flag is not a validation waiver or permission to leave the 48x48 canvas.",
            "save the validation findings and attempted fit in RESULT_DIR for manual review. "
            "Do not request a gallery flag, waive validation, or leave the 48x48 canvas.",
        )
        content = re.sub(
            r"7\. \*\*Build and look\.\*\*.*?(?=8\. \*\*Report\.)",
            "7. **Export locally and look.**\n\n"
            "   Save `icon.to_svg()` as `RESULT_DIR/<icon-id>.svg` and\n"
            "   save the retrieval metadata beside it as `RESULT_DIR/<icon-id>.metadata.json`.\n"
            "   Preserve the helper's concept, source UUID, reference path, category,\n"
            "   and optional brief as `concept`, `source_uuid`, `reference_path`,\n"
            "   `category`, and `brief` (null when absent). Keep the exact strings,\n"
            "   including multiline brief content; do not substitute inferred values.\n"
            "   Include the complete original stdout as `retrieval_stdout` to retain\n"
            "   any additional fields, and stderr warnings as `retrieval_stderr`.\n"
            "   Write this JSON as soon as retrieval succeeds, even if drawing fails.\n"
            "   Save\n"
            "   `report.describe()` as `RESULT_DIR/validation.txt`. Render that SVG\n"
            "   directly with CairoSVG into light and dark PNGs at native 48px and\n"
            "   enlarged size, all inside RESULT_DIR. Inspect both themes. Save a\n"
            "   `result.json` containing source UUID/path, icon ID, author, validation\n"
            "   status, visual-review findings, omissions and artifact filenames.\n"
            "   Retain invalid candidates with their failure findings; do not claim\n"
            "   they passed. If validation or rendering raises, retain the source and\n"
            "   save the error in this same folder. No library build is needed.\n\n",
            content, count=1, flags=re.DOTALL,
        )
        content = content.replace(
            "Existing matches are patched in place, with source metadata\n  preserved or added and `AUTHOR` updated to you.",
            "Source metadata is preserved in the standalone result module;\n  earlier runs and registered originals remain unchanged.",
        ).replace(
            "- Tests green; `build.py --family solo` exits 0; the icon is in\n"
            f"  `{DEFAULT_DIST.relative_to(REPO_ROOT).as_posix()}/solo48/manifest.json`.",
            "- Source, SVG, matching retrieval metadata JSON, previews, validation findings\n"
            "  and result.json are saved\n"
            "  together in RESULT_DIR; link this directory and its SVG in the final response.\n"
            "- No gallery, published output, registry, queue or runtime-state updates.",
        )
        # Ray takes explicit reference files (batched in TASKS.md) instead of the next-icon
        # helper, so parallel tasks never draw the same reference. Thuan keeps `content`.
        ray, replaced = re.subn(
            r"Invoke this skill without parameters\..*?then follow the full authoring workflow below\.",
            "Arguments: $ARGUMENTS\n\n"
            "Run from the repository containing `icon_set/`. The arguments are one or more "
            "reference SVG files, normally from `icon_set/work/todo-references/`. Process them "
            "in the order given, one icon per file; do not retrieve, add or substitute other "
            "references. If no file is given, say so and stop.\n\n"
            "For each file, the brief is the file itself: its filename is "
            "`<concept>_<source-uuid>.svg`. The **source UUID** is the UUID at the end of the "
            "filename, the **concept** is the text before it, and the **reference path** is the "
            "file path as given. Render and inspect the reference, then follow the full "
            "authoring workflow below. Skip a file whose "
            "`icon_set/work/primitive-make-ray/<source-uuid>/*/result.json` already exists and "
            "report it as already done. If a file is missing or has no UUID in its name, report "
            "that and continue with the next file. After the last file, report every file's result.",
            content, count=1, flags=re.DOTALL,
        )
        if replaced != 1:
            raise ValueError("primitive-make-ray: intro paragraph not found")
        for old, new in (
            ("The next-icon helper skips a source UUID once a run contains an authored "
             "Python module and a readable result.json with that source_uuid. "
             "Validation failures, warnings, and failed exports still count as attempts; "
             "do not retry them automatically. Write result.json last, including failures. "
             "Only attempts without a saved result remain eligible for automatic retry. "
             "If retrieval fails or no TODO icon remains, report that result and stop.",
             "A file counts as done once its run folder holds an authored Python module and "
             "a result.json with that source_uuid. Write result.json last."),
            # Otherwise keep icon-solo's own wording: its solo definition, and step 7's
            # visual judgement in place of Thuan's keep-the-failure instructions.
            ("Every input stays in `RESULT_DIR/`, subclasses `Solo48`, and uses "
             "`semantic_role = \"MAIN\"`, `semantic_kind = \"noun\"`. Keep the complete "
             "composition on the 48×48 canvas; do not reroute it to another family or "
             "enlarge the canvas.\n\n",
             re.search(r"A \*\*solo\*\* icon[^\n]*\n\n", render("solo")).group(0)),
            ("   Retain invalid candidates with their failure findings; do not claim\n"
             "   they passed. If validation or rendering raises, retain the source and\n"
             "   save the error in this same folder. No library build is needed.\n\n",
             "   No library build is needed.\n\n"
             "   Open the PNG and judge it at 48 pixels. Numeric success is not\n"
             "   visual approval; if two candidates are close, render both and keep the stronger.\n\n"),
            ("   Preserve the helper's concept, source UUID, reference path, category,\n"
             "   and optional brief as `concept`, `source_uuid`, `reference_path`,\n"
             "   `category`, and `brief` (null when absent). Keep the exact strings,\n"
             "   including multiline brief content; do not substitute inferred values.\n"
             "   Include the complete original stdout as `retrieval_stdout` to retain\n"
             "   any additional fields, and stderr warnings as `retrieval_stderr`.\n"
             "   Write this JSON as soon as retrieval succeeds, even if drawing fails.\n",
             "   Record the input as `concept`, `source_uuid` and `reference_path`,\n"
             "   taken exactly from the filename and the path as given; do not\n"
             "   substitute inferred values. Write this JSON before drawing, even if\n"
             "   drawing fails.\n"),
            ("author the complete retrieved reference", "author the complete given reference"),
            ("retrieval metadata", "input metadata"),
            ("name: primitive-make-ray\n",
             "name: primitive-make-ray\nargument-hint: <reference.svg> [more.svg ...]\n"),
        ):
            if old not in ray:
                raise ValueError(f"primitive-make-ray: text not found: {old[:60]!r}")
            ray = ray.replace(old, new)
        ray = re.sub(
            r"^description: .*",
            "description: Author each given reference SVG file (a TODO reference, usually from "
            "icon_set/work/todo-references/) as a complete Pictographic SOLO48 icon, including "
            "text, digits, logos, symbols, avatars, wrappers and combinations. Takes one or more "
            "file paths; the source UUID and concept come from each filename. Save results and "
            "input metadata in a standalone folder without gallery updates. Generated from the "
            "contracts by icon_set/scripts/generate_skills.py; do not edit by hand.",
            ray, count=1, flags=re.MULTILINE,
        )
        if agent in ("all", "claude"):
            outputs[SKILLS_DIR / "primitive-make-ray" / "SKILL.md"] = ray
        if agent in ("all", "codex"):
            outputs[CODEX_SKILLS_DIR / "primitive-make-ray" / "SKILL.md"] = (
                render_codex(ray).replace(
                    "# /primitive-make-ray —", "# $primitive-make-ray —", 1
                )
            )
        # Thuan: Ray's workflow on the side-mains page's missing mains, drawn as referenced.
        thuan = content.replace(
            "name: primitive-make-ray\n", "name: side-main-make-thuan\n", 1
        ).replace("# /primitive-make-ray —", "# /side-main-make-thuan —", 1).replace(
            "python3 icon_set/scripts/next_icon.py", "python3 icon_set/scripts/next_side_main.py"
        ).replace(
            "Retrieve the next TODO icon by running this command without parameters:",
            "Retrieve the next missing side-combination main (the Missing bucket of "
            "`gallery/side-mains.html`) by running this command without parameters:",
        ).replace(
            "TODO icon remains", "missing side main remains"
        ).replace(
            "icon_set/work/primitive-make-ray/", "icon_set/work/side-main-make-thuan/"
        ).replace(
            "The next-icon helper skips", "The next-side-main helper skips"
        )
        thuan = re.sub(
            r"^description: .*",
            "description: Retrieve the next missing side-combination main (gallery side-mains "
            "page), or several with an optional count and --offset, and author each as a "
            "Pictographic SOLO48 icon exactly like its reference, with no classification or "
            "routing. Save results and retrieval metadata in a standalone folder without gallery "
            "updates. Generated from the contracts by icon_set/scripts/generate_skills.py; do not "
            "edit by hand.",
            thuan, count=1, flags=re.MULTILINE,
        ).replace(
            "name: side-main-make-thuan\n",
            "name: side-main-make-thuan\nargument-hint: [count] [--offset N]\n", 1,
        )
        # Optional batch arguments: a count of mains per invocation and a queue offset, so
        # parallel workers can start at different positions.
        thuan, replaced = re.subn(
            r"Invoke this skill without parameters\..*?report that result and stop\.",
            "Arguments: $ARGUMENTS\n\n"
            "Run from the repository containing `icon_set/`. Both arguments are optional: the first "
            "number is the **count** of mains to author in this invocation (default 1), and "
            "`--offset N` skips the first N missing mains, so parallel workers can take different "
            "sources (`--offset 0`, `--offset 1`, ...).\n\n"
            "Retrieve each main from the Missing bucket of `gallery/side-mains.html` with the same "
            "command every time:\n\n"
            "```bash\npython3 icon_set/scripts/next_side_main.py --offset <N>\n```\n\n"
            "Use its output as the brief, including the source ID and reference path, then follow "
            "the full authoring workflow below. A main whose run folder holds a `result.json` "
            "leaves the queue, so once a main is saved the same offset returns the next one; if it "
            "returns a source you already saved in this invocation, rerun it with the offset "
            "raised by one. Repeat until **count** mains are saved, then report all of them. If "
            "retrieval fails or no missing side main remains, report that result and stop.",
            thuan, count=1, flags=re.DOTALL,
        )
        if replaced != 1:
            raise ValueError("side-main-make-thuan: intro paragraph not found")
        thuan = re.sub(
            r"\*\*Generate every input:\*\*.*?(?=Letters and digits)",
            "**Draw the reference as it is:** author the retrieved main `reference` as one "
            "SOLO48 icon that follows the reference. Do not classify, triage, route, skip or "
            "split it into component briefs, whatever it contains. The `combination context` "
            "SVGs only show how this main is used beside a sub modifier; never draw that "
            "side modifier. Preserve the reference's defining features and arrangement.\n\n",
            thuan, count=1, flags=re.DOTALL,
        )
        thuan = thuan.replace(
            "Inspect the complete reference before reduction. Treat its text, enclosure, main "
            "subject and modifiers as parts of the requested composition; do not reject or "
            "split combinations.",
            "Inspect the complete reference before reduction, then glance at the "
            "(at most two) combination-context SVGs to confirm which part is the main. Draw only the "
            "reference; do not reject, reroute or split it.",
        ).replace(
            "   `category`, and `brief` (null when absent). Keep the exact strings,\n",
            "   `category`, `aliases`, `uses` and `combination_context` (a list of the\n"
            "   context lines). Keep the exact strings,\n",
        ).replace(
            "   including multiline brief content; do not substitute inferred values.\n",
            "   do not substitute inferred values.\n",
        )
        if agent in ("all", "claude"):
            outputs[SKILLS_DIR / "side-main-make-thuan" / "SKILL.md"] = thuan
        if agent in ("all", "codex"):
            outputs[CODEX_SKILLS_DIR / "side-main-make-thuan" / "SKILL.md"] = (
                render_codex(thuan).replace(
                    "# /side-main-make-thuan —", "# $side-main-make-thuan —", 1
                )
            )
    # Thuan fixes: claim disapproved solo icons on production, redraw each with /primitive-make-ray,
    # then upload before/after and report. Only the claiming and uploading live here.
    if skill in (None, "primitive-fix-thuan"):
        fix = render_primitive_fix()
        if agent in ("all", "claude"):
            outputs[SKILLS_DIR / "primitive-fix-thuan" / "SKILL.md"] = fix
        if agent in ("all", "codex"):
            outputs[CODEX_SKILLS_DIR / "primitive-fix-thuan" / "SKILL.md"] = re.sub(
                r"(?<![\w./-])/primitive-", "$primitive-", render_codex(fix)
            )
    # Thuan subs: the side-subs page's missing subs, drawn on strict SUB32 into a standalone folder.
    if skill in (None, "side-sub-make-thuan"):
        sub = render_side_sub()
        if agent in ("all", "claude"):
            outputs[SKILLS_DIR / "side-sub-make-thuan" / "SKILL.md"] = sub
        if agent in ("all", "codex"):
            outputs[CODEX_SKILLS_DIR / "side-sub-make-thuan" / "SKILL.md"] = (
                render_codex(sub).replace("# /side-sub-make-thuan —", "# $side-sub-make-thuan —", 1)
            )
    if agent in ("all", "codex"):
        for name in ("icon-brief", "icon-making", "icon-review", "icon-color", "icon-solo-distilled", "icon-solo-distilled-force", "icon-solo-queue", "fix-icon-sub", "fix-icon-queue"):
            if skill is not None and skill != name:
                continue
            source = (SKILLS_DIR / name / "SKILL.md").read_text(encoding="utf-8")
            outputs[CODEX_SKILLS_DIR / name / "SKILL.md"] = render_codex(source, name)
        # Portable skills are generated from the same Codex text, not edited separately.
        for target, content in list(outputs.items()):
            if target.parent.parent == CODEX_SKILLS_DIR:
                outputs[REPO_ROOT / "skills" / target.parent.name / "SKILL.md"] = content
    if skill is not None:
        outputs = {target: content for target, content in outputs.items() if target.parent.name == skill}
        if not outputs:
            print(f"No generated output for {skill} with agent={agent}", file=sys.stderr)
            return 1
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
    parser.add_argument("--skill", help="generate/check only one named skill, such as icon-color")
    args = parser.parse_args(argv)
    return write_all(check_only=args.check, agent=args.agent, skill=args.skill)


if __name__ == "__main__":
    raise SystemExit(main())
