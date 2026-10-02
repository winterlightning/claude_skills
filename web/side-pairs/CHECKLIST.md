# Side pairs: features of the old page (the spec)

The old Progression › Side page (`side-pairs-grid.js`, `side-layout-editor.js`, `side-pair-maker.js`,
`side-repair-flags.js` at commit `4c7f6f9795^`). Each row must work in the Svelte page, or be marked as a
deliberate change. Combined icons are composed in the browser (`combine-side.js`); the Worker only stores them.

Status: ☐ to do · ☑ shown working in Chrome · ✕ deliberately dropped (reason given)

## L · The list

| # | Feature | Status |
|---|---|---|
| L1 | Summary: N side pairs, made from M main icons (D drawings) and S sub icons (D drawings) | ☑ |
| L2 | Summary: Main icons Generated / Needs fix / Not generated, each linking to `side-mains.html?status=` | ☑ |
| L3 | Summary: Sub icons Generated / Text / Needs fix / Not generated, linking to `side-subs.html?status=` | ☑ |
| L4 | Summary: Icon review states of main and sub drawings (Approved / To review / Needs fix / Rejected) linking to `index.html?family=side_main|side_sub&status=` | ☑ |
| L5 | Summary: combined icons Approved / To review / Needs fix linking to Icon review (`side_combination64`) | ☑ |
| L6 | Build all: one button building every pair whose parts are drawn (was "Combine N approved side pairs"), with progress and result | ☑ |
| L7 | Search: concept, pair id, main / sub reference ids, their concepts and icon names | ☑ |
| L8 | Filter: All, Ready, Fix sub, Fix main, Waiting, Needs main, Needs sub, Needs text sub, Not combined, Text sub, 2+ subs, From review, Main / sub changed | ☑ |
| L9 | Group: No grouping / Group by main / Group by sub; groups sorted by size, open state kept, heading with shared icon, its size and pair count | ☑ |
| L10 | Page size 24 / 48 / 96 (pairs or groups per page); Previous / Next at top and bottom | ☑ |
| L11 | Filter, group, page size and search kept in the URL | ☑ |
| L12 | Status line for the last action (built, applied, kept…) | ☑ |
| L13 | "N disapproved" count of mains / subs (repair flags toolbar) | ☑ |

## C · Each pair

| # | Feature | Status |
|---|---|---|
| C1 | Row: Original → Main · 48 → Sub · 32 → Combined · 64 | ☑ |
| C2 | Head: concept, side and canvas ("Bottom-right · 64×64"), status badge with hint | ☑ |
| C3 | Badges: Text sub, From review, Main / sub changed, "N mains · showing first", Adjusted layout, Outdated: recombine (with which part changed) | ☑ |
| C4 | Original reference image, or "Reference missing" | ☑ |
| C5 | Part figure: picture, caption with ink size ("Sub 28×24 / 32"), native size, or "generated"; "Main needed" / "Sub needed" | ☑ |
| C6 | Fix badge on a part with its reasons: fails validation, model validation, needs a SUB32 redraw, ink exceeds 32×32, disapproved / rejected | ☑ |
| C7 | Click a part: inspect dialog (artwork + centerline / artwork / centerline, grid, facts: pair, family, canvas, ink, sizing, validation, SUB32 status, problems, Python model, SVG) | ☑ |
| C8 | Edit main icon / Edit sub icon (stroke editor, `side-component-editor.js`) | ☑ |
| C9 | Combined icon; click it: popup with main / sub bounds, centerline, download | ☑ |
| C10 | Recombine this icon / Recombine (outdated): build from the current drawings | ☑ |
| C11 | Edit layout button under the combined icon (opens the layout editor) | ☑ |
| C12 | Change main / sub: picker with search, candidates (approved / fails badges), "None of these: it needs drawing" name, position, Save, Close, Remove / Use published | ☑ |
| C13 | "To draw: name" under a part a saved pair still waits for (kept in `reference_parts.draw_name`, migration 0016) | ☑ |
| C14 | Download SVG (marked once clicked) | ☑ |
| C15 | Main and sub review: status chip, Approve, Disapprove, optional feedback note | ☑ |
| C16 | Several subs: pick one, "Keep this sub · remove others" | ✕ a pair has one sub per size in the combination tables |
| C17 | Log in prompt for guests ("Log in to recombine this icon or adjust its layout") | ☑ |
| C18 | Approve / Disapprove the combined icon (added on the new page) | ☑ |

## E · The layout editor

| # | Feature | Status |
|---|---|---|
| E1 | Title "Adjust layout · concept"; Close | ☑ |
| E2 | Click selects: Whole icon / Element / Path (path splits that element) | ☑ |
| E3 | Shift- or ⌘ / Ctrl-click adds or removes; a click on artwork under the selection frame picks it | ☑ |
| E4 | Drag moves the selection; 8 handles (corners and edges) resize with the opposite side pinned | ☑ |
| E5 | Width and height independent; Shift keeps proportions | ☑ |
| E6 | Dragged edge lands on a grid line; touching pieces stay touching | ☑ |
| E7 | Arrows move 1 (Shift 8); Alt+arrows resize by 1; + / − both sides; Esc clears the selection | ☑ |
| E8 | Size presets main 32–64 / sub 20–44 (every 4), Free, painted size; keyshape tiles at the chosen size with painted sizes, "· own" | ☑ |
| E9 | Dashed keyshape guide of the chosen preset | ☑ |
| E10 | Canvas shows main and sub whole (editing view), one-unit grid, every 8 stronger; strokes keep 4 units | ☑ |
| E11 | Centerline toggle (kept between visits) | ☑ |
| E12 | Live label on the frame: ink W×H · box W×H · at x,y; red when outside the canvas | ☑ |
| E13 | Element list: per part, each piece by name with its size, tick to select; child paths tick to split; Select all per part | ☑ |
| E14 | Split into paths; Clear selection | ☑ |
| E15 | Combined result beside the canvas (the sub erases the main), with its centerline | ☑ |
| E16 | Output at 32, 48 and 64 px | ☑ |
| E17 | Readout: "N elements: painted W×H at (x, y)", outside-canvas warning | ☑ |
| E18 | Save layout (disabled while nothing changed or outside the canvas) | ☑ |
| E19 | Reset to automatic (saves the pair with no layout) | ☑ |
| E20 | Discard changes (back to the saved layout) | ☑ |
| E21 | A saved layout that no longer fits the drawings: opens automatic with a warning | ☑ |
| E22 | Apply to pairs using this main: same side / other sides lists with picture, side, sub, "different sub" and "adjusted" badges, Select all / none, "Save + apply to N pairs", ✓ / ✕ per pair | ☑ |
| E23 | Apply moves the layout like `combination_layouts.transfer` (same side copies; other side re-anchors each part; a different sub fits its own groups to the edited sub's box) | ☑ |

## A · Added since (kept)

| # | Feature | Status |
|---|---|---|
| A1 | 64 / 72 switch; at 72 main-54 / sub-36 parts, sizes main 38–70 / sub 24–48, tracer's 54 / 36 keyshapes | ☑ |
| A2 | State filter Built / Stale / Not built / Needs a drawing; Rebuild every stale pair | ☑ |
| A3 | `?edit=<id>` opens a pair's editor; `?make=<primitive>` makes a side pair from a primitive | ☑ |

## Svelte version (step 2)

The page is now the Svelte app in `web/side-pairs` (`npm run build` in `web/` writes `side-pairs-app.js` / `.css` to
`published/gallery`). Every row above was rechecked in Chrome against the old scripts side by side (the old
`primitives.html` with `side-pairs-grid.js`, `side-layout-editor.js`, `side-pair-maker.js`), on next's data read-only,
with the same scripted clicks and keys on both pages:

- List: every filter, grouping (main / sub, 24 / 48), page size, page 2 and five searches give the same rows; the
  summary, its links, the build bar, toolbar options and each row's text, buttons, links and images match on the
  first page and on Fix sub, Fix main, Changed, From review, Stale, Not built, Not combined, Text sub, and at 72.
- Rows: inspect main / sub (three views), the combined popup, Change main / sub (search, pick, the save request),
  Recombine and combined Approve (same requests), download mark, guest view, groups staying open, `?edit` / `?make`.
- Editor: 32 steps (clicks, Shift-clicks, arrows, Alt+arrows, + / −, moves, corner / edge / Shift drags, levels,
  list, split, presets, keyshapes, Free, centerline, Apply layout, Save, Apply to 8 pairs, Discard, Reset) at 64 and 72
  show the same readout, frame label, buttons and artwork; Save, Save + apply and Reset send byte-identical requests.
  A saved layout that no longer fits opens with the same warning (E21).
- Build: Rebuild stale sends the same 45 builds and reports the same result.

Kept from the old page on purpose: the layout markup and class names (so `site.css` and the reused scripts work).
One old quirk not copied: after Save, the old editor left "Reset to automatic" disabled until the next redraw.
