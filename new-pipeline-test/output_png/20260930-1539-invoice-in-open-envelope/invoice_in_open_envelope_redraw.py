"""invoice-in-open-envelope (redraw of the new-pipeline traced SVG).

Plan: an open envelope whose pocket holds an upright invoice sheet with two
rules, on SQUARE (the suggested keyshape, fit score 1.11), centerline box
(6,6)-(42,42); mirrored about x=24.
- pocket: one closed contour. Walls at x=6 / x=42 from the shoulders (y=23)
  down to radius-3 corners and the base at y=42; the front flap is a V of
  slope 1/2 from each shoulder to the vertex (24,32), split where the sheet
  sides land on it at (14,27) / (34,27).
- sheet: sides at x=14 / x=34 rising from the V to the top edge at y=6, with
  round-joined square corners (radius-2 arcs made the exact-8 rule gaps a
  sampled `review`; all-straight edges certify them). The sides sit exactly 8
  inside the walls.
- back flap: two 45-degree lines from each shoulder up to the sheet sides at
  (14,15) / (34,15), splitting the sides there; they show the opened flap
  behind the sheet.
- rules: two strokes x 22..26 at y=14 and y=22, 8 from the top edge, 8 from
  each other, 8 from the sides, and 8.05 from the V.
The top edge reaches y=6, the walls x=6/42 and the base y=42, so SQUARE is
filled exactly on both axes. Lucide `mail-open` informed the pocket (square
body, V flap from the shoulders); the sheet and rules follow the image.

Metric issues fixed:
- clearance e0/e1 (V vertex 5.93 above the base): the V is flatter (slope 1/2)
  and ends at y=32, 10 above the base.
- clearance e1/e3, e1/e4 (sheet sides 5.58 from the walls): the sheet is
  narrowed so its sides stand 8 inside the walls.
- clearance e2/e5, e2/e6, e3/e5, e3/e6, e4/e5, e4/e6 (rules 5.2-5.8 from the
  sheet sides and flap): the rules end 8 from each side; the back flap now
  meets the sides at y=15, well away from the rules.
- clearance e0/e6 (lower rule 7.77 from the V): the V drops lower; the rule
  end (22,22) is 8.05 from it.
- clearance e5/e6 (rules 4.24 apart): the rules are 8 apart.
- keyshape-short-axis (y 86%): the sheet top at y=6 and the base at y=42 fill
  SQUARE on y, the walls fill it on x.
- stroke-count (7, budget 6): drawn as 6 strokes (pocket, sheet, two flap
  lines, two rules); the trace's separate V path is part of the pocket.
- stroke-width (info): redrawn at stroke 4 with every gap budgeted at 8.
Trade-off: the 8-unit clearance to the sheet sides leaves the rules 4 long
(ink 8 of the sheet's 16 interior), shorter than in the image.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "57201c70-c002-40bb-8fad-0abd9f9ca4db"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1539-invoice-in-open-envelope/invoice-in-open-envelope_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
WALL = 18                  # half-width of the pocket: walls at x=6 / 42
SHOULDER, BASE, BODY_R = 23, 42, 3
V_Y = 32                   # V vertex; slope 1/2 from the shoulders
SHEET = 10                 # half-width of the sheet: sides at x=14 / 34
SHEET_TOP = 6
FLAP_Y = 15                # back flap meets the sheet sides (45 degrees)
SIDE_Y = SHOULDER + (WALL - SHEET) // 2   # sheet side lands on the V
RULE_YS, RULE_HALF = (14, 22), 2


class InvoiceInOpenEnvelopeRedraw(Solo48):
    icon_id = "invoice-in-open-envelope-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/office"
    aliases = ("invoice envelope", "bill in envelope", "open envelope with letter", "mailed invoice")
    keywords = ("invoice", "bill", "envelope", "mail", "letter", "open", "document", "payment")

    def build(self) -> None:
        lx, rx = AXIS - WALL, AXIS + WALL
        sl, sr = AXIS - SHEET, AXIS + SHEET

        self.add_line("wall-left", (lx, SHOULDER), (lx, BASE - BODY_R))
        self.add_arc("corner-bl", (lx, BASE - BODY_R), (lx + BODY_R, BASE), radius_x=BODY_R, sweep=False)
        self.add_line("base", (lx + BODY_R, BASE), (rx - BODY_R, BASE))
        self.add_arc("corner-br", (rx - BODY_R, BASE), (rx, BASE - BODY_R), radius_x=BODY_R, sweep=False)
        self.add_line("wall-right", (rx, BASE - BODY_R), (rx, SHOULDER))
        self.add_line("v-right-outer", (rx, SHOULDER), (sr, SIDE_Y))
        self.add_line("v-right-inner", (sr, SIDE_Y), (AXIS, V_Y))
        self.add_line("v-left-inner", (AXIS, V_Y), (sl, SIDE_Y))
        self.add_line("v-left-outer", (sl, SIDE_Y), (lx, SHOULDER))
        self.add_contour(
            "pocket", "wall-left", "corner-bl", "base", "corner-br", "wall-right",
            "v-right-outer", "v-right-inner", "v-left-inner", "v-left-outer", closed=True,
        )

        self.add_line("side-left-low", (sl, SIDE_Y), (sl, FLAP_Y))
        self.add_line("side-left-up", (sl, FLAP_Y), (sl, SHEET_TOP))
        self.add_line("top", (sl, SHEET_TOP), (sr, SHEET_TOP))
        self.add_line("side-right-up", (sr, SHEET_TOP), (sr, FLAP_Y))
        self.add_line("side-right-low", (sr, FLAP_Y), (sr, SIDE_Y))
        self.add_contour(
            "sheet", "side-left-low", "side-left-up", "top", "side-right-up", "side-right-low",
        )
        self.relate("connect", "sheet", "pocket")

        self.add_line("flap-left", (lx, SHOULDER), (sl, FLAP_Y))
        self.add_line("flap-right", (rx, SHOULDER), (sr, FLAP_Y))
        self.relate("connect", "flap-left", "pocket")
        self.relate("connect", "flap-left", "sheet")
        self.relate("connect", "flap-right", "pocket")
        self.relate("connect", "flap-right", "sheet")

        for index, y in enumerate(RULE_YS, start=1):
            self.add_line(f"rule-{index}", (AXIS - RULE_HALF, y), (AXIS + RULE_HALF, y))
