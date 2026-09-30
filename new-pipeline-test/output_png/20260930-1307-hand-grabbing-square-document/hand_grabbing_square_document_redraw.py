"""hand-grabbing-square-document (redraw of the new-pipeline traced SVG).

Subject: a blank square document held at its lower-right corner by a hand
rising from the lower right; the thumb lies across the front of the sheet and
the fingers wrap behind it.

Plan: SQUARE (centerline box (6,6)-(42,42)).
- document: one open contour for the sheet, (6,6)-(DOC_R,DOC_B); its right
  edge stops where the thumb's upper side crosses it and its bottom edge stops
  where the thumb's lower side crosses it, so the corner hides behind the hand.
- thumb: a 45-degree finger pointing up-left, centre line through THUMB_C,
  half-width 3 grid steps along each diagonal (8.49 between the sides), tip a
  true semicircle drawn as two quarter-circle cubics so all nodes stay integer.
- hand-front: wrist -> palm bulge -> thumb lower side -> tip -> thumb upper
  side -> short knuckle crease past the sheet edge (one contour, free end).
- hand-back: the fingers leave the sheet's right edge at BACK_Y, run
  down-right to the knuckle, turn down in one tangent cubic and fall straight
  to the right wrist corner (42,42).

Metric issues (svg_metrics) and what happened to them:
- stroke-width (info): redrawn at stroke 4 with every gap budgeted for it.
- clearance e2/e3 3.29 (back of hand vs thumb on the sheet edge): the back of
  hand now leaves the sheet 12 above the thumb (was ~4); >= 9 from the thumb
  side and tip.
- clearance e1/e2 7.73 (wrist sides): wrist opened to 9 between centerlines
  (x=33 -> x=42 at the bottom edge).
- clearance e1/e3 7.99 (palm vs thumb crease): the crease is shortened to end
  at (31,27) and the palm bulge swings clear of it (> 8).
- hole 0.45 at (33.2,24.1): the pinched sliver between the crease end and the
  back of hand is gone; the palm is open to the wrist and the only closed
  region is the sheet interior.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6818d5fa-ca7b-4205-ab33-ff7acb27ba99"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1307-hand-grabbing-square-document/hand-grabbing-square-document_raw.svg"
AUTHOR = "claude-opus-5-5"

DOC_L, DOC_T, DOC_R, DOC_B = 6, 6, 28, 30
THUMB_C = (22, 24)          # centre of the thumb-tip semicircle
HALF = 3                    # half-width in diagonal grid steps (radius 3*sqrt2)
CREASE = 3                  # crease runs this many steps past the sheet edge
BACK_Y = 12                 # where the fingers leave the sheet's right edge
KNUCKLE = (34, 16)
HEEL = (40, 24)
WRIST_L, WRIST_R = (33, 42), (42, 42)
K = 0.5523 * HALF           # quarter-circle handle, per diagonal step


class HandGrabbingSquareDocumentRedraw(Solo48):
    icon_id = "hand-grabbing-square-document-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/document"
    aliases = ("hand holding document", "hand holding paper", "holding a sheet")
    keywords = ("hand", "document", "paper", "sheet", "page", "hold", "grab", "file", "give", "receive")

    def build(self) -> None:
        cx, cy = THUMB_C
        upper0 = (cx + HALF, cy - HALF)             # thumb upper side start
        lower0 = (cx - HALF, cy + HALF)             # thumb lower side start
        tip = (cx - HALF, cy - HALF)
        # where the thumb sides cross the sheet's right and bottom edges
        right_x = (DOC_R, upper0[1] + (DOC_R - upper0[0]))
        bottom_x = (lower0[0] + (DOC_B - lower0[1]), DOC_B)
        crease_end = (right_x[0] + CREASE, right_x[1] + CREASE)

        # Sheet: bottom-right corner hidden behind the hand.
        self.add_polyline("document", right_x, (DOC_R, BACK_Y), (DOC_R, DOC_T),
                          (DOC_L, DOC_T), (DOC_L, DOC_B), bottom_x)

        # Front of hand: wrist, palm, thumb, crease.
        self.add_bezier("palm", WRIST_L, ((31, 40.5), (26, 36), (25, 33)),
                        ((24.5, 31.5), (23, 31), bottom_x))
        self.add_line("thumb-lower", bottom_x, lower0)
        self.add_bezier(
            "thumb-tip", lower0,
            ((lower0[0] - K, lower0[1] - K), (tip[0] - K, tip[1] + K), tip),
            ((tip[0] + K, tip[1] - K), (upper0[0] - K, upper0[1] - K), upper0),
        )
        self.add_line("thumb-upper", upper0, right_x)
        self.add_line("crease", right_x, crease_end)
        self.add_contour("hand-front", "palm", "thumb-lower", "thumb-tip",
                         "thumb-upper", "crease")
        self.relate("connect", "hand-front", "document")

        # Back of hand: fingers behind the sheet, knuckle, heel, wrist.
        self.add_line("back-fingers", (DOC_R, BACK_Y), KNUCKLE)
        self.add_bezier("back-knuckle", KNUCKLE,
                        ((37.6, 18.4), (39.7, 21.5), HEEL))
        self.add_line("back-wrist", HEEL, WRIST_R)
        self.add_contour("hand-back", "back-fingers", "back-knuckle", "back-wrist")
        self.relate("connect", "hand-back", "document")
