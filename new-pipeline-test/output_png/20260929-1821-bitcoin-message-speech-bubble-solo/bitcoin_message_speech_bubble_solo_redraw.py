"""bitcoin-message-speech-bubble-solo (redraw of the new-pipeline traced SVG).

Plan: a rounded speech bubble with a Lucide message-square corner tail at the
lower left, holding an upright serifed Bitcoin B.
- keyshape VRECT_L (centerline box (8,4)-(40,44)) instead of the suggested
  SQUARE. A B with two counters that pass the 6-unit hole rule is 20 tall on
  centerlines, and it needs 8 to each bubble wall, so the bubble interior must
  be 36 tall before the tail. SQUARE gives 36 in total; VRECT_L gives 40, which
  leaves the 4-unit tail.
- bubble: walls x=8 / x=40, top y=4, bottom edge y=40, corner radius 6.
  The lower-left corner is replaced by the tail: the left wall runs straight
  down to the tip (8,44), and a 1:2 diagonal climbs back to the bottom edge
  at (16,40). The straight walls are standalone lines joined to the corner
  arcs by connect, because an exact 8 gap only certifies straight-vs-straight.
- B: spine x=19, top edge y=12, waist y=22, bottom edge y=32 (exactly 8 from
  the top wall and the bottom edge). Both counters are 10 tall with r5
  bowls. The lower bowl sits one unit further right (x=31) than the upper
  (x=30), as in the generated image. Serifs run left from the spine to x=16,
  8 from the left wall. Edges+serifs, spine, waist and the bowl pair are
  separate line/arc parts sharing exact nodes, all related with connect.
Extremes: x 8 (left wall, tail tip) / 40 (right wall), y 4 (top) / 44 (tip).

Metric issues fixed:
- stroke-width: redrawn at stroke 4; every gap re-budgeted for it.
- clearance e0/e1, e0/e4, e0/e6, e0/e7 (bars 4.7-5 from the bubble): bars
  removed (see below); the B's top and bottom edges now sit exactly 8 from
  the bubble.
- clearance e1/e3, e1/e4, e1/e5, e3/e4, e5/e7, e6/e7, e2/e5, e2/e7 (bars,
  spine and bowls 3-7.9 apart): each counter is now 10 tall and 11-12 wide.
  There are no bars.
- hole at (23.2,17.9) 2.6 and at (23.4,24.8) 3.2: both counters are now
  6 inscribed.
- loose-join e4/e5, e5/e6: spine, edges, waist and bowls share exact
  integer nodes and every contact is related with connect.
Not fixed:
- stroke-count (8, budget 6): as painted strokes the icon reads as 2 marks
  (bubble outline, B), but the SVG has 11 paths. The bubble walls and B
  edges have to be standalone lines, because the exact 8-unit gaps return
  `review` inside contours that contain arcs. The paths share nodes and
  render as two continuous marks.
Not kept:
- the two currency bars. There is no vertical room: bars need about 4 more
  units above and below the B plus 8 to the wall, which makes 44 of interior
  against 36 available. Bars joined to the bubble wall make 8x8 pockets
  (4 inscribed, hole fail). The serifed B in the bubble carries the sign.
Lucide: message-square (corner tail: the left wall runs to the tip, then a
short diagonal back to the bottom edge) and bitcoin (B built from a stem and
two stacked bowls).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "692b5811-84ae-4db0-8d66-219feaafec3e"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1821-bitcoin-message-speech-bubble-solo/bitcoin-message-speech-bubble-solo_raw.svg"
AUTHOR = "claude-opus-5-5"

# bubble
L, R, T, B = 8, 40, 4, 40      # walls, top, bottom edge
CR = 6                         # corner radius
TIP = (L, 44)                  # tail tip on the left wall line
TAIL_JOIN = (16, B)            # diagonal meets the bottom edge (1:2 slope)

# Bitcoin B
SPINE = 19
SERIF = 16
TOP, MID, BOT = 12, 22, 32
R_BOWL = (MID - TOP) // 2      # 5, both counters
UP_X, LOW_X = 25, 26           # bowl centres; lower bowl one unit wider


class BitcoinMessageSpeechBubbleSoloRedraw(Solo48):
    icon_id = "bitcoin-message-speech-bubble-solo-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "communication"
    aliases = ("bitcoin message", "crypto chat", "bitcoin chat")
    keywords = ("bitcoin", "btc", "crypto", "message", "chat", "speech bubble",
                "comment", "payment request")

    def build(self) -> None:
        # speech bubble. The top wall, bottom edge, tail and left wall are
        # standalone lines so their exact 8-unit gaps to the B's flat edges and
        # serif ends certify; the corner arcs join them at shared nodes.
        self.add_line("top", (L + CR, T), (R - CR, T))
        self.add_arc("corner-tr", (R - CR, T), (R, T + CR), radius_x=CR, sweep=True)
        self.add_line("right", (R, T + CR), (R, B - CR))
        self.add_arc("corner-br", (R, B - CR), (R - CR, B), radius_x=CR, sweep=True)
        self.add_contour("bubble-right", "corner-tr", "right", "corner-br")
        self.add_line("bottom", (R - CR, B), TAIL_JOIN)
        self.add_line("tail", TAIL_JOIN, TIP)
        self.add_line("left", TIP, (L, T + CR))
        self.add_arc("corner-tl", (L, T + CR), (L + CR, T), radius_x=CR, sweep=True)
        chain = ("top", "bubble-right", "bottom", "tail", "left", "corner-tl", "top")
        for a, b in zip(chain, chain[1:]):
            self.relate("connect", a, b)

        # Bitcoin B. The flat top and bottom edges (with their serifs) are
        # line-only contours so their exact 8-unit gaps to the bubble walls
        # certify; the two bowls form one arc contour meeting at the waist.
        self.add_line("serif-top", (SERIF, TOP), (SPINE, TOP))
        self.add_line("top-edge", (SPINE, TOP), (UP_X, TOP))
        self.add_contour("b-top", "serif-top", "top-edge")
        self.add_line("bottom-edge", (LOW_X, BOT), (SPINE, BOT))
        self.add_line("serif-bot", (SPINE, BOT), (SERIF, BOT))
        self.add_contour("b-bottom", "bottom-edge", "serif-bot")
        self.add_line("spine-top", (SPINE, TOP), (SPINE, MID))
        self.add_line("spine-bot", (SPINE, MID), (SPINE, BOT))
        self.add_contour("b-spine", "spine-top", "spine-bot")
        self.add_line("waist", (SPINE, MID), (UP_X, MID))
        self.add_arc("bowl-up", (UP_X, TOP), (UP_X, MID), radius_x=R_BOWL, sweep=True)
        self.add_line("waist-run", (UP_X, MID), (LOW_X, MID))
        self.add_arc("bowl-low", (LOW_X, MID), (LOW_X, BOT), radius_x=R_BOWL, sweep=True)
        self.add_contour("b-bowls", "bowl-up", "waist-run", "bowl-low")
        for part in ("b-top", "b-bottom", "waist"):
            self.relate("connect", part, "b-spine")
            self.relate("connect", part, "b-bowls")
