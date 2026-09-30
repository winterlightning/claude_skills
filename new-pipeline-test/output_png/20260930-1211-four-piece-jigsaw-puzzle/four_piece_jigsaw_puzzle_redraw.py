"""four-piece-jigsaw-puzzle (redraw of the new-pipeline traced SVG).

Plan: a rounded square frame cut into a two-by-two puzzle by one cross of
seams, on SQUARE (centerline box (6,6)-(42,42)).
- frame: rounded square, corner r4, split at the four seam feet so every
  seam shares an endpoint with it.
- cross: vertical seam x=CROSS, horizontal seam y=CROSS, meeting at
  (CROSS,CROSS); four seam halves, all declared connected.
- tabs: one r4 semicircle knob on each long seam half, centred on it so the
  knob sits exactly 8 (centerline) from the frame and from the crossing seam.
  The bottom-right piece pushes one tab up into the top-right piece and one
  tab left into the bottom-left piece; the drawing is mirror-symmetric about
  the (6,6)-(42,42) diagonal.
Keyshape: SQUARE as suggested (fill 1.0/1.0, square subject).

Reduction: the trace has four tabs on a centred cross. At stroke 4, a tab
needs 8 + 2*4 + 8 = 24 units of seam (8 to the frame, the knob, 8 to the
crossing seam), but a centred cross leaves only 18 per half. Drawn that way,
the build gate fails with 8 undersized holes and zero ink clearance between
knob and frame. So the cross moves to 18: the two long halves (24 each) carry
one tab each, and the two short halves stay straight.

Metric issues fixed:
- clearance e0/e1 7.62 and e0/e2 7.84: every knob now sits 8 or more from the
  frame (exactly 8 at each knob apex).
- clearance e1/e2 0.0 (seams crossing): the seams are split into four halves
  that share the (18,18) junction and are declared connected, not left as an
  undeclared overlap.
- stroke width 2.76 -> 4, with every gap budgeted for stroke 4.
Not fixed as drawn: four tabs on a centred cross (reduced to two, see above).
Lucide reference: icon_set/references/lucide/original/puzzle.svg (a
semicircle-ish tab interrupting a straight edge).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "cab69194-7d72-4ec5-92ef-c43974df941f"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1211-four-piece-jigsaw-puzzle/"
    "four-piece-jigsaw-puzzle_raw.svg"
)
AUTHOR = "claude-opus-5-5"

LO, HI = 6, 42           # SQUARE centerline box
CORNER = 4               # frame corner radius
CROSS = 18               # seam crossing (x and y)
TAB = 4                  # tab radius
TAB_C = (CROSS + HI) // 2  # 30: tab centre along each long half


class FourPieceJigsawPuzzleRedraw(Solo48):
    icon_id = "four-piece-jigsaw-puzzle-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/toys"
    aliases = ("jigsaw puzzle", "puzzle")
    keywords = ("four", "piece", "jigsaw", "puzzle", "pieces", "interlocking")

    def build(self) -> None:
        a, b, r = LO, HI, CORNER
        self.add_line("frame-0", (CROSS, a), (b - r, a))
        self.add_arc("frame-1", (b - r, a), (b, a + r), radius_x=r)
        self.add_line("frame-2", (b, a + r), (b, CROSS))
        self.add_line("frame-3", (b, CROSS), (b, b - r))
        self.add_arc("frame-4", (b, b - r), (b - r, b), radius_x=r)
        self.add_line("frame-5", (b - r, b), (CROSS, b))
        self.add_line("frame-6", (CROSS, b), (a + r, b))
        self.add_arc("frame-7", (a + r, b), (a, b - r), radius_x=r)
        self.add_line("frame-8", (a, b - r), (a, CROSS))
        self.add_line("frame-9", (a, CROSS), (a, a + r))
        self.add_arc("frame-10", (a, a + r), (a + r, a), radius_x=r)
        self.add_line("frame-11", (a + r, a), (CROSS, a))
        self.add_contour("frame", *[f"frame-{i}" for i in range(12)], closed=True)

        self.add_line("seam-top", (CROSS, a), (CROSS, CROSS))
        self.add_line("seam-left", (a, CROSS), (CROSS, CROSS))

        self.add_line("seam-bottom-0", (CROSS, CROSS), (CROSS, TAB_C - TAB))
        self.add_arc("seam-bottom-tab", (CROSS, TAB_C - TAB), (CROSS, TAB_C + TAB),
                     radius_x=TAB, sweep=False)
        self.add_line("seam-bottom-1", (CROSS, TAB_C + TAB), (CROSS, b))
        self.add_contour("seam-bottom", "seam-bottom-0", "seam-bottom-tab", "seam-bottom-1")

        self.add_line("seam-right-0", (CROSS, CROSS), (TAB_C - TAB, CROSS))
        self.add_arc("seam-right-tab", (TAB_C - TAB, CROSS), (TAB_C + TAB, CROSS),
                     radius_x=TAB, sweep=True)
        self.add_line("seam-right-1", (TAB_C + TAB, CROSS), (b, CROSS))
        self.add_contour("seam-right", "seam-right-0", "seam-right-tab", "seam-right-1")

        seams = ("seam-top", "seam-left", "seam-bottom", "seam-right")
        for seam in seams:
            self.relate("connect", seam, "frame")
        for i, seam in enumerate(seams):
            for other in seams[i + 1:]:
                self.relate("connect", seam, other)


if __name__ == "__main__":
    print(FourPieceJigsawPuzzleRedraw().validate_icon().describe())
