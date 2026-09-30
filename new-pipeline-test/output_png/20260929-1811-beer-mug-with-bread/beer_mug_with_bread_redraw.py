"""beer mug with bread (redraw of the new-pipeline traced SVG).

Plan: HRECT_M (centerline box (4,10)-(44,38)), as suggested. Left to right
as in the image: C handle, foamy mug, domed loaf, as three separate readable
objects. The 40-unit width is the whole budget: handle 10 + mug 10 + gap 8 +
loaf 12. Handle after Lucide `beer` (straight arms into a rounded loop); the
foam is the mug outline's own two-lobed top instead of a separate cloud
overlapping the rim, which would crowd the narrow mug.
- handle: arm (14,23)->(8,23), radius-4 bend to the grip x=4 (the x=4
  extreme), radius-4 bend and arm back to (14,33). 10x10 on centerlines.
- mug: one closed contour. Walls x=14 and x=24 on y=38 (radius-2 corners);
  foam top = two mirrored cubic lobes from the walls (y=13) to a centre cusp
  (19,13), apexes on the y=10 extreme.
- rim line: y=RIM_Y (23) across the mug, splitting foam from beer; it shares
  its left node with the handle's top arm.
- loaf: one closed contour. Walls x=32 and x=44 (the x=44 extreme) on y=38
  with radius-2 corners, and an elliptical dome (rx 6, ry 5) with its crown
  at (38,28).
Tried and rejected: mug 12 + loaf 10 (the 10x10 loaf reads as a bun or a
tombstone); handle 8 + mug 12 + loaf 12 (passes the validator but the 4-ink
handle opening fills in at 48 px, the metrics' hole issue); loaf in front of
the mug sharing a junction (frees 4 units, but the merged silhouette reads
as a boot).
Metric issues:
- stroke-width (trace 2.63): redrawn at stroke 4 on the integer grid.
- keyshape-short-axis (y filled 84%): fixed; foam apexes on y=10, both bases
  on y=38, handle grip on x=4, loaf wall on x=44.
- clearance e0-e1 (foam cloud vs mug/handle 0.96): fixed; the foam is the
  mug contour's own top, so there is no separate foam part to clear.
- clearance e1-e2 (mug vs loaf 2.66): fixed; mug wall x=24 is 8 from the
  loaf wall x=32.
- hole (16.5,15.6) (foam bubble 2.8): fixed; the foam band between the
  cusp (y=13) and the rim (y=23) holds a 6-ink circle.
- hole (7.1,23.1) (handle 2.2): fixed; the handle loop is 10x10 on
  centerlines, a 6-ink opening.
- hole (38.2,31.4) (loaf 4.6): fixed; the loaf is 12 wide and 10 tall on
  centerlines, a 6-ink opening. The loaf's diagonal score is dropped: any
  mark inside a 10-tall loaf is under 8 from the base and would split the
  hole.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f7b3cdc5-a4f3-4160-a8d1-71f476dc0fda"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1811-beer-mug-with-bread/beer-mug-with-bread_raw.svg"
AUTHOR = "claude-opus-5-5"

BASE_Y = 38
CORNER_R = 2

HANDLE_X = 4
HANDLE_R = 4

MUG_L, MUG_R = 14, 24
MUG_MID = (MUG_L + MUG_R) // 2
FOAM_TOP = 10
LOBE_H = 3
CUSP_Y = FOAM_TOP + LOBE_H
LOBE_PULL = CUSP_Y - LOBE_H * 4 / 3  # cubic handles that put the lobe apex on FOAM_TOP
RIM_Y = CUSP_Y + 10

HANDLE_TOP = RIM_Y
HANDLE_BOTTOM = HANDLE_TOP + 10

LOAF_L, LOAF_R = 32, 44
LOAF_MID = (LOAF_L + LOAF_R) // 2
LOAF_RX = (LOAF_R - LOAF_L) // 2
LOAF_RY = 5
LOAF_SHOULDER_Y = 33


class BeerMugWithBreadRedraw(Solo48):
    icon_id = "beer-mug-with-bread-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/drink"
    aliases = ("beer and bread", "pub food", "beer mug and loaf")
    keywords = ("beer", "mug", "bread", "loaf", "pub", "bar", "food", "drink", "foam")

    def build(self) -> None:
        self._mug()
        self._handle()
        self._loaf()

    def _mug(self) -> None:
        l, r, m = MUG_L, MUG_R, MUG_MID
        self.add_line("mug-wall-l-up", (l, RIM_Y), (l, CUSP_Y))
        self.add_bezier("foam-lobe-l", (l, CUSP_Y), ((l, LOBE_PULL), (m, LOBE_PULL), (m, CUSP_Y)))
        self.add_bezier("foam-lobe-r", (m, CUSP_Y), ((m, LOBE_PULL), (r, LOBE_PULL), (r, CUSP_Y)))
        self.add_line("mug-wall-r-up", (r, CUSP_Y), (r, RIM_Y))
        self.add_line("mug-wall-r", (r, RIM_Y), (r, BASE_Y - CORNER_R))
        self.add_arc("mug-corner-r", (r, BASE_Y - CORNER_R), (r - CORNER_R, BASE_Y),
                     radius_x=CORNER_R, sweep=True)
        self.add_line("mug-base", (r - CORNER_R, BASE_Y), (l + CORNER_R, BASE_Y))
        self.add_arc("mug-corner-l", (l + CORNER_R, BASE_Y), (l, BASE_Y - CORNER_R),
                     radius_x=CORNER_R, sweep=True)
        self.add_line("mug-wall-l-low", (l, BASE_Y - CORNER_R), (l, HANDLE_BOTTOM))
        self.add_line("mug-wall-l-mid", (l, HANDLE_BOTTOM), (l, RIM_Y))
        self.add_contour("mug", "mug-wall-l-up", "foam-lobe-l", "foam-lobe-r",
                         "mug-wall-r-up", "mug-wall-r", "mug-corner-r",
                         "mug-base", "mug-corner-l", "mug-wall-l-low", "mug-wall-l-mid",
                         closed=True)
        self.add_line("rim-line", (l, RIM_Y), (r, RIM_Y))
        self.relate("connect", "rim-line", "mug")

    def _handle(self) -> None:
        x0, x2 = MUG_L, HANDLE_X
        x1 = x2 + HANDLE_R
        self.add_line("handle-top", (x0, HANDLE_TOP), (x1, HANDLE_TOP))
        self.add_arc("handle-bend-t", (x1, HANDLE_TOP), (x2, HANDLE_TOP + HANDLE_R),
                     radius_x=HANDLE_R, sweep=False)
        self.add_line("handle-grip", (x2, HANDLE_TOP + HANDLE_R), (x2, HANDLE_BOTTOM - HANDLE_R))
        self.add_arc("handle-bend-b", (x2, HANDLE_BOTTOM - HANDLE_R), (x1, HANDLE_BOTTOM),
                     radius_x=HANDLE_R, sweep=False)
        self.add_line("handle-bottom", (x1, HANDLE_BOTTOM), (x0, HANDLE_BOTTOM))
        self.add_contour("handle", "handle-top", "handle-bend-t", "handle-grip",
                         "handle-bend-b", "handle-bottom")
        self.relate("connect", "handle", "mug")
        self.relate("connect", "handle", "rim-line")

    def _loaf(self) -> None:
        l, r, m = LOAF_L, LOAF_R, LOAF_MID
        crown = LOAF_SHOULDER_Y - LOAF_RY
        self.add_line("loaf-wall-l", (l, BASE_Y - CORNER_R), (l, LOAF_SHOULDER_Y))
        self.add_arc("loaf-dome-l", (l, LOAF_SHOULDER_Y), (m, crown),
                     radius_x=LOAF_RX, radius_y=LOAF_RY, sweep=True)
        self.add_arc("loaf-dome-r", (m, crown), (r, LOAF_SHOULDER_Y),
                     radius_x=LOAF_RX, radius_y=LOAF_RY, sweep=True)
        self.add_line("loaf-wall-r", (r, LOAF_SHOULDER_Y), (r, BASE_Y - CORNER_R))
        self.add_arc("loaf-corner-r", (r, BASE_Y - CORNER_R), (r - CORNER_R, BASE_Y),
                     radius_x=CORNER_R, sweep=True)
        self.add_line("loaf-base", (r - CORNER_R, BASE_Y), (l + CORNER_R, BASE_Y))
        self.add_arc("loaf-corner-l", (l + CORNER_R, BASE_Y), (l, BASE_Y - CORNER_R),
                     radius_x=CORNER_R, sweep=True)
        self.add_contour("loaf", "loaf-wall-l", "loaf-dome-l", "loaf-dome-r", "loaf-wall-r",
                         "loaf-corner-r", "loaf-base", "loaf-corner-l", closed=True)
