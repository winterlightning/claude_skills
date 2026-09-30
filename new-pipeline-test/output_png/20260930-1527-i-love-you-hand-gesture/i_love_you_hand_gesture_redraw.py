"""I love you hand gesture (redraw of the new-pipeline traced SVG).

Plan: a palm-facing hand making the ASL "I love you" sign, one open outline
from the left wrist round to the right wrist.
- Index finger (walls x 12/20, r4 tip, top y 8) and a shorter little finger
  (walls x 36/44, r4 tip, top y 12) stand up as 8-wide tubes.
- Middle and ring fingers fold down as two r4 knuckle bumps sharing the finger
  walls (x 20-28-36, y 25), each wall carried 3 below the bumps as a short
  crease stub so the folds read as fingers.
- The thumb sticks out left on a 1:3 band: upper edge from the index wall
  (12,23) to the r5 cap top (9,22), cap centre (9,27) reaching x 4 exactly,
  lower edge flowing into the palm side.
- Palm sides are cubics that curve in and land vertically on a 20-wide open
  wrist (x 18/38, y 40), mirrored about the finger block's axis x 28 where the
  thumb allows.

Keyshape: HRECT_L, not the suggested VRECT_L. Two 8-wide fingers and two 8-wide
knuckles already need 32, the full VRECT_L width, which leaves no room for the
outward thumb that tells this sign apart from the rock "horns" hand.
HRECT_L gives 40: 32 for the fingers and 8 for the thumb.

Metric issues:
- clearance e0/e1 (6.11) and e2/e3 (5.52): fixed. Walls are 8 apart and the
  knuckle arcs share their end nodes with the finger walls (connected, not near
  misses).
- keyshape-short-axis (y fill 93%): fixed. Every extreme sits on the HRECT_L
  centerline box (4,8)-(44,40): thumb x 4, little finger x 44, index tip y 8,
  wrist y 40.
- stroke-width (trace 2.46 vs 4): handled by redrawing at stroke 4 with
  8-unit centerline spacing instead of scaling the trace.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5a3ae175-815d-4ada-bbd0-26b81be8cd4e"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1527-i-love-you-hand-gesture/i-love-you-hand-gesture_raw.svg"
AUTHOR = "claude-opus-5-5"

INDEX_L, INDEX_R, INDEX_TOP = 12, 20, 8     # index tube, r4 tip
PINKY_L, PINKY_R, PINKY_TOP = 36, 44, 12    # little finger tube, r4 tip
KNUCKLE_Y, CREASE_Y = 25, 28                # folded-finger bumps, crease stub ends
THUMB_C, THUMB_R = (9, 27), 5               # thumb cap centre; leftmost x 4
WRIST_L, WRIST_R, BASE = 18, 38, 40          # open wrist, palm curves end vertical
PALM_SIDE_Y = 30                            # little-finger wall turns into the palm curve


def _path(icon, name, start, steps, closed=False):
    """steps: (x, y) line | ((x, y), r, sweep[, large]) arc | ('c', c1, c2, end) cubic."""
    members, point = [], start
    for i, step in enumerate(steps):
        member = f"{name}-{i + 1}"
        if step[0] == "c":
            icon.add_bezier(member, point, (step[1], step[2], step[3])); point = step[3]
        elif isinstance(step[0], (int, float)):
            icon.add_line(member, point, step); point = step
        else:
            end, r, sweep = step[:3]
            large = step[3] if len(step) > 3 else False
            icon.add_arc(member, point, end, radius_x=r, radius_y=r, sweep=sweep, large_arc=large); point = end
        members.append(member)
    icon.add_contour(name, *members, closed=closed)
    return members


class ILoveYouHandGestureRedraw(Solo48):
    icon_id = "i-love-you-hand-gesture-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "wayfinding"
    aliases = ("ily sign", "asl i love you", "love hand sign")
    keywords = ("i", "love", "you", "hand", "gesture", "sign language", "asl", "fingers", "thumb")

    def build(self) -> None:
        cx, cy = THUMB_C
        tip = (INDEX_R - INDEX_L) // 2
        mid = (INDEX_R + PINKY_L) // 2
        cap_top = (cx, cy - THUMB_R)            # (9,22): circle top, 1:3 upper edge
        cap_low = (cx - 3, cy + 4)              # (6,31): 3-4-5 point, lower edge
        crotch = (INDEX_L, cap_top[1] + 1)      # (12,23): 1:3 back to the index wall
        _path(self, "hand", (WRIST_L, BASE), [
            ("c", (WRIST_L, BASE - 5), (cap_low[0] + 4, cap_low[1] + 3), cap_low),
            (cap_top, THUMB_R, True),
            crotch,
            (INDEX_L, INDEX_TOP + tip),
            ((INDEX_R, INDEX_TOP + tip), tip, True),
            (INDEX_R, KNUCKLE_Y),
            ((mid, KNUCKLE_Y), tip, True),
            ((PINKY_L, KNUCKLE_Y), tip, True),
            (PINKY_L, PINKY_TOP + tip),
            ((PINKY_R, PINKY_TOP + tip), tip, True),
            (PINKY_R, PALM_SIDE_Y),
            ("c", (PINKY_R, PALM_SIDE_Y + 5), (WRIST_R, BASE - 5), (WRIST_R, BASE)),
        ])
        for name, x in (("crease-index", INDEX_R), ("crease-middle", mid), ("crease-pinky", PINKY_L)):
            self.add_line(name, (x, KNUCKLE_Y), (x, CREASE_Y))
            self.relate("connect", name, "hand")
