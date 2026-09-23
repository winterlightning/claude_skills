---
name: fix-icon-queue
description: Take the next disapproved Pictographic icon from the shared production work queue, fix it, and report the result. Claims the icon on production first so no other machine or agent fixes the same one, then repairs it with the matching family skill, publishes, and reports done (the revision returns to Ready) or cannot-fix. Use when asked to work through disapproved icons, process review feedback, or run the fix queue. Hand-authored; edit this file directly.
argument-hint: [--family sub|solo|container] [--worker hostname/agent]
---

# /fix-icon-queue — claim, fix, report one disapproved icon

Request: $ARGUMENTS

Run every command from the `claude_skills` directory containing `icon_set/`.
The maintained source is `.claude/skills/fix-icon-queue/SKILL.md`; regenerate
its Codex and portable copies with `icon_set/scripts/generate_skills.py`.
Full reference: `docs/work-claims.md`.

## Why the queue exists

Reviews live in **one database, on production**. Several machines and agents
fix icons at the same time. Before touching an icon you must **claim** it on
production; the claim is what stops another machine from taking the same icon.
An icon is claimable only while its review status is Disapproved and nobody
holds a live claim. After you report `done`, production sets that revision back
to **Ready** for the reviewer and keeps it out of the queue until a reviewer
disapproves it again.

Never fix an icon you have not claimed. Never report `done` without a saved,
validated fix.

## Procedure

1. **Identify yourself.** Set the worker name once per session; it is stored on
   the claim and must match on every later call:

   ```bash
   export PICTOGRAPHIC_WORKER="$(hostname -s)/<your-model>"   # e.g. mac-a/claude-fable-5-1
   ```

   The API base defaults to the production tunnel recorded in `deploy.py`;
   override with `--base-url` or `PICTOGRAPHIC_API` when it changed.

2. **Claim the next icon.** Pass `--family` when the request names one.

   ```bash
   python3 icon_set/scripts/work_queue.py next --family sub --out fix-input.txt
   ```

   Exit code 3 means the queue is empty: report that and stop. The brief lists
   the icon key, family, Python source, current `svg_sha256`, disapproval reason,
   the reviewer's feedback, and the reference SVG when one is declared. Read the
   feedback as the specification. Inspect the reference and the current Python
   source before drawing.

3. **Fix it with the family skill.** Preserve the parent: author the repair as a
   new variant (`python3 icon_set/scripts/create_variant.py --icon <id> --family <family> --label "<what changed>"`)
   or, for a sub icon that fails validation, run `/fix-icon-sub` with the
   original reference and the current icon. Use `/icon-solo`, `/icon-sub`,
   `/icon-container` or `/icon-avatar` for the drawing rules of that family.
   Validation must be `valid` with zero warnings; a `review` is not a pass.

4. **Build and publish only this icon.** Never run a full library build or a
   plain `publish` for one fix.

   ```bash
   python3 -m icon_set build --icon <path-to-new-variant.py> --no-png --no-report
   python3 -m icon_set publish --no-build      # compacts catalogs, writes release.json, no rebuild
   ```

   Inspect the export at native size in both themes. Commit the new Python
   module together with the files the build touched under `published/`
   (the family folder, `gallery/icons.json`, `release.json`), then push.
   Production receives the new revision on its next pull.

5. **Report.** Choose exactly one:

   - Fixed: `python3 icon_set/scripts/work_queue.py done --icon <key> --note "<variant id or commit>"`
     The disapproved revision returns to Ready; its feedback is kept so the
     reviewer can compare.
   - No meaning-preserving drawing passes: `python3 icon_set/scripts/work_queue.py cannot-fix --icon <key> --note "<the blocking check and element>"`
   - You must stop without a result: `python3 icon_set/scripts/work_queue.py abandon --icon <key>`
     so another machine can take it. A claim you neither report nor extend
     expires after 3 hours (`heartbeat` extends it).

6. **Say what happened.** Name the icon key, the variant or module you wrote,
   the validation status, the report you sent, and the queue position left
   (`python3 icon_set/scripts/work_queue.py queue --family <family>`).

## Never

- Skip the claim, or work on an icon the queue reported as `working`, `done`
  or `cannot-fix` for someone else.
- Report `done` for an unvalidated, unpublished or unrelated change.
- Reuse another worker's name, or change the production status through
  `/api/reviews` to hide a failed fix.
- Edit the registered parent module in place; repairs are new variants.
