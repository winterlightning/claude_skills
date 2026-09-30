---
name: generate-png-solo
description: Draw a clean 48x48-ready solo line icon PNG for one or more subjects (black Lucide / Feather style strokes on white, uniform width, natural proportions) and save it under new-pipeline-test/output_png. The model picks the 2 to 4 recognizable parts and the overall shape, follows the fixed prompt as its drawing brief, generates the PNG with an image generation model (never hand-drawn code, never a library icon), checks it at 48 px, vectorizes it to <slug>_raw.svg in the same folder with new-pipeline-test/vectorize/process.sh, and reports. Use when asked to generate a PNG icon, draw an icon as PNG, or start the PNG -> vectorize -> redraw pipeline. Generated from .claude/skills/generate-png-solo/SKILL.md by icon_set/scripts/generate_skills.py; edit the source, not this copy.
---

# /generate-png-solo — subject in, PNG icon out

Use the subjects named in the user's skill invocation or request.

Run from the repository root containing `icon_set/`. The deliverable is a PNG made by an image generation model from the filled
brief. Do not stop at writing a prompt, do not draw the icon by hand in code,
and do not touch `published/`, the registered icon folders, or the build.

## Parse the request

- Split the arguments on commas or newlines. Each piece is one subject, a short
  noun phrase such as `coffee mug` or `paper plane`. Trim it.
- `--shape tall|wide|square|round` applies to every subject in the call and
  overrides the shape you would pick. Anything else is part of the subject text.
- If a piece is a path to an SVG or PNG, use `/generate-png-solo-with-reference`
  for that piece instead.
- `--source-id <uuid>` inside a piece is the original icon id that this
  drawing replaces or fixes; it belongs to that piece only. It becomes
  `SOURCE_ICON_ID` on the Solo48 model the redraw step writes, so it cannot be
  left out silently. Take it out of the piece before reading the rest.
- A piece without `--source-id`: ask the user for its original icon id before
  generating anything, one question listing every piece that lacks one.
  If the user says there is none (a brand-new concept), record
  `source_icon_id: null` and add a warning to the report. When you cannot ask
  (non-interactive run), do not guess an id: use `null` and warn.
- Never invent, derive or look up an id yourself; only the user or the
  caller supplies it. Keep it exactly as given.
- No subjects: say so and stop.

## Decide the drawing

For each subject decide, in Lucide / Feather terms:

1. **Parts.** The 2 to 4 features that make the subject recognizable at 48 px.
   Name concrete shapes and positions: "a rounded cup open at the top, a
   C-shaped handle on the right, two short steam lines above". Prefer the most
   common front or side view. No decoration, texture, brand marks, text or
   digits. Drop anything thinner than one stroke width or closer than one
   stroke width to another line.
2. **Shape.** One word for the overall silhouette: `tall` (portrait
   rectangle), `wide` (landscape rectangle), `square`, or `round`. Pick from the
   subject's natural proportions: a pencil is tall, a bus is wide, a clock is
   round, a mug is square.
3. **Stroke count.** At most 6 strokes or closed shapes. Merge or drop parts
   until they fit.
4. **People.** Any person, user, worker, athlete or body part in a pose is a
   stick figure, as in `icon_set/references/human_ref/full_body_ref.png`:
   detached circle head, single-line torso and limbs, round ends, no face or
   clothes. A bust is the circle head over one shoulder arc
   (`human_ref/user.svg`). Say "stick figure" in the parts sentence and
   describe the pose by limb positions ("left arm raised, legs apart").
   Held objects stay simple outlines next to the hand end of the arm.

A combination (a screen with an upload arrow, a folder with a plus badge) is
still one drawing; keep the hosted mark large and well separated. Text-only
subjects and logos get drawn too, with a one-line warning in the report.

## The brief you draw against

Fill this brief and follow every line of it while drawing. It is
`new-pipeline-test/prompt.md` with three lines filled: the shape word in
front, the parts sentence instead of "Reduce the subject...", and the exact
save path on the last line. The numbers are the SOLO48 rules: 1/12 stroke and
margin are 4 of 48 units, one stroke width of gap is the 8-unit spacing the
build gate enforces, half a stroke width is the 6-unit opening minimum.

```
{{SHAPE_WORD}} minimal line icon of {{SUBJECT}}, in the style of Lucide / Feather icons.
Show only {{PARTS}}, nothing else.

Style:
- Black outline strokes on a plain white background. No fill, no shading, no gradient, no color.
- One uniform stroke width, about 1/12 of the icon size. Round caps, round joins.
- Flat front view. Simple geometric lines, right angles and circular arcs.
- People: draw any person as a stick figure. A small outlined circle for the head, floating above the body with a clear gap, one line for the torso, one line per arm and leg with round ends. No face, hair, hands, fingers, clothes or body outline. A head-and-shoulders person is the circle head above one rounded shoulder arc, open at the bottom.

Layout:
- Keep the subject's natural proportions. A tall subject fits a portrait rectangle, a wide subject a landscape rectangle, a round subject a circle, a compact one a square.
- One icon, centered. Its longest side reaches a small even margin; the shorter side can leave more white space. Never stretch or squash the subject to fill the square.
- At least one stroke width of clear white space between separate lines.
- Openings and holes at least half a stroke width wide.
- At most 6 strokes. Drop any detail smaller than one stroke width.

Do not draw: text, letters, numbers, a border, a background tile or button, shadows, multiple variants.
The icon will be displayed at 48x48 pixels and must stay readable there.

Save the output as '/Applications/Workspaces/pictographic/claude_skills/new-pipeline-test/output_png/{{RUN_FOLDER}}/{{SLUG}}.png'
```

`{{RUN_FOLDER}}` is `<YYYYMMDD-HHMM>-<subject-slug>` (local time, e.g. `20260928-1435-coffee-mug`) and `{{SLUG}}` the subject
slug (lowercase, hyphens). Shape words: `Tall`, `Wide`, `Square`, `Round`.

## Generate the PNG with an image model

The point of this pipeline is a **freshly generated picture**, not another
hand-constructed drawing. Therefore:

- Never author the icon as SVG, path data, PIL/cairo/matplotlib drawing code,
  or any other geometry you write yourself.
- Never open, copy, trace or adapt an existing icon from `icon_set/`,
  `published/`, `pictographic-primitives/`, Lucide, Feather or any other
  library file. The reference (with-reference skill only) is looked at, not
  reused.
- The PNG must come out of an image generation model, using the filled brief
  as the prompt, verbatim.

Use the first of these that is available in the host:

1. **In Codex: you must trigger the `$imagegen` skill** (its built-in
   `image_gen` tool). Invoke it explicitly for every subject; do not decide on
   your own that the subject is "an icon better done in SVG". The imagegen
   skill's "when not to use" note about icon systems does **not** apply here:
   this pipeline exists to get a generated bitmap that is vectorized later,
   and the user has asked for it. Pass the filled brief as the prompt,
   unchanged, and ask for 1024x1024, PNG, opaque white background, no
   transparency.
   The tool saves under `$CODEX_HOME/generated_images/`; copy the selected
   output into the run folder as `<slug>.png` before finishing. Never leave
   the result only in `$CODEX_HOME`.
   In another host, use its native image generation tool the same way.
2. The OpenAI Images API when `OPENAI_API_KEY` is set (model `gpt-image-1`
   unless `IMAGE_MODEL` says otherwise):

   ```bash
   python3 - <<'PY'
   import base64, json, os, pathlib, urllib.request
   prompt = pathlib.Path("prompt.txt").read_text()
   req = urllib.request.Request(
       "https://api.openai.com/v1/images/generations",
       data=json.dumps({"model": os.environ.get("IMAGE_MODEL", "gpt-image-1"),
                        "prompt": prompt, "size": "1024x1024",
                        "background": "opaque", "output_format": "png"}).encode(),
       headers={"Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
                "Content-Type": "application/json"})
   data = json.load(urllib.request.urlopen(req))["data"][0]["b64_json"]
   pathlib.Path("SLUG.png").write_bytes(base64.b64decode(data))
   PY
   ```
   Run it inside the run folder with `SLUG` replaced.
3. Neither exists: stop, write `prompt.txt` and `choice.json` anyway, and
   report that no image generation model was available. Do **not** fall back
   to drawing the icon yourself, and do not treat "imagegen says not for
   icons" as the tool being unavailable.

After generation:

- Flatten to opaque white and collapse ink to black if needed
  (`new-pipeline-test/vectorize/pre_process_input.py` does this), keep the
  result as `<slug>.png` at 1024x1024.
- Check readability at 48 px without producing a 48 px deliverable: view the
  1024 PNG scaled down (a temporary downscale in your scratch directory, or
  the host's image viewer zoomed out). Never save a 48 px PNG into the run
  folder; 48x48 is the target the icon must survive, not an output.
- At 48 px every part must be identifiable and every gap visible; at 1024 px
  the strokes must be one width, unfilled, black on white, one icon with no
  tile or text. If not, adjust the prompt with one fix from
  "Fixing a bad result" and generate again, up to three times. Only the
  generation you judge best for vectorizing is kept, as `<slug>.png`. Rejected
  attempts stay in your scratch directory or `$CODEX_HOME/generated_images`;
  never copy them into the run folder. If none of the three is good, keep the
  best one and say what is still wrong.

## Vectorize the PNG

Every final `<slug>.png` is traced to SVG right away, in the same run folder,
so the redraw step in `new-pipeline-test/process.md` finds the PNG and its
SVG side by side. Run from the repository root:

```bash
new-pipeline-test/vectorize/process.sh \
  new-pipeline-test/output_png/<run-folder>/<slug>.png
```

The SVG is always written next to the PNG. Feed the 1024 px final PNG. The script flattens the PNG, traces one SVG per
connected component, merges them, fits the drawing onto a 1024x1024 canvas and
snaps it to the nearest keyshape. It saves only the finished
**`<slug>_raw.svg`**; the intermediates stay in a temp folder that is deleted
afterwards. The `done:` line reports the part count, e.g.
`done: .../<slug>_raw.svg (3 parts)`. A re-run overwrites `<slug>_raw.svg`.

Then check the result:

- View `<slug>_raw.svg` scaled to 48 px the same temporary way and compare it
  with the PNG. Do not save that render into the run folder either.
- Read the part count on the `done:` line. More parts than separate objects in the drawing
  means a stroke broke apart; fewer means two parts fused. A broken or fused
  drawing is a bad result: apply one fix from "Fixing a bad result" (usually
  the stroke or gap line), generate again, and vectorize the new final.
- If `process.sh` fails (no object SVGs, or the snap falls back to the
  pre-snap drawing), say so in the report; do not hand-edit the SVG.

## Save and report

- Folder `new-pipeline-test/output_png/<YYYYMMDD-HHMM>-<subject-slug>/` per
  subject. Never overwrite an earlier folder; a second run in the same minute adds `-2`, `-3`.
- Files: `<slug>.png` (1024, the one final generation), the vectorize output
  `<slug>_raw.svg` (nothing
  else from the vectorizer), `prompt.txt` (the filled brief that produced
  the final image), and `choice.json` with `subject`, `source_icon_id` (the
  original icon id as given, or `null`), `parts`, `shape`,
  `stroke_count`, `shape_source` (`user` or `agent`), `image_model` (`codex:image_gen`,
  an API model id, or the host tool name), `attempts`, and `created_at`.
- Reply with one line per subject: the PNG path, the `<slug>_raw.svg` path
  with its part count, the image model used, the parts you chose, and any
  warning. Show the 1024 PNG when the host can display images.

## Fixing a bad result

Change the prompt, then generate again. One change per attempt:

- Filled or silhouetted shapes: move "outline strokes only, hollow interior"
  to the first line.
- Uneven or tapered line width: lower "at most 6 strokes" to 4.
- Drawn on a rounded tile, button or with a shadow: add "on a plain white
  page, not on a button".
- Lines too thin to trace: change the stroke to "about 1/10 of the icon size".
- Tall or wide subject squashed square: repeat the shape word in the second
  sentence ("Show only ..., as a tall upright drawing").
- Parts merge at 48 px: drop the smallest part from the parts sentence.
- Wrong parts chosen: rewrite the parts sentence, more literal about position
  and count.
- Person came back with a face, hands, clothes or a filled body: start the
  parts sentence with "a stick figure with" and add "no face, no hands" to
  the do-not-draw line.
