# Combination database

The editable local library shares `icon_set/state/feedback.sqlite3` with progression. It
contains container and side pairs from `combination_data.json`, with the resolved
component references and artwork candidates from `published/gallery/combinations.json`.
Use `python3 -m icon_set combinations` to manage it. No additional packages are required.

The database is runtime state, excluded from Git. The existing tracked
`combination_data.json` remains the gallery's source of truth. Builds do not seed,
read or modify the combination tables. This version supplies database and command-line
editing, plus live links to progression; it does not add a gallery editor.

## Shared progression data

Progression decisions stay in `primitive_status`, alongside the library's `pairs`,
`components` and `pair_history` tables in the same database. The
`progression_combination_requirements` view reads every `skip` decision with reason
`container` or `combination` (side). It includes saved main/sub briefs, position,
notes and reviewer attribution, even when neither component is assigned yet.

`combination_entries` joins these requirements with existing pairs by source UUID.
An existing pair of the same kind appears once, with its progression information.
Requirements without a pair appear with `origin=progression` and a stable
`progression:KIND:UUID` ID. Changes made through the existing progression page,
agent scripts or direct database updates are visible immediately in this view and
the `list`/`show` commands. There is no copied flag or periodic sync job. These
links also work with an already-running gallery server.

Restoring a source to TODO removes its unassigned progression requirement. Existing
catalog pairs and their edit history are retained. Changing kind creates a
requirement for the new kind, while retaining any old authored pair; compare
`kind` with `progression_kind` to find pairs needing reconciliation. Archiving a
pair does not change the progression decision or recreate a duplicate requirement.

Main and sub each expose a readiness value: `needed`, `brief_ready`,
or `artwork_available`. The last means the imported artwork snapshot has a
candidate; it does not imply current artwork validation or reviewer approval.
No component is guessed from a combined reference's generated artwork.

```sh
python3 -m icon_set combinations migrate-legacy
python3 -m icon_set combinations sync-progression
```

Migration copies the old standalone library, including edits, archives and history,
into the shared database without replacing review/progression data. It is repeatable
when the copied rows are unchanged; conflicting rows stop the transaction. The old
`icon_set/state/combinations.sqlite3` remains as a backup and is no longer the
default. `sync-progression` indexes reference names and paths from the published
primitive catalog; run it after adding new source references. Flags and briefs
remain live even if names have not yet been indexed (the UUID is shown instead).

Progression-only rows are requirements, not yet editable pair definitions. To
assign components, create a pair using the requirement's UUID as `id` (or
`source_id`), its kind and the chosen component references. The view then links
the new pair automatically. Do not pass a `progression:...` ID as `--pair-id`.
Definition exports include authored pairs only, not unassigned live requirements;
back up the shared database to preserve the entire workflow.

## Import and browse

```sh
python3 -m icon_set combinations import-current
python3 -m icon_set combinations summary
python3 -m icon_set combinations list --kind side --query cloud
python3 -m icon_set combinations list --kind container --limit 100 --offset 100
python3 -m icon_set combinations show PAIR_ID
python3 -m icon_set combinations history PAIR_ID
```

`--database PATH`, before the subcommand, selects a separate working database.
Import is transactional and repeatable: existing pairs, edits and archives are
preserved. Changed upstream definitions are reported as conflicts for deliberate
reconciliation, not overwritten. New upstream pairs are added. Removed upstream
pairs are retained until explicitly archived. Artwork candidates are an import-time
snapshot, not a claim about current availability or approval.

Each pair has a stable `pair_id`, separate from its original source ID. Container
and side pairs may share a source ID. Missing component references remain null;
they are never guessed. Reviewed remaps are available in the resolved columns,
while original definitions are retained losslessly. Explicit `family/icon` keys
stay distinct from source UUIDs. Existing side position codes and detailed
placement, text, component, fit and review metadata are preserved.

## Add, edit, archive and restore

Save a JSON **definition** (the `definition` object returned by `show`, not the
whole response). For a new side pair, for example:

```json
{
  "id": "my-new-source-or-concept-id",
  "concept": "Cloud with plus",
  "main_id": "solo/cloud",
  "sub_id": "sub/plus",
  "component_selection": "explicit",
  "position": "br"
}
```

The keys in this example are illustrative; select actual library keys before
using them. Unbuilt components are allowed as planning requirements. Positions
support the existing `tl`, `tr`, `bl`, `br`, `to`, `bo`, `le`, `ri` codes, plus
`top`, `bottom`, `left`, `right`. Container pairs use their placement metadata.

```sh
python3 -m icon_set combinations save /tmp/pair.json --kind side --actor jakes
python3 -m icon_set combinations save /tmp/pair.json --kind side --pair-id PAIR_ID --revision 1 --actor jakes
python3 -m icon_set combinations save /tmp/pair.json --kind side --pair-id PAIR_ID --revision 2 --status archived --actor jakes
```

Editing requires the current revision from `show`; stale revisions are rejected.
Use `--status active` with the next revision to restore an archived pair. Every
save records the actor and full snapshot in `pair_history`. Pair identity and kind
cannot change during an edit; archive the old pair and create another when moving
between kinds. If a component changes, cached resolution candidates are cleared.

## Export reviewed changes

```sh
python3 -m icon_set combinations export /tmp/reviewed-combination-data.json
```

Export excludes archived pairs and produces the same container/side definition
format as `combination_data.json`; `--include-archived` exports both states.
Unknown editorial fields are preserved. It refuses to overwrite an existing file.
An untouched import/export round trip exactly preserves the original JSON data.

Review the exported diff against `combination_data.json`, then replace that source
file with the reviewed export when ready. Follow the normal publication workflow
to regenerate and publish the gallery. Source changes and publication remain
explicit; exporting alone never changes the website. For a full backup including
archives, history and resolved candidates, use SQLite's backup facility, not this
definition-only export. Production keeps its own database; do not copy local state
over the production review database.

## Tables

| Table | Purpose |
| --- | --- |
| `components` | Shared source UUIDs or exact icon keys, reference image URLs and imported artwork candidates |
| `pairs` | Kind, concept, main/sub links, side position, state, revision, original and editable definitions, resolved candidates |
| `pair_history` | Append-only per-revision snapshots and attribution |
| `primitive_status` | Existing authoritative progression decisions and component briefs |
| `combination_source_references` | Source names and paths indexed from the primitive catalog |
| `progression_combination_requirements` (view) | All currently flagged container/side sources |
| `combination_entries` (view) | Pairs and unassigned requirements, linked without duplication |

Indexes support lookup by kind, state, main and sub. Foreign keys protect component
links. Multiple concepts can intentionally use the same components and position;
uniqueness is enforced on `(kind, source_id)` rather than merging those concepts.
