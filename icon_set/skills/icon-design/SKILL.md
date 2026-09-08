---
name: icon-design
description: Design a new icon for the Pictographic icon set from a text brief, or from a brief plus reference images. Use when asked to create, draw, add, or redesign an icon, symbol, or glyph in this repository. Covers choosing the family (sub 32, solo 48, container 64), keyshape selection, authoring geometry with the Python model, Lucide construction references, the validator chain, and container composition.
---

# Designing an icon

You author **geometry**, not SVG. A Python `Icon` subclass owns typed primitives;
the SVG, the PNG and the metadata record are build artifacts produced from it.
Never hand-write or hand-patch a final SVG — repair the model and re-emit.

Preserve the reference icon's supplied ID in every generated Python filename
and in `SOURCE_ICON_ID`, with its source path in `SOURCE_PATH`. Search by that ID
before authoring so existing icons can be patched in place. Follow
[naming.md](naming.md#reference-ids-in-python-scripts) for extraction, filenames,
and handling references without IDs.

Read [`../../README.md`](../../README.md) first if you have not: it states the
three families, the keyshape table, and the two frozen tolerance decisions.

## Visual priorities

The default aesthetic is **Lucide-style geometry: clean construction, smooth
curves, and appropriate balance**. Inspect a relevant local Lucide original and its
atomic-debug geometry when a useful match exists; carry over the construction
principle, then re-author on this family's grid, stroke and keyshape.

Prefer mirrored geometry and visual balance only where they preserve the icon's
meaning, recognizability, and natural shape. These are optional design choices,
not requirements: skip mirroring or forced balance when they would distort the
subject. A palm tree, for example, may retain uneven fronds and a leaning trunk;
mirror only the parts where it helps the drawing read clearly.

For symmetric subjects, derive paired geometry from one axis with mirrored
coordinates, matching radii and equal spacing. Preserve meaningful asymmetry
in directional or perspective subjects. Use tangent-continuous joins where
curves should flow smoothly, while retaining intentional corners and the
subject's recognizable features. Do not distort the subject just to mirror it.

These are design priorities, alongside the existing validation rules. Follow the
construction checklist in [authoring.md](authoring.md) and the local reference
workflow in [intake.md](intake.md). Judge smoothness, symmetry and negative space
at native size in both themes, not only from a passing validation report.

## The three families

Every icon belongs to exactly one family. The family fixes the folder its module
lives in, the profile it is authored on, and the dist folder it ships to. These
are one decision, not three, and no family may borrow another's canvas.

| Family | Profile | Canvas | Folder | Base class | Job |
|---|---|---|---|---|---|
| `sub` | `SUB32` | 32×32 | `sub/` | `Sub32` | Read small and hosted: a verb, state, modifier, or a simple noun shape that works as content. Its canvas *is* the container slot. |
| `solo` | `SOLO48` | 48×48 | `solo/` | `Solo48` | A standalone subject read on its own: a primary noun with its own silhouette. Hosts nothing, is hosted by nothing. |
| `container` | `CONTAINER64` | 64×64 | `container/` | `Container64` | An enclosure or framed device drawn at 64, with whatever interior furniture its subject has. Stands alone as a noun and is the outer half of a composition when its interior has room. |

Folders are under `icon_set/model/icons/`. The binding lives in
`icon_set/model/contracts/icon-profile.v1.json` under `families`, and three
independent guards enforce it: the family base resolves its profile from the
contract and has no attribute to override; the registry refuses a module whose
class belongs to another family's folder; the validator rejects any icon whose
profile is not its family's. The build ships each family to its own folder with
its own manifest — `dist/sub32/`, `dist/solo48/`, `dist/container64/` — so the
three never mix.

**How to choose.** Ask what the icon *does in the set*:

- Will it sit inside a container, or act as a mark, operator, arrow, state or
  modifier next to something else? → `sub`.
- Is it a subject that stands on its own — a device, an object, a badge, a
  traced drawing whose proportions matter? → `solo`.
- Is it an enclosure meant to hold something? → `container`.

A `heart` at 32 is a sub icon: a small noun shape that works as content. A
`smartwatch` at 48 is a solo subject. A `container-circle` at 64 hosts. If the
same concept is genuinely wanted in two families, each is a **separately
authored drawing** with a profile suffix (see [naming.md](naming.md)); the
model rejects scale transforms and the round-trip check rejects them in SVG.

## The five steps

1. **Name the concept.** One short sentence for what it is, then a kebab-case
   id. See [naming.md](naming.md).
2. **Pick the family.** That decides the folder, the profile and the canvas, as
   above. Then declare `semantic_kind` — what the subject is — and
   `semantic_role`, which is what it is *standing alone*: MAIN for a noun, SUB
   for a verb, state or modifier. The two must agree and the validator checks
   it. A role is a description, not a permission: `heart` and `circle` are MAIN
   nouns in the `sub` family and are fine inside a container.
3. **Pick the keyshape, then design backwards from its four extreme
   coordinates.** This is the step people skip and then pay for.
   See [authoring.md](authoring.md) and [keyshape-fitting.md](keyshape-fitting.md).
4. **Author the geometry** as a subclass of the family base, in a new module in
   the family's folder. See [geometry.md](geometry.md).
5. **Validate, repair, and review at native size.**
   See [validation.md](validation.md).

## Intake

Two modes, both described in [intake.md](intake.md):

- **Brief only** — a concept name and a minimal description. No fabricated
  source SVG, no detector run, no invented reference.
- **Brief plus references** — images or files the user placed in scope. A
  reference is evidence about the *subject*; it is never a grid, a stroke
  weight, or permission to draw something else.

Copy-paste request forms are in [request-templates.md](request-templates.md).

## What you may not do

These are the rules that keep the set coherent. None of them bends.

- **Never weaken a rule to force a pass.** Not the stroke, not the grid, not the
  clearance, not a tolerance, not a profile constant. Repair the geometry and
  restart the chain, or report the blocker.
- **Never put a family on another family's canvas.** A `solo` icon is 48 and
  lives in `solo/`; there is no 64-unit solo and no 48-unit container. If the
  subject needs a different canvas, it is a different family and a different
  drawing.
- **Never scale.** A `SOLO48` sibling of a `SUB32` icon is a separately authored
  drawing. The model rejects scale transforms and the round-trip check rejects
  them in emitted SVG.
- **Never leave the canvas.** Painted ink stays within `[0, canvas]`.
- **A `review` verdict is not a pass.** It means a rule could not be proved.
- **Integers only.** Every authored coordinate is an integer on grid 1.

## Where things live

| Need | Path |
|---|---|
| Locked numbers and the family binding | `icon_set/model/contracts/*.json` |
| Authoring API | `icon_set/model/icons/base.py` |
| Family bases | `icon_set/model/icons/family.py`, then `sub/_base.py`, `solo/_base.py`, `container/_base.py` |
| Existing icons to imitate | `icon_set/model/icons/sub/`, `icon_set/model/icons/solo/`, `icon_set/model/icons/container/` |
| Registry (discovers by folder) | `icon_set/model/icons/registry.py` |
| Validator chain | `icon_set/validation/validator.py` |
| Lucide references | `icon_set/references/lucide/` |
| Build | `icon_set/scripts/build.py` |
| Visual review | `icon_set/scripts/contact_sheet.py` |
| Per-family slash skills (`/icon-sub`, `/icon-solo`, `/icon-container`) | `.claude/skills/icon-*/SKILL.md`, generated by `icon_set/scripts/generate_skills.py` |
| Folder-by-mission map | `icon_set/STRUCTURE.md` |

## Definition of done

- `python3 -m unittest discover -s icon_set/tests -t .` is green.
- `python3 icon_set/scripts/build.py` exits 0 and the icon is in **its family's**
  manifest — `dist/sub32/manifest.json`, `dist/solo48/manifest.json` or
  `dist/container64/manifest.json`.
- `validate_icon()` returns `valid`, with **no warnings** — a warning is an
  uncertified `review`.
- You have looked at it at native size, in both themes, via
  `contact_sheet.py --family <family>`. Numeric success is not visual approval.
