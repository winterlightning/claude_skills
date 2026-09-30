"""clipboard (redraw of the new-pipeline traced SVG).

Plan: a tall rounded board with a broad rounded clip centred on its top
edge, VRECT_M keyshape (centerline box (10,4)-(38,44)), mirrored about x=24.
- board: open contour, corner radius 4, walls on x=10 / x=38, bottom on
  y=44, top on y=10; the top edge stops at the clip's side walls (x=17 and
  x=31) so the clip interrupts it as in the generated image.
- clip: closed rounded rectangle x 17..31, y 4..14, corner radius 3. It
  rises 6 above the board top and hangs 4 below it (the image shows about
  3.3 above and 4.2 below at a thinner stroke); each side wall is split at
  y=10 so the board shares that endpoint and the contact is declared.
Every arc centre and endpoint is on the integer grid; nothing is copied
from the trace coordinates.

Metric issues:
- error `hole` (clip interior 2.2 wide at (19.9, 7.7)): fixed. The clip is
  10 tall on centerlines, so its interior is 10 x 6 ink-free at stroke 4
  (the 6 inscribed minimum).
- warn `keyshape-short-axis` (y filled 96%): fixed. The clip top is the
  y=4 extreme and the board bottom the y=44 extreme; the walls sit on x=10
  and x=38, so all four VRECT_M extremes are exact.
- info `stroke-width` (trace 2.55, target 4): fixed by construction at
  stroke 4; the only near pair, board corner to clip wall, is joined at the
  shared (17,10) / (31,10) endpoints.
Lucide construction used: `clipboard` (rounded board whose top edge is
interrupted by a separate rounded clip rectangle).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8a44db68-8509-4e9a-b460-4143125c86a9"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1924-clipboard-solo/clipboard-solo_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
BOARD_L, BOARD_R, BOARD_TOP, BOARD_BOTTOM, BOARD_RAD = 10, 38, 10, 44, 4
CLIP_HALF, CLIP_TOP, CLIP_BOTTOM, CLIP_RAD = 7, 4, 14, 3
CLIP_L, CLIP_R = AXIS - CLIP_HALF, AXIS + CLIP_HALF


class ClipboardSoloRedraw(Solo48):
    icon_id = "clipboard-solo-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/office"
    aliases = ("clip board", "board with clip")
    keywords = ("clipboard", "board", "clip", "paste", "notes", "checklist", "office")

    def build(self) -> None:
        l, r, t, b, k = BOARD_L, BOARD_R, BOARD_TOP, BOARD_BOTTOM, BOARD_RAD
        self.add_line("board-top-left", (CLIP_L, t), (l + k, t))
        self.add_arc("board-tl", (l + k, t), (l, t + k), radius_x=k, sweep=False)
        self.add_line("board-left", (l, t + k), (l, b - k))
        self.add_arc("board-bl", (l, b - k), (l + k, b), radius_x=k, sweep=False)
        self.add_line("board-bottom", (l + k, b), (r - k, b))
        self.add_arc("board-br", (r - k, b), (r, b - k), radius_x=k, sweep=False)
        self.add_line("board-right", (r, b - k), (r, t + k))
        self.add_arc("board-tr", (r, t + k), (r - k, t), radius_x=k, sweep=False)
        self.add_line("board-top-right", (r - k, t), (CLIP_R, t))
        self.add_contour("board", "board-top-left", "board-tl", "board-left", "board-bl",
                         "board-bottom", "board-br", "board-right", "board-tr", "board-top-right")

        cl, cr, ct, cb, q = CLIP_L, CLIP_R, CLIP_TOP, CLIP_BOTTOM, CLIP_RAD
        self.add_line("clip-top", (cl + q, ct), (cr - q, ct))
        self.add_arc("clip-tr", (cr - q, ct), (cr, ct + q), radius_x=q, sweep=True)
        self.add_line("clip-right-upper", (cr, ct + q), (cr, t))
        self.add_line("clip-right-lower", (cr, t), (cr, cb - q))
        self.add_arc("clip-br", (cr, cb - q), (cr - q, cb), radius_x=q, sweep=True)
        self.add_line("clip-bottom", (cr - q, cb), (cl + q, cb))
        self.add_arc("clip-bl", (cl + q, cb), (cl, cb - q), radius_x=q, sweep=True)
        self.add_line("clip-left-lower", (cl, cb - q), (cl, t))
        self.add_line("clip-left-upper", (cl, t), (cl, ct + q))
        self.add_arc("clip-tl", (cl, ct + q), (cl + q, ct), radius_x=q, sweep=True)
        self.add_contour("clip", "clip-top", "clip-tr", "clip-right-upper", "clip-right-lower",
                         "clip-br", "clip-bottom", "clip-bl", "clip-left-lower",
                         "clip-left-upper", "clip-tl", closed=True)
        self.relate("connect", "board", "clip")
