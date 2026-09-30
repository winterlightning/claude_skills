"""heart-message-22-solo (redraw of the new-pipeline traced SVG).

Plan: a rounded rectangular speech bubble with a short tail below its
lower-left corner, and one hollow heart centred inside. On the suggested
SQUARE (centerline box (6,6)-(42,42)); the tail tip supplies the y=42
extreme, so the body keeps the trace's landscape proportion instead of
being stretched 1.15 on y.
- bubble: one closed contour. Body walls x 6 / 42, top y 6, bottom y 37,
  r6 corners (integer centres). The bottom-left arc lands on (12,37),
  where the tail drops straight down to its tip (12,42) and runs back up
  at 45 degrees to the bottom edge at (17,37), as in the generated image.
- heart: one closed contour on the axis x=24. Tip (24,27), 45-degree
  lines up to (18,21)/(30,21) and one mirrored cubic lobe on each side,
  tangent to its line, closing in the notch (24,16). Lobe tops at y~14.1
  and sides at x~16.1/31.9, so the heart is 15.8 x 13.9 and keeps more
  than 8 from every bubble wall (tip to bottom edge 9, lobes to top edge
  ~8.1, sides to walls ~10.1). The tip sits 9, not 8, above the bottom
  edge: exactly 8 came back `review`.

Metric issues fixed:
- clearance e0/e1 (4.04, error): the heart tip sat 4 above the bubble's
  bottom edge. The body is 31 tall and the heart ~14 tall, so the tip
  keeps 9 from the bottom edge and the lobes ~8.1 from the top.
- keyshape-short-axis (warn, y filled 87%): the body stays 31 tall and the
  tail reaches y=42, so all four SQUARE extremes are hit exactly
  (x 6 / 42, y 6 / 42) without stretching the bubble.
- stroke-width (info): redrawn at stroke 4 with every gap sized for it.

Lucide: message-square (rounded body with the tail at the lower left)
and heart (tangent lobes over a 45-degree point) informed the construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2a3f04f0-a404-41db-90b7-a6ee5813413b"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1544-heart-message-22-solo/heart-message-22-solo_raw.svg"
AUTHOR = "claude-opus-5-5"

L, T, R, B = 6, 6, 42, 37     # bubble body walls
CR = 6                        # corner radius
TX, TY = L + CR, 42           # tail: drops from the bottom-left arc end to (TX, TY)
CX = 24                       # heart axis
TIP, SHOULDER, NOTCH = 28, 22, 16
HW = 6                        # half width at the shoulder (45-degree lines)


class HeartMessage22SoloRedraw(Solo48):
    icon_id = "heart-message-22-solo-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ("heart speech bubble", "love message")
    keywords = ("heart", "message", "speech bubble", "chat", "love",
                "like", "comment", "favorite")

    def build(self) -> None:
        # Bubble, clockwise from the top-left corner.
        self.add_line("top", (L + CR, T), (R - CR, T))
        self.add_arc("tr", (R - CR, T), (R, T + CR), radius_x=CR, sweep=True)
        self.add_line("right", (R, T + CR), (R, B - CR))
        self.add_arc("br", (R, B - CR), (R - CR, B), radius_x=CR, sweep=True)
        self.add_line("bottom", (R - CR, B), (TX + (TY - B), B))
        self.add_line("tail-back", (TX + (TY - B), B), (TX, TY))
        self.add_line("tail-front", (TX, TY), (TX, B))
        self.add_arc("bl", (TX, B), (L, B - CR), radius_x=CR, sweep=True)
        self.add_line("left", (L, B - CR), (L, T + CR))
        self.add_arc("tl", (L, T + CR), (L + CR, T), radius_x=CR, sweep=True)
        self.add_contour("bubble", "top", "tr", "right", "br", "bottom",
                         "tail-back", "tail-front", "bl", "left", "tl",
                         closed=True)

        # Heart, mirrored about x=CX: tip -> left shoulder -> lobe -> notch
        # -> lobe -> right shoulder -> tip.
        ls, rs = (CX - HW, SHOULDER), (CX + HW, SHOULDER)
        self.add_line("heart-left", (CX, TIP), ls)
        self.add_bezier("lobe-left", ls,
                        ((CX - 11, SHOULDER - 5), (CX - 5, NOTCH - 5),
                         (CX, NOTCH)))
        self.add_bezier("lobe-right", (CX, NOTCH),
                        ((CX + 5, NOTCH - 5), (CX + 11, SHOULDER - 5), rs))
        self.add_line("heart-right", rs, (CX, TIP))
        self.add_contour("heart", "heart-left", "lobe-left", "lobe-right",
                         "heart-right", closed=True)
