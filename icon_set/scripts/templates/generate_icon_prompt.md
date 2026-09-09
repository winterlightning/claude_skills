# Mission: generate a new standalone icon

Read .agents/skills/icon-making/SKILL.md, then the matching icon-sub, icon-solo, or icon-container skill.
Use the requested name and description to design a NEW standalone icon. If family is auto, choose sub, solo, or container by meaning and explain the choice. Otherwise honor the requested family.
Choose a unique icon_id, Python filename, and class name. This is a new icon, not a fix or variant of an existing icon; do not set variant_of.
Create exactly ONE candidate in ONE NEW public Python module under icon_set/model/icons/<family>/.
Do not modify existing icons, contracts, skills, registry, or other existing files. Use existing dependencies only. Do not publish outside this workspace.
Validate the candidate using the matching family skill. If the request cannot produce one standalone icon, explain and stop.
Write candidate.json at the workspace root with {"path":"icon_set/model/icons/<family>/<filename>.py","family":"sub|solo|container","icon_id":"..."}.
The reviewer will choose whether to add this candidate to the grid or discard it. Do not accept or approve it yourself.

## New icon request (JSON)
{{REQUEST_JSON}}
