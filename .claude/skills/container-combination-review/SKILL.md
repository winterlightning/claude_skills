---
name: container-combination-review
description: Review the layout of Pictographic container combination icons (a CONTAINER64 container with a SYMBOL32 symbol inside) and adjust it - for each pair, look at how the combination reads and balances, then pick the symbol's size and position (usually 32, bigger for a complex symbol in an open frame, smaller when the largest fit looks crowded, moved when it sits off the shape the eye reads), checked against the 4 px gap and recorded as a proposal the user approves on the review page (small.html); report what a layout change cannot fix. Never redraws an icon, never approves, never overrides a user approval. Arguments are a container id, reference ids, --next N (the next N containers with undecided pairs) or --recheck CONTAINER. Use when asked to review container combinations, check or fix their layout, or size and position their symbols. Hand-authored; edit this file directly.
---

# /container-combination-review — review and adjust the layout of container pairs

A container pair is a CONTAINER64 container (circle, pin, monitor, folder ...) with a SYMBOL32 symbol placed in its
room. `combo.py` builds every pair; this skill reviews each combination as a whole - does it read, is it balanced -
and adjusts its layout: **how big the symbol is and where it sits**. Problems a layout change cannot fix (a symbol
that is the wrong subject, too wide for any room, a container whose room centre is wrong) are reported, not forced. You propose; the user approves on the size review page; **Apply**
writes `combos.json` and recombines.

Work folder: `icon_set/work/container-combination64/` (run every command from there, with
`/opt/homebrew/bin/python3`).

This workflow requires that local experiment folder, including `combo.py`, `size_pick.py`,
`size_server.py` and its pair data. Check those resources before starting; they may be absent
in a fresh checkout. If they are missing, report the missing paths instead of inventing data or tools.

## What you decide

| | |
|---|---|
| **size** | any even number 16..40: the symbol's 32 box scaled to it (stroke stays 4) |
| **position** | `offset` [dx, dy] in whole units from the container's room centre (absolute, as `combos.json` holds it) |
| **hard limit** | the symbol's ink keeps **at least 4 px** from the container's ink and stays on the canvas; `propose` refuses anything else |

Not the largest by default, not the smallest: the size that makes the combination read best.

## Scope of one run

- **One container is one unit of review.** Every run takes a whole container: all of its symbol pairs are looked at
  together, so sizes and positions stay consistent across the group. `--next N` = N whole containers, one after the
  other; a container id = that container. Reference ids are only for a re-look at single pairs a user points at.
- **Pairs without a decision are proposed.** Pairs the user approved are not re-proposed (the server refuses it), but
  they are the reference for the rest: look at them first (`look CONTAINER --all`) and match their sizes and
  positions unless a pair clearly needs otherwise.
- **`--recheck CONTAINER`** reviews the container again: every pair except the user's approvals gets a fresh look and,
  where it changes, a new proposal (`look CONTAINER --all`, then propose the changed ones).
- Finish a container before starting the next: every undecided pair proposed, `report` checked.

## How to judge (from the user's own 1,075 approvals, 2026-10-13)

1. **32 is the baseline.** If 32 keeps 4 px, take 32 unless one of the rules below applies. (The user kept 32 for 129
   of 143 circle pairs although 36-40 fitted.)
2. **If 32 does not fit, take the largest size that does** - a tight 4-5 px fit too. This alone matched the user's
   size on 93.5% of their approvals; `look` marks it as `rule` (`*` on the sheet).
3. **Go above 32 (34-40) only when all of these hold**, and look before you do:
   - the symbol is **complex with fine detail** that clogs at 32 - several parts or small inner shapes: atom, bicycle,
     handshake, car horn, broccoli and carrot, chili trio, tulip, woman bust, fingerprint, face, currency signs with
     double bars (₩ ₴ ฿);
   - it is **roughly square** (aspect about 1.25 or less) - a long arrow or a flat bar never goes up;
   - the container is an **open, even frame** (`open_frame` true: circle, rounded square, camera viewfinder, brackets,
     house, oval bubble, head profile) - never a pin, monitor, folder, calendar, phone, watch or document;
   - the bigger symbol keeps **5 px or more** and the container still reads as a frame around it (the symbol does not
     fill it edge to edge).
   About 1 pair in 12 qualifies. Typical step: 36 (circle 28 -> 36, viewfinder 32 -> 36-40, house 24 -> 34).
4. **Simple, thin or long symbols stay at 32** even when 40 fits: single lines, minus, arrows, chevrons, dots,
   ellipsis, plus, check, a single letter-like stroke. Big and simple looks heavy and empty.
5. **Go smaller than the largest fit when it looks crowded.** A fit at 4.0-4.3 px where the symbol presses on a
   feature (a tab, a stand, a strap, the narrowing of a pin, a cross arm) reads cramped; one step down (2-4 units) with
   5-7 px of air is better. User examples: eye in the head profile 32 -> 28, text lines in the round smartwatch
   30 -> 24, volume icon in the smartwatch 32 -> 28, paw in the medical cross 30 -> 20, car in the crown shield 30 -> 28,
   star in double circles 24 -> 20.
6. **Position for balance, not just for room.**
   - Keep the current position unless the symbol looks off-centre in the shape the eye reads: a pin's round head (not
     the point), a folder's body (below the tab), a monitor's screen (above the stand), a bubble's body (not the tail),
     a house's walls (under the roof).
   - Compare `near` (the smallest move that keeps 4 px) with `centred` (the position with the most air on all sides,
     within 4 units). Prefer moves of 0-2 units; a 4-6 unit move needs a visible reason.
7. **Be consistent inside a container.** Similar symbols get the same size and position (all currency signs in the
   circle, all people in the viewfinder, all arrows in the bubble), unless one is much more complex.
8. **Text pairs are out of scope** (their size comes from the typeface fit); so are pairs with a crossing mark (the
   prohibited slash).

## Workflow

0. **Prepare.**
   - The size server must run: `curl -s http://127.0.0.1:8766/api/size-decisions >/dev/null || (/opt/homebrew/bin/python3 size_server.py &)`
     (run it in the background; it serves small.html and keeps `size-decisions.json`).
   - If a symbol module or `combos.json` changed since `combos-every.json` was written, run `combo.py --every` first.
1. **Pick the work.** `size_pick.py todo --next N` lists containers with undecided pairs (largest first). With a
   container id, take that one; with reference ids, `look --refs ...`. One container at a time.
2. **Look.** If the container has approved pairs, run `size_pick.py look CONTAINER --all` first and note the sizes and
   positions the user chose (the JSON's `decision`); they set the standard for the rest. Then
   `size_pick.py look CONTAINER` writes `size-review/CONTAINER-<n>.png` (8 pairs per sheet) and
   `size-review/CONTAINER.json`. Each sheet row is one pair: the pair now, then every size that keeps 4 px at its
   `near` position (top) and its `centred` position (below, when different), each labelled `size dx,dy g<gap>`; the
   left column has the concept, symbol, parts / segments / aspect and the `rule` pick. Open every sheet and look at
   the pairs at their real size - numbers alone never decide.
   The JSON per pair has `now`, `decision` (an existing one), `symbol_facts`, `open_frame`, `fits`
   (`near` / `centred` offsets and gaps), `too_tight` (sizes that cannot keep 4 px, with their best gap) and `rule`.
3. **Decide each pair** with the rules above: start from `rule`, then ask *does it read? is it balanced? is it
   consistent with its neighbours?* When unsure between options, or when you want a position the sheet does not show,
   render them: `size_pick.py try REF --size 32 --offset 0,-2 --size 36 --offset 0,-2` -> `size-review/try-<ref>.png`
   with gap and ok/NO per option.
4. **Record.** Write the picks to a JSON file (one per container is fine), each with a short reason a person can check:
   ```json
   [{"reference_id": "...", "size": 36, "offset": [0, -1], "reason": "complex atom, open circle, 36 keeps 6 px"},
    {"reference_id": "...", "size": 32, "offset": [0, 0], "reason": "32 baseline"}]
   ```
   then `size_pick.py propose picks.json --by <your-model-id>`. It re-renders each pick, refuses any with gap < 4 or off
   the canvas (fix and re-run those), saves the drawing to `small/prop/<ref>.svg`, and records it as **propose** with
   your reason. It skips pairs the user approved. Propose every undecided pair of the container, including the
   plain 32s, so the user can approve the container in one click.
5. **Check.** `size_pick.py report CONTAINER` lists what is decided; every size above 32, below the current size or
   moved must have a reason that matches the drawing.
6. **Report to the user** (per container): the counts by size, each pick above 32 and each pick below the largest fit
   with its reason, anything that needs more than a size (a symbol too wide for the room, a room centre that is wrong,
   a symbol that should be redrawn), and the link http://127.0.0.1:8766/small.html (filter **Proposed**; the container
   dropdown jumps to it).

## What the user sees

On small.html a proposed card has a purple border and a note `✦ <model>: 36 ↦ 0,-1 · <reason>`, with that size
preselected. **Approve** (or **Approve all** for the container with "each card's pick") turns it into the user's
approval; **Undo** on an approved proposal goes back to the proposal. Only approvals are applied.

## Never

- Approve, apply, or edit `combos.json` / `size-decisions.json` by hand - proposals go through `size_pick.py propose`.
- Replace or re-propose over a pair the user approved (the server refuses it; do not work around it).
- Pick a size or position that keeps less than 4 px, or go past 40, to make something "fit".
- Redraw, swap or edit a symbol or container module; report it instead.
- Size text pairs or crossing-mark pairs.

## Files

| File | |
|---|---|
| `size_pick.py` | todo / look / try / propose / report / backtest (this skill's helper) |
| `size_server.py` | serves small.html on :8766, keeps `size-decisions.json`, applies approvals to `combos.json` |
| `small_scan.py` | builds small.html (`--page` only rewrites it); the full scan refreshes the size options |
| `size-decisions.json` | `{ref: {size, offset (absolute), status: approve|propose, by, reason, gap, img, applied_*}}` |
| `size-review/` | review sheets and facts |
| `combos.json` | what combo.py reads; written only by Apply |
