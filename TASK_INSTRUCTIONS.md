# TodoPusher files — claude_skills

This folder is a TodoPusher project. Two files at the project root are kept in
two-way sync with the app: the app rewrites them when something changes in the
app, and edits made to the files are picked up within a second.

| File | Holds | Edit it to |
|---|---|---|
| `TASKS.md` | the task list | queue work for the agent |
| `DESCRIPTION.md` | the project description | describe what the project is |

# Tasks: `TASKS.md`

To queue work for the agent, add a line to `TASKS.md`. Nothing else is needed.

## Format

```markdown
## Queued

- [ ] Add a retry to the upload client
  Wrap the PUT in a three-attempt retry with backoff. Every line after
  the first is indented by two spaces and is still part of the prompt.

- [ ] A one-line task is just its line

## Backlog

- [ ] Something for later
  Continuation lines here too.

## Done

- [x] A finished task (tp:1a2b3c4d)
```

## Rules

- **One task per `- [ ]` line.** The text on that line is the prompt sent
  to the agent — there is no separate title. Write it as a complete
  instruction; the first line is what shows in tab titles.
- **Indented lines continue the prompt.** Indent each by two spaces. A
  blank line ends the prompt only if the next non-blank line is not
  indented.
- **The section heading is the status.** `## Queued` runs next (top first,
  in order), `## Backlog` waits, `## Done` and `## Failed` are finished.
  Move a line between sections to change its status.
- **Check the box to finish.** `- [x]` anywhere marks the task done. An
  unchecked line under `## Done` reopens it into the backlog.
- **Never write or change `(tp:xxxxxxxx)` tags.** The app appends one to
  each line it owns. New lines you add must have no tag; the app assigns one
  on the next sync. Deleting a tagged line deletes that task.
- **Running tasks are protected.** A task that is currently running cannot
  have its status changed or be deleted from the file. Its prompt still
  updates.
- **Do not restructure the file.** Keep the `## Queued` / `## Backlog` /
  `## Done` / `## Failed` headings as they are; the app regenerates
  everything outside the task lines.

## Example: queueing a follow-up

```markdown
## Queued

- [ ] Fix the flaky login test
  tests/auth/login_test.py fails about one run in five with a timeout on
  the token refresh mock. Find the race, fix it, and run the suite three
  times to confirm it is stable.
```

Save the file. The app assigns the task a tag, and if Auto is on it is
pushed into the terminal as soon as the current turn ends.

# Description: `DESCRIPTION.md`

The project description is shown under the project name in the app: the
first three lines in the header, the whole thing in its own tab. It is
the context a person gets at a glance before reading any task, so keep it
current. To write or update it, edit `DESCRIPTION.md`.

## Format

The file starts with an HTML comment the app owns; everything after it is
the description, as markdown.

```markdown
<!--
Synced with the TodoPusher app: this file is the project's description, ...
-->

Upload service for the mobile app. Go, deployed to Fly.io from `main`.

- API: `cmd/server`, handlers in `internal/http`
- Storage: S3 via `internal/blob`; local disk in dev (`make dev`)
- Run tests with `make test`; integration tests need `LOCALSTACK=1`
```

## Rules

- **Keep the leading comment.** The app strips it when reading and writes
  it back; only the text after it is the description.
- **Write for a reader who has never seen the project.** Lead with one
  sentence saying what the project is and the stack it uses; the header
  shows only the first three lines, so put the most useful facts first.
- **Then the facts that save a reader time.** Where the entry points are,
  how to build, test, and run, conventions that are not obvious from the
  code, and links (relative paths and URLs are clickable in the app).
- **Markdown, short.** Headings, lists, code spans, and links render;
  aim for a screenful, not a manual. Deeper documentation belongs in the
  repo — link to it.
- **Replace, do not append.** The file is the whole description. Rewrite
  stale parts instead of adding "update:" notes; an empty file (after
  the comment) clears the description.

Save the file. The app picks it up within a second and shows it under the
project name.
