---
name: icon-review
description: Visually review existing Pictographic icons for intended symmetry, proportions, keyshape choice, and profile fit, then write concrete repair briefs. Use for AI design review, missed diagonal or local symmetry, cramped or stretched silhouettes, and profile-aware fix suggestions. Generated from .claude/skills/icon-review/SKILL.md by icon_set/scripts/generate_skills.py; edit the source, not this copy.
---

# Icon review

Review the supplied icon IDs, references, or selected batch. Default to reviewing
and suggesting repairs; when the user requests fixes, carry the findings through
the existing variant and family-authoring workflow. A review request alone does
not change icon sources or gallery approval state.

Run from the repository containing `icon_set/`. Locate it from the current
workspace; for a symlinked skill, its resolved path is inside that repository.
The maintained source is `.claude/skills/icon-review/SKILL.md`; regenerate its
Codex and portable copies with `icon_set/scripts/generate_skills.py`.

## Establish the current drawing and its rules

Resolve the exact registered icon and Python source. Read its metadata, source
reference, variant history when relevant, and any explicit user design choices.
Freshly render the Python model: gallery images and existing exports can be stale.
Use this evidence helper for registered icons:

```bash
python3 icon_set/scripts/prepare_icon_review.py --icon badminton-shuttlecock --out work/icon-review/badminton-shuttlecock
```

Open `sheet.png` with an image-viewing tool, and inspect `evidence.json` and the
Python source. The sheet includes native-size light/dark views and enlarged
views; use enlargement to locate defects and native size to judge their impact.
When a source reference exists, the helper renders `reference.png`; open it too.
Missing references or checker errors must remain visible in the review. For an
unregistered SVG, render it directly, use the user-supplied profile or establish
the intended family through `$icon-making`, and label model QA as unavailable.

Read the active values in `icon_set/model/contracts/icon-profile.v1.json`, using
`Profile.spec` and `Keyshape.bounds_for(profile)` for resolved dimensions. Read
the matching family skill (`$icon-sub`, `$icon-solo`, `$icon-container`, or the
solo `$icon-avatar` specialization) and the relevant shared design guidance.
Prefer active structured contract values over historical notes. Do not transfer
one family's dimensions or clearance rules to another. Review:

- The declared family/profile, canvas, integer grid, stroke, caps and joins.
- The chosen keyshape's actual painted bounds or radial envelope; the interior
  guide constrains detail rather than the entire silhouette.
- Minimum ink clearance, openings and pinches, actual contacts, and any applicable
  human/avatar construction rules. A head and its own body are one subject.

The helper records model and full build-QA findings. Treat them as measured
evidence, separate from the agent's design judgment. A `pass` does not certify
good design; `not_applicable` from the symmetry checker means only that neither
of its horizontal/vertical ink-overlap triggers fired.

## Decide what should be symmetric

Make this decision for every reviewed icon, even when all numeric checks pass or
ink overlap is low. Start from the visible subject, viewpoint and user intent,
then use coordinates to investigate. A title alone is insufficient evidence.

State the expected structure and its reason:

- **Whole-object mirror:** the chosen depiction has paired sides around its
  structural axis, which may be vertical, horizontal, diagonal or off-center.
- **Local mirror / repeated parts:** a body, face, enclosure, pair of wings,
  wheels or repeated units should agree while another feature is directional
  or intentionally unequal. Name the exact parts and relationships.
- **Radial / rotational structure:** assess repeated placements, radii and
  spacing around a center; do not substitute a horizontal mirror test.
- **Intentional asymmetry:** viewpoint, pose, motion, perspective, organic
  growth, a handle, a logo feature or another meaningful detail explains it.
- **Uncertain:** competing interpretations remain; identify the missing visual
  or semantic evidence and give a conditional recommendation.

Orientation alone is not perspective. A tilted symmetric object can still mirror
about its own tilted axis. Conversely, a symmetric real object can be depicted
asymmetrically in perspective. Do not force every noun, face, animal, tree or
directional symbol into a whole-icon mirror. Preserve meaningful asymmetry and
review symmetric subparts independently. User-specified symmetry is design intent
even if the current drawing has drifted far from it.

Choose an axis from structural landmarks: center of the base, midpoint of a
divider, shaft, tip, paired attachments, or the center of a repeated group.
Record it as two points (or an equation), its scope, and confidence with reasons.
Do not optimize an axis merely to hide one malformed side. When useful, generate
an overlay for the agent-chosen mirror axis, then open the resulting image:

```bash
python3 icon_set/scripts/prepare_icon_review.py --icon badminton-shuttlecock --axis 14 34 30 18 --out work/icon-review/badminton-shuttlecock
```

Blue is authored geometry; red is its reflection. This diagnostic is not an
automatic design verdict. For local symmetry, compare only the named parts and
explain why other overlay differences are intentional. For rotational structure,
inspect the relevant repeated units directly rather than using this mirror view.

## Review shape quality and identify the owning repair

Compare silhouette, paired widths/lengths, matching radii, equivalent curve
bulges, attachment positions, repeated spacing and negative space on both sides.
Check contour continuity and tangents where a smooth join is intended; rounded
stroke joins can hide a geometric kink. Preserve purposeful corners. Judge the
subject's recognizability, visual weight and reduction at its native profile size.
Use `icon_set/skills/icon-design/authoring.md` and
`icon_set/skills/icon-design/symbol-construction.md` for construction principles.

### Judge the keyshape as a design choice

Assess whether the current keyshape suits the subject, even when the icon fits
it exactly and passes validation. A legal envelope can still produce an overly
narrow, wide, stretched, squat, cramped or visually oversized drawing. Separate
an envelope problem from a local proportion problem: the body-to-neck ratio,
waist width, interior spacing or another owning shape may need adjustment while
the current keyshape remains appropriate.

When the envelope contributes to a visible problem, compare the current choice
with a plausible legal alternative within the same profile. State both resolved
painted dimensions, the change in aspect ratio and usable centerline space, and
the intended visual benefit. Treat “smaller” precisely: shorter, narrower, lower
area and less visual weight are different changes. A smaller envelope does not
automatically improve balance or leave enough room for required clearances.

Recommend the keyshape and the corresponding reconstruction together. Explain
how the body's proportions, lengths, radii, spacing and extreme points would
change. Merely changing the keyshape token or shrinking the finished SVG is not
a repair; stroke width and profile rules stay fixed. In review-only mode, label
an unrendered alternative as a hypothesis. When fixes are requested, compare the
current and reconstructed candidate at native size in both themes, and rerun
envelope, clearance and full build QA before selecting it.

For example, if `acoustic-guitar` on SOLO48 `VRECT_L` looks too narrow or tall,
consider whether a shorter, wider envelope or a local body/neck rebalance would
help. At the time of this example, `VRECT_L` has painted dimensions 36×44,
`SQUARE` 40×40, and `VRECT_M` 32×44. The M rectangle is smaller in width but
more slender; it is not automatically the answer to “too narrow.” Re-read the
current contract and inspect the current drawing before recommending one.
Preserve the guitar's identity and meaningful details; this example does not
establish a preferred keyshape for every guitar.

If the current proportions and keyshape already work, explicitly retain them.
Do not manufacture a defect or propose a redesign to fill out the review.

For every actionable finding, give:

1. **Observation:** affected visible region and exact element/contour IDs when
   available; distinguish visual judgment from measured facts.
2. **Expected relationship:** the proposed axis, paired feature, repeat pattern,
   tangent, attachment, envelope or clearance constraint and why it matters.
3. **Repair:** which owning shape/shared parameter should change, what to derive
   together, and what identity, topology and deliberate asymmetry must survive.
4. **Profile fit:** current or proposed legal keyshape, applicable dimensions and
   spacing budget, plus any feasibility issue requiring a candidate render.
5. **Acceptance evidence:** what should visibly improve and which unchanged
   validation checks and geometric relationships should hold afterward.

Prefer rebuilding a flawed pair from shared dimensions over moving independent
endpoints until it looks close. Do not mirror a malformed half just because it
is available. For a diagonal axis `x+y=k`, reflection is `(x,y) -> (k-y,k-x)`;
for `y=x+b`, it is `(x,y) -> (y-b,x+b)`. Integer k/b preserve this grid. Other
angles may require reconstructing legal geometry rather than rounding transformed
points. Account for reflected arc sweep, swapped ellipse radii on quarter-turn
diagonal reflections, contour traversal and exact joins. Verify actual API support
before prescribing primitives. Diagnostic SVG transforms are not authoring output.

A suggested repair can change the keyshape within the same profile when justified
by the subject's proportions. Explain that choice and derive the new envelope.
Preserve the current orientation unless a change is needed and justified. Never
change profile constants, tolerances or checker thresholds to excuse a design,
invent contacts, scale between families, or patch a generated SVG as the repair.
A concept sketch or coordinate proposal remains unvalidated until implemented.

## Deliver the review or carry out requested fixes

Save a concise `review.md` beside the evidence. Include icon/source identity and
SVG hash, profile/keyshape and its keep/change rationale, visual verdict
(`keep`, `repair`, or `uncertain`),
symmetry intent/scope/axis/confidence, numeric QA status separately, actionable
findings, and an executable authoring brief naming the relevant family skill.
Link the actual inspected renders. For a batch, review each icon visually in
manageable sheets, keep per-icon findings, prioritize consequential defects, and
state exactly which icons were reviewed. Never mark unviewed icons as reviewed.

If fixes are requested, existing authorization is sufficient to proceed:

```bash
python3 icon_set/scripts/create_variant.py --icon <parent-id> --family <family> --label "<specific repair>"
```

Use the matching family skill to edit the returned new Python file, preserving
the parent, source identity and variant links. Re-render before/after evidence,
run model and full build QA, and verify the chosen symmetry relationships even
when the old checker cannot test that axis. Complete the family skill's applicable
build and review steps. Report remaining failures honestly; a visual improvement
is not an automated pass. Do not approve a candidate in the gallery merely because
this skill reviewed or generated it.

### Calibration case: badminton-shuttlecock

Use this when reviewing that icon or diagnosing a similar diagonal blind spot;
reinspect the current revision rather than assuming these observations remain true.
The simplified tilted depiction has a cork and an empty feather fan. Its cork
center `(14,34)` and divider midpoint `(18,30)` suggest `x+y=48`; the divider
endpoints `(14,26)` and `(22,34)` reflect exactly. The old horizontal/vertical
checker can return `not_applicable` while the fan remains visibly lopsided.
Inspect `feather-left`, `feather-base` and the outer feather arcs as paired
structure. A repair brief should rebuild the fan around the same structural axis,
with paired side lengths and coherent mirrored feather curves, retaining the
cork/divider and empty interior. Do not add an internal rib just to imply symmetry.
Check the current SOLO48 keyshape and stroke envelope after rebuilding. This is
an example of intended symmetry that needs agent judgment, not a rule that every
shuttlecock viewpoint or feather arrangement must be mirrored.
