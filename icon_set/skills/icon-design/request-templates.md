# Request templates

Copy-paste forms for asking an agent to design an icon. Fill in the angle
brackets and delete what does not apply.

## Text-only brief

```text
Use icon_set/skills/icon-design/SKILL.md to create icons for:

- <concept name> — <one-sentence description of the subject>
- <concept name> — <one-sentence description>

Family: <sub (32) | solo (48) | container (64), or "you choose and say why">

For each: author a subclass of the family base in a new module in that
family's folder, and pass the full validator chain with no warnings. Deliver the geometry, the
exported SVG, and a native-size visual review of the result.

Choose the keyshape first and design backwards from its four extreme
coordinates. Consult Lucide references for construction where they answer a
real question, and say which you used and what you took from each.

Do not weaken any rule to force a pass. If an icon cannot be made to pass,
report which check and which element blocked it and stop.
```

## Brief plus reference images

```text
Use icon_set/skills/icon-design/SKILL.md to create icons for:

- <concept name> — <one-sentence description>

References (in scope, nothing else): <paths to images or files>
Family: <sub (32) | solo (48) | container (64), or "you choose and say why">

Treat the references as evidence about the subject — which parts carry its
identity and how they sit together. They do not set the grid, the stroke, or
the proportions: recompose on the family's canvas at stroke 4 on the integer
grid. Do not reproduce extraction defects, and do not add features the brief
did not ask for. If a reference and the brief conflict, ask before authoring.

Record what you took from each reference. Then as above: keyshape first, full
validator chain with no warnings, native-size review.
```

## Container composition

```text
Use icon_set/skills/icon-design/SKILL.md.

Compose <container icon id> with <sub icon id> as a CONTAINER_COMBINE, via
icon_set/scripts/compose.py. If either does not exist yet, author it first:
the host in the container family (64), the content in the sub family (32).

A hosted child lands in (16,16)-(48,48). Nothing reserves it — draw the
container as its subject goes, then let compose.py measure whether this pair
clears. Validate the composition and review it at native size.
```

## Redesign an existing icon

```text
Use icon_set/skills/icon-design/SKILL.md to redesign <icon id>.

What is wrong: <describe what reads badly at native size>

Keep its concept id, family, keyshape and semantic role unless you can say why
they should change. Moving it to another family is a new drawing, not a redesign. Render the current and the proposed version side by side at
native size, and show me both before committing.
```
