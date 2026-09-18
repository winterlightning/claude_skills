# Mission: generate a new standalone icon

For family `symbol`, use `icon_set/skills/icon-design/symbol-family.md` as the family instructions. Keep `symbol` / `SYMBOL32`; do not reroute it to sub based on older skill catalogs.
Read .agents/skills/icon-making/SKILL.md, then the matching icon-sub, icon-solo, or icon-container skill.
Read icon_set/skills/icon-design/symbol-construction.md before placing points. Record a compact symbol plan in the candidate module and implement its shape, nesting, repetition, symmetry, and attachment constraints using the existing Python geometry API.
If the request lists reference_images, look at each one before designing: PNGs (and a rasterized preview_png of each SVG) are attached to this conversation, and every file is in the workspace at its path. Use them as visual references for subject, silhouette, proportions and key details. Redraw to the family skill's grid and rules; never copy reference path data verbatim. The written brief wins where it and a reference disagree.
Use the requested name and description to design a NEW standalone icon. If family is auto, choose sub, solo, or container by meaning and explain the choice. Otherwise honor the requested family.
Choose a unique icon_id, Python filename, and class name. This is a new icon, not a fix or variant of an existing icon; do not set variant_of.
Create exactly ONE candidate in ONE NEW public Python module under icon_set/model/icons/<family>/.
Do not modify existing icons, contracts, skills, registry, or other existing files. Use existing dependencies only. Do not publish outside this workspace.
Validate the candidate using the matching family skill. If the request cannot produce one standalone icon, explain and stop.
Write candidate.json at the workspace root with {"path":"icon_set/model/icons/<family>/<filename>.py","family":"sub|symbol|solo|container","icon_id":"..."}.
The reviewer will choose whether to add this candidate to the grid or discard it. Do not accept or approve it yourself.

## New icon request (JSON)
{{REQUEST_JSON}}
