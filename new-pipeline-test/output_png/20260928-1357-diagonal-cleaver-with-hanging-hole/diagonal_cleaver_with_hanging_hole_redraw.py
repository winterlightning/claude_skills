"""diagonal-cleaver-with-hanging-hole (redraw of the new-pipeline traced SVG).

Plan: cleaver on VRECT_M (centerline box (10,4)-(38,44)) built on the
45-degree diagonal so every straight edge is pixel-clean at 48 px.
- blade: spine S->B along (1,-1), heel B->C and front D->F along (1,1),
  cutting edge C->D parallel to the spine; 25.5 long x 14.1 deep (1.8:1).
- rounded top-front corner: the virtual corner A=(8,34) is replaced by two
  cubics F->V->S (tangent length 4). V=(10,34) is the leftmost point with a
  vertical tangent, so the keyshape fit stays exact.
- handle: one stroke continuing the spine from B, so the blade hangs below
  the handle like a real cleaver (a centred handle read as a USB stick).
The reference's hanging hole and outlined grip are dropped for a clean
48 px silhouette. No Lucide cleaver exists; the 45-degree construction and
single-stroke handle follow Lucide's diagonal tools (axe, hammer, knife).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1357-diagonal-cleaver-with-hanging-hole/"
    "diagonal-cleaver-with-hanging-hole_raw.svg"
)
AUTHOR = "claude-opus-5-5"

S = (12, 30)           # spine start, end of the rounded corner (A + 4*(1,-1))
B = (26, 16)           # heel-spine corner (A + 18*(1,-1)); handle root
C = (36, 26)           # heel-edge corner  (B + 10*(1,1))
D = (18, 44)           # front-edge corner (A + 10*(1,1))
F = (12, 38)           # front edge top, start of the rounded corner (A + 4*(1,1))
V = (10, 34)           # leftmost point of the corner, vertical tangent
HANDLE_END = (38, 4)   # B + 12*(1,-1)
K = 1.06               # cubic handle per axis on the 45-degree ends
KV = 1.5               # cubic handle at the vertical tangent


class DiagonalCleaverWithHangingHoleRedraw(Solo48):
    icon_id = "diagonal-cleaver-with-hanging-hole-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/kitchen"
    aliases = ("meat cleaver", "butcher knife", "chopper")
    keywords = ("cleaver", "butcher", "knife", "chop", "meat", "kitchen", "cooking")

    def build(self) -> None:
        self.add_line("spine", S, B)
        self.add_line("heel", B, C)
        self.add_line("edge", C, D)
        self.add_line("front", D, F)
        self.add_bezier(
            "corner", F,
            ((F[0] - K, F[1] - K), (V[0], V[1] + KV), V),
            ((V[0], V[1] - KV), (S[0] - K, S[1] + K), S),
        )
        self.add_contour("blade", "spine", "heel", "edge", "front", "corner", closed=True)

        self.add_line("handle", B, HANDLE_END)
        self.relate("connect", "handle", "blade")
