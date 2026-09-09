# Mission: fix an existing icon as a new variant

Read the existing Python file identified in source.python_source.path and inspect source.python_source.class_name. The source icon_id and family identify the exact icon to fix, including when its module defines multiple icons.
Read .agents/skills/icon-making/SKILL.md, then the icon-sub, icon-solo, or icon-container skill matching the EXISTING family. Preserve that family; do not auto-select another type.
Apply the requested feedback to this icon. Preserve its identity and all details the feedback does not ask to change.
Keep the old Python file and old icon unchanged. Create exactly ONE candidate in ONE NEW public Python module under icon_set/model/icons/<family>/, with a unique variant filename, class name, and icon_id. Set variant_of to source.icon_id and provide a descriptive variant_label.
Do not redefine unrelated sibling icons from the source module. Do not modify contracts, skills, registry, or any other existing file. Use existing dependencies only. Do not publish outside this workspace.
Validate the fixed variant using its family skill. If the request cannot produce one standalone icon, explain and stop.
Write candidate.json at the workspace root with {"path":"icon_set/model/icons/<family>/<filename>.py","family":"sub|solo|container","icon_id":"..."}.
The reviewer will compare old and new versions and choose whether to add or discard the candidate. Do not accept or approve it yourself.

## Existing icon and requested changes (JSON)
{{REQUEST_JSON}}
