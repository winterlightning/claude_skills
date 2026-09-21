---
name: icon-solo-queue
description: Process a page of the Pictographic solo generation queue with icon-solo-distilled, generating standalone icons and saving verified component briefs for combinations. Use when asked to run a solo queue batch at a given offset. Hand-authored; edit this file directly.
argument-hint: <offset>
---

# /icon-solo-queue — process one queue page

Queue offset argument: $ARGUMENTS

Treat the invocation's single nonnegative integer as the queue **offset**, not
the item count. `/icon-solo-queue 10` means `--offset 10`. If omitted, use 50,
matching the original workflow. Reject an invalid argument before fetching.
Run commands from the repository root containing `icon_set/`.

Read and apply `../icon-solo-distilled/SKILL.md` for every item, including its
reference triage, authoring, validation, build and visual review requirements.
This skill orchestrates the batch; it does not replace those requirements.

## Fetch and freeze the batch

Run the following with the parsed offset substituted for `<offset>`:

```bash
python3 icon_set/scripts/generation_queue.py <offset>
```

Use the returned JSON's `briefs` array as a fixed worklist. Process every item
in that response in order. Keep the script's default page size (currently 10);
do not use `--all`, follow `next_offset`, or fetch replacement items as the
queue changes. Preserve the exact source UUIDs, source paths and editorial
content from the response. If fetching fails or the JSON is malformed, report
the error rather than treating it as an empty queue.

## Process each reference

1. Immediately before starting an item, read its current gallery status and
   saved reference brief from `/api/primitives/status` and
   `/api/primitives/briefs` using the original UUID and the same gallery server
   as the queue fetch. Use the existing API schema and authorized session.
   If it is no longer eligible, already generated, or being handled, record
   the reason and continue without overwriting the newer state. If current
   state cannot be read, report the item as blocked and continue.
2. Render and visually inspect the actual reference before deciding its
   classification or creating any Python original. A supplied `solo` family
   is not proof that the source is standalone. If the reference cannot be
   inspected or its interpretation remains ambiguous, report that limitation
   and skip drawing this item.
3. For a standalone subject, follow `/icon-solo-distilled`: search for an
   existing original by source ID, author the icon, validate to `valid` with
   zero warnings, build only that original, inspect the actual light and dark
   renders at 48 pixels, and verify the export in the solo manifest. Preserve
   source attribution and editorial details. Do not count unresolved
   validation, failed builds or uninspected renders as completed icons.
4. For a container or side combination, perform the combination intake below,
   skip all drawing for this source, and continue to the next item.

## Persist combinations before reporting them prepared

Follow the detailed payload rules in `/icon-solo-distilled`. Merge with the
current saved data, retaining useful editorial instructions and valid existing
component content. Describe the inspected components specifically; do not
replace them with generic placeholders or redraw typeface glyphs.

- POST to `/api/primitives/status` for the original UUID with `status: "skip"`,
  the review note, and both `main_brief` and `sub_brief`. Each brief must have
  `name`, `family`, and `description`. Container combinations use
  `reason: "container"`, main family `container`, sub family `sub`, and no
  `sub_position`. Side combinations use `reason: "combination"`, main family
  `solo` (or `container` for a wrapper), sub family `sub`, and the observed
  `sub_position`.
- POST to `/api/primitives/briefs` with `uuid`, the main component's `family`,
  and an amended `brief` explaining the split and deferred generation. Retain
  the exact source UUID/path and useful editorial details; replace obsolete
  instructions to draw the whole combination as one solo. There is no `side`
  family.
- Read back both endpoints for that UUID and verify the classification,
  saved reference family, and both component briefs against the intended
  payloads. A successful HTTP response alone is insufficient verification.

If either save or readback fails, explicitly report the UUID, which fields
were saved or remain unverified, the error, and the prepared payloads for
retry. Do not report the combination as prepared. Still skip drawing and
continue the batch. Do not start component generation jobs or alter the
original reference artwork.

## Batch report

Account for every queued UUID: generated icons (validation, visual findings
and output paths), verified prepared combinations (type and component names),
items skipped because their current status changed, and failures or unresolved
items. Include the requested offset and returned item count. Explicitly
identify any saving failures and retain their retry payloads. Continue past
individual failures without claiming that incomplete work succeeded.
