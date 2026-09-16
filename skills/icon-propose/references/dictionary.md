# Updating the draft concept dictionary

Read this only when the task calls for updating the Pictographic draft page.

## Files and scope

- Editable data: `icon_set/scripts/templates/concept-dictionary.json`
- Existing local preview data: `icon_set/dist/gallery/concept-dictionary.json`
- Preview: `/gallery/concept-dictionary.html?category=<existing-category-key>` on the user's running local server. Do not assume its port.
- Page behavior: `icon_set/scripts/templates/concept-dictionary.js`

Preserve other categories, existing IDs, source references, unknown metadata fields, and the user's saved shortlist keys. Keep exact category keys from the source catalog, even if a display name corrects spelling. Read the current schema before editing; the format below describes version 1.

If a preview data file already exists, copy the updated source JSON to it after validation. Do not run a full icon/gallery build, add this page to `gallery.py`, edit global navigation, deploy it, or publish source-review changes as a side effect.

For a category that is not curated yet, add its title, a short category-specific summary, a principle, and entries inside the existing `categories` mapping. Do not replace the dictionary root or remove existing categories.

## Version 1 data shape

```json
{
  "version": 1,
  "categories": {
    "websites": {
      "title": "Websites",
      "summary": "Standalone subjects for web use.",
      "principle": "One subject. One clear meaning. Many useful aliases.",
      "entries": [
        {
          "id": "hardware-security-token",
          "name": "Hardware security token",
          "group": "Privacy & trust",
          "meaning": "A physical key for signing in.",
          "brief": "One compact USB security token with an integrated touch contact and an exposed connector.",
          "aliases": ["security key", "authentication key", "USB token"],
          "source_ids": [],
          "status": "proposed",
          "priority": "Core",
          "why": "Adds a physical authentication object beyond a generic key."
        }
      ]
    }
  }
}
```

The example demonstrates the shape, not an additional idea to add: it already exists in the Websites dictionary.

## Field behavior

- `id`: stable lowercase kebab-case, unique within its category. The shortlist identifies concepts by `category/id`; do not rename old IDs or recycle removed ones casually.
- `name`: canonical visual noun phrase. Search aliases as well as IDs to detect semantic duplication.
- `group`: a meaningful category-specific theme; filter options are read from these values.
- `status`: `proposed` for a proposed drawing, `reuse` for an existing reference candidate.
- `priority`: `Core` or `Extended`, shown as “Start here” and “Extend later.”
- `source_ids`: actual source UUIDs from `primitives.json`, used as the card's existing-reference preview. Never invent a UUID or use a model ID here. New text-only proposals normally use an empty list.
- `why`: explain usefulness and related-source overlap. Explicitly identify experimental metaphors or uncertain recognition here and in `meaning` where helpful.

For an extracted-subject proposal whose original depicts a larger composition, keep `source_ids` empty so the preview does not misrepresent the proposed drawing. Record the original UUID/path and the extraction in `why`. Do not silently treat the whole composition as the new reference.

The existing page displays proposal placeholders, not generated artwork. Distinguish proposed drawings from assets ready for use. Related-name matches require inspection before claiming reuse suitability.

## Safe edits and validation

### Cross-category reuse in version 1

The current page stores entries inside category lists and keys shortlists by `category/id`; it has no global concept-reference field or related-category UI. Keep the **one canonical icon, multiple categories** rule without claiming those features already exist:

- For an existing source-backed icon, an additional category entry can use `status: "reuse"` and the same verified source UUIDs. Preserve its canonical name and identify the shared icon/model in `why`. This is a category association, not a new drawing.
- For an existing ungenerated proposal, identify its current `category/id` as the canonical pending proposal. Report the requested association separately; do not duplicate its `proposed` entry under another category or mark it as generated/reusable artwork.
- Record primary category, related categories, and the reason for the relationship in the brief output or `why` until structured category associations are supported. Use actual catalog category keys when available.
- Do not migrate the schema, move existing entries, break shortlist identities, or add a category-management interface merely to propose icons. Implement that functionality only when requested.

### Checks

Reload the current file immediately before writing so another task's additions are preserved. Merge by stable category and ID; resolve any collision before writing. Work from the latest content, not a stale full-file copy. If the file changed during preparation, reapply only your additions to the latest version.

Validate:

1. JSON parses; the expected categories and their existing entries remain.
2. New IDs and normalized subject names do not duplicate existing entries or each other. Aliases are also checked for the same concept under another name.
3. Required entry fields are populated, `aliases` and `source_ids` are lists, and status/priority values are supported.
4. Every referenced UUID resolves to an actual catalog row.
5. The requested new-proposal count excludes reuse entries, new category associations, and references to proposals from previous turns or other categories. Count each new canonical subject once.
6. Source and local preview JSON agree after syncing.

If the user wants proposed drawings emphasized, keep core proposals first, then extended proposals, then reuse candidates; preserve relative ordering inside each group. Otherwise preserve existing ordering and append additions.

When the local browser is available, reload the existing preview and confirm the new counts and a representative added brief. A JSON-only content change does not need a full icon test suite. If no browser/server is available, report data validation without claiming browser verification.
