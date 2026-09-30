"""hand-holding-rakhi-thread (redraw of the new-pipeline traced SVG).

Plan: a side-view hand entering from the left pinches a thread at its
fingertip; the thread drops to a round rakhi medallion whose two loose ends
curl down and out. SQUARE, centerline box (6,6)-(42,42).
- hand: one open contour, open at the wrist (x=6). Upper edge rises in a
  tangent S-bezier from the wrist (6,14) to the knuckle line y=6, runs flat to
  (28,6), turns round the fingertip on a semicircle r=6 about (28,12) and
  arrives at the pinch (28,18) heading left; the thumb/palm edge leaves the
  pinch slightly downward (a small notch, so fingertip and thumb read as
  meeting) and falls back in an S-bezier to the wrist (6,28). The wrist is 14
  tall, the fingers 12 thick.
- thread: a vertical line from the pinch (28,18) to the medallion top (28,28).
- medallion: a circle r=6 about (28,34), four cardinal quarter arcs split at
  the thread (top) and the two tie points (22,34) / (34,34).
- thread ends: mirrored beziers about x=28 from the tie points to (14,42) and
  (42,42), leaving the circle horizontally and landing horizontally.
Extremes: wrist x=6, knuckles y=6, right thread end x=42, both ends y=42.

Metric issues (hand-holding-rakhi-thread_metrics.json):
- stroke-width (trace 2.38 after fit): fixed, stroke 4 and every gap budgeted
  at 8 on centerlines.
- stroke-count (10, budget 6): fixed, 5 strokes (hand, thread, medallion, two
  thread ends); the two tiny bead rings and the curled-thumb loop are dropped.
- keyshape-short-axis (SQUARE y filled 72%): fixed, all four extremes on the
  box (knuckles y=6, thread ends y=42) by stacking hand over medallion.
- clearance errors e0/e2/e6/e8/e9 (bead rings on the thread ends, 1.8-7.5):
  fixed by dropping the beads; the ends now tie straight into the medallion.
- clearance errors e1/e5/e7/e3 (thumb loop inside the hand and the pinch,
  1.8-7.2): fixed by dropping the thumb loop -- the hand is 12 thick, which
  leaves no 16-wide band for an interior stroke -- and meeting finger and
  thumb at one tangent pinch node.
- clearance e3/e4, e5/e9 (hand vs medallion/thread): fixed, the medallion is
  hung 16 below the pinch (build-gate internal spacing thumb/ring >= 4 ink) so hand to ring is >= 8 on centerlines.
- hole: the medallion's inscribed opening is 8 (r=6, stroke 4); the hand's
  interior is >= 8 wide everywhere.
Reference: Lucide `hand-grab` / `hand` (tangent finger outline over an open
wrist); no Lucide rakhi exists, the medallion follows Lucide `circle`.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8b38c950-ec94-4fcb-a8d0-90a189601728"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1250-hand-holding-rakhi-thread/hand-holding-rakhi-thread_raw.svg"
AUTHOR = "claude-opus-5-5"

WRIST_X, WRIST_TOP, WRIST_BOTTOM = 6, 14, 28
KNUCKLE_Y, KNUCKLE_X = 6, 18
PINCH = (28, 18)                      # fingertip semicircle ends here
TIP_R = 6
MED_C, MED_R = (28, 34), 6            # medallion hung 16 below the pinch
END_Y, END_DX = 42, 14                # thread ends land 14 either side of axis


class HandHoldingRakhiThreadRedraw(Solo48):
    icon_id = "hand-holding-rakhi-thread-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ("rakhi", "raksha bandhan")
    keywords = ("rakhi", "raksha bandhan", "thread", "hand", "holding", "festival", "india", "bracelet")

    def build(self) -> None:
        px, py = PINCH
        top_end = (px, KNUCKLE_Y)
        self.add_bezier(
            "hand-back", (WRIST_X, WRIST_TOP),
            ((12, WRIST_TOP), (12, KNUCKLE_Y), (KNUCKLE_X, KNUCKLE_Y)),
        )
        self.add_line("hand-top", (KNUCKLE_X, KNUCKLE_Y), top_end)
        self.add_arc("fingertip", top_end, PINCH, radius_x=TIP_R, sweep=True)
        self.add_bezier(
            "thumb", PINCH,
            ((21, py + 1), (15, WRIST_BOTTOM), (WRIST_X, WRIST_BOTTOM)),
        )
        self.add_contour("hand", "hand-back", "hand-top", "fingertip", "thumb")

        cx, cy = MED_C
        r = MED_R
        top, right, bottom, left = (cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)
        self.add_line("thread", PINCH, top)
        ring = [top, right, bottom, left]
        for i, p in enumerate(ring):
            self.add_arc(f"medallion-{i + 1}", p, ring[(i + 1) % 4], radius_x=r, sweep=True)
        self.add_contour("medallion", "medallion-1", "medallion-2", "medallion-3", "medallion-4", closed=True)

        self.add_bezier("end-right", right, ((cx + 12, cy), (cx + 9, END_Y), (cx + END_DX, END_Y)))
        self.add_bezier("end-left", left, ((cx - 12, cy), (cx - 9, END_Y), (cx - END_DX, END_Y)))

        self.relate("connect", "hand", "thread")
        self.relate("connect", "thread", "medallion")
        self.relate("connect", "medallion", "end-right")
        self.relate("connect", "medallion", "end-left")
